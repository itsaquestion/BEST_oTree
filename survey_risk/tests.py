from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Survey,
               {'sur_q01': '接受', 'sur_q02': '接受', 'sur_q03': '接受',
                'sur_q04': '接受', 'sur_q05': '接受', 'sur_q06': '接受',
                'sur_q07': '接受', 'sur_q08': '接受', })
