# Chapter 26 Practice Bank (Categories 1-8): Debugging Production Issues

A deeper set of practice problems, organized by topic, for extra reps
beyond the main exercises — including scenario-based problems written
in the same style you'll meet in real interviews. Topics 1-5 cover
Categories 1-2 (Crashes & Exceptions, Performance); Topics 6-10 cover
Categories 3-8 (Memory Leaks, Concurrency & Deadlocks, Data
Corruption, Deployment & Environment, Database & API Failures, and
Logging & Observability). Standard library only — `json`, `copy`,
`math`, `collections` — no installs needed.

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

## Topic 6: Unbounded Growth & Shared State

- **6.1** `bounded_history(events, maxlen)` — cap a growing list with
  `collections.deque(maxlen=...)`.
- **6.2** `evict_oldest(cache, maxsize)` — evict the oldest-inserted
  key once a dict-based cache exceeds `maxsize`.
- **6.3 (Debug the Code)** — `Logger` uses a class-level `history = []`
  shared by every instance; fix it to be a per-instance attribute.
- **6.A (Scenario)** `should_use_weakref_registry(purpose_is_tracking_not_owning)`.
- **6.B (Interview Prep)** `explain_reachable_vs_leaked()`.

## Topic 7: Concurrency Shapes (Modeled Without Real Threads)

- **7.1** `simulate_lost_updates(reads_before_writes)` — given a list of
  "read" values recorded before each of several delayed "writes,"
  compute the final counter value showing how many increments a race
  condition would lose.
- **7.2** `acquisition_order_is_consistent(lock_orders)` — check
  whether every lock-acquisition order in a list of `(first, second)`
  pairs agrees on the same relative ordering (no deadlock risk).
- **7.3 (Debug the Code)** — `pop_if_any()` does a check-then-act on a
  shared list in two separate steps; fix it to be a single atomic
  check-and-pop.
- **7.A (Scenario)** `should_use_multiprocessing(is_cpu_bound)`.
- **7.B (Interview Prep)** `explain_gil_and_threading()`.

## Topic 8: Data Corruption & Precision

- **8.1** `deep_independent_copy(original)` — use `copy.deepcopy()` so
  nested mutations never leak back to the original.
- **8.2** `floats_close(a, b)` — compare floats with `math.isclose()`,
  never `==`.
- **8.3 (Debug the Code)** — `page_slice()` has a pagination off-by-one
  that silently drops the first page; fix the offset math.
- **8.A (Scenario)** `explain_mutable_default_argument_trap()`.
- **8.B (Interview Prep)** `explain_shallow_vs_deep_copy()`.

## Topic 9: Deployment & Environment

- **9.1** `missing_required_env(env, required_keys)` — list every
  missing required environment variable at once.
- **9.2** `resolve_config_value(env, key, default)` — read from
  configuration instead of hardcoding a value.
- **9.3 (Debug the Code)** — `startup_check()` swallows a missing
  environment variable with a bare `except:`; fix it to validate and
  raise a clear error naming what's missing.
- **9.A (Scenario)** `explain_works_on_my_machine()`.
- **9.B (Interview Prep)** `explain_pinning_dependencies()`.

## Topic 10: Database & API Reliability, and Observability

- **10.1** `join_without_n_plus_1(records, lookup_table, key_name)` —
  attach a looked-up field to every record using one dict built up
  front.
- **10.2** `charge_idempotently(processed, idempotency_key, amount)` —
  a safe retry that never double-charges.
- **10.3 (Debug the Code)** — `summarize_log()` builds a free-text log
  message instead of a structured dict; fix it to return structured
  data a log aggregator could filter on.
- **10.A (Scenario)** `explain_unknown_vs_no()`.
- **10.B (Interview Prep)** `explain_log_exception_vs_str_e()`.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks.
