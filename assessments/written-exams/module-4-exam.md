# Module 4 Written Exam — Real-World Python

Covers Chapters 17-21: Generators, Iterators & Context Managers, Regular
Expressions, Working with APIs & JSON, Multithreading, and Working with
Databases.

**Format:** 8 short-answer + 3 scenario questions + 1 synthesis question.
Suggested time: 60 minutes. Closed notes recommended for the first
attempt; open notes is fine for self-paced learners checking their own
understanding.

---

## Section A — Short Answer (2 points each, 16 points)

**A1.** What's the difference between a generator function (using
`yield`) and a normal function that builds and returns a full list?

**A2.** Why does `re.findall(r"<.*>", html)` (a greedy quantifier) risk
matching much more text than intended on a string containing several
separate `<tag>...</tag>` pairs, compared to `re.findall(r"<.*?>", html)`?

**A3.** What does `response.json()` do, in the `requests` library, and
what would calling it on a response that isn't actually JSON cause?

**A4.** Why does `dict.get("key", default)` help avoid a common bug when
working with data parsed from JSON, compared to `data["key"]`?

**A5.** What does the GIL (Global Interpreter Lock) actually prevent, and
why does that still leave threading useful for I/O-bound work?

**A6.** Why is `counter += 1` not automatically safe to run from
multiple threads at once, even though it looks like a single operation?

**A7.** What is a parameterized query (`cursor.execute(sql, params)`),
and what specific problem does it prevent?

**A8.** What's the key structural difference between a relational
database row and a MongoDB document?

---

## Section B — Scenario Questions (6 points each, 18 points)

**B1.** A regex `r"(\d{3})-(\d{4})"` is used with `re.search()` on the
string `"Call 555-1234 now"`. Explain what `match.group(0)`,
`match.group(1)`, and `match.group(2)` each return, and why groups exist
as a feature separate from just matching the whole pattern.

**B2.** A program reads a large log file line by line using a generator
function instead of loading the whole file into a list first. A teammate
asks why this matters if the file is only a few megabytes. Explain the
real benefit of the generator approach and when it stops mattering much.

**B3.** Four threads each call a function that reads a shared
`total` variable, adds a different amount to it, and writes the new
value back — with no lock. The final result printed at the end is
noticeably lower than the mathematically correct total, and it's a
different (still wrong) number on different runs. Explain exactly what's
happening and how to fix it.

---

## Section C — Synthesis (6 points)

**C1.** Combine ideas from at least three different chapters in this
module: write a small custom context manager class `LineCounter` whose
`__enter__` sets up a `count` attribute at `0` and returns `self`, and
whose `__exit__` returns `False` (chosen deliberately, so any exception
raised inside the `with` block still propagates rather than being
silently swallowed). Then write a generator function `non_blank_lines(lines)`
that yields each non-empty, stripped line from an iterable `lines`
(skipping lines that are empty or only whitespace). Finally, write a
`with LineCounter(...) as lc:` block that iterates over
`non_blank_lines(lc.lines)`, increments `lc.count` for each line
yielded, and collects the stripped lines into a list. Your answer should
correctly use a custom context manager (`__enter__`/`__exit__`), a
generator function (`yield`), and iteration over that generator inside
the `with` block.

---

## Answer Key

**A1.** A generator function computes and yields one value at a time,
pausing between each `yield` and resuming exactly where it left off,
without ever holding the entire sequence in memory at once. A normal
function that builds and returns a full list computes every value up
front and holds the complete result in memory before returning anything.
For a very large or unbounded sequence, the generator's lazy,
one-at-a-time approach uses dramatically less memory.

**A2.** A greedy quantifier (`.*`) matches as much text as it possibly
can while still allowing the overall pattern to succeed — on a string
containing multiple `<tag>` pairs, `<.*>` will stretch from the very
first `<` all the way to the very last `>` in the string, swallowing
everything in between (including other complete tags) into a single
match. A non-greedy quantifier (`.*?`) matches as little text as
possible instead, stopping at the first `>` it finds, which is almost
always the intended behavior when matching individual tags.

**A3.** `response.json()` parses the response body as JSON and returns
it as ordinary Python data (a dict, list, or other JSON-compatible
value). If the response body isn't actually valid JSON (an error page's
HTML, for instance), calling `.json()` raises an exception rather than
returning some sensible fallback — which is exactly why checking
`response.status_code` before calling `.json()` is standard practice.

**A4.** `data["key"]` raises a `KeyError` and crashes the program if
`"key"` doesn't exist, which is a real risk with JSON data from an
external source that isn't guaranteed to include every expected field
on every response. `dict.get("key", default)` returns `default` instead
of crashing when the key is missing, letting a program handle a missing
field gracefully rather than failing outright.

**A5.** The GIL prevents more than one thread from executing Python
bytecode at the exact same instant, even on a multi-core machine — so
multiple Python threads never truly run Python code in parallel on
separate cores. Threading still helps I/O-bound work because a thread
waiting on I/O (network, disk, `time.sleep()`) releases the GIL for the
duration of that wait, letting another thread run during it — the
benefit comes from overlapping waits, not from simultaneous computation.

**A6.** `counter += 1` is really three separate steps under the hood:
read the current value, add 1 to it, and write the new value back. The
GIL only prevents two threads from executing bytecode at the literal
same instant — it does not prevent a thread from being paused between
these three steps while another thread runs. If one thread's
read-modify-write sequence gets interrupted by another thread's, an
update can be silently lost.

**A7.** A parameterized query writes `%s` as a placeholder inside the
SQL string wherever a value belongs, then passes the actual values
separately as a tuple to `cursor.execute(sql, params)`. The driver fills
in each placeholder in a way that always treats the substituted value
strictly as data, never as SQL syntax — this prevents SQL injection,
where untrusted input glued directly into a query string could otherwise
change what the query actually does.

**A8.** A relational row has a fixed schema — every row in the same
table shares the exact same set of columns. A MongoDB document has a
flexible schema — different documents in the same collection can have
entirely different fields, and a field can hold a nested list or nested
document directly, without needing a separate related table.

---

**B1.** `match.group(0)` returns the entire matched text, `"555-1234"`.
`match.group(1)` returns just the first parenthesized group's match,
`"555"`. `match.group(2)` returns the second group's match, `"1234"`.
Groups exist so a pattern can extract specific sub-parts of a match
individually (the area code separately from the rest of the number, for
instance) rather than only getting back the whole matched string and
having to re-parse it manually afterward.

**B2.** The real benefit is memory: a generator-based line-by-line
approach never holds the whole file's contents in memory at once, only
one line (plus whatever small amount of state the processing code
tracks) at any given moment — which matters enormously once a file is
too large to comfortably fit in memory at all (multi-gigabyte log
files, for instance). For a file of only a few megabytes, the practical
difference in memory usage between "load it all into a list" and
"stream it line by line" is small enough that it usually doesn't matter
much either way — the generator approach becomes essential specifically
as file size grows toward or past what comfortably fits in available
memory.

**B3.** This is a classic race condition: `total` is shared, mutable
state that all four threads both read and write, with no lock
coordinating access. Because reading, adding, and writing back is really
three separate steps, one thread's read-modify-write sequence can get
interrupted by another thread's, causing one thread's update to
overwrite another's instead of building on it — silently losing
increments, and losing a different, unpredictable amount depending on
exactly how the threads happen to interleave on a given run. The fix is
to wrap the read-modify-write sequence in `with lock:`, using a shared
`threading.Lock()`, so only one thread can execute that block at a time.

---

**C1.** A correct answer defines a context manager class with
`__enter__` returning `self` and setting up `count`, `__exit__`
returning `False`, a generator function using `yield` to filter and
strip lines lazily, and a `with` block driving iteration over that
generator — for example:

```python
class LineCounter:
    def __init__(self, lines):
        self.lines = lines

    def __enter__(self):
        self.count = 0
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False


def non_blank_lines(lines):
    for line in lines:
        if line.strip():
            yield line.strip()


raw_lines = ["Log start", "", "  ", "Error: disk full", "Done"]
with LineCounter(raw_lines) as lc:
    collected = []
    for line in non_blank_lines(lc.lines):
        lc.count += 1
        collected.append(line)

print(collected, lc.count)
# ['Log start', 'Error: disk full', 'Done'] 3
```

---

## Grading Guidance

| Section | Points | Notes |
|---|---|---|
| A (8 x 2) | 16 | Award partial credit (1 pt) for a mostly-correct answer missing precise terminology. |
| B (3 x 6) | 18 | Full credit requires both identifying the cause AND stating the fix (B3) or the concrete mechanism (B1, B2). |
| C (1 x 6) | 6 | Award full credit for any correct approach; code doesn't need to match the sample exactly, but must genuinely combine a custom context manager and a generator function used together inside a `with` block. |
| **Total** | **40** | 34+ = strong grasp of Module 4; 24-33 = solid but revisit weak areas; below 24 = re-read the relevant chapters before Module 5. |
