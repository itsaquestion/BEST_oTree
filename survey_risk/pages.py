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

        p.choice = getattr(p, "sur_q0" + str(p.pay_round))

        if str(p.choice) == "接受":
            if random.choice([0, 1]) == 0:
                p.payoff = 0
                p.win = False
            else:
                p.payoff = (11 - p.pay_round) * 10
                p.win = True
        else:
            p.payoff = Constants.endowment

        win_str = "赢" if self.player.win else "输"
        # pay_round = p.pay_round
        # choice = p.choice
        # payoff = p.payoff

        risk_result_html = """
        <p>被随机抽取的赌局决策结果是第<b>{p.pay_round}</b>项，你的选择是<b>{p.choice}</b>赌局。</p>
        <p>结果是：{win_str}。</p>
        <p>因此你获得了{p.payoff}。</p>
        """

        self.participant.vars['risk_result_html'] = risk_result_html.format_map(vars())


class Results(Page):
    pass


page_sequence = [
    Survey,
    Results
]
