import ulid
from django.db import models
from django.utils.translation import gettext_lazy as _
from .generators import generate_ulid


class UUIDPrimaryKeyMixin(models.Model):
    id = models.CharField(
        primary_key=True,
        editable=False,
        max_length=26,  # ULID string length
        default=generate_ulid,  # Generate ULID
        verbose_name=_("ID"),
    )

    class Meta:
        abstract = True


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        editable=False, auto_now_add=True, verbose_name=_("Created At")
    )

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(
        editable=False, auto_now=True, verbose_name=_("Updated At")
    )

    class Meta:
        abstract = True
