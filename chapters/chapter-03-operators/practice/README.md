# Chapter 3 Practice Bank: Operators

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses only what
Chapters 1-3 covered: `print()`, variables, basic types, `input()`,
`type()`/`id()`, the conversion functions, and this chapter's
arithmetic/assignment, relational/logical, bitwise, and `is`/`in`
operators. No `if`/loops/functions/lists yet — conditions are just
printed, not used to branch.

## How to run

```bash
python3 starter.py
```

## Topic 1: Arithmetic & assignment

1. Given `a = 17` and `b = 5`, print the result of all seven arithmetic operators (`+ - * / // % **`).
2. Start with `score = 50` and apply `+= 10`, `-= 5`, `*= 2`, `//= 3`, `%= 7`, `**= 2` in turn, printing after each.
3. Convert `celsius = 25` to Fahrenheit using `celsius * 9 / 5 + 32`.
4. **Debug the Code:** fix a precedence bug where `-number ** 2` computes `-(number ** 2)` instead of `(-number) ** 2`.
5. Given `length = 8` and `width = 3`, compute and print area and perimeter.
6. **Scenario — Grocery Bill Split:** split a bill of 1875 cents among 4 friends using `//` and `%`.
7. **Scenario — Interview Prep:** prove that `/` always returns a float, even when the division is exact.

## Topic 2: Relational & logical

1. Given `x = 8` and `y = 3`, print the result of all six relational operators (`== != < > <= >=`).
2. Given `age = 25`, print a single `and` expression checking it's between 18 and 65 inclusive.
3. Given `temperature = 95`, print a single `or` expression checking too hot or too cold.
4. Given `is_raining = False`, print `not is_raining`.
5. Given `credit_score = 720` and `has_income = True`, print a combined `and` eligibility check.
6. **Scenario — Login Gatekeeper:** print whether login is allowed based on `is_active_account and correct_password`.
7. **Scenario — Interview Prep:** prove short-circuit evaluation with `x != 0 and 10 / x > 1` when `x = 0`, without crashing.

## Topic 3: Bitwise

1. Given `a = 5` and `b = 6`, print `a & b`, `a | b`, `a ^ b`.
2. Print `a << 1` and `a >> 1`.
3. Print `~a` and explain in a comment what bitwise NOT does.
4. Given `read = 4`, `write = 2`, `execute = 1`, combine `read` and `write` with `|`.
5. Check whether the write flag is set in `permissions` using `&`.
6. **Scenario — Unix File Permissions:** combine `read`, `write`, and `execute` into one `full_permissions` value with `|`.
7. **Scenario — Interview Prep:** explain why bit flags use powers of 2, and prove it by combining and checking flags with `|`/`&`.

## Topic 4: Special: `is` / `in`

1. Given `a = 10` and `b = 10`, compare `a is b` and `a == b`.
2. Given `name = "Ada"` and `name_alias = name`, print `name is name_alias`.
3. Given `word = "python"`, check whether `"th"` is inside it with `in`.
4. Check whether `"z"` is NOT inside `word` with `not in`.
5. Given `pin = "4821"` and `digit = "8"`, check membership with `in`.
6. **Scenario — Access Code Validator:** check whether an entered hex character is inside `"ABCDEF0123456789"`.
7. **Scenario — Interview Prep:** compare `x == y` and `x is y` for `x = 300` and `y = 300`, and explain why `is` isn't safe here (Python only guarantees small-integer caching, roughly -5 to 256).

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
