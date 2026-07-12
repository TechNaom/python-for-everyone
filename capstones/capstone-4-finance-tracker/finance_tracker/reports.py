"""
finance_tracker.reports -- reporting built entirely on polymorphism.

Every function here takes a plain list of Transaction objects (Income
and/or Expense, freely mixed) and computes its answer by calling
.signed_amount() / .amount / .category / .date polymorphically. None of
these functions ever check `type(t) is Income` or `isinstance(t, Expense)`
to decide HOW to do arithmetic -- that's the whole payoff of
signed_amount() living on the class hierarchy instead of here: a running
balance is one line, and it stays correct even if a third subclass
(Transfer? Refund?) gets added later, with zero changes needed in this
file.

The one place isinstance() would ever be reasonable here is a genuine
filtering feature (e.g. "income only" view) -- not present in the MVP,
but the reason it isn't used anywhere below is architectural, not an
oversight: filtering by kind is a different concern than summing amounts.
"""

from collections import defaultdict


def balance(transactions) -> float:
    """The running balance across a (possibly mixed) list of Transaction
    objects. One line, zero isinstance/type() branching -- every object
    in the list just answers .signed_amount() for itself."""
    return sum(t.signed_amount() for t in transactions)


def totals_by_category(transactions) -> dict:
    """Net signed total per category, built the same accumulate-and-count
    way earlier chapters' projects build dicts. A category with only
    expenses nets negative, one with only income nets positive, and a
    category with both nets to their combined signed total -- again with
    no branching on the object's type, just its category and its own
    signed_amount()."""
    totals = defaultdict(float)
    for transaction in transactions:
        totals[transaction.category] += transaction.signed_amount()
    return dict(totals)


def monthly_summary(transactions, year: int, month: int) -> dict:
    """Summarize one calendar month (dates stored as 'YYYY-MM-DD' strings,
    so a simple string prefix match is enough -- no date-parsing library
    needed). Returns a dict with income total, expense total, and net
    balance for that month, plus how many transactions matched.
    """
    prefix = f"{year:04d}-{month:02d}"
    month_transactions = [t for t in transactions if t.date.startswith(prefix)]

    total_income = sum(t.signed_amount() for t in month_transactions if t.signed_amount() > 0)
    total_expense = sum(t.signed_amount() for t in month_transactions if t.signed_amount() < 0)

    return {
        "year": year,
        "month": month,
        "count": len(month_transactions),
        "total_income": total_income,
        "total_expense": total_expense,
        "net": total_income + total_expense,
    }
