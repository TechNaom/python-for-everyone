"""
Chapter 27 Exercises: Testing Your Code
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every task here uses only the standard library (unittest, unittest.mock) --
no installs needed. This file demonstrates the functions/tests by running
them as a plain script; see the README for how to also run this chapter's
work with the actual `pytest` command if you have it installed.
"""

import unittest
from unittest.mock import Mock


# TODO 1: Write add(a, b). Return a + b.


# TODO 2: Write divide(a, b). Return a / b, but raise ValueError with the
# message "Cannot divide by zero" if b == 0.


# TODO 3: Write a unittest.TestCase class named TestMathOps with two test
# methods: test_add (asserts add(2, 3) == 5) and test_divide_by_zero_raises
# (asserts divide(10, 0) raises ValueError, using self.assertRaises as a
# with block).


# TODO 4: Write a unittest.TestCase class named TestCartFixture with a
# setUp(self) method that sets self.cart = [], and one test method
# test_cart_starts_empty that asserts self.cart == [].


# TODO 5: Write get_username(user_id, db_client). It should call
# db_client.fetch_user(user_id) and return the "username" key from the
# dict that comes back. (This models code that depends on an external
# database client -- the kind of dependency you mock rather than call
# for real in a test.)


# TODO 6: Write a unittest.TestCase class named TestGetUsername with one
# test method test_get_username_uses_mocked_db. Inside it: build a
# unittest.mock.Mock(), set mock.fetch_user.return_value to
# {"username": "grace"}, call get_username(1, mock), assert the result
# is "grace", and assert mock.fetch_user was called exactly once with
# argument 1 (mock.fetch_user.assert_called_once_with(1)).


# TODO 7: Write apply_late_fee(balance, days_late). If days_late <= 0,
# return balance unchanged. Otherwise return balance + (days_late * 5).


# TODO 8: Write a unittest.TestCase class named TestLateFee with THREE
# test methods following the AAA pattern (Arrange/Act/Assert), each
# testing a different case of apply_late_fee: no days late (fee
# unchanged), some days late (fee added correctly), and exactly 0 days
# late (treated the same as no days late). Name each test method after
# the exact case it checks.


# TODO 9 (Debug the Code): this test is supposed to prove that two
# separate calls to make_empty_cart() never share state, but it has a
# bug -- read it carefully. Find and fix the bug (either in
# make_empty_cart() or in the test, whichever is actually wrong).
def make_empty_cart(_shared_cart=[]):
    return _shared_cart


class TestMakeEmptyCart(unittest.TestCase):
    def test_two_calls_are_independent(self):
        cart_a = make_empty_cart()
        cart_a.append("apple")

        cart_b = make_empty_cart()

        self.assertEqual(cart_b, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
