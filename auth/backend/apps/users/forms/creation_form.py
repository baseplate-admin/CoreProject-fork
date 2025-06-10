from django.contrib.auth.forms import UserCreationForm

from ..models import CustomUser


class CustomUserCreationForm(UserCreationForm[CustomUser]):  # type: ignore
    class Meta:
        model = CustomUser
        fields = ("email",)
