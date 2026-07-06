# Chapter 12 Project: ATM Simulator

A menu-driven ATM simulator built **around custom exceptions** as its
core organizing principle -- every rule about what makes a transaction
valid (can't withdraw more than the balance, can't deposit or withdraw
a non-positive amount) is enforced by *raising* a custom exception
class subclassed from `Exception`, and the menu loop's whole job is
just to *catch* those exceptions and print a friendly message, exactly
like Chapter 11's project was organized around `math`/`datetime`. Each
operation lives in its own small function, matching Chapter 10's
function-library pattern.

## What you'll build

A function library covering this chapter's core tools -- **custom
exception classes, `raise`, and `try`/`except`** -- plus a menu loop
offering five options:

1. Check balance
2. Deposit
3. Withdraw
4. View transaction history
5. Quit

The library itself is built from these pieces:

- `InsufficientFundsError(Exception)` -- a custom exception raised when
  a withdrawal amount is more than the current balance. Its
  `__init__` stores `amount` and `balance` as attributes (so calling
  code can inspect exactly what was attempted, not just read a
  message) and builds a clear message via `super().__init__(...)`.
- `InvalidAmountError(Exception)` -- a custom exception raised when a
  deposit/withdrawal amount is zero, negative, or not a number at all.
  Stores the bad `amount` as an attribute the same way.
- `validate_amount(amount)` -- raises `InvalidAmountError` if `amount`
  isn't a positive number.
- `parse_amount(raw)` -- converts typed text into a positive float,
  catching the built-in `ValueError` from a bad `float(raw)` call and
  **re-raising** it as `InvalidAmountError` (`raise ... from e`) so the
  rest of the program only ever has to handle this project's own
  exception types, not a mix of built-in and custom ones.
- `deposit(balance, amount)` -- validates the amount, then returns the
  new balance.
- `withdraw(balance, amount)` -- validates the amount, checks it
  against the balance, and raises `InsufficientFundsError` if it's too
  much; otherwise returns the new balance.
- `record_transaction(history, kind, amount, balance_after, today)` --
  builds one transaction dict and appends it to the running `history`
  list.
- `print_transaction(entry, index)` -- prints one numbered, aligned
  transaction line.

Every transaction during the session is appended to a running
`history` list, so option 4 can report on the full session -- the same
running-state pattern earlier chapters' projects have used, just now
organized around custom exceptions instead of a data structure or
module.

Example run:

```
=== ATM Simulator ===
Today's date: 2026-07-06
Starting balance: $100.00

1. Check balance
2. Deposit
3. Withdraw
4. View transaction history
5. Quit
Choose an option (1-5): 2
Amount to deposit: $50
Deposited $50.00. New balance: $150.00

1. Check balance
2. Deposit
3. Withdraw
4. View transaction history
5. Quit
Choose an option (1-5): 3
Amount to withdraw: $30
Withdrew $30.00. New balance: $120.00

1. Check balance
2. Deposit
3. Withdraw
4. View transaction history
5. Quit
Choose an option (1-5): 3
Amount to withdraw: $99999
Withdrawal failed: cannot withdraw $99999.00 -- balance is only $120.00

1. Check balance
2. Deposit
3. Withdraw
4. View transaction history
5. Quit
Choose an option (1-5): 3
Amount to withdraw: $-5
Withdrawal failed: amount must be a positive number, got -5.0

1. Check balance
2. Deposit
3. Withdraw
4. View transaction history
5. Quit
Choose an option (1-5): 4

1. [2026-07-06] deposit    $50.00  (balance after: $150.00)
2. [2026-07-06] withdraw   $30.00  (balance after: $120.00)

1. Check balance
2. Deposit
3. Withdraw
4. View transaction history
5. Quit
Choose an option (1-5): 5

Session summary: 2 transaction(s), final balance $120.00.
Goodbye!
```

Notice that two of the calls above -- withdrawing more than the
balance, and withdrawing a negative amount -- both raise a custom
exception, and the program keeps running afterward instead of
crashing. That's the entire point of this project: exceptions aren't
decorative, they're the actual mechanism enforcing "this transaction
isn't allowed," caught gracefully at the one place (the menu loop)
that knows how to explain the problem to a user.

## How to run it

```bash
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Add a `NegativeBalanceError` guard rail: raise a custom exception if
  any bug elsewhere ever leaves `balance` negative after a deposit or
  withdrawal, as a defensive double-check on top of `withdraw`'s own
  validation.
- Add a "transfer to another simulated account" option that runs
  `withdraw` on one balance and `deposit` on another, re-raising
  `InsufficientFundsError` if the withdrawal half fails so the deposit
  half never happens.
- Add a `DailyLimitExceededError` custom exception that tracks total
  withdrawals for the session and blocks any single day's withdrawals
  from exceeding a fixed limit (e.g. $500), reusing the same
  raise/catch pattern as `InsufficientFundsError`.

## Why this project matters

An ATM refusing an overdraft, a payment API rejecting a negative
charge amount, a banking app locking an account after too many bad
PIN attempts -- all of these are, underneath, the exact same shape:
some rule about what's allowed gets violated, a specific, well-named
exception gets raised carrying the details of what went wrong, and
code further up the call stack catches that specific exception and
decides what to tell the user. That's the real skill this project
practices -- custom exceptions with real attributes (`e.amount`,
`e.balance`) that carry actual debugging context, not just a generic
error string, are what separates a defensive, production-ready
function from one that merely "works on the happy path."

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
ATM Simulator above is fully built out with a starter and reference
solution -- the four ideas below are not. Each is a real, grounded use
case solvable with only what's been taught through Chapter 12
(everything through Chapter 11's modules material, plus `try`/`except`/
`else`/`finally`/`raise` and custom exception classes subclassing
`Exception`). No starter or solution files are provided on purpose --
building one of these unassisted, menu loop and all, is the point.

### 1. Signup Form Validator

**Problem:** Every signup form -- a SaaS product, a newsletter, a game
account -- needs to reject bad input (an empty username, a password
that's too short, an age that isn't a number) with a specific, useful
error message per rule, not one generic "invalid input" message that
leaves the user guessing what to fix.

**What it should do:** Define one custom exception per validation rule
-- e.g. `UsernameTooShortError`, `WeakPasswordError`,
`InvalidAgeError` -- each carrying the offending value as an attribute.
Build `validate_username(username)`, `validate_password(password)`,
and `validate_age(raw_age)` functions that each raise their specific
exception when a rule is broken. A menu loop collects a full signup
attempt (username, password, age) and reports every rule that failed,
not just the first one, by trying each validator inside its own
`try`/`except` instead of stopping at the first failure.

**Suggested approach:** Reuse this project's pattern of a custom
exception's `__init__` building a clear message via
`super().__init__(...)` while also storing the bad value as an
attribute. A `run_all_validators(username, password, raw_age)` function
that calls each validator in its own `try`/`except Exception as e` and
collects `str(e)` into a list of problems (instead of letting the
first exception stop the whole check) is the core engine.

### 2. Inventory Stock Manager

**Problem:** Any store or warehouse system -- physical retail,
e-commerce, a small business's back office -- needs to refuse selling
more of an item than is in stock, and refuse an obviously broken order
(a negative or zero quantity), without the whole system crashing over
one bad request.

**What it should do:** Track a running `{item_name: quantity}`
inventory dict. Define `OutOfStockError` (raised when a requested sale
quantity is more than what's on hand, carrying the item name and how
much was requested vs. available) and `InvalidQuantityError` (raised
for a zero/negative/non-numeric quantity). Menu options: add stock for
an item, sell/remove stock for an item (raising the custom exceptions
as needed), check current stock for an item, and list all items low on
stock (below some threshold).

**Suggested approach:** A `sell(inventory, item_name, quantity)`
function mirrors this project's `withdraw` almost exactly -- validate
the quantity first, then compare it against
`inventory.get(item_name, 0)` and raise `OutOfStockError` if it's too
much, otherwise subtract and return the new quantity.

### 3. Unit Conversion Tool

**Problem:** A cooking app converting cups to milliliters, a shipping
calculator converting pounds to kilograms, a science tool converting
Celsius to Kelvin -- all need to convert between compatible units, and
clearly reject a request to convert between two units that don't make
sense together (like trying to convert kilograms into liters).

**What it should do:** Support a handful of unit categories (length,
weight, temperature) each with a small set of convertible units.
Define `UnsupportedConversionError`, raised when a requested "from
unit" and "to unit" pair aren't in the same category (carrying both
unit names as attributes so the error message can name exactly which
pair failed). Menu options: pick a category, enter a value and the
from/to units, and see the converted result; trying an unsupported
pair should print a clear message and return to the menu instead of
crashing.

**Suggested approach:** A dict-of-dicts (or a dict keyed by
`(from_unit, to_unit)` tuples) mapping valid conversion pairs to a
conversion function is the core lookup; a
`convert(category, from_unit, to_unit, value)` function raises
`UnsupportedConversionError` the moment a requested pair isn't a key
in that lookup, before attempting any math.

### 4. Quiz Answer Grader

**Problem:** An online quiz tool, a classroom auto-grader, or a
trivia app all need to accept a learner's typed answer, grade it
against the correct answer, and gracefully reject malformed input (an
empty answer, or a numeric-answer question where the learner typed
letters) instead of crashing the whole quiz session over one bad
response.

**What it should do:** Store a list of question dicts (prompt, correct
answer, expected answer type -- text or number). Define
`MalformedAnswerError`, raised when a numeric question receives
non-numeric text, or any question receives a blank answer (carrying
the raw offending input as an attribute). A `grade_answer(question,
raw_answer)` function raises that exception for bad input, and
otherwise returns whether the answer was correct. Menu options: run
through the full quiz asking every question, show the running score,
and re-attempt any question that was answered with malformed input
instead of silently counting it wrong.

**Suggested approach:** For a numeric question, try converting
`raw_answer` with `float(raw_answer)` inside a `try`/`except
ValueError`, re-raising as `MalformedAnswerError` (`raise ... from e`)
-- the same re-raise pattern this project's `parse_amount` uses to
turn a built-in exception into the project's own custom one.
