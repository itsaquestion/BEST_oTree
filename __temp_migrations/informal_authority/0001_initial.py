# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-06 07:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('treatment', otree.db.models.StringField(max_length=10000, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informal_authority_group', to='otree.Session')),
            ],
            options={
                'db_table': 'informal_authority_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('treatment', otree.db.models.StringField(max_length=10000, null=True)),
                ('label', otree.db.models.StringField(max_length=10000, null=True)),
                ('label_partner', otree.db.models.StringField(max_length=10000, null=True)),
                ('pay_round', otree.db.models.IntegerField(null=True)),
                ('co_payoff_points', otree.db.models.FloatField(null=True)),
                ('gamble_round', otree.db.models.IntegerField(null=True)),
                ('gamble_payoff_points', otree.db.models.FloatField(null=True)),
                ('total_payoff_points', otree.db.models.FloatField(null=True)),
                ('correct', otree.db.models.IntegerField(null=True)),
                ('id_choice_01', otree.db.models.IntegerField(choices=[(0, 0), (1, 1)], null=True)),
                ('co_choice_01', otree.db.models.StringField(choices=[('"主"角色', '"主"角色'), ('"从"角色', '"从"角色')], max_length=10000, null=True)),
                ('co_choice_02', otree.db.models.StringField(choices=[('"主"角色', '"主"角色'), ('"从"角色', '"从"角色')], max_length=10000, null=True)),
                ('co_choice_03', otree.db.models.StringField(choices=[('"主"角色', '"主"角色'), ('"从"角色', '"从"角色')], max_length=10000, null=True)),
                ('co_choice_04', otree.db.models.StringField(choices=[('"主"角色', '"主"角色'), ('"从"角色', '"从"角色')], max_length=10000, null=True)),
                ('co_choice_05', otree.db.models.StringField(choices=[('"主"角色', '"主"角色'), ('"从"角色', '"从"角色')], max_length=10000, null=True)),
                ('sur_q01', otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（1） 50%的可能，你将得到0个实验币；50%的可能，你将得到150实验币')),
                ('sur_q02', otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（2） 50%的可能，你将得到0个实验币；50%的可能，你将得到140实验币')),
                ('sur_q03', otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（3） 50%的可能，你将得到0个实验币；50%的可能，你将得到130实验币')),
                ('sur_q04', otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（4） 50%的可能，你将得到0个实验币；50%的可能，你将得到120实验币')),
                ('sur_q05', otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（5） 50%的可能，你将得到0个实验币；50%的可能，你将得到110实验币')),
                ('sur_q06', otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（6） 50%的可能，你将得到0个实验币；50%的可能，你将得到100实验币')),
                ('sur_q07', otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（7） 50%的可能，你将得到0个实验币；50%的可能，你将得到90实验币')),
                ('sur_q08', otree.db.models.StringField(choices=[('接受', '接受'), ('拒绝', '拒绝')], max_length=10000, null=True, verbose_name='（8） 50%的可能，你将得到0个实验币；50%的可能，你将得到80实验币')),
                ('sur_birth_year', otree.db.models.IntegerField(null=True, verbose_name='你出生的年份是')),
                ('sur_birth_month', otree.db.models.IntegerField(null=True, verbose_name='你出生的月份是(1-12)')),
                ('sur_gender', otree.db.models.StringField(choices=[('男', '男'), ('女', '女')], max_length=10000, null=True, verbose_name='你的性别是')),
                ('sur_grade', otree.db.models.StringField(choices=[('大一', '大一'), ('大二', '大二'), ('大三', '大三'), ('大四', '大四'), ('研一', '研一'), ('研二', '研二')], max_length=10000, null=True, verbose_name='你就读的年级为')),
                ('sur_school', otree.db.models.StringField(max_length=10000, null=True, verbose_name='你就读的学院为')),
                ('sur_party_member', otree.db.models.StringField(choices=[('是', '是'), ('否', '否')], max_length=10000, null=True, verbose_name='你是否为党员')),
                ('sur_student_leader', otree.db.models.StringField(choices=[('是', '是'), ('否', '否')], max_length=10000, null=True, verbose_name='你是否为学生干部')),
                ('sur_project_01', otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择')),
                ('sur_project_02', otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择')),
                ('sur_project_03', otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择')),
                ('sur_project_04', otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择')),
                ('sur_project_05', otree.db.models.StringField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3')], max_length=10000, null=True, verbose_name='你会选择')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='informal_authority.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informal_authority_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informal_authority_player', to='otree.Session')),
            ],
            options={
                'db_table': 'informal_authority_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='informal_authority_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'informal_authority_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informal_authority.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informal_authority.Subsession'),
        ),
    ]
