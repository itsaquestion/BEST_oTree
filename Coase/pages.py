from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GroupChecker(Page):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class ResultsCorp(Page):
    pass


class ResultsRes(Page):
    pass


class ResultsFinal(Page):
    pass


class IntroCorp(Page):
    def is_displayed(self):
        return self.player.the_role == "corp" and self.round_number in [1, 11, 21]


class IntroRes(Page):
    def is_displayed(self):
        return self.player.the_role == "res" and self.round_number in [1, 11, 21]


class ChoiceCorp(Page):
    form_model = 'player'
    form_fields = ['corp_price']

    def offer_max(self):
        return self.player.session.vars['corp_profit']

    def is_displayed(self):
        return self.player.the_role == "corp"


class ChoiceRes(Page):
    form_model = 'player'
    form_fields = ['res_price']

    def offer_max(self):
        return Constants.res_endowment

    def is_displayed(self):
        return self.player.the_role == "res"


class Preface(Page):
    def is_displayed(self):
        return self.round_number == 1


class Requirement(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    Requirement,
    Preface,
    IntroCorp,
    IntroRes,
    ChoiceCorp,
    ChoiceRes,
    ResultsWaitPage,
    ResultsCorp,
    ResultsRes,
    ResultsFinal

]
