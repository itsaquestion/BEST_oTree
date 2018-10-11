from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'informal_authority'
    players_per_group = 2
    num_rounds = 1

    label_color1 = "天蓝方"
    label_color2 = "海蓝方"

    label_winner = "胜方"
    label_loser = "败方"

    label_color_loser1 = "天蓝败方"
    label_color_loser2 = "海蓝败方"


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        self.session.vars['is_debug'] = self.session.config['debug_mode']
        self.session.vars['matrix_x'] = self.session.config['matrix_x']
        self.session.vars['matrix_y'] = self.session.config['matrix_y']
        self.session.vars['game_time_sec'] = self.session.config['game_time_sec']
        self.session.vars['correct_threshold'] = self.session.config['correct_threshold']

        if self.round_number == 1:
            for g in self.get_groups():
                if 'treatment' in self.session.config:
                    g.set_treatment(self.session.config['treatment'])
                else:
                    g.set_treatment(random.choice(['choice_color', 'choice_wl', 'compete_wl', 'compete_wl_color']))


class Group(BaseGroup):
    def set_treatment(self, treatment):
        for p in self.get_players():
            p.treatment = treatment

    def set_label(self):
        '''
        根据treatment的不同设定不同的label
        '''
        if self.get_player_by_id(1).treatment == "choice_color":
            self.set_label_color()

        if self.get_player_by_id(1).treatment == "choice_wl":
            self.set_label_wl()

        if self.get_player_by_id(1).treatment == "compete_wl":
            self.set_label_compete_wl()

        if self.get_player_by_id(1).treatment == "compete_wl_color":
            self.set_label_compete_wl_color()

    def set_label_compete_wl_color(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        n = self.session.vars['correct_threshold']

        if p1.correct < n and p2.correct < n:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser

        if p1.correct >= n and p1.correct > p2.correct:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser

        if p2.correct >= n and p2.correct > p1.correct:
            p2.label = Constants.label_winner
            p1.label = Constants.label_loser

        # 平局p1算胜利者，因为p1p2本身已经是随机设定的。
        if p1.correct == p2.correct:
            p1.label = Constants.label_color_loser1
            p2.label = Constants.label_color_loser2

    def set_label_compete_wl(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.correct > p2.correct:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser

        if p1.correct < p2.correct:
            p1.label = Constants.label_loser
            p2.label = Constants.label_winner

        # 平局p1算胜利者，因为p1p2本身已经是随机设定的。
        if p1.correct == p2.correct:
            p1.label = Constants.label_color_loser1
            p2.label = Constants.label_color_loser2

    def set_label_color(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.choice_01 == p2.choice_01:
            p1.label = Constants.label_color1
            p2.label = Constants.label_color2
        else:
            p1.label = Constants.label_color2
            p2.label = Constants.label_color1

    def set_label_wl(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.choice_01 == p2.choice_01:
            p1.label = Constants.label_winner
            p2.label = Constants.label_loser
        else:
            p1.label = Constants.label_loser
            p2.label = Constants.label_winner


class Player(BasePlayer):
    treatment = models.StringField()
    label = models.StringField()

    choice_01 = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[0, 1]
    )

    choice_02 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["X", "Y"]
    )

    correct = models.IntegerField()
