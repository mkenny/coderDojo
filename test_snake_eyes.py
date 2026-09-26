# To run the tests, from the snakeEyes folder:
#   python3 -m unittest -v

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from snake_eyes import auto_roll, calculate_balance


class TestCalculateBalance(unittest.TestCase):
    def test_snake_eyes_adds_35x_points(self):
        self.assertEqual(calculate_balance(100, 10, 1, 1), 450)

    def test_other_roll_subtracts_points(self):
        self.assertEqual(calculate_balance(100, 10, 3, 4), 90)


class TestAutoRoll(unittest.TestCase):
    # patch("builtins.input") answers "10" when asked for the number of rolls.
    # patch("snake_eyes.random.randint") makes every die land on the number we choose.

    def test_every_roll_is_snake_eyes(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="10"), patch("snake_eyes.random.randint", return_value=1):
            with redirect_stdout(output):
                auto_roll()
        self.assertIn("Snake eyes came up 10 times: 100.00%", output.getvalue())

    def test_no_rolls_are_snake_eyes(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="10"), patch("snake_eyes.random.randint", return_value=4):
            with redirect_stdout(output):
                auto_roll()
        self.assertIn("Snake eyes came up 0 times: 0.00%", output.getvalue())


if __name__ == "__main__":
    unittest.main()
