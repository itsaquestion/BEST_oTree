from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):
        regrouped = self.player.round_number in self.session.vars['regroup_rounds']

        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'regrouped': regrouped
        }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.record_partner_decision()
            p.set_payoff()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        me = self.player

        return {
            'player_in_all_rounds': self.player.in_all_rounds(),
            'total_payoff': me.total_payoff
        }


class RegroupWaitPage(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number in self.session.vars['regroup_rounds']


class FinalWaitPage(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Introduction,
    RegroupWaitPage,
    Decision,
    ResultsWaitPage,
    FinalWaitPage,
    Results
]
