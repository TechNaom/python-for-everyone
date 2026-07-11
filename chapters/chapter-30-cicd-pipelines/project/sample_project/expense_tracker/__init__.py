"""expense_tracker -- a tiny personal expense tracking library.

This package exists as the sample project for Chapter 30 (CI/CD Pipelines).
It's small enough to read in five minutes, but structured like a real
installable package: a proper package directory, a couple of cooperating
modules, and a real pytest suite -- exactly the shape a CI workflow is
built to lint and test.
"""

from .models import Expense
from .tracker import ExpenseTracker

__all__ = ["Expense", "ExpenseTracker"]
__version__ = "0.1.0"
