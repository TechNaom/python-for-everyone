"""
Chapter 27 Exercises: Testing Your Code -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

import unittest
from unittest.mock import Mock


# TODO 1
def add(a, b):
    return a + b


print("add(2, 3):", add(2, 3))


# TODO 2
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


print("divide(10, 2):", divide(10, 2))


# TODO 3
class TestMathOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


# TODO 4
class TestCartFixture(unittest.TestCase):
    def setUp(self):
        self.cart = []

    def test_cart_starts_empty(self):
        self.assertEqual(self.cart, [])


# TODO 5
def get_username(user_id, db_client):
    user = db_client.fetch_user(user_id)
    return user["username"]


# TODO 6
class TestGetUsername(unittest.TestCase):
    def test_get_username_uses_mocked_db(self):
        mock_db = Mock()
        mock_db.fetch_user.return_value = {"username": "grace"}

        result = get_username(1, mock_db)

        self.assertEqual(result, "grace")
        mock_db.fetch_user.assert_called_once_with(1)


# TODO 7
def apply_late_fee(balance, days_late):
    if days_late <= 0:
        return balance
    return balance + (days_late * 5)


print("apply_late_fee(100, 3):", apply_late_fee(100, 3))


# TODO 8
class TestLateFee(unittest.TestCase):
    def test_no_days_late_leaves_balance_unchanged(self):
        # Arrange
        balance, days_late = 100, 0
        # Act
        result = apply_late_fee(balance, days_late)
        # Assert
        self.assertEqual(result, 100)

    def test_some_days_late_adds_correct_fee(self):
        # Arrange
        balance, days_late = 100, 3
        # Act
        result = apply_late_fee(balance, days_late)
        # Assert
        self.assertEqual(result, 115)

    def test_negative_days_late_treated_as_not_late(self):
        # Arrange
        balance, days_late = 100, -5
        # Act
        result = apply_late_fee(balance, days_late)
        # Assert
        self.assertEqual(result, 100)


# TODO 9 (Debug the Code)
# Bug: _shared_cart=[] is the classic mutable default argument gotcha --
# it's built once, at def time, and reused across every call, so
# cart_a.append("apple") also shows up in cart_b. Fixed with the
# None-sentinel pattern.
def make_empty_cart(_shared_cart=None):
    if _shared_cart is None:
        _shared_cart = []
    return _shared_cart


class TestMakeEmptyCart(unittest.TestCase):
    def test_two_calls_are_independent(self):
        cart_a = make_empty_cart()
        cart_a.append("apple")

        cart_b = make_empty_cart()

        self.assertEqual(cart_b, [])


if __name__ == "__main__":
    print()
    print("Running the test suite:")
    unittest.main(verbosity=2, exit=False)
