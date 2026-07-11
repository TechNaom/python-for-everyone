# Chapter 27 Exercises: Testing Your Code

These exercises use what Chapter 27 covered: writing tests with
`unittest`, fixtures/`setUp`, mocking external dependencies with
`unittest.mock`, and the Arrange-Act-Assert pattern. Every task here
uses only the standard library -- no installs needed.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

The file both defines the functions/tests from each TODO and runs the
test suite at the bottom via `unittest.main()`, so running it directly
shows you pass/fail output immediately -- no separate test command
needed for the built-in `unittest` parts of this exercise.

**Optional: running with pytest.** If you have pytest installed
(`pip install pytest`), you can also run the exact same test classes
with `pytest starter.py -v` from inside this folder -- pytest can run
`unittest.TestCase` classes directly, no changes needed. This is a good
way to compare pytest's output style against unittest's, since both are
testing identical code.

## Task 1 — A function to test

Find `# TODO 1`. Write `add(a, b)` — return `a + b`.

## Task 2 — A function that raises

Find `# TODO 2`. Write `divide(a, b)` — return `a / b`, but raise
`ValueError("Cannot divide by zero")` if `b == 0`.

## Task 3 — Your first TestCase

Find `# TODO 3`. Write a `unittest.TestCase` class `TestMathOps` with
two test methods: `test_add` (checks `add(2, 3) == 5`) and
`test_divide_by_zero_raises` (checks that `divide(10, 0)` raises
`ValueError`, using `self.assertRaises` as a `with` block).

## Task 4 — A fixture with setUp

Find `# TODO 4`. Write a `unittest.TestCase` class `TestCartFixture`
with a `setUp(self)` method that builds `self.cart = []`, and one test
method `test_cart_starts_empty` that checks `self.cart == []`.

## Task 5 — Code with an external dependency

Find `# TODO 5`. Write `get_username(user_id, db_client)` — call
`db_client.fetch_user(user_id)` and return the `"username"` key from
the dict it returns. This models a function that depends on a database
client, the kind of dependency you mock in a test instead of hitting a
real database.

## Task 6 — Mocking that dependency

Find `# TODO 6`. Write a `unittest.TestCase` class `TestGetUsername`
with one test method `test_get_username_uses_mocked_db`. Build a
`unittest.mock.Mock()`, set `mock.fetch_user.return_value` to
`{"username": "grace"}`, call `get_username(1, mock)`, assert the
result is `"grace"`, and assert `mock.fetch_user` was called exactly
once with `1` (`mock.fetch_user.assert_called_once_with(1)`).

## Task 7 — A function with edge cases

Find `# TODO 7`. Write `apply_late_fee(balance, days_late)` — if
`days_late <= 0`, return `balance` unchanged; otherwise return
`balance + (days_late * 5)`.

## Task 8 — Testing those edge cases with AAA

Find `# TODO 8`. Write a `unittest.TestCase` class `TestLateFee` with
**three** test methods, each following Arrange/Act/Assert and testing a
different case: no days late, some days late, and a negative
`days_late` (treated the same as no days late). Name each test method
after the exact case it checks.

## Task 9 — Debug the Code

Find `# TODO 9`. This test is supposed to prove that two separate calls
to `make_empty_cart()` never share state, but it fails as written.
Find the bug and fix it — the bug could be in `make_empty_cart()`
itself or in the test; read carefully before deciding which.

## Checking your work

Compare your output against `solution.py`. Every test in the solution
passes (`OK`, exit code 0). If a test you wrote fails, read the
assertion's diff carefully — it tells you exactly what was expected
versus what actually happened.
