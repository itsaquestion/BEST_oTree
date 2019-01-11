from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


def get_game_time(page: Page):
    if page.session.config['debug_mode']:
        return page.session.config['debug_play_sec']
    else:
        return page.session.config['game_play_sec']


def get_rest_time(page: Page):
    if page.session.config['debug_mode']:
        return page.session.config['debug_rest_sec']
    else:
        return page.session.config['game_rest_sec']


class Intro1(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'fix': self.session.config['fee'],
                'bonus': self.session.config['bonus']
                }


class Intro2(Page):
    def is_displayed(self):
        return self.round_number == 1


class Intro3(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'bonus': self.session.config['bonus']}


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_result()


class FinalResults(Page):
    def is_displayed(self):
        return self.round_number == 3

    def vars_for_template(self):
        round_1_player = self.player.in_round(1)
        round_2_player = self.player.in_round(2)
        round_3_player = self.player.in_round(3)
        return {'op_r1_correct': round_1_player.op_correct_final,
                'op_r2_correct': round_2_player.op_correct_final,
                'op_r3_correct': round_3_player.op_correct_final,
                'results_01': round_1_player.results_final,
                'results_02': round_2_player.results_final,
                'results_03': round_3_player.results_final,
                'r1_correct': round_1_player.correct_final,
                'r2_correct': round_2_player.correct_final,
                'r3_correct': round_3_player.correct_final,
                'payoff_final': self.player.in_round(self.player.pay_round).fee_final
                }


class Results(Page):
    pass


class Game01(Page):
    form_model = 'player'
    form_fields = ['correct_01', 'total_01']

    def get_timeout_seconds(self):
        return get_game_time(self)


class Game02(Page):
    form_model = 'player'
    form_fields = ['correct_02', 'total_02']

    def get_timeout_seconds(self):
        return get_game_time(self)


class BeginWaitPage(WaitPage):
    pass


class RestWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_result()


class PrepareHigh(Page):
    def is_displayed(self):
        return self.player.treatment == 'high'


class PrepareMid(Page):
    def is_displayed(self):
        return self.player.treatment == 'mid'


class PrepareLow(Page):
    def is_displayed(self):
        return self.player.treatment == 'low'


class RestLow(Page):
    def get_timeout_seconds(self):
        return get_rest_time(self)

    def is_displayed(self):
        return self.player.treatment == 'low'


class RestMid(Page):
    def get_timeout_seconds(self):
        return get_rest_time(self)

    def vars_for_template(self):
        if self.player.win_01 == 1:
            return {'rank': '领先'}
        elif self.player.win_01 == -1:
            return {'rank': '落后'}
        else:
            return {'rank': '与对手不相上下'}

    def is_displayed(self):
        return self.player.treatment == 'mid'


class RestHigh(Page):
    def get_timeout_seconds(self):
        return get_rest_time(self)

    def vars_for_template(self):
        if self.player.win_01 == 1:
            return {'feedback': '领先对手' + str(abs(self.player.correct_01-self.player.op_correct_01)) + '个汉字',
                    'op_wrong': self.player.op_wrong_01,
                    'op_correct': self.player.op_correct_01,
                    'dif': abs(self.player.correct_01-self.player.op_correct_01)}
        elif self.player.win_01 == -1:
            return {'feedback': '落后对手' + str(abs(self.player.correct_01-self.player.op_correct_01)) + '个汉字',
                    'op_wrong': self.player.op_wrong_01,
                    'op_correct': self.player.op_correct_01,
                    }
        else:
            return {'feedback': '与对手不相上下',
                    'op_wrong': self.player.op_wrong_01,
                    'op_correct': self.player.op_correct_01,
                   }

    def is_displayed(self):
        return self.player.treatment == 'high'


class Practice(Page):
    form_model = 'player'
    form_fields = ['correct_p', 'total_p']

    def get_timeout_seconds(self):
        return get_game_time(self)

    def is_displayed(self):
        return self.round_number == 1


class Survey(Page):
    form_model = 'player'
    form_fields = ['sur_gender', 'sur_birth_year', 'sur_nationality', 'sur_school', 'sur_grade', 'sur_computer_exp']

    def is_displayed(self):
        return self.round_number == 3


page_sequence = [
    Intro1,
    Intro2,
    Practice,
    Intro3,
    PrepareLow,
    PrepareMid,
    PrepareHigh,
    BeginWaitPage,
    Game01,
    RestWaitPage,
    RestLow,
    RestMid,
    RestHigh,
    Game02,
    ResultsWaitPage,
    Results,
    Survey,
    FinalResults
]
