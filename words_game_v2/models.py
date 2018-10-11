
import random
from words_game_v2.utils import csv2odict
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
    name_in_url = 'preference_separation'
    players_per_group = 2
    num_rounds = 1

    dict_01 = csv2odict(name_in_url + os.path.sep + "dicts" + os.path.sep + "dict_01.csv")
    dict_02 = csv2odict(name_in_url + os.path.sep + "dicts" + os.path.sep + "dict_02.csv")
    dict_03 = csv2odict(name_in_url + os.path.sep + "dicts" + os.path.sep + "dict_03.csv")
    dict_p = csv2odict(name_in_url + os.path.sep + "dicts" + os.path.sep + "dict_p.csv")

    # dict_size = words_numbers_47.__len__()

    # timeout_game_sec = 90
    # timeout_game_min = timeout_game_sec / 60


class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly()
        self.session.vars['is_debug'] = self.session.config['debug_mode']
        self.session.vars['points_for_one_yuan'] = self.session.config['points_for_one_yuan']
        self.session.vars['game_time_sec'] = self.session.config['game_time_sec']
        self.session.vars['game_time_min'] = self.session.vars['game_time_sec'] / 60

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

        p1.result_01 = "一样多"
        p2.result_01 = "一样多"

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

            winner.result_01 = "赢了"
            loser.result_01 = "输了"

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
            p1.profit_02 = p1.target_02

        if p2.correct_02 >= p2.target_02:
            p2.profit_02 = p2.target_02


    def set_payoffs_03(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        # record partners
        p1.partner_03 = p2.participant.id_in_session
        p2.partner_03 = p1.participant.id_in_session

        # default value
        p1.profit_03 = p1.correct_03
        p2.profit_03 = p2.correct_03

        p1.result_03 = "一样多"
        p2.result_03 = "一样多"

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

            winner.result_03 = "赢了"
            loser.result_03 = "输了"

            if winner.will_compete_03:
                winner.profit_03 = winner.correct_03 * 2

            if loser.will_compete_03:
                loser.profit_03 = 0


class Player(BasePlayer):

    # 第一次
    total_01 = models.PositiveIntegerField()
    correct_01 = models.PositiveIntegerField()
    result_01 = models.CharField(
        choices=[
            '赢了',
            '一样多',
            '输了',
        ],
        widget=widgets.RadioSelect
    )
    show_result_01 = models.BooleanField()
    profit_01 = models.PositiveIntegerField()
    guess_win_01 = models.CharField(
        choices=[
            ['赢了', '赢了 (数字键 1)'],
            ['一样多', '一样多 (数字键 2)'],
            ['输了', '输了 (数字键 3)']
        ],
        widget=widgets.RadioSelect
    )
    partner_01 = models.CharField()

    # 第二次是自己和自己玩
    target_02 = models.PositiveIntegerField()
    total_02 = models.PositiveIntegerField()
    correct_02 = models.PositiveIntegerField()
    profit_02 = models.PositiveIntegerField()
    accomplish_02 = models.BooleanField(
        choices=[
            [True, "完成了目标 (数字键 1)"],
            [False, "没有完成目标 (数字键 2)"],
        ]
    )

    # 第三次
    will_compete_03 = models.BooleanField(
        choices=[
            [True, "比赛 (数字键 1)"],
            [False, "不比赛 (数字键 2)"],
        ]
    )
    partner_03 = models.CharField()

    total_03 = models.PositiveIntegerField()
    correct_03 = models.PositiveIntegerField()
    result_03 = models.CharField(
        choices=[
            '赢了',
            '一样多',
            '输了',
        ],
        widget=widgets.RadioSelect
    )
    guess_win_03 = models.CharField(
        choices=[
            ['赢了', '赢了 (数字键 1)'],
            ['一样多', '一样多 (数字键 2)'],
            ['输了', '输了 (数字键 3)']
        ],
        widget=widgets.RadioSelect
    )
    profit_03 = models.PositiveIntegerField()
    profit_final = models.PositiveIntegerField()

    # 结果
    pay_round = models.PositiveIntegerField()

    payoff_plus_fee = models.CurrencyField()

    def set_final_payoff(self):
        self.pay_round = random.randint(1, 3)

        pfo = self.session.vars['points_for_one_yuan']
        if self.pay_round == 1:
            self.profit_final = self.profit_01
            self.payoff = self.profit_01 / pfo
        if self.pay_round == 2:
            self.profit_final = self.profit_02
            self.payoff = self.profit_02 / pfo
        if self.pay_round == 3:
            self.profit_final = self.profit_03
            self.payoff = self.profit_03 / pfo

        self.payoff_plus_fee = self.payoff + self.session.config['participation_fee']

