# Generated by Django 3.2.6 on 2021-08-21 10:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20210813_2152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_rename_profile_customer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Profile',
        ),
    ]