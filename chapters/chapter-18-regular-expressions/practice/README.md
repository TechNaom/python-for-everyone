# Chapter 18 Practice Bank: Regular Expressions

A deeper set of practice problems, organized by topic, on top of the main
`exercises/` folder — including scenario-based problems written in the
same style you'll see in real interviews. This is the chapter where the
`re` module's pattern matching (`match()`/`search()`/`fullmatch()`,
`findall()`/`finditer()`, character classes, quantifiers, anchors, groups
& named groups, `re.sub()`/`re.split()`, `re.compile()`, greedy/non-greedy
quantifiers, raw strings, and flags) becomes allowed, on top of everything
from Chapters 1-17 (including generators, iterators, context managers,
all OOP, exceptions, and file/CSV handling). No import beyond
`re`/`math`/`datetime`/`random`/`csv`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: `match()` / `search()` / `fullmatch()`

1. Use `re.match()` to find digits at the start of a string.
2. Use `re.search()` to find digits anywhere in a string.
3. Compare `re.fullmatch()` succeeding vs. failing on two different strings.
4. Loop over words checking whether each one starts with a given prefix.
5. **Debug the Code:** fix a call using `re.match()` where `re.search()` was actually needed.
6. **Scenario — Validating a Username Field on a Signup Form:** write `is_valid_username()` using `re.fullmatch()`.
7. **Scenario — Interview Prep:** explain the actual difference between `re.match()` and `re.search()`.

## Topic 2: `findall()` & `finditer()`

1. Use `re.findall()` to extract every dollar amount from text.
2. Use `re.finditer()` to get each match's text and position.
3. Count every word in a string using `findall()`.
4. Extract every hashtag from a string of social-media-style text.
5. **Debug the Code:** fix a pattern missing a `+` quantifier, splitting multi-digit numbers into single digits.
6. **Scenario — Extracting Every Error Code From a Support Ticket:** write `extract_error_codes()`.
7. **Scenario — Interview Prep:** explain when to reach for `findall()` vs. `finditer()`.

## Topic 3: Character Classes, Quantifiers & Anchors

1. Count every vowel in a string using a character class.
2. Match two spellings of a word using an optional `?` quantifier.
3. Match a specific letter+digit code pattern using `{n}` quantifiers.
4. Validate strings against a `{m,n}`-quantified, anchored pattern.
5. **Debug the Code:** fix an unescaped literal decimal point.
6. **Scenario — Validating a Simple Password Policy:** write `is_strong_password()`.
7. **Scenario — Interview Prep:** explain how quantifiers and anchors work together in validation.

## Topic 4: Groups & Named Groups

1. Extract two numbered groups from an email-shaped pattern.
2. Extract the same pieces using named groups instead.
3. Use `.groups()` to get every numbered group as a tuple.
4. Loop over multiple matches, printing each one's `.groupdict()`.
5. **Debug the Code:** fix a named group missing the required `P` in `(?P<name>...)`.
6. **Scenario — Parsing a "Last, First" Name Field:** write `split_last_first()`.
7. **Scenario — Interview Prep:** explain what problem groups actually solve.

## Topic 5: `re.sub()` & `re.split()`

1. Mask a credit card number with `re.sub()`.
2. Strip punctuation/symbols out of text with `re.sub()`.
3. Split text on a semicolon with optional surrounding whitespace.
4. Collapse repeated dashes down to a single dash.
5. **Debug the Code:** fix `re.sub()` arguments given in the wrong order.
6. **Scenario — Redacting Social Security Numbers From a Document:** write `redact_ssns()`.
7. **Scenario — Interview Prep:** explain why `re.sub()`/`re.split()` beat plain string methods here.

## Topic 6: Compiled Patterns

1. Build a compiled digit pattern and call `.findall()` on it.
2. Build a compiled email pattern and scan multiple lines with it.
3. Build a compiled "5+ letter word" pattern.
4. Build a compiled IP-address-shaped pattern and scan multiple lines.
5. **Debug the Code:** fix code that compiled a pattern but never used the compiled object.
6. **Scenario — Scanning Many Log Lines for the Same Error Pattern:** write `count_error_lines()`.
7. **Scenario — Interview Prep:** explain when compiling a pattern is actually worth it.

## Topic 7: Bringing It Together — Greedy Matching, Raw Strings & Flags

1. Compare a greedy `.*` match against a non-greedy `.*?` match on the same text.
2. Confirm a raw-string pattern behaves as expected.
3. Use `re.IGNORECASE` to match regardless of capitalization.
4. Use `re.MULTILINE` so `^` anchors to each line instead of the whole string.
5. **Debug the Code:** fix a greedy `.*` that swallowed two separate quoted phrases into one match.
6. **Scenario — A Log-Scanning Tool Combining Everything:** write `scan_log_for_errors()` using a compiled pattern, named groups, and a flag together.
7. **Scenario — Interview Prep:** name the most common regex mistakes beginners make.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
