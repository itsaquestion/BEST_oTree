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
        # 1,11,21轮换treatment + 组内

        # 11轮和21轮，组内乱序。其余按上一轮。
        if self.round_number in [11, 21]:
            gm = self.get_group_matrix()
            new_gm = oh.shuffle_in_groups(gm)
            self.set_group_matrix(new_gm)

        elif self.round_number > 1:
            self.group_like_round(self.round_number - 1)

        # 先定义每个组的treatment = treatment_list
        # 5轮swap，10轮shift(2)
        treatment_list: List[str] = ['corp_1', 'corp_3', 'corp_3']

        gs: List[Group] = self.get_groups()

        t1 = 'corp'
        t2 = 'res'

        if self.round_number in range(1, 6):
            # 1 ~ 5：原版
            apply_treatment(gs, treatment_list)

        elif self.round_number in range(6, 11):
            # 6 ~ 10：原版 + 对换产权
            apply_treatment(gs, oh.swap_str(treatment_list, t1, t2))

        elif self.round_number in range(11, 16):
            # 11 ~ 15：原版 + 平移1格
            apply_treatment(gs, oh.shift(treatment_list, 1))

        elif self.round_number in range(16, 21):
            # 11 ~ 15：原版 + 平移1格 + 对换产权
            apply_treatment(gs, oh.swap_str(oh.shift(treatment_list, 1), t1, t2))

        elif self.round_number in range(21, 26):
            # 21 ~ 25：原版 + 平移2格
            apply_treatment(gs, oh.shift(treatment_list, 2))
        else:
            # 26 ~ ：原版 + 平移2格 + 对换产权
            apply_treatment(gs, oh.swap_str(oh.shift(treatment_list, 2), t1, t2))


        # 把role保存起来
        for p in self.get_players():
            p.the_role = p.role()

        # 保留角色重排
        if self.round_number in [6, 16, 26]:
            gm = self.get_group_matrix()
            new_gm = oh.shuffle_in_groups_by_role(gm, "res")
            self.set_group_matrix(new_gm)

        # 生成GID
        for gid, g in enumerate(gs):
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


def apply_treatment(gs: List[Group], treatment_list: List[str]):
    for gid, g in enumerate(gs):
        set_treatment(g, treatment_list[gid])


def set_treatment(g: Group, treatment: str):
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
