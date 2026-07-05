# Module 2 Written Exam — Data Structures & Functions

Covers Chapters 6-10: Strings Deep Dive, Lists & Tuples, Dictionaries &
Sets, Comprehensions/Lambda & Functional Tools, and Functions Deep Dive.

**Format:** 8 short-answer + 3 scenario questions + 1 synthesis question.
Suggested time: 60 minutes. Closed notes recommended for the first
attempt; open notes is fine for self-paced learners checking their own
understanding.

---

## Section A — Short Answer (2 points each, 16 points)

**A1.** Strings are immutable in Python. What does that actually mean,
and what happens if you try to do `name[0] = "J"`?

**A2.** What does the slice `text[2:8:2]` mean, in plain English?

**A3.** What's the difference between `backup = original` and
`backup = original.copy()` for a list?

**A4.** Give one real reason you'd choose a tuple over a list for a
piece of data.

**A5.** Why is `my_dict.get(key, default)` usually safer than
`my_dict[key]` when you're not sure the key exists?

**A6.** What does the `&` operator do when used between two sets?

**A7.** Rewrite this loop as a single list comprehension:
```python
result = []
for n in numbers:
    if n % 2 == 0:
        result.append(n * n)
```

**A8.** What's the difference between what `*args` collects and what
`**kwargs` collects, inside a function definition?

---

## Section B — Scenario Questions (6 points each, 18 points)

**B1.** A function takes a list, does `data.append("done")` inside it,
and the caller is surprised to see `"done"` in their original list after
the call returns — they expected the function to only affect its own
copy. Explain what's actually happening and why it's not a bug.

**B2.** A dictionary is being built up inside a loop with
`tally[word] = tally[word] + 1`, and it crashes with `KeyError` the
first time a new word shows up. What's wrong, and what's the one-line
fix?

**B3.** A function is defined as
`def add_item(item, cart=[]):` and every call seems to remember items
from previous calls, even though `cart` is supposed to default to a
fresh empty list each time. Explain why this happens and how to fix it.

---

## Section C — Synthesis (6 points)

**C1.** Write a function `top_scorers(students, cutoff=90)` that takes a
list of dicts like `{"name": "Priya", "score": 94}` and returns a list
of just the names of students whose score is at or above `cutoff`
(default 90). Your answer should correctly use concepts from at least
three different chapters in this module (e.g. a default argument,
dictionary key access, and a comprehension or loop).

---

## Answer Key

**A1.** Immutable means a string's characters can never be changed in
place once created — any "modification" actually builds and returns a
brand-new string, leaving the original untouched. `name[0] = "J"` raises
a `TypeError: 'str' object does not support item assignment`.

**A2.** Starting at index 2, up to (but not including) index 8, taking
every 2nd character.

**A3.** `backup = original` doesn't copy anything — both names now point
to the exact same list in memory, so mutating one through methods like
`.append()` affects both. `backup = original.copy()` creates a genuinely
separate list with the same contents, so changes to one don't affect
the other.

**A4.** Any reasonable real use case is acceptable — e.g. representing a
fixed record that shouldn't accidentally change (like GPS coordinates
or an (x, y) point), or signaling to readers of the code that this data
is meant to stay constant.

**A5.** `my_dict[key]` raises a `KeyError` and crashes the program if
the key is missing, while `.get(key, default)` returns the fallback
value instead of crashing, letting your code keep running.

**A6.** It returns a new set containing only the elements that appear
in *both* sets (the intersection).

**A7.**
```python
result = [n * n for n in numbers if n % 2 == 0]
```

**A8.** `*args` collects any extra *positional* arguments into a tuple.
`**kwargs` collects any extra *keyword* arguments into a dictionary
(mapping argument name to value).

---

**B1.** Lists are mutable, and Python passes them into functions by
object reference, not by making a copy — so `data` inside the function
and the caller's original variable both refer to the exact same list in
memory. Calling a mutating method like `.append()` on it changes that
one shared list, which is visible from both places. This is standard,
expected Python behavior (not a bug) — if the function needed to avoid
this, it would need to work on `data.copy()` instead.

**B2.** `tally[word]` on the right-hand side tries to *read* a value
that doesn't exist yet for a first-seen word, raising `KeyError` before
the assignment can even happen. Fix: use
`tally[word] = tally.get(word, 0) + 1`, which supplies `0` as a fallback
the first time.

**B3.** A default argument value (like `[]`) is created only *once*,
when the function is defined — not fresh on every call. Since lists are
mutable, every call that relies on the default is actually sharing and
mutating that same original list. Fix: use `def add_item(item,
cart=None):` and then `if cart is None: cart = []` as the first line
inside the function body.

**C1.** A correct answer uses a default argument (Chapter 10), reads a
dict key like `student["score"]` (Chapter 8), and a comprehension or
loop (Chapter 9/any) — for example:

```python
def top_scorers(students, cutoff=90):
    return [student["name"] for student in students if student["score"] >= cutoff]
```

---

## Grading Guidance

| Section | Points | Notes |
|---|---|---|
| A (8 x 2) | 16 | Award partial credit (1 pt) for a mostly-correct answer missing precise terminology. |
| B (3 x 6) | 18 | Full credit requires both identifying the cause AND stating the fix. |
| C (1 x 6) | 6 | Award full credit for any correct approach; code doesn't need to match the sample exactly. |
| **Total** | **40** | 34+ = strong grasp of Module 2; 24-33 = solid but revisit weak areas; below 24 = re-read the relevant chapters before Module 3. |
