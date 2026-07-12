"""
finance_tracker.models -- the Transaction/Income/Expense class hierarchy.

This module is the actual OOP design this capstone is graded on, and it
directly descends from three earlier chapters' patterns:

  * Chapter 14 (OOP Basics): a general class with __init__ setting instance
    attributes, instance methods, and a __str__ for readable printing --
    the same shape as the Library project's Book class.
  * Chapter 15 (OOP Deeper): `amount` is a @property with a validating
    @amount.setter that rejects any value <= 0 -- exactly like
    BankAccount.balance rejecting a negative value. `is_valid_category` is
    a @staticmethod (no instance needed), mirroring
    BankAccount.is_valid_account_number. `from_row` is a @classmethod
    alternative constructor, mirroring BankAccount.open_new_account.
  * Chapter 16 (Inheritance & Polymorphism): Income and Expense both call
    super().__init__() for shared setup (exactly like Car/Motorcycle/Truck
    all calling super().__init__(make, model, daily_rate)), and each
    overrides signed_amount() and describe() with genuinely different
    behavior, extending -- not replacing -- the base describe() string via
    super().describe(), exactly like every Vehicle subclass does.

This module deliberately knows nothing about sqlite3, argparse, or print()
-- it is pure object modeling, reused unchanged by db.py, reports.py, and
cli.py.
"""

VALID_CATEGORIES = {
    "salary",
    "freelance",
    "investment",
    "gift",
    "other_income",
    "housing",
    "food",
    "transportation",
    "utilities",
    "entertainment",
    "healthcare",
    "shopping",
    "education",
    "other_expense",
}


class Transaction:
    """Base class for any money movement: a validated amount, a category,
    a date, and an optional description. Income and Expense both build on
    top of this shared shape via super().__init__()."""

    def __init__(self, amount, category, date, description=""):
        # amount is routed through the @amount.setter below (not a bare
        # self._amount = amount) so the "never <= 0" rule applies here too,
        # exactly like BankAccount.__init__ routing balance through
        # self.balance = balance instead of self._balance = balance.
        self.amount = amount

        if not Transaction.is_valid_category(category):
            raise ValueError(f"Invalid category: {category!r}")
        self._category = category

        self._date = date
        self._description = description

    # -- @property / @amount.setter (Chapter 15) -------------------------

    @property
    def amount(self):
        """Read-facing amount -- looks like plain attribute access at every
        call site, but is really a validated method underneath."""
        return self._amount

    @amount.setter
    def amount(self, value):
        """Validates before storing: rejects zero or a negative amount, no
        matter which code path sets it -- construction, from_row(), or a
        direct `transaction.amount = ...` assignment later. This is the
        single most important correctness guarantee in this project: the
        check lives HERE, not only in __init__, so it can never be
        bypassed by mutating an existing object."""
        if amount_is_invalid(value):
            raise ValueError(
                f"amount must be a positive number, got {value!r}"
            )
        self._amount = value

    @property
    def category(self):
        return self._category

    @property
    def date(self):
        return self._date

    @property
    def description(self):
        return self._description

    # -- @staticmethod (Chapter 15) ---------------------------------------

    @staticmethod
    def is_valid_category(name):
        """Format/membership check with no instance needed at all -- the
        textbook use case for a staticmethod, mirroring
        BankAccount.is_valid_account_number."""
        return isinstance(name, str) and name.strip().lower() in VALID_CATEGORIES

    # -- @classmethod alternate constructor (Chapter 15) -------------------

    @classmethod
    def from_row(cls, db_row):
        """Alternate constructor: build a Transaction subclass instance
        from a row fetched out of SQLite (a tuple in column order
        id, type, amount, category, date, description, extra).

        Routed to by db.py, which decides Income vs. Expense based on the
        stored `type` column and calls Income.from_row/Expense.from_row
        (both of which reuse this base implementation via super()).
        Because this still assigns through self.amount / the subclass's
        own __init__, a corrupted row with a non-positive amount raises
        ValueError here exactly as it would from a fresh, hand-built
        object -- from_row() gives the database no special bypass around
        validation.
        """
        _id, _type, amount, category, date, description, extra = db_row
        return cls(amount, category, date, description, extra)

    # -- Chapter 16: base implementations subclasses override -------------

    def signed_amount(self):
        """Base behavior: an un-typed Transaction just returns its raw
        amount. Income and Expense both override this with genuinely
        different signs -- this base version exists mainly so
        Transaction is never left with an abstract method that would
        blow up if somehow called directly."""
        return self.amount

    def describe(self):
        """Base summary line. Both subclasses extend this via
        super().describe() rather than replacing it outright, exactly
        like every Vehicle subclass extending Vehicle.describe()."""
        return f"[{self.category}] {self.date}: ${self.amount:,.2f}"

    def __str__(self):
        return self.describe()

    def __repr__(self):
        return (
            f"{type(self).__name__}(amount={self.amount!r}, "
            f"category={self.category!r}, date={self.date!r})"
        )


def amount_is_invalid(value):
    """Shared validation rule used by the @amount.setter: True if `value`
    is not a positive number."""
    try:
        return float(value) <= 0
    except (TypeError, ValueError):
        return True


class Income(Transaction):
    """Money coming in. Adds a `source` (e.g. 'employer', 'client').
    Overrides signed_amount() (+amount) and describe() (extends the base
    string with the source), both genuinely different from the base
    class and from Expense."""

    def __init__(self, amount, category, date, description="", source=""):
        super().__init__(amount, category, date, description)
        self._source = source

    @property
    def source(self):
        return self._source

    def signed_amount(self):
        # Income increases the running balance.
        return self.amount

    def describe(self):
        base = super().describe()
        source_part = f" from {self.source}" if self.source else ""
        return f"INCOME  {base}{source_part}"


class Expense(Transaction):
    """Money going out. Adds a `payment_method` (e.g. 'credit_card',
    'cash'). Overrides signed_amount() (-amount) and describe() (extends
    the base string with the payment method), both genuinely different
    from the base class and from Income."""

    def __init__(self, amount, category, date, description="", payment_method=""):
        super().__init__(amount, category, date, description)
        self._payment_method = payment_method

    @property
    def payment_method(self):
        return self._payment_method

    def signed_amount(self):
        # Expense decreases the running balance.
        return -self.amount

    def describe(self):
        base = super().describe()
        method_part = f" via {self.payment_method}" if self.payment_method else ""
        return f"EXPENSE {base}{method_part}"
