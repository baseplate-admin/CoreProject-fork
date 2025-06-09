from django.db import models
from django.utils.translation import gettext_lazy as _


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(
        editable=False, auto_now=True, verbose_name=_("Updated At")
    )

    class Meta:
        abstract = True
