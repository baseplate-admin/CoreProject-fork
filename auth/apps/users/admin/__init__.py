from .user import CustomUserAdmin as CustomUserAdmin

# MoneyPatch
# https://stackoverflow.com/questions/6191662/django-admin-login-form-overriding-max-length-failing
from django.contrib.auth.forms import AuthenticationForm  # noqa

AuthenticationForm.base_fields[
    "username"
].label = "Email | Username (with discriminator) "
