import pytest

from Calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add_one_plus_one_gives_two(calc):
    # Arrange
    num1 = 1
    num2 = 1
    expected_answer = 2
    # Act
    result = calc.add(num1, num2)
    # Assert
    assert expected_answer == result

def test_add_one_plus_two_gives_three(calc):
    # Arrange
    num1 = 1
    num2 = 2
    expected_answer = 3
    # Act
    result = calc.add(num1, num2)
    # Assert
    assert expected_answer == result

def test_sub_two_minus_one_gives_one(calc):
    # Arrange
    num1 = 2
    num2 = 1
    expected_answer = 1
    # Act
    result = calc.sub(num1, num2)
    # Assert
    assert expected_answer == result

def test_sub_four_minus_one_gives_three(calc):
    # Arrange
    num1 = 4
    num2 = 1
    expected_answer = 3
    # Act
    result = calc.sub(num1, num2)
    # Assert
    assert expected_answer == result