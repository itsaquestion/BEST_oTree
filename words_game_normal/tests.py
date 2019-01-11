from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random
from otree.api import Submission

class PlayerBot(Bot):
    # Intro,
    # Practice,
    # BeginWaitPage,
    # Game01,
    # RestWaitPage,
    # Rest,
    # Game02,
    # ResultsWaitPage,
    # Results
    def play_round(self):
        if self.round_number == 1:
            yield (pages.Intro)
            yield (pages.Practice)

        n = random.randint(2, 10)
        yield (pages.Game01, {'total_01': n, 'correct_01': n - 2})

        yield Submission(pages.Rest,timeout_happened=True)

        n = random.randint(2, 10)
        yield (pages.Game01, {'total_02': n, 'correct_02': n - 2})

        yield (pages.Results)