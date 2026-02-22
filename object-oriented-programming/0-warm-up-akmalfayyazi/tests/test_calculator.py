import math
import pytest

from calc.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_tambah(calc):
    assert calc.tambah(5, 3) == 8
    assert calc.tambah(-2, 10) == 8

def test_kurang(calc):
    assert calc.kurang(10, 3) == 7
    assert calc.kurang(5, 7) == -2

def test_kali(calc):
    assert calc.kali(4, 3) == 12
    assert calc.kali(-2, 5) == -10

def test_bagi_valid(calc):
    assert calc.bagi(10, 2) == 5
    assert calc.bagi(9, 3) == 3

def test_bagi_zero(calc):
    result = calc.bagi(10, 0)
    assert math.isnan(result)
