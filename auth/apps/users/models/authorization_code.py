import uuid

from django.db import models

from django.utils import timezone


class AuthorizationCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)
    redirect_uri = models.TextField()
    scope = models.TextField()
    nonce = models.CharField(max_length=255, blank=True, null=True)
    code_challenge = models.CharField(max_length=255, blank=True, null=True)
    code_challenge_method = models.CharField(max_length=20, blank=True, null=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() < self.expires_at
