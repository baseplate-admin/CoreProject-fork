from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDPrimaryKeyMixin(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("ID"))

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
