# Generated by Django 4.0.4 on 2022-04-25 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0014_alter_episodetimestampmodel_episode_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="episodetimestampmodel",
            old_name="episode_number",
            new_name="episode",
        ),
    ]
