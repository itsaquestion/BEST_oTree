from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from random import randint


class PlayerBot(Bot):

    # IntroCorp,
    # IntroRes,
    # ChoiceCorp,
    # ChoiceRes,
    # ResultsWaitPage,
    # ResultsCorp,
    # ResultsRes

    def play_round(self):
        # if self.round_number == 1:
        #     yield (pages.Requirement)
        #     yield (pages.Preface)
        #
        # if self.player.role() == "corp" and self.round_number in [1, 6, 11, 16, 21, 26]:
        #     yield (pages.IntroCorp)
        #
        # if self.player.role() == "res" and self.round_number in [1, 6, 11, 16, 21, 26]:
        #     yield (pages.IntroRes)

        if self.player.role() == "corp":
            yield (pages.ChoiceCorp, {'price': randint(1, self.session.vars['high_value'])})

        if self.player.role() == "res":
            yield (pages.ChoiceRes, {'price': randint(1, self.session.vars['high_value'])})

        # if self.player.role() == "corp":
        #     yield (pages.ResultsCorp)
        #
        # if self.player.role() == "res":
        #     yield (pages.ResultsRes)

        if self.round_number == Constants.num_rounds:
            id = self.participant.id_in_session
            text_file = open("Coase/test_results/p" + str(id) + ".html", "w", encoding='utf-8')
            text_file.write(self.html)
            text_file.close()

            #yield (pages.ResultsFinal)
            #pass
