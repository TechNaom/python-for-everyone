"""
Chapter 26 Project (Categories 1-2): Production Incident Runbook
See README.md in this folder for full instructions.
Run this from inside the project/ folder: python3 starter.py

Standard library only -- no installs needed.
"""

# The catalog: each entry mirrors one issue card from the Categories
# 1-2 lesson. "keywords" are lowercase substrings the classifier looks
# for in a symptom description.
CATALOG = [
    {
        "id": 1,
        "exception": "KeyError",
        "keywords": ["keyerror", "missing key", "config key", "no such key"],
        "root_cause": "A dict was accessed with [] on a key that isn't present -- often a config/env var missing in this environment.",
        "fix": "Use .get(key, default) for optional keys, or validate all required keys explicitly at startup and fail with a clear message.",
    },
    {
        "id": 2,
        "exception": "IndexError",
        "keywords": ["indexerror", "index out of range", "list index"],
        "root_cause": "A loop bound (often range(n)) assumed a list was at least as long as n, and it wasn't.",
        "fix": "Bound the loop by the list's own length, e.g. range(min(n, len(items))), or slice instead of indexing.",
    },
    {
        "id": 3,
        "exception": "(silent -- no exception)",
        "keywords": ["bare except", "silently returns", "wrong value returned", "no error but wrong"],
        "root_cause": "A bare except: (or overly broad except Exception:) caught an unrelated bug and silently returned a fallback value.",
        "fix": "Catch only the specific exception you expect (e.g. except KeyError:), never a bare except:.",
    },
    {
        "id": 4,
        "exception": "TypeError",
        "keywords": ["typeerror", "unsupported operand", "str and int", "wrong type"],
        "root_cause": "External input (form data, query params) arrived as a string and was passed through several calls before arithmetic failed.",
        "fix": "Convert and validate external input at the boundary where it enters the system, not deep inside business logic.",
    },
    {
        "id": 5,
        "exception": "AttributeError",
        "keywords": ["attributeerror", "nonetype", "has no attribute"],
        "root_cause": "A function implicitly returned None on some code path (no explicit return), and a caller called a method on the result without checking.",
        "fix": "Check for `is None` right where the value comes back, before calling any method on it, or raise a named exception instead of returning None.",
    },
    {
        "id": 6,
        "exception": "(silent -- no exception)",
        "keywords": ["swallowed", "custom exception", "except exception", "insufficientfunds"],
        "root_cause": "A caller's except Exception: caught a specific custom exception too, treating a meaningful failure like a generic one.",
        "fix": "Catch the specific custom exception type and handle it deliberately, instead of catching Exception broadly.",
    },
    {
        "id": 7,
        "exception": "RecursionError",
        "keywords": ["recursionerror", "maximum recursion depth"],
        "root_cause": "A recursive function's base case can be stepped over (e.g. `!= 0` with a starting value that skips past 0) instead of reliably reached.",
        "fix": "Use a base case that can't be skipped, like `<= 0` instead of `!= 0`, or validate input before recursion begins.",
    },
    {
        "id": 8,
        "exception": "ZeroDivisionError",
        "keywords": ["zerodivisionerror", "division by zero"],
        "root_cause": "A denominator sourced from external/variable data (e.g. a count of reviews) was a legitimate 0 that the code never checked for.",
        "fix": "Check the denominator before dividing and return a sensible value (0, None, or a message) for the zero case.",
    },
    {
        "id": 9,
        "exception": "PermissionError",
        "keywords": ["permissionerror", "permission denied"],
        "root_cause": "Code only caught FileNotFoundError, but the file exists and the process lacks OS-level permission to read it -- a different exception entirely.",
        "fix": "Catch FileNotFoundError and PermissionError separately, and handle each differently (missing vs. misconfigured access).",
    },
    {
        "id": 10,
        "exception": "JSONDecodeError",
        "keywords": ["jsondecodeerror", "expecting value", "not valid json"],
        "root_cause": "Code assumed an API response body was always JSON without checking the status code first -- an outage/redirect returned HTML instead.",
        "fix": "Check response.status_code before parsing, and wrap json.loads() in its own try/except for a clear error on non-JSON bodies.",
    },
    {
        "id": 11,
        "exception": "(no exception -- slow)",
        "keywords": ["quadratic", "gets slower as", "scales badly", "membership check slow"],
        "root_cause": "A membership check (`in`) against a list, done repeatedly inside a loop, is O(n) per check -- doing it n times makes the whole function O(n^2).",
        "fix": "Use a set instead of a list for repeated membership checks -- O(1) average case regardless of size.",
    },
    {
        "id": 12,
        "exception": "(no exception -- slow)",
        "keywords": ["insert(0", "insert at the front", "prepend slow"],
        "root_cause": "list.insert(0, x) shifts every existing element over by one -- O(n) per call, O(n^2) total when called n times in a loop.",
        "fix": "Append to the end instead (O(1) amortized), then call .reverse() once at the end if order matters.",
    },
    {
        "id": 13,
        "exception": "(no exception -- slow)",
        "keywords": ["recompute", "recalculating", "redundant work", "repeated lookup slow"],
        "root_cause": "The same expensive computation was repeated for every occurrence of the same input, instead of being computed once and reused.",
        "fix": "Cache results in a dict keyed by whatever determines the result, and only recompute for genuinely new inputs.",
    },
    {
        "id": 14,
        "exception": "(no exception -- slow)",
        "keywords": ["nested loop", "join two lists", "n times m", "times out"],
        "root_cause": "A nested loop scanned an entire second list once per item of the first -- O(n*m) instead of O(n+m).",
        "fix": "Build a dict mapping the join key to record once, up front, then look up each item in O(1) instead of scanning.",
    },
    {
        "id": 15,
        "exception": "(no exception -- slow)",
        "keywords": ["regex slow", "re.search slow", "recompiling"],
        "root_cause": "re.search(pattern, text) re-parses the pattern string internally on every call when the same pattern is reused repeatedly.",
        "fix": "Call re.compile(pattern) once, outside any loop, and reuse the compiled pattern object.",
    },
    {
        "id": 16,
        "exception": "(no exception -- slow)",
        "keywords": ["sorted()[-1]", "sorting just to get", "sort for max"],
        "root_cause": "sorted() is O(n log n) and orders the entire list, even when only the single largest or smallest value is actually needed.",
        "fix": "Use max() or min() for a single extreme value -- O(n), no sorting required.",
    },
    {
        "id": 17,
        "exception": "(no exception -- slow)",
        "keywords": ["len() in loop", "len(items) every iteration"],
        "root_cause": "Calling len() fresh on every iteration of a while loop repeats small, avoidable function-call overhead across every pass.",
        "fix": "Compute len(items) once, store it in a variable before the loop, and check against that instead.",
    },
    {
        "id": 18,
        "exception": "(no exception -- slow)",
        "keywords": ["re-reading the file", "reopening the file", "reading disk repeatedly"],
        "root_cause": "The same file was opened and read from disk once per search term, even though its contents never changed between calls.",
        "fix": "Read the file into memory exactly once, then run every search against that in-memory content.",
    },
    {
        "id": 19,
        "exception": "(no exception -- slow)",
        "keywords": ["materializes", "list comprehension slow", "builds the full list first"],
        "root_cause": "A list comprehension computed every value up front, even though the consuming loop could exit early after finding a match.",
        "fix": "Use a generator expression instead -- values are produced lazily, so unconsumed values are never computed at all.",
    },
    {
        "id": 20,
        "exception": "(no exception -- slow)",
        "keywords": ["dict.keys() slow", "in dict.keys()"],
        "root_cause": "key in some_dict.keys() adds an unnecessary view-object layer -- key in some_dict is already O(1) on its own.",
        "fix": "Drop the .keys() -- check membership directly against the dict.",
    },
    {
        "id": 21,
        "exception": '(no exception -- memory leak)',
        "keywords": ['unbounded cache', 'memory climbs', 'never shrinks', 'cache never evicts'],
        "root_cause": 'Chapter 8 covered dicts as a natural cache: check if a key exists, compute and store it if not. What it didn\'t warn about is that a dict at module scope lives for the entire lifetime of the process -- every distinct user_id ever looked up adds one more entry that\'s never removed, so the cache\'s size is really just "total distinct requests since startup."',
        "fix": 'Bound the cache: use functools.lru_cache(maxsize=...) (issue #29 below), a time-based expiry, or an explicit eviction policy so the cache\'s size reflects "recently useful data," not "everything ever requested."',
    },
    {
        "id": 22,
        "exception": '(no exception -- delayed gc)',
        "keywords": ['reference cycle', 'circular reference', 'gc.collect', 'not destroyed immediately'],
        "root_cause": "Chapter 25 covered that CPython primarily uses reference counting: an object is freed the instant its reference count hits zero. A parent that holds a reference to its child, while the child holds a reference back to its parent, creates a cycle -- each object's count never reaches zero on its own, even after nothing outside the cycle refers to either one. Only the separate, periodic cyclic garbage collector (gc) can break cycles like this, and it doesn't run instantly.",
        "fix": 'Break the cycle deliberately -- store the child-to-parent link as a weakref.ref instead of a normal reference (issue #30 below takes this further), so the parent can still be freed by simple reference counting the moment nothing outside the cycle needs it.',
    },
    {
        "id": 23,
        "exception": '(no exception -- memory leak)',
        "keywords": ['event listener leak', 'never unregistered', 'widget stays alive', 'subscriber never removed'],
        "root_cause": "Chapter 10 covered passing functions (including bound methods) as values. Subscribing self._on_event to an EventBus hands the bus a reference to the method -- which keeps self alive too, since a bound method holds a reference to its instance. The caller can drop every other reference to a Widget, but as long as the bus's subscriber list still references its callback, the whole widget (and everything it holds, like self.data) stays alive.",
        "fix": 'Provide (and actually call) an unsubscribe()/disconnect() method when an object is done with an event bus -- or have the bus hold subscribers as weakrefs so a widget with no other references can still be collected even if it forgot to unsubscribe.',
    },
    {
        "id": 24,
        "exception": '(no exception -- memory leak)',
        "keywords": ['closure captures', 'grows forever', 'history never trimmed', 'closure memory'],
        "root_cause": "Chapter 9 covered closures: the inner log_request() function captures history from its enclosing scope and keeps a live reference to it. That's the entire point of a closure -- but it means history lives exactly as long as log_request itself does, which here is the whole program, and nothing ever trims it.",
        "fix": "Cap history's size explicitly (e.g. a collections.deque(maxlen=1000) instead of a plain list), or don't accumulate history in the closure at all -- write each entry somewhere with its own retention policy (a log file, a database) instead of an ever-growing in-memory list.",
    },
    {
        "id": 25,
        "exception": '(no exception -- memory leak)',
        "keywords": ['recent errors list', 'never actually recent', 'unbounded list', 'grows without bound'],
        "root_cause": 'Chapter 4 and 5 covered append() as the basic way to build up a list -- but nothing about append() automatically implies a size limit. The name recent_errors describes an intent, not an actual constraint the code enforces; every batch adds more entries, and the list quietly becomes "every error since the process started," not "recent" ones.',
        "fix": 'Use a bounded structure that enforces the intent in code, not just in the variable\'s name -- collections.deque(maxlen=500) automatically drops the oldest entry once it\'s full, so "recent" stays true no matter how long the process runs.',
    },
    {
        "id": 26,
        "exception": 'OSError',
        "keywords": ['too many open files', 'file handles', 'never closed', 'file descriptor'],
        "root_cause": 'Chapter 13 covered open() and the with statement for automatic cleanup -- but this code opens a file, does not use with, and additionally stores the handle in a list "to flush them all at shutdown." Each open file consumes one of the operating system\'s limited file-descriptor slots per process; without an explicit close(), those slots are never returned.',
        "fix": "Always use with open(...) as f: so the file is closed automatically the moment the block exits, even if an exception happens inside it -- and avoid keeping long-lived references to open file objects unless there's a real reason the file needs to stay open.",
    },
    {
        "id": 27,
        "exception": '(no exception -- shared state bug)',
        "keywords": ['mutable class attribute', 'shared by every instance', 'class-level list'],
        "root_cause": "Chapter 14 covered the difference between a class attribute (defined directly in the class body, shared by every instance) and an instance attribute (assigned via self.x = ... in __init__, unique per instance). history = [] written at class level is a class attribute -- there's exactly one list object, and every instance's self.history resolves to that same shared list unless an instance explicitly overrides it. This is the class-level cousin of the mutable-default-argument bug (issue #41 in Category 5).",
        "fix": 'Create the mutable list inside __init__ as an instance attribute -- self.history = [] -- so each instance gets its own fresh list instead of sharing one across the entire class.',
    },
    {
        "id": 28,
        "exception": '(no exception -- memory leak)',
        "keywords": ['just in case', 'results list never released', 'retained rows', 'grows in a straight line'],
        "root_cause": 'Chapter 25 covered measuring what a program actually holds in memory at once. Here, every batch\'s rows are appended to all_rows_seen "in case a report needs to look back," and the running average is recomputed over the entire history on every batch -- so both the memory and the work grow without bound, for a feature that\'s speculative at best.',
        "fix": "Only keep what's actually needed going forward: a running total and count (two numbers) produce the same average without retaining a single row, or persist historical data somewhere with its own storage and retention policy instead of an in-memory Python list.",
    },
    {
        "id": 29,
        "exception": '(no exception -- memory leak)',
        "keywords": ['lru_cache no maxsize', 'unbounded lru_cache', 'cache never hits', 'zero cache hits'],
        "root_cause": "Chapter 25's caching guidance applies just as much to functools.lru_cache as to a hand-rolled dict: maxsize=None means unbounded. Caching only pays off when the same input recurs; here every image_id is a one-off (a fresh upload), so the cache never gets a hit -- it just accumulates one new entry per request, forever, with zero benefit.",
        "fix": "Set a concrete maxsize so the cache evicts old entries once full (issue #21's fix, applied via the standard library this time) -- and more importantly, verify the access pattern actually has repeats before adding a cache at all. A cache on non-repeating input is pure memory overhead with no upside.",
    },
    {
        "id": 30,
        "exception": '(no exception -- memory leak)',
        "keywords": ['registry keeps alive', 'session registry', 'weakvaluedictionary', 'keeps objects alive'],
        "root_cause": 'A plain dict holds a strong reference to every value it contains -- that\'s normal dict behavior, and usually exactly what\'s wanted. But a registry whose entire job is "let me look this up if it still exists" doesn\'t need to be the thing keeping it alive; here, every Session the caller creates and discards stays alive anyway, purely because the registry still references it.',
        "fix": 'Use weakref.WeakValueDictionary instead of a plain dict when a collection\'s purpose is tracking, not owning -- entries disappear automatically the moment nothing else references the value, which is usually the actual intent of a "registry."',
    },
    {
        "id": 31,
        "exception": '(no exception -- race condition)',
        "keywords": ['race condition', 'shared counter', 'lost update', 'no lock'],
        "root_cause": "Chapter 20 covered starting and joining threads, but counter += 1 is not one atomic step -- it's read counter, add 1, write the result back. If two threads both read the same value before either writes its update back, one thread's increment is silently lost. Python's GIL (Global Interpreter Lock) prevents two threads from running Python bytecode at the exact same instant, but it does not prevent a thread from being switched out in the middle of a multi-step operation like this one -- which is exactly where the race lives.",
        "fix": 'Protect the read-modify-write with a threading.Lock (issue #40 below) so only one thread can execute that sequence at a time -- turning three separate steps back into one effectively atomic one.',
    },
    {
        "id": 32,
        "exception": '(hang -- deadlock)',
        "keywords": ['deadlock', 'two locks', 'different orders', 'hangs forever'],
        "root_cause": "transfer_a_to_b() acquires lock_a then lock_b; transfer_b_to_a() acquires lock_b then lock_a -- the opposite order. If both threads grab their first lock at roughly the same time, each ends up waiting forever for the lock the other thread is holding. Neither thread can proceed, and neither will ever release what it's holding, since the release happens only after the wait -- a classic deadlock.",
        "fix": 'Establish one global ordering for acquiring locks (e.g. always sort accounts by ID and lock the lower one first) and have every code path follow it -- if both functions always acquired lock_a before lock_b, the deadlock in this exact shape becomes structurally impossible.',
    },
    {
        "id": 33,
        "exception": '(no exception -- no speedup)',
        "keywords": ['threading cpu-bound', 'gil', 'no speedup', 'expecting a speedup'],
        "root_cause": "Chapter 20 covered that CPython's GIL allows only one thread to execute Python bytecode at a time, no matter how many CPU cores are available. Threading genuinely helps when threads spend most of their time waiting (for a network response, for disk I/O) -- the GIL is released during that wait. A tight pure-Python loop like count_down() never waits for anything; it's 100% CPU-bound Python bytecode, so the GIL keeps the two threads running one at a time, exactly as if they'd run sequentially (plus a bit of thread-switching overhead).",
        "fix": 'For CPU-bound work, use multiprocessing instead of threading -- separate processes each get their own Python interpreter and their own GIL, so they genuinely run in parallel across cores. Reserve threading for I/O-bound work, where waiting (not computing) is most of what a thread does.',
    },
    {
        "id": 34,
        "exception": '(no exception -- stale result)',
        "keywords": ['forgot to join', 'missing join', 'results empty', 'thread not joined'],
        "root_cause": 'Chapter 20 covered thread.start() as non-blocking: it schedules the thread to run and returns immediately, without waiting for it to finish. run_batch_missing_join() starts three threads but never calls t.join() on any of them -- so it returns before any of the threads have necessarily completed their time.sleep(0.3) plus computation, and results is still empty at that moment.',
        "fix": 'Call t.join() on every thread the function started before reading anything those threads were supposed to produce -- join() blocks until that specific thread has actually finished, which is the whole point of it.',
    },
    {
        "id": 35,
        "exception": '(hang -- no shutdown signal)',
        "keywords": ['producer consumer', 'queue hangs', 'no sentinel', 'never exits'],
        "root_cause": 'Chapter 20\'s threading model extends naturally to queue.Queue for producer/consumer patterns -- but q.get() blocks by default when the queue is empty, waiting for the next item to arrive. The producer here puts three items and then simply stops, with no mechanism telling the consumer "that was the last one." The consumer\'s while True: q.get() is left waiting on a fourth item that will never come.',
        "fix": "Have the producer put a sentinel value (like None) onto the queue once it's done, and have the consumer break its loop when it sees that sentinel -- or use q.join()/task_done() together with a separate shutdown signal so the consumer knows precisely when to stop waiting.",
    },
    {
        "id": 36,
        "exception": 'IndexError',
        "keywords": ['check-then-act', 'pop from empty list', 'shared list threads', 'race on list'],
        "root_cause": "The check (if not shared_queue) and the act (shared_queue.pop()) are two separate steps, and nothing stops another thread from running its own pop in between them. Thread A can see a non-empty list, get interrupted, and by the time it actually calls .pop(), thread B has already emptied it -- the check was true when made, but false by the time it's acted on.",
        "fix": 'Make the check-and-pop a single atomic operation instead of two separate steps -- wrap both in the same with lock: block, or catch IndexError around the pop() and treat it as "someone else got there first" rather than a fatal error.',
    },
    {
        "id": 37,
        "exception": '(hang -- self deadlock)',
        "keywords": ['lock not reentrant', 'deadlocks against itself', 'same thread', 'plain lock re-acquire'],
        "root_cause": "A plain threading.Lock doesn't track which thread holds it -- once acquired, any further attempt to acquire it blocks, even from the exact same thread that's already holding it. outer() acquires lock, then calls inner(), which tries to acquire the same lock again from within the same thread -- and blocks waiting for itself to release something it's currently holding.",
        "fix": 'Use threading.RLock (a re-entrant lock) when the same thread legitimately needs to acquire the same lock more than once, such as one locked method calling another -- an RLock tracks the owning thread and lets it re-acquire without blocking on itself.',
    },
    {
        "id": 38,
        "exception": '(no exception -- swallowed)',
        "keywords": ['future exception', 'threadpool exception swallowed', 'never surfaced', 'result() never called'],
        "root_cause": "A concurrent.futures.Future captures an exception raised inside its worker function rather than letting it propagate immediately -- it's stored on the Future object, waiting to be re-raised the moment someone calls .result(). If nothing ever calls .result() on a given future, that captured exception is simply never looked at again.",
        "fix": 'Always call .result() on every Future a pool produces (or iterate with concurrent.futures.as_completed() and call .result() on each) so any exception a worker raised gets re-raised where it can actually be seen and handled.',
    },
    {
        "id": 39,
        "exception": 'RuntimeError',
        "keywords": ['dictionary changed size during iteration', 'mutate dict threads', 'iterate while mutating'],
        "root_cause": "Chapter 8 covered that mutating a dict's size while iterating it is unsafe -- that rule doesn't go away just because the mutation happens on a different thread. While report_active_sessions() iterates sessions.items(), expire_old_sessions() deletes keys from the very same dict on another thread; Python detects the dict's size changed mid-iteration and raises, rather than silently producing a wrong count.",
        "fix": 'Protect the shared dict with a threading.Lock that both the reader and the writer acquire, or take a snapshot (list(sessions.items())) while holding the lock briefly, then release the lock and iterate the snapshot instead of the live dict.',
    },
    {
        "id": 40,
        "exception": '(no exception -- fixed with lock)',
        "keywords": ['lock fixes race', 'threading.lock', 'read-modify-write protected'],
        "root_cause": "Issue #31's counter += 1 was unsafe specifically because it's three separate steps that another thread can interleave with. Wrapping those same three steps in with lock: means only one thread can be inside that block at any moment -- any other thread calling increment_safe() simply waits at the with lock: line until the current holder finishes and releases it.",
        "fix": "This is the fix -- a threading.Lock acquired around the entire read-modify-write sequence, released automatically (even on an exception) by the with statement, matching Chapter 12's with-block cleanup guarantee.",
    },
    {
        "id": 41,
        "exception": '(no exception -- data corruption)',
        "keywords": ['mutable default argument', 'shared cart', 'default value evaluated once'],
        "root_cause": "Chapter 10 covered default argument values -- what it's easy to miss is that a default value is evaluated exactly once, when the def statement runs, not fresh on every call. cart=[] creates one single list object at function-definition time; every call that doesn't pass its own cart argument gets that same object, and any mutation (like .append()) persists onto the next such call.",
        "fix": 'Use cart=None as the default, and create a fresh list inside the function body when cart is None -- def add_item(item, cart=None): cart = [] if cart is None else cart. This is one of the most well-known Python gotchas precisely because the code reads as obviously correct until you know to look for it.',
    },
    {
        "id": 42,
        "exception": '(no exception -- data corruption)',
        "keywords": ['shallow copy', 'deep copy', 'dict.copy() shares', 'nested list shared'],
        "root_cause": 'Chapter 8 and Chapter 15 covered dict.copy() as a shallow copy: it creates a new dict, but each value inside it is the same object as in the original, not a new copy of that value. Reassigning a key (order_a["status"] = "shipped") only affects the new dict, because that replaces which object the key points to. But mutating a shared nested object in place (order_a["items"].append(...)) changes the one list both dicts are still pointing at.',
        "fix": 'Use copy.deepcopy() when a copy needs to be fully independent, including everything nested inside it -- it recursively copies every mutable value, not just the top-level container, so mutating the copy never touches the original.',
    },
    {
        "id": 43,
        "exception": '(no exception -- wrong comparison)',
        "keywords": ['float equality', 'comparing floats', 'floating-point', '== on floats'],
        "root_cause": "Chapter 2 introduced floats; what it's easy to gloss over is that most decimal fractions (including something as simple as 0.1) can't be represented exactly in binary floating point -- the same way 1/3 can't be written exactly in decimal. Each addition accumulates a tiny rounding error, and after ten additions, the result is off from 1.0 by a sliver too small to see when printed casually, but large enough that == reports False.",
        "fix": 'Never compare floats for exact equality when they result from arithmetic -- use math.isclose(a, b) for a tolerance-based comparison, or use decimal.Decimal instead of float entirely for money, where exact decimal representation actually matters.',
    },
    {
        "id": 44,
        "exception": '(no exception -- silent truncation)',
        "keywords": ['silent truncation', 'int() truncates', 'fractional quantity lost'],
        "root_cause": 'Chapter 2 covered int() as a way to convert to an integer -- what it didn\'t stress is that int() truncates toward zero rather than rounding, and does so completely silently. int(float("4.9")) doesn\'t round to 5; it discards everything after the decimal point and returns 4, with nothing in the output to suggest data was thrown away.',
        "fix": 'Decide deliberately what fractional quantities should mean before converting -- round() if the nearest whole number is correct, an explicit validation error if fractional units should never be allowed at all, or keep the value as a float/Decimal if fractions are actually meaningful data, rather than letting int() make that decision implicitly.',
    },
    {
        "id": 45,
        "exception": 'UnicodeDecodeError',
        "keywords": ['wrong encoding', 'cp1252', 'csv encoding', 'unicodedecodeerror'],
        "root_cause": "Chapter 13 covered reading files with open(), defaulting (on most platforms) to UTF-8. Many Windows tools instead save text as cp1252 (Windows-1252), which encodes accented characters using different byte sequences than UTF-8 does. Opening a cp1252 file while assuming UTF-8 means the decoder eventually hits a byte sequence that isn't valid UTF-8 and has no way to guess what it was actually supposed to mean.",
        "fix": 'Know (or detect) the actual encoding of files coming from outside your own system, and pass it explicitly: open(path, encoding="cp1252"). When the true encoding is genuinely unknown, a library like chardet can guess from the byte patterns, but "just assume UTF-8" silently breaks the moment that assumption is wrong.',
    },
    {
        "id": 46,
        "exception": '(no exception -- dropped records)',
        "keywords": ['off-by-one pagination', 'silently drops records', 'page_number', 'pagination bug'],
        "root_cause": 'Chapter 6 and Chapter 7 covered slicing as zero-based -- records[0:10] is the first ten items. This API\'s page_number is 1-based (page 1 is the first page, matching how a human thinks about it), but the slicing math treats it as if it were already 0-based: start = page_number * page_size computes 1 * 10 = 10 for "page 1," which is actually where the second page of results starts.',
        "fix": 'Convert the 1-based page number to a 0-based offset explicitly before slicing: start = (page_number - 1) * page_size. Writing a quick unit test for "page 1 includes the very first record" would have caught this immediately -- it\'s exactly the kind of boundary case Chapter 12-adjacent testing habits are meant to cover.',
    },
    {
        "id": 47,
        "exception": '(no exception -- wrong column order)',
        "keywords": ['dict key order', 'column order', 'csv export wrong order'],
        "root_cause": 'Chapter 8 covered that modern Python dicts preserve insertion order -- a real, documented guarantee since Python 3.7. The bug here isn\'t that the guarantee is false; it\'s relying on it for something it was never meant to guarantee: which order a dict\'s keys end up in depends entirely on the order they were first assigned, which can differ between two code paths that build "the same" record from different sources.',
        "fix": "Never rely on a dict's insertion order to imply a fixed column layout -- explicitly list the field order once (e.g. a tuple of column names) and build every row by looking up each field from that fixed list: [record[field] for field in COLUMN_ORDER], so all rows are aligned regardless of how each record was originally built.",
    },
    {
        "id": 48,
        "exception": '(no exception -- lookup fails)',
        "keywords": ['unicode normalization', 'visually identical strings', 'nfc', 'combining accent'],
        "root_cause": 'Chapter 6 covered strings as sequences of characters, but some accented characters can be represented two different ways in Unicode: as one single "precomposed" code point, or as a plain letter followed by a separate combining accent mark. Both render identically on screen, but they are different sequences of code points -- different lengths, even -- so Python\'s == correctly reports them as unequal strings.',
        "fix": 'Normalize any text that crosses a system boundary (typed by a user, read from a file, received from an API) to one consistent Unicode form -- typically NFC -- using unicodedata.normalize("NFC", text), before comparing it or storing it as a lookup key.',
    },
    {
        "id": 49,
        "exception": '(no exception -- silent wraparound)',
        "keywords": ['silent wraparound', 'fixed-width field', 'bitmask overflow', '0xffffffff'],
        "root_cause": "Chapter 3 covered bitwise operators including and. Masking a value with and 0xFFFFFFFF keeps only its lowest 32 bits -- for any value that already fits in 32 bits, this is a no-op. But for a value that exceeds 2^3^2 - 1 (4,294,967,295), the higher bits are silently discarded, producing a completely different, smaller number with no error or warning of any kind -- unlike issue #4's TypeError, this is a valid Python int operation the whole way through.",
        "fix": "Validate the value's range before masking or packing it into a fixed-width field, and raise an explicit error (or widen the field) when it doesn't fit -- Python's own integers have no size limit, so this kind of overflow only happens at a boundary you construct yourself, and only that boundary can catch it.",
    },
    {
        "id": 50,
        "exception": '(no exception -- byte limit exceeded)',
        "keywords": ['byte limit', 'character count vs bytes', 'varchar too long', 'utf-8 bytes'],
        "root_cause": 'Chapter 6 covered len() on a string as the number of characters. Many database column types (a fixed-width VARBINARY, or VARCHAR under certain encodings) actually enforce a limit in bytes, not characters. Once text is encoded to UTF-8, characters outside the basic ASCII range take up 2, 3, or 4 bytes each -- so a 10-character string can easily be 12+ bytes, silently exceeding a byte-based limit that a character-based truncation never accounted for.',
        "fix": 'Know which unit a given limit is actually measured in, and truncate accordingly -- for a byte limit, encode first, truncate the bytes (carefully, so as not to split a multi-byte character in half), then decode back, rather than truncating the original string by character count and hoping it happens to fit.',
    },
    {
        "id": 51,
        "exception": 'SyntaxError',
        "keywords": ['python version', 'newer language feature', 'match/case', 'works on my machine'],
        "root_cause": "Python's standard library and syntax both grow over time -- structural pattern matching (match/case) arrived in 3.10; tomllib became part of the standard library only in 3.11. Code written and tested on a developer's up-to-date local Python has no way to know that a production server, provisioned from an older base image, is running a version from before that feature existed.",
        "fix": 'Pin the exact Python version in a .python-version file (or the container base image tag) and match it across every environment -- local, CI, and production -- so "works on my machine" and "works in production" are testing the same interpreter, not just the same source code.',
    },
    {
        "id": 52,
        "exception": '(no exception -- broke on deploy)',
        "keywords": ['unpinned dependency', 'requirements.txt', 'no version specified', 'worked yesterday'],
        "root_cause": 'Chapter 11 covered installing packages, but a requirements.txt line like requests (no version specified) doesn\'t mean "the version I tested with" -- it means "whatever the newest compatible version is, at the exact moment pip install runs." A library\'s new release, even a routine one, can change default behavior, deprecate something the code relies on, or pull in its own updated (and possibly incompatible) sub-dependencies.',
        "fix": 'Pin exact versions (requests==2.31.0) or use a lockfile-based tool (pip-tools, poetry, uv) that records the exact resolved version of every dependency, direct and transitive, so every install -- local, CI, or production -- gets identical package versions.',
    },
    {
        "id": 53,
        "exception": 'KeyError',
        "keywords": ['environment variable missing', 'os.environ', 'set locally but not in production'],
        "root_cause": "This is issue #1's KeyError pattern, but the missing key lives in os.environ instead of a plain dict. A developer's shell profile or a local .env file quietly exports variables like PAYMENT_API_KEY every time a terminal opens -- a freshly provisioned production container has no such setup unless someone explicitly configured that variable in the deployment platform.",
        "fix": "Validate all required environment variables at startup, before the service accepts any traffic, and fail with a clear message naming exactly which variable is missing (echoing issue #1's fix) -- that turns a runtime KeyError deep in request-handling code into an immediate, unambiguous deployment failure.",
    },
    {
        "id": 54,
        "exception": 'FileNotFoundError',
        "keywords": ['relative file path', 'working directory', 'cron job', 'systemd'],
        "root_cause": "Chapter 13 covered open() with a relative path -- what's easy to miss is that a relative path is resolved against the process's current working directory, not against the location of the script file itself. A developer's habit of always running python app.py from inside the project folder makes the working directory always happen to line up; a systemd unit or cron job has no such habit and typically defaults to a different directory entirely (often / or the user's home directory).",
        "fix": "Build paths relative to the script's own location using pathlib.Path(__file__).resolve().parent, rather than relying on whatever the current working directory happens to be at launch -- that makes the code's file access independent of how or from where it's started.",
    },
    {
        "id": 55,
        "exception": '(no exception -- wrong time)',
        "keywords": ['naive datetime', 'timezone', 'different moment', 'fires at the wrong time'],
        "root_cause": 'datetime(2026, 7, 9, 9, 0, 0) with no timezone attached is a naive datetime -- it represents "9 o\'clock" without saying 9 o\'clock where. A developer\'s laptop, set to their local timezone, and a production server, very often configured for UTC, will interpret that exact same naive value as two different real moments in time, hours apart.',
        "fix": "Use timezone-aware datetimes everywhere a specific moment in time matters -- attach tzinfo=timezone.utc (or the specific zone via zoneinfo) explicitly, so the same datetime object means the same real moment no matter which machine's local settings are evaluating it.",
    },
    {
        "id": 56,
        "exception": 'PermissionError',
        "keywords": ['locked-down server', 'fresh server permissions', 'file write fails'],
        "root_cause": "This is issue #9's distinction (FileNotFoundError vs. PermissionError) showing up at deployment time instead of at request time. A developer's local machine or an old server, set up manually over time, often accumulates permissive file permissions on its working directories. A freshly provisioned server -- especially one built from a hardened base image -- may create that same directory with much stricter default permissions, denying write access to the process's user.",
        "fix": 'Explicitly set required permissions as part of the deployment process (a Dockerfile RUN chmod/chown step, an infrastructure-as-code rule) rather than relying on whatever a server happens to default to -- permissions should be declared and version-controlled, not discovered by trial and error after a migration.',
    },
    {
        "id": 57,
        "exception": '(no exception -- info disclosure)',
        "keywords": ['debug=true', 'debug mode production', 'stack trace exposed'],
        "root_cause": "Web frameworks like Flask and FastAPI (Chapter 22) offer a debug mode specifically to help local development: it shows detailed tracebacks in the browser and, in some frameworks, even exposes an interactive in-browser debugger console. That's an enormous convenience while developing locally, and an equally enormous information disclosure risk (internal hostnames, file paths, sometimes even a remote code execution surface via the interactive console) if the exact same flag ships unchanged to a publicly reachable production deployment.",
        "fix": 'Drive debug mode from an environment variable that defaults to False/off, and never hardcode debug=True directly in application code that also runs in production -- treat "is this environment allowed to show internals to the client" as a deployment-time decision, not a code-time one.',
    },
    {
        "id": 58,
        "exception": 'ConnectionRefusedError',
        "keywords": ['hardcoded localhost', 'connection refused', 'database url hardcoded'],
        "root_cause": 'On a developer\'s machine, localhost genuinely does have a database server running -- installed locally, or running in a local Docker container mapped to that port. "localhost" hardcoded into source code isn\'t a placeholder that gets swapped out; it\'s a literal value that means exactly the same thing everywhere it runs. In a production container, "localhost" refers to the container itself, which has no database server running inside it -- the real database is a separate host entirely.',
        "fix": 'Read connection details from configuration (environment variables, a config file injected at deploy time) rather than hardcoding them -- the exact same pattern as issue #1 and #53: values that differ by environment belong in configuration, not in source code.',
    },
    {
        "id": 59,
        "exception": '(exception at import time)',
        "keywords": ['import fails before config', 'sdk import side effect', 'config not loaded yet'],
        "root_cause": "Chapter 11 covered that a module's code runs once, at first import, top to bottom -- including any setup logic the module's own author put at import time. Some SDKs (particularly ones that validate credentials, open connections, or read config as soon as they're imported) fail immediately if their required setup isn't ready yet. Placing that import at the very top of a file, before the application's own environment/config loading step has run, means the SDK's import-time check can run before the very thing it needs has been set up.",
        "fix": 'Load and validate configuration first, at the very top of the entry point, before importing anything whose own import has side effects that depend on that configuration -- or better, prefer libraries that defer their setup to an explicit init()/configure() call rather than doing it implicitly at import time.',
    },
    {
        "id": 60,
        "exception": 'ModuleNotFoundError',
        "keywords": ['only imports in ide', 'sys.path', 'works in editor not terminal'],
        "root_cause": "Chapter 11 covered how Python resolves imports by searching sys.path. Many IDEs and editors automatically add a project's src/ folder to sys.path (via a workspace setting, a .pth file, or an editable install) as a convenience -- entirely invisibly to the developer, who never has to think about it. A bare python scripts/deploy_check.py, run from a plain shell on a server with none of that IDE tooling present, has no such convenience: src/ was never added to the path, so the import genuinely can't find the package.",
        "fix": "Don't depend on IDE-specific path magic for anything that needs to run outside the IDE -- install the project properly (pip install -e .) so the package is genuinely importable everywhere, or set PYTHONPATH explicitly as part of how the script is invoked in deployment.",
    },
    {
        "id": 61,
        "exception": '(security -- SQL injection)',
        "keywords": ['sql injection', 'string-formatted query', "or '1'='1"],
        "root_cause": "Chapter 21 covered running SQL from Python, but building the query with an f-string means the username value becomes literal SQL text, not data. An input like ' OR '1'='1 closes the string literal early and adds a condition that's always true -- turning WHERE username = '' into WHERE username = '' OR '1'='1', which matches every row in the table. This is the single most well-known real-world security vulnerability class, and it comes directly from mixing code and data.",
        "fix": 'Always use parameterized queries -- pass values as separate arguments (conn.execute(query, (username,))) rather than formatting them into the SQL string. The database driver handles escaping correctly, and a malicious value can never be interpreted as part of the SQL structure.',
    },
    {
        "id": 62,
        "exception": '(no exception -- pool exhausted)',
        "keywords": ['connection pool exhausted', 'too many connections', 'connection never returned'],
        "root_cause": "Chapter 21's pattern of opening a connection and doing work with it has a step that's easy to skip under pressure: releasing the connection back to the pool when done. A connection pool has a fixed maximum size; every call that checks one out without ever checking it back in permanently reduces the pool's effective capacity by one, until nothing is left to hand out to the next caller.",
        "fix": "Always release (or close) a connection in a finally block or, better, a with block -- so it's returned to the pool no matter whether the code using it succeeded or raised an exception partway through.",
    },
    {
        "id": 63,
        "exception": '(no exception -- slow)',
        "keywords": ['n+1 query', 'one query per row', '151 total queries'],
        "root_cause": "This is Category 2's nested-loop pattern (issue #14), but expressed as database round-trips instead of in-memory list scans: one query fetches all the books, and then a separate query fetches each book's author, one at a time, inside a loop. For 150 books, that's 151 total queries -- and every query is a full network round-trip to the database, which is far slower than any in-memory operation.",
        "fix": 'Use a JOIN to fetch books and their authors together in a single query -- the database is specifically built to do this kind of combination efficiently, in one round-trip, rather than paying network latency once per row.',
    },
    {
        "id": 64,
        "exception": 'KeyError',
        "keywords": ['429', 'rate limit', 'retry-after', 'rate-limited response'],
        "root_cause": 'Chapter 19 covered parsing a JSON response body, but assumed every response has the same shape. Once an API\'s rate limit is exceeded, it typically returns a 429 status with a completely different body (an error description, not the requested data) -- code that reaches straight for response.json()["data"] without first checking the status code has no way to distinguish a successful response from a rate-limited one until the KeyError happens.',
        "fix": "Check the status code before trusting the response body's shape, and implement a retry with exponential backoff specifically for 429s (many APIs also return a Retry-After header telling you exactly how long to wait) -- rather than assuming every response that comes back is the one that was asked for.",
    },
    {
        "id": 65,
        "exception": '(hang -- no timeout)',
        "keywords": ['no timeout', 'hangs forever', 'network call stuck', 'hung request'],
        "root_cause": "A network call with no timeout configured will wait indefinitely for a response, by design -- that's the default behavior of raw sockets and most HTTP client libraries unless a timeout is explicitly requested. If the remote server is overloaded, or a firewall silently drops the packets rather than actively refusing the connection, there is nothing to make the call fail on its own; it just waits, forever, holding whatever resources (a thread, a connection) it was using.",
        "fix": 'Always set an explicit timeout on any network call -- a deliberately failed request that can be retried or reported is always better than a silently hung one. Most production incidents involving a "stuck" service trace back to exactly this: one downstream call with no timeout, upstream of everything else.',
    },
    {
        "id": 66,
        "exception": '(no exception -- double charge)',
        "keywords": ['double-charging', 'retry non-idempotent', 'charged twice'],
        "root_cause": 'Chapter 12 covered retrying operations after a failure -- but retrying is only safe when the operation is idempotent, meaning doing it twice has the same effect as doing it once. A payment charge is not naturally idempotent: if the server-side charge succeeded but the response was lost on the way back (a timeout, a dropped connection), the client has no way to know that, and blindly retrying the same request charges the customer a second time for what the client believes is still a single failed attempt.',
        "fix": 'Attach a unique idempotency key to the request (generated once per logical operation, reused on every retry) so the server can recognize "I\'ve already processed this exact request" and return the original result instead of charging again -- most real payment APIs (Stripe, for example) support this pattern natively.',
    },
    {
        "id": 67,
        "exception": 'TypeError',
        "keywords": ['trusting api response', 'null field', 'unvalidated response', 'temperature_c none'],
        "root_cause": 'Chapter 19 covered parsing JSON responses, but not every field in a real API\'s response is guaranteed to be populated -- a weather API might legitimately return null/None for a temperature it couldn\'t determine. Code that does arithmetic directly on a field pulled from a response (forecast["temperature_c"] * 9 / 5 + 32) is implicitly assuming that field is always a usable number, which the API itself never actually promised.',
        "fix": 'Validate response data at the boundary where it enters the system -- check for None (or use a schema-validation library like pydantic) before doing anything that assumes a specific type, and decide explicitly what should happen when a field is missing or unusable, rather than letting the first arithmetic operation on it decide by crashing.',
    },
    {
        "id": 68,
        "exception": '(exception -- connection closed)',
        "keywords": ['connection already closed', 'reusing closed connection', 'connection invalidated'],
        "root_cause": "Code held onto a database connection object across a period during which something else (a connection pool recycling it, a restart, an explicit .close() call elsewhere in the codebase) invalidated it. Once a connection is closed, it stays closed -- there's no automatic reconnection, and every operation attempted on it afterward fails immediately, since the underlying resource it wraps genuinely no longer exists.",
        "fix": "Don't hold long-lived references to a single connection object across a function or module's entire lifetime -- acquire a fresh connection (or one from a pool) for each unit of work, or wrap database access in a helper that detects a closed/invalid connection and transparently reconnects.",
    },
    {
        "id": 69,
        "exception": '(no exception -- not committed)',
        "keywords": ['never committed', 'conn.commit', 'write not visible', 'transaction not committed'],
        "root_cause": "Chapter 21 covered running an UPDATE statement, but a database transaction isn't visible to other connections until it's explicitly committed. Without conn.commit(), the change exists only inside this specific connection's pending transaction -- correct as far as this connection is concerned, invisible to everyone else, and vulnerable to being silently lost entirely if the connection is dropped before a commit ever happens.",
        "fix": "Always call conn.commit() after a write that should actually persist -- many ORMs and frameworks handle this automatically at the end of a request, but raw sqlite3/psycopg2-style code has to do it explicitly, and it's easy to forget on a code path that isn't exercised by casual manual testing.",
    },
    {
        "id": 70,
        "exception": '(no exception -- wrong interpretation)',
        "keywords": ['api call failed vs not exist', 'broad except dependency', 'out of stock incorrectly'],
        "root_cause": 'This is issue #6\'s broad-except pattern, applied to a dependency instead of a business-logic exception. Catching Exception broadly around an API call and returning False ("not in stock") on any failure conflates two completely different situations: "the inventory service says this item has zero stock" and "the inventory service is unreachable and we have no idea." Both produce the exact same user-facing result, even though only one of them is actually true.',
        "fix": 'Distinguish a definitive answer from a failure to get an answer -- catch the specific exception type a downed dependency raises, and respond differently: show a "temporarily unable to check availability" state, use a cached last-known value, or fail the request loudly, rather than silently reinterpreting "unknown" as "no."',
    },
    {
        "id": 71,
        "exception": '(no exception -- missing logs)',
        "keywords": ['print instead of logging', 'nothing in the log aggregator', 'stdout vs logging'],
        "root_cause": "print() writes to standard output; the logging module writes through a configurable pipeline of handlers, levels, and formatters. In many real deployments those two things are captured completely differently -- stdout might go to a container's raw log stream while the actual logging pipeline ships to a searchable aggregator (or vice versa). And separately, logging.info() calls are silently dropped entirely if the effective log level (default: WARNING) is set above INFO.",
        "fix": "Use the logging module everywhere in application code, never print(), so every message flows through one consistent, configurable pipeline -- and explicitly configure the logging level appropriate for each environment (more verbose in development, less in production) rather than relying on the library's default.",
    },
    {
        "id": 72,
        "exception": '(security -- secrets logged)',
        "keywords": ['secrets logged', 'password in logs', 'plaintext token logged'],
        "root_cause": 'A debug-friendly log line that dumps "the whole request context" is convenient while actively troubleshooting -- it\'s also indiscriminate. It has no concept of which fields are sensitive, so a password or API token passed through the same function as an ordinary username gets logged with exactly the same lack of ceremony, and log files are typically retained (and searchable) far longer than anyone consciously decided they should be.',
        "fix": 'Never log raw credentials, tokens, or other secrets -- redact or omit sensitive fields explicitly before logging (password=***), and treat "does this log line contain anything sensitive" as a required check during code review, not an afterthought caught only by a later security audit.',
    },
    {
        "id": 73,
        "exception": '(no exception -- untraceable)',
        "keywords": ['no correlation id', "can't be traced", 'logs interleave'],
        "root_cause": 'Each function in the pipeline logs its own step ("validating payment," "reserving inventory") with no identifier tying that specific log line back to the specific order it was processing. When multiple orders are processed around the same time -- concurrently, or just close together -- their log lines interleave in the output with nothing to distinguish which line belongs to which logical operation.',
        "fix": 'Generate a unique correlation ID (or request ID) at the start of each logical operation, and include it in every log line produced anywhere during that operation -- then any log aggregator can filter to "everything that happened for order-102" with a single search, regardless of how many other operations were interleaved in the raw output.',
    },
    {
        "id": 74,
        "exception": '(no exception -- missing evidence)',
        "keywords": ['log level misconfigured', 'info messages vanish', 'warning level'],
        "root_cause": 'A production config sets the logger\'s level to WARNING "to reduce noise" -- a reasonable-sounding goal that has a real cost: every logger.info() call anywhere in the codebase becomes silently invisible, not just the noisy ones. The line confirming a batch started, and the line confirming it processed however many records, are gone right alongside whatever noise the level change was actually trying to suppress.',
        "fix": 'Be deliberate about what counts as "noise" versus "the minimum evidence needed to reconstruct what happened" -- key lifecycle events (a batch starting, finishing, or being skipped) usually belong at INFO or higher regardless of overall verbosity settings, precisely because their absence is what makes an incident unanswerable later.',
    },
    {
        "id": 75,
        "exception": '(no exception -- silently wrong)',
        "keywords": ['logged but continued', 'caught and continued', 'looks handled'],
        "root_cause": 'This is issue #6\'s pattern (a real, specific exception caught and absorbed) with logging added on top -- which makes it more dangerous, not less, because it now looks handled. The function logs the real error correctly, but then falls through to its normal "success" return value regardless of whether charge_customer() actually succeeded, so nothing downstream of this function has any way to know the charge failed.',
        "fix": "Logging an error is not the same as handling it -- the function's return value (or a re-raised exception) needs to reflect what actually happened, so callers and downstream systems can react correctly, rather than trusting a log line that only a human, only if they happen to be looking, will ever see.",
    },
    {
        "id": 76,
        "exception": '(no exception -- insufficient info)',
        "keywords": ['log.error(str(e))', 'log.exception', 'traceback missing from log'],
        "root_cause": "str(e) converts an exception to just its message text -- everything else about the exception (which file, which line, the full call stack that led there) is discarded. logger.error(str(e)) logs only that bare message, which is often not unique or specific enough to pinpoint the actual failure once there's more than one place in the codebase that could raise a similarly worded error.",
        "fix": "Use logger.exception(message) instead, called from inside an except block -- it automatically attaches the full traceback to the log record, giving anyone reading the log the exact same information they'd have seen if the exception had crashed the program uncaught.",
    },
    {
        "id": 77,
        "exception": '(no exception -- wasted work)',
        "keywords": ['expensive log message', 'eager f-string', 'debug logging disabled but slow'],
        "root_cause": 'An f-string is evaluated the instant Python reaches that line -- logger.debug(f"...{expensive_summary(data)}") calls expensive_summary(data) immediately, building the entire formatted string, before logger.debug() even gets a chance to decide whether the message will actually be used. If the logger\'s level is above DEBUG (the common case in production), all of that formatting work happens for absolutely nothing -- the result is computed and then immediately discarded.',
        "fix": 'For genuinely expensive debug-only computations, guard them with if logger.isEnabledFor(logging.DEBUG): so the expensive work only happens when the message will actually be used. (For ordinary log arguments, logging\'s built-in %-style lazy formatting -- logger.debug("value: %s", x) -- already defers formatting; it\'s specifically an expensive function call embedded in an eager f-string that needs this extra guard.)',
    },
    {
        "id": 78,
        "exception": 'OSError',
        "keywords": ['log file grows forever', 'disk full', 'no log rotation'],
        "root_cause": "A plain logging.FileHandler opens one file and keeps appending to it, with no concept of a size limit -- there's nothing built into it that ever rotates, truncates, or deletes old content. For a service that logs continuously over weeks or months of uptime, that one file grows without bound until it eventually consumes all available disk space, at which point every disk-writing operation on the whole machine starts failing, not just logging.",
        "fix": 'Use logging.handlers.RotatingFileHandler (or TimedRotatingFileHandler) instead of a plain FileHandler -- it automatically rotates to a new file once the current one hits a size limit, and deletes the oldest backups once a configured number of backups is exceeded, capping total disk usage.',
    },
    {
        "id": 79,
        "exception": '(no exception -- no record)',
        "keywords": ['swallowed exception no log', 'except pass', 'zero record of failure'],
        "root_cause": "This is issue #3's bare except: pattern taken to its most damaging extreme: except Exception: pass doesn't just catch too broadly -- it produces zero record of the failure ever happening. Even a badly written log line beats no log line at all; with nothing logged, there is no starting point from which to even begin investigating, because there's no evidence the failure occurred in the first place.",
        "fix": "Never write a bare except: pass (or except Exception: pass) in production code -- at an absolute minimum, log the exception (with logger.exception(), per issue #76) even in a code path that's deliberately designed to continue past a failure, so there's a permanent record that something went wrong, even if the immediate decision is not to stop and surface it to the caller.",
    },
    {
        "id": 80,
        "exception": '(no exception -- unqueryable)',
        "keywords": ['unstructured log', 'regex to parse logs', "can't be queried at scale"],
        "root_cause": 'A free-form log message like f"Order {order_id} for customer {customer_id}: ${amount} - {status}" is easy for a human to read in isolation, but a log aggregator has no idea that the second number is a dollar amount or that the last word is a status -- to it, it\'s just an unstructured string. Extracting any specific field back out means writing a regex that has to be updated every time the message\'s wording changes even slightly.',
        "fix": 'Log structured data -- typically JSON -- so each field is explicitly named and typed: {"order_id": ..., "amount": ..., "status": ...}. Nearly every modern log aggregator can index structured fields directly, turning "how many failed orders over $500" from a regex-writing exercise into a straightforward filter.',
    },
]


# TODO 1: Write classify_symptom(description). Lowercase `description`,
# then return a list of every CATALOG entry whose "keywords" list has
# at least one keyword that's a substring of the lowercased
# description -- most-specific-match-first isn't required, just
# preserve CATALOG order. Return an empty list if nothing matches.


# TODO 2: Write format_runbook_entry(entry). Return a multi-line string:
#   "Issue #{id}: {exception}"
#   "  Root cause: {root_cause}"
#   "  Fix: {fix}"


# TODO 3: Write diagnose(description). Call classify_symptom(). If no
# matches, return "No matching catalog entry for this symptom yet --
# check the lesson's catalog for the closest pattern." If there are
# matches, return format_runbook_entry() for each match, joined by a
# blank line between entries.


def run():
    sample_symptoms = [
        "Service crashes on startup with a KeyError for a missing config key",
        "Function looks like it works but silently returns the wrong value -- no error, just a bare except somewhere",
        "API call returns 503 but our code tries json.loads on it anyway and gets 'Expecting value'",
        "Report generator gets slower as the dataset grows -- looks quadratic",
        "Our memory climbs steadily and the unbounded cache never shrinks",
        "Two threads occasionally deadlock with two locks acquired in different orders",
        "A copy.copy of the order used a shallow copy and a nested list got shared with the original",
        "Deploy failed because of an unpinned dependency in requirements.txt",
        "We're seeing the n+1 query pattern -- one query per row instead of a join",
        "Secrets logged in plaintext were found by a security review",
        "Everything is fine, no crash at all",
    ]
    for symptom in sample_symptoms:
        print(f"SYMPTOM: {symptom}")
        print(diagnose(symptom))
        print()


if __name__ == "__main__":
    run()
