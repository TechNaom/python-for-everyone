# Chapter 6 Project: Password Strength & Policy Auditor

A menu-driven mini-app that scores a password against five common
policy rules and tracks stats for the whole session &mdash; a genuinely
useful, portfolio-worthy tool built entirely out of string methods,
iteration, and the accumulator pattern from Chapter 5.

## What you'll build

A script with a `while True` menu loop offering three options:

1. Check a password
2. View session stats
3. Quit

Checking a password evaluates five rules using nothing but string
methods and a `for` loop over its characters (no `re` module):

- At least 8 characters long
- Contains an uppercase letter
- Contains a lowercase letter
- Contains a digit
- Contains a special character (from `!@#$%^&*()-_=+`)

Each rule is worth one point (score out of 5), mapped to a rating:

| Score | Rating |
|-------|--------|
| 0-2   | Weak   |
| 3-4   | Medium |
| 5     | Strong |

The tool also prints specific feedback on exactly which rules were
missed, not just the score &mdash; e.g. "Add a digit" or "Add a special
character."

Session stats (option 2) use the accumulator pattern: a running count
of how many passwords were checked, and how many were rated Strong.

Example run:

```
=== Password Strength & Policy Auditor ===

1. Check a password
2. View session stats
3. Quit
Choose an option (1-3): 1
Enter a password to check: abc

--- Result for 'abc' ---
Score: 1/5  ->  Rating: Weak
Checklist:
  [ ] At least 8 characters long
  [ ] Contains an uppercase letter
  [x] Contains a lowercase letter
  [ ] Contains a digit
  [ ] Contains a special character (!@#$%^&*()-_=+)
Suggestions:
  - Make it at least 8 characters long
  - Add an uppercase letter
  - Add a digit
  - Add a special character, e.g. one of !@#$%^&*()-_=+

1. Check a password
2. View session stats
3. Quit
Choose an option (1-3): 2

--- Session Stats ---
Passwords checked: 1
Strong passwords: 0
Strong rate: 0.0%

1. Check a password
2. View session stats
3. Quit
Choose an option (1-3): 3

Session summary: checked 1 password(s), 0 rated Strong.
Goodbye!
```

## How to run it

```bash
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Add a rule that rejects passwords containing the word "password"
  (case-insensitive) &mdash; use `.lower()` and the `in` operator.
- Track the single strongest password's score this session.
- Print a percentage breakdown of how many checks landed in each of
  Weak / Medium / Strong.

## Why this project matters

Password policy checks like this run in real signup forms, admin
panels, and security tooling every day. The logic here is small on
purpose &mdash; a single pass over each character, a handful of booleans,
an accumulator for stats &mdash; but it's the same shape as production
validation code: clear rules, specific feedback, and a running record
of what happened.
