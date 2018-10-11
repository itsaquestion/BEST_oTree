# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-27 03:33
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('informal_authority', '0037_auto_20180527_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sur_student_leader',
            field=otree.db.models.StringField(choices=[('是', '是'), ('否', '否')], max_length=10000, null=True, verbose_name='你是否为学生干部'),
        ),
    ]
