from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import otree_helper as oh
from typing import List
import random

author = 'Li Weicheng'

doc = """
Coase Theory Test
"""


class Constants(BaseConstants):
    name_in_url = 'Coase'
    players_per_group = 8

    num_rounds: int = 30

    corp_endowment = 10
    corp_pollution = 15

    res_endowment = 10


class Subsession(BaseSubsession):
    def creating_session(self):

        # 11轮和21轮，组内乱序。其余按上一轮。
        if self.round_number in [11, 21]:
            gm = self.get_group_matrix()
            new_gm = oh.shuffle_in_groups(gm)
            self.set_group_matrix(new_gm)

        elif self.round_number > 1:
            self.group_like_round(self.round_number - 1)


        # 初始的treatment顺序列表，表示每个10轮的起始（G1）的treatment
        # 即：1，11，21轮开始的G1的treatment
        # 对于G2，G3等等，利用oh.shift()对这个treatment列表进行平移即可

        treatment_list_base: List[str] = ['corp_1', 'corp_3', 'corp_3']
        treatment_list_base_swap: List[str] = ['res_1', 'res_3', 'res_3']

        t1 = 'corp'
        t2 = 'res'

        g: Group
        for gid, g in enumerate(self.get_groups()):
            treatment_list = oh.shift(treatment_list_base, gid)
            treatment_list_swap = oh.shift(treatment_list_base_swap, gid)
            if self.round_number in range(1, 6):
                set_treatment(g, treatment_list[0])

            elif self.round_number in range(6, 11):
                set_treatment(g, treatment_list_swap[0])

            elif self.round_number in range(11, 16):
                set_treatment(g, treatment_list[1])

            elif self.round_number in range(16, 21):
                set_treatment(g, treatment_list_swap[1])

            elif self.round_number in range(21, 26):
                set_treatment(g, treatment_list[2])

            else:
                set_treatment(g, treatment_list_swap[2])

        # 把role保存起来
        for p in self.get_players():
            p.the_role = p.role()

        # 保留角色重排
        if self.round_number in [6, 16, 26]:
            gm = self.get_group_matrix()
            new_gm = oh.shuffle_in_groups_by_role(gm, "res")
            self.set_group_matrix(new_gm)

        # 生成GID
        for gid, g in enumerate(self.get_groups()):
            for p in g.get_players():
                p.gid = (gid + 1) * 10 + p.id_in_group


class Group(BaseGroup):
    treatment = models.StringField()

    # 无产权的一方出价，高于对方出价，则deal = True，以无产权方出价为准
    def set_payoff(self):
        if self.treatment == "corp_1":
            # 1v1，产权归企业
            # p1 vs p2, p3 vs p4
            self.get_player_by_id(1)

        if self.treatment == "corp_3":
            # 1v1，产权归企业
            # p1 vs p2, p3 vs p4
            res_price = sum(p.offer for p in self.get_players_by_role("res"))


def set_treatment(g: Group, treatment: str):
    """
    把treatment:str写入Group以及其下的Players的treatement属性里
    :param g: a Group
    :param treatment: the treatment string
    :return: none
    """
    g.treatment = treatment
    for p in g.get_players():
        p.treatment = treatment


def res_offer_field():
    # 居民offer，上限是居民endowment
    return models.IntegerField(min=0, max=Constants.res_endowment)


def corp_offer_field():
    # 企业offer，上限是企业endowment
    return models.IntegerField(min=0, max=Constants.corp_endowment)


class Player(BasePlayer):

    def role(self):
        # 1v1: p1、p3为企业
        # 1v3：p1为企业
        if self.treatment in ["corp_1", "res_1"]:
            if self.id_in_group in [1, 3, 5, 7]:
                return 'corp'
            else:
                return 'res'
        else:
            if self.id_in_group in [1, 5]:
                return 'corp'
            else:
                return 'res'

    # ========================================================
    # 控制变量
    # ========================================================

    treatment = models.StringField()

    gid = models.IntegerField()

    # ========================================================
    # 数据变量
    # ========================================================

    res_price = res_offer_field()
    corp_price = corp_offer_field()

    # 是否达成协议
    deal = models.BooleanField()

    # 保存角色
    the_role = models.StringField()