# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-27 03:30
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('informal_authority', '0032_auto_20180527_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='sur_school',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='你就读的学院为'),
        ),
    ]
