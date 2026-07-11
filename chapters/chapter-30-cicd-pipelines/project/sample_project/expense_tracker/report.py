"""Turn an ExpenseTracker's data into a human-readable summary report.

NOTE FOR LEARNERS: this file has one intentional lint violation (an unused
import) left in on purpose -- see the chapter project README for why, and
run `ruff check .` yourself to watch it get caught.
"""

import sys  # unused import -- intentionally left in for the lint job to catch

from .tracker import ExpenseTracker


def summary_lines(tracker: ExpenseTracker) -> list[str]:
    """Build a list of report lines summarizing a tracker's expenses."""
    lines = [f"Total spent: ${tracker.total():.2f}"]

    by_category = tracker.by_category()
    if by_category:
        lines.append("By category:")
        for category, amount in sorted(by_category.items()):
            lines.append(f"  {category}: ${amount:.2f}")
    else:
        lines.append("No expenses recorded yet.")

    if tracker.monthly_budget is not None:
        remaining = tracker.remaining_budget()
        if tracker.is_over_budget():
            lines.append(f"Over budget by ${-remaining:.2f}!")
        else:
            lines.append(f"Remaining budget: ${remaining:.2f}")

    return lines


def print_summary(tracker: ExpenseTracker) -> None:
    """Print a summary report of a tracker's expenses to stdout."""
    for line in summary_lines(tracker):
        print(line)
