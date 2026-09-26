import unittest

from main import calculate_new_balance


class TestCalculateNewBalance(unittest.TestCase):
    def test_snake_eyes_adds_35x_points(self):
        self.assertEqual(calculate_new_balance(100, 10, 1, 1), 450)

    def test_other_roll_subtracts_points(self):
        self.assertEqual(calculate_new_balance(100, 10, 3, 4), 90)

    def test_single_one_is_a_loss(self):
        self.assertEqual(calculate_new_balance(100, 10, 1, 6), 90)


if __name__ == "__main__":
    unittest.main()
