from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm[CustomUser]):  # type: ignore
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm[CustomUser]):  # type: ignore
    class Meta:
        model = CustomUser
        fields = ("email",)
