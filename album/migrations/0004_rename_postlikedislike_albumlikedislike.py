# Generated by Django 3.2.8 on 2021-10-14 07:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0003_postlikedislike'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostLikeDislike',
            new_name='AlbumLikeDislike',
        ),
    ]
