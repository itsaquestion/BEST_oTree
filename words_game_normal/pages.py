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


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_result()


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


class Rest(Page):
    def get_timeout_seconds(self):
        return get_rest_time(self)


class Practice(Page):
    form_model = 'player'
    form_fields = ['correct_p', 'total_p']

    def get_timeout_seconds(self):
        return get_game_time(self)

    def is_displayed(self):
        return self.round_number == 1



page_sequence = [
    Intro,
    Practice,
    BeginWaitPage,
    Game01,
    RestWaitPage,
    Rest,
    Game02,
    ResultsWaitPage,
    Results
]
