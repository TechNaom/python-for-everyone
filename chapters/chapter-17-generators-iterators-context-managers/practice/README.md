# Chapter 17 Practice Bank: Generators, Iterators & Context Managers

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. This is the chapter
where `yield`/generator functions, generator expressions, and the
context-manager protocol (`__enter__`/`__exit__`) become allowed, on
top of everything from Chapters 1-16 (including general classes,
`__init__`, dunder methods, `@staticmethod`/`@classmethod`/`@property`,
inheritance, `super()`, method overriding, polymorphism, and
`isinstance()`). No import beyond `math`/`datetime`/`random`/`csv`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Iterables vs. Iterators

1. Write a `Countdown` class with `__iter__`/`__next__` that counts down from a starting value to 0, raising `StopIteration` after.
2. Write a `RepeatTwice` iterable and a matching iterator class that yields each item in a list twice in a row.
3. Manually drive `iter()`/`next()` on a list without a `for` loop, catching `StopIteration` yourself.
4. Write an `EvenNumbers` class with `__iter__`/`__next__` that produces every even number up to a limit.
5. **Debug the Code:** fix a `__next__` method that never raises `StopIteration`, which would loop forever.
6. **Scenario — A Paginated API Client Walking Pages by Hand:** write a `PageWalker` iterator that walks through a list of pages one at a time.
7. **Scenario — Interview Prep:** explain what makes an object "iterable" versus an "iterator," and how a `for` loop uses that distinction.

## Topic 2: Generator Functions

1. Write a generator function `count_up_to(limit)` using `yield` to produce integers one at a time.
2. Write a generator function `squares_up_to(limit)` using `yield` to produce squares.
3. Write a generator function `alternating_signs(limit)` mixing `if`/`else` logic with `yield`.
4. Write a generator function `countdown_then_liftoff(start)` that yields numbers, then a final string.
5. **Debug the Code:** fix a function meant to be a generator that used `return` instead of `yield` inside its loop.
6. **Scenario — Streaming Sensor Readings One at a Time:** write a generator function that lazily filters sensor readings above a threshold.
7. **Scenario — Interview Prep:** explain the difference between a function using `return` and a generator function using `yield`.

## Topic 3: Generator Expressions

1. Compare a list comprehension and a generator expression built from the same source, checking their types.
2. Sum values directly over a generator expression with `sum()`.
3. Find the max of a generator expression with `max()`.
4. Use `any()` over a generator expression to short-circuit on the first match.
5. **Debug the Code:** fix square brackets that were supposed to be parentheses, turning a list comprehension back into a lazy generator expression.
6. **Scenario — Checking a Huge Log File for One Matching Line Without Loading It All:** use `any()` with a generator expression to check for a matching line.
7. **Scenario — Interview Prep:** explain why you'd choose a generator expression over a list comprehension.

## Topic 4: The `with` Protocol Generalized (`__enter__`/`__exit__`)

1. Write a `ManagedResource` class with `__enter__`/`__exit__` and use it in a `with` block, showing state before/after.
2. Write a `Timer` class showing `__exit__` runs automatically when the block ends.
3. Write a `NoisyBlock` class showing the exact order `__enter__`/block-body/`__exit__` run.
4. Write a `SuppressValueError` class whose `__exit__` suppresses a `ValueError` by returning `True`.
5. **Debug the Code:** fix a class missing `__exit__` entirely, which raises `TypeError` the moment `with` runs.
6. **Scenario — Guaranteeing a Lock Is Always Released:** write a `SimpleLock` context manager guaranteeing release.
7. **Scenario — Interview Prep:** explain what problem the `with` statement and context-manager protocol solve.

## Topic 5: Writing a Custom Context Manager Class

1. Write your first fully custom context manager, `LoggingContext`, from scratch.
2. Write a `CallCounter` context manager tracking how many times it's been entered.
3. Write an `ExceptionLogger` context manager that collects errors instead of crashing.
4. Write a `Transaction` context manager that tracks whether it committed successfully.
5. **Debug the Code:** fix an `__exit__` that accidentally returns `True`, silently swallowing exceptions it shouldn't.
6. **Scenario — A Reusable Timing Context Manager for Performance Checks:** write a `StepTracker` context manager counting completed steps.
7. **Scenario — Interview Prep:** explain exactly what Python does, step by step, when it executes a `with SomeClass() as x:` block.

## Topic 6: Bringing It Together — Real-World Use

1. Write a generator function `stream_lines(text)` that lazily yields lines from text, one at a time.
2. Combine a generator function with a custom context manager to count long lines as they're filtered.
3. Write `first_n_matching(items, predicate_threshold, limit)`, a generator that lazily stops after N matches.
4. Write a `FileSimulator` context manager with a `lines()` generator method, standing in for a real file.
5. **Debug the Code:** fix a generator function that used `return` with a list comprehension instead of `yield`, defeating laziness.
6. **Scenario — A Log-Processing Pipeline Combining Everything:** combine a context manager and a generator function to filter error lines.
7. **Scenario — Interview Prep:** describe a real production system where generators, iterators, and context managers all show up together.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
