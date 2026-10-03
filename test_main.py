# To run the tests, from the snakeEyes folder:
#   python3 -m pytest -v

from main import calculate_balance


def test_snake_eyes_adds_35x_points():
    assert calculate_balance(100, 10, 1, 1) == 450


def test_other_roll_subtracts_points():
    assert calculate_balance(100, 10, 3, 4) == 90
