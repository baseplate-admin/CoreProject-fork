import jwt
import datetime
import hashlib
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from django.conf import settings
from django.utils import timezone
import secrets


def generate_rsa_key():
    return rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )


def get_jwk(private_key):
    public_key = private_key.public_key()
    public_numbers = public_key.public_numbers()
    return {
        "kty": "RSA",
        "kid": "default",
        "alg": "RS256",
        "use": "sig",
        "n": base64.urlsafe_b64encode(public_numbers.n.to_bytes(256, "big"))
        .decode("utf-8")
        .rstrip("="),
        "e": base64.urlsafe_b64encode(public_numbers.e.to_bytes(3, "big"))
        .decode("utf-8")
        .rstrip("="),
    }


def create_id_token(user, client, scope, nonce, auth_time, access_token_hash=None):
    id_token = {
        "iss": settings.OIDC_ISSUER,
        "sub": str(user.sub),
        "aud": str(client.client_id),
        "exp": (timezone.now() + datetime.timedelta(minutes=10)).timestamp(),
        "iat": timezone.now().timestamp(),
        "auth_time": auth_time.timestamp(),
        "name": user.get_full_name(),
        "email": user.email,
        "preferred_username": user.username,
        "nonce": nonce,
    }

    if "profile" in scope:
        id_token.update(
            {
                "given_name": user.first_name,
                "family_name": user.last_name,
            }
        )

    if access_token_hash:
        id_token["at_hash"] = access_token_hash

    return id_token


def create_refresh_token_payload(user, client, scope):
    return {
        "iss": settings.OIDC_ISSUER,
        "sub": str(user.sub),
        "aud": str(client.client_id),
        "exp": (timezone.now() + datetime.timedelta(days=30)).timestamp(),
        "iat": timezone.now().timestamp(),
        "scope": " ".join(scope),
        "client_id": str(client.client_id),
    }


def encode_jwt(payload, private_key):
    return jwt.encode(
        payload,
        private_key,
        algorithm="RS256",
        headers={"kid": "default", "typ": "JWT"},
    )


def generate_token_value():
    return secrets.token_urlsafe(64)


def compute_at_hash(access_token):
    digest = hashlib.sha256(access_token.encode()).digest()
    half = digest[: len(digest) // 2]
    return base64.urlsafe_b64encode(half).decode("utf-8").rstrip("=")


def verify_pkce(code_verifier, code_challenge, method):
    if method == "S256":
        verifier = (
            base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode()).digest())
            .decode()
            .rstrip("=")
        )
        return verifier == code_challenge
    elif method == "plain":
        return code_verifier == code_challenge
    return False
