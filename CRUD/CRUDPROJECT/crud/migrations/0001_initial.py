# Generated by Django 3.2.8 on 2021-10-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=30)),
                ('city', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
