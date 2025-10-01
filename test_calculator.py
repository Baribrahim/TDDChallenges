import pytest

from Calculator import Calculator

def test_add_one_plus_one_gives_two():
    # Arrange
    calc = Calculator()
    num1 = 1
    num2 = 1
    expected_answer = 2
    # Act
    result = calc.add(num1, num2)
    # Assert
    assert expected_answer == result

def test_add_one_plus_two_gives_three():
    # Arrange
    calc = Calculator()
    num1 = 1
    num2 = 2
    expected_answer = 3
    # Act
    result = calc.add(num1, num2)
    # Assert
    assert expected_answer == result

def test_sub_two_minus_one_gives_one():
    # Arrange
    calc = Calculator()
    num1 = 2
    num2 = 1
    expected_answer = 1
    # Act
    result = calc.sub(num1, num2)
    # Assert
    assert expected_answer == result