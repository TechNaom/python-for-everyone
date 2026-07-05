# Chapter 10 Practice Bank: Functions Deep Dive

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses everything from
Chapters 1-9 plus this chapter's own toolkit: `def`, parameters and
default arguments, `*args` and `**kwargs`, local/global scope with
`global`/`nonlocal`, recursion, closures, and decorators (hand-written,
no `functools`). No `try`/`except`, file I/O, classes, or imports.

## How to run

```bash
python3 starter.py
```

## Topic 1: Function Basics

1. Write `greet(name)`, a function that returns a greeting string.
2. Write `add(a, b)`, a function that returns the sum of two arguments.
3. Write `is_even(n)`, a function that returns `True`/`False`.
4. Write `describe_number(n)` using `if`/`elif`/`else` inside a function.
5. **Debug the Code:** fix a function that prints its result instead of returning it.
6. **Scenario — Order Total Calculator:** write `calculate_total(price, quantity)`.
7. **Scenario — Interview Prep:** explain the difference between a function that returns a value and one that only prints it.

## Topic 2: Default Arguments

1. Write `power(base, exponent=2)` with a default exponent.
2. Write `make_greeting(name, greeting="Hello")` with a default greeting.
3. Write `apply_discount(price, percent=10)` with a default discount percent.
4. Write `build_profile(name, age=18, city="Unknown")` and call it three different ways.
5. **Debug the Code:** fix a function using a mutable list as a default argument.
6. **Scenario — Configurable Report Header:** write `report_header(title, author="Unknown Author", year=2024)`.
7. **Scenario — Interview Prep:** explain why mutable default arguments are dangerous, and fix it with the `None`-default pattern.

## Topic 3: `*args` and `**kwargs`

1. Write `sum_all(*args)` to sum any number of positional arguments.
2. Write `join_words(*args)` to join any number of words with spaces.
3. Write `print_profile(**kwargs)` to print each keyword argument.
4. Write `build_settings(*args, **kwargs)` returning both collected together.
5. **Debug the Code:** fix a function that tries to divide a tuple (`args`) directly instead of summing it first.
6. **Scenario — Flexible Logger:** write `log_event(event_name, **details)`.
7. **Scenario — Interview Prep:** explain the difference between `*args` and `**kwargs`.

## Topic 4: Scope (local/global, `global`/`nonlocal`)

1. Demonstrate a local variable shadowing a global one without modifying the global.
2. Use `global` to modify a module-level variable from inside a function.
3. Use `nonlocal` inside a nested function to modify an enclosing function's variable.
4. Demonstrate that a function parameter is just a local variable, even when it shares a name with a global.
5. **Debug the Code:** fix an `UnboundLocalError` caused by a missing `global` declaration.
6. **Scenario — Shared Application Counter:** track `active_users` across login/logout functions with `global`.
7. **Scenario — Interview Prep:** explain the difference between `global` and `nonlocal`.

## Topic 5: Recursion

1. Write a recursive `factorial(n)`.
2. Write a recursive `fibonacci(n)`.
3. Write a recursive `sum_digits(n)`.
4. Write a recursive `count_down(n)` with a "Liftoff!" base case.
5. **Debug the Code:** fix a recursive factorial function that's missing its base case entirely.
6. **Scenario — Counting Items in Nested Categories:** recursively total numbers inside a nested list.
7. **Scenario — Interview Prep:** explain what a base case is and why every recursive function needs one.

## Topic 6: Closures

1. Write `make_multiplier(factor)` returning a closure that multiplies by `factor`.
2. Write `make_greeter(greeting)` and show two closures remembering different greetings.
3. Write `make_counter()` and show two independent counters tracking separate state.
4. Write `make_running_total()` and call the returned closure repeatedly.
5. **Debug the Code:** fix a closure that reassigns a local list instead of appending to the enclosing one.
6. **Scenario — Per-User Rate Limiter Counter:** build a closure-based request counter that blocks past a limit.
7. **Scenario — Interview Prep:** explain what a closure is using `make_adder(n)`.

## Topic 7: Decorators

1. Write a decorator `shout` that uppercases a function's string result.
2. Write a decorator `call_counter` that tracks how many times a function has been called.
3. Write a decorator `double_result` that doubles a function's numeric result.
4. Write a decorator `log_call` that prints the arguments before calling the function.
5. **Debug the Code:** fix a decorator's wrapper that forgot to `return` the inner function's result.
6. **Scenario — Timing-Style Instrumentation Without a Timer:** build `track_calls`, a decorator that logs a running call count.
7. **Scenario — Interview Prep:** explain what a decorator does under the hood using `ensure_positive`.

## Topic 8: Bringing It Together — Real-World Functions in Production

1. Write `validate_and_format_price(price)`, a small validation helper.
2. Write `retry_with_default(values, index, default=None)`, a defensive list-lookup pattern.
3. Write `build_api_response(status, **data)`, modeling a flexible API response wrapper.
4. Write a decorator `retry_once` that retries a function call once if it returns `None`.
5. **Debug the Code:** fix a recursive discount function that never decrements its `rounds` argument.
6. **Scenario — Production-Style Input Sanitizer Pipeline:** write `sanitize_signup_data(name, email, age=None, **extra)`.
7. **Scenario — Interview Prep:** combine a closure-based running-average tracker with a logging decorator.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
