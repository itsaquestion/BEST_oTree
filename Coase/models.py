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

    res_endowment = 10


class Subsession(BaseSubsession):
    def creating_session(self):

        # =================================================================
        # 读取全局设置
        # =================================================================
        self.session.vars['is_debug'] = self.session.config['debug_mode']
        self.session.vars['points_for_one_yuan'] = self.session.config['points_for_one_yuan']
        self.session.vars['participation_fee'] = self.session.config['participation_fee']

        # =================================================================
        # 关键变量
        # =================================================================
        self.session.vars['high_value'] = self.session.config['high_value']
        self.session.vars['low_value'] = self.session.config['low_value']
        self.session.vars['high_value_one_third'] = round(self.session.vars['high_value'] / 3, 2)
        self.session.vars['low_value_one_third'] = round(self.session.vars['low_value'] / 3, 2)

        # =================================================================
        # 分组和treatment设置
        # =================================================================

        # 11轮和21轮，组内乱序。其余按上一轮。
        if self.round_number in [11, 21]:
            gm = self.get_group_matrix()
            new_gm = oh.shuffle_in_groups(gm)
            self.set_group_matrix(new_gm)

        elif self.round_number > 1:
            self.group_like_round(self.round_number - 1)

        set_treatment_for_all(self.get_groups(), self.round_number)

        # 保留角色重排
        if self.round_number in [6, 16, 26]:
            gm = self.get_group_matrix()
            new_gm = oh.shuffle_in_groups_by_role(gm, "res")
            self.set_group_matrix(new_gm)

            # 重排后还要重设一下group的treatment信息
            set_treatment_for_all(self.get_groups(), self.round_number)

        # =================================================================
        # 生成和保留信息
        # =================================================================

        # 把role保存起来
        for p in self.get_players():
            p.the_role = p.role()

        # 生成GID
        for gid, g in enumerate(self.get_groups()):
            for p in g.get_players():
                p.gid = (gid + 1) * 10 + p.id_in_group

        # 生成subgame_counter
        for g in self.get_groups():
            g.subgame_counter = (self.round_number - 1) % 5 + 1


class Group(BaseGroup):
    subgame_counter = models.IntegerField()
    treatment = models.StringField()
    init_property = models.StringField()
    res_number = models.IntegerField()

    corp_profit = models.IntegerField()
    core_pollution = models.IntegerField()
    res_total_health = models.IntegerField()

    def set_treatment(self, treatment):
        """
           把treatment:str写入Group以及其下的Players的treatment属性里
           :param g: a Group
           :param treatment: the treatment string
           :return: none
           """
        self.treatment = treatment

        if "corp" in treatment:
            # 产权归企业
            self.init_property = "corp"

        else:
            # 产权归居民
            self.init_property = "res"

        if "1" in treatment:
            self.res_number = 1
        else:
            self.res_number = 3

        p: Player
        for p in self.get_players():
            p.treatment = treatment
            if p.role() == self.init_property:
                p.is_seller = True
            else:
                p.is_seller = False

    # 无产权的一方出价，高于对方出价，则deal = True，以无产权方出价为准
    def set_payoff(self):
        # if self.treatment == "corp_1":
        #     # 1v1，产权归企业
        #     # p1 vs p2, p3 vs p4
        #     self.get_player_by_id(1)
        #
        # if self.treatment == "corp_3":
        #     # 1v1，产权归企业
        #     # p1 vs p2, p3 vs p4
        #     res_price = sum(p.offer for p in self.get_players_by_role("res"))
        pass

    def set_profit(self):
        # if self.res_number == 1:
        #     set_profit_for_1v1(self)
        # else:
        #     set_profit_for_1v3(self)
        pass


def set_profit_for_1v1(g: Group):
    pass


def set_profit_for_1v3(g: Group):
    pass


def set_treatment_for_all(gs: List[Group], round_number: int):
    """
    初始的treatment顺序列表，表示每个10轮的起始（G1）的treatment
    即：1，11，21轮开始的G1的treatment
    对于G2，G3等等，利用oh.shift()对这个treatment列表进行平移即可
    :param gs:
    :param round_number:
    :return:
    """

    treatment_list_base: List[str] = ['corp_1', 'corp_3', 'crop_3']
    treatment_list_base_swap: List[str] = ['res_1', 'res_3', 'res_3']

    t1 = 'corp'
    t2 = 'res'

    g: Group
    for idg, g in enumerate(gs):
        treatment_list = oh.shift(treatment_list_base, idg)
        treatment_list_swap = oh.shift(treatment_list_base_swap, idg)
        if round_number in range(1, 6):
            g.set_treatment(treatment_list[0])

        elif round_number in range(6, 11):
            g.set_treatment(treatment_list_swap[0])

        elif round_number in range(11, 16):
            g.set_treatment(treatment_list[1])

        elif round_number in range(16, 21):
            g.set_treatment(treatment_list_swap[1])

        elif round_number in range(21, 26):
            g.set_treatment(treatment_list[2])

        else:
            g.set_treatment(treatment_list_swap[2])


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

    # 一个人不可能同时担任2种角色，因此一个price表示他们的选择即可
    price = models.IntegerField(min=0)

    # 权力的持有者，即卖方
    is_seller = models.BooleanField()

    # 是否达成协议
    deal = models.BooleanField()

    # 保存角色
    the_role = models.StringField()


def set_profit_core(seller_list: List[Player], buyer_list: List[Player]):
    """
    计算双方的赢利。
    若buyer的price之和 >= 若seller的price之和，则deal，否则no deal
    :param seller_list:
    :param buyer_list:
    :return:
    """

    def set_deal(deal: bool):
        for p in seller_list:
            p.deal = deal
        for p in buyer_list:
            p.deal = deal

    def set_payoff_on_price():
        for p in seller_list:
            p.payoff = p.price
        for p in buyer_list:
            p.payoff = p.price

    seller_price = sum([p.price for p in seller_list])
    buyer_price = sum([p.price for p in buyer_list])

    the_deal = (buyer_price >= seller_price)

    set_deal(the_deal)

    if the_deal:
        set_payoff_on_price()

    # 如果deal，那么
    #   seller.payoff = seller.price
    #   buyer.payoff = high_value - buyer.price

    # no deal，那么
    #   seller.payoff = low_value
    #   buyer.payoff = 0
