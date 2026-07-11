"""Data model for a single expense."""

from datetime import date

ALLOWED_CATEGORIES = {"food", "transport", "housing", "entertainment", "other"}


class Expense:
    """A single expense record.

    Attributes:
        amount: The expense amount in dollars. Must be positive.
        category: One of ALLOWED_CATEGORIES.
        note: A free-text description of the expense.
        on: The date the expense occurred (defaults to today).
    """

    def __init__(self, amount, category, note="", on=None):
        if amount <= 0:
            raise ValueError(f"amount must be positive, got {amount}")
        if category not in ALLOWED_CATEGORIES:
            raise ValueError(
                f"category must be one of {sorted(ALLOWED_CATEGORIES)}, "
                f"got {category!r}"
            )
        self.amount = amount
        self.category = category
        self.note = note
        self.on = on if on is not None else date.today()

    def to_dict(self):
        """Serialize this expense to a plain dict (e.g. for JSON export)."""
        return {
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "on": self.on.isoformat(),
        }
