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
    form_model = models.Player
    form_fields = ['intro_q1', 'intro_q2']


class Intro03(Page):
    pass


class Intro04(Page):
    form_model = models.Player
    form_fields = ['intro_q1', 'intro_q2']


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.group_randomly()


class Game01(Page):
    form_model = models.Player
    form_fields = ['correct_01', 'total_01']

    def get_timeout_seconds(self):
        return self.session.config['game_time_sec']


class Game02(Page):
    form_model = models.Player
    form_fields = ['g2_q{}'.format(int(i)) for i in range(1, 11)]


class Game03(Page):
    form_model = models.Player
    form_fields = ['correct_03', 'total_03']

    def get_timeout_seconds(self):
        return self.session.config['game_time_sec']


class Game04(Page):
    form_model = models.Player
    form_fields = ['g4_q{}'.format(int(i)) for i in range(1, 11)]


class Results01WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_01()
        # self.group.random_show_result_01()


class Results02WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_02()


class Results04WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_04()


class Results03WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_03()


class Results01(Page):
    pass


class Results02(Page):
    pass


class Results03(Page):
    pass


class Results04(Page):
    def before_next_page(self):
        self.player.set_final_payoff()

    pass


class ResultsFinal(Page):
    pass


class Practice(Page):
    # timeout_seconds = models.Constants.timeout_practice
    pass


class IntroProcess(Page):
    pass


class Send01(Page):
    pass


class Send03(Page):
    pass


class Question01(Page):
    form_model = models.Player
    form_fields = ['will_compete_01']


class Question03(Page):
    form_model = models.Player
    form_fields = ['will_compete_03']


# class Question03p2(Page):
#     form_model = models.Player
#     form_fields = ['accomplish_02']
#
#
# class Question03p3(Page):
#     form_model = models.Player
#     form_fields = ['guess_win_03']
#
#     def before_next_page(self):
#         self.player.set_final_payoff()


class BlankPage(Page):
    pass


class eprime01(Page):
    pass

class eprime02(Page):
    pass

class PracticeFinish(WaitPage):
    wait_for_all_groups = True


class WaitForAll(WaitPage):
    wait_for_all_groups = True


page_sequence = [


    # start
    IntroProcess,  # 03-

    Intro00,  # 01-
    Practice,  # 02-
    PracticeFinish,

    # Game 1
    Intro01,  # 04-
    Question01,
    WaitForAll,
    Send01,
    Game01,  # 05-
    Results01WaitPage,
    Results01,  # 07-

    # Game 2
    ShuffleWaitPage,
    Intro02,  # 08
    Game02,  # 09
    Results02WaitPage,
    Results02,

    # Game 3
    ShuffleWaitPage,
    eprime01,
    Intro03,  # 10
    Question03,
    WaitForAll,
    Send03,
    Game03,  # 11
    Results03WaitPage,
    Results03,

    # Game 4
    ShuffleWaitPage,
    Intro04,  # 08
    Game04,  # 09
    Results04WaitPage,
    Results04,
    eprime02,
    ResultsFinal  # 13
]
