# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-27 05:57
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('informal_authority', '0042_auto_20180527_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gamble_payoff_points',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='gamble_round',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='total_payoff_points',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
