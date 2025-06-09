import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField

CLIENT_TYPES = [
    ("animecore", "AnimeCore"),
    ("soundcore", "SoundCore"),
]


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    client_id = models.CharField(max_length=100, unique=True)
    client_secret = models.CharField(max_length=255, blank=True, null=True)
    client_name = models.CharField(max_length=200)
    client_type = models.CharField(
        max_length=20, choices=CLIENT_TYPES, default="confidential"
    )
    redirect_uris = models.TextField(help_text="Comma separated URIs")
    scope = ArrayField(
        models.CharField(max_length=100),
        default=["openid", "profile", "email"],
        help_text="Scopes that the client can request",
    )
    require_pkce = models.BooleanField(default=False)
    allowed_grant_types = models.TextField(default="authorization_code,refresh_token")
    jwks_uri = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
