from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from string import Template
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey_risk'
    players_per_group = None
    num_rounds = 1

    endowment = 50


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.pay_round = random.randint(1, 8)


class Group(BaseGroup):
    pass


def make_survey_field(n: int):
    return models.StringField(
        choices=['接受', '拒绝'],
        verbose_name=make_question_string(n),
        widget=widgets.RadioSelectHorizontal
    )


def make_question_string(i: int):
    """
     生成提问字符串
    :param i:
    :return:
    """

    token = (11 - i) * 10
    s = Template('（$number） 50%的可能，你将损失$endowment个代币；50%的可能，你将得到$token代币')
    return s.substitute(number=str(i), token=str(token), endowment=str(Constants.endowment))


class Player(BasePlayer):
    pay_round = models.IntegerField()
    choice = models.StringField()
    win = models.BooleanField()

    sur_q01 = make_survey_field(1)

    sur_q02 = make_survey_field(2)

    sur_q03 = make_survey_field(3)

    sur_q04 = make_survey_field(4)

    sur_q05 = make_survey_field(5)

    sur_q06 = make_survey_field(6)

    sur_q07 = make_survey_field(7)

    sur_q08 = make_survey_field(8)
