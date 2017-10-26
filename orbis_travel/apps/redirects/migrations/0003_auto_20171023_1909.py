# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirects', '0002_auto_20160805_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='new_path',
            field=models.CharField(blank=True, help_text="This can be either an absolute path (as above) or a full URL starting with 'http://'.", max_length=200, verbose_name='redirect to'),
        ),
        migrations.AlterField(
            model_name='redirect',
            name='old_path',
            field=models.CharField(db_index=True, help_text="This should be an absolute path, excluding the domain name. Example: '/events/search/'.", max_length=200, unique=True, verbose_name='redirect from'),
        ),
        migrations.AlterField(
            model_name='redirect',
            name='regular_expression',
            field=models.BooleanField(default=False, help_text="This will allow using regular expressions to match and replace patterns in URLs. See the <a href='https://docs.python.org/2/library/re.html' target='_blank'>Python regular expression documentation</a> for details."),
        ),
        migrations.AlterField(
            model_name='redirect',
            name='test_path',
            field=models.CharField(blank=True, help_text='You will need to specify a test path to ensure your regular expression is valid.', max_length=200, null=True),
        ),
    ]