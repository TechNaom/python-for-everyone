# Chapter 4 Practice Bank: Control Flow (if / elif / else)

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses only what
Chapters 1-4 covered: `print()`, variables, `input()`, the conversion
functions, arithmetic/relational/logical/bitwise operators, `is`/`in`,
and `if` / `if-else` / `elif` chains / nested `if`. No loops,
functions, lists, dicts, or f-strings yet.

## How to run

```bash
python3 starter.py
```

## Topic 1: Simple if

1. Print a message only if `temperature` is above 32 — then show that a print() right after the if block always runs either way.
2. Use `in` to check whether `"@"` appears inside an email string.
3. Use the bitwise `&` operator to check whether a number is odd.
4. Use `is` (not `==`) to check whether a boolean variable is `True`.
5. Ask for a password with `input()` and print "Access granted." only if it matches.
6. **Scenario — Free Shipping Threshold:** print a free-shipping message if `cart_total` is 75 or more.
7. **Scenario — Interview Prep:** prove that code right after an `if` block always runs, even when the condition is `False`.

## Topic 2: if-else

1. Compare two prices and print which one is more expensive using if-else.
2. Use if-else and `and` (or a chained comparison) to validate a percentage is between 0 and 100.
3. Use if-else and `in` to check whether a letter is a vowel or a consonant.
4. Use if-else and bitwise `&` to print whether a number is odd or even.
5. Ask "Subscribe to our newsletter? (yes/no):" with `input()` and print a matching if-else response.
6. **Scenario — Age-Based Ticket Pricing:** print the child or adult ticket price based on `visitor_age`.
7. **Scenario — Login Permission Check (Interview Prep):** grant or deny access based on matching username *and* password.

## Topic 3: elif chains

1. Use an elif chain to turn a traffic light color ("red"/"yellow"/"green") into an action.
2. Use if/elif/else to classify a number as positive, negative, or zero.
3. **Debug the Code:** fix a classification bug caused by three separate `if` statements overwriting each other instead of using `elif`.
4. Use an elif chain to print "FizzBuzz" / "Fizz" / "Buzz" / the number itself for a single value `n` (check divisible-by-15 first).
5. Ask for a day number (1-7) with `input()` and use an elif chain to print the matching weekday name.
6. **Scenario — Discount Tier by Purchase Amount:** use an elif chain (highest threshold first) to print a Platinum/Gold/Silver/no-discount tier.
7. **Scenario — Interview Prep:** explain in a comment why an elif chain must check the highest threshold first.

## Topic 4: Nested if

1. Use a nested if (outer: positive check, inner: even/odd check) to classify a number.
2. Use a nested if (outer: username check, inner: password check) to simulate a login flow with three distinct outcomes.
3. Use a nested if (outer: passing score, inner: attendance) to decide pass / not-eligible / fail.
4. Use a nested if (outer: positive check, inner: magnitude check) to classify a number as large/small positive, or not positive.
5. Ask for age and (if 18+) whether the user has an ID, using nested `input()` calls, to decide entry.
6. **Scenario — Bank Withdrawal:** use a nested if (outer: sufficient funds, inner: valid amount) to process a withdrawal.
7. **Scenario — Interview Prep:** write the nested-if and single-`and`-condition versions of the same check side by side, and explain in a comment when nesting is genuinely required instead of just a style choice.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
