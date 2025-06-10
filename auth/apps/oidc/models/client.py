from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from mixins import UUIDPrimaryKeyMixin, CreatedAtMixin, UpdatedAtMixin

CLIENT_TYPES = [
    ("confidential", "Confidential"),
    ("public", "Public"),
]


class Client(UUIDPrimaryKeyMixin, CreatedAtMixin, UpdatedAtMixin):  # type: ignore
    client_id = models.CharField(max_length=100, unique=True)
    client_secret = models.CharField(max_length=255, blank=True, null=True)
    client_name = models.CharField(max_length=200)
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPES)
    redirect_uris = ArrayField(
        models.TextField(),
        help_text="Comma separated URIs",
    )
    scope = ArrayField(
        models.TextField(),
        # default=["openid", "profile", "email"],
        help_text="Scopes that the client can request",
    )
    require_pkce = models.BooleanField(default=False)
    allowed_grant_types = ArrayField(
        models.TextField(),
        # default=["authorization_code", "refresh_token"],
        help_text="Allowed grant types for the client",
    )
    jwks_uri = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.client_name

    class Meta(UUIDPrimaryKeyMixin.Meta, CreatedAtMixin.Meta, UpdatedAtMixin.Meta):
        indexes = [
            # Proper array index without operator class specification
            GinIndex(fields=["redirect_uris"], name="client_redirect_uris_gin"),
        ]
