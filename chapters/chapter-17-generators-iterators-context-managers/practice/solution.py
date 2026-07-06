"""
Chapter 17 Practice Bank: Generators, Iterators & Context Managers -- reference solution.
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py
"""

# ============================================================
# Topic 1: Iterables vs. Iterators
# ============================================================

# TODO 1.1
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


countdown = Countdown(3)
for n in countdown:
    print(n)


# TODO 1.2
class RepeatTwiceIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
        self.repeats = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        value = self.items[self.index]
        self.repeats += 1
        if self.repeats == 2:
            self.index += 1
            self.repeats = 0
        return value


class RepeatTwice:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return RepeatTwiceIterator(self.items)


repeater = RepeatTwice(["a", "b"])
for value in repeater:
    print(value)


# TODO 1.3
numbers = [10, 20, 30]
it_ = iter(numbers)
print(next(it_))
print(next(it_))
print(next(it_))
try:
    next(it_)
except StopIteration:
    print("No more items")


# TODO 1.4
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


evens = EvenNumbers(10)
result = []
for value in evens:
    result.append(value)
print(result)


# TODO 1.5 (Debug the Code)
class UpToThree:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 3:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


for n in UpToThree():
    print(n)


# TODO 1.A (Scenario -- A Paginated API Client Walking Pages by Hand)
class PageWalker:
    def __init__(self, pages):
        self.pages = pages
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.pages):
            raise StopIteration
        page = self.pages[self.index]
        self.index += 1
        return page


walker = PageWalker(["page1-data", "page2-data", "page3-data"])
pages_seen = []
for page in walker:
    pages_seen.append(page)
print(pages_seen)


# TODO 1.B (Scenario -- Interview Prep)
def explain_iterable_vs_iterator():
    return (
        "An iterable is any object with an __iter__ method that can "
        "produce an iterator (a list, a string, a custom class defining "
        "__iter__), while an iterator is the object actually doing the "
        "work -- it defines __next__, which returns the next value each "
        "time it's called and raises StopIteration when there's nothing "
        "left. A for loop calls iter() on the iterable once to get an "
        "iterator, then calls next() on that iterator over and over, "
        "catching StopIteration internally to know when to stop, which "
        "is exactly what the for loop hides from the programmer to make "
        "looping feel automatic."
    )


print(explain_iterable_vs_iterator())


# ============================================================
# Topic 2: Generator Functions
# ============================================================

# TODO 2.1
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1


gen = count_up_to(4)
for value in gen:
    print(value)


# TODO 2.2
def squares_up_to(limit):
    n = 1
    while n <= limit:
        yield n * n
        n += 1


result = list(squares_up_to(5))
print(result)


# TODO 2.3
def alternating_signs(limit):
    n = 1
    while n <= limit:
        if n % 2 == 0:
            yield n
        else:
            yield -n
        n += 1


gen = alternating_signs(6)
for value in gen:
    print(value)


# TODO 2.4
def countdown_then_liftoff(start):
    n = start
    while n >= 1:
        yield n
        n -= 1
    yield "Liftoff!"


gen = countdown_then_liftoff(3)
for value in gen:
    print(value)


# TODO 2.5 (Debug the Code)
def double_each(numbers):
    for n in numbers:
        yield n * 2


gen = double_each([1, 2, 3])
print(list(gen))


# TODO 2.A (Scenario -- Streaming Sensor Readings One at a Time)
def sensor_readings(readings, threshold):
    for reading in readings:
        if reading > threshold:
            yield reading


gen = sensor_readings([12, 45, 8, 99, 31], 20)
alerts = []
for value in gen:
    alerts.append(value)
print(alerts)


# TODO 2.B (Scenario -- Interview Prep)
def explain_yield_vs_return():
    return (
        "A function using return runs from top to bottom exactly once "
        "and then its local state is gone -- calling it again starts "
        "over completely fresh -- while a function containing yield "
        "becomes a generator function: calling it doesn't run the body "
        "at all, it just creates a generator object, and each time "
        "next() is called on that generator (directly or via a for "
        "loop), the function's body runs until it hits a yield, hands "
        "back that one value, and then pauses with its local variables "
        "and position in the code frozen exactly where it left off, "
        "resuming from that exact point the next time next() is "
        "called, which is what makes generators memory-efficient for "
        "producing a long or even infinite sequence of values one at a "
        "time instead of building the whole thing in memory first."
    )


print(explain_yield_vs_return())


# ============================================================
# Topic 3: Generator Expressions
# ============================================================

# TODO 3.1
squares_list = [n * n for n in range(1, 6)]
print(squares_list)
print(type(squares_list))

squares_gen = (n * n for n in range(1, 6))
print(type(squares_gen))
print(list(squares_gen))


# TODO 3.2
evens_gen = (n for n in range(1, 21) if n % 2 == 0)
print(sum(evens_gen))


# TODO 3.3
words = ["apple", "kiwi", "banana", "fig", "grapefruit"]
lengths_gen = (len(word) for word in words)
print(max(lengths_gen))


# TODO 3.4
names = ["ann", "Bob", "carl", "Diana"]
print(any(name[0].isupper() for name in names))


# TODO 3.5 (Debug the Code)
cubes = (n ** 3 for n in range(1, 6))
print(type(cubes))


# TODO 3.A (Scenario -- Checking a Huge Log File for One Matching Line Without Loading It All)
def has_error_line(log_lines):
    return any("ERROR" in line for line in log_lines)


lines = ["INFO: ok", "INFO: ok", "ERROR: disk full", "INFO: ok"]
print(has_error_line(lines))


# TODO 3.B (Scenario -- Interview Prep)
def explain_genexpr_memory_benefit():
    return (
        "A list comprehension builds and stores every single result in "
        "memory all at once, which is fine for a short list but "
        "wasteful (or even impossible) for a very large or effectively "
        "unbounded sequence, while a generator expression produces "
        "exactly one value at a time, on demand, and never holds the "
        "whole sequence in memory at once. This matters most when the "
        "calling code (sum(), max(), any(), a for loop that might stop "
        "early) only ever needs to look at one value at a time anyway, "
        "since a generator expression gets the same result with a "
        "fraction of the memory and can even represent a sequence too "
        "large to ever fit in a list at all."
    )


print(explain_genexpr_memory_benefit())


# ============================================================
# Topic 4: The `with` Protocol Generalized (`__enter__`/`__exit__`)
# ============================================================

# TODO 4.1
class ManagedResource:
    def __init__(self, name):
        self.name = name
        self.is_open = False

    def __enter__(self):
        self.is_open = True
        print(f"Opening {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.is_open = False
        print(f"Closing {self.name}")


with ManagedResource("Database Connection") as resource:
    print(resource.is_open)
print(resource.is_open)


# TODO 4.2
class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = 0
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Timer stopped.")


with Timer() as timer:
    print("Timing something...")
# __exit__ runs automatically the moment the with block ends, even
# though nothing inside the block raised an error.


# TODO 4.3
class NoisyBlock:
    def __enter__(self):
        print("Entering block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting block")
        return False


with NoisyBlock():
    print("Inside the block")


# TODO 4.4
class SuppressValueError:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is ValueError:
            return True
        return False


with SuppressValueError():
    raise ValueError("boom")
print("Program continues")


# TODO 4.5 (Debug the Code)
class HalfManager:
    def __enter__(self):
        print("Starting up")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleaning up")
        return False


with HalfManager():
    print("Doing work")


# TODO 4.A (Scenario -- Guaranteeing a Lock Is Always Released)
class SimpleLock:
    def __init__(self):
        self.locked = False

    def __enter__(self):
        self.locked = True
        print("Lock acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.locked = False
        print("Lock released")
        return False


with SimpleLock() as lock:
    print(lock.locked)
print(lock.locked)


# TODO 4.B (Scenario -- Interview Prep)
def explain_with_protocol_purpose():
    return (
        "with is a general protocol built on two special methods, "
        "__enter__ and __exit__ -- __enter__ runs when the block starts "
        "and its return value is what gets bound after 'as', while "
        "__exit__ is guaranteed to run when the block ends, whether it "
        "ended normally or an exception was raised inside it. This "
        "matters because cleanup code (closing a file, releasing a "
        "lock, closing a network connection) that lives inside __exit__ "
        "will always run, which removes an entire category of bugs "
        "where a raised exception skips past ordinary cleanup code that "
        "was only ever going to run 'at the end' of a plain, non-with "
        "block."
    )


print(explain_with_protocol_purpose())


# ============================================================
# Topic 5: Writing a Custom Context Manager Class
# ============================================================

# TODO 5.1
class LoggingContext:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        print(f"[{self.label}] start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"[{self.label}] end")
        return False


with LoggingContext("Task A") as ctx:
    print("Doing the task")


# TODO 5.2
class CallCounter:
    def __init__(self):
        self.count = 0

    def __enter__(self):
        self.count += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False


counter = CallCounter()
with counter:
    pass
with counter:
    pass
with counter:
    pass
print(counter.count)


# TODO 5.3
class ExceptionLogger:
    def __init__(self):
        self.errors = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.errors.append(str(exc_value))
            return True
        return False


logger = ExceptionLogger()
with logger:
    raise ValueError("bad input")
print(logger.errors)


# TODO 5.4
class Transaction:
    def __init__(self):
        self.committed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.committed = exc_type is None
        return False


txn = Transaction()
with txn:
    x = 1 + 1
print(txn.committed)


# TODO 5.5 (Debug the Code)
class AuditLog:
    def __init__(self):
        self.entries = []

    def __enter__(self):
        self.entries.append("entered")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.entries.append("exited")
        return False


audit = AuditLog()
with audit:
    print(audit.entries)


# TODO 5.A (Scenario -- A Reusable Timing Context Manager for Performance Checks)
class StepTracker:
    def __init__(self, label):
        self.label = label
        self.steps = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.steps += 1
        return False


tracker = StepTracker("batch-job")
with tracker:
    pass
with tracker:
    pass
print(tracker.steps)


# TODO 5.B (Scenario -- Interview Prep)
def explain_context_manager_lifecycle():
    return (
        "Python first calls SomeClass() to create the instance, then "
        "immediately calls that instance's __enter__() method, binding "
        "whatever __enter__() returns to the name after 'as'; the code "
        "inside the with block then runs normally; once the block "
        "finishes -- whether it completed normally or raised an "
        "exception -- Python calls the same instance's "
        "__exit__(exc_type, exc_value, traceback) method, passing "
        "exception details if one occurred (or None, None, None if "
        "not); if __exit__ returns a truthy value, Python treats the "
        "exception as handled and suppresses it, but if __exit__ "
        "returns a falsy value (or nothing at all, since a function "
        "with no return returns None), any exception that occurred "
        "continues propagating normally past the with block."
    )


print(explain_context_manager_lifecycle())


# ============================================================
# Topic 6: Bringing It Together -- Real-World Use
# ============================================================

# TODO 6.1
def stream_lines(text):
    for line in text.split("\n"):
        yield line.strip()


sample_text = "first line\nsecond line\nthird line"
for line in stream_lines(sample_text):
    print(line)


# TODO 6.2
class LineCounter:
    def __init__(self):
        self.count = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False


def long_lines(lines, min_length):
    for line in lines:
        if len(line) > min_length:
            yield line


lines = ["short", "a fairly long line here", "tiny", "another long one indeed"]
with LineCounter() as counter:
    kept = []
    for line in long_lines(lines, 10):
        counter.count += 1
        kept.append(line)
print(kept)
print(counter.count)


# TODO 6.3
def first_n_matching(items, predicate_threshold, limit):
    found = 0
    for item in items:
        if found >= limit:
            return
        if item > predicate_threshold:
            found += 1
            yield item


gen = first_n_matching([5, 12, 3, 18, 25, 7, 30], 10, 3)
result = list(gen)
print(result)


# TODO 6.4
class FileSimulator:
    def __init__(self, content):
        self.content = content
        self.closed = True

    def __enter__(self):
        self.closed = False
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.closed = True
        return False

    def lines(self):
        for line in self.content.split("\n"):
            yield line


sim = FileSimulator("alpha\nbeta\ngamma")
with sim as opened:
    collected = []
    for line in opened.lines():
        collected.append(line)
print(collected)
print(sim.closed)


# TODO 6.5 (Debug the Code)
def even_numbers_from(data):
    for n in data:
        if n % 2 == 0:
            yield n


gen = even_numbers_from([1, 2, 3, 4, 5, 6])
print(list(gen))
print(type(even_numbers_from([1, 2])))


# TODO 6.A (Scenario -- A Log-Processing Pipeline Combining Everything)
class LogSource:
    def __init__(self, content):
        self.content = content
        self.opened = False

    def __enter__(self):
        self.opened = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.opened = False
        return False


def error_lines(content):
    for line in content.split("\n"):
        if "ERROR" in line:
            yield line


log_text = "INFO: boot\nERROR: disk full\nINFO: ready\nERROR: timeout"
with LogSource(log_text) as source:
    errors = list(error_lines(source.content))
print(errors)
print(len(errors))


# TODO 6.B (Scenario -- Interview Prep)
def explain_bringing_together():
    return (
        "A realistic example is a program processing a huge log or "
        "data file: with open('big_log.txt') as f: is a context "
        "manager guaranteeing the file handle gets closed no matter "
        "what happens while reading it, even if an error occurs "
        "partway through; for line in f: relies on the file object "
        "being an iterator under the hood, pulling one line at a time "
        "from disk instead of loading the entire file into memory "
        "first; and a generator function wrapping that loop (yielding "
        "only lines matching some condition, or transforming each line "
        "lazily) lets the rest of the program consume results one at a "
        "time without ever materializing the full, possibly enormous, "
        "result set in memory -- together, these three tools are "
        "exactly how real systems handle data that's too large, too "
        "slow, or too risky (in terms of needing guaranteed cleanup) to "
        "process any other way."
    )


print(explain_bringing_together())
