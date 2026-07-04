# Chapter 5 Project: Number Pattern Generator

Pattern printing is a classic exercise for building real comfort with
nested loops — and a genuinely common interview warm-up question.

## What you'll build

A script that prints three patterns using nested for loops.

Example run:

```
--- Pattern 1: Increasing triangle ---
1
12
123
1234
12345
--- Pattern 2: Star pyramid ---
*
**
***
****
*****
--- Pattern 3: Decreasing triangle ---
54321
5432
543
54
5
```

## How to run it

```bash
python3 starter.py
```

Fill in the `# TODO` sections in `starter.py`. Want to see one finished
version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Make the size (5 rows) a variable instead of hardcoded.
- Print a pattern using letters (A, AB, ABC, ...) instead of numbers.
- Try building a diamond by combining an increasing and decreasing
  pyramid back to back.

## Why this project matters

Nested loops are exactly how you'd process a grid, a matrix, or any
two-dimensional data — spreadsheets, game boards, image pixels. Pattern
printing looks decorative, but the underlying skill (an outer loop
controlling rows, an inner loop controlling columns) is used constantly
in real software.
