# Generated by Django 4.1.7 on 2023-03-12 16:03

import functools

import django.db.models.deletion
import django.utils.crypto
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        default=functools.partial(
                            django.utils.crypto.get_random_string, *(16,), **{}
                        ),
                        editable=False,
                        max_length=16,
                        unique=True,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "token",
                "verbose_name_plural": "tokens",
            },
        ),
        migrations.AddIndex(
            model_name="token",
            index=models.Index(fields=["token"], name="api_token_token_5cc0f7_idx"),
        ),
    ]
