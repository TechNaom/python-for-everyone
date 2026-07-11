# Chapter 27 Project: Test Suite for an Earlier Project

A comprehensive **pytest test suite** for a small, self-contained
`TaskManager` module (add/complete/overdue-check workflow), written
against real code rather than toy examples — demonstrating pytest,
fixtures, and mocking together the way you'd actually use them on a
real project.

## What you'll build

The `TaskManager` module (`Task`, `TaskManager`, `NotificationSender`)
is already provided and finished — it's the "earlier project" being
tested, standing in for a small class you might have built back in
Chapter 11's OOP chapter. Your job is the test suite itself:

1. **Happy-path tests** for `add_task()`, `complete_task()`, and
   `get_overdue_tasks()` — the normal, expected-input case for each.
2. **Edge-case tests** — an empty title, a whitespace-only title,
   completing a task that doesn't exist, two tasks sharing a title, a
   completed task that's technically past its due date, an empty
   manager.
3. **A mocked external dependency** — `notify_overdue()` calls out to
   a `NotificationSender`, which stands in for a real
   email/SMS/push-notification service. Your tests inject a
   `unittest.mock.MagicMock()` in its place so no real notification is
   ever sent, then assert on *how* it was called (`call_count`,
   `assert_any_call()`) — plus one test that proves the mock is
   actually intercepting the real class via `unittest.mock.patch.object()`.
4. **Fixtures with no shared state** — `manager` and `fixed_now` each
   return fresh values per test, so no test can leak state into
   another (test isolation, sub-topic 4).

## Example run

```text
$ python3 -m pytest solution.py -v
============================= test session starts ==============================
collected 13 items

solution.py::test_add_task_returns_task_with_given_title PASSED          [  7%]
solution.py::test_add_task_appends_to_manager_tasks_list PASSED          [ 15%]
solution.py::test_add_task_rejects_empty_title PASSED                    [ 23%]
solution.py::test_add_task_rejects_whitespace_only_title PASSED          [ 30%]
solution.py::test_complete_task_marks_matching_task_done PASSED          [ 38%]
solution.py::test_complete_task_returns_false_when_no_match PASSED       [ 46%]
solution.py::test_complete_task_only_affects_first_pending_match PASSED  [ 53%]
solution.py::test_get_overdue_tasks_returns_only_past_due_incomplete_tasks PASSED [ 61%]
solution.py::test_get_overdue_tasks_excludes_completed_tasks_even_if_past_due PASSED [ 69%]
solution.py::test_get_overdue_tasks_empty_when_no_tasks_added PASSED     [ 76%]
solution.py::test_notify_overdue_calls_notifier_send_once_per_overdue_task PASSED [ 84%]
solution.py::test_notify_overdue_does_not_count_failed_sends PASSED      [ 92%]
solution.py::test_notify_overdue_never_touches_the_real_notification_sender PASSED [100%]

============================== 13 passed in 0.05s ==============================
```

## How to run

```bash
cd chapters/chapter-27-testing-your-code/project
pip install pytest    # if you don't already have it
python3 -m pytest starter.py -v
```

Fill in the 13 numbered `# TODO` test functions. Want to see a
finished version? Run `python3 -m pytest solution.py -v`.

## The pieces

- **`Task` / `TaskManager` / `NotificationSender`** — the finished
  "earlier project" under test. `TaskManager` takes its notifier as a
  constructor argument (dependency injection), which is exactly what
  makes `notify_overdue()` mockable without touching real code.
- **`manager` fixture** — a fresh, empty `TaskManager` for every test.
- **`fixed_now` fixture** — a fixed `datetime` so overdue checks are
  deterministic instead of depending on when the test happens to run.
- **13 test functions** — each following the AAA pattern (Arrange,
  Act, Assert), covering happy paths, edge cases, and one mocked
  external dependency.

## Ideas to make it your own

- Point this same pattern at one of your own earlier chapter projects
  (the Chapter 13 CSV reader, the Chapter 21 database layer) instead
  of the built-in `TaskManager` example.
- Add a `@pytest.mark.parametrize` test that checks several
  empty/whitespace/`None` titles all raise `ValueError` in one test
  function instead of writing one test per case.
- Add a test for what happens when `NotificationSender.send()` raises
  an exception instead of returning `False` — should `notify_overdue()`
  propagate it, or catch and skip?

## Why this project matters

A test suite is the thing that lets you change code later without
re-checking everything by hand — and mocking is what makes that
practical the moment your code talks to anything external (an API, a
database, the clock, a notification service). Writing tests against
*real* code, not a toy example, is what makes the difference between
"I know the syntax" and "I can actually protect a real project."

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Test Suite above is fully built out with a starter and reference
solution — the four ideas below are not. Each is a real, grounded use
case solvable with only what's been taught through Chapter 27. No
starter or solution files are provided on purpose — building one of
these unassisted is the point.

### 1. A Test Suite for a REST API Client

**Problem:** A small API client class (methods like `get_user(id)`,
`create_order(data)`) makes real HTTP requests — but a test suite
should never make a real network call.

**What it should do:** Write pytest tests that mock the HTTP layer
(e.g. patch a `requests.get`/`requests.post` call, or an injected
`http_client` dependency) and assert the client parses a mocked JSON
response correctly, handles a mocked error status code, and passes the
right URL/parameters to the mocked call.

**Suggested approach:** Build a tiny API client class first (Chapter
20's `requests`/JSON knowledge), inject its HTTP dependency the same
way `TaskManager` injects its `notifier`, then `unittest.mock.patch`
it in tests — never let a test actually reach the network.

### 2. A Test Suite for a CSV Data-Cleaning Pipeline

**Problem:** A CSV-cleaning function (strip whitespace, drop blank
rows, convert types, flag malformed rows) needs confidence it handles
messy real-world data correctly.

**What it should do:** Write pytest tests using small in-memory CSV
strings (via `io.StringIO`, no real files needed) covering a clean
row, a row with extra whitespace, a blank row, a row with a bad
numeric field, and an entirely empty file.

**Suggested approach:** Reuse Chapter 13's CSV-reading logic as the
function under test; a `tmp_path` pytest fixture or `io.StringIO` both
work for feeding in fake CSV content without touching the real
filesystem.

### 3. Tests That Mock the Clock for a Subscription-Expiry Checker

**Problem:** A `is_subscription_expired(subscription, now=None)`-style
function needs to be tested at multiple points in time — signup day,
the day before expiry, the exact expiry moment, well after expiry —
without the test's outcome depending on today's real date.

**What it should do:** Write pytest tests that pass a fixed `datetime`
into the function for each of those points in time (the same `now`
parameter pattern `Task.is_overdue()` uses above), asserting the
correct True/False at each boundary — especially the exact boundary
moment itself, a classic off-by-one edge case.

**Suggested approach:** A `@pytest.fixture` returning a fixed
`datetime`, plus `@pytest.mark.parametrize` to run the same test body
against several different fixed "now" values and expected results in
one pass.

### 4. Parametrized Tests for a Validation Function

**Problem:** A single validation function (e.g.
`is_valid_email(text)` from Chapter 18's regex work, or
`is_strong_password(text)` from an earlier chapter) has many valid and
invalid input cases worth checking, and writing one near-identical
test function per case gets repetitive fast.

**What it should do:** Write ONE pytest test function using
`@pytest.mark.parametrize` that runs the same assertion against a list
of `(input, expected_result)` pairs — at least 8-10 cases covering
clearly valid input, clearly invalid input, and boundary/edge cases
(empty string, missing `@`, minimum-length password, etc.).

**Suggested approach:**
`@pytest.mark.parametrize("text,expected", [...])` above a test
function with `text` and `expected` as parameters — pytest runs and
reports the function once per tuple in the list, each as its own named
test result.
