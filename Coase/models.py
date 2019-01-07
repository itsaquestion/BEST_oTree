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

    pay_rounds: List[int] = [4, 15, 27]


class Subsession(BaseSubsession):
    def creating_session(self):

        # =================================================================
        # 读取全局设置
        # =================================================================
        self.session.vars['is_debug'] = self.session.config['debug_mode']
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
        hv = self.session.vars['high_value']
        lv = self.session.vars['low_value']

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p5 = self.get_player_by_id(5)
        p6 = self.get_player_by_id(6)
        p7 = self.get_player_by_id(7)
        p8 = self.get_player_by_id(8)

        if self.treatment == "corp_1":
            set_profit_core([p1], [p2], hv, lv)
            set_profit_core([p3], [p4], hv, lv)
            set_profit_core([p5], [p6], hv, lv)
            set_profit_core([p7], [p8], hv, lv)

        if self.treatment == "corp_3":
            set_profit_core([p1], [p2, p3, p4], hv, lv)
            set_profit_core([p5], [p6, p7, p8], hv, lv)

        if self.treatment == "res_1":
            set_profit_core([p2], [p1], hv, lv)
            set_profit_core([p4], [p3], hv, lv)
            set_profit_core([p6], [p5], hv, lv)
            set_profit_core([p8], [p7], hv, lv)

        if self.treatment == "res_3":
            set_profit_core([p2, p3, p4], [p1], hv, lv)
            set_profit_core([p6, p7, p8], [p5], hv, lv)

        if self.round_number in Constants.pay_rounds:
            p: Player
            for p in self.get_players():
                p.payoff = p.profit

    def set_final_payoff(self):
        # Constants.pay_rounds
        p: Player
        pp: Player
        all_p: List[Player]

        for p in self.get_players():
            all_p = p.in_all_rounds()
            pay_p = [pp for idp, pp in enumerate(all_p) if (idp + 1) in Constants.pay_rounds]
            pay_p_profit_list = [pp.profit for pp in pay_p]
            p.profit_list_str = ', '.join(str(x) for x in pay_p_profit_list)
            p.total_profit = sum(pay_p_profit_list)
            pay_rounds_str = ', '.join([str(x) for x in Constants.pay_rounds])

            # p.payoff = round(p.total_profit / self.session.vars['points_for_one_yuan'], 2) + self.session.vars[
            #     'participation_fee']
            #
            # p.participant.payoff = p.payoff

            coase_results_html = """
                <p>电脑在6个任务总共30轮中随机抽取了3轮，并根据这3轮的结果的总和来支付实验报酬。</p>
                <p>这3轮分别是：{pay_rounds_str}</p>
                <p>所获得代币分别是：{p.profit_list_str}，总和是{p.total_profit}代币。</p>
            """

            p.participant.vars['coase_results_html'] = coase_results_html.format_map(vars())


def set_treatment_for_all(gs: List[Group], round_number: int):
    """
    初始的treatment顺序列表，表示每个10轮的起始（G1）的treatment
    即：1，11，21轮开始的G1的treatment
    对于G2，G3等等，利用oh.shift()对这个treatment列表进行平移即可
    :param gs:
    :param round_number:
    :return:
    """

    treatment_list_base: List[str] = ['corp_1', 'corp_3', 'corp_3']
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

    profit = models.FloatField()

    # 被抽中轮次的代币之和
    total_profit = models.FloatField()

    # 被抽中轮次的代币，以逗号分隔
    profit_list_str = models.StringField()

    # 一个人不可能同时担任2种角色，因此一个price表示他们的选择即可

    # 参与人输入的数字
    price = models.IntegerField(min=0)

    # 己方输入的数字之和
    price_total = models.IntegerField(min=0)

    # 己方输入数字列表，用逗号隔开
    price_list = models.StringField()

    # 对方输入的数字之和
    counterpart_price_total = models.IntegerField(min=0)

    # 对方输入数字的列表，用逗号隔开
    counterpart_price_list = models.StringField()

    # 权力的持有者，即卖方
    is_seller = models.BooleanField()

    # 是否达成协议
    deal = models.BooleanField()

    # 保存角色
    the_role = models.StringField()


def set_profit_core(seller_list: List[Player], buyer_list: List[Player], high_value: int, low_value: int):
    """
    计算双方的赢利。

    :param seller_list:
    :param buyer_list:
    :return:
    """

    seller_price_list = [p.price for p in seller_list]
    buyer_price_list = [p.price for p in buyer_list]

    seller_price_list_str = ','.join(str(x) for x in [p.price for p in seller_list])
    buyer_price_list_str = ','.join(str(x) for x in [p.price for p in buyer_list])

    seller_price_total = sum(seller_price_list)
    buyer_price_total = sum(buyer_price_list)

    seller_size = len(seller_list)
    buyer_size = len(buyer_list)

    buyer: Player
    seller: Player
    the_deal: bool

    # 记录已知信息
    for p in seller_list:
        p.price_total = seller_price_total
        p.price_list = seller_price_list_str
        p.counterpart_price_total = buyer_price_total
        p.counterpart_price_list = buyer_price_list_str

    for p in buyer_list:
        p.price_total = buyer_price_total
        p.price_list = buyer_price_list_str
        p.counterpart_price_total = seller_price_total
        p.counterpart_price_list = seller_price_list_str

    # 计算盈利
    if buyer_price_total >= seller_price_total:
        # Deal
        for p in seller_list:
            p.deal = True
            p.profit = p.price

        for p in buyer_list:
            p.deal = True
            p.profit = round(high_value / buyer_size, 2) - p.price
    else:
        # No Deal
        for p in seller_list:
            p.deal = False
            p.profit = round(low_value / seller_size, 2)

        for p in buyer_list:
            p.deal = False
            p.profit = 0
