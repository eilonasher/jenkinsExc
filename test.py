import pytest
from main import Calculator

def test_addition():
    c = Calculator()
    assert c.addition(1,2) == 3
    # assert c.addition(1, 2) == 'a'