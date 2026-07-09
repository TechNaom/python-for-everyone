# Chapter 26 Practice Bank (Categories 1-2): Debugging Production Issues

A deeper set of practice problems, organized by topic, for extra reps
beyond the main exercises — including scenario-based problems written
in the same style you'll meet in real interviews. Standard library
only — `json`, no installs needed.

## How to run

Run this **from inside this `practice/` folder**:

```bash
cd practice
python3 starter.py
```

## Topic 1: Missing Keys & Out-of-Range Access

- **1.1** `required_config_or_raise(config, required_keys)` — raise a
  `RuntimeError` listing every missing key at once.
- **1.2** `safe_slice_sum(values, n)` — sum the first `n` items without
  ever indexing past the end.
- **1.3 (Debug the Code)** — `last_n_scores()` uses `range(n)` to index
  from the front instead of slicing from the back; fix it.
- **1.A (Scenario)** `should_use_get(key_always_present)`.
- **1.B (Interview Prep)** `explain_keyerror_vs_get()`.

## Topic 2: Exception Handling That Hides Bugs

- **2.1** `divide_or_none(a, b)` — catch `ZeroDivisionError`
  specifically.
- **2.2** `parse_int_or_default(raw, default)` — catch `ValueError`
  specifically, nothing else.
- **2.3 (Debug the Code)** — `get_setting()` uses a bare `except:`
  that would hide unrelated bugs; fix it to catch only `KeyError`.
- **2.A (Scenario)** `explain_why_bare_except_is_risky()`.
- **2.B (Interview Prep)** `explain_specific_vs_broad_except()`.

## Topic 3: None, Zero, and Other Quiet Failure Values

- **3.1** `find_or_none(items, predicate_key, predicate_value)`.
- **3.2** `get_email_safe(items, name)` — handle a `None` result from
  `find_or_none()` safely.
- **3.3 (Debug the Code)** — `average_price()` crashes on an empty
  list; fix it to return `None` instead.
- **3.A (Scenario)** `parse_api_results(raw_text)` — handle a
  non-JSON API response.
- **3.B (Interview Prep)** `explain_none_vs_exception()`.

## Topic 4: Accidental O(n^2) Patterns

- **4.1** `has_common_element(list_a, list_b)` — convert one list to a
  set for an O(1) membership check.
- **4.2** `unique_in_order(items)` — deduplicate while preserving
  order, using a set to track what's seen.
- **4.3 (Debug the Code)** — `merge_prepend()` uses `list.insert(0, x)`
  in a loop (O(n^2)); fix it with list concatenation (O(n)).
- **4.A (Scenario)** `should_use_set_for_lookup(collection_size, checked_repeatedly)`.
- **4.B (Interview Prep)** `explain_quadratic_pattern()`.

## Topic 5: Caching & Redundant Work

- **5.1** `memoized_calls(keys, compute_fn)` — cache repeated keys
  instead of recomputing.
- **5.2** `count_distinct_calls(keys)` — the number of "real"
  computations a cache would actually need to perform.
- **5.3 (Debug the Code)** — `tax_totals()` recomputes an expensive
  lookup per item instead of caching by region; fix it.
- **5.A (Scenario)** `should_cache_by_region(num_items, num_distinct_regions)`.
- **5.B (Interview Prep)** `explain_when_caching_is_safe()`.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks.
