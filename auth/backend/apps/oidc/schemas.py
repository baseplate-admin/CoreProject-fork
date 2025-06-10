from ninja import Schema
from typing import List, Optional


class AuthorizationRequest(Schema):
    response_type: str = "code"
    client_id: str
    redirect_uri: str
    scope: str
    state: str
    nonce: str
    code_challenge: Optional[str] = None
    code_challenge_method: Optional[str] = None


class TokenRequest(Schema):
    grant_type: str
    code: Optional[str] = None
    redirect_uri: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    refresh_token: Optional[str] = None
    code_verifier: Optional[str] = None


class TokenResponse(Schema):
    access_token: str
    token_type: str = "Bearer"
    expires_in: int
    id_token: str
    refresh_token: Optional[str] = None
    scope: str


class UserInfoResponse(Schema):
    sub: str
    name: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    preferred_username: Optional[str] = None
    email: Optional[str] = None
    email_verified: bool = False


class DiscoveryResponse(Schema):
    issuer: str
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: str
    jwks_uri: str
    scopes_supported: List[str]
    response_types_supported: List[str]
    token_endpoint_auth_methods_supported: List[str]
    id_token_signing_alg_values_supported: List[str]
