# Chapter 17 Exercises: Generators, Iterators & Context Managers

These exercises use what Chapter 17 covered: the iterator protocol
(`__iter__`/`__next__`), generator functions with `yield`, generator
expressions, the `with` statement's `__enter__`/`__exit__` protocol,
custom context manager classes, and streaming a file line-by-line with
a generator.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — A custom iterator class

Find `# TODO 1`. Write a class `Countdown` whose `__init__` takes
`start` and stores it as `self.current`. Give it `__iter__(self)`
that returns `self`, and `__next__(self)` that raises
`StopIteration` once `self.current` is `0` or less, otherwise
returns the current value and decrements it by `1`. Create a
`Countdown(4)` and loop over it with a `for` loop, printing each
value.

## Task 2 — A generator function with `yield`

Find `# TODO 2`. Write a generator function `evens_up_to(n)` that
starts a counter at `0` and, while the counter is less than or equal
to `n`, `yield`s the counter and then increases it by `2`. Loop over
`evens_up_to(10)` with a `for` loop and print each value.

## Task 3 — A generator expression

Find `# TODO 3`. Use `sum()` with a generator expression (not a list
comprehension) to add up the cubes (`n ** 3`) of every number from
`1` to `5` inclusive. Store the result in `total` and print it.

## Task 4 — The `with` statement recap

Find `# TODO 4`. Use `with open(...) as f:` to write the three lines
`"1"`, `"2"`, and `"3"` (each on its own line) to a file named
`"numbers.txt"`. Then use a second `with open(...) as f:` block to
read all the lines back with `.readlines()` into a variable `lines`.
Print `len(lines)`, then print `f.closed` right after the block ends.

## Task 5 — A custom context manager class

Find `# TODO 5`. Write a class `Timer` with `__enter__(self)` that
sets `self.entered = True` and returns `self`, and
`__exit__(self, exc_type, exc_value, traceback)` that sets
`self.exited = True` and returns `False`. Use
`with Timer() as t: pass` and then print `t.entered` and `t.exited`.

## Task 6 — Streaming a file with a generator

Find `# TODO 6`. Write a generator function `read_lines(filename)`
that opens the file with `with`, loops over it with `for line in f:`,
and `yield`s each line with `.strip()` applied. First, write the
three lines `"alpha"`, `"beta"`, and `"gamma"` to a file named
`"stream.txt"` using `with open(...) as f:`. Then loop over
`read_lines("stream.txt")` with a `for` loop and print each line.

## Task 7 — Debug the Code

Find `# TODO 7`. This generator function accidentally uses
`return count` instead of `yield count` inside its loop, so calling
it and looping over it only ever produces the very first value
before the generator ends — the caller never sees the rest of the
count. Find and fix it.

## Task 8 — Debug the Code

Find `# TODO 8`. This custom context manager's `__exit__` method
handles a `ZeroDivisionError` by printing a message, but it
mistakenly `return`s `True` at the end no matter what — silently
swallowing the exception so the code that called it never finds out
anything went wrong. Find and fix it so the exception still
propagates after being logged.

## Checking your work

Compare your output against `solution.py`. Every example here uses
fixed, explicit values, so your output should match `solution.py`
exactly.
