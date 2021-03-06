from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Survey(Page):
    form_model = 'player'
    form_fields = ['sur_q01', 'sur_q02', 'sur_q03', 'sur_q04',
                   'sur_q05', 'sur_q06', 'sur_q07', 'sur_q08',
                   'sur_q09', 'sur_q10', 'sur_q11', 'sur_q12',
                   'sur_q13', 'sur_q14', 'sur_q15', 'sur_q16',
                   'sur_q17', 'sur_q18', 'sur_q19'
                   ]


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            pay_round = p.pay_round

            p.choice = getattr(p, "sur_q0" + str(pay_round))

            if p.choice == "接受":
                if random.choice([0, 1]) == 0:
                    p.profit = 0
                else:
                    p.profit = (11 - p.pay_round) * 10
            else:
                p.profit = Constants.endowment

            p.payoff = p.profit


class Results(Page):
    def vars_for_template(self):
        return {'gamble_choice': self.player.choice}


page_sequence = [
    Survey,
    #ResultsWaitPage,
    #Results
]
