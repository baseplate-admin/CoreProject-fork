from typing import TYPE_CHECKING, Any

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from .models import CustomUser


class UserManager(
    BaseUserManager["CustomUser"],
):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(
        self,
        email: str,
        password: str,
        **extra_fields: dict[str, dict[str, Any]],
    ) -> "CustomUser":
        """Create and save a User with the given email and password."""

        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user: CustomUser = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        **extra_fields: Any,
    ) -> "CustomUser":
        """Create and save a SuperUser with the given email and password."""
        for key in ("is_staff", "is_superuser", "is_active"):
            extra_fields.setdefault(key, True)

        # Sanity Check
        for key, value in {
            "is_staff": _("Superuser must have is_staff=True."),
            "is_superuser": _("Superuser must have is_superuser=True."),
        }.items():
            if extra_fields.get(key) is not True:
                raise ValueError(value)

        return self.create_user(email, password, **extra_fields)
