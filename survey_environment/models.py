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
    name_in_url = 'survey_environment'
    players_per_group = None
    num_rounds = 1

    endowment = 50


class Subsession(BaseSubsession):
    def creating_session(self):
        pass


class Group(BaseGroup):
    pass


def make_survey_field(n: int, msg: str):
    return models.StringField(
        choices=['非常不赞成', '不赞成', '持中', '赞成', '非常赞成'],
        verbose_name=str(n) + ". " + msg,
        widget=widgets.RadioSelectHorizontal
    )


class Player(BasePlayer):
    sur_q01 = make_survey_field(1, '环境是当今社会面临的最重要的问题之一')

    sur_q02 = make_survey_field(2, '我们应该付出相当多的钱来保护我们的环境')

    sur_q03 = make_survey_field(3, '必须立即采取严格的全球措施，以制止环境恶化')

    sur_q04 = make_survey_field(4, '应该投入大量资金用于环境保护')

    sur_q05 = make_survey_field(5, '除非我们每个人都认识到保护环境的必要性，否则后代将承受后果')

    sur_q06 = make_survey_field(6, '保护环境的益处并不能证明所涉及的费用是合理的')

    sur_q07 = make_survey_field(7, '在决定我们将来做什么时，环境问题不应成为主要考虑因素')

    sur_q08 = make_survey_field(8, '就个人而言，我无法帮助减缓环境恶化')

    sur_q09 = make_survey_field(9, '环境的重要性经常被夸大')

    sur_q10 = make_survey_field(10, '克服环境恶化的益处不足以保证所涉及的费用')

    sur_q11 = make_survey_field(11, '即使我们每个人都为环境保护做出了贡献，但综合影响仍然微不足道')

    sur_q12 = make_survey_field(12, '人们在环境问题上大惊小怪')
    sur_q13 = make_survey_field(13, '政府应该对环境保护负起责任')
    sur_q14 = make_survey_field(14, '日益严重的环境破坏是一个严重的问题')
    sur_q15 = make_survey_field(15, '每个人都有责任在日常生活中保护环境')
    sur_q16 = make_survey_field(16, '与环境有关的问题非常重要')
    sur_q17 = make_survey_field(17, '如果我们每个人都能为环境保护各自做出贡献，那将会产生重大影响')
    sur_q18 = make_survey_field(18, '作为个人，我们每个人都可以为环境保护做出贡献')
    sur_q19 = make_survey_field(19, '企业应该始终把盈利放在环保之上')
