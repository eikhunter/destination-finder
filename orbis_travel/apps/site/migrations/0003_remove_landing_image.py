# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0002_landing_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landing',
            name='image',
        ),
    ]