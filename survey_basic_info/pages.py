from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Survey(Page):
    form_model = 'player'
    form_fields = ['sur_gender', 'sur_birth_year', 'sur_birth_month',
                   'sur_nationality', 'sur_party_member',
                   'sur_student_leader', 'sur_school', 'sur_grade',
                   'sur_height', 'sur_weight', 'sur_expenses',
                   'sur_n_big_bro', 'sur_n_big_sis', 'sur_n_small_bro',
                   'sur_n_small_sis', 'sur_m_edu', 'sur_f_edu',
                   'sur_urban_rural', 'sur_birth_province', 'sur_family_income']


class Results(Page):
    def vars_for_template(self):
        return {'gamble_choice': self.player.choice}


page_sequence = [
    Survey

]
