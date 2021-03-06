# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 08:38
from __future__ import unicode_literals

import cms.apps.media.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0003_file_alt_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the setting', max_length=1024)),
                ('key', models.CharField(help_text='The key used to reference the setting', max_length=1024)),
                ('type', models.CharField(choices=[('string', 'String'), ('text', 'Text'), ('number', 'Number'), ('image', 'Image')], max_length=1024)),
                ('string', models.CharField(blank=True, max_length=2048, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('image', cms.apps.media.models.ImageRefField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='media.File')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
