from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Survey, {
            'sur_gender': '男',
            'sur_birth_year': 1990,
            'sur_birth_month': 12,
            'sur_nationality': '汉族',
            'sur_party_member': '是',
            'sur_student_leader': '是',
            'sur_school': '经管',
            'sur_grade': '大一',
            'sur_height': 170,
            'sur_weight': 60,
            'sur_expenses': 3000,
            'sur_n_big_bro': 0,
            'sur_n_big_sis': 0,
            'sur_n_small_bro': 0,
            'sur_n_small_sis': 0,
            'sur_m_edu':'小学及以下',
            'sur_f_edu':'小学及以下',
            'sur_urban_rural':'农村',
            'sur_birth_province':'北京',
            'sur_family_income':'5万以下'
        })
