"""The ExpenseTracker: holds a collection of Expense records and answers
questions about them (totals, filtering by category, over/under budget)."""

from .models import Expense


class ExpenseTracker:
    """An in-memory collection of expenses with basic query operations."""

    def __init__(self, monthly_budget=None):
        self._expenses = []
        self.monthly_budget = monthly_budget

    def add(self, expense):
        """Add an expense to the tracker."""
        if not isinstance(expense, Expense):
            raise TypeError("add() expects an Expense instance")
        self._expenses.append(expense)

    def total(self):
        """Total of every expense recorded so far."""
        return sum(e.amount for e in self._expenses)

    def total_by_category(self, category):
        """Total of every expense in a single category."""
        return sum(e.amount for e in self._expenses if e.category == category)

    def by_category(self):
        """A dict mapping each category present to its running total."""
        totals = {}
        for e in self._expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals

    def count(self):
        """How many expenses have been recorded."""
        return len(self._expenses)

    def is_over_budget(self):
        """Whether the running total exceeds monthly_budget.

        Returns False if no budget was set -- there's nothing to be over.
        """
        if self.monthly_budget is None:
            return False
        return self.total() > self.monthly_budget

    def remaining_budget(self):
        """How much budget is left this month, or None if no budget is set."""
        if self.monthly_budget is None:
            return None
        return self.monthly_budget - self.total()

    def largest_expense(self):
        """The single largest expense recorded, or None if there are none."""
        if not self._expenses:
            return None
        return max(self._expenses, key=lambda e: e.amount)
