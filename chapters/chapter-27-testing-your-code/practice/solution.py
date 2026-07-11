"""
Chapter 27 Practice Bank: Testing Your Code (unittest / pytest / mock)
-- reference solution.
Run this from inside the practice/ folder: python3 solution.py

Uses the standard library's unittest and unittest.mock (no installs
needed for those). Topic 3's pytest problems return pytest-style
SOURCE CODE as strings rather than actually invoking pytest, so this
file runs standalone with no pytest install required -- if you want
to actually run the generated pytest file, `pip install pytest` and
save the returned string to a .py file.
"""

import unittest
from unittest import mock

# ============================================================
# Topic 1: Why Testing Matters
# ============================================================

def average(numbers):
    return sum(numbers) / len(numbers)


# TODO 1.1
def manual_check(fn, args, expected):
    return fn(*args) == expected


print(manual_check(average, ([1, 2, 3],), 2.0))


# TODO 1.2
def would_have_caught_bug(fn, args, expected):
    try:
        result = fn(*args)
    except Exception:
        return True
    return result != expected


print(would_have_caught_bug(average, ([],), 0))
print(would_have_caught_bug(average, ([2, 4],), 3.0))


# TODO 1.3 (Debug the Code)
# Bug: the except block always returned "no error" regardless of
# whether an exception actually happened -- fixed by returning the
# caught exception's type name.
def silent_bug_report():
    try:
        average([])
        return "no error"
    except Exception as e:
        return type(e).__name__


print(silent_bug_report())


# TODO 1.A (Scenario -- Why We Test)
def cost_of_bug_in_stage(stage):
    costs = {"test": 1, "code_review": 10, "production": 100}
    return costs.get(stage)


print(cost_of_bug_in_stage("test"))
print(cost_of_bug_in_stage("production"))
print(cost_of_bug_in_stage("unknown"))


# TODO 1.B (Scenario -- Interview Prep)
def explain_why_manual_testing_doesnt_scale():
    return (
        "Manually re-running print statements only checks whatever you "
        "remembered to try, at the moment you tried it -- it doesn't "
        "re-verify old behavior every time the code changes, so "
        "regressions creep in silently as the codebase grows. Automated "
        "tests are repeatable, fast, and run on every change, which is "
        "what actually catches a fix in one function breaking another."
    )


print(explain_why_manual_testing_doesnt_scale())


# ============================================================
# Topic 2: Writing Tests with unittest
# ============================================================

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


# TODO 2.1
class AddTestCase(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)


# TODO 2.2
class DivideTestCase(unittest.TestCase):
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


# TODO 2.3 (Debug the Code)
# Bugs: assertEqual used instead of assertTrue for a boolean check,
# and unittest.main() called from inside a function instead of
# building/running a proper TestSuite.
def run_is_even_suite():
    class _IsEvenCase(unittest.TestCase):
        def test_four_is_even(self):
            self.assertTrue(is_even(4))

        def test_five_is_not_even(self):
            self.assertTrue(not is_even(5))

    suite = unittest.TestLoader().loadTestsFromTestCase(_IsEvenCase)
    result = unittest.TextTestRunner(verbosity=0).run(suite)
    return result.testsRun - len(result.failures) - len(result.errors)


print("run_is_even_suite() passed:", run_is_even_suite())


# TODO 2.A (Scenario -- Rescuing an Untested Function)
def parse_price(text):
    cleaned = text.replace("$", "").strip()
    if cleaned == "":
        raise ValueError("empty price")
    return float(cleaned)


def unittest_covers_parse_price():
    class _ParsePriceCase(unittest.TestCase):
        def test_normal_price_with_dollar_sign(self):
            self.assertEqual(parse_price("$19.99"), 19.99)

        def test_price_without_dollar_sign(self):
            self.assertEqual(parse_price("5"), 5.0)

        def test_empty_string_raises_value_error(self):
            with self.assertRaises(ValueError):
                parse_price("")

    suite = unittest.TestLoader().loadTestsFromTestCase(_ParsePriceCase)
    result = unittest.TextTestRunner(verbosity=0).run(suite)
    return len(result.failures) == 0 and len(result.errors) == 0


print("unittest_covers_parse_price():", unittest_covers_parse_price())


# TODO 2.B (Scenario -- Interview Prep)
def explain_assert_methods():
    return (
        "assertEqual(a, b) checks two values match exactly -- e.g. "
        "assertEqual(add(2, 3), 5). assertTrue(x) checks a boolean "
        "condition -- e.g. assertTrue(is_even(4)). assertRaises(Error) "
        "used as a context manager checks that code inside the 'with' "
        "block raises that exception type -- e.g. "
        "'with self.assertRaises(ValueError): divide(1, 0)'. assertIn(a, "
        "b) checks membership -- e.g. assertIn('error', response_text) "
        "when you only care that a substring or item appears, not the "
        "whole value."
    )


print(explain_assert_methods())


# ============================================================
# Topic 3: Writing Tests with pytest
# ============================================================

# TODO 3.1
def pytest_test_file_source():
    return (
        "from starter import add\n"
        "\n"
        "def test_add_two_numbers():\n"
        "    assert add(2, 3) == 5\n"
    )


print(pytest_test_file_source())


# TODO 3.2
def pytest_naming_is_valid(name):
    if not name.endswith(".py"):
        return False
    stem = name[:-3]
    return stem.startswith("test_") or stem.endswith("_test")


print(pytest_naming_is_valid("test_add.py"))
print(pytest_naming_is_valid("add_test.py"))
print(pytest_naming_is_valid("add.py"))
print(pytest_naming_is_valid("Test_add.py"))


# TODO 3.3 (Debug the Code)
# Bug: counted every occurrence of the substring "assert" anywhere,
# including inside "self.assertEqual" and "assertion_count" -- fixed
# to only count lines that are genuine bare `assert` statements.
def count_pytest_style_asserts(source):
    count = 0
    for line in source.splitlines():
        words = line.strip().split()
        if words and words[0] == "assert":
            count += 1
    return count


print(count_pytest_style_asserts("assert x == 1\nself.assertEqual(x, 1)\nassertion_count = 3"))


# TODO 3.A (Scenario -- Migrating unittest to pytest)
def convert_assert_equal_to_pytest(unittest_line):
    inner = unittest_line.strip()
    prefix = "self.assertEqual("
    inner = inner[len(prefix):-1]  # strip "self.assertEqual(" and trailing ")"
    left, right = inner.split(",", 1)
    return f"assert {left.strip()} == {right.strip()}"


print(convert_assert_equal_to_pytest("self.assertEqual(result, expected)"))


# TODO 3.B (Scenario -- Interview Prep)
def explain_pytest_vs_unittest():
    return (
        "unittest requires subclassing TestCase and using assert* "
        "methods (assertEqual, assertTrue); pytest lets you write plain "
        "functions with bare `assert` statements and still gives "
        "readable failure diffs by inspecting the assert expression "
        "itself. pytest also uses simple @pytest.fixture functions "
        "instead of setUp/tearDown methods, and its test discovery is "
        "more flexible (any test_*.py file, any test_* function, no "
        "class required). Teams already invested in unittest (or "
        "needing its OOP-style structure) often keep it; teams starting "
        "fresh usually prefer pytest for the shorter, more readable "
        "tests -- and pytest can run unittest-style TestCases too, so "
        "the two aren't mutually exclusive."
    )


print(explain_pytest_vs_unittest())


# ============================================================
# Topic 4: Fixtures and setUp/tearDown
# ============================================================

# TODO 4.1
class CounterTestCase(unittest.TestCase):
    def setUp(self):
        self.counter = 0

    def test_increment(self):
        self.counter += 1
        self.assertEqual(self.counter, 1)

    def test_starts_at_zero(self):
        self.assertEqual(self.counter, 0)


# TODO 4.2
def pytest_fixture_source():
    return (
        "import pytest\n"
        "\n"
        "@pytest.fixture\n"
        "def empty_list():\n"
        "    return []\n"
        "\n"
        "def test_append_to_empty_list(empty_list):\n"
        "    empty_list.append(1)\n"
        "    assert empty_list == [1]\n"
    )


print(pytest_fixture_source())


# TODO 4.3 (Debug the Code)
# Bug: items was a class attribute shared across every test instance
# -- fixed by moving it into setUp() so each test gets a fresh list.
class SharedStateTestCase(unittest.TestCase):
    def setUp(self):
        self.items = []

    def test_a_appends_one_item(self):
        self.items.append("a")
        self.assertEqual(len(self.items), 1)

    def test_b_starts_empty(self):
        self.assertEqual(len(self.items), 0)


# TODO 4.A (Scenario -- Fixing a Flaky CI Suite)
def tests_are_independent(results_in_order, results_reversed):
    return sorted(results_in_order) == sorted(results_reversed)


print(tests_are_independent([True, True, False], [False, True, True]))
print(tests_are_independent([True, True, False], [True, False, False]))


# TODO 4.B (Scenario -- Interview Prep)
def explain_setup_teardown_purpose():
    return (
        "setUp/tearDown (or a pytest fixture) exist to give every test "
        "a known, freshly-built starting state and to clean up afterward "
        "(closing files, resetting a fake database, clearing a shared "
        "cache) -- so each test is isolated and its result doesn't "
        "depend on which other tests ran before it or in what order. A "
        "test that only passes because an earlier test happened to "
        "leave behind the right leftover state isn't a working test, "
        "it's a hidden ordering dependency that will eventually break "
        "when the suite is reordered, parallelized, or run alone."
    )


print(explain_setup_teardown_purpose())


# ============================================================
# Topic 5: Mocking and Test Doubles
# ============================================================

def get_current_price_from_api(ticker):  # pragma: no cover - stands in for a real network call
    raise RuntimeError("this would make a real network call in production")


def save_order_to_database(order):  # pragma: no cover - stands in for a real DB write
    raise RuntimeError("this would make a real database write in production")


def place_order(ticker, quantity):
    price = get_current_price_from_api(ticker)
    total = price * quantity
    save_order_to_database({"ticker": ticker, "quantity": quantity, "total": total})
    return total


# TODO 5.1
def mocked_price_lookup(mock_price):
    with mock.patch(f"{__name__}.get_current_price_from_api", return_value=mock_price):
        return get_current_price_from_api("AAPL")


print(mocked_price_lookup(150.0))


# TODO 5.2
def place_order_without_real_calls(ticker, quantity, fake_price):
    with mock.patch(f"{__name__}.get_current_price_from_api", return_value=fake_price):
        with mock.patch(f"{__name__}.save_order_to_database", return_value=None):
            return place_order(ticker, quantity)


print(place_order_without_real_calls("AAPL", 3, 100.0))


# TODO 5.3 (Debug the Code)
# Bug: patched get_current_price_from_api twice (once shadowing the
# other) and never patched save_order_to_database at all -- fixed to
# patch both real dependencies and assert on the database mock.
def broken_mock_test():
    with mock.patch(f"{__name__}.get_current_price_from_api", return_value=100.0):
        with mock.patch(f"{__name__}.save_order_to_database", return_value=None) as fake_db:
            place_order("AAPL", 2)
            return fake_db.call_count == 1


print(broken_mock_test())


# TODO 5.A (Scenario -- Fixing a Teammate's Wrong Mock)
def identify_unused_mock(function_under_test_uses, mock_target):
    return function_under_test_uses != mock_target


print(identify_unused_mock("time.time", "datetime.now"))
print(identify_unused_mock("time.time", "time.time"))


# TODO 5.B (Scenario -- Interview Prep)
def explain_when_to_mock():
    return (
        "Good candidates for mocking are dependencies that are slow, "
        "unreliable, costly, or non-deterministic if called for real in "
        "a test: external APIs, databases, the system clock, random "
        "number generators, and the filesystem/network. You generally "
        "don't mock the exact function or class you're testing -- "
        "mocking the thing under test would just make the test check "
        "that the mock returns what you told it to, proving nothing "
        "about whether the real code works."
    )


print(explain_when_to_mock())


# ============================================================
# Topic 6: Test Coverage & What Good Tests Look Like
# ============================================================

def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


# TODO 6.1
def aaa_pattern_labels():
    return ("Arrange", "Act", "Assert")


print(aaa_pattern_labels())


# TODO 6.2
def edge_cases_for_clamp():
    cases = [
        (-5, 0, 10),
        (15, 0, 10),
        (0, 0, 10),
        (10, 0, 10),
    ]
    return [(value, low, high, clamp(value, low, high)) for value, low, high in cases]


print(edge_cases_for_clamp())


# TODO 6.3 (Debug the Code)
# Bug: every returned name was vague (test_1, test_2, test_3) instead
# of describing the scenario and expected outcome.
def badly_named_test_report():
    return [
        "test_value_below_low_returns_low",
        "test_value_above_high_returns_high",
        "test_value_equal_to_low_returns_low",
    ]


print(badly_named_test_report())


# TODO 6.A (Scenario -- Code Review Judgment Call)
def should_keep_test(tests_public_behavior, is_redundant_with_existing):
    return tests_public_behavior and not is_redundant_with_existing


print(should_keep_test(True, False))
print(should_keep_test(False, False))
print(should_keep_test(True, True))


# TODO 6.B (Scenario -- Interview Prep)
def explain_happy_path_vs_edge_cases():
    return (
        "A happy-path test checks the normal, expected case -- e.g. "
        "clamp(5, 0, 10) == 5, a value already inside the range. An "
        "edge-case test checks the boundaries and unusual inputs -- "
        "clamp(-5, 0, 10) == 0, clamp(15, 0, 10) == 10, and the exact "
        "boundary values clamp(0, 0, 10) and clamp(10, 0, 10). Shipping "
        "only happy-path tests gives false confidence because most real "
        "bugs live at the edges -- off-by-one errors, boundary "
        "conditions, empty inputs -- exactly the inputs a happy-path-only "
        "suite never exercises."
    )


print(explain_happy_path_vs_edge_cases())
