from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import numpy as np

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


def cal_random_rounds(low=8, high=13, size=9):
    '''
    100回合中重新分组9次，每次随机玩8 ~ 12回合，求具体那些回合要重新分组。

    :param low: 每次分组，博弈次数下限（包含)
    :param high: 每次分组，博弈次数上限（不包含。例如high = 13，则最多为12）
    :param size: 重新分组次数。
    :return: 一个List，包含具体分组的回合数。
    '''
    break_points = np.random.randint(low, high, size=size)
    # break_points

    np.mean(break_points)

    regroup_rounds = [0] * len(break_points)
    regroup_rounds[0] = break_points[0]
    for i in range(1, len(break_points)):
        regroup_rounds[i] = break_points[i] + regroup_rounds[i - 1]

    return regroup_rounds


class Constants(BaseConstants):
    name_in_url = 'repeat_prisoner'
    players_per_group = 2
    num_rounds = 10

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = 300
    betrayed_payoff = 0

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = 200
    both_defect_payoff = 100


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['is_debug'] = self.session.config['debug_mode']

        # init
        if self.round_number == 1:
            self.session.vars['regroup_rounds'] = cal_random_rounds(low=2, high=5, size=2)
            # self.session.vars['regroup_rounds'] = [4,6]

            for p in self.get_players():
                p.participant.vars['total_payoff'] = 0

        # regroup
        if self.round_number == 1:
            self.group_randomly()
        else:
            if self.round_number in self.session.vars['regroup_rounds']:
                self.group_randomly()
            else:
                self.group_like_round(self.round_number - 1)

        for p in self.get_players():
            p.record_partner_id()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    partner_id = models.IntegerField()

    partner_decision = models.StringField()

    total_payoff = models.CurrencyField()

    decision = models.StringField(
        choices=['合作', '欺骗'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    def record_partner_id(self):
        self.partner_id = self.get_other_player().participant.id_in_session

    def get_other_player(self):
        return self.get_others_in_group()[0]

    def record_partner_decision(self):
        self.partner_decision = self.get_other_player().decision

    def set_payoff(self):
        payoff_matrix = {
            '合作':
                {
                    '合作': Constants.both_cooperate_payoff,
                    '欺骗': Constants.betrayed_payoff
                },
            '欺骗':
                {
                    '合作': Constants.betray_payoff,
                    '欺骗': Constants.both_defect_payoff
                }
        }

        self.payoff = payoff_matrix[self.decision][self.get_other_player().decision]

        self.participant.vars['total_payoff'] = self.participant.vars['total_payoff'] + self.payoff

        self.total_payoff = self.participant.vars['total_payoff']
