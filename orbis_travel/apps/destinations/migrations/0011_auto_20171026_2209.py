# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20151002_1655'),
        ('destinations', '0010_destinationslanding'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationLanding',
            fields=[
                ('page', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='pages.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='destinationslanding',
            name='page',
        ),
        migrations.DeleteModel(
            name='DestinationsLanding',
        ),
    ]
