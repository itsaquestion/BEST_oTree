from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)

from string import Template

import otree_helper as oh

import random

author = 'Your name here'

doc = """
Your app description
"""


def calc_payoff(c_self, c_other, pay1, pay2):
    """
    根据双方的选择，决定赢利。相同为0；不同，则如果自己选择主，那么给pay1，否则给pay2
    :param c_self:
    :param c_other:
    :param pay1:
    :param pay2:
    :return:
    """
    if c_self == c_other:
        return 0
    elif c_self == '"主"角色':
        return pay1
    else:
        return pay2


def make_question_string(i: int):
    """
     生成提问字符串
    :param i:
    :return:
    """
    token = (16 - i) * 10
    s = Template('（$number） 50%的可能，你将得到0个实验币；50%的可能，你将得到$token实验币')
    return s.substitute(number=str(i), token=str(token))


class Constants(BaseConstants):
    name_in_url = 'informal_authority'
    players_per_group = 2
    num_rounds = 1

    label_color1 = "天蓝方"
    label_color2 = "海蓝方"

    label_winner = "胜方"
    label_loser = "败方"

    winners_reward = 50

    # label_color_loser1 = "天蓝败方"
    # label_color_loser2 = "海蓝败方"


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        self.session.vars['is_debug'] = self.session.config['debug_mode']
        self.session.vars['matrix_x'] = self.session.config['matrix_x']
        self.session.vars['matrix_y'] = self.session.config['matrix_y']
        self.session.vars['game_time_sec'] = self.session.config['game_time_sec']
        self.session.vars['correct_threshold'] = self.session.config['correct_threshold']
        self.session.vars['points_for_one_yuan'] = self.session.config['points_for_one_yuan']
        self.session.vars['participation_fee'] = self.session.config['participation_fee']

        # 锁定匹配，1号配对最后一号，2号配对倒数第二号，如此类推。
        # treatment有设定则按设定，没有设定则循环设置。
        if self.round_number == 1:
            matrix = self.get_group_matrix()
            new_structure = oh.head_tail_pairing(matrix)
            self.set_group_matrix(new_structure)

        all_treatments = oh.get_all_treatments_from_config(self)
        self.session.vars['all_treatments'] = all_treatments

        # 循环设定treatment ====
        if self.round_number == 1:

            # 循环设定treatment
            n = len(all_treatments)
            for g in self.get_groups():
                pid = g.get_player_by_id(1).id_in_subsession
                g.set_treatment(all_treatments[(pid - 1) % n])


class Group(BaseGroup):
    treatment = models.StringField(widget=widgets.RadioSelect)

    def set_treatment(self, treatment):
        self.treatment = treatment
        for p in self.get_players():
            p.treatment = treatment

    def set_label(self):
        """
        根据treatment，设置label
        :return:
        """
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if self.treatment.startswith("choice_color"):
            self.set_label_choice_color()

        if self.treatment.startswith("choice_wl"):
            self.set_label_choice_wl()

        if self.treatment.startswith("compete_wl"):
            self.set_label_compete_wl()

        # if p1.treatment == "compete_wl_color":
        #     self.set_label_compete_wl_color()

        p1.label_partner = p2.label
        p2.label_partner = p1.label

    def set_label_compete_wl_color(self):
        """
        数0 - 颜色
        :return:
        """
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        n = self.session.vars['correct_threshold']

        if p1.correct < n and p2.correct < n:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser

        if p1.correct >= n and p1.correct > p2.correct:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser

        if p2.correct >= n and p2.correct > p1.correct:
            p2.label = Constants.label_winner
            p1.label = Constants.label_loser

        # 平局p1算胜利者，因为p1p2本身已经是随机设定的。
        if p1.correct == p2.correct:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser

    def set_label_compete_wl(self):
        """
        数0 - 输赢
        :return:
        """
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.correct > p2.correct:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser

        if p1.correct < p2.correct:
            p1.label = Constants.label_loser
            p2.label = Constants.label_winner

        # 平局p1算胜利者，因为p1p2本身已经是随机设定的。
        if p1.correct == p2.correct:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser

    def set_label_choice_color(self):
        """
        选择 - 颜色
        :return:
        """
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.id_choice_01 == p2.id_choice_01:
            p1.label = Constants.label_color1
            p2.label = Constants.label_color2
        else:
            p1.label = Constants.label_color2
            p2.label = Constants.label_color1

    def set_label_choice_wl(self):
        """
        选择 - 输赢
        :return:
        """
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.id_choice_01 == p2.id_choice_01:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser
        else:
            p1.label = Constants.label_loser
            p2.label = Constants.label_winner


def make_survey_field(n: int):
    return models.StringField(
        choices=['接受', '拒绝'],
        verbose_name=make_question_string(n),
        widget=widgets.RadioSelectHorizontal
    )


def make_role_choice_field():
    return models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=['"主"角色', '"从"角色']
    )


def make_project_choice_field():
    return models.StringField(
        verbose_name="你会选择",
        choices=['项目1', '项目2', '项目3'],
        widget=widgets.RadioSelectHorizontal
    )


class Player(BasePlayer):
    treatment = models.StringField(widget=widgets.RadioSelect)

    # 双方的身份标签
    label = models.StringField()
    label_partner = models.StringField()

    pay_round = models.IntegerField()
    co_payoff_points = models.FloatField()

    gamble_round = models.IntegerField()
    gamble_payoff_points = models.FloatField()

    total_payoff_points = models.FloatField()

    correct = models.IntegerField()

    id_choice_01 = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[0, 1]
    )

    co_choice_01 = make_role_choice_field()

    co_choice_02 = make_role_choice_field()

    co_choice_03 = make_role_choice_field()

    co_choice_04 = make_role_choice_field()

    co_choice_05 = make_role_choice_field()

    def is_reward_show_after(self):
        return 'showafter' in self.treatment

    def set_payoff(self):
        self.pay_round = random.choice([1, 2, 3, 4, 5])

        co_choice_string = "co_choice_0" + str(self.pay_round)

        c_self = getattr(self, co_choice_string)
        c_other = getattr(self.get_others_in_group()[0], co_choice_string)

        if self.pay_round == 1:
            self.co_payoff_points = calc_payoff(c_self, c_other, 400, 200)

        if self.pay_round == 2:
            self.co_payoff_points = calc_payoff(c_self, c_other, 500, 100)

        if self.pay_round == 3:
            self.co_payoff_points = calc_payoff(c_self, c_other, 300, 300)

        if self.pay_round == 4:
            self.co_payoff_points = calc_payoff(c_self, c_other, 450, 150)

        if self.pay_round == 5:
            self.co_payoff_points = calc_payoff(c_self, c_other, 350, 250)

        self.gamble_round = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
        get_list = [150, 140, 130, 120, 110, 100, 90, 80]
        if random.choice([0, 1]) == 0:
            self.gamble_payoff_points = 0
        else:
            self.gamble_payoff_points = get_list[(self.gamble_round - 1)]

    # 以下是survey 用变量 ================================================

    sur_q01 = make_survey_field(1)

    sur_q02 = make_survey_field(2)

    sur_q03 = make_survey_field(3)

    sur_q04 = make_survey_field(4)

    sur_q05 = make_survey_field(5)

    sur_q06 = make_survey_field(6)

    sur_q07 = make_survey_field(7)

    sur_q08 = make_survey_field(8)

    sur_birth_year = models.IntegerField(verbose_name="你出生的年份是")
    sur_birth_month = models.IntegerField(verbose_name="你出生的月份是(1-12)", min=1, max=12)
    sur_gender = models.StringField(
        choices=['男', '女'],
        verbose_name="你的性别是",
        widget=widgets.RadioSelectHorizontal)
    sur_grade = models.StringField(
        choices=['大一', '大二', '大三', '大四', '研一', '研二'],
        verbose_name="你就读的年级为",
        widget=widgets.RadioSelectHorizontal)
    sur_school = models.StringField(
        verbose_name="你就读的学院为")
    sur_party_member = models.StringField(
        verbose_name="你是否为党员",
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_student_leader = models.StringField(
        verbose_name="你是否为学生干部",
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )

    sur_project_01 = make_project_choice_field()
    sur_project_02 = make_project_choice_field()
    sur_project_03 = make_project_choice_field()
    sur_project_04 = make_project_choice_field()
    sur_project_05 = make_project_choice_field()
