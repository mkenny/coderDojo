# To run the tests, from the snakeEyes folder (not inside tests/):
#   python3 -m unittest -v

import unittest

from snake_eyes import calculate_balance


class TestCalculateBalance(unittest.TestCase):
    def test_snake_eyes_adds_35x_points(self):
        self.assertEqual(calculate_balance(100, 10, 1, 1), 450)

    def test_other_roll_subtracts_points(self):
        self.assertEqual(calculate_balance(100, 10, 3, 4), 90)


if __name__ == "__main__":
    unittest.main()
