# Generated by Django 4.2 on 2023-04-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("characters", "0003_charactermodel_is_locked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="charactermodel",
            name="is_locked",
            field=models.BooleanField(default=False),
        ),
    ]
