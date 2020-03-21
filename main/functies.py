""" this is where you are supposed to find all the definitions used to run this generator.
 I will try to use classes, namedtuples, default dicts and make it as phytonic as i am capable of at this time.
 Simple and working is what i strive for. I will comment as much as possible (also with variable names.
 """
import pandas as pd
import math

CORE_LARGE = 76
CORE_SMALL = 40
CORE_TINY = 25

MATERIAL = 145




class Roll():
    """"all things that are needed to build a roll, be it with numbers or with images"""

    # init method or constructor
    def __init__(self, order_number, begin_nummer, posities, vlg0, aantal_per_rol, hoogte):

        self.order_number = order_number
        self.begin_nummer = begin_nummer
        self.posities = posities
        self.aantal_per_rol = aantal_per_rol
        self.vlg0 = vlg0
        self.hoogte = hoogte



    def one(order_number):
            ''''initial test file'''
            return order_number




class Number(Roll):
    """"specifics for every number this includes vlg prefix postfix and should contain a step"""

    def __init__(self, prefix, postfix, stap):
        self.prefix = prefix
        self.postfix = postfix
        self.stap = stap

    def nummer_vlg(self):
        pass


class Checking_results():
    """"probably  belongs with pytest"""
    pass


class Concatenating_data():
    """"merging and concatenating the Dataframes and csv files"""
    pass


class Output():
    """"exporting files and summaries"""
    pass


class InloopUitloop:

    def __init__(self, amount_per_roll, height, core=76):
        material = 145

        self.amount_per_roll = amount_per_roll
        self.core = core
        self.height = height

    def wikkel(self, amount_per_rol=100, height=10):
        pi = math.pi
        # kern = 76  # global andere is 40 en 25
        # materiaal = 145  # global var_1
        var_1 = int(math.sqrt((4 / pi) * ((amount_per_rol * height) / 1000) * MATERIAL + pow(CORE_LARGE, 2)))
        wikkel = int(2 * pi * (var_1 / 2) / height + 2)
        return wikkel




a = InloopUitloop(1,1)
print(a.wikkel(100,100))