# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-11 09:30
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('repeat_prisoner', '0003_auto_20181011_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='partner_decision',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
