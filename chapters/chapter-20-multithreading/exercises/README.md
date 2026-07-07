# Chapter 20 Exercises: Multithreading

These exercises use what Chapter 20 covered: creating and starting threads
(`threading.Thread`, `.start()`, `.join()`), the I/O-bound vs. CPU-bound
distinction, race conditions, `threading.Lock`, and
`concurrent.futures.ThreadPoolExecutor`. Every "download" or "wait" here
uses `time.sleep()` to stand in for a slow network or disk operation -- no
real network access or file I/O happens anywhere in this folder.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — Creating and joining threads

Find `# TODO 1`. Write `square_task(n, results_list)` that appends `n * n`
to `results_list`. Create a thread for each of `[2, 3, 4]`, start every
thread, join every thread, then print `sorted(results)`.

## Task 2 — I/O-bound vs. CPU-bound

Find `# TODO 2`. Write `classify_work(description)` returning
`"I/O-bound"` for `"downloading a file"`, `"calling an API"`, or
`"reading from a database"`, and `"CPU-bound"` otherwise.

## Task 3 — A race condition

Find `# TODO 3`. Run `increment_unsafe(times)` (already provided, with no
lock) on 4 threads and print the (unreliable, too-low) final count.

## Task 4 — Fixing it with a lock

Find `# TODO 4`. Write `increment_safe(times)` -- identical to
`increment_unsafe`, but with the shared counter's read/write wrapped in
`with lock:`. Confirm the final count is always exactly correct.

## Task 5 — `ThreadPoolExecutor.map()`

Find `# TODO 5`. Write `cube(n)` returning `n ** 3`, and run it across
`[1, 2, 3]` using `ThreadPoolExecutor(max_workers=3).map()`.

## Task 6 — Locking a shared results list

Find `# TODO 6`. Write `add_order_total(order, totals_list, lock_obj)`
that safely appends `sum(order)` to a shared list from multiple threads.

## Task 7 — Debug the Code

Find `# TODO 7`. This is supposed to run three simulated downloads
concurrently, but it calls `t.join()` immediately after `t.start()` inside
the same loop, so each thread fully finishes before the next one even
starts -- running them one at a time instead of concurrently. Find and
fix it.

## Task 8 — Debug the Code

Find `# TODO 8`. This is supposed to safely increment a shared counter
across 4 threads, but it reads and writes the shared counter without ever
using `total_lock`, so it's vulnerable to the same race condition as
Task 3. Find and fix it.

## Checking your work

Compare your output against `solution.py`. Every task's output is exactly
reproducible **except** Task 3's deliberately-unsafe demo, whose final
number will vary between runs (and between your machine and this
README) -- that unpredictability is the entire point of that task. Every
other task's output matches `solution.py` exactly, every time.
