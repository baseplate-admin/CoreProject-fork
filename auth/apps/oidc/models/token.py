from django.db import models
from django.utils import timezone
from django.contrib.postgres.indexes import BrinIndex, GinIndex

from mixins import UUIDPrimaryKeyMixin, CreatedAtMixin, ExpiresAtMixin

from apps.users.models import CustomUser


class Token(UUIDPrimaryKeyMixin, CreatedAtMixin, ExpiresAtMixin):  # type: ignore
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, unique=True)
    refresh_token = models.CharField(max_length=255, unique=True, blank=True, null=True)
    token_type = models.CharField(max_length=20, default="Bearer")
    scope = models.TextField()

    revoked_at = models.DateTimeField(blank=True, null=True)

    def is_valid(self):
        return timezone.now() < self.expires_at

    class Meta(UUIDPrimaryKeyMixin.Meta, CreatedAtMixin.Meta, ExpiresAtMixin.Meta):
        indexes = [
            models.Index(fields=["access_token"], name="token_access_idx"),
            models.Index(fields=["refresh_token"], name="token_refresh_idx"),
            # BRIN for time-series expiration data
            BrinIndex(fields=["expires_at"], name="token_expires_brin"),
            # BRIN for creation time
            BrinIndex(fields=["created_at"], name="token_created_brin"),
            # Standard index for revocation
            models.Index(fields=["revoked_at"], name="token_revoked_idx"),
            # Proper array index without operator class
            GinIndex(fields=["scope"], name="token_scope_gin"),
        ]
