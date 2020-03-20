import pytest

from main.functies import Roll


def test_roll():
    expected = Roll.one("mike")
    assert expected == 'mike'

def test_wikkel():
    expected = Roll.voorloop_wikkel(3)
    assert expected == 3




