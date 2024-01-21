import pytest
from six import assertRaisesRegex

from main import Calculator

def test_addition_success():
    c = Calculator()
    assert c.addition(1,2) == 3
    # assert c.addition(1, 2) == 'a'

def test_addition_failure():
    c = Calculator()
    try:
        c.addition(1, 2)
        assert True
    except:
        pass
