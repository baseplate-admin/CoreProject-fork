from typing import Any
from ninja import Router
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from .models import Client, AuthorizationCode, Token
from django.utils import timezone
from .schemas import (
    AuthorizationRequest,
    TokenRequest,
    TokenResponse,
    UserInfoResponse,
    DiscoveryResponse,
)
from .auth import TokenAuth
from .utils import (
    encode_jwt,
    create_id_token,
    generate_token_value,
    compute_at_hash,
    verify_pkce,
)
from ninja.errors import HttpError
import datetime
from .helper import validate_redirect_uri, authenticate_client
from django.contrib.auth import get_user_model

User = get_user_model()
router = Router()


@router.get("/authorize", url_name="authorize")
def authorization_endpoint(request, params: AuthorizationRequest):
    client = get_object_or_404(Client, client_id=params.client_id)

    # Validate redirect URI
    if not validate_redirect_uri(client, params.redirect_uri):
        return redirect(
            f"{params.redirect_uri}?error=invalid_request&error_description=Invalid+redirect_uri"
        )

    # Require PKCE for public clients
    if client.client_type == "public" and not client.require_pkce:
        return redirect(
            f"{params.redirect_uri}?error=invalid_request&error_description=PKCE+required"
        )

    # Check if user is authenticated
    if not request.user.is_authenticated:
        # Store authorization params in session
        request.session["oidc"] = {
            "params": params.dict(),
            "next": reverse("oidc_authorize"),
        }
        return redirect(f"{settings.LOGIN_URL}?next={reverse('oidc_authorize')}")

    # Create authorization code

    code = AuthorizationCode.objects.create(
        user=request.user,
        client=client,
        code=generate_token_value(),
        redirect_uri=params.redirect_uri,
        scope=params.scope,
        nonce=params.nonce,
        code_challenge=params.code_challenge,
        code_challenge_method=params.code_challenge_method,
        expires_at=timezone.now() + settings.CLIENT_EXPIRERY_TIME,
    )

    return redirect(f"{params.redirect_uri}?code={code.code}&state={params.state}")


@router.post("/token", response=TokenResponse, url_name="token")
def token_endpoint(request, payload: TokenRequest):
    def handle_authorization_code_grant(payload: TokenRequest) -> dict[str, Any]:
        client = authenticate_client(payload.client_id, payload.client_secret)
        if not client:
            raise HttpError(401, "Invalid client credentials")

        try:
            code_obj = AuthorizationCode.objects.get(code=payload.code, client=client)
        except AuthorizationCode.DoesNotExist:
            raise HttpError(400, "Invalid grant")

        if not code_obj.is_valid():
            code_obj.used_at = timezone.now()
            code_obj.save()
            raise HttpError(400, "Code expired or already used")

        if code_obj.redirect_uri != payload.redirect_uri:
            raise HttpError(400, "Invalid redirect_uri")

        if code_obj.code_challenge:
            if not payload.code_verifier:
                raise HttpError(400, "code_verifier required")
            if not verify_pkce(
                payload.code_verifier,
                code_obj.code_challenge,
                code_obj.code_challenge_method,
            ):
                raise HttpError(400, "Invalid code_verifier")

        # Generate tokens
        access_token_value = generate_token_value()

        # Encode JWT tokens
        id_token = encode_jwt(
            create_id_token(
                code_obj.user,
                client,
                code_obj.scope,
                code_obj.nonce,
                code_obj.user.last_login,
                access_token_hash=compute_at_hash(access_token_value),
            ),
            settings.OIDC_PRIVATE_KEY,
        )

        refresh_token_value = (
            generate_token_value()
            if "refresh_token" in client.allowed_grant_types
            else None
        )

        # Create token record
        token = Token.objects.create(
            user=code_obj.user,
            client=client,
            access_token=access_token_value,
            refresh_token=refresh_token_value,
            scope=code_obj.scope,
            expires_at=timezone.now() + datetime.timedelta(minutes=60),
        )

        # Revoke previous tokens
        Token.objects.filter(
            user=code_obj.user, client=client, revoked_at__isnull=True
        ).exclude(pk=token.pk).update(revoked_at=timezone.now())

        # Mark code as used
        code_obj.used_at = timezone.now()
        code_obj.save()

        return {
            "access_token": access_token_value,
            "token_type": "Bearer",
            "expires_in": 3600,
            "id_token": id_token,
            "refresh_token": refresh_token_value,
            "scope": " ".join(code_obj.scope),
        }

    def handle_refresh_token_grant(payload: TokenRequest) -> dict[str, Any]:
        client = authenticate_client(payload.client_id, payload.client_secret)
        if not client:
            raise HttpError(401, "Invalid client credentials")

        try:
            old_token = Token.objects.get(
                refresh_token=payload.refresh_token, client=client
            )
        except Token.DoesNotExist:
            raise HttpError(400, "Invalid refresh token")

        if not old_token.is_valid():
            raise HttpError(400, "Refresh token expired or revoked")

        # Generate new tokens
        access_token_value = generate_token_value()
        new_refresh_token = generate_token_value()

        # Encode JWT tokens
        id_token = encode_jwt(
            create_id_token(
                old_token.user,
                client,
                old_token.scope,
                None,
                old_token.user.last_login,
                access_token_hash=compute_at_hash(access_token_value),
            ),
            settings.OIDC_PRIVATE_KEY,
        )

        # Create new token record
        new_token = Token.objects.create(
            user=old_token.user,
            client=client,
            access_token=access_token_value,
            refresh_token=new_refresh_token,
            scope=old_token.scope,
            expires_at=timezone.now() + datetime.timedelta(minutes=60),
        )

        # Revoke previous tokens
        Token.objects.filter(
            user=old_token.user, client=client, revoked_at__isnull=True
        ).exclude(pk=new_token.pk).update(revoked_at=timezone.now())

        old_token.revoked_at = timezone.now()
        old_token.save()

        return {
            "access_token": access_token_value,
            "token_type": "Bearer",
            "expires_in": 3600,
            "id_token": id_token,
            "refresh_token": new_refresh_token,
            "scope": " ".join(old_token.scope),
        }

    if payload.grant_type == "authorization_code":
        return handle_authorization_code_grant(payload)
    elif payload.grant_type == "refresh_token":
        return handle_refresh_token_grant(payload)
    else:
        raise HttpError(400, "Unsupported grant type")


@router.get(
    "/userinfo", response=UserInfoResponse, auth=TokenAuth(), url_name="userinfo"
)
def userinfo_endpoint(request) -> dict[str, Any]:
    user = request.auth
    return {
        "sub": str(user.id),
        "name": user.get_full_name(),
        "given_name": user.first_name,
        "family_name": user.last_name,
        "preferred_username": user.username,
        "email": user.email,
        "email_verified": False,
    }


@router.get(
    "/.well-known/openid-configuration",
    response=DiscoveryResponse,
    url_name="oidc-config",
)
def discovery_endpoint(request) -> dict[str, Any]:
    base_url = settings.OIDC_ISSUER
    return {
        "issuer": base_url,
        "authorization_endpoint": f"{base_url}/oidc/authorize/",
        "token_endpoint": f"{base_url}/oidc/token/",
        "userinfo_endpoint": f"{base_url}/oidc/userinfo/",
        "jwks_uri": f"{base_url}/oidc/jwks/",
        "scopes_supported": ["openid", "profile", "email", "offline_access"],
        "response_types_supported": ["code"],
        "token_endpoint_auth_methods_supported": [
            "client_secret_basic",
            "client_secret_post",
            "none",
        ],
        "id_token_signing_alg_values_supported": ["RS256"],
    }


@router.get("/jwks", url_name="jwks")
def jwks_endpoint(request) -> dict[str, Any]:
    return {"keys": [settings.OIDC_JWK]}
