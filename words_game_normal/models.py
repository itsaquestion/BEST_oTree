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

            if p.correct_01 > partner.correct_01:
                p.win_01 = 1
            elif p.correct_01 <  partner.correct_01:
                p.win_01 = -1
            else:
                p.win_01 = 0

            if p.correct_02 > partner.correct_02:
                p.win_02 = 1
            elif p.correct_02 < partner.correct_02:
                p.win_02 = -1
            else:
                p.win_02 = 0

            p.correct_final = p.correct_01 + p.correct_02
            p.total_final = p.total_01 + p.total_02
            if p.correct_final > partner.correct_final:
                p.win_final = 1
            elif p.correct_final < partner.correct_final:
                p.win_final = -1
            else:
                p.win_final = 0


class Player(BasePlayer):
    treatment = models.StringField()

    correct_p = models.IntegerField(initial=0)
    correct_01 = models.IntegerField(initial=0)
    correct_02 = models.IntegerField(initial=0)

    correct_final = models.IntegerField(initial=0)
    total_p = models.IntegerField(initial=0)
    total_01 = models.IntegerField(initial=0)
    total_02 = models.IntegerField(initial=0)
    total_final = models.IntegerField(initial=0)

    win_01 = models.IntegerField()
    win_02 = models.IntegerField()
    win_final = models.IntegerField()
