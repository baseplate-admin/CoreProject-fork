from ninja.errors import HttpError
from ninja.security import HttpBearer
from .models import Token

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
