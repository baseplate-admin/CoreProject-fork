import requests
import secrets
import hashlib
import base64
import json
import logging
import time
from urllib.parse import urlencode, parse_qs, urlparse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("OIDCTester")


class OIDCTester:
    def __init__(
        self,
        client_id: str,
        client_secret: str = None,
        redirect_uri: str = "http://localhost:8000/callback",
        scope: str = "openid",
        discovery_url: str = None,
        authorization_endpoint: str = None,
        token_endpoint: str = None,
        userinfo_endpoint: str = None,
        issuer: str = None,
        use_pkce: bool = True,
        nonce_length: int = 16,
    ):
        """
        Initialize OIDC tester with configuration

        :param client_id: OAuth client ID
        :param client_secret: Client secret (for confidential clients)
        :param redirect_uri: Redirect URI registered with OIDC provider
        :param scope: Scopes to request (space-separated)
        :param discovery_url: OIDC discovery document URL
        :param authorization_endpoint: Authorization endpoint URL
        :param token_endpoint: Token endpoint URL
        :param userinfo_endpoint: Userinfo endpoint URL
        :param issuer: Expected token issuer
        :param use_pkce: Enable PKCE (recommended)
        :param nonce_length: Length of nonce value in bytes
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.use_pkce = use_pkce
        self.state = secrets.token_urlsafe(16)
        self.code_verifier = self._generate_code_verifier() if use_pkce else None
        self.nonce = secrets.token_urlsafe(nonce_length)
        self.tokens = {}
        self.issuer = issuer

        # Discover endpoints if discovery URL provided
        if discovery_url:
            self._discover_endpoints(discovery_url)
        else:
            self.authorization_endpoint = authorization_endpoint
            self.token_endpoint = token_endpoint
            self.userinfo_endpoint = userinfo_endpoint

    def _discover_endpoints(self, discovery_url: str):
        """Fetch endpoints from OIDC discovery document"""
        try:
            response = requests.get(discovery_url)
            response.raise_for_status()
            discovery_doc = response.json()
            self.authorization_endpoint = discovery_doc["authorization_endpoint"]
            self.token_endpoint = discovery_doc["token_endpoint"]
            self.userinfo_endpoint = discovery_doc.get("userinfo_endpoint")

            # Set issuer if not already provided
            if not self.issuer:
                self.issuer = discovery_doc.get("issuer")

            logger.info("Discovered endpoints from %s", discovery_url)
        except Exception as e:
            logger.error("Discovery failed: %s", str(e))
            raise

    def _generate_code_verifier(self) -> str:
        """Generate PKCE code verifier (RFC 7636)"""
        return secrets.token_urlsafe(64)

    def _generate_code_challenge(self) -> str:
        """Generate PKCE code challenge (S256 method)"""
        if not self.code_verifier:
            raise ValueError("Code verifier not generated")
        digest = hashlib.sha256(self.code_verifier.encode()).digest()
        return base64.urlsafe_b64encode(digest).decode().rstrip("=")

    def build_authorization_url(self) -> str:
        """
        Construct authorization request URL with nonce

        :return: Complete authorization URL with parameters
        """
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": self.scope,
            "state": self.state,
            "nonce": self.nonce,  # Include nonce in request
        }

        if self.use_pkce:
            params.update(
                {
                    "code_challenge": self._generate_code_challenge(),
                    "code_challenge_method": "S256",
                }
            )

        url_parts = urlparse(self.authorization_endpoint)
        query = parse_qs(url_parts.query)
        query.update(params)
        return f"{url_parts.scheme}://{url_parts.netloc}{url_parts.path}?{urlencode(query, doseq=True)}"

    def parse_authorization_response(self, redirect_response: str) -> dict:
        """
        Parse authorization response from redirect URI

        :param redirect_response: Full redirect URL received at callback
        :return: Dictionary with authorization code and state
        """
        parsed = urlparse(redirect_response)
        query = parse_qs(parsed.query)

        if "error" in query:
            error = query["error"][0]
            error_desc = query.get("error_description", [""])[0]
            logger.error("Authorization error: %s - %s", error, error_desc)
            raise ValueError(f"Authorization error: {error} - {error_desc}")

        if "code" not in query:
            raise ValueError("Authorization code missing in response")

        response_state = query.get("state", [None])[0]
        if response_state != self.state:
            raise ValueError("State mismatch - possible CSRF attack")

        return {"code": query["code"][0], "state": response_state}

    def exchange_code_for_tokens(
        self, code: str, validate_id_token: bool = True
    ) -> dict:
        """
        Exchange authorization code for tokens

        :param code: Authorization code from redirect
        :param validate_id_token: Perform ID token validation
        :return: Token response from server
        """
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "code": code,
        }

        if self.use_pkce:
            data["code_verifier"] = self.code_verifier

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        # Add client secret if confidential client
        if self.client_secret:
            data["client_secret"] = self.client_secret

        try:
            response = requests.post(self.token_endpoint, data=data, headers=headers)
            response.raise_for_status()
            self.tokens = response.json()
            logger.info("Successfully obtained tokens")

            # Validate ID token if present
            if validate_id_token and "id_token" in self.tokens:
                self.validate_id_token(self.tokens["id_token"])

            return self.tokens
        except requests.exceptions.HTTPError as e:
            logger.error("Token exchange failed: %s", e.response.text)
            raise

    def get_userinfo(self) -> dict:
        """
        Retrieve userinfo using access token

        :return: Userinfo claims
        """
        if not self.tokens.get("access_token"):
            raise ValueError("No access token available")

        headers = {
            "Authorization": f"Bearer {self.tokens['access_token']}",
            "Accept": "application/json",
        }

        try:
            response = requests.get(self.userinfo_endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error("Userinfo request failed: %s", e.response.text)
            raise

    def refresh_tokens(self, validate_id_token: bool = True) -> dict:
        """
        Refresh access token using refresh token

        :param validate_id_token: Validate new ID token if included
        :return: New token response
        """
        if not self.tokens.get("refresh_token"):
            raise ValueError("No refresh token available")

        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "refresh_token": self.tokens["refresh_token"],
        }

        if self.client_secret:
            data["client_secret"] = self.client_secret

        try:
            response = requests.post(self.token_endpoint, data=data)
            response.raise_for_status()
            self.tokens = response.json()
            logger.info("Tokens refreshed successfully")

            # Validate new ID token if present
            if validate_id_token and "id_token" in self.tokens:
                self.validate_id_token(self.tokens["id_token"])

            return self.tokens
        except requests.exceptions.HTTPError as e:
            logger.error("Token refresh failed: %s", e.response.text)
            raise

    def validate_id_token(self, id_token: str) -> bool:
        """
        Validate ID token claims (without cryptographic verification)

        :param id_token: ID Token JWT
        :return: True if basic validation passes
        """
        try:
            # Split JWT into header, payload, signature
            parts = id_token.split(".")
            if len(parts) != 3:
                raise ValueError("Invalid JWT structure")

            # Decode payload
            payload = parts[1]
            # Add padding if needed
            payload += "=" * (4 - len(payload) % 4)
            claims = json.loads(base64.urlsafe_b64decode(payload))

            # Validate claims
            current_time = time.time()

            # 1. Check issuer
            if self.issuer and claims.get("iss") != self.issuer:
                raise ValueError(
                    f"Issuer mismatch: expected {self.issuer}, got {claims.get('iss')}"
                )

            # 2. Check audience
            aud = claims.get("aud")
            if not aud:
                raise ValueError("Missing aud claim")

            if isinstance(aud, list):
                if self.client_id not in aud:
                    raise ValueError(
                        f"Client ID {self.client_id} not in audience {aud}"
                    )
            elif aud != self.client_id:
                raise ValueError(
                    f"Audience mismatch: expected {self.client_id}, got {aud}"
                )

            # 3. Check expiration
            if claims.get("exp", 0) < current_time:
                raise ValueError("Token has expired")

            # 4. Check nonce
            token_nonce = claims.get("nonce")
            if token_nonce != self.nonce:
                raise ValueError(
                    f"Nonce mismatch: expected {self.nonce}, got {token_nonce}"
                )

            # 5. Check issued-at time
            if claims.get("iat", current_time + 10) > current_time + 10:
                raise ValueError("Token issued in the future")

            logger.info("ID token claims validated successfully")
            return True

        except Exception as e:
            logger.error("ID token validation failed: %s", str(e))
            raise

    def reset_nonce(self, length: int = 16) -> None:
        """
        Generate a new nonce value

        :param length: Length of new nonce in bytes
        """
        self.nonce = secrets.token_urlsafe(length)
        logger.info("Nonce reset to: %s", self.nonce)


if __name__ == "__main__":
    # Initialize tester
    oidc = OIDCTester(
        client_id="your_client_id",
        client_secret="your_secret",
        redirect_uri="http://localhost:8000/callback",
        discovery_url="http://127.0.0.1:8000/api/v1/oidc/.well-known/openid-configuration",
    )

    # 1. Get authorization URL
    auth_url = oidc.build_authorization_url()
    print(f"Authorization URL: {auth_url}")

    # 2. Simulate redirect (in real flow user would authenticate here)
    redirect_response = input("Paste full redirect URL: ")

    # 3. Parse response
    auth_response = oidc.parse_authorization_response(redirect_response)

    # 4. Exchange code for tokens
    tokens = oidc.exchange_code_for_tokens(auth_response["code"])
    print(f"ID Token: {tokens['id_token']}")

    # 5. Get userinfo
    userinfo = oidc.get_userinfo()
    print(f"User email: {userinfo['email']}")

    # 6. Refresh tokens (when access token expires)
    new_tokens = oidc.refresh_tokens()
