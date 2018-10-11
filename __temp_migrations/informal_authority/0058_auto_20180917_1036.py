# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-17 02:36
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('informal_authority', '0057_group_treatment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='sur_birth_month',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_birth_year',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_gender',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_grade',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_party_member',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_project_01',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_project_02',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_project_03',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_project_04',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_project_05',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_q01',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_q02',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_q03',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_q04',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_q05',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_q06',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_q07',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_q08',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_school',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sur_student_leader',
        ),
        migrations.AddField(
            model_name='player',
            name='svy_birth_month',
            field=otree.db.models.IntegerField(null=True, verbose_name='你出生的月份是(1-12)'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_birth_year',
            field=otree.db.models.IntegerField(null=True, verbose_name='你出生的年份是'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_gender',
            field=otree.db.models.StringField(choices=[('男', '男'), ('女', '女')], max_length=10000, null=True, verbose_name='你的性别是'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_grade',
            field=otree.db.models.StringField(choices=[('大一', '大一'), ('大二', '大二'), ('大三', '大三'), ('大四', '大四'), ('研一', '研一'), ('研二', '研二')], max_length=10000, null=True, verbose_name='你就读的年级为'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_party_member',
            field=otree.db.models.StringField(choices=[('是', '是'), ('否', '否')], max_length=10000, null=True, verbose_name='你是否为党员'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_project_01',
            field=otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_project_02',
            field=otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_project_03',
            field=otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_project_04',
            field=otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_project_05',
            field=otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_q01',
            field=otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（1） 50%的可能，你将得到0个实验币；50%的可能，你将得到150实验币'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_q02',
            field=otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（2） 50%的可能，你将得到0个实验币；50%的可能，你将得到140实验币'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_q03',
            field=otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（3） 50%的可能，你将得到0个实验币；50%的可能，你将得到130实验币'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_q04',
            field=otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（4） 50%的可能，你将得到0个实验币；50%的可能，你将得到120实验币'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_q05',
            field=otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（5） 50%的可能，你将得到0个实验币；50%的可能，你将得到110实验币'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_q06',
            field=otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（6） 50%的可能，你将得到0个实验币；50%的可能，你将得到100实验币'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_q07',
            field=otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（7） 50%的可能，你将得到0个实验币；50%的可能，你将得到90实验币'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_q08',
            field=otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（8） 50%的可能，你将得到0个实验币；50%的可能，你将得到80实验币'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_school',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='你就读的学院为'),
        ),
        migrations.AddField(
            model_name='player',
            name='svy_student_leader',
            field=otree.db.models.StringField(choices=[('是', '是'), ('否', '否')], max_length=10000, null=True, verbose_name='你是否为学生干部'),
        ),
    ]
