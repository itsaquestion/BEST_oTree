from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GroupChecker(Page):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    pass


class IntroCorp(Page):
    def is_displayed(self):
        return self.player.the_role == "corp"


class IntroRes(Page):
    def is_displayed(self):
        return self.player.the_role == "res"


class OfferCorp(Page):
    form_model = 'player'
    form_fields = ['corp_price']

    def is_displayed(self):
        return self.player.the_role == "corp"


class OfferRes(Page):
    form_model = 'player'
    form_fields = ['res_price']

    def is_displayed(self):
        return self.player.the_role == "res"


class Preface(Page):
    pass


page_sequence = [
    Preface,
    IntroCorp,
    IntroRes,
    OfferCorp,
    OfferRes,
    ResultsWaitPage,
    Results
]
