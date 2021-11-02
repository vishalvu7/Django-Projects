# Generated by Django 3.2.8 on 2021-10-29 11:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relation', '0004_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='fkey',
        ),
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
