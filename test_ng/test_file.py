import pytest
from pathlib import Path
from main.functies import Roll, InloopUitloop
from main.wikkel import wrap
from main.paden import DirMaker, wdir


CORE_LARGE = 76
CORE_SMALL = 40
CORE_TINY = 25

MATERIAL = 145


def test_roll():
    expected = Roll.one("mike")
    assert expected == 'mike'



def test_wrap_1():
    expected = 6
    w = wrap(500,80)

    assert w == expected

def test_wrap():
    expected = 4
    w = InloopUitloop(1,1)
    vvw = w.wikkel(100,100)
    assert vvw == expected

# checking paden

def test_filename_maker():
    expected = "mike.csv"
    file = DirMaker("pad","fn","dirn",10)
    name = file.file_name_maker("mike1969",".csv", 2)

    assert name == ["mike1969_00001.csv","mike1969_00002.csv"]

def test_paden_maker():
    expected = Path(r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\Nummer_generator_2.0\test_ng\padnaam")
    panaamtester = DirMaker("pad","fn","dirn",10)
    temakenpad = panaamtester.paden_maker("padnaam")
    # ga testen of het directories maakt op de juiste plek
    assert temakenpad == expected
