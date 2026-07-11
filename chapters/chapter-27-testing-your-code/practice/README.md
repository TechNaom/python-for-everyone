# Chapter 27 Practice Bank: Testing Your Code

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Standard library
`unittest` and `unittest.mock` need no installs; Topic 3's pytest
problems return pytest-style source code as strings, so the file runs
standalone — install pytest (`pip install pytest`) only if you want to
actually run the generated test files yourself.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Why Testing Matters

1. Write `manual_check()`, testing "by hand" before a framework.
2. **Debug the Code:** fix `would_have_caught_bug()`'s bug detection.
3. **Debug the Code:** fix `silent_bug_report()` swallowing the real exception type.
4. **Scenario — Why We Test:** write `cost_of_bug_in_stage()`.
5. **Scenario — Interview Prep:** explain why manual testing doesn't scale.

## Topic 2: Writing Tests with unittest

1. Write `AddTestCase`, a `unittest.TestCase` using `assertEqual`.
2. Write `DivideTestCase`, using `assertEqual` and `assertRaises`.
3. **Debug the Code:** fix `run_is_even_suite()`'s wrong assert method and unsafe `unittest.main()` call.
4. **Scenario — Rescuing an Untested Function:** write `unittest_covers_parse_price()`.
5. **Scenario — Interview Prep:** explain `assertEqual` vs. `assertTrue` vs. `assertRaises` vs. `assertIn`.

## Topic 3: Writing Tests with pytest

1. Write `pytest_test_file_source()`, a plain-assert pytest test as a string.
2. Write `pytest_naming_is_valid()`, checking pytest's discovery rules.
3. **Debug the Code:** fix `count_pytest_style_asserts()` matching substrings instead of real assert statements.
4. **Scenario — Migrating unittest to pytest:** write `convert_assert_equal_to_pytest()`.
5. **Scenario — Interview Prep:** explain pytest vs. unittest trade-offs.

## Topic 4: Fixtures and setUp/tearDown

1. Write `CounterTestCase`, proving `setUp()` re-runs fresh per test.
2. Write `pytest_fixture_source()`, an `@pytest.fixture`-based test as a string.
3. **Debug the Code:** fix `SharedStateTestCase`'s class-attribute state leak between tests.
4. **Scenario — Fixing a Flaky CI Suite:** write `tests_are_independent()`.
5. **Scenario — Interview Prep:** explain what setUp/tearDown or fixtures are for.

## Topic 5: Mocking and Test Doubles

1. Write `mocked_price_lookup()`, patching a fake API response.
2. Write `place_order_without_real_calls()`, mocking two dependencies at once.
3. **Debug the Code:** fix `broken_mock_test()` patching the wrong target.
4. **Scenario — Fixing a Teammate's Wrong Mock:** write `identify_unused_mock()`.
5. **Scenario — Interview Prep:** explain what's worth mocking and what isn't.

## Topic 6: Test Coverage & What Good Tests Look Like

1. Write `aaa_pattern_labels()`, naming the Arrange-Act-Assert pattern.
2. Write `edge_cases_for_clamp()`, covering `clamp()`'s boundary inputs.
3. **Debug the Code:** fix `badly_named_test_report()`'s vague test names.
4. **Scenario — Code Review Judgment Call:** write `should_keep_test()`.
5. **Scenario — Interview Prep:** explain happy-path vs. edge-case tests.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks. For the
`pytest_test_file_source()`/`pytest_fixture_source()` tasks, you can
paste the returned string into a real `.py` file and run it with
`pytest` to double-check it actually passes.
