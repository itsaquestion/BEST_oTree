
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
    def before_next_page(self):
        # models.Constants.words_numbers = csv2odict("words_game/words_numbers_100.csv")
        pass


class Intro02(Page):
    form_model = models.Player
    form_fields = ['target_02']
    def before_next_page(self):
        # models.Constants.words_numbers = csv2odict("words_game/words_numbers_100.csv")
        pass


class Intro03(Page):
    form_model = models.Player
    form_fields = ['will_compete_03']
    def before_next_page(self):
        # models.Constants.words_numbers = csv2odict("words_game/words_numbers_100.csv")
        pass


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.group_randomly()


class Game01(Page):
    timeout_seconds = models.Constants.timeout_game_sec
    form_model = models.Player
    form_fields = ['correct_01','total_01']

    def before_next_page(self):
        pass


class Game02(Page):
    timeout_seconds = models.Constants.timeout_game_sec
    form_model = models.Player
    form_fields = ['correct_02','total_02']

    def before_next_page(self):
        pass


class Game03(Page):
    timeout_seconds = models.Constants.timeout_game_sec
    form_model = models.Player
    form_fields = ['correct_03','total_03']

    def before_next_page(self):
        pass


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


class IntroPayment(Page):
    pass


class Guess01(Page):
    form_model = models.Player
    form_fields = ['guess_win_01']


class InputId(Page):
    form_model = models.Player
    form_fields = ['student_id']

    def before_next_page(self):
        self.player.set_final_payoff()


page_sequence = [

    Intro00,        # 01-

    Practice,       # 02-
    IntroPayment,   # 03-

    # Game 1
    Intro01,        # 04-
    Game01,         # 05-
    Guess01,        # 06-
    Results01WaitPage,

    Results01,      # 07-

    # Game 2
    ShuffleWaitPage,
    Intro02,        # 08
    Game02,         # 09
    Results02WaitPage,
    #Results02,

    # Game 3
    ShuffleWaitPage,
    Intro03,        # 10
    Game03,         # 11
    Results03WaitPage,
    # Results03,

    # Final
    InputId,        # 12
    ResultsFinal    # 13
]
