from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.set_payoff()


class Results(Page):
    def vars_for_template(self):
        p_fee = self.session.vars['participation_fee']
        poy = self.session.vars['points_for_one_yuan']

        result = {}
        result["p_fee"] = p_fee
        result["payoff"] = self.player.co_payoff_points / poy + p_fee

        result["c01_1"] = self.player.co_choice_01
        result["c01_2"] = self.player.get_others_in_group()[0].co_choice_01

        result["c02_1"] = self.player.co_choice_02
        result["c02_2"] = self.player.get_others_in_group()[0].co_choice_02

        result["c03_1"] = self.player.co_choice_03
        result["c03_2"] = self.player.get_others_in_group()[0].co_choice_03

        result["c04_1"] = self.player.co_choice_04
        result["c04_2"] = self.player.get_others_in_group()[0].co_choice_04

        result["c05_1"] = self.player.co_choice_05
        result["c05_2"] = self.player.get_others_in_group()[0].co_choice_05

        if self.player.pay_round == 1:
            result['role1'] = result["c01_1"]
            result['role2'] = result["c01_2"]

        if self.player.pay_round == 2:
            result['role1'] = result["c02_1"]
            result['role2'] = result["c02_2"]

        if self.player.pay_round == 3:
            result['role1'] = result["c03_1"]
            result['role2'] = result["c03_2"]

        if self.player.pay_round == 4:
            result['role1'] = result["c04_1"]
            result['role2'] = result["c04_2"]

        if self.player.pay_round == 5:
            result['role1'] = result["c05_1"]
            result['role2'] = result["c05_2"]

        if self.player.gamble_round == 1:
            result['gamble_choice'] = self.player.sur_q01
        if self.player.gamble_round == 2:
            result['gamble_choice'] = self.player.sur_q02
        if self.player.gamble_round == 3:
            result['gamble_choice'] = self.player.sur_q03
        if self.player.gamble_round == 4:
            result['gamble_choice'] = self.player.sur_q04
        if self.player.gamble_round == 5:
            result['gamble_choice'] = self.player.sur_q05
        if self.player.gamble_round == 6:
            result['gamble_choice'] = self.player.sur_q06
        if self.player.gamble_round == 7:
            result['gamble_choice'] = self.player.sur_q07
        if self.player.gamble_round == 8:
            result['gamble_choice'] = self.player.sur_q08

        if result['gamble_choice'] == "拒绝":
            self.player.gamble_payoff_points = 50.0

        self.player.total_payoff_points = self.player.co_payoff_points + self.player.gamble_payoff_points

        self.player.payoff = self.player.total_payoff_points / poy + p_fee

        return result


class IdentityChoiceColor(Page):
    '''
    IdentityChoiceColor：
        Identity 确定参与人的标签
        Choice 选01
        Color 用颜色来表示
    '''
    form_model = 'player'
    form_fields = ['id_choice_01']

    def is_displayed(self):
        return self.player.treatment == "choice_color"

    def vars_for_template(self):
        if self.player.id_in_group == 1:
            return {'color_1': Constants.label_color1, 'color_2': Constants.label_color2}
        else:
            return {'color_1': Constants.label_color2, 'color_2': Constants.label_color1}


class IdentityChoiceWl(Page):
    '''
    IdentityChoiceWl：
        Identity 确定参与人的标签
        Choice 选01
        Wl 用胜负方来表示
    '''
    form_model = 'player'
    form_fields = ['id_choice_01']

    def is_displayed(self):
        return self.player.treatment == "choice_wl"

    def vars_for_template(self):
        if self.player.id_in_group == 1:
            return {'wl_1': Constants.label_winner, 'wl_2': Constants.label_loser}
        else:
            return {'wl_1': Constants.label_loser, 'wl_2': Constants.label_winner}


class IdentityWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_label()


class NormalWaitPage(WaitPage):
    pass


class ShowLabel(Page):

    def vars_for_template(self):
        return {
            'choice_self': self.player.id_choice_01,
            'choice_partner': self.player.get_others_in_group()[0].id_choice_01,

            'label_self': self.player.label,
            'label_partner': self.player.get_others_in_group()[0].label,

            'correct_self': self.player.correct,
            'correct_partner': self.player.get_others_in_group()[0].correct,

            'is_compete': is_treatment_compete(self),
        }


class CoordinationTest(Page):
    pass


class CoordinationChoice01(Page):
    form_model = 'player'
    form_fields = ['co_choice_01']

    def vars_for_template(self):
        return {
            'role1_get': 400,
            'role2_get': 200,
        }


class CoordinationChoice02(Page):
    form_model = 'player'
    form_fields = ['co_choice_02']

    def vars_for_template(self):
        return {
            'role1_get': 500,
            'role2_get': 100,
        }


class CoordinationChoice03(Page):
    form_model = 'player'
    form_fields = ['co_choice_03']

    def vars_for_template(self):
        return {
            'role1_get': 300,
            'role2_get': 300,
        }


class CoordinationChoice04(Page):
    form_model = 'player'
    form_fields = ['co_choice_04']

    def vars_for_template(self):
        return {
            'role1_get': 450,
            'role2_get': 150,
        }


class CoordinationChoice05(Page):
    form_model = 'player'
    form_fields = ['co_choice_05']

    def vars_for_template(self):
        return {
            'role1_get': 350,
            'role2_get': 250,
        }


class CoordinationResult(Page):
    pass


class Introduction(Page):
    pass


class IdentityCompeteGame(Page):
    form_model = 'player'
    form_fields = ['correct']

    def is_displayed(self):
        return is_treatment_compete(self)

    def get_timeout_seconds(self):
        return self.session.config['game_time_sec']


class IdentityCompeteIntro(Page):
    def is_displayed(self):
        return is_treatment_compete(self)

    def vars_for_template(self):
        m, s = divmod(self.session.config['game_time_sec'], 60)
        h, m = divmod(m, 60)
        if m > 0:
            return {
                'timeout_string': ("%02d分%02d秒" % (m, s)),
                'correct_threshold': self.session.vars['correct_threshold']
            }
        else:
            return {
                'timeout_string': ("%02d秒" % (s)),
                'correct_threshold': self.session.vars['correct_threshold']
            }


def is_treatment_compete(page):
    return (page.player.treatment == "compete_wl") or (page.player.treatment == "compete_wl_color")


class Survey01(Page):
    pass


class Survey02(Page):
    form_model = 'player'
    form_fields = ['sur_q01', 'sur_q02', 'sur_q03', 'sur_q04',
                   'sur_q05', 'sur_q06', 'sur_q07', 'sur_q08']


class Survey03(Page):
    form_model = 'player'
    form_fields = ['sur_birth_year', 'sur_birth_month', 'sur_gender',
                   'sur_grade', 'sur_school', 'sur_party_member', 'sur_student_leader',
                   'sur_project_01', 'sur_project_02', 'sur_project_03', 'sur_project_04',
                   'sur_project_05', ]


page_sequence = [

    Introduction,
    IdentityChoiceColor,
    IdentityChoiceWl,

    IdentityCompeteIntro,
    IdentityCompeteGame,

    IdentityWaitPage,
    ShowLabel,

    NormalWaitPage,
    CoordinationTest,
    CoordinationChoice01,
    CoordinationChoice02,
    CoordinationChoice03,
    CoordinationChoice04,
    CoordinationChoice05,
    CoordinationResult,

    Survey01,
    Survey02,
    Survey03,
    ResultsWaitPage,
    Results
]
