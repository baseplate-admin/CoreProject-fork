from django.db import models
from django.utils import timezone

from ..mixins import UUIDPrimaryKeyMixin, CreatedAtMixin


class Token(UUIDPrimaryKeyMixin, CreatedAtMixin): # type: ignore
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, unique=True)
    refresh_token = models.CharField(max_length=255, unique=True, blank=True, null=True)
    token_type = models.CharField(max_length=20, default="Bearer")
    scope = models.TextField()
    expires_at = models.DateTimeField()

    def is_valid(self):
        return timezone.now() < self.expires_at
