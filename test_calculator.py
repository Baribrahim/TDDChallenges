import pytest

from Calculator import Calculator

def test_add_one_plus_one_gives_two():
    calc = Calculator()
    num1 = 1
    num2 = 1
    expected_answer = 2
    result = calc.add(num1, num2)
    assert expected_answer == result

def test_add_one_plus_two_gives_three():
    calc = Calculator()
    num1 = 1
    num2 = 2
    expected_answer = 3
    result = calc.add(num1, num2)
    assert expected_answer == result