from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        value = '1.非常不赞成'
        yield (pages.Survey,
               {'sur_q01': value, 'sur_q02': value, 'sur_q03': value, 'sur_q04': value, 'sur_q05': value, 'sur_q06': value,
                'sur_q07': value, 'sur_q08': value,
                'sur_q09': value, 'sur_q10': value, 'sur_q11': value, 'sur_q12': value, 'sur_q13': value, 'sur_q14': value,
                'sur_q15': value, 'sur_q16': value,
                'sur_q17': value, 'sur_q18': value, 'sur_q19': value,
                })
