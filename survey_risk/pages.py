from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Survey(Page):
    form_model = 'player'
    form_fields = ['sur_q01', 'sur_q02', 'sur_q03', 'sur_q04',
                   'sur_q05', 'sur_q06', 'sur_q07', 'sur_q08']

    def before_next_page(self):
        p = self.player
        pay_round = p.pay_round

        p.choice = getattr(p, "sur_q0" + str(pay_round))

        if str(p.choice) == "接受":
            if random.choice([0, 1]) == 0:
                p.payoff = 0
                p.win = False
            else:
                p.payoff = (11 - p.pay_round) * 10
                p.win = True
        else:
            p.payoff = Constants.endowment


class Results(Page):
    def vars_for_template(self):
        return {'gamble_choice': self.player.choice,
                'win': "赢" if self.player.win else "输"}


page_sequence = [
    Survey,
    Results
]
