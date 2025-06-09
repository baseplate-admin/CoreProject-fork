from django.db import models


class ExpiresAtMixin(models.Model):
    expires_at = models.DateTimeField()

    class Meta:
        abstract = True
