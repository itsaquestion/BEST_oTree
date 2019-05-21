
import random
from words_game.utils import csv2odict
import os
from django.conf import settings

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Li Weicheng'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'words_game'
    players_per_group = 2
    num_rounds = 1

    words_numbers_47 = csv2odict("words_game" + os.path.sep + "words_numbers_47.csv")
    words_numbers_03 = csv2odict("words_game" + os.path.sep + "words_numbers_03.csv")

    dict_size = words_numbers_47.__len__()

    timeout_game_sec = 180
    timeout_game_min = timeout_game_sec / 60

    is_debug = settings.DEBUG
    # is_debug = False

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    def set_payoffs_01(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        # record partners
        p1.partner_01 = p2.participant.id_in_session
        p2.partner_01 = p1.participant.id_in_session

        # default value
        p1.profit_01 = p1.correct_01
        p2.profit_01 = p2.correct_01

        p1.result_01 = "平局"
        p2.result_01 = "平局"

        # if there is a winner
        if p1.correct_01 != p2.correct_01:
            winner = None
            loser = None
            if p1.correct_01 > p2.correct_01:
                winner = p1
                loser = p2

            if p1.correct_01 < p2.correct_01:
                winner = p2
                loser = p1

            winner.result_01 = "胜利"
            loser.result_01 = "失败"

            # winner gets double
            winner.profit_01 = winner.correct_01 * 2
            loser.profit_01 = 0

    def random_show_result_01(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        p1.show_result_01 = True
        p2.show_result_01 = True

        # random show winner information
        if random.randint(1, 3) == 1:
            p1.show_result_01 = False

        if random.randint(1, 3) == 1:
            p2.show_result_01 = False

    def set_payoffs_02(self):
        '''
        自己和自己玩，不用对比
        :return:
        '''
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        # default value
        p1.profit_02 = 0
        p2.profit_02 = 0

        if p1.correct_02 >= p1.target_02:
            p1.profit_02 = p1.correct_02

        if p2.correct_02 >= p2.target_02:
            p2.profit_02 = p2.correct_02


    def set_payoffs_03(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        # record partners
        p1.partner_03 = p2.participant.id_in_session
        p2.partner_03 = p1.participant.id_in_session

        # default value
        p1.profit_03 = p1.correct_03
        p2.profit_03 = p2.correct_03

        p1.result_03 = "平局"
        p2.result_03 = "平局"

        # if there is a winner
        if p1.correct_03 != p2.correct_03:
            winner = None
            loser = None
            if p1.correct_03 > p2.correct_03:
                winner = p1
                loser = p2

            if p1.correct_03 < p2.correct_03:
                winner = p2
                loser = p1

            winner.result_03 = "胜利"
            loser.result_03 = "失败"

            if winner.will_compete_03:
                winner.profit_03 = winner.correct_03 * 2

            if loser.will_compete_03:
                loser.profit_03 = 0


class Player(BasePlayer):
    student_id = models.PositiveIntegerField()

    # 第一次
    total_01 = models.PositiveIntegerField()
    correct_01 = models.PositiveIntegerField()
    result_01 = models.CharField(
        choices=[
            '胜利',
            '平局',
            '失败',
        ],
        widget=widgets.RadioSelect
    )
    show_result_01 = models.BooleanField()
    profit_01 = models.PositiveIntegerField()
    guess_win_01 = models.CharField(
        choices=[
            '胜利',
            '平局',
            '失败',
        ],
        widget=widgets.RadioSelect
    )
    partner_01 = models.CharField()

    # 第二次是自己和自己玩
    target_02 = models.PositiveIntegerField()
    total_02 = models.PositiveIntegerField()
    correct_02 = models.PositiveIntegerField()
    profit_02 = models.PositiveIntegerField()

    # 第三次
    will_compete_03 = models.BooleanField(
        choices=[
            [True, "进行比赛"],
            [False, "不进行比赛"],
        ]
    )
    partner_03 = models.CharField()

    total_03 = models.PositiveIntegerField()
    correct_03 = models.PositiveIntegerField()
    result_03 = models.CharField(
        choices=[
            '胜利',
            '平局',
            '失败',
        ],
        widget=widgets.RadioSelect
    )
    # show_result_03 = models.BooleanField()
    profit_03 = models.PositiveIntegerField()

    # 结果
    pay_round = models.PositiveIntegerField()

    def set_final_payoff(self):
        self.pay_round = random.randint(1, 3)

        if self.pay_round == 1:
            self.payoff = self.profit_01
        if self.pay_round == 2:
            self.payoff = self.profit_02
        if self.pay_round == 3:
            self.payoff = self.profit_03


