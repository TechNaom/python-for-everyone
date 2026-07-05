# Chapter 8 Practice Bank: Dictionaries & Sets

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses everything from
Chapters 1-7 plus this chapter's own toolkit: dictionary literals,
indexing/`KeyError`, `.get()` with a default, `in` for key existence,
dict methods (`.update()`, `.pop()`, `.setdefault()`, `.keys()`/
`.values()`/`.items()`, `del`), looping over dictionaries, sets
(creation, `.add()`/`.remove()`, union/intersection/difference), and
nested dictionaries. No comprehensions, `lambda`, functions (`def`),
`try`/`except`, file I/O, classes, or imports yet.

## How to run

```bash
python3 starter.py
```

## Topic 1: Creating Dictionaries & Accessing Values

1. Given `student = {"name": "Asha", "age": 21, "major": "CS"}`, print the dict and access two values with square brackets.
2. Given `prices = {"apple": 1.50, "banana": 0.75}`, explain why `prices["mango"]` raises a `KeyError`.
3. Use `.get("mango", 0)` and `.get("apple", 0)` on `prices` to look up safely.
4. Given `inventory = {"pens": 40, "notebooks": 15}`, check key existence with `in`.
5. **Debug the Code:** fix a `KeyError` from indexing a missing key by using `.get()` with a default instead.
6. **Scenario — Employee Lookup:** print an employee's name/department, and safely look up a missing "manager" field.
7. **Scenario — Interview Prep:** explain why `.get()` is safer than square-bracket indexing for optional fields.

## Topic 2: Dict Methods That Add, Update & Remove

1. Use `.update()` to change an existing key and add a new one in one call.
2. Use `.pop()` to remove a key and capture its value.
3. Use `.setdefault()` on a missing key and on an existing key, and see the difference.
4. **Debug the Code:** fix a `KeyError` from `.pop()` on a missing key by passing a default.
5. Print `.keys()`, `.values()`, `.items()` (as lists), then remove a key with `del`.
6. **Scenario — Shopping Cart Update:** use `.update()` and `.pop()` together to edit a cart.
7. **Scenario — Interview Prep:** explain the difference between `.get()` and `.setdefault()`.

## Topic 3: Looping Over Dictionaries

1. Loop over a dict directly (`for name in ages`) to see it visits keys.
2. Loop with `.items()` and tuple unpacking to get key and value together.
3. Add keys one at a time and loop over the dict to confirm insertion order is preserved.
4. **Debug the Code:** fix a loop that treats plain dict iteration as if it were `.items()` pairs.
5. Loop over `.items()` with an accumulator to total up dictionary values.
6. **Scenario — Attendance Sheet:** print each person's status and count how many are "Present".
7. **Scenario — Interview Prep:** explain that Python dicts preserve insertion order since 3.7.

## Topic 4: Sets — Unique Collections & Set Operations

1. Build a set from a list with duplicates using `set()`, and create an empty set with `set()`.
2. Use `.add()` and `.remove()` on a set of tags.
3. Compute a union (`|`) and an intersection (`&`) of two sets.
4. **Debug the Code:** fix a `KeyError`-style crash from `.remove()` on a value not in the set by checking `in` first.
5. Compute a set difference (`-`) to find "students who didn't pass".
6. **Scenario — Tag Deduplication:** build a set from a raw list of repeated tags.
7. **Scenario — Interview Prep:** explain why membership checks on a set beat a list for large collections.

## Topic 5: Nested Dictionaries & Real-World Records

1. Access values in a dict-of-dicts with double indexing.
2. Mutate a nested value with `students["Asha"]["major"] = ...`.
3. Loop over a dict-of-dicts with `.items()` unpacking and print formatted lines.
4. **Debug the Code:** fix indexing order swapped on a nested dict lookup.
5. Combine a dict with lists as values (dept → list of employees) and loop over it.
6. **Scenario — Customer Order Record:** print fields and loop over a list-valued field.
7. **Scenario — Interview Prep:** explain modeling "one user, many phone numbers" with a dict + list.

## Topic 6: Real-World Dicts & Sets in Production

1. Build a word-frequency dictionary using `.get(word, 0) + 1`.
2. Deduplicate a list of emails using a set and compare lengths.
3. Use a dict as a lookup table, with `.get()` handling a missing key.
4. **Debug the Code:** fix a `KeyError` from `counts[grade] += 1` on a first-seen key by using `.get()`.
5. Use set intersection and difference to compare two teams' emails.
6. **Scenario — Log Line Word Frequency:** build and print a frequency table from log words.
7. **Scenario — Interview Prep:** find a count of unique visitors using a set's length.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
