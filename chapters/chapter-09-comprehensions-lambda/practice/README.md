# Chapter 9 Practice Bank: Comprehensions, Lambda & Functional Tools

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses everything from
Chapters 1-8 plus this chapter's own toolkit: list comprehensions
(with and without a filter `if`), dict and set comprehensions, nested
comprehensions, `lambda` functions, and the functional tools `map()`,
`filter()`, and `sorted()`/`.sort()` with `key=lambda`. No `def`
(that's Chapter 10), `try`/`except`, file I/O, classes, or imports yet.

## How to run

```bash
python3 starter.py
```

## Topic 1: List Comprehensions

1. Build a list of squares from `numbers` using a basic list comprehension, and compare it to the equivalent `for` loop.
2. Filter a list comprehension with `if` to keep only even numbers.
3. Use a list comprehension with `if` to keep only strings longer than a given length.
4. Combine a transform and a filter in one comprehension (square only the even numbers).
5. **Debug the Code:** fix a list comprehension that forgot the expression before the `for`.
6. **Scenario — Cleaning Form Input:** strip whitespace from a list of raw form entries with a list comprehension.
7. **Scenario — Interview Prep:** explain why a list comprehension is preferred over a manual `for` loop with `.append()` for simple transforms.

## Topic 2: Dict & Set Comprehensions

1. Build a dict comprehension mapping each word to its length.
2. Build a dict comprehension with an `if` filter to keep only even values.
3. Build a set comprehension to collect unique lengths of words in a list.
4. Build a dict comprehension from two parallel lists using `zip()`-free indexing with `range(len(...))`.
5. **Debug the Code:** fix a dict comprehension that used square brackets instead of curly braces with a colon.
6. **Scenario — Price Lookup Table:** build a dict comprehension mapping product names to prices from two lists.
7. **Scenario — Interview Prep:** explain when you'd reach for a set comprehension instead of a list comprehension.

## Topic 3: Nested Comprehensions & Readability Limits

1. Flatten a list of lists using a nested comprehension.
2. Build a multiplication table as a list of lists using a nested comprehension.
3. Use a nested comprehension with a filter to flatten only the even numbers out of a list of lists.
4. **Debug the Code:** fix a nested comprehension with the `for` clauses written in the wrong order.
5. Rewrite an overly-dense nested comprehension as an equivalent, more readable `for` loop, and comment on which reads better.
6. **Scenario — Flattening Nested Survey Data:** flatten a list of per-department lists of names into one list.
7. **Scenario — Interview Prep:** explain why deeply nested comprehensions are usually a readability smell in production code.

## Topic 4: Lambda Functions

1. Write a `lambda` that doubles a number and call it directly.
2. Write a `lambda` that takes two arguments and returns their sum.
3. Store a `lambda` in a variable and call it several times with different arguments.
4. Use a conditional expression inside a `lambda` to return "even" or "odd".
5. **Debug the Code:** fix a `lambda` that incorrectly tried to use a `return` statement.
6. **Scenario — Quick One-Off Formatter:** use a `lambda` to format a price with a currency symbol.
7. **Scenario — Interview Prep:** explain the single-expression limitation of `lambda` and when you'd use `def` instead.

## Topic 5: `map()`, `filter()`, and `sorted()` with `key=lambda`

1. Use `map()` with a `lambda` to convert a list of strings to their lengths.
2. Use `filter()` with a `lambda` to keep only positive numbers.
3. Use `sorted()` with `key=lambda` to sort a list of tuples by the second element.
4. Use `.sort()` with `key=lambda` to sort a list of dicts by one field, in place.
5. **Debug the Code:** fix a `sorted(..., key=lambda)` call that referenced the wrong field name.
6. **Scenario — Sorting Employee Records:** sort a list of employee dicts by salary using `sorted()` and `key=lambda`.
7. **Scenario — Interview Prep:** explain why `map()`/`filter()` results must be wrapped in `list()` to see their contents.

## Topic 6: Real-World Comprehensions & Functional Tools in Production

1. Clean a list of raw log lines with a list comprehension (strip whitespace, drop empty lines).
2. Build a lookup dictionary from a list of records using a dict comprehension.
3. Combine `filter()` and a list comprehension to validate and transform a batch of user records.
4. **Debug the Code:** fix a data-cleaning pipeline that filtered before converting types, causing a crash.
5. Use `sorted()` with `key=lambda` to rank a list of products by a computed score.
6. **Scenario — Deduplicating and Sorting API Results:** deduplicate a list of records with a set comprehension idea, then sort the result.
7. **Scenario — Interview Prep:** explain why comprehensions and functional tools are so common in real data-cleaning pipelines compared to manual loops.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
