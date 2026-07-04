# Chapter 6 Practice Bank: Strings Deep Dive

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses everything from
Chapters 1-5 plus this chapter's own toolkit: `len()`, indexing/slicing,
the string methods covered in the lesson, f-strings, and iterating a
string or a `.split()` result with a bare for-loop. No lists/dicts,
comprehensions, functions, or `try`/`except` yet.

## How to run

```bash
python3 starter.py
```

## Topic 1: Indexing & Slicing

1. Given `word = "Programming"`, print the first character with a positive index and the last character with a negative index.
2. Given `phrase = "Hello, World!"`, print its length with `len()`, then print the slice `phrase[7:12]`.
3. Given `code = "abcdefghij"`, print every other character using a slice with a step of 2.
4. Given `word = "Python"`, print it reversed using a slice with a step of -1.
5. **Debug the Code:** fix an `IndexError` caused by using `word[len(word)]` instead of `word[len(word) - 1]`.
6. **Scenario — Phone Number Parser:** pull the area code out of `"(555) 123-4567"` using slicing.
7. **Scenario — Interview Prep:** prove that slicing out of range never crashes, unlike indexing out of range.

## Topic 2: Common String Methods

1. Clean leading/trailing whitespace from `"   mpapasani   "` with `.strip()`.
2. Compare `.upper()`, `.lower()`, `.title()`, and `.capitalize()` on `"new york"`.
3. Remove dashes from `"555-123-4567"` with `.replace()`.
4. **Debug the Code:** fix a crash caused by `.index()` on a missing substring by switching to `.find()`.
5. Count occurrences of `"Hello"` in a sentence with `.count()`, then count total words with `.split()` + a for-loop.
6. **Scenario — Filename Validator:** check a filename's prefix/suffix with `.startswith()` / `.endswith()`.
7. **Scenario — Interview Prep:** show why login checks should compare `.lower()` versions of usernames.

## Topic 3: String Formatting with f-strings

1. Embed two variables in a sentence with an f-string.
2. Compute a value directly inside an f-string's `{}`.
3. Round a float to 2 decimal places using the `:.2f` format specifier.
4. **Debug the Code:** fix a missing `f` prefix that left `{temperature}` printing literally.
5. Build a simple aligned text "table" row using `:<10` and `:>5` padding.
6. **Scenario — Receipt Line:** format a receipt line with a computed, 2-decimal total.
7. **Scenario — Interview Prep:** compare old-style `+`/`str()` concatenation with the f-string equivalent.

## Topic 4: Immutability & String Identity

1. Explain why strings can't be changed in place, and rebuild one correctly with slicing.
2. Use `id()` to show two variables can point at the same string object, and that reassigning one gives it a new id.
3. Watch `id()` change on every iteration of a loop that builds a string with `+=`.
4. **Debug the Code:** fix a `TypeError` from trying to mutate a string via index assignment.
5. Compare `id()` and `is` for two identical string literals (interning).
6. **Scenario — Log Builder Anti-Pattern:** explain why repeated `+=` in a loop is a real performance problem at scale.
7. **Scenario — Interview Prep:** show that reassigning one variable doesn't affect another variable that shares its old value.

## Topic 5: Searching & Validating Strings

1. Check substring membership with `in` / `not in`.
2. Validate a numeric-looking string with `.isdigit()` before converting it with `int()`.
3. Check `.isalpha()` on strings with and without digits.
4. Check `.isupper()` and `.islower()`.
5. Detect a whitespace-only field with `.isspace()`.
6. **Scenario — PIN Validator:** combine `.isdigit()` and `len()` to validate a 4-digit PIN.
7. **Scenario — Interview Prep:** explain why `.isalnum()` rejects underscores, and build a custom check that allows them.

## Topic 6: Real-World Text Processing

1. Clean a messy form field by chaining `.strip()` and `.lower()`.
2. Tally vowels in a sentence with the accumulator pattern.
3. Parse a `"key: value"` log line using `.find()` and slicing.
4. **Debug the Code:** fix a case-sensitive email comparison that should have been case-insensitive.
5. Mask all but the last 4 characters of a card number for a receipt.
6. **Scenario — Log Line Splitter:** split a pipe-delimited log line and print each field.
7. **Scenario — Interview Prep:** show why `.count()` on a raw substring can overcount compared to counting whole words.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
