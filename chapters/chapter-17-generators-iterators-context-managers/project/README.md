# Chapter 17 Project: Large-File Streaming Log Analyzer

A menu-driven log analyzer built **around this chapter's core tools** as its
organizing principle -- a generator function, `stream_lines()`, reads a log
file one line at a time using `yield`, instead of ever calling
`file.readlines()` or otherwise loading the whole file into a list. Two more
generators build on top of it: `stream_matching()` yields only the lines
containing a search keyword, and `summarize()` streams the whole file once
to build line/level counts -- both still process the file lazily, one line
at a time, never holding more than the current line in memory. A custom
context manager class, `SessionTimer`, built from `__enter__`/`__exit__`,
wraps every streaming operation to time how long it took and report that
timing even if something goes wrong mid-read -- its `__exit__` checks
whether an exception occurred and reports accordingly, but always returns
`False` so it never silently swallows a real error.

## What you'll build

An object model and generator pipeline covering this chapter's core tools --
**generator functions, `yield`, the iterator protocol behind file objects,
and a custom context manager class** -- plus a menu loop offering four real
operations:

1. Generate sample log file
2. Stream & search for a keyword
3. Stream & summarize (line/level counts)
4. Show last operation's timing info
5. Quit

The pipeline itself is built from these pieces:

- `SessionTimer` -- a context manager class. `__enter__` records the start
  time and returns `self`. `__exit__` computes elapsed time and prints a
  report -- a different message depending on whether an exception occurred
  (`exc_type is None` or not) -- then returns `False` so any real exception
  still propagates normally after being reported.
- `generate_sample_log(path, num_lines, seed)` -- writes a few hundred
  realistic-looking log lines (`[INFO]`, `[WARNING]`, `[ERROR]`, `[DEBUG]`
  entries with a service name and message) to `sample_log.txt`, so the rest
  of the menu has something real to stream through. A seeded `random.Random`
  keeps the output reproducible.
- `stream_lines(path)` -- the core generator. Opens the file with `with`,
  loops `for raw_line in f:` (a file object is itself an iterator over its
  own lines), and `yield`s each line stripped of its newline. Because this
  is a generator function, calling it doesn't read anything yet -- reading
  only happens as something actually iterates over the returned generator.
- `stream_matching(path, keyword)` -- a generator that loops over
  `stream_lines(path)` and yields only the lines containing `keyword`
  (case-insensitive). Filtering happens lazily, line by line, as the file
  streams through -- never on a pre-built list of every line.
- `summarize(path)` -- streams the whole file once via `stream_lines()`,
  accumulating a total line count and a per-level count dictionary. The
  only thing that grows here is the small summary dictionary -- the file
  content itself is never held in memory beyond the current line.

Every option that touches the log file is wrapped in a `with SessionTimer(...)
as timer:` block, so timing information is always available afterward via
option 4, and the `SessionTimer`'s `__exit__` still runs (and still reports)
even on an operation that somehow fails partway through.

Example run:

```
=== Large-File Streaming Log Analyzer ===

1. Generate sample log file
2. Stream & search for a keyword
3. Stream & summarize (line/level counts)
4. Show last operation's timing info
5. Quit
Choose an option (1-5): 1

[timer] starting: generating sample log file
[timer] finished: generating sample log file (0.0317s)
Wrote 400 lines to sample_log.txt.

1. Generate sample log file
2. Stream & search for a keyword
3. Stream & summarize (line/level counts)
4. Show last operation's timing info
5. Quit
Choose an option (1-5): 2

Search for keyword (e.g. ERROR, billing): ERROR
[timer] starting: streaming search for 'ERROR'
  2026-07-06 05:35:05 [ERROR] checkout: unhandled exception in handler
  2026-07-08 07:49:31 [ERROR] billing: unhandled exception in handler
  ...
[timer] finished: streaming search for 'ERROR' (0.0002s)
  ... and 33 more match(es)
Found 43 matching line(s) for 'ERROR'.

1. Generate sample log file
2. Stream & search for a keyword
3. Stream & summarize (line/level counts)
4. Show last operation's timing info
5. Quit
Choose an option (1-5): 3

[timer] starting: streaming summary
[timer] finished: streaming summary (0.0004s)
Summary of sample_log.txt:
  Total lines: 400
  INFO: 232
  WARNING: 67
  ERROR: 43
  DEBUG: 58

1. Generate sample log file
2. Stream & search for a keyword
3. Stream & summarize (line/level counts)
4. Show last operation's timing info
5. Quit
Choose an option (1-5): 4

Last timed operation: 'streaming summary' took 0.0004s

1. Generate sample log file
2. Stream & search for a keyword
3. Stream & summarize (line/level counts)
4. Show last operation's timing info
5. Quit
Choose an option (1-5): 5

Goodbye!
```

Notice that the search and summary options both go through `stream_lines()`
one line at a time -- neither one ever builds a Python list containing every
line of the file. The sample file here is only 400 lines so the example runs
fast enough to read on a course page, but the exact same generator function
would stream a 10GB log file identically: at any given moment, it only ever
holds the current line in memory, whether the file is a few hundred lines
or a few hundred million.

## How to run it

```bash
cd chapters/chapter-17-generators-iterators-context-managers/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder) -- option 1 will (re)generate `sample_log.txt` for you.

## Ideas to make it your own (optional stretch goals)

- Add a "streaming word count" menu option that counts, across the whole
  file, how many lines mention each service name in `SERVICES` -- still via
  one pass of `stream_lines()`, no `readlines()`.
- Add a second custom context manager, `SafeFileReport`, whose `__exit__`
  catches a `FileNotFoundError` specifically (returning `True` only for that
  one exception type) and prints a friendly "no log file yet" message,
  demonstrating that a context manager's `__exit__` can choose to suppress
  one specific kind of exception while still letting others propagate.
- Change `stream_matching()` to accept multiple keywords and yield a line
  if it contains *any* of them, still processing the file lazily one line
  at a time.

## Why this project matters

Real production systems -- web servers, payment processors, data pipelines --
generate log files that can reach many gigabytes per day, and analyzing them
by loading the whole thing into memory first (`readlines()`, `pandas` with
no chunking, etc.) is one of the most common ways a data-processing script
crashes a production machine or a CI job runs out of memory. The pattern
this project builds -- a generator that reads and processes one line (or one
record) at a time, wrapped in `with` so file handles are always released
correctly even if something goes wrong mid-read -- is exactly the technique
real log analyzers, ETL pipelines, and streaming data tools use to process
files far larger than available RAM. The custom `SessionTimer` context
manager mirrors a genuinely common production pattern too: wrapping a
long-running operation to measure and report its duration for monitoring
and performance debugging, regardless of whether it succeeds or fails.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Large-File Streaming Log Analyzer above is fully built out with a starter
and reference solution -- the four ideas below are not. Each is a real,
grounded use case solvable with only what's been taught through Chapter 17
(everything through Chapter 16's inheritance/polymorphism/`isinstance()`,
plus this chapter's generator functions, generator expressions, and the
`__enter__`/`__exit__` context-manager protocol). No starter or solution
files are provided on purpose -- building one of these unassisted is the
point.

### 1. Custom `PrimeNumbers` Iterator/Generator

**Problem:** A math teaching tool, a cryptography demo, or a number-theory
exercise needs a source of prime numbers that can be pulled from one at a
time, without ever knowing in advance how many will actually be needed --
computing "the first million primes" up front just to maybe use the first
five would be wasteful.

**What it should do:** Build a generator function `primes()` that `yield`s
prime numbers one at a time, forever (an infinite generator -- it never
runs out on its own, since there's no largest prime), using a simple
primality check (trial division up to the square root of the candidate
number, using `math.sqrt` from earlier chapters). Menu options: show the
first N primes (prompt for N, then pull exactly N values from a fresh call
to `primes()` using `next()` in a loop, or `itertools`-free manual
iteration), check whether a specific number is prime, show the sum of the
first N primes, and quit.

**Suggested approach:** Because `primes()` is infinite, never do
`list(primes())` -- always pull a bounded number of values by calling
`next()` in a loop a fixed number of times, or by breaking out of a `for`
loop once a counter reaches the requested N.

### 2. CSV Streaming Summarizer

**Problem:** A data analyst needs to summarize a large CSV file (e.g. sales
transactions, sensor readings) -- computing totals, averages, or counts per
category -- without loading the entire file into memory as a list of rows
first, exactly the same memory concern as the streaming log file in this
chapter's main project, just applied to structured CSV data instead of
plain text lines.

**What it should do:** Build a generator function that opens a CSV file
with `csv.DictReader` (from Chapter 12's `csv` module) and `yield`s one row
(a dict) at a time -- `DictReader` is itself already an iterator, so the
generator can simply loop `for row in reader: yield row`. Menu options:
generate a sample CSV file of transactions (category, amount columns),
stream & compute the total amount per category, stream & find the single
largest transaction, and quit.

**Suggested approach:** Keep a running dictionary of category totals (or a
single "largest so far" variable) that updates as each row streams through,
the same accumulation pattern as this chapter's `summarize()` function,
just reading dict rows instead of plain text lines.

### 3. Reusable `Stopwatch` Context Manager Library

**Problem:** Almost any program benefits from being able to time specific
sections of its own code during development or in production monitoring --
but writing `start = time.perf_counter()` / `elapsed = time.perf_counter() -
start` by hand around every section that needs timing is repetitive and
easy to forget the cleanup half of.

**What it should do:** Build a `Stopwatch` context manager class (similar to
this chapter's `SessionTimer`, but designed to be genuinely reusable across
different projects) that supports being used multiple times in the same
program, keeps a running list of every timed lap's label and duration on
the instance, and has a `report()` method that prints every lap recorded so
far. Menu options: run a "fake slow operation" (e.g. a loop that does
busywork or calls `time.sleep()` for a random short duration) wrapped in the
stopwatch under a label the user provides, show the full lap report so far,
show which labeled lap took the longest, and quit.

**Suggested approach:** Store laps as a list of `(label, elapsed)` tuples on
`self` inside `__init__`, append to that list from `__exit__` every time the
context manager is used, and have `report()` and the "longest lap" menu
option simply loop over that list -- no need to reach for anything beyond
what earlier chapters already taught for storing and scanning a list of
tuples.

### 4. Batch Processor (Fixed-Size Chunk Generator)

**Problem:** Some operations -- sending records to an API with a per-request
limit, writing rows to a database in transactions, processing images in
memory-bounded groups -- need to process a large collection in fixed-size
batches (e.g. 50 items at a time) rather than either one item at a time or
the whole collection at once.

**What it should do:** Build a generator function `batched(items, size)`
that `yield`s successive fixed-size chunks (as lists) from an iterable
`items`, with the final chunk being shorter if the total count doesn't
divide evenly by `size`. Menu options: generate a sample list of N fake
"records" (plain strings or numbers), process them in batches of a
user-chosen size (printing each batch as it's produced, with a fake "sending
batch to API" message per batch), show how many total batches a given N and
size would produce without actually processing them, and quit.

**Suggested approach:** Inside `batched()`, build each chunk with a plain
list and a counter, `yield`ing the chunk and resetting it once it reaches
`size` items, then `yield`ing whatever's left over (if anything) once the
input is exhausted -- the same kind of accumulate-then-emit pattern as
`summarize()` in this chapter's main project, but emitting a list at a time
instead of an integer count.
