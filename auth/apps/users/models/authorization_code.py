from django.db import models

from django.utils import timezone
from ..mixins import UUIDPrimaryKeyMixin, CreatedAtMixin, ExpiresAtMixin


class AuthorizationCode(UUIDPrimaryKeyMixin, CreatedAtMixin, ExpiresAtMixin):  # type: ignore
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)
    redirect_uri = models.TextField()
    scope = models.TextField()
    nonce = models.CharField(max_length=255, blank=True, null=True)
    code_challenge = models.CharField(max_length=255, blank=True, null=True)
    code_challenge_method = models.CharField(max_length=20, blank=True, null=True)

    def is_valid(self):
        return timezone.now() < self.expires_at
