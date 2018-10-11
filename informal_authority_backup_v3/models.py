from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)

from itertools import chain

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'informal_authority'
    players_per_group = 2
    num_rounds = 1

    label_color1 = "天蓝方"
    label_color2 = "海蓝方"

    label_winner = "胜方"
    label_loser = "败方"

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
            n = len(matrix) * len(matrix[0])

            new_structure = [None] * int(n / 2)
            for i in range(1, int(n / 2) + 1):
                # print(i)
                new_structure[i - 1] = [i, n - i + 1]

            self.set_group_matrix(new_structure)

            tm = []
            if 'treatment' in self.session.config:
                tm = self.session.config['treatment']
            else:
                tm = ['choice_color', 'choice_wl', 'compete_wl']

            # 循环设定treatment
            n = len(tm)
            for g in self.get_groups():
                pid = g.get_player_by_id(1).id_in_subsession
                g.set_treatment(tm[(pid - 1) % n])


class Group(BaseGroup):
    def set_treatment(self, treatment):
        for p in self.get_players():
            p.treatment = treatment

    def set_label(self):
        '''
        根据treatment的不同设定不同的label
        '''
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.treatment == "choice_color":
            self.set_label_color()

        if p1.treatment == "choice_wl":
            self.set_label_wl()

        if p1.treatment == "compete_wl":
            self.set_label_compete_wl()

        if p1.treatment == "compete_wl_color":
            self.set_label_compete_wl_color()

        p1.label_partner = p2.label
        p2.label_partner = p1.label

    def set_label_compete_wl_color(self):
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

    def set_label_color(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.id_choice_01 == p2.id_choice_01:
            p1.label = Constants.label_color1
            p2.label = Constants.label_color2
        else:
            p1.label = Constants.label_color2
            p2.label = Constants.label_color1

    def set_label_wl(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.id_choice_01 == p2.id_choice_01:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser
        else:
            p1.label = Constants.label_loser
            p2.label = Constants.label_winner


class Player(BasePlayer):
    treatment = models.StringField()
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

    co_choice_01 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=['"主"角色', '"从"角色']
    )

    co_choice_02 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=['"主"角色', '"从"角色']
    )

    co_choice_03 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=['"主"角色', '"从"角色']
    )

    co_choice_04 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=['"主"角色', '"从"角色']
    )

    co_choice_05 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=['"主"角色', '"从"角色']
    )

    def set_payoff(self):
        self.pay_round = random.choice([1, 2, 3, 4, 5])

        if self.pay_round == 1:
            c_self = self.co_choice_01
            c_other = self.get_others_in_group()[0].co_choice_01
            self.co_payoff_points = calc_payoff(c_self, c_other, 400, 200)

        if self.pay_round == 2:
            c_self = self.co_choice_02
            c_other = self.get_others_in_group()[0].co_choice_02
            self.co_payoff_points = calc_payoff(c_self, c_other, 500, 100)

        if self.pay_round == 3:
            c_self = self.co_choice_03
            c_other = self.get_others_in_group()[0].co_choice_03
            self.co_payoff_points = calc_payoff(c_self, c_other, 300, 300)

        if self.pay_round == 4:
            c_self = self.co_choice_04
            c_other = self.get_others_in_group()[0].co_choice_04
            self.co_payoff_points = calc_payoff(c_self, c_other, 450, 150)

        if self.pay_round == 5:
            c_self = self.co_choice_05
            c_other = self.get_others_in_group()[0].co_choice_05
            self.co_payoff_points = calc_payoff(c_self, c_other, 350, 250)

        self.gamble_round = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
        get_list = [150, 140, 130, 120, 110, 100, 90, 80]
        if random.choice([0, 1]) == 0:
            self.gamble_payoff_points = 0
        else:
            self.gamble_payoff_points = get_list[(self.gamble_round - 1)]

    sur_q01 = models.StringField(
        choices=['接受', '拒绝'],
        verbose_name='（1） 50%的可能，你将得到0个实验币；50%的可能，你将得到150实验币',
        widget=widgets.RadioSelectHorizontal)

    sur_q02 = models.StringField(
        choices=['接受', '拒绝'],
        verbose_name='（2） 50%的可能，你将得到0个实验币；50%的可能，你将得到140实验币',
        widget=widgets.RadioSelectHorizontal)

    sur_q03 = models.StringField(
        choices=['接受', '拒绝'],
        verbose_name='（3） 50%的可能，你将得到0个实验币；50%的可能，你将得到130实验币',
        widget=widgets.RadioSelectHorizontal)

    sur_q04 = models.StringField(
        choices=['接受', '拒绝'],
        verbose_name='（4） 50%的可能，你将得到0个实验币；50%的可能，你将得到120实验币',
        widget=widgets.RadioSelectHorizontal)

    sur_q05 = models.StringField(
        choices=['接受', '拒绝'],
        verbose_name='（5） 50%的可能，你将得到0个实验币；50%的可能，你将得到110实验币',
        widget=widgets.RadioSelectHorizontal)

    sur_q06 = models.StringField(
        choices=['接受', '拒绝'],
        verbose_name='（6） 50%的可能，你将得到0个实验币；50%的可能，你将得到100实验币',
        widget=widgets.RadioSelectHorizontal)

    sur_q07 = models.StringField(
        choices=['接受', '拒绝'],
        verbose_name='（7） 50%的可能，你将得到0个实验币；50%的可能，你将得到90实验币',
        widget=widgets.RadioSelectHorizontal)

    sur_q08 = models.StringField(
        choices=['接受', '拒绝'],
        verbose_name='（8） 50%的可能，你将得到0个实验币；50%的可能，你将得到80实验币',
        widget=widgets.RadioSelectHorizontal)

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

    sur_project_01 = models.StringField(
        verbose_name="你会选择",
        choices=['项目1', '项目2', '项目3'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_project_02 = models.StringField(
        verbose_name="你会选择",
        choices=['项目1', '项目2', '项目3'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_project_03 = models.StringField(
        verbose_name="你会选择",
        choices=['项目1', '项目2', '项目3'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_project_04 = models.StringField(
        verbose_name="你会选择",
        choices=['项目1', '项目2', '项目3'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_project_05 = models.StringField(
        verbose_name="你会选择",
        choices=['项目1', '项目2', '项目3'],
        widget=widgets.RadioSelectHorizontal
    )


def calc_payoff(c_self, c_other, pay1, pay2):
    '''
    根据双方的选择，决定赢利。相同为0；不同，则如果自己选择主，那么给pay1，否则给pay2
    :param c_self:
    :param c_other:
    :param pay1:
    :param pay2:
    :return:
    '''
    if c_self == c_other:
        return 0
    elif c_self == '"主"角色':
        return pay1
    else:
        return pay2
