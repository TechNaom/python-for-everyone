# Chapter 11 Practice Bank: Modules & Packages

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses everything from
Chapters 1-10 plus this chapter's own toolkit: `import x`,
`from x import y`, `import x as y`, `from x import y as z`, and the
`math`, `random`, and `datetime` modules. No `try`/`except`, file I/O,
classes, or any import beyond `math`/`datetime`/`random`.

Note: any problem involving `datetime.date.today()` or `random` has
output that's different every time you run it (that's the whole point
of "random") — the solution checks a *property* of the result (like
"is this in range" or "does the set of elements still match") instead
of one exact value, so don't worry if your printed numbers don't match
someone else's.

## How to run

```bash
python3 starter.py
```

## Topic 1: What Is a Module?

1. Write `pi_times_two()`, returning `math.pi * 2`.
2. Write `describe_module(name, purpose)`, returning a formatted sentence.
3. Compare a hand-typed `3.14159` against `math.pi`.
4. Write `circle_circumference(radius)` using `math.pi`.
5. **Debug the Code:** fix a function that's missing its `import math` statement entirely.
6. **Scenario — Why Real Projects Use Modules:** explain what a module is and why `math`/`random`/`datetime` are modules.
7. **Scenario — Interview Prep:** explain why `math.pi` beats a hand-typed constant.

## Topic 2: Import Variations

1. Use the plain `import math` to write `sqrt_via_plain_import(n)`.
2. Add `from math import sqrt` and write `sqrt_via_from_import(n)`.
3. Add `import math as m` and write `pi_via_aliased_import()`.
4. Add `from random import randint as ri` and write a dice roller.
5. **Debug the Code:** fix a function calling a nonexistent `math.round()` instead of `math.ceil()`.
6. **Scenario — Picking the Right Import Style:** explain when to use each import style.
7. **Scenario — Interview Prep:** explain the difference between `import x` and `from x import y`.

## Topic 3: The `math` Module

1. Write `hypotenuse(a, b)` using `math.sqrt`.
2. Write `round_down_and_up(n)` using `math.floor` and `math.ceil`.
3. Write `power_of(base, exponent)` using `math.pow`.
4. Write `circle_area(radius)` using `math.pi`.
5. **Debug the Code:** fix a container-count function using `math.floor` instead of `math.ceil`.
6. **Scenario — Shipping Box Calculator:** write `boxes_required(num_items, items_per_box)`.
7. **Scenario — Interview Prep:** explain the difference between `math.floor`, `math.ceil`, and `round()`.

## Topic 4: The `datetime` Module

1. Write `make_date(year, month, day)` using `datetime.date`.
2. Write `format_date_long(a_date)` using `.strftime("%B %d, %Y")`.
3. Write `days_between(date_a, date_b)` using date subtraction.
4. Write `days_since_today()` using `datetime.date.today()`.
5. **Debug the Code:** fix a deadline countdown that subtracts in the wrong order.
6. **Scenario — Subscription Renewal Countdown:** write `days_until_renewal(signup_date, renewal_days=365)`.
7. **Scenario — Interview Prep:** explain how date subtraction produces a `timedelta`.

## Topic 5: The `random` Module

1. Write `roll_die()` using `random.randint(1, 6)`.
2. Write `pick_random_name(names)` using `random.choice`.
3. Write `shuffled_copy(items)` using `random.shuffle` on a copy.
4. Write `random_percentage()` using `random.randint(0, 100)`.
5. **Debug the Code:** fix a card picker calling `random.choice()` with no arguments.
6. **Scenario — Randomized A/B Test Assignment:** write `assign_ab_group()`.
7. **Scenario — Interview Prep:** explain why random code needs property-based checks instead of exact-value assertions.

## Topic 6: Bringing It Together — Modules in Production

1. Write `generate_order_id(order_number)` combining `datetime` and string formatting.
2. Write `distance_between_points(x1, y1, x2, y2)` using `math.sqrt`.
3. Write `pick_daily_special(menu_items)` using `random.choice`.
4. Write `subscription_status(start_date, length_days=30)` using `datetime`.
5. **Debug the Code:** fix a discount function that adds instead of subtracts.
6. **Scenario — Production Order Confirmation Builder:** combine `math`, `datetime`, and dicts into one function.
7. **Scenario — Interview Prep:** explain how `math`/`random`/`datetime` show up in real production code.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks. Remember that any random or "today's date"
output will legitimately differ each time you run it.
