from ..models import AuthorizationCode

from django.contrib import admin


@admin.register(AuthorizationCode)
class AuthorizationCodeAdmin(admin.ModelAdmin):
    pass
