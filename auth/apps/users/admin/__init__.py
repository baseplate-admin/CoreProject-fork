from .user import CustomUserAdmin as CustomUserAdmin
from .client import ClientAdmin as ClientAdmin
from .authorization_code import AuthorizationCodeAdmin as AuthorizationCodeAdmin
from .token import TokenAdmin as TokenAdmin


# MoneyPatch
# https://stackoverflow.com/questions/6191662/django-admin-login-form-overriding-max-length-failing
from django.contrib.auth.forms import AuthenticationForm  # noqa

AuthenticationForm.base_fields[
    "username"
].label = "Email | Username (with discriminator) "
