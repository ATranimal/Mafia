# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-24 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mafia', '0007_auto_20171223_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='action',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
    ]