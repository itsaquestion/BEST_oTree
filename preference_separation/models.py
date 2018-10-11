
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
    timeout_practice = 30


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        self.session.vars['is_debug'] = self.session.config['debug_mode']
        self.session.vars['points_for_one_yuan'] = self.session.config['points_for_one_yuan']
        self.session.vars['game_time_sec'] = self.session.config['game_time_sec']
        self.session.vars['game_time_min'] = self.session.vars['game_time_sec'] / 60
        self.session.vars['fee'] = self.session.config['participation_fee']


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

        winner = None
        loser = None

        # 选出胜利和失败者，即使选择了不比赛
        if p1.correct_01 != p2.correct_01:
            # if there is a winner
            if p1.correct_01 > p2.correct_01:
                winner = p1
                loser = p2

            if p1.correct_01 < p2.correct_01:
                winner = p2
                loser = p1
        else:
            # no winner , pick one
            if random.random() < 0.5:
                winner = p1
                loser = p2
            else:
                winner = p2
                loser = p1

        winner.result_01 = "赢了"
        loser.result_01 = "输了"

        # winner gets double
        if winner.will_compete_01:
            winner.profit_01 = winner.correct_01 * 2
        else:
            winner.profit_01 = winner.correct_01

        if loser.will_compete_01:
            loser.profit_01 = 0
        else:
            loser.profit_01 = loser.correct_01



    # def random_show_result_01(self):
    #     p1 = self.get_player_by_id(1)
    #     p2 = self.get_player_by_id(2)
    #
    #     p1.show_result_01 = True
    #     p2.show_result_01 = True
    #
    #     # random show winner information
    #     if random.randint(1, 3) == 1:
    #         p1.show_result_01 = False
    #
    #     if random.randint(1, 3) == 1:
    #         p2.show_result_01 = False

    def set_payoffs_02(self):
        '''
        自己和自己玩，不用对比
        :return:
        '''
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        p1.set_payoff_02()
        p2.set_payoff_02()

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

        winner = None
        loser = None

        if p1.correct_03 != p2.correct_03:
            # if there is a winner
            if p1.correct_03 > p2.correct_03:
                winner = p1
                loser = p2

            if p1.correct_03 < p2.correct_03:
                winner = p2
                loser = p1

        else:
            # no winner , pick one
            if random.random() < 0.5:
                winner = p1
                loser = p2
            else:
                winner = p2
                loser = p1

        winner.result_03 = "赢了"
        loser.result_03 = "输了"

        # winner gets double
        if winner.will_compete_03:
            winner.profit_03 = winner.correct_03 * 2
        else:
            winner.profit_03 = winner.correct_03

        if loser.will_compete_03:
            loser.profit_03 = 0
        else:
            loser.profit_03 = loser.correct_03

    def set_payoffs_04(self):
        '''
        自己和自己玩，不用对比
        :return:
        '''
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        p1.set_payoff_04()
        p2.set_payoff_04()


def option_a(amount):
    """O 1/10的概率获得20元，9/10的概率获得16元"""
    s = '{n1}/10的概率获得20元， {n2}/10的概率获得16元；'
    return s.format(n1=amount, n2=10 - amount)


def option_b(amount):
    s = '{n1}/10的概率获得38.5元， {n2}/10的概率获得1元；'
    return s.format(n1=amount, n2=10 - amount)


class Player(BasePlayer):

    # Game 1
    will_compete_01 = models.BooleanField(
        choices=[
            [True, "比赛"],
            [False, "不比赛"],
        ],
        widget=widgets.RadioSelect
    )

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
    # show_result_01 = models.BooleanField()
    profit_01 = models.CurrencyField()
    # guess_win_01 = models.CharField(
    #     choices=[
    #         ['赢了', '赢了 (数字键 1)'],
    #         ['一样多', '一样多 (数字键 2)'],
    #         ['输了', '输了 (数字键 3)']
    #     ],
    #     widget=widgets.RadioSelect
    # )
    partner_01 = models.CharField()


    # 临时问题

    intro_q1 = models.IntegerField(choices=[[1, "10对全部支付"], [2, "随机选择其中一对支付"], ], widget=widgets.RadioSelectHorizontal)
    intro_q2 = models.IntegerField(choices=[[1, "确定m元"], [2, "确定n元"], [3, "m元或n元，由计算机根据它们的概率随机决定"],], widget=widgets.RadioSelectHorizontal)

    # Game 2
    g2_q1 = models.CharField(choices=[["A", option_a(1)], ["B", option_b(1)], ], widget=widgets.RadioSelectHorizontal)
    g2_q2 = models.CharField(choices=[["A",option_a(2)], ["B", option_b(2)], ], widget=widgets.RadioSelectHorizontal)
    g2_q3 = models.CharField(choices=[["A",option_a(3)], ["B", option_b(3)], ], widget=widgets.RadioSelectHorizontal)
    g2_q4 = models.CharField(choices=[["A",option_a(4)], ["B", option_b(4)], ], widget=widgets.RadioSelectHorizontal)
    g2_q5 = models.CharField(choices=[["A",option_a(5)], ["B", option_b(5)], ], widget=widgets.RadioSelectHorizontal)
    g2_q6 = models.CharField(choices=[["A",option_a(6)], ["B", option_b(6)], ], widget=widgets.RadioSelectHorizontal)
    g2_q7 = models.CharField(choices=[["A",option_a(7)], ["B", option_b(7)], ], widget=widgets.RadioSelectHorizontal)
    g2_q8 = models.CharField(choices=[["A",option_a(8)], ["B", option_b(8)], ], widget=widgets.RadioSelectHorizontal)
    g2_q9 = models.CharField(choices=[["A",option_a(9)], ["B", option_b(9)], ], widget=widgets.RadioSelectHorizontal)
    g2_q10 = models.CharField(choices=[["A",option_a(10)], ["B", option_b(10)], ], widget=widgets.RadioSelectHorizontal)


    # 选择哪个选项作为给钱的选项
    payoff_02_num = models.PositiveIntegerField()
    profit_02 = models.CurrencyField()
    ans_02 =  models.CharField()

    def set_payoff_02_by_num(self, ans):
        print(ans)
        if ans == "A":
            if random.random() < (self.payoff_02_num / 10):
                self.profit_02 = 20
            else:
                self.profit_02 = 16

        if ans == "B":
            if random.random() < (self.payoff_02_num / 10):
                self.profit_02 = 38.5
            else:
                self.profit_02 = 1

    def set_payoff_02(self):
        """从1到10中随机选择一个，作为给钱的答案"""
        self.payoff_02_num = random.randint(1, 10)
        if self.payoff_02_num == 1:
            ans = self.g2_q1
        if self.payoff_02_num == 2:
            ans = self.g2_q2
        if self.payoff_02_num == 3:
            ans = self.g2_q3
        if self.payoff_02_num == 4:
            ans = self.g2_q4
        if self.payoff_02_num == 5:
            ans = self.g2_q5
        if self.payoff_02_num == 6:
            ans = self.g2_q6
        if self.payoff_02_num == 7:
            ans = self.g2_q7
        if self.payoff_02_num == 8:
            ans = self.g2_q8
        if self.payoff_02_num == 9:
            ans = self.g2_q9
        if self.payoff_02_num == 10:
            ans = self.g2_q10

        self.ans_02 = ans
        self.set_payoff_02_by_num(ans)

    # Game 3
    will_compete_03 = models.BooleanField(
        choices=[
            [True, "比赛"],
            [False, "不比赛"],
        ],
        widget=widgets.RadioSelect
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
    # guess_win_03 = models.CharField(
    #     choices=[
    #         ['赢了', '赢了 (数字键 1)'],
    #         ['一样多', '一样多 (数字键 2)'],
    #         ['输了', '输了 (数字键 3)']
    #     ],
    #     widget=widgets.RadioSelect
    # )
    profit_03 = models.CurrencyField()

    # Game 4
    g4_q1 = models.CharField(choices=[["A",option_a(1)], ["B", option_b(1)], ], widget=widgets.RadioSelectHorizontal)
    g4_q2 = models.CharField(choices=[["A",option_a(2)], ["B", option_b(2)], ], widget=widgets.RadioSelectHorizontal)
    g4_q3 = models.CharField(choices=[["A",option_a(3)], ["B", option_b(3)], ], widget=widgets.RadioSelectHorizontal)
    g4_q4 = models.CharField(choices=[["A",option_a(4)], ["B", option_b(4)], ], widget=widgets.RadioSelectHorizontal)
    g4_q5 = models.CharField(choices=[["A",option_a(5)], ["B", option_b(5)], ], widget=widgets.RadioSelectHorizontal)
    g4_q6 = models.CharField(choices=[["A",option_a(6)], ["B", option_b(6)], ], widget=widgets.RadioSelectHorizontal)
    g4_q7 = models.CharField(choices=[["A",option_a(7)], ["B", option_b(7)], ], widget=widgets.RadioSelectHorizontal)
    g4_q8 = models.CharField(choices=[["A",option_a(8)], ["B", option_b(8)], ], widget=widgets.RadioSelectHorizontal)
    g4_q9 = models.CharField(choices=[["A",option_a(9)], ["B", option_b(9)], ], widget=widgets.RadioSelectHorizontal)
    g4_q10 = models.CharField(choices=[["A",option_a(10)], ["B", option_b(10)], ], widget=widgets.RadioSelectHorizontal)

    # 选择哪个选项作为给钱的选项
    payoff_04_num = models.PositiveIntegerField()
    profit_04 = models.CurrencyField()
    ans_04 = models.CharField()

    def set_payoff_04_by_num(self, ans):
        print(ans)
        if ans == "A":
            if random.random() < (self.payoff_04_num / 10):
                self.profit_04 = 20
            else:
                self.profit_04 = 16

        if ans == "B":
            if random.random() < (self.payoff_04_num / 10):
                self.profit_04 = 38.5
            else:
                self.profit_04 = 1

    def set_payoff_04(self):
        """从1到10中随机选择一个，作为给钱的答案"""
        self.payoff_04_num = random.randint(1, 10)
        if self.payoff_04_num == 1:
            ans = self.g4_q1
        if self.payoff_04_num == 2:
            ans = self.g4_q2
        if self.payoff_04_num == 3:
            ans = self.g4_q3
        if self.payoff_04_num == 4:
            ans = self.g4_q4
        if self.payoff_04_num == 5:
            ans = self.g4_q5
        if self.payoff_04_num == 6:
            ans = self.g4_q6
        if self.payoff_04_num == 7:
            ans = self.g4_q7
        if self.payoff_04_num == 8:
            ans = self.g4_q8
        if self.payoff_04_num == 9:
            ans = self.g4_q9
        if self.payoff_04_num == 10:
            ans = self.g4_q10

        self.ans_04 = ans
        self.set_payoff_04_by_num(ans)

    #profit_final = models.PositiveIntegerField()

    # 结果
    pay_round_01 = models.PositiveIntegerField()
    pay_round_02 = models.PositiveIntegerField()

    payoff_plus_fee = models.CurrencyField()

    def set_final_payoff(self):
        self.pay_round_01 = [1, 2][random.randint(0, 1)]
        self.pay_round_02 = [1, 2][random.randint(0, 1)]

        self.payoff = 0
        #pfo = self.session.vars['points_for_one_yuan']
        if self.pay_round_01 == 1:
            self.payoff = self.payoff + self.profit_01

        if self.pay_round_01 == 2:
            self.payoff = self.payoff + self.profit_03

        if self.pay_round_02 == 1:
            self.payoff = self.payoff + self.profit_02

        if self.pay_round_02 == 2:
            self.payoff = self.payoff + self.profit_04

        self.payoff_plus_fee = self.payoff + self.session.config['participation_fee']

