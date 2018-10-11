
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from words_game.utils import csv2odict


class Intro00(Page):
    pass


class Demo(Page):
    pass


class Intro01(Page):
    pass


class Intro02(Page):
        pass

class Intro03(Page):
        pass


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.group_randomly()


class Game01(Page):
    form_model = models.Player
    form_fields = ['correct_01','total_01']

    def get_timeout_seconds(self):
        return self.session.config['game_time_sec']

class Game02(Page):
    form_model = models.Player
    form_fields = ['correct_02','total_02']

    def get_timeout_seconds(self):
        return self.session.config['game_time_sec']


class Game03(Page):
    form_model = models.Player
    form_fields = ['correct_03','total_03']

    def get_timeout_seconds(self):
        return self.session.config['game_time_sec']


class Results01WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_01()
        self.group.random_show_result_01()


class Results02WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_02()


class Results03WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_03()


class Results01(Page):
    pass


class ResultsFinal(Page):
    pass


class Practice(Page):
    #timeout_seconds = models.Constants.timeout_practice
    pass


class IntroProcess(Page):
    pass


class Question01(Page):
    form_model = models.Player
    form_fields = ['guess_win_01']


class Question02(Page):
    form_model = models.Player
    form_fields = ['target_02']


class Question03p1(Page):
    form_model = models.Player
    form_fields = ['will_compete_03']


class Question03p2(Page):
    form_model = models.Player
    form_fields = ['accomplish_02']


class Question03p3(Page):
    form_model = models.Player
    form_fields = ['guess_win_03']

    def before_next_page(self):
        self.player.set_final_payoff()


class BlankPage(Page):
    pass


class PracticeFinish(Page):
    pass


page_sequence = [

    Intro00,        # 01-

    Practice,       # 02-
    PracticeFinish,
    IntroProcess,   # 03-

    #Game 1
    Intro01,        # 04-
    Game01,         # 05-
    BlankPage,
    Question01,     # 06-
    BlankPage,
    Results01WaitPage,

    Results01,      # 07-


    # Game 2
    ShuffleWaitPage,
    Intro02,        # 08
    Question02,
    BlankPage,
    Game02,         # 09
    Results02WaitPage,


    # Game 3
    ShuffleWaitPage,
    BlankPage,
    Intro03,        # 10
    Question03p1,
    BlankPage,
    Game03,         # 11
    Results03WaitPage,

    BlankPage,
    Question03p2,
    BlankPage,

    Question03p3,  # 012
    BlankPage,
    ResultsFinal    # 13
]
