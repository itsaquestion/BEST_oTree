from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        id = self.participant.id_in_session
        text_file = open("Coase_payment/test_results/p" + str(id) + ".html", "w", encoding='utf-8')
        text_file.write(self.html)
        text_file.close()
        #yield (pages.Payment)

