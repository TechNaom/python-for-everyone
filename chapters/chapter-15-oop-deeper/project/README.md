# Chapter 15 Project: Bank Account System

A menu-driven bank account system built **around this chapter's deeper OOP
tools** as its core organizing principle -- a `BankAccount` class exposes
`balance` as a `@property` with a validating `@balance.setter` (rejects
setting it directly to a negative value), a `@classmethod` alternative
constructor (`open_new_account`, which builds an account a different way
than a plain `__init__` call by generating its own account number), and a
`@staticmethod` utility (`is_valid_account_number`) that validates an
account-number format with no need for any particular instance's data.
Encapsulation is practiced with a single leading underscore (`_balance`,
`_owner`, `_account_number`) -- an internal-use naming convention, not
enforced privacy, matching this chapter's "consenting adults" philosophy
covered in `interview-questions.html`.

## What you'll build

An object model covering this chapter's core tools -- **`@staticmethod`,
`@classmethod`, `@property` getters and setters, and encapsulation
conventions** -- plus a menu loop offering six real operations:

1. Open a new account
2. Deposit
3. Withdraw
4. Check balance
5. View account details
6. List all accounts
7. Quit

The object model itself is built from these pieces:

- `BankAccount.__init__(self, owner, account_number, balance=0)` -- sets
  `self._owner`, validates `account_number` via the staticmethod (raising
  `ValueError` if it's badly formatted), sets `self._account_number`, then
  routes `balance` through the `@balance.setter` so the same validation
  rule applies to a starting balance too.
- `BankAccount.open_new_account(cls, owner, opening_deposit=0)` -- a
  `@classmethod` alternative constructor. It generates its own account
  number (`f"ACC-{cls._next_suffix}"`, incrementing a shared class
  attribute counter) instead of requiring the caller to supply one, then
  returns `cls(owner, account_number, opening_deposit)`. Using `cls`
  instead of hard-coding `BankAccount(...)` is what makes this a proper
  classmethod pattern.
- `BankAccount.is_valid_account_number(account_number)` -- a
  `@staticmethod` that checks the format is `"ACC-"` followed by one or
  more digits. It needs no instance or class data at all, just the string
  passed in -- the textbook use case for a staticmethod.
- `BankAccount.balance` -- a `@property` getter that returns `self._balance`,
  paired with a `@balance.setter` that raises `ValueError` if the incoming
  value is negative, otherwise stores it. Every deposit, withdrawal, and
  the initial balance in `__init__` all funnel through this one setter, so
  the "never negative" rule only has to be written once.
- `BankAccount.owner` / `BankAccount.account_number` -- read-only
  properties (getter only, no setter) exposing the underlying
  `_owner`/`_account_number` without allowing them to be reassigned through
  the public interface.
- `BankAccount.deposit(amount)` / `BankAccount.withdraw(amount)` -- instance
  methods that adjust `self.balance` through the property (not
  `self._balance` directly), returning `True`/`False` depending on whether
  the operation was valid.
- `BankAccount.__str__(self)` -- returns a readable one-line string like
  `Account ACC-1000 (Aria Chen) -- balance: $500.00`.
- `find_account(accounts, account_number)` -- loops over a list of
  `BankAccount` objects and returns the first match, or `None`.

Two accounts are seeded into the session when the program starts, so the
menu has something to work with right away.

Example run:

```
=== Bank Account System ===
Loaded 2 account(s).

1. Open a new account
2. Deposit
3. Withdraw
4. Check balance
5. View account details
6. List all accounts
7. Quit
Choose an option (1-7): 4

Account number: ACC-1000
Balance for ACC-1000: $500.00

1. Open a new account
2. Deposit
3. Withdraw
4. Check balance
5. View account details
6. List all accounts
7. Quit
Choose an option (1-7): 6

All accounts (2):
  Account ACC-1000 (Aria Chen) -- balance: $500.00
  Account ACC-1001 (Devon Brooks) -- balance: $150.00

1. Open a new account
2. Deposit
3. Withdraw
4. Check balance
5. View account details
6. List all accounts
7. Quit
Choose an option (1-7): 7

Goodbye!
```

Notice how much of this chapter shows up in one small program: a
`@staticmethod` validating raw input with no instance in sight, a
`@classmethod` building a new object a different way than the ordinary
constructor, and a `@property`/`@x.setter` pair that lets `account.balance`
still read like plain attribute access everywhere in the menu code while
actually enforcing "never negative" behind the scenes. If a much stricter
rule showed up later -- say, a minimum balance, or a daily withdrawal cap
-- it could be added entirely inside `balance`'s setter, with zero changes
needed anywhere else that already reads or writes `account.balance`. That's
the real point of a property: the public interface (`account.balance = x`)
never has to change even as the validation behind it gets richer.

## How to run it

```bash
cd chapters/chapter-15-oop-deeper/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder).

## Ideas to make it your own (optional stretch goals)

- Add a "close account" option that only allows closing an account if its
  balance is exactly 0, reusing `find_account`.
- Add a `BankAccount.interest_rate` class attribute and an
  `apply_interest()` instance method that increases `self.balance` by that
  rate, then a matching menu option to apply interest to every account at
  once.
- Add a `minimum_balance` check inside the `@balance.setter` (e.g. no
  account may ever drop below a shared class-level minimum) -- notice how
  this can be added in exactly one place without touching `deposit`,
  `withdraw`, or any menu code at all.

## Why this project matters

Every real banking app, payment platform, or point-of-sale system relies on
exactly this pattern: money-related fields that absolutely cannot be set to
an invalid value by accident, and constructors that need to build the same
kind of object from more than one shape of starting data (a brand-new
account opened in a branch versus one restored from a backup file, for
example). A `@property` setter is precisely how real production code
guarantees "this value is always validated, no matter which code path
touches it" without forcing every single caller to remember to call some
`validate_and_set_balance()` function by hand -- and a `@classmethod`
alternative constructor is precisely how real classes offer more than one
sane way to build an object without duplicating `__init__`'s logic.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The Bank
Account System above is fully built out with a starter and reference
solution -- the four ideas below are not. Each is a real, grounded use case
solvable with only what's been taught through Chapter 15 (everything
through Chapter 14's general classes and dunder methods, plus
`@staticmethod`, `@classmethod`, and `@property` getters/setters -- no
inheritance, since that's Chapter 16). No starter or solution files are
provided on purpose -- building one of these unassisted is the point.

### 1. Temperature Converter Class

**Problem:** A weather app or science tool needs to represent a temperature
that's always physically valid (never below absolute zero) and needs to be
constructed from more than one real-world unit -- most data comes in as
Celsius, but plenty of sources (older US weather data, some APIs) give
Fahrenheit instead.

**What it should do:** Build a `Temperature` class storing the value
internally in Celsius, with a `celsius` `@property` and `@celsius.setter`
that raises `ValueError` if the value is below -273.15 (absolute zero), a
read-only `fahrenheit` `@property` that computes `celsius * 9/5 + 32` on
the fly, and a `@classmethod` alternative constructor
`from_fahrenheit(cls, f)` that converts an incoming Fahrenheit value to
Celsius before constructing the instance. Menu options: create a
temperature from Celsius, create one from Fahrenheit, view both units for
a stored temperature, attempt to set an invalid (impossibly low) value to
see the validation reject it, and quit.

**Suggested approach:** Keep a running list of `Temperature` objects (or
just one "current" temperature if you want to keep it simpler), and derive
`fahrenheit` purely from the stored `celsius` value inside its getter --
never store both independently, or they could drift out of sync with each
other.

### 2. Product Catalog with Price Validation

**Problem:** An online store's product catalog needs every listed price to
always be a sane, non-negative number -- a bug or bad data import that
sets a price to a negative value would let an order actually charge a
customer negative money, or crash a checkout calculation downstream.

**What it should do:** Build a `Product` class with a `name` attribute, a
`price` `@property` with a `@price.setter` that rejects negative values (
`raise ValueError`), a `@staticmethod` `is_valid_sku(sku)` that checks a
product SKU code matches a fixed format (e.g. three uppercase letters
followed by four digits), and a `@classmethod`
`from_discount(cls, name, sku, original_price, discount_percent)`
alternative constructor that computes a discounted price before
constructing the instance. Menu options: add a product at full price, add
a discounted product, update a product's price, list all products, and
quit.

**Suggested approach:** Validate the SKU inside `__init__` using the
staticmethod (the same pattern this chapter's `BankAccount.__init__` uses
for `is_valid_account_number`), and have `from_discount` compute
`original_price * (1 - discount_percent / 100)` before calling `cls(...)`.

### 3. Employee Record System with CSV Import

**Problem:** An HR or payroll system needs a consistent `Employee` object
for every staff member, but employee data often arrives as a row from a
CSV export (from a different system, or a spreadsheet HR maintains) rather
than as neatly separated function arguments.

**What it should do:** Build an `Employee` class with `name`, `role`, and
`salary` instance attributes, a `salary` `@property` with a
`@salary.setter` that rejects a negative salary, and a `@classmethod`
`from_csv_row(cls, row)` alternative constructor that takes a single
comma-separated string like `"Sam Rivera,Engineer,95000"`, splits it, and
builds an `Employee` from the pieces. Menu options: add an employee
manually (prompting for each field), add an employee by pasting a CSV row,
give an employee a raise (validated through the property), list all
employees, and quit.

**Suggested approach:** Reuse Chapter 13's `csv` module ideas conceptually
even without reading an actual file -- `row.split(",")` on a single pasted
line is enough to build the three pieces `from_csv_row` needs, then
`cls(name, role, float(salary_str))`.

### 4. Rectangle/Circle Shape Validator

**Problem:** A drawing or CAD-style tool needs shape objects whose
dimensions are always physically valid (no shape can have a negative width,
height, or radius), and needs a shared way to validate raw numeric input
before it's ever used to build a shape.

**What it should do:** Build a `Rectangle` class with `width` and `height`
`@property`/`@x.setter` pairs that each reject non-positive values, an
`area()` instance method, and a `@staticmethod` `is_positive_number(value)`
that both setters call internally to check a value before accepting it.
Do the same for a separate `Circle` class with a `radius` property and an
`area()` method. Menu options: create a rectangle, create a circle, view a
shape's area, attempt to set an invalid (zero or negative) dimension to
see the validation reject it, and quit.

**Suggested approach:** Since `Rectangle` and `Circle` are two separate,
unrelated classes at this stage (no inheritance until Chapter 16), define
`is_positive_number` as a `@staticmethod` on each class separately, or as a
plain standalone function shared by both if you want to avoid repeating
it -- both are reasonable until Chapter 16 introduces a shared parent class
as the cleaner fix.
