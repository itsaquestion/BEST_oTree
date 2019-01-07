from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from string import Template
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey_basic_info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sur_gender = models.StringField(
        choices=['男', '女'],
        verbose_name="你的性别是",
        widget=widgets.RadioSelectHorizontal)

    sur_birth_year = models.IntegerField(verbose_name="你出生的年份是")
    sur_birth_month = models.IntegerField(verbose_name="你出生的月份是(1-12)", min=1, max=12)

    sur_nationality = models.StringField(
        verbose_name="你的民族是"
    )

    sur_party_member = models.StringField(
        verbose_name="你是否为党员",
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )

    sur_student_leader = models.StringField(
        verbose_name="你在大学期间是否担任学生干部",
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )

    sur_school = models.StringField(
        verbose_name="你就读的学院为")

    sur_grade = models.StringField(
        choices=['大一', '大二', '大三', '大四', '研一', '研二'],
        verbose_name="你就读的年级为",
        widget=widgets.RadioSelectHorizontal)

    sur_height = models.IntegerField(verbose_name="你的身高为(cm)")

    sur_weight = models.IntegerField(verbose_name="你的体重为(kg)")

    sur_expenses = models.IntegerField(verbose_name="你每个月的生活费平均有(元)")

    sur_n_big_bro = models.IntegerField(verbose_name="你的亲哥哥的数量为(没有请填0)")

    sur_n_big_sis = models.IntegerField(verbose_name="你的亲姐姐的数量为(没有请填0)")

    sur_n_small_bro = models.IntegerField(verbose_name="你的亲弟弟的数量为(没有请填0)")

    sur_n_small_sis = models.IntegerField(verbose_name="你的亲妹妹的数量为(没有请填0)")

    sur_m_edu = models.StringField(
        choices=['小学及以下', '初中', '高中', '大学及以上'],
        verbose_name="你母亲的最高学历是",
        widget=widgets.RadioSelectHorizontal)

    sur_f_edu = models.StringField(
        choices=['小学及以下', '初中', '高中', '大学及以上'],
        verbose_name="你父亲的最高学历是",
        widget=widgets.RadioSelectHorizontal)

    sur_urban_rural = models.StringField(
        choices=['农村', '城镇'],
        verbose_name="你是来自农村还是城镇",
        widget=widgets.RadioSelectHorizontal)

    sur_birth_province = models.StringField(
        verbose_name='你出生的省份（自治区、直辖市），请填省区名前两个字（比如四川、新疆）'
    )

    sur_family_income = models.StringField(
        choices=['5万以下', '5万-10万','10万-25万','25万-50万','50万-100万','100万及以上'],
        verbose_name = '你的家庭年总收入大概的范围是'
    )