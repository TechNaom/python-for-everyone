# Chapter 10 Project: Tip & Bill-Split Calculator Library

A small, genuine library of well-designed, reusable functions for
splitting bills, calculating tips, applying discounts, and adding fees
&mdash; wired up to a simple menu-driven CLI on top. This is the first
project in the course actually **built around functions** as its
organizing principle: every calculation lives in a standalone, named
function with clear inputs and a clear return value, and the
`while True` menu loop at the bottom does nothing but call into that
library and print results. That's the whole point of this chapter --
earlier projects crammed their logic straight into the menu loop's
`if`/`elif` branches; this one doesn't.

## What you'll build

A function library covering this chapter's core tools --
**`def`, default arguments, `*args`/`**kwargs`** -- plus a menu loop
offering six options:

1. Calculate a tip only
2. Apply a discount to a bill
3. Split a bill across people
4. Build a full receipt (discount + tip + fees + split)
5. Show session history
6. Quit

The library itself is six small functions:

- `calculate_tip(bill_amount, tip_percent=15)` -- a **default argument**
  means most tips can be calculated with just a bill amount, while still
  allowing a custom percentage.
- `apply_discount(bill_amount, discount_percent=0)` -- defaults to no
  discount at all, so it's safe to call even when there isn't one.
- `apply_surcharges(bill_amount, *surcharges)` -- **`*args`** lets the
  caller tack on any number of flat fees (delivery, service, ...)
  without this function needing to know in advance how many there'll be.
- `split_bill(total, num_people=1)` -- defaults to "no split" (one
  person), and guards against splitting across zero or a negative
  number of people.
- `summarize_fees(**fees)` -- **`**kwargs`** totals up any number of
  *named* fees (`delivery_fee=5, service_fee=2`) without a fixed
  parameter for every possible fee name.
- `build_receipt(bill_amount, tip_percent=15, discount_percent=0, num_people=1, **extra_fees)`
  -- the "bring it all together" function. It doesn't duplicate any
  math itself; it just calls the five functions above in the right
  order and assembles their results into one receipt dict. This is
  function composition in action: small, single-purpose functions,
  reused instead of retyped.

Two small helpers, `read_float(prompt, default)` and
`read_int(prompt, default)`, handle "press Enter to accept the
default" input parsing so the menu loop's `input()` calls stay short.

Every receipt built during the session is appended to a running
`receipts` list, so option 5 can show session history -- the same
running-state pattern earlier chapters' projects have used, just now
built on top of function calls instead of inline logic.

Example run:

```
=== Tip & Bill-Split Calculator Library ===

1. Calculate a tip only
2. Apply a discount to a bill
3. Split a bill across people
4. Build a full receipt (discount + tip + fees + split)
5. Show session history
6. Quit
Choose an option (1-6): 4
Bill amount: $100
Discount percent (blank = 0): 10
Tip percent (blank = 15): 18
Number of people (blank = 1): 2
Add extra fees? (y/n): y
How many fees to add? 2
  Fee #1 name (e.g. delivery_fee): delivery fee
  Fee #1 amount: $5
  Fee #2 name (e.g. delivery_fee): service fee
  Fee #2 amount: $2.5

--- Receipt ---
Original bill:        $100.00
Discount:             10.0% -> $90.00
Tip (18.0%):          $16.20
Delivery Fee:         $5.00
Service Fee:          $2.50
Grand total:          $113.70
Per person (2):       $56.85

1. Calculate a tip only
2. Apply a discount to a bill
3. Split a bill across people
4. Build a full receipt (discount + tip + fees + split)
5. Show session history
6. Quit
Choose an option (1-6): 5

--- Session History (1 receipt(s)) ---
1. Bill $100.00 -> Grand total $113.70

1. Calculate a tip only
2. Apply a discount to a bill
3. Split a bill across people
4. Build a full receipt (discount + tip + fees + split)
5. Show session history
6. Quit
Choose an option (1-6): 6

Session summary: 1 receipt(s) built.
Goodbye!
```

## How to run it

```bash
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Add a "recalculate last receipt with a different tip" option that
  rebuilds the most recent entry in `receipts` using a new tip
  percentage, reusing `build_receipt(...)` rather than writing new math.
- Write a `round_up_to_nearest(amount, nearest=1)` function and use it
  to offer a "round the grand total up" option on a receipt.
- Add a `best_tip_for_budget(bill_amount, max_total)` function that
  works backward from a maximum total the customer can spend to figure
  out the highest tip percentage they can afford.

## Why this project matters

Splitting a bill and calculating a tip sounds trivial, but the real
skill this project practices is **function design**: deciding what
belongs in its own small function, what a good default argument is,
and when `*args`/`**kwargs` genuinely simplify a call versus just
adding noise. That's precisely the skill behind any real-world
calculation library -- a payments system's fee calculator, a payroll
system's tax-and-deduction functions, an e-commerce checkout's
discount-and-shipping pipeline -- all of them are built the same way
this project is: small functions with clear responsibilities, composed
together by one function that calls them in the right order.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Tip & Bill-Split Calculator Library above is fully built out with a
starter and reference solution &mdash; the four ideas below are not.
Each is a real, grounded use case solvable with only what's been taught
through Chapter 10 (everything through comprehensions and lambda, plus
`def`, parameters/defaults, `*args`/`**kwargs`, scope, recursion,
closures, and decorators). No starter or solution files are provided on
purpose &mdash; building one of these unassisted, menu loop and all, is
the point.

### 1. Unit-Conversion Function Library

**Problem:** Recipes, shipping labels, fitness apps, and engineering
tools constantly need to convert between units -- and a reliable
conversion library is the backbone of every one of them.

**What it should do:** Build small functions like
`celsius_to_fahrenheit(c)`, `miles_to_km(miles)`,
`pounds_to_kg(pounds)`, and a general-purpose
`convert(value, from_unit, to_unit)` that dispatches to the right
specific function based on the unit names passed in. Menu options:
convert temperature, convert distance, convert weight, and show a
conversion history of everything converted this session.

**Suggested approach:** Write each specific conversion as its own
one-line function with a clear name and a docstring, then have
`convert(...)` use `if`/`elif` to call the right one -- this keeps each
individual formula isolated and testable on its own, exactly like this
chapter's `calculate_tip`/`apply_discount` split. Store each conversion
performed as a dict in a running list for the history option.

### 2. Text-Statistics Toolkit

**Problem:** Writers, editors, and content platforms need quick
readability stats -- word count, sentence count, average word length --
computed consistently every time.

**What it should do:** Build functions like `count_words(text)`,
`count_sentences(text)`, `count_characters(text, include_spaces=True)`,
and `average_word_length(text)`. Menu options: paste in a block of text,
run the full toolkit on it and print every stat, and compare two texts
side by side using the same functions on both.

**Suggested approach:** `count_sentences` can use a simple approach
like counting `.`, `!`, and `?` characters with `.count(...)`; keep
`include_spaces=True` as a default argument on `count_characters` so
most calls don't need to think about it. Build a `build_report(text)`
function that composes all four smaller functions into one summary
dict, the same "bring it all together" pattern `build_receipt` uses
here.

### 3. Grade & GPA Calculator Library

**Problem:** Students and teachers alike need a reliable way to turn a
list of scores or letter grades into a final weighted grade or GPA --
by hand, this is error-prone and inconsistent.

**What it should do:** Build functions like
`weighted_average(*scores, weights=None)`,
`percent_to_letter_grade(percent)`, and `gpa_from_letters(*letters)`.
Menu options: enter scores and weights for one class and get the
weighted average, convert a percent to a letter grade, and compute a
GPA across several classes' letter grades.

**Suggested approach:** `weighted_average` is a great real use case for
`*args` (any number of scores) alongside a `weights` parameter that
defaults to `None`, meaning "treat every score equally" when no weights
are given -- inside the function, build an equal-weights list yourself
if `weights is None`. `percent_to_letter_grade` is a clean `if`/`elif`
chain returning a single-character string.

### 4. Password-Strength-Scoring Function Library

**Problem:** Signup forms need to score password strength in real
time and explain *why* a password is weak -- reusing the string-check
ideas from Chapter 6/3 but now organized as a real function library
instead of one big block of `if` statements.

**What it should do:** Build functions like `has_uppercase(password)`,
`has_digit(password)`, `has_symbol(password)`,
`score_password(password)` (returns a 0-4 strength score based on which
checks pass), and `strength_label(score)` (turns that score into
"Weak"/"Fair"/"Strong"). Menu options: score a single password and
show which checks it passed/failed, and batch-score a list of sample
passwords showing each one's label.

**Suggested approach:** Each `has_*` check is a one-line function
returning `True`/`False`; `score_password` calls all of them and counts
how many returned `True`, exactly the same "small functions composed by
one bigger function" shape as `build_receipt` in this chapter's main
project. Keep the individual checks reusable on their own, since a
real signup form often needs to show which specific rule failed, not
just a final score.
