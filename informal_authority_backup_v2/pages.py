from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


class IdentityChoiceColor(Page):
    '''
    IdentityChoiceColor：
        Identity 确定参与人的标签
        Choice 选01
        Color 用颜色来表示
    '''
    form_model = 'player'
    form_fields = ['choice_01']

    def is_displayed(self):
        return self.player.treatment == "choice_color"

    def vars_for_template(self):
        if self.player.id_in_group == 1:
            return {'color_1': Constants.label_color1, 'color_2': Constants.label_color2}
        else:
            return {'color_1': Constants.label_color2, 'color_2': Constants.label_color1}


class IdentityChoiceWl(Page):
    '''
    IdentityChoiceWl：
        Identity 确定参与人的标签
        Choice 选01
        Wl 用胜负方来表示
    '''
    form_model = 'player'
    form_fields = ['choice_01']

    def is_displayed(self):
        return self.player.treatment == "choice_wl"

    def vars_for_template(self):
        if self.player.id_in_group == 1:
            return {'wl_1': Constants.label_winner, 'wl_2': Constants.label_loser}
        else:
            return {'wl_1': Constants.label_loser, 'wl_2': Constants.label_winner}


class IdentityWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_label()


class NormalWaitPage(WaitPage):
    pass


class ShowLabel(Page):

    def vars_for_template(self):
        return {
            'choice_self': self.player.choice_01,
            'choice_partner': self.player.get_others_in_group()[0].choice_01,

            'label_self': self.player.label,
            'label_partner': self.player.get_others_in_group()[0].label,

            'correct_self': self.player.correct,
            'correct_partner': self.player.get_others_in_group()[0].correct,

            'is_compete': is_treatment_compete(self),
        }


class CooperationTest(Page):
    def vars_for_template(self):
        return {
            # 'choice_self': self.player.choice_01,
            # 'choice_partner': self.player.get_others_in_group()[0].choice_01,
            'label_self': self.player.label,
            'label_partner': self.player.get_others_in_group()[0].label,
        }


class CooperationChoice(Page):
    form_model = 'player'
    form_fields = ['choice_02']

    def vars_for_template(self):
        return {
            # 'choice_self': self.player.choice_01,
            # 'choice_partner': self.player.get_others_in_group()[0].choice_01,
            'label_self': self.player.label,
            'label_partner': self.player.get_others_in_group()[0].label,
        }


class CooperationResult(Page):
    pass


class Introduction(Page):
    pass


class IdentityCompeteGame(Page):
    form_model = 'player'
    form_fields = ['correct']

    def is_displayed(self):
        return is_treatment_compete(self)

    def get_timeout_seconds(self):
        return self.session.config['game_time_sec']


class IdentityCompeteIntro(Page):
    def is_displayed(self):
        return is_treatment_compete(self)

    def vars_for_template(self):
        m, s = divmod(self.session.config['game_time_sec'], 60)
        h, m = divmod(m, 60)
        if m>0:
            return {
                'timeout_string': ("%02d分%02d秒" % (m, s)),
                'correct_threshold': self.session.vars['correct_threshold']
            }
        else:
            return {
                'timeout_string': ("%02d秒" % (s)),
                'correct_threshold': self.session.vars['correct_threshold']
            }


def is_treatment_compete(page):
    return (page.player.treatment == "compete_wl") or (page.player.treatment == "compete_wl_color")


page_sequence = [

    Introduction,
    IdentityChoiceColor,
    IdentityChoiceWl,

    IdentityCompeteIntro,
    IdentityCompeteGame,

    IdentityWaitPage,
    ShowLabel,

    NormalWaitPage,
    CooperationTest,
    CooperationChoice,
    CooperationResult,

    Results
]
