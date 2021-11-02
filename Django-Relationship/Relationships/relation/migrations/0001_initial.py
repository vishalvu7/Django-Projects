# Generated by Django 3.2.8 on 2021-10-28 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('acc_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankname', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
