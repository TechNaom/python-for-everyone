# Chapter 18 Exercises: Regular Expressions

These exercises use what Chapter 18 covered: `re.match()`/`re.search()`/
`re.fullmatch()`, `re.findall()`/`re.finditer()`, character classes,
quantifiers, anchors, groups & named groups, `re.sub()`/`re.split()`,
`re.compile()`, non-greedy quantifiers, raw strings, and regex flags.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — `re.search()` and `.group()`

Find `# TODO 1`. Use `re.search()` with the pattern `r"\d+"` to find the
first run of digits in the string `"Order #4471 shipped"`. Print the
`Match` object, then print `match.group()` to see just the matched text.

## Task 2 — `re.findall()` with a character class + quantifier

Find `# TODO 2`. Use `re.findall()` with the pattern `r"[A-Z][a-z]+"` to
find every capitalized word in the string `"Alice and Bob went to Paris"`.
Store the result in a variable named `names` and print it.

## Task 3 — Named groups

Find `# TODO 3`. Use `re.match()` with the pattern
`r"(?P<area>\d{3})-(?P<number>\d{4})"` on the string
`"555-1234 is the number"`. Print `match.group("area")` and
`match.group("number")`, then print `match.groupdict()`.

## Task 4 — `re.sub()`

Find `# TODO 4`. Use `re.sub()` with the pattern `r"\s+"` to replace every
run of one or more whitespace characters in `"too    many     spaces"`
with a single space `" "`. Store the result in `cleaned` and print it.

## Task 5 — `re.compile()`

Find `# TODO 5`. Use `re.compile()` to build a compiled pattern from
`r"^\d{5}$"` (a valid 5-digit ZIP code, start to end). Then loop over the
list `["90210", "1002", "733210", "60614"]`, and for each one, use the
compiled pattern's `.fullmatch()` method to print whether it's a valid ZIP
code (print `f"{zip_code}: valid"` or `f"{zip_code}: invalid"`).

## Task 6 — Non-greedy matching

Find `# TODO 6`. Use `re.findall()` with a non-greedy pattern
`r"\(.*?\)"` to find every parenthesized note in the string
`"Total (before tax) is $40 (approx.) for two items"`. Print the result —
it should find both `"(before tax)"` and `"(approx.)"` as two separate
matches, not one giant match spanning both.

## Task 7 — Debug the Code

Find `# TODO 7`. This pattern is supposed to match a literal price like
`"$19.99"`, but it forgot to escape the dot, so `"$19x99"` (with an `x`
instead of a period) matches too, which is wrong — an unescaped `.` means
"any character," not a literal period. Find and fix it.

## Task 8 — Debug the Code

Find `# TODO 8`. This pattern is meant to match the standalone word `"cat"`
using a word-boundary anchor, but the pattern string was written without
the `r` prefix, so Python's own string-escaping rules silently turn `\b`
into a backspace character instead of the word-boundary anchor — meaning
it never matches anything at all. Find and fix it.

## Checking your work

Compare your output against `solution.py`. Every example here uses fixed,
explicit values, so your output should match `solution.py` exactly.
