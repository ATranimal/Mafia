# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-20 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mafia', '0004_role_action'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setup',
            name='playerNumber',
        ),
        migrations.AddField(
            model_name='setup',
            name='maximumPlayes',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='setup',
            name='minimumPlayers',
            field=models.IntegerField(default=8),
        ),
    ]
