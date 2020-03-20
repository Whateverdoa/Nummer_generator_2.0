"this is the calculation for a wikkel around a rol"

import math

CORE_LARGE = 76
CORE_SMALL = 40
CORE_TINY = 25

MATERIAL = 145


def wrap(Aantalperrol, formaat_hoogte):
    """ importing in a fuction?"""

    pi = math.pi
    # kern = 76  # global andere is 40 en 25
    # materiaal = 145  # global var_1
    var_1 = int(math.sqrt((4 / pi) * ((Aantalperrol * formaat_hoogte) / 1000) * MATERIAL + pow(CORE_LARGE, 2)))
    wikkel = int(2 * pi * (var_1 / 2) / formaat_hoogte + 2)
    return wikkel


class WrapAround:

    def __init__(self, amount_per_roll, height, core=76):
        material = 145

        self.amount_per_roll = amount_per_roll
        self.core = core
        self.height = height


class NoWrapAround(WrapAround):

    def _geen_wikkel(self):
        self._geen_wikkel = True


noop = NoWrapAround(100, 25, 100)

yep = WrapAround(100, 76, 40)

print(f'apr = {yep.amount_per_roll}')

#     self._core = [76, 40, 25, ]
#
# def material(self):
#     self._material = [145, ]
#
#
# def core(self):
#     pass
#
# def width(self):
#     pass
#
# def height(self):
#     pass
#
# def around(self):
#     """boolean"""
#     pass
