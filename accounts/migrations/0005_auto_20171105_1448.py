# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 14:48
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171103_2315'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('paris', django.db.models.manager.Manager()),
            ],
        ),
    ]