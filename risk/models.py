from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

h = ['A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失20.0代币',
     'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失40.0代币', 'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失60.0代币',
     'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失80.0代币', 'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失100.0代币',
     'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失120.0代币', 'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失140.0代币',
     'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失160.0代币', 'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失180.0代币',
     'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失200.0代币', 'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失240.0代币',
     'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失280.0代币', 'A: 50%可能损失400代币，也有50%的可能损失0代币----B：100%损失320.0代币',
     'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失24.5代币', 'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失44.0代币',
     'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失63.5代币', 'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失83.0代币',
     'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失102.5代币', 'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失122.0代币',
     'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失141.5代币', 'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失161.0代币',
     'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失180.5代币', 'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失200.0代币',
     'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失239.0代币', 'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失278.0代币',
     'A: 50%可能损失395代币，也有50%的可能损失5代币----B：100%损失317.0代币', 'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失29.0代币',
     'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失48.0代币', 'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失67.0代币',
     'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失86.0代币', 'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失105.0代币',
     'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失124.0代币', 'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失143.0代币',
     'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失162.0代币', 'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失181.0代币',
     'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失200.0代币', 'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失238.0代币',
     'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失276.0代币',
     'A: 50%可能损失390代币，也有50%的可能损失10代币----B：100%损失314.0代币', 'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失33.5代币',
     'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失52.0代币', 'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失70.5代币',
     'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失89.0代币', 'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失107.5代币',
     'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失126.0代币', 'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失144.5代币',
     'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失163.0代币', 'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失181.5代币',
     'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失200.0代币', 'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失237.0代币',
     'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失274.0代币', 'A: 50%可能损失385代币，也有50%的可能损失15代币----B：100%损失311.0代币',
     'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失38.0代币', 'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失56.0代币',
     'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失74.0代币', 'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失92.0代币',
     'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失110.0代币', 'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失128.0代币',
     'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失146.0代币', 'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失164.0代币',
     'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失182.0代币', 'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失200.0代币',
     'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失236.0代币', 'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失272.0代币',
     'A: 50%可能损失380代币，也有50%的可能损失20代币----B：100%损失308.0代币', 'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失42.5代币',
     'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失60.0代币', 'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失77.5代币',
     'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失95.0代币', 'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失112.5代币',
     'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失130.0代币', 'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失147.5代币',
     'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失165.0代币', 'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失182.5代币',
     'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失200.0代币',
     'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失235.0代币', 'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失270.0代币',
     'A: 50%可能损失375代币，也有50%的可能损失25代币----B：100%损失305.0代币']

m = ['A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失96.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失108.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失119.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失131.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失142.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失154.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失165.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失177.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失188.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失200.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失223.0代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失246.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失269.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失101.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失112.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失123.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失134.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失145.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失156.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失167.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失178.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失189.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失200.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失222.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失244.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失266.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失105.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失116.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失126.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失137.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失147.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失158.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失168.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失179.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失189.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失200.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失221.0代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失242.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失263.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失110.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失120.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失130.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失140.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失150.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失160.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失170.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失180.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失190.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失200.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失220.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失240.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失260.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失114.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失124.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失133.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失143.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失152.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失162.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失171.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失181.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失190.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失200.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失219.0代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失238.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失257.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失119.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失128.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失137.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失146.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失155.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失164.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失173.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失182.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失191.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失200.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失218.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失236.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失254.0代币']

l = ['A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失173.0代币', 'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失176.0代币',
     'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失179.0代币', 'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失182.0代币',
     'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失185.0代币', 'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失188.0代币',
     'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失191.0代币', 'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失194.0代币',
     'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失197.0代币', 'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失200.0代币',
     'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失206.0代币', 'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失212.0代币',
     'A: 50%可能损失230代币，也有50%的可能损失170代币----B：100%损失218.0代币', 'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失177.5代币',
     'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失180.0代币', 'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失182.5代币',
     'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失185.0代币', 'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失187.5代币',
     'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失190.0代币', 'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失192.5代币',
     'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失195.0代币', 'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失197.5代币',
     'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失200.0代币', 'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失205.0代币',
     'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失210.0代币', 'A: 50%可能损失225代币，也有50%的可能损失175代币----B：100%损失215.0代币',
     'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失182.0代币', 'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失184.0代币',
     'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失186.0代币', 'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失188.0代币',
     'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失190.0代币', 'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失192.0代币',
     'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失194.0代币', 'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失196.0代币',
     'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失198.0代币', 'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失200.0代币',
     'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失204.0代币', 'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失208.0代币',
     'A: 50%可能损失220代币，也有50%的可能损失180代币----B：100%损失212.0代币', 'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失186.5代币',
     'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失188.0代币', 'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失189.5代币',
     'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失191.0代币', 'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失192.5代币',
     'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失194.0代币', 'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失195.5代币',
     'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失197.0代币', 'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失198.5代币',
     'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失200.0代币', 'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失203.0代币',
     'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失206.0代币', 'A: 50%可能损失215代币，也有50%的可能损失185代币----B：100%损失209.0代币',
     'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失191.0代币', 'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失192.0代币',
     'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失193.0代币', 'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失194.0代币',
     'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失195.0代币', 'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失196.0代币',
     'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失197.0代币', 'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失198.0代币',
     'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失199.0代币', 'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失200.0代币',
     'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失202.0代币', 'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失204.0代币',
     'A: 50%可能损失210代币，也有50%的可能损失190代币----B：100%损失206.0代币', 'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失195.5代币',
     'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失196.0代币', 'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失196.5代币',
     'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失197.0代币', 'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失197.5代币',
     'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失198.0代币', 'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失198.5代币',
     'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失199.0代币', 'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失199.5代币',
     'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失200.0代币', 'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失201.0代币',
     'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失202.0代币', 'A: 50%可能损失205代币，也有50%的可能损失195代币----B：100%损失203.0代币']

m2 = ['A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失96.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失108.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失119.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失131.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失142.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失154.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失165.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失177.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失188.5代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失200.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失223.0代币', 'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失246.0代币',
     'A: 50%可能损失315代币，也有50%的可能损失85代币----B：100%损失269.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失101.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失112.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失123.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失134.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失145.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失156.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失167.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失178.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失189.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失200.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失222.0代币',
     'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失244.0代币', 'A: 50%可能损失310代币，也有50%的可能损失90代币----B：100%损失266.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失105.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失116.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失126.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失137.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失147.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失158.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失168.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失179.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失189.5代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失200.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失221.0代币', 'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失242.0代币',
     'A: 50%可能损失305代币，也有50%的可能损失95代币----B：100%损失263.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失110.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失120.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失130.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失140.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失150.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失160.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失170.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失180.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失190.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失200.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失220.0代币',
     'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失240.0代币', 'A: 50%可能损失300代币，也有50%的可能损失100代币----B：100%损失260.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失114.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失124.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失133.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失143.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失152.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失162.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失171.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失181.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失190.5代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失200.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失219.0代币', 'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失238.0代币',
     'A: 50%可能损失295代币，也有50%的可能损失105代币----B：100%损失257.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失119.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失128.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失137.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失146.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失155.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失164.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失173.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失182.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失191.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失200.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失218.0代币',
     'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失236.0代币', 'A: 50%可能损失290代币，也有50%的可能损失110代币----B：100%损失254.0代币']


author = 'Guo Yu chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'risk_breeds'
    players_per_group = 3
    num_rounds = 12
    endowment = c(400)
    tasks = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6']
    tasks1 = ['M7', 'M8', 'M9', 'M10', 'M11', 'M12']


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, 7))
                random.shuffle(round_numbers)
                p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
                round_numbers1 = list(range(7, 13))
                random.shuffle(round_numbers1)
                p.participant.vars['task_rounds1'] = dict(zip(Constants.tasks1, round_numbers1))

            #self.session.vars['is_debug'] = self.session.config['debug_mode']
            #self.session.vars['matrix_x'] = self.session.config['matrix_x']
            #self.session.vars['matrix_y'] = self.session.config['matrix_y']
            #self.session.vars['game_time_sec'] = self.session.config['game_time_sec']


class Group(BaseGroup):
    pass

def make_hrisk_field(n : int):
    return models.StringField(
        choices=['A', 'B'],
        verbose_name=h[n],
        widget=widgets.RadioSelectHorizontal
    )


def make_mrisk_field(n: int):
    return models.StringField(
        choices=['A', 'B'],
        verbose_name=m[n],
        widget=widgets.RadioSelectHorizontal
    )

def make_lrisk_field(n: int):
    return models.StringField(
        choices=['A', 'B'],
        verbose_name=l[n],
        widget=widgets.RadioSelectHorizontal
    )

def make_m2risk_field(n: int):
    return models.StringField(
        choices=['A', 'B'],
        verbose_name=m2[n],
        widget=widgets.RadioSelectHorizontal
    )

class Player(BasePlayer):
    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.participant.vars['expiry'] - time.time() > 3
    pay_round = models.IntegerField()
    choice = models.StringField()
    payoff_choice = models.IntegerField()
    #count_number = models.IntegerField()

    sur_birth_year = models.StringField(
        choices=['03', '02', '01', '00', '99', '98', '97', '96', '95', '94'],
        verbose_name="1.你出生的年份是(请填后面2位数)",
        widget=widgets.RadioSelectHorizontal)
    sur_birth_month = models.StringField(
        choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        verbose_name="你出生的月份是(1-12)", min=1, max=12,
        widget=widgets.RadioSelectHorizontal)
    sur_place = models.StringField(verbose_name="7.你的籍贯省份是（如:福建，上海）")
    sur_nation = models.StringField(
        choices=['汉族', '其它'],
        verbose_name="8.你的民族是",
        widget=widgets.RadioSelectHorizontal)
    sur_gender = models.StringField(
        choices=['男', '女'],
        verbose_name="2.你的性别是",
        widget=widgets.RadioSelectHorizontal)
    sur_grade = models.StringField(
        choices=['大一', '大二', '大三', '大四', '研一', '研二', '研三'],
        verbose_name="3.你就读的年级为",
        widget=widgets.RadioSelectHorizontal)
    sur_school = models.StringField(
        verbose_name="4.你就读的学院为")
    sur_economy = models.StringField(
        verbose_name="9.可以写是否修过/正在学习经济学类的课程",
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )

    sur_height = models.IntegerField(verbose_name="10.你的身高是(cm)")
    sur_weight = models.IntegerField(verbose_name="11.你的体重是（kg）")
    sur_cash = models.IntegerField(verbose_name="12.你每个月的生活费是多少（元）")
    sur_big_brother = models.IntegerField(verbose_name="13.你有几个哥哥（没有请填0）")
    sur_little_brother = models.IntegerField(verbose_name="你有几个弟弟（没有请填0）")
    sur_big_sister = models.IntegerField(verbose_name="你有几个姐姐（没有请填0）")
    sur_little_sister = models.IntegerField(verbose_name="你有几个妹妹（没有请填0）")
    sur_mother = models.StringField(
        choices=['小学及以下', '初中', '高中', '中专', '大专', '大学及以上'],
        verbose_name="14.母亲的最高学历",
        widget = widgets.RadioSelectHorizontal)
    sur_father = models.StringField(
        choices=['小学及以下', '初中', '高中', '中专', '大专', '大学及以上'],
        verbose_name="父亲的最高学历",
        widget=widgets.RadioSelectHorizontal)
    sur_come_from = models.StringField(
        verbose_name="15.你是来自农村还是城镇",
        choices=['农村', '城镇'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_income = models.StringField(
        verbose_name="16.你的家庭年收入是什么范围",
        choices=['5万以下', '5万-10万', '10万-25万', '25万-50万', '50万-100万', '100万以上'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_party_member = models.StringField(
        verbose_name="5.你是否为党员",
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_student_leader = models.StringField(
        verbose_name="6.你是否为学生干部",
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )
    sur_left_behind = models.StringField(verbose_name="17.是否11岁之前有过以下经历",
                                        choices=['与父亲分离连续长达12个月及以上', '与母亲分离连续长达12个月及以上',
                                                 '以上两种经历都有', '以上两种经历都没有'],
                                        widget=widgets.RadioSelect
                                        )
    sur_risk = models.StringField(
        verbose_name="18.在现实生活中遇到以下情况，你将会选择哪个",
        choices=['有100%的机会赢取1000元现金', '有50%的机会赢取5万元现金',
                 '有25%的机会赢取50万元现金', '有10%的机会赢取100万元现金',
                 ],
        widget=widgets.RadioSelect
    )

    # sur_risk = models.StringField(
    #     verbose_name="18.在现实生活中遇到以下情况，你将会选择哪个",
    #     choices=['0.1%的可能性损失10万元, 否则,损失0元', '1%的可能性损失1万元, 否则,损失0元',
    #              '10%的可能性损失1000元, 否则,损失0元', '25%的可能性损失400元, 否则,损失0元',
    #              '50%的可能性损失200元, 否则,损失0元', '75%的可能性损失133元, 否则,损失0元',
    #              '100%的可能性损失100元'],
    #     widget=widgets.RadioSelect
    # )
    sur_risk1 = models.StringField(
        verbose_name="19.以下哪项描述最符合你的投资态度？",
        choices=['厌恶风险，不希望本金损失，希望获得稳定回报', '保守投资，不希望本金损失，愿意承担一定幅度的收益波动',
                 '寻求资金的较高收益和成长性，愿意为此承担有限本金损失', '希望赚取高回报，愿意为此承担较大本金损失'],
        widget=widgets.RadioSelect
    )
    sur_risk2 = models.StringField(
        verbose_name="20.假设有两种投资：投资A预期获得10%的收益，可能承担的损失非常小；投资B预期获得30%的收益，"
                     "但可能承担较大亏损。您会怎么支配您的投资？",
        choices=['全部投资于收益较小且风险较小的A',"同时投资于A和B，但大部分资金投资于收益较小且风险较小的A",
                 "同时投资于A和B，但大部分资金投资于收益较大且风险较大的B","全部投资于收益较大且风险较大的B"],
        widget=widgets.RadioSelect
    )
    sur_risk3 = models.StringField(
        verbose_name="21.你认为自己能承受的最大投资损失是多少？",
        choices=['10%以内','10%-30%','30%-50%','超过50%'],
        widget=widgets.RadioSelectHorizontal
    )



    mhf01 = make_hrisk_field(0)
    mhf02 = make_hrisk_field(1)
    mhf03 = make_hrisk_field(2)
    mhf04 = make_hrisk_field(3)
    mhf05 = make_hrisk_field(4)
    mhf06 = make_hrisk_field(5)
    mhf07 = make_hrisk_field(6)
    mhf08 = make_hrisk_field(7)
    mhf09 = make_hrisk_field(8)
    mhf10 = make_hrisk_field(9)
    mhf11 = make_hrisk_field(10)
    mhf12 = make_hrisk_field(11)
    mhf13 = make_hrisk_field(12)
    mhf14 = make_hrisk_field(13)
    mhf15 = make_hrisk_field(14)
    mhf16 = make_hrisk_field(15)
    mhf17 = make_hrisk_field(16)
    mhf18 = make_hrisk_field(17)
    mhf19 = make_hrisk_field(18)
    mhf20 = make_hrisk_field(19)
    mhf21 = make_hrisk_field(20)
    mhf22 = make_hrisk_field(21)
    mhf23 = make_hrisk_field(22)
    mhf24 = make_hrisk_field(23)
    mhf25 = make_hrisk_field(24)
    mhf26 = make_hrisk_field(25)
    mhf27 = make_hrisk_field(26)
    mhf28 = make_hrisk_field(27)
    mhf29 = make_hrisk_field(28)
    mhf30 = make_hrisk_field(29)
    mhf31 = make_hrisk_field(30)
    mhf32 = make_hrisk_field(31)
    mhf33 = make_hrisk_field(32)
    mhf34 = make_hrisk_field(33)
    mhf35 = make_hrisk_field(34)
    mhf36 = make_hrisk_field(35)
    mhf37 = make_hrisk_field(36)
    mhf38 = make_hrisk_field(37)
    mhf39 = make_hrisk_field(38)
    mhf40 = make_hrisk_field(39)
    mhf41 = make_hrisk_field(40)
    mhf42 = make_hrisk_field(41)
    mhf43 = make_hrisk_field(42)
    mhf44 = make_hrisk_field(43)
    mhf45 = make_hrisk_field(44)
    mhf46 = make_hrisk_field(45)
    mhf47 = make_hrisk_field(46)
    mhf48 = make_hrisk_field(47)
    mhf49 = make_hrisk_field(48)
    mhf50 = make_hrisk_field(49)
    mhf51 = make_hrisk_field(50)
    mhf52 = make_hrisk_field(51)
    mhf53 = make_hrisk_field(52)
    mhf54 = make_hrisk_field(53)
    mhf55 = make_hrisk_field(54)
    mhf56 = make_hrisk_field(55)
    mhf57 = make_hrisk_field(56)
    mhf58 = make_hrisk_field(57)
    mhf59 = make_hrisk_field(58)
    mhf60 = make_hrisk_field(59)
    mhf61 = make_hrisk_field(60)
    mhf62 = make_hrisk_field(61)
    mhf63 = make_hrisk_field(62)
    mhf64 = make_hrisk_field(63)
    mhf65 = make_hrisk_field(64)
    mhf66 = make_hrisk_field(65)
    mhf67 = make_hrisk_field(66)
    mhf68 = make_hrisk_field(67)
    mhf69 = make_hrisk_field(68)
    mhf70 = make_hrisk_field(69)
    mhf71 = make_hrisk_field(70)
    mhf72 = make_hrisk_field(71)
    mhf73 = make_hrisk_field(72)
    mhf74 = make_hrisk_field(73)
    mhf75 = make_hrisk_field(74)
    mhf76 = make_hrisk_field(75)
    mhf77 = make_hrisk_field(76)
    mhf78 = make_hrisk_field(77)

    mmf01 = make_mrisk_field(0)
    mmf02 = make_mrisk_field(1)
    mmf03 = make_mrisk_field(2)
    mmf04 = make_mrisk_field(3)
    mmf05 = make_mrisk_field(4)
    mmf06 = make_mrisk_field(5)
    mmf07 = make_mrisk_field(6)
    mmf08 = make_mrisk_field(7)
    mmf09 = make_mrisk_field(8)
    mmf10 = make_mrisk_field(9)
    mmf11 = make_mrisk_field(10)
    mmf12 = make_mrisk_field(11)
    mmf13 = make_mrisk_field(12)
    mmf14 = make_mrisk_field(13)
    mmf15 = make_mrisk_field(14)
    mmf16 = make_mrisk_field(15)
    mmf17 = make_mrisk_field(16)
    mmf18 = make_mrisk_field(17)
    mmf19 = make_mrisk_field(18)
    mmf20 = make_mrisk_field(19)
    mmf21 = make_mrisk_field(20)
    mmf22 = make_mrisk_field(21)
    mmf23 = make_mrisk_field(22)
    mmf24 = make_mrisk_field(23)
    mmf25 = make_mrisk_field(24)
    mmf26 = make_mrisk_field(25)
    mmf27 = make_mrisk_field(26)
    mmf28 = make_mrisk_field(27)
    mmf29 = make_mrisk_field(28)
    mmf30 = make_mrisk_field(29)
    mmf31 = make_mrisk_field(30)
    mmf32 = make_mrisk_field(31)
    mmf33 = make_mrisk_field(32)
    mmf34 = make_mrisk_field(33)
    mmf35 = make_mrisk_field(34)
    mmf36 = make_mrisk_field(35)
    mmf37 = make_mrisk_field(36)
    mmf38 = make_mrisk_field(37)
    mmf39 = make_mrisk_field(38)
    mmf40 = make_mrisk_field(39)
    mmf41 = make_mrisk_field(40)
    mmf42 = make_mrisk_field(41)
    mmf43 = make_mrisk_field(42)
    mmf44 = make_mrisk_field(43)
    mmf45 = make_mrisk_field(44)
    mmf46 = make_mrisk_field(45)
    mmf47 = make_mrisk_field(46)
    mmf48 = make_mrisk_field(47)
    mmf49 = make_mrisk_field(48)
    mmf50 = make_mrisk_field(49)
    mmf51 = make_mrisk_field(50)
    mmf52 = make_mrisk_field(51)
    mmf53 = make_mrisk_field(52)
    mmf54 = make_mrisk_field(53)
    mmf55 = make_mrisk_field(54)
    mmf56 = make_mrisk_field(55)
    mmf57 = make_mrisk_field(56)
    mmf58 = make_mrisk_field(57)
    mmf59 = make_mrisk_field(58)
    mmf60 = make_mrisk_field(59)
    mmf61 = make_mrisk_field(60)
    mmf62 = make_mrisk_field(61)
    mmf63 = make_mrisk_field(62)
    mmf64 = make_mrisk_field(63)
    mmf65 = make_mrisk_field(64)
    mmf66 = make_mrisk_field(65)
    mmf67 = make_mrisk_field(66)
    mmf68 = make_mrisk_field(67)
    mmf69 = make_mrisk_field(68)
    mmf70 = make_mrisk_field(69)
    mmf71 = make_mrisk_field(70)
    mmf72 = make_mrisk_field(71)
    mmf73 = make_mrisk_field(72)
    mmf74 = make_mrisk_field(73)
    mmf75 = make_mrisk_field(74)
    mmf76 = make_mrisk_field(75)
    mmf77 = make_mrisk_field(76)
    mmf78 = make_mrisk_field(77)

    mlf01 = make_lrisk_field(0)
    mlf02 = make_lrisk_field(1)
    mlf03 = make_lrisk_field(2)
    mlf04 = make_lrisk_field(3)
    mlf05 = make_lrisk_field(4)
    mlf06 = make_lrisk_field(5)
    mlf07 = make_lrisk_field(6)
    mlf08 = make_lrisk_field(7)
    mlf09 = make_lrisk_field(8)
    mlf10 = make_lrisk_field(9)
    mlf11 = make_lrisk_field(10)
    mlf12 = make_lrisk_field(11)
    mlf13 = make_lrisk_field(12)
    mlf14 = make_lrisk_field(13)
    mlf15 = make_lrisk_field(14)
    mlf16 = make_lrisk_field(15)
    mlf17 = make_lrisk_field(16)
    mlf18 = make_lrisk_field(17)
    mlf19 = make_lrisk_field(18)
    mlf20 = make_lrisk_field(19)
    mlf21 = make_lrisk_field(20)
    mlf22 = make_lrisk_field(21)
    mlf23 = make_lrisk_field(22)
    mlf24 = make_lrisk_field(23)
    mlf25 = make_lrisk_field(24)
    mlf26 = make_lrisk_field(25)
    mlf27 = make_lrisk_field(26)
    mlf28 = make_lrisk_field(27)
    mlf29 = make_lrisk_field(28)
    mlf30 = make_lrisk_field(29)
    mlf31 = make_lrisk_field(30)
    mlf32 = make_lrisk_field(31)
    mlf33 = make_lrisk_field(32)
    mlf34 = make_lrisk_field(33)
    mlf35 = make_lrisk_field(34)
    mlf36 = make_lrisk_field(35)
    mlf37 = make_lrisk_field(36)
    mlf38 = make_lrisk_field(37)
    mlf39 = make_lrisk_field(38)
    mlf40 = make_lrisk_field(39)
    mlf41 = make_lrisk_field(40)
    mlf42 = make_lrisk_field(41)
    mlf43 = make_lrisk_field(42)
    mlf44 = make_lrisk_field(43)
    mlf45 = make_lrisk_field(44)
    mlf46 = make_lrisk_field(45)
    mlf47 = make_lrisk_field(46)
    mlf48 = make_lrisk_field(47)
    mlf49 = make_lrisk_field(48)
    mlf50 = make_lrisk_field(49)
    mlf51 = make_lrisk_field(50)
    mlf52 = make_lrisk_field(51)
    mlf53 = make_lrisk_field(52)
    mlf54 = make_lrisk_field(53)
    mlf55 = make_lrisk_field(54)
    mlf56 = make_lrisk_field(55)
    mlf57 = make_lrisk_field(56)
    mlf58 = make_lrisk_field(57)
    mlf59 = make_lrisk_field(58)
    mlf60 = make_lrisk_field(59)
    mlf61 = make_lrisk_field(60)
    mlf62 = make_lrisk_field(61)
    mlf63 = make_lrisk_field(62)
    mlf64 = make_lrisk_field(63)
    mlf65 = make_lrisk_field(64)
    mlf66 = make_lrisk_field(65)
    mlf67 = make_lrisk_field(66)
    mlf68 = make_lrisk_field(67)
    mlf69 = make_lrisk_field(68)
    mlf70 = make_lrisk_field(69)
    mlf71 = make_lrisk_field(70)
    mlf72 = make_lrisk_field(71)
    mlf73 = make_lrisk_field(72)
    mlf74 = make_lrisk_field(73)
    mlf75 = make_lrisk_field(74)
    mlf76 = make_lrisk_field(75)
    mlf77 = make_lrisk_field(76)
    mlf78 = make_lrisk_field(77)

    mm2f01 = make_m2risk_field(0)
    mm2f02 = make_m2risk_field(1)
    mm2f03 = make_m2risk_field(2)
    mm2f04 = make_m2risk_field(3)
    mm2f05 = make_m2risk_field(4)
    mm2f06 = make_m2risk_field(5)
    mm2f07 = make_m2risk_field(6)
    mm2f08 = make_m2risk_field(7)
    mm2f09 = make_m2risk_field(8)
    mm2f10 = make_m2risk_field(9)
    mm2f11 = make_m2risk_field(10)
    mm2f12 = make_m2risk_field(11)
    mm2f13 = make_m2risk_field(12)
    mm2f14 = make_m2risk_field(13)
    mm2f15 = make_m2risk_field(14)
    mm2f16 = make_m2risk_field(15)
    mm2f17 = make_m2risk_field(16)
    mm2f18 = make_m2risk_field(17)
    mm2f19 = make_m2risk_field(18)
    mm2f20 = make_m2risk_field(19)
    mm2f21 = make_m2risk_field(20)
    mm2f22 = make_m2risk_field(21)
    mm2f23 = make_m2risk_field(22)
    mm2f24 = make_m2risk_field(23)
    mm2f25 = make_m2risk_field(24)
    mm2f26 = make_m2risk_field(25)
    mm2f27 = make_m2risk_field(26)
    mm2f28 = make_m2risk_field(27)
    mm2f29 = make_m2risk_field(28)
    mm2f30 = make_m2risk_field(29)
    mm2f31 = make_m2risk_field(30)
    mm2f32 = make_m2risk_field(31)
    mm2f33 = make_m2risk_field(32)
    mm2f34 = make_m2risk_field(33)
    mm2f35 = make_m2risk_field(34)
    mm2f36 = make_m2risk_field(35)
    mm2f37 = make_m2risk_field(36)
    mm2f38 = make_m2risk_field(37)
    mm2f39 = make_m2risk_field(38)
    mm2f40 = make_m2risk_field(39)
    mm2f41 = make_m2risk_field(40)
    mm2f42 = make_m2risk_field(41)
    mm2f43 = make_m2risk_field(42)
    mm2f44 = make_m2risk_field(43)
    mm2f45 = make_m2risk_field(44)
    mm2f46 = make_m2risk_field(45)
    mm2f47 = make_m2risk_field(46)
    mm2f48 = make_m2risk_field(47)
    mm2f49 = make_m2risk_field(48)
    mm2f50 = make_m2risk_field(49)
    mm2f51 = make_m2risk_field(50)
    mm2f52 = make_m2risk_field(51)
    mm2f53 = make_m2risk_field(52)
    mm2f54 = make_m2risk_field(53)
    mm2f55 = make_m2risk_field(54)
    mm2f56 = make_m2risk_field(55)
    mm2f57 = make_m2risk_field(56)
    mm2f58 = make_m2risk_field(57)
    mm2f59 = make_m2risk_field(58)
    mm2f60 = make_m2risk_field(59)
    mm2f61 = make_m2risk_field(60)
    mm2f62 = make_m2risk_field(61)
    mm2f63 = make_m2risk_field(62)
    mm2f64 = make_m2risk_field(63)
    mm2f65 = make_m2risk_field(64)
    mm2f66 = make_m2risk_field(65)
    mm2f67 = make_m2risk_field(66)
    mm2f68 = make_m2risk_field(67)
    mm2f69 = make_m2risk_field(68)
    mm2f70 = make_m2risk_field(69)
    mm2f71 = make_m2risk_field(70)
    mm2f72 = make_m2risk_field(71)
    mm2f73 = make_m2risk_field(72)
    mm2f74 = make_m2risk_field(73)
    mm2f75 = make_m2risk_field(74)
    mm2f76 = make_m2risk_field(75)
    mm2f77 = make_m2risk_field(76)
    mm2f78 = make_m2risk_field(77)




















