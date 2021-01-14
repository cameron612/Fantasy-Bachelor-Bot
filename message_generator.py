import os
import random
import requests
from lxml import html
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

bachelor_quotes = [
    '"If it\'s a pomegranate then God bless it." — Ashley S.',
    '"I just think Hannah G. has coasted on her beauty for so much of her life." — Caelynn',
    '"Robby has 12 abs, you should only have 6. What do you do for a living? Stop working out. I don’t trust you." — Raven',
    '"Like, I\'m done. Done. That was glitter. Glitter." — Krystal',
    '"I am worth the world. I am amazing." — Demi',
    '"Deep, intellectual things are just my jam." — Olivia',
    '"What drama is happening that I can just sit and watch?" — Carly',
    '"I thought I knew what kind of man you were. What you just made me go through, I would never want my children having a father like you." — Clare',
    '"How do we move forward? And \'we\' meaning you two." — Chris Harrison',
    '"Is it awkward if I ask you for a better kiss?" — Lace',
    '"I don\'t want to have to physically fight you, but if there\'s no way to stop you from saying what you\'re saying, then I will physically have to hurt you." — Chad',
    '"Michael Jordan took naps. Abe Lincoln took naps. Why am I getting in trouble for napping?" — Corinne',
    '"Evan does give me erectile dysfunction." — Carly',
    '"I really am a golden retriever. And Jenna’s a frisbee." — Jordan',
    '"Let\'s do the damn thing!" — Becca'
]

class MessageGenerator:

    def get_league_standings(self):
        return "http://www.fantasy4reality.com/leagues/4247"

    def get_random_quote(self):
        return random.choice(bachelor_quotes)

    def get_source(self):
        return "https://github.com/cameron612/Fantasy-Bachelor-Bot"

    def get_congrats_message(self):
        return 'Congrats! 🎈🎉'

    def get_barb_message(self):
        return 'You called?'