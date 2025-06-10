from django.db import models
from django.utils.translation import gettext_lazy as _
from generators import generate_ulid


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
