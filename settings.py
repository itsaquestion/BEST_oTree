import os
from os import environ

import dj_database_url

import otree.settings

BROWSER_COMMAND = 'C:/Program Files/Mozilla Firefox/firefox.exe'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SENTRY_DSN = 'http://38b3b3045f244cf8bf5e8c9b60a4aa01:222bf70e524b4259a1723171cf59224f@sentry.otree.org/96'

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

# don't share this with anybody.
SECRET_KEY = 't9^m1wyod_ytgsu@#uvq+dwko5!a31=gpeg5dy1hg(^%9tw+9t'

# BROWSER_COMMAND = 'firefox'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = False

# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'zh-hans'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [{
    'name': 'pc_99',
    'display_name': 'Room of 99 PCs',
    'participant_label_file': '_rooms/pc_99.txt',
    'use_secure_urls': True,
},
]

mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7 * 24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': []
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.00,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    # {
    #     'name': 'words_numbers_v2',
    #     'display_name': "words_numbers_v2",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'preference_separation',
    #     ],
    #     'game_time_sec': 90,
    #     'points_for_one_yuan': 10,
    #     'debug_mode': False,
    #     'participation_fee': 2,
    # },
    # {
    #     'name': 'words_numbers_v2_debug',
    #     'display_name': "words_numbers_v2 debug mode",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'preference_separation',
    #     ],
    #     'game_time_sec': 90,
    #     'points_for_one_yuan': 10,
    #     'debug_mode': True,
    #     'participation_fee': 2,
    #
    # },
    # {
    #     'name': 'preference_separation',
    #     'display_name': "preference_separation",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'preference_separation',
    #     ],
    #     'game_time_sec': 90,
    #     'points_for_one_yuan': 1,
    #     'debug_mode': False,
    #     'participation_fee': 40,
    # },
    # {
    #     'name': 'preference_separation_debug',
    #     'display_name': "preference_separation debug mode",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'preference_separation',
    #     ],
    #     'game_time_sec': 15,
    #     'points_for_one_yuan': 1,
    #     'debug_mode': True,
    #     'participation_fee': 40,
    #
    # },
    # {
    #     'name': 'informal_authority',
    #     'display_name': "Informal Authority",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'informal_authority',
    #     ],
    #     # 'treatment': 'choice_color',
    #     'points_for_one_yuan': 10,
    #     'correct_threshold': 10,
    #     'game_time_sec': 480,
    #     'matrix_x': 15,
    #     'matrix_y': 5,
    #     'debug_mode': False,
    #     'participation_fee': 15,
    # },
    #
    # {
    #     'name': 'informal_authority_debug',
    #     'display_name': "Informal Authority Debug ",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'informal_authority',
    #     ],
    #     # 'treatment': 'choice_color',
    #     'points_for_one_yuan': 10,
    #     'correct_threshold': 10,
    #     'game_time_sec': 30,
    #     'matrix_x': 15,
    #     'matrix_y': 5,
    #     'debug_mode': True,
    #     'participation_fee': 15,
    # },
    #
    # {
    #     'name': 'informal_authority_debug_treatment_color',
    #     'display_name': "Informal Authority Debug (treatment: choice + color)",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'informal_authority',
    #     ],
    #     'treatment': ['choice_color'],
    #     'points_for_one_yuan': 10,
    #     'correct_threshold': 10,
    #     'game_time_sec': 30,
    #     'matrix_x': 15,
    #     'matrix_y': 5,
    #     'debug_mode': True,
    #     'participation_fee': 15,
    # },
    # {
    #     'name': 'informal_authority_debug_treatment_wl',
    #     'display_name': "Informal Authority Debug (treatment: choice + winner/loser)",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'informal_authority',
    #     ],
    #     'treatment': ['choice_wl'],
    #     'points_for_one_yuan': 10,
    #     'correct_threshold': 10,
    #     'game_time_sec': 30,
    #     'matrix_x': 15,
    #     'matrix_y': 5,
    #     'debug_mode': True,
    #     'participation_fee': 15,
    # },
    #
    # {
    #     'name': 'informal_authority_debug_treatment_compete',
    #     'display_name': "Informal Authority Debug (treatment: compete + winner/loser)",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'informal_authority',
    #     ],
    #     'treatment': ['compete_wl'],
    #     'points_for_one_yuan': 10,
    #     'correct_threshold': 10,
    #     'game_time_sec': 30,
    #     'matrix_x': 15,
    #     'matrix_y': 5,
    #     'debug_mode': True,
    #     'participation_fee': 15,
    # },
    #
    # {
    #     'name': 'informal_authority_treatment_compete',
    #     'display_name': "Informal Authority (treatment: compete)",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'informal_authority',
    #     ],
    #     'treatment': ['compete_wl'],
    #     'points_for_one_yuan': 10,
    #     'correct_threshold': 10,
    #     'game_time_sec': 480,
    #     'matrix_x': 15,
    #     'matrix_y': 5,
    #     'debug_mode': False,
    #     'participation_fee': 15,
    # },
    #
    # {
    #     'name': 'informal_authority_treatment_choice_x2',
    #     'display_name': "Informal Authority (treatment: choice x2)",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'informal_authority',
    #     ],
    #     'treatment': ['choice_color', 'choice_wl'],
    #     'points_for_one_yuan': 10,
    #     'correct_threshold': 10,
    #     'game_time_sec': 480,
    #     'matrix_x': 15,
    #     'matrix_y': 5,
    #     'debug_mode': False,
    #     'participation_fee': 15,
    # },
    {
        'name': 'informal_authority_treatment_selection',
        'display_name': "Informal Authority (treatment selection)",
        'num_demo_participants': 2,
        'app_sequence': [
            'informal_authority',
        ],
        'Treatment_choice_color': True,
        'Treatment_choice_wl': True,
        'Treatment_compete_wl': True,
        'Treatment_compete_wl_practice': True,
        'Treatment_compete_wl_practice_reward': True,
        'Treatment_compete_wl_reward_showafter': True,
        'Treatment_choice_wl_tips': True,
        'Treatment_compete_wl_tips': True,
        'points_for_one_yuan': 10,
        'correct_threshold': 10,
        'game_time_sec': 480,
        'matrix_x': 15,
        'matrix_y': 5,
        'debug_mode': False,
        'participation_fee': 15,
    },
    {
        'name': 'informal_authority_debug_treatment_selection',
        'display_name': "Informal Authority Debug (treatment selection)",
        'num_demo_participants': 2,
        'app_sequence': [
            'informal_authority',
        ],
        'Treatment_choice_color': True,
        'Treatment_choice_wl': True,
        'Treatment_compete_wl': True,
        'Treatment_compete_wl_practice': True,
        'Treatment_compete_wl_practice_reward': True,
        'Treatment_compete_wl_reward_showafter': True,
        'Treatment_choice_wl_tips': True,
        'Treatment_compete_wl_tips': True,
        'points_for_one_yuan': 10,
        'correct_threshold': 10,
        'game_time_sec': 15,
        'matrix_x': 15,
        'matrix_y': 5,
        'debug_mode': True,
        'participation_fee': 15,
    },
    {
        'name': 'repeat_prisoner_debug',
        'display_name': "Repeat Prisoner's Dilemma (测试用)",
        'num_demo_participants': 2,
        'app_sequence': ['repeat_prisoner'],
        'debug_mode': True,
    },
    {
        'name': 'repeat_prisoner',
        'display_name': "Repeat Prisoner's Dilemma (正式用)",
        'num_demo_participants': 2,
        'app_sequence': ['repeat_prisoner'],
        'debug_mode': False,
    },
    {
        'name': 'coase_debug_24',
        'display_name': "Coase Theorem (Debug 24P)",
        'num_demo_participants': 24,
        'app_sequence': [
            'Coase'
        ],
        'points_for_one_yuan': 10,
        'game_time_sec': 15,
        'debug_mode': True,
        'participation_fee': 15,
        'high_value': 189,
        'low_value': 99
    },
    {
        'name': 'coase_debug_8',
        'display_name': "Coase Theorem (Debug 8P)",
        'num_demo_participants': 8,
        'app_sequence': [
            'Coase'
        ],
        'points_for_one_yuan': 10,
        'game_time_sec': 15,
        'debug_mode': True,
        'participation_fee': 15,
        'high_value': 189,
        'low_value': 99
    },
    {
        'name': 'public_goods_survey_risk',
        'display_name': "Public Goods",
        'num_demo_participants': 3,
        'points_for_one_yuan': 10,
        'app_sequence': ['public_goods', 'survey_risk'],
    },
    {
        'name': 'survey_risk',
        'display_name': "Survey: Risk",
        'num_demo_participants': 1,
        'points_for_one_yuan': 10,
        'app_sequence': ['survey_risk'],
    },
    # {
    #     'name': 'survey',
    #     'display_name': "Survey",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['survey', 'payment_info'],
    # },
    # {
    #     'name': 'quiz',
    #     'display_name': "Quiz",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['quiz'],
    # },
    # {
    #     'name': 'informal_authority_treatment_compete_color',
    #     'display_name': "Informal Authority Debug (treatment: compete + winner/loser + color)",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'informal_authority',
    #     ],
    #     'treatment': 'compete_wl_color',
    #     'points_for_one_yuan': 10,
    #     'correct_threshold': 10,
    #     'game_time_sec': 30,
    #     'matrix_x': 15,
    #     'matrix_y': 10,
    #     'debug_mode': True,
    #     'participation_fee': 15,
    # },

]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
