# Chapter 7 Practice Bank: Lists & Tuples

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses everything from
Chapters 1-6 plus this chapter's own toolkit: list literals,
indexing/negative indexing/slicing, mutability, `len()`, the list
methods covered in the lesson (`append`, `insert`, `extend`, `remove`,
`pop`, `clear`, `sort`, `sorted()`, `reverse`, `count`, `index`),
tuples (creation, indexing/slicing, packing/unpacking), nested lists,
and copying lists with `.copy()` or slicing. No dictionaries/sets,
comprehensions, `lambda`, functions (`def`), or `try`/`except` yet.

## How to run

```bash
python3 starter.py
```

## Topic 1: Creating Lists & Accessing Elements

1. Given `fruits = ["apple", "banana", "cherry", "date"]`, print the list and its length with `len()`.
2. Given `scores = [88, 92, 79, 95, 84]`, print the first score with a positive index and the last with a negative index.
3. Given `letters = ["a", "b", "c", "d", "e", "f"]`, print a slice `letters[1:4]` and the whole list reversed with `letters[::-1]`.
4. Given `inventory = [10, 25, 30]`, mutate `inventory[1] = 40` and explain why that works on a list but not on a string.
5. **Debug the Code:** fix an `IndexError` caused by using `nums[len(nums)]` instead of `nums[len(nums) - 1]`.
6. **Scenario — Employee Roster:** print the first and last name on a roster, plus its length.
7. **Scenario — Interview Prep:** demonstrate list mutability vs. string immutability and explain the core distinction.

## Topic 2: List Methods That Grow, Shrink & Reorder

1. Use `.append()` and `.insert()` to build up a shopping cart.
2. Use `.extend()` to merge two task lists, and explain how it differs from `.append()`.
3. Use `.remove()` by value and `.pop()` by index on a queue, printing the popped value.
4. **Debug the Code:** fix a `ValueError` from `.remove()` on a missing value by checking `in` first.
5. Compare `sorted()` (returns a new list) with `.sort()` (mutates in place), then `.reverse()`, `.count()`, and `.index()`.
6. **Scenario — To-Do List Manager:** append a new task and remove a completed one.
7. **Scenario — Interview Prep:** explain the difference between `sort()` and `sorted()`.

## Topic 3: Tuples — Immutable Sequences & Packing/Unpacking

1. Index and slice a tuple with `point = (3, 7)` and `coords = (10, 20, 30, 40)`.
2. Unpack `person = ("Asha", 29, "Engineer")` into three variables in one line.
3. Explain tuple immutability, then build a new tuple via concatenation.
4. **Debug the Code:** fix a `ValueError` from unpacking a 3-item tuple into only 2 variables.
5. Swap two variables in one line with tuple packing/unpacking (`a, b = b, a`).
6. **Scenario — GPS Coordinates:** unpack a `(latitude, longitude)` tuple into a report line.
7. **Scenario — Interview Prep:** explain why you'd choose a tuple over a list for data that shouldn't change.

## Topic 4: Nested Lists & 2D Data

1. Access an element of a 2D grid with double indexing, `grid[1][2]`.
2. Mutate a single nested element with `grid[0][0] = 100`.
3. Use a nested `for` loop to print every value in a grid.
4. **Debug the Code:** fix indices swapped in the wrong order (and out of range) on a nested list.
5. Use a nested loop with an accumulator to sum every value across a 2D list.
6. **Scenario — Tic-Tac-Toe Board:** check whether a row is all the same mark.
7. **Scenario — Interview Prep:** explain the difference between `matrix[0]` (a row) and `matrix[0][0]` (a single value).

## Topic 5: Copying Lists — Shallow Copies & the is-vs-== Trap

1. Demonstrate the aliasing bug: `alias = original` shares the same list object.
2. Fix it with `.copy()` and with slicing (`original[:]`).
3. Compare `==` (value equality) and `is` (identity) on separately-built lists.
4. **Debug the Code:** fix a "backup" that was actually just an alias, not a real copy.
5. Show the shallow-copy trap: copying a nested list still shares the inner lists.
6. **Scenario — Backup Before Editing:** make a true independent copy before making edits.
7. **Scenario — Interview Prep:** explain `==` vs. `is` for two lists with equal contents.

## Topic 6: Real-World Lists & Tuples in Production

1. Sum and average a list of order totals with the accumulator pattern.
2. Loop over a list of `(x, y)` tuples to compute a squared distance for each point.
3. Build a small pass/fail report from a list of scores.
4. **Debug the Code:** fix an accumulator that uses `=` instead of `+=` and never actually accumulates.
5. Filter a list down to values above a threshold, then sort the result.
6. **Scenario — Sales Report:** compute line totals and a grand total from a list of `(product, price, qty)` tuples.
7. **Scenario — Interview Prep:** deduplicate a list while preserving order, then find the min/max/average without `min()`/`max()`.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
