from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from apps.users.validators import username_validator
from django.core.validators import RegexValidator
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        blank=False,
        unique=True,
        help_text=_("Required. A valid email with a valid domain"),
    )

    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        unique=True,
        validators=[
            username_validator,
            RegexValidator(
                rf"^[a-zA-Z0-9_-]+#[0-9]{{{settings.DISCRIMINATOR_LENGTH}}}$",
                message="Username is not valid for this regex `^[a-zA-Z0-9_-]+#[0-9]{4}$`",
            ),
        ],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.pk}. {self.email}"
