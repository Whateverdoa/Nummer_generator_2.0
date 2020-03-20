""" this is where you are supposed to find all the definitions used to run this generator.
 I will try to use classes, namedtuples, default dicts and make it as phytonic as i am capable of at this time.
 Simple and working is what i strive for. I will comment as much as possible (also with variable names.
 """
import pandas as pd





class Roll():
    """"all things that are needed to build a roll, be it with numbers or with images"""

    # init method or constructor
    def __init__(self, order_number, begin_nummer, posities, vlg0, aantal_per_rol, hoogte, wikkel):

        self.order_number = order_number
        self.begin_nummer = begin_nummer
        self.posities = posities
        self.aantal_per_rol = aantal_per_rol
        self.vlg0 = vlg0
        self.hoogte = hoogte
        self.wikkel = wikkel


    def one(order_number):
            ''''initial test file'''
            return order_number

    def voorloop_wikkel(wikkel):
        ''''wikkel formule --> int'''

        return wikkel


class Number(Roll):
    """"specifics for every number this includes vlg prefix postfix and should contain a step"""

    def __init__(self, prefix, postfix, stap):
        self.prefix = prefix
        self.postfix = postfix
        self.stap = stap

    def nummer_vlg(self):
        begin_nummer
        

class Checking_results():
    """"probably  belongs with pytest"""
    pass


class Concatenating_data():
    """"merging and concatenating the Dataframes and csv files"""
    pass


class Output():
    """"exporting files and summaries"""
    pass


