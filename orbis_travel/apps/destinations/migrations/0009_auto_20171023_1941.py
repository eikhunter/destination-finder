# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0008_auto_20171023_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='continent',
            new_name='country',
        ),
    ]
