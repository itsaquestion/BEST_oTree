from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import re
import random

class H1_Page(Page):
    form_model = 'player'
    form_fields = ['mhf27', 'mhf28', 'mhf29', 'mhf30', 'mhf31',  'mhf32', 'mhf33', 'mhf34', 'mhf35',
                   'mhf36', 'mhf37', 'mhf38', 'mhf39']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number == self.participant.vars['task_rounds']['H1']
    def vars_for_template(self):
        return {
            'H1': self.participant.vars['task_rounds']['H1']
        }
class H2_Page(Page):
    form_model = 'player'
    form_fields = ['mhf53', 'mhf54', 'mhf55', 'mhf56', 'mhf57', 'mhf58', 'mhf59', 'mhf60', 'mhf61',
                   'mhf62', 'mhf63', 'mhf64', 'mhf65']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number == self.participant.vars['task_rounds']['H2']
    def vars_for_template(self):
        return {
            'H2': self.participant.vars['task_rounds']['H2']
        }


class H3_Page(Page):
    form_model = 'player'
    form_fields = ['mhf14', 'mhf15', 'mhf16', 'mhf17', 'mhf18', 'mhf19', 'mhf20','mhf21', 'mhf22', 'mhf23',
                   'mhf24', 'mhf25', 'mhf26']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number == self.participant.vars['task_rounds']['H3']
    def vars_for_template(self):
        return {
            'H3': self.participant.vars['task_rounds']['H3']
        }
class H4_Page(Page):
    form_model = 'player'
    form_fields = ['mhf66', 'mhf67', 'mhf68', 'mhf69', 'mhf70', 'mhf71','mhf72', 'mhf73','mhf74',
                   'mhf75', 'mhf76', 'mhf77', 'mhf78']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number == self.participant.vars['task_rounds']['H4']
    def vars_for_template(self):
        return {
            'H4': self.participant.vars['task_rounds']['H4']
        }


class H5_Page(Page):
    form_model = 'player'
    form_fields = ['mhf01', 'mhf02', 'mhf03', 'mhf04', 'mhf05', 'mhf06', 'mhf07', 'mhf08', 'mhf09', 'mhf10',
                   'mhf11', 'mhf12', 'mhf13']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number == self.participant.vars['task_rounds']['H5']
    def vars_for_template(self):
        return {
            'H5': self.participant.vars['task_rounds']['H5']
        }

class H6_Page(Page):
    form_model = 'player'
    form_fields = ['mhf40', 'mhf41', 'mhf42', 'mhf43', 'mhf44', 'mhf45','mhf46', 'mhf47','mhf48',
                   'mhf49', 'mhf50', 'mhf51', 'mhf52']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number == self.participant.vars['task_rounds']['H6']
    def vars_for_template(self):
        return {
            'H6': self.participant.vars['task_rounds']['H6']
        }

class M1_Page(Page):
    form_model = 'player'
    form_fields = ['mmf27', 'mmf28', 'mmf29', 'mmf30', 'mmf31',  'mmf32', 'mmf33', 'mmf34', 'mmf35',
                   'mmf36', 'mmf37', 'mmf38','mmf39']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == self.participant.vars['task_rounds']['H1']
    def vars_for_template(self):
        return {
            'H1': self.participant.vars['task_rounds']['H1']
        }
class M2_Page(Page):
    form_model = 'player'
    form_fields = ['mmf53', 'mmf54', 'mmf55', 'mmf56', 'mmf57', 'mmf58', 'mmf59', 'mmf60', 'mmf61',
                   'mmf62', 'mmf63', 'mmf64', 'mmf65']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == self.participant.vars['task_rounds']['H2']
    def vars_for_template(self):
        return {
            'H2': self.participant.vars['task_rounds']['H2']
        }
class M3_Page(Page):
    form_model = 'player'
    form_fields = ['mmf14', 'mmf15', 'mmf16', 'mmf17', 'mmf18', 'mmf19', 'mmf20','mmf21', 'mmf22', 'mmf23',
                   'mmf24', 'mmf25', 'mmf26']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == self.participant.vars['task_rounds']['H3']
    def vars_for_template(self):
        return {
            'H3': self.participant.vars['task_rounds']['H3']
        }
class M4_Page(Page):
    form_model = 'player'
    form_fields = ['mmf66', 'mmf67', 'mmf68', 'mmf69', 'mmf70', 'mmf71','mmf72', 'mmf73','mmf74',
                   'mmf75', 'mmf76', 'mmf77', 'mmf78']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == self.participant.vars['task_rounds']['H4']
    def vars_for_template(self):
        return {
            'H4': self.participant.vars['task_rounds']['H4']
        }
class M5_Page(Page):
    form_model = 'player'
    form_fields = ['mmf01', 'mmf02', 'mmf03', 'mmf04', 'mmf05', 'mmf06', 'mmf07', 'mmf08', 'mmf09', 'mmf10',
                   'mmf11', 'mmf12', 'mmf13']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == self.participant.vars['task_rounds']['H5']
    def vars_for_template(self):
        return {
            'H5': self.participant.vars['task_rounds']['H5']
        }
class M6_Page(Page):
    form_model = 'player'
    form_fields = ['mmf40', 'mmf41', 'mmf42', 'mmf43', 'mmf44', 'mmf45','mmf46', 'mmf47','mmf48',
                   'mmf49', 'mmf50', 'mmf51', 'mmf52']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == self.participant.vars['task_rounds']['H6']
    def vars_for_template(self):
        return {
            'H6': self.participant.vars['task_rounds']['H6']
        }
class L1_Page(Page):
    form_model = 'player'
    form_fields = ['mlf27', 'mlf28', 'mlf29', 'mlf30', 'mlf31',  'mlf32', 'mlf33', 'mlf34', 'mlf35',
                   'mlf36', 'mlf37', 'mlf38','mlf39']

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number == self.participant.vars['task_rounds']['H1']
    def vars_for_template(self):
        return {
            'H1': self.participant.vars['task_rounds']['H1']
        }
class L2_Page(Page):
    form_model = 'player'
    form_fields = ['mlf53', 'mlf54', 'mlf55', 'mlf56', 'mlf57', 'mlf58', 'mlf59', 'mlf60', 'mlf61',
                   'mlf62', 'mlf63', 'mlf64', 'mlf65']

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number == self.participant.vars['task_rounds']['H2']
    def vars_for_template(self):
        return {
            'H2': self.participant.vars['task_rounds']['H2']
        }
class L3_Page(Page):
    form_model = 'player'
    form_fields = ['mlf14', 'mlf15', 'mlf16', 'mlf17', 'mlf18', 'mlf19', 'mlf20','mlf21', 'mlf22', 'mlf23',
                   'mlf24', 'mlf25', 'mlf26']

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number == self.participant.vars['task_rounds']['H3']
    def vars_for_template(self):
        return {
            'H3': self.participant.vars['task_rounds']['H3']
        }
class L4_Page(Page):
    form_model = 'player'
    form_fields = ['mlf66', 'mlf67', 'mlf68', 'mlf69', 'mlf70', 'mlf71','mlf72', 'mlf73','mlf74',
                   'mlf75', 'mlf76', 'mlf77', 'mlf78']

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number == self.participant.vars['task_rounds']['H4']
    def vars_for_template(self):
        return {
            'H4': self.participant.vars['task_rounds']['H4']
        }
class L5_Page(Page):
    form_model = 'player'
    form_fields = ['mlf01', 'mlf02', 'mlf03', 'mlf04', 'mlf05', 'mlf06', 'mlf07', 'mlf08', 'mlf09', 'mlf10',
                   'mlf11', 'mlf12', 'mlf13']

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number == self.participant.vars['task_rounds']['H5']
    def vars_for_template(self):
        return {
            'H5': self.participant.vars['task_rounds']['H5']
        }
class L6_Page(Page):
    form_model = 'player'
    form_fields = ['mlf40', 'mlf41', 'mlf42', 'mlf43', 'mlf44', 'mlf45','mlf46', 'mlf47','mlf48',
                   'mlf49', 'mlf50', 'mlf51', 'mlf52']

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number == self.participant.vars['task_rounds']['H6']
    def vars_for_template(self):
        return {
            'H6': self.participant.vars['task_rounds']['H6']
        }
class M7_Page(Page):
    form_model = 'player'
    form_fields = ['mm2f01', 'mm2f02', 'mm2f03', 'mm2f04', 'mm2f05', 'mm2f06', 'mm2f07', 'mm2f08', 'mm2f09', 'mm2f10',
                   'mm2f11', 'mm2f12', 'mm2f13']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds1']['M7']
    def vars_for_template(self):
        return {
            'M7': self.participant.vars['task_rounds1']['M7']
        }
class M8_Page(Page):
    form_model = 'player'
    form_fields = ['mm2f14', 'mm2f15', 'mm2f16', 'mm2f17', 'mm2f18', 'mm2f19', 'mm2f20','mm2f21', 'mm2f22', 'mm2f23',
                   'mm2f24', 'mm2f25', 'mm2f26']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds1']['M8']
    def vars_for_template(self):
        return {
            'M8': self.participant.vars['task_rounds1']['M8']
        }
class M9_Page(Page):
    form_model = 'player'
    form_fields = ['mm2f27', 'mm2f28', 'mm2f29', 'mm2f30', 'mm2f31', 'mm2f32', 'mm2f33', 'mm2f34', 'mm2f35', 'mm2f36',
                   'mm2f37', 'mm2f38', 'mm2f39']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds1']['M9']
    def vars_for_template(self):
        return {
            'M9': self.participant.vars['task_rounds1']['M9']
        }
class M10_Page(Page):
    form_model = 'player'
    form_fields = ['mm2f40', 'mm2f41', 'mm2f42', 'mm2f43', 'mm2f44', 'mm2f45', 'mm2f46','mm2f47', 'mm2f48', 'mm2f49',
                   'mm2f50', 'mm2f51', 'mm2f52']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds1']['M10']
    def vars_for_template(self):
        return {
            'M10': self.participant.vars['task_rounds1']['M10']
        }

class M11_Page(Page):
    form_model = 'player'
    form_fields = ['mm2f53', 'mm2f54', 'mm2f55', 'mm2f56', 'mm2f57', 'mm2f58', 'mm2f59', 'mm2f60', 'mm2f61', 'mm2f62',
                   'mm2f63', 'mm2f64', 'mm2f65']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds1']['M11']
    def vars_for_template(self):
        return {
            'M11': self.participant.vars['task_rounds1']['M11']
        }
class M12_Page(Page):
    form_model = 'player'
    form_fields = ['mm2f66', 'mm2f67', 'mm2f68', 'mm2f69', 'mm2f70', 'mm2f71', 'mm2f72','mm2f73', 'mm2f74', 'mm2f75',
                   'mm2f76', 'mm2f77', 'mm2f78']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds1']['M12']
    def vars_for_template(self):
        return {
            'M12': self.participant.vars['task_rounds1']['M12']
        }
class Results(Page):
    def vars_for_template(self):
        return{
            'final_pay': (47-self.player.payoff.to_real_world_currency(self.session)),
            'round': self.player.pay_round,
            'round1': self.player.payoff_choice
        }
    def is_displayed(self):
        return self.round_number == 12

class IdentityCompete1(Page):
    def is_displayed(self):
        return self.round_number == 1


class SurveyIntro(Page):
    def is_displayed(self):
        return self.round_number == 12

class Survey(Page):
    form_model = 'player'
    form_fields = ['sur_birth_year', 'sur_birth_month', 'sur_place', 'sur_nation', 'sur_gender', 'sur_grade',
                   'sur_school', 'sur_economy', 'sur_height', 'sur_weight', 'sur_cash','sur_big_brother',
                   'sur_little_brother', 'sur_big_sister', 'sur_little_sister', 'sur_mother', 'sur_father',
                   'sur_come_from', 'sur_income', 'sur_party_member', 'sur_student_leader', 'sur_left_behind',
                   'sur_risk','sur_risk1','sur_risk2','sur_risk3']

    def before_next_page(self):
        p = self.player
        m2 = ['A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失96.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失108.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失119.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失131.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失142.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失154.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失165.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失177.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失188.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失200.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失223.0代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失246.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币；  B：100%损失269.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失101.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失112.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失123.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失134.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失145.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失156.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失167.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失178.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失189.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失200.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失222.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失244.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币；  B：100%损失266.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失105.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失116.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失126.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失137.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失147.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失158.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失168.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失179.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失189.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失200.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失221.0代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失242.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币；  B：100%损失263.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失110.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失120.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失130.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失140.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失150.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失160.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失170.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失180.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失190.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失200.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失220.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失240.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币；  B：100%损失260.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失114.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失124.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失133.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失143.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失152.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失162.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失171.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失181.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失190.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失200.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失219.0代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失238.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币；  B：100%损失257.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失119.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失128.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失137.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失146.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失155.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失164.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失173.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失182.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失191.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失200.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失218.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失236.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币；  B：100%损失254.0代币']

        sur_choice = ['mm2f01', 'mm2f02', 'mm2f03', 'mm2f04', 'mm2f05', 'mm2f06', 'mm2f07', 'mm2f08', 'mm2f09',
                      'mm2f10',
                      'mm2f11', 'mm2f12', 'mm2f13', 'mm2f14', 'mm2f15', 'mm2f16', 'mm2f17', 'mm2f18', 'mm2f19',
                      'mm2f20', 'mm2f21', 'mm2f22', 'mm2f23',
                      'mm2f24', 'mm2f25', 'mm2f26', 'mm2f27', 'mm2f28', 'mm2f29', 'mm2f30', 'mm2f31', 'mm2f32',
                      'mm2f33', 'mm2f34', 'mm2f35', 'mm2f36',
                      'mm2f37', 'mm2f38', 'mm2f39', 'mm2f40', 'mm2f41', 'mm2f42', 'mm2f43', 'mm2f44', 'mm2f45',
                      'mm2f46', 'mm2f47', 'mm2f48', 'mm2f49',
                      'mm2f50', 'mm2f51', 'mm2f52', 'mm2f53', 'mm2f54', 'mm2f55', 'mm2f56', 'mm2f57', 'mm2f58',
                      'mm2f59', 'mm2f60', 'mm2f61', 'mm2f62',
                      'mm2f63', 'mm2f64', 'mm2f65', 'mm2f66', 'mm2f67', 'mm2f68', 'mm2f69', 'mm2f70', 'mm2f71',
                      'mm2f72', 'mm2f73', 'mm2f74', 'mm2f75',
                      'mm2f76', 'mm2f77', 'mm2f78']
        sur_choice1 = str(random.sample(sur_choice, 1))
        Ss = re.findall(r"\d+\.?\d*", sur_choice1)
        n = int(Ss[1]) - 1
        i = 0
        if (n + 1) % 13 == 0:
            i = 13
        else:
            i = (n + 1) % 13
        j = ((n + 1) // 13) + 7
        p.pay_round = j
        p.payoff_choice = i
        sj = m2[n]
        print(sj)
        str_sj = str(sj)
        Sss = re.findall(r"\d+\.?\d*", str_sj)
        a = Sss[1]
        b = Sss[3]
        c = Sss[5]
        if str(p.choice) == "A":
            if random.choice([0, 1]) == 0:
                p.payoff = a
            else:
                p.payoff = b
        else:
            p.payoff = c

    def is_displayed(self):
        return self.round_number == 12
    # def vars_for_template(self):
    #     m, s = divmod(self.session.config['game_time_sec'], 60)
    #     h, m = divmod(m, 60)
    #
    #     show_next_info = "practice" in self.group.treatment
    #     has_reward = "reward" in self.group.treatment
    #
    #     return_vars = {
    #         'correct_threshold': self.session.vars['correct_threshold'],
    #         'show_next_info': show_next_info,
    #         'has_reward': has_reward,
    #         'reward_show_after': self.player.is_reward_show_after()
    #     }
    #
    #     if m > 0:
    #         return_vars['timeout_string'] = "%02d分%02d秒" % (m, s)
    #     else:
    #         return_vars['timeout_string'] = "%02d秒" % s
    #
    #     return return_vars
class _Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class _Introgame(Page):
    def is_displayed(self):
        return self.round_number == 1

class _Introlottery(Page):
    def is_displayed(self):
        return self.round_number == 1

class _Intro_we(Page):
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [
    _Intro_we,
    _Intro,
    _Introgame,
    IdentityCompete1,
    _Introlottery,
    H1_Page,
    M1_Page,
    L1_Page,
    H2_Page,
    M2_Page,
    L2_Page,
    H3_Page,
    M3_Page,
    L3_Page,
    H4_Page,
    M4_Page,
    L4_Page,
    H5_Page,
    M5_Page,
    L5_Page,
    H6_Page,
    M6_Page,
    L6_Page,
    M7_Page,
    M8_Page,
    M9_Page,
    M10_Page,
    M11_Page,
    M12_Page,
    SurveyIntro,
    Survey,
    Results
]
