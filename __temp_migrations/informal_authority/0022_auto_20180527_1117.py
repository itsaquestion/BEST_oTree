# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-27 03:17
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('informal_authority', '0021_auto_20180527_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='sur_birth_month',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='sur_birth_year',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
