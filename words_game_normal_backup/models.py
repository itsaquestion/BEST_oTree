from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import otree_helper as oh
from typing import List
import random
import os
import words_game_normal.utils as utils

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'words_game_normal'
    players_per_group = 8
    num_rounds = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        #self.session.vars['debug_mode'] =

        path = "./words_game_normal/dicts/3500常用字.txt"
        self.session.vars['chars'] = utils.read_char_list(path)

        #定随机轮
        if self.round_number == 3:
            p: Player
            for p in self.get_players():
                p.pay_round = random.randrange(1, 3, 1)

        # 每轮都组内重新匹配
        gm = self.get_group_matrix()
        new_gm = oh.shuffle_in_groups(gm)
        self.set_group_matrix(new_gm)

        # 滚动设置treatment
        treatment_list_base: List = ['low', 'mid', 'high']
        g: Group
        for idg, g in enumerate(self.get_groups()):
            treatment_list = oh.shift(treatment_list_base, idg)
            g.set_treatment(treatment_list[(self.round_number % len(treatment_list_base)) - 1])


class Group(BaseGroup):
    treatment = models.StringField()

    def set_treatment(self, treatment):
        self.treatment = treatment
        p: Player
        for p in self.get_players():
            p.treatment = treatment

    def set_result(self):
        p:Player
        for p in self.get_players():
            my_id = p.id_in_group
            partner: Player
            if my_id % 2 == 0:
                partner = self.get_player_by_id(my_id - 1)
            else:
                partner = self.get_player_by_id(my_id + 1)

            p.wrong_01 = p.total_01 - p.correct_01
            if p.correct_01 > partner.correct_01:
                p.win_01 = 1
            elif p.correct_01 <  partner.correct_01:
                p.win_01 = -1
            else:
                p.win_01 = 0

            p.wrong_02 = p.total_02 - p.correct_02
            if p.correct_02 > partner.correct_02:
                p.win_02 = 1
            elif p.correct_02 < partner.correct_02:
                p.win_02 = -1
            else:
                p.win_02 = 0

            p.correct_final = p.correct_01 + p.correct_02
            p.total_final = p.total_01 + p.total_02
            p.wrong_final = p.total_final - p.correct_final
            if p.correct_final > partner.correct_final:
                p.win_final = 1
            elif p.correct_final < partner.correct_final:
                p.win_final = -1
                p.results_final = '失败'
            else:
                if p.id_in_group > partner.id_in_group:
                    p.win_final = 1
                else:
                    p.win_final = -1

            if p.win_final == 1:
                p.results_final = '获胜'
                p.fee_final = p.session.config['fee'] + p.session.config['bonus']
            else:
                p.results_final = '失败'
                p.fee_final = p.session.config['fee']

            # 填入对手资料
            p.op_correct_01 = partner.correct_01
            p.op_correct_02 = partner.correct_02
            p.op_correct_final = partner.correct_final
            p.op_wrong_01 = partner.wrong_01
            p.op_wrong_02 = partner.wrong_02
            p.op_wrong_final = partner.wrong_final
            p.op_total_01 = partner.total_01
            p.op_total_02 = partner.total_02
            p.op_total_final = partner.total_final


class Player(BasePlayer):
    treatment = models.StringField()
    pay_round = models.IntegerField(initial=0)
    fee_final = models.IntegerField(initial=0)

    correct_p = models.IntegerField(initial=0)
    correct_01 = models.IntegerField(initial=0)
    correct_02 = models.IntegerField(initial=0)
    correct_final = models.IntegerField(initial=0)

    total_p = models.IntegerField(initial=0)
    total_01 = models.IntegerField(initial=0)
    total_02 = models.IntegerField(initial=0)
    total_final = models.IntegerField(initial=0)

    wrong_01 = models.IntegerField(initial=0)
    wrong_02 = models.IntegerField(initial=0)
    wrong_final = models.IntegerField(initial=0)

    op_correct_p = models.IntegerField(initial=0)
    op_correct_01 = models.IntegerField(initial=0)
    op_correct_02 = models.IntegerField(initial=0)
    op_correct_final = models.IntegerField(initial=0)

    op_total_p = models.IntegerField(initial=0)
    op_total_01 = models.IntegerField(initial=0)
    op_total_02 = models.IntegerField(initial=0)
    op_total_final = models.IntegerField(initial=0)

    op_wrong_01 = models.IntegerField(initial=0)
    op_wrong_02 = models.IntegerField(initial=0)
    op_wrong_final = models.IntegerField(initial=0)

    win_01 = models.IntegerField()
    win_02 = models.IntegerField()
    win_final = models.IntegerField()
    results_final= models.StringField()
    # 问卷
    sur_gender = models.StringField(
        choices=['男', '女'],
        verbose_name="你的性别是",
        widget=widgets.RadioSelectHorizontal
    )

    sur_birth_year = models.IntegerField(
        verbose_name="你的年龄是"
    )

    sur_nationality = models.StringField(
        verbose_name="你的民族是"
    )
    sur_school = models.StringField(
        verbose_name="你就读的学院为"
    )

    sur_grade = models.StringField(
        choices=['大一', '大二', '大三', '大四', '研一', '研二'],
        verbose_name="你就读的年级为",
        widget=widgets.RadioSelectHorizontal
    )

    sur_computer_exp =models.IntegerField(
        choices=['非常不熟练', '不熟练', '一般', '熟练', '非常熟练'],
        verbose_name="请问你打字的熟练程度是",
        widget=widgets.RadioSelectHorizontal
    )
