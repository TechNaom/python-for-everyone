# Chapter 2 Practice Bank: Variables & Data Types

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder -- including scenario-based problems written
in the same style you'll see in real interviews. Uses only what
Chapters 1-2 covered: `print()`, variables, `input()`, string
concatenation with `+` and `str()`, valid/invalid identifier naming,
dynamic typing, `type()`, `id()`, and the conversion functions
`int()`, `float()`, `str()`, `bool()`, `complex()`.

## How to run

```bash
python3 starter.py
```

## Topic 1: Naming variables properly

1. Create three properly named (snake_case) variables for a person's first name, last name, and age, and print each.
2. Rename a badly chosen variable (`x` for a shopping cart total) to something descriptive.
3. Create `total`, `Total`, and `TOTAL` with different values and print all three to prove they're separate variables.
4. Create a variable name that starts with an underscore, assign it a value, and print it.
5. Rewrite three badly chosen identifiers (`2nd_place`, `user name`, `api-key`) as valid snake_case variables.
6. **Scenario -- Config Keys:** name three config variables (max retry count, API timeout, debug mode flag) with proper snake_case.
7. **Scenario -- Interview Prep:** explain why `total`, `Total`, and `TOTAL` can coexist as separate variables.

## Topic 2: Python decides the type for you

1. Create a `str`, `int`, `float`, and `bool` variable and print all four in one `print()` call.
2. Create `signal = 10`, print it, reassign to the string `"ten"`, print again.
3. Create `ready = True`, print it, reassign to the string `"yes"`, print again.
4. Create a complex number variable and print it directly.
5. Create a float variable, print it, reassign it to an int, print again.
6. **Scenario -- Feature Flag:** reassign a boolean feature flag to a string to simulate a config reload, and explain why this is legal in Python but not in a statically typed language.
7. **Scenario -- Debug the Code (Interview Prep):** fix a `TypeError` caused by joining a cart item count directly with a string.

## Topic 3: type() and id()

1. Create a float variable and print its type.
2. Create two variables holding the same small int and print both `id()` values.
3. Create a string variable and print both its type and its id.
4. Create two variables holding the same larger int (`500`) and compare their ids, noting what the lesson said about small-integer caching.
5. Create a boolean variable, print its type, reassign it to an int, and print its type again.
6. **Scenario -- QA Type Check:** prove a config value is really an `int` before it's used in a billing system.
7. **Scenario -- Interview Prep:** explain why `id(x)` and `id(y)` match when `x = 5` and `y = 5`.

## Topic 4: Converting between types

1. Ask for the user's age with `input()`, convert it to an `int`, and print the value and its type.
2. Convert a string like `"3.14"` to a `float` and print it.
3. Convert an `int` to a `str` and print the value and its type.
4. Convert `0` and `1` to `bool` and compare how they print.
5. **Debug the Code:** fix a `ValueError` caused by calling `int()` on non-numeral text (`"three"`).
6. **Scenario -- Signup Form:** convert a typed-in age to an `int` and print the user's age next year.
7. **Scenario -- Interview Prep:** explain why `bool("False")` returns `True`.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match -- the goal is that your program runs without errors and
does what each TODO asks. Note: `id()` values will differ every time
you run the program (and between different machines), so don't expect
your exact numbers to match the ones in `solution.py`.
