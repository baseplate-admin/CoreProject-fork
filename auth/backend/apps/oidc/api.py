from ninja import Router
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import login
from apps.users.models import CustomUser
from .models import Client, AuthorizationCode
from django.utils import timezone
from .schemas import (
    AuthorizationRequest,
    TokenRequest,
    TokenResponse,
    UserInfoResponse,
    DiscoveryResponse,
)
from django.conf import settings
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
from .helper import validate_redirect_uri, authenticate_client


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
