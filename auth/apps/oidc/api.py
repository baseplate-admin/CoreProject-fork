from ninja import Router
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import login
from apps.users.models import CustomUser
from .models import Client, AuthorizationCode, Token
from django.utils import timezone
from .schemas import (
    AuthorizationRequest,
    TokenRequest,
    TokenResponse,
    UserInfoResponse,
    DiscoveryResponse,
)
from .utils import (
    encode_jwt,
    create_id_token,
    create_access_token_payload,
    create_refresh_token_payload,
    generate_token_value,
    compute_at_hash,
    verify_pkce,
)
import datetime
from ninja.errors import HttpError
from ninja.security import HttpBearer

router = Router()


def validate_redirect_uri(client, redirect_uri):
    return redirect_uri in client.redirect_uris.split(",")


def authenticate_client(client_id, client_secret=None):
    try:
        client = Client.objects.get(client_id=client_id)

        # For public clients, skip secret validation
        if client.client_type == "confidential" and not client_secret:
            return None

        # For confidential clients, validate secret if provided
        if (
            client.client_type == "confidential"
            and client_secret != client.client_secret
        ):
            return None

        return client
    except Client.DoesNotExist:
        return None


class TokenAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            # Lookup token in database
            token_obj = Token.objects.get(access_token=token)

            # Check expiration
            if token_obj.is_valid():
                return token_obj.user
        except Token.DoesNotExist:
            pass
        return None


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
        expires_at=timezone.now() + datetime.timedelta(minutes=10),
    )

    return redirect(f"{params.redirect_uri}?code={code.code}&state={params.state}")
