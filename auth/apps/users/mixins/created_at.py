from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        editable=False, auto_now_add=True, verbose_name=_("Created At")
    )

    class Meta:
        abstract = True
