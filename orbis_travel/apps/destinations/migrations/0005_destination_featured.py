# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0004_auto_20171022_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='featured',
            field=models.BooleanField(default=False, help_text='Only one card should be featured.'),
        ),
    ]
