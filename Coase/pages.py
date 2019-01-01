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


class Intro(Page):
    pass


class CorpOffer(Page):
    form_model = 'player'
    form_fields = ['corp_price']

    def is_displayed(self):
        return self.player.role() == "corp"


class ResOffer(Page):
    form_model = 'player'
    form_fields = ['res_price']

    def is_displayed(self):
        return self.player.role() == "res"


page_sequence = [
    Intro,
    CorpOffer,
    ResOffer,
    ResultsWaitPage,
    Results
]
