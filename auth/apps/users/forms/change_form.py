from django.contrib.auth.forms import UserChangeForm

from ..models import CustomUser


class CustomUserChangeForm(UserChangeForm[CustomUser]):  # type: ignore
    class Meta:
        model = CustomUser
        fields = ("email",)
