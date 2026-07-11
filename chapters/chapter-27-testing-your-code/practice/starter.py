"""
Chapter 27 Practice Bank: Testing Your Code (unittest / pytest / mock)
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Uses the standard library's unittest and unittest.mock (no installs
needed for those), plus pytest for Topic 3 -- install with:
    pip install pytest
"""

import unittest
from unittest import mock
import subprocess
import sys
import os

# ============================================================
# Topic 1: Why Testing Matters
# ============================================================

# A small "production" function under test throughout this topic --
# deliberately has one bug (division truncates oddly for negatives).
def average(numbers):
    return sum(numbers) / len(numbers)


# TODO 1.1: Write manual_check(fn, args, expected). Call fn(*args) and
# return True if the result equals expected, else False. This is what
# "testing by hand" looks like before you learn a framework.


# TODO 1.2: Write would_have_caught_bug(fn, args, expected). Same idea
# as 1.1, but wrap the call in try/except -- if fn(*args) raises any
# Exception, return True (a test WOULD have caught this crash). If it
# returns a value, return True only if that value does NOT equal
# expected (a test would have caught a wrong answer). If it returns
# the correct value, return False (nothing to catch).


# TODO 1.3 (Debug the Code): silent_bug_report() below is supposed to
# report that average([]) raises ZeroDivisionError, but it wrongly
# reports "no error" because the try/except swallows the exception
# without checking what kind it is. Fix it so it returns the specific
# exception's type name (e.g. "ZeroDivisionError") instead of always
# returning "no error".
def silent_bug_report():
    try:
        average([])
        return "no error"
    except Exception:
        return "no error"


print(silent_bug_report())


# TODO 1.A (Scenario -- Why We Test): write
# cost_of_bug_in_stage(stage). A shipped-code truism: the later a bug
# is caught, the more it costs to fix. Given stage as one of "test",
# "code_review", or "production", return 1 for "test", 10 for
# "code_review", and 100 for "production" (relative cost multiplier).
# Return None for any other stage.


# TODO 1.B (Scenario -- Interview Prep): write
# explain_why_manual_testing_doesnt_scale() describing why re-running
# print statements by hand breaks down as a codebase grows.


# ============================================================
# Topic 2: Writing Tests with unittest
# ============================================================

# Production code under test for this topic.
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


# TODO 2.1: Write a unittest.TestCase subclass named AddTestCase with
# one test method, test_add_positive_numbers(self), that asserts
# add(2, 3) == 5 using self.assertEqual.


# TODO 2.2: Write a unittest.TestCase subclass named DivideTestCase
# with two test methods: test_divide_normal(self) asserting
# divide(10, 2) == 5, and test_divide_by_zero_raises(self) asserting
# divide(10, 0) raises ValueError (use self.assertRaises as a context
# manager).


# TODO 2.3 (Debug the Code): run_is_even_suite() below is supposed to
# run a small unittest suite checking is_even() and report how many
# tests passed, but it builds the TestCase wrong -- it calls
# self.assertEqual instead of self.assertTrue for a boolean check, and
# unittest.main() is not the right way to run tests from inside a
# function (it would try to parse sys.argv and could exit the whole
# script). Fix it to build a proper TestSuite and run it with
# unittest.TextTestRunner(verbosity=0), returning
# result.testsRun - len(result.failures) - len(result.errors) as the
# pass count.
def run_is_even_suite():
    class _IsEvenCase(unittest.TestCase):
        def test_four_is_even(self):
            self.assertEqual(is_even(4), None)

        def test_five_is_not_even(self):
            self.assertEqual(is_even(5), None)

    unittest.main()
    return 0


# TODO 2.A (Scenario -- Rescuing an Untested Function): a teammate
# wrote parse_price(text) below and shipped it with zero tests. Write
# unittest_covers_parse_price(). Build (in-function) a TestCase with
# at least 3 test methods covering: a normal price like "$19.99", a
# price with no dollar sign like "5", and a bad input like "" that
# should raise ValueError. Run it with unittest.TextTestRunner and
# return True if every test passed (0 failures and 0 errors).
def parse_price(text):
    cleaned = text.replace("$", "").strip()
    if cleaned == "":
        raise ValueError("empty price")
    return float(cleaned)


# TODO 2.B (Scenario -- Interview Prep): write
# explain_assert_methods() describing when you'd reach for
# assertEqual vs. assertTrue vs. assertRaises vs. assertIn, with one
# concrete example of each.


# ============================================================
# Topic 3: Writing Tests with pytest
# ============================================================

# TODO 3.1: Write a small pytest-style test FILE as a triple-quoted
# string and return it from pytest_test_file_source(). It must define
# a function named test_add_two_numbers() (pytest discovers any
# function starting with "test_", no class or import needed beyond
# whatever the test itself uses) that plain-asserts add(2, 3) == 5
# using a bare `assert` statement (not self.assertEqual -- pytest
# tests don't need a TestCase). Assume `from starter import add` is
# already available at the top of the string you return (include that
# import line in the string).


# TODO 3.2: Write pytest_naming_is_valid(name). pytest's default
# discovery only picks up test FILES named test_*.py or *_test.py,
# and test FUNCTIONS named test_*. Given a filename string, return
# True if it would be discovered, else False (case-sensitive, exact
# pytest default rules, no config overrides).


# TODO 3.3 (Debug the Code): count_pytest_style_asserts() below is
# supposed to count how many plain `assert` statements appear in a
# block of source code (a rough proxy for "how many checks does this
# pytest test file make"), but it counts occurrences of the substring
# "assert" anywhere, which also matches inside words like
# "self.assertEqual" or a variable named "assertion_count". Fix it to
# only count lines whose FIRST non-whitespace word is exactly
# "assert" (i.e. genuine bare assert statements, not "assertEqual"
# calls or unrelated identifiers containing "assert").
def count_pytest_style_asserts(source):
    return source.count("assert")


print(count_pytest_style_asserts("assert x == 1\nself.assertEqual(x, 1)\nassertion_count = 3"))


# TODO 3.A (Scenario -- Migrating unittest to pytest): a teammate
# wants to convert `self.assertEqual(result, expected)` lines to
# plain pytest asserts. Write
# convert_assert_equal_to_pytest(unittest_line). Given a string like
# "self.assertEqual(result, expected)", return the pytest-style
# string "assert result == expected". Assume the input always has
# exactly that two-argument self.assertEqual(...) shape (no extra
# whitespace tricks needed beyond a simple parse).


# TODO 3.B (Scenario -- Interview Prep): write
# explain_pytest_vs_unittest() describing the practical differences
# between the two (plain assert vs. assert* methods, no boilerplate
# class needed, fixtures vs. setUp/tearDown) and when a team might
# prefer one over the other.


# ============================================================
# Topic 4: Fixtures and setUp/tearDown
# ============================================================

# TODO 4.1: Write a unittest.TestCase subclass named CounterTestCase
# that uses setUp(self) to initialize self.counter = 0 before every
# test, and has two test methods -- test_increment(self), which
# increments self.counter and asserts it equals 1, and
# test_starts_at_zero(self), which asserts self.counter equals 0 --
# proving setUp() re-runs fresh for every test (if it didn't, the
# order tests happen to run in would make one of these fail).


# TODO 4.2: Write a pytest-style fixture as a triple-quoted string
# and return it from pytest_fixture_source(). It must define a
# function decorated with @pytest.fixture named empty_list() that
# returns a fresh empty list, and a test function
# test_append_to_empty_list(empty_list) that takes the fixture as a
# parameter, appends 1 to it, and plain-asserts the result equals
# [1]. Include the `import pytest` line in the string.


# TODO 4.3 (Debug the Code): SharedStateTestCase below has a classic
# test-interdependence bug -- self.items is a CLASS attribute (shared
# across every instance/test), not reset per test in setUp(), so
# tests that append to it leak state into each other depending on run
# order. Fix it by moving the list creation into setUp(self) so each
# test gets its own fresh self.items.
class SharedStateTestCase(unittest.TestCase):
    items = []

    def test_a_appends_one_item(self):
        self.items.append("a")
        self.assertEqual(len(self.items), 1)

    def test_b_starts_empty(self):
        self.assertEqual(len(self.items), 0)


# TODO 4.A (Scenario -- Fixing a Flaky CI Suite): your team's CI is
# flaky because two tests share a module-level dict that one test
# mutates and never cleans up, so the other test passes or fails
# depending on run order. Write
# tests_are_independent(results_in_order, results_reversed). Given
# two lists of pass/fail booleans -- the results when tests run in
# their normal order, and the results when the SAME tests run in
# reverse order -- return True if the two lists contain the exact
# same booleans in the same test-to-result mapping regardless of
# order (i.e. sorted(results_in_order) == sorted(results_reversed)),
# which is the property a properly-isolated suite must have.


# TODO 4.B (Scenario -- Interview Prep): write
# explain_setup_teardown_purpose() describing what setUp/tearDown (or
# a pytest fixture) are for, and why relying on one test's leftover
# state to make another test pass is a bug, not a shortcut.


# ============================================================
# Topic 5: Mocking and Test Doubles
# ============================================================

# Pretend external dependencies -- these would be slow/unreliable/
# costly in real life, which is exactly why we mock them in tests.
def get_current_price_from_api(ticker):  # pragma: no cover - stands in for a real network call
    raise RuntimeError("this would make a real network call in production")


def save_order_to_database(order):  # pragma: no cover - stands in for a real DB write
    raise RuntimeError("this would make a real database write in production")


def place_order(ticker, quantity):
    price = get_current_price_from_api(ticker)
    total = price * quantity
    save_order_to_database({"ticker": ticker, "quantity": quantity, "total": total})
    return total


# TODO 5.1: Write mocked_price_lookup(mock_price). Using
# unittest.mock.patch as a context manager to replace
# "__main__.get_current_price_from_api" (or the equivalent name in
# whatever module this runs as) with a Mock whose return_value is
# mock_price, call get_current_price_from_api("AAPL") through the
# patched name and return what it returns. This proves you can swap
# out a real dependency for a controlled fake within a test's scope.
# Hint: patch(f"{__name__}.get_current_price_from_api")


# TODO 5.2: Write place_order_without_real_calls(ticker, quantity,
# fake_price). Using two nested (or combined) mock.patch calls,
# replace both get_current_price_from_api to return fake_price AND
# save_order_to_database to return None (so no real network/DB calls
# ever happen), then call place_order(ticker, quantity) through the
# patches and return its result. This is the core mocking skill: test
# place_order()'s own logic (the multiplication) in complete isolation
# from its two real dependencies.


# TODO 5.3 (Debug the Code): broken_mock_test() below is supposed to
# prove save_order_to_database gets called exactly once when
# place_order() runs, but it patches the WRONG target -- it patches
# "get_current_price_from_api" twice instead of patching
# "save_order_to_database", so the assertion below is checking the
# wrong mock and would pass even if save_order_to_database were never
# called at all. Fix it to patch both real dependencies correctly
# (price lookup AND the database write) and assert on the DATABASE
# mock's call count.
def broken_mock_test():
    with mock.patch(f"{__name__}.get_current_price_from_api", return_value=100.0):
        with mock.patch(f"{__name__}.get_current_price_from_api", return_value=100.0) as fake_price_again:
            place_order("AAPL", 2)
            return fake_price_again.call_count == 1


print(broken_mock_test())


# TODO 5.A (Scenario -- Fixing a Teammate's Wrong Mock): a teammate's
# PR mocks datetime.now() to freeze time for a test, but the function
# under test actually calls time.time(), not datetime.now() -- so the
# mock silently does nothing and the real clock is still used. Write
# identify_unused_mock(function_under_test_uses, mock_target). Given
# what the function ACTUALLY calls (a string like "time.time") and
# what was mocked (a string like "datetime.now"), return True if the
# mock is USELESS (the two strings don't match, meaning the real
# dependency is still live), else False.


# TODO 5.B (Scenario -- Interview Prep): write
# explain_when_to_mock() describing what kinds of dependencies are
# good candidates for mocking (external APIs, databases, the system
# clock, random number generators, filesystems) and why you generally
# don't mock the exact function/class you're testing itself.


# ============================================================
# Topic 6: Test Coverage & What Good Tests Look Like
# ============================================================

def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


# TODO 6.1: Write aaa_pattern_labels(). Return the tuple
# ("Arrange", "Act", "Assert") -- the three-part structure most tests
# follow (set up data/mocks, call the thing under test, check the
# result).


# TODO 6.2: Write edge_cases_for_clamp(). Looking at clamp(value, low,
# high) above, return a list of (value, low, high, expected) tuples
# covering at least these 4 edge cases: value below low, value above
# high, value exactly equal to low, and value exactly equal to high.
# Each tuple's `expected` must be clamp()'s actual correct output for
# that input (you can call clamp() itself to compute it, or work it
# out by hand).


# TODO 6.3 (Debug the Code): badly_named_test_report() below is
# supposed to return a list of well-named unittest-style test method
# names for testing clamp(), but every name it returns is vague
# (test_1, test_2, test_3) instead of describing what's being tested
# and what's expected -- which is exactly the anti-pattern good test
# naming avoids. Fix it to return descriptive names following the
# pattern "test_<scenario>_<expected_outcome>", e.g.
# "test_value_below_low_returns_low".
def badly_named_test_report():
    return ["test_1", "test_2", "test_3"]


print(badly_named_test_report())


# TODO 6.A (Scenario -- Code Review Judgment Call): a teammate's PR
# adds a test that asserts a private helper function's internal
# variable naming matches an exact style, and another test that
# calls the SAME clamp(5, 0, 10) input three times expecting the same
# answer each time (redundant, learns nothing new). Write
# should_keep_test(tests_public_behavior, is_redundant_with_existing).
# Return True (keep it) only if tests_public_behavior is True AND
# is_redundant_with_existing is False -- i.e. don't test private
# implementation details, and don't duplicate coverage that already
# exists.


# TODO 6.B (Scenario -- Interview Prep): write
# explain_happy_path_vs_edge_cases() describing the difference
# between a "happy path" test and an edge-case test, using clamp() as
# the concrete example, and why shipping only happy-path tests gives
# false confidence.
