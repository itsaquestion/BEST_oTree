from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass


class ResultsFinalWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass


class ResultsCorp(Page):
    def is_displayed(self):
        return self.player.the_role == "corp"


class ResultsRes(Page):
    def is_displayed(self):
        return self.player.the_role == "res"


class ResultsFinal(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class IntroCorp(Page):
    def is_displayed(self):
        return self.player.the_role == "corp" and self.round_number in [1, 6, 11, 16, 21, 26]


class IntroRes(Page):
    def is_displayed(self):
        return self.player.the_role == "res" and self.round_number in [1, 6, 11, 16, 21, 26]


class ChoiceCorp(Page):
    form_model = 'player'
    form_fields = ['price']

    def offer_max(self):
        return self.player.session.vars['corp_profit']

    def is_displayed(self):
        return self.player.the_role == "corp"


class ChoiceRes(Page):
    form_model = 'player'
    form_fields = ['price']

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


class Blank(Page):
    def is_displayed(self):
        return self.round_number == 30


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
    Blank,
    ResultsFinalWaitPage,
    ResultsFinal

]
