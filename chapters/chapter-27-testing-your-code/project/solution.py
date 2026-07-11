"""
Chapter 27 Project: Test Suite for an Earlier Project -- reference solution.

Run this from inside the project/ folder:
    python3 -m pytest solution.py -v

(Standard library's unittest can also discover/run this file, since every
test function here uses plain `assert` -- but pytest is what actually
reports each one individually and is what this project is built around.)

This file contains BOTH pieces on purpose, in one file, so the project
stays a single download like every other chapter:

  1. The "earlier project" under test: TaskManager, a small task-tracking
     class (the kind of thing you might have built back in Chapter 11's
     OOP chapter) with an add/complete/overdue-check workflow, PLUS one
     method, notify_overdue(), that calls an external dependency
     (a NotificationSender) -- exactly the kind of method that's worth
     mocking rather than actually invoking in a test.

  2. The test suite itself -- pytest fixtures, unittest.mock, and a set
     of tests that actually exercise TaskManager: happy path, edge
     cases, and the mocked external call.
"""

from datetime import datetime, timedelta

import pytest
from unittest.mock import MagicMock, patch


# =======================================================================
# PART 1: The "earlier project" under test
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
# PART 2: The test suite
# =======================================================================
# AAA pattern throughout: Arrange, Act, Assert. Fixtures build fresh
# state for every test so no test can leak state into another (Chapter
# 27's sub-topic 4) -- notice `manager` below returns a brand-new
# TaskManager every time it's requested, never a shared/module-level one.

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

def test_add_task_returns_task_with_given_title(manager, fixed_now):
    # Arrange
    due = fixed_now + timedelta(days=1)
    # Act
    task = manager.add_task("Write report", due)
    # Assert
    assert task.title == "Write report"
    assert task.due_date == due
    assert task.completed is False


def test_add_task_appends_to_manager_tasks_list(manager, fixed_now):
    manager.add_task("Write report", fixed_now + timedelta(days=1))
    manager.add_task("Review PR", fixed_now + timedelta(days=2))

    assert len(manager.tasks) == 2


def test_add_task_rejects_empty_title(manager, fixed_now):
    with pytest.raises(ValueError):
        manager.add_task("", fixed_now + timedelta(days=1))


def test_add_task_rejects_whitespace_only_title(manager, fixed_now):
    # Edge case: "   " is truthy as a non-empty string, so a naive
    # `if not title` check alone would let this slip through uncaught.
    with pytest.raises(ValueError):
        manager.add_task("   ", fixed_now + timedelta(days=1))


# --- complete_task(): happy path + edge cases --------------------------

def test_complete_task_marks_matching_task_done(manager, fixed_now):
    manager.add_task("Write report", fixed_now + timedelta(days=1))

    result = manager.complete_task("Write report")

    assert result is True
    assert manager.tasks[0].completed is True


def test_complete_task_returns_false_when_no_match(manager):
    # Edge case: completing a task that was never added.
    result = manager.complete_task("Nonexistent task")

    assert result is False


def test_complete_task_only_affects_first_pending_match(manager, fixed_now):
    # Edge case: two tasks share a title -- only the first pending one
    # should flip to completed, the second stays untouched.
    manager.add_task("Standup", fixed_now)
    manager.add_task("Standup", fixed_now)

    manager.complete_task("Standup")

    assert manager.tasks[0].completed is True
    assert manager.tasks[1].completed is False


# --- get_overdue_tasks(): happy path + edge cases -----------------------

def test_get_overdue_tasks_returns_only_past_due_incomplete_tasks(manager, fixed_now):
    overdue_task = manager.add_task("Late thing", fixed_now - timedelta(days=1))
    manager.add_task("Future thing", fixed_now + timedelta(days=1))

    result = manager.get_overdue_tasks(now=fixed_now)

    assert result == [overdue_task]


def test_get_overdue_tasks_excludes_completed_tasks_even_if_past_due(manager, fixed_now):
    # Edge case: a task can be technically past its due date but should
    # NOT count as overdue once it's been completed.
    manager.add_task("Late but done", fixed_now - timedelta(days=1))
    manager.complete_task("Late but done")

    result = manager.get_overdue_tasks(now=fixed_now)

    assert result == []


def test_get_overdue_tasks_empty_when_no_tasks_added(manager, fixed_now):
    # Edge case: an empty manager shouldn't error, just return [].
    assert manager.get_overdue_tasks(now=fixed_now) == []


# --- notify_overdue(): the mocking example ------------------------------

def test_notify_overdue_calls_notifier_send_once_per_overdue_task(fixed_now):
    # Arrange: inject a Mock in place of a real NotificationSender so
    # this test never actually sends anything -- it only checks that
    # TaskManager *asked* the notifier to send, the correct number of
    # times, with the right arguments.
    mock_notifier = MagicMock()
    mock_notifier.send.return_value = True
    manager = TaskManager(notifier=mock_notifier)
    manager.add_task("Late thing", fixed_now - timedelta(days=1))
    manager.add_task("Also late", fixed_now - timedelta(days=2))
    manager.add_task("Not due yet", fixed_now + timedelta(days=1))

    # Act
    sent_count = manager.notify_overdue("dev@example.com", now=fixed_now)

    # Assert
    assert sent_count == 2
    assert mock_notifier.send.call_count == 2
    mock_notifier.send.assert_any_call("Late thing", "dev@example.com")
    mock_notifier.send.assert_any_call("Also late", "dev@example.com")


def test_notify_overdue_does_not_count_failed_sends(fixed_now):
    # Edge case: if the notifier reports failure (returns False), that
    # task should not be counted as sent.
    mock_notifier = MagicMock()
    mock_notifier.send.return_value = False
    manager = TaskManager(notifier=mock_notifier)
    manager.add_task("Late thing", fixed_now - timedelta(days=1))

    sent_count = manager.notify_overdue("dev@example.com", now=fixed_now)

    assert sent_count == 0


def test_notify_overdue_never_touches_the_real_notification_sender(fixed_now, capsys):
    # This test demonstrates WHY mocking matters: using the real
    # NotificationSender in a test would print/perform a real side
    # effect on every test run. Patching it here proves the real one is
    # never invoked -- nothing is printed to stdout.
    with patch.object(NotificationSender, "send") as mock_send:
        mock_send.return_value = True
        manager = TaskManager()  # uses the real NotificationSender class
        manager.add_task("Late thing", fixed_now - timedelta(days=1))

        manager.notify_overdue("dev@example.com", now=fixed_now)

        mock_send.assert_called_once()
        captured = capsys.readouterr()
        assert captured.out == ""  # the real .send()'s print() never ran


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
