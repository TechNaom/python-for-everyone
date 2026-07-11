"""
Chapter 27 Project: Test Suite for an Earlier Project
See README.md in this folder for full instructions.

Run this from inside the project/ folder:
    python3 -m pytest starter.py -v

Standard library's `pytest` and `unittest.mock` only -- install pytest
first if you don't have it: `pip install pytest`.

PART 1 below (TaskManager and friends) is already finished for you --
it's the "earlier project" you're testing, not what you're building today.
Your job is PART 2: fill in the TODO-marked test functions.
"""

from datetime import datetime, timedelta

import pytest
from unittest.mock import MagicMock, patch


# =======================================================================
# PART 1: The "earlier project" under test (already complete -- read it,
# don't rewrite it. You're writing tests AGAINST this code.)
# =======================================================================

class NotificationSender:
    """Stands in for a real external dependency -- an email/SMS/push
    notification service. In real code this would make a network call;
    here it just prints, but the point is the SAME either way: a test
    should never actually call this during a test run.
    """

    def send(self, task_title, recipient):
        print(f"Sending overdue notice for '{task_title}' to {recipient}")
        return True


class Task:
    """A single task: a title, a due date, and a completed flag."""

    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.completed = False

    def is_overdue(self, now=None):
        """A task is overdue if it isn't completed and its due_date has
        passed. `now` defaults to the real current time -- accepting it
        as a parameter (instead of always calling datetime.now() inside)
        is what makes this method testable without waiting for real time
        to pass, or needing to mock datetime itself.
        """
        if self.completed:
            return False
        current_time = now if now is not None else datetime.now()
        return current_time > self.due_date

    def __repr__(self):
        status = "done" if self.completed else "pending"
        return f"Task({self.title!r}, due={self.due_date:%Y-%m-%d}, {status})"


class TaskManager:
    """Tracks a list of Task objects: add, complete, list overdue, and
    notify about overdue tasks via an injected NotificationSender."""

    def __init__(self, notifier=None):
        self.tasks = []
        # Dependency injection: a real NotificationSender by default, but
        # a caller (or a test) can swap in something else entirely --
        # this is exactly what makes notify_overdue() mockable below.
        self.notifier = notifier if notifier is not None else NotificationSender()

    def add_task(self, title, due_date):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = Task(title, due_date)
        self.tasks.append(task)
        return task

    def complete_task(self, title):
        """Mark the first not-yet-completed task with this title as
        completed. Returns True if a task was found and completed,
        False if no matching pending task exists."""
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.completed = True
                return True
        return False

    def get_overdue_tasks(self, now=None):
        return [task for task in self.tasks if task.is_overdue(now)]

    def notify_overdue(self, recipient, now=None):
        """Send one notification per overdue task via self.notifier.
        Returns the number of notifications actually sent. This is the
        method worth mocking in tests -- it has a real side effect
        (calling out to NotificationSender.send()) that a test suite
        should never trigger for real.
        """
        overdue = self.get_overdue_tasks(now)
        sent = 0
        for task in overdue:
            if self.notifier.send(task.title, recipient):
                sent += 1
        return sent


# =======================================================================
# PART 2: The test suite -- YOUR WORK STARTS HERE
# =======================================================================
# Use the AAA pattern (Arrange, Act, Assert) in every test. Each fixture
# below must build FRESH state -- no test should be able to leak state
# into another (Chapter 27's sub-topic 4 on test isolation).

@pytest.fixture
def manager():
    """A fresh, empty TaskManager for every test that asks for it."""
    return TaskManager()


@pytest.fixture
def fixed_now():
    """A fixed point in time so overdue checks are deterministic --
    never depend on the real datetime.now() in a test, or the test's
    pass/fail would depend on when it happens to run."""
    return datetime(2026, 6, 15, 12, 0, 0)


# --- add_task(): happy path + edge cases -------------------------------

# TODO 1: test_add_task_returns_task_with_given_title(manager, fixed_now)
# Arrange a due date one day after fixed_now. Act: call
# manager.add_task("Write report", due). Assert the returned task's
# .title, .due_date, and .completed (should start False) are correct.


# TODO 2: test_add_task_appends_to_manager_tasks_list(manager, fixed_now)
# Add two different tasks via manager.add_task(). Assert
# len(manager.tasks) == 2.


# TODO 3: test_add_task_rejects_empty_title(manager, fixed_now)
# Assert that calling manager.add_task("", ...) raises ValueError.
# Use `with pytest.raises(ValueError):`.


# TODO 4: test_add_task_rejects_whitespace_only_title(manager, fixed_now)
# Edge case: a title of "   " (spaces only) should ALSO raise
# ValueError, even though "   " is a non-empty, truthy string.


# --- complete_task(): happy path + edge cases --------------------------

# TODO 5: test_complete_task_marks_matching_task_done(manager, fixed_now)
# Add a task, then call manager.complete_task() with its title. Assert
# the call returns True and manager.tasks[0].completed is True.


# TODO 6: test_complete_task_returns_false_when_no_match(manager)
# Edge case: call manager.complete_task() on a title that was never
# added. Assert it returns False (not an exception).


# TODO 7: test_complete_task_only_affects_first_pending_match(manager, fixed_now)
# Edge case: add two tasks with the SAME title, then complete_task()
# once. Assert only tasks[0] is completed and tasks[1] is still pending.


# --- get_overdue_tasks(): happy path + edge cases -----------------------

# TODO 8: test_get_overdue_tasks_returns_only_past_due_incomplete_tasks(manager, fixed_now)
# Add one task due BEFORE fixed_now and one due AFTER it. Call
# manager.get_overdue_tasks(now=fixed_now). Assert the result contains
# only the past-due task.


# TODO 9: test_get_overdue_tasks_excludes_completed_tasks_even_if_past_due(manager, fixed_now)
# Edge case: add a task due before fixed_now, then complete_task() it.
# Assert get_overdue_tasks(now=fixed_now) returns an empty list --
# completed tasks never count as overdue, no matter their due date.


# TODO 10: test_get_overdue_tasks_empty_when_no_tasks_added(manager, fixed_now)
# Edge case: an empty manager. Assert get_overdue_tasks() returns [].


# --- notify_overdue(): the mocking example ------------------------------

# TODO 11: test_notify_overdue_calls_notifier_send_once_per_overdue_task(fixed_now)
# This one does NOT use the `manager` fixture -- build your own
# TaskManager here, injecting a unittest.mock.MagicMock() as the
# notifier (TaskManager(notifier=mock_notifier)), so no real
# notification is ever sent.
#   1. Set mock_notifier.send.return_value = True.
#   2. Add two overdue tasks and one NOT-yet-due task.
#   3. Call manager.notify_overdue("dev@example.com", now=fixed_now).
#   4. Assert the returned count is 2.
#   5. Assert mock_notifier.send.call_count == 2.
#   6. Assert mock_notifier.send.assert_any_call() was called with each
#      overdue task's title and "dev@example.com".


# TODO 12: test_notify_overdue_does_not_count_failed_sends(fixed_now)
# Edge case: set mock_notifier.send.return_value = False this time (the
# notifier reports failure). Add one overdue task. Assert
# notify_overdue() returns 0 -- a failed send should NOT be counted.


# TODO 13: test_notify_overdue_never_touches_the_real_notification_sender(fixed_now, capsys)
# This test proves mocking is actually happening, not just assumed. Use
# `with patch.object(NotificationSender, "send") as mock_send:` around
# a TaskManager() built WITHOUT passing a notifier (so it uses the real
# NotificationSender class, but patched). Add one overdue task, call
# notify_overdue(), then:
#   1. Assert mock_send.assert_called_once().
#   2. Use capsys.readouterr() and assert captured.out == "" -- proving
#      the real send()'s print() statement never actually ran.


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
