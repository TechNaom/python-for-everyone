"""
Chapter 17 Practice Bank: Generators, Iterators & Context Managers
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py
"""

# ============================================================
# Topic 1: Iterables vs. Iterators
# ============================================================

# TODO 1.1: Write a class Countdown with __init__(self, start) storing
# self.current = start, an __iter__(self) that returns self, and a
# __next__(self) that raises StopIteration if self.current < 0,
# otherwise decrements self.current by 1 after returning the value it
# had before decrementing (so calling next() repeatedly yields start,
# start - 1, ..., 0, then stops) -- showing how a for loop is really
# just repeated calls to __next__() until StopIteration. Create
# countdown = Countdown(3) and use a for loop to print each value.


# TODO 1.2: Write a class RepeatTwice with __init__(self, items)
# storing self.items = items, an __iter__(self) that returns
# RepeatTwiceIterator(self.items) (a second class you also define,
# with __init__(self, items) storing self.items and self.index = 0,
# and self.repeats = 0), and a __next__(self) on
# RepeatTwiceIterator that returns each item in self.items twice in a
# row before moving to the next item, raising StopIteration once
# every item has been yielded twice. Create
# repeater = RepeatTwice(["a", "b"]) and use a for loop to print each
# value (should print "a", "a", "b", "b").


# TODO 1.3: Manually drive the built-in iterator protocol without a
# for loop: create numbers = [10, 20, 30], call it_ = iter(numbers) to
# get its iterator, then call next(it_) three times, printing each
# result, and finally wrap a fourth next(it_) call in a
# try/except StopIteration that prints "No more items" when the
# exception is caught -- showing exactly what a for loop does for you
# under the hood.


# TODO 1.4: Write a class EvenNumbers with __init__(self, limit)
# storing self.limit = limit and self.current = 0, an __iter__(self)
# that returns self, and a __next__(self) that raises StopIteration
# once self.current > self.limit, otherwise saves value = self.current,
# adds 2 to self.current, and returns value -- producing every even
# number from 0 up to and including limit if limit is even. Create
# evens = EvenNumbers(10) and use a for loop to collect every value
# into a list called result, then print result.


# TODO 1.5 (Debug the Code): this class is supposed to be usable in a
# for loop, but its __next__ method never raises StopIteration -- it
# just keeps returning self.current forever, so the for loop below
# never terminates (an infinite loop). Fix __next__ so it raises
# StopIteration once self.current > 3, matching the intended behavior
# of counting from 1 up to 3 and then stopping. (Comment out the
# for loop's print or reduce it in your head; do not actually run an
# infinite loop -- reason through the fix instead.)
class UpToThree:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += 1
        return value


# for n in UpToThree():
#     print(n)


# TODO 1.A (Scenario -- A Paginated API Client Walking Pages by Hand):
# a real API client often exposes "give me the next page" without a
# built-in for-loop wrapper, and the calling code has to drive that
# manually. Write a class PageWalker with __init__(self, pages) storing
# self.pages = pages and self.index = 0, an __iter__(self) that
# returns self, and a __next__(self) that raises StopIteration once
# self.index is out of range for self.pages, otherwise saves
# page = self.pages[self.index], adds 1 to self.index, and returns
# page -- modeling how a client walks through a list of already-fetched
# pages one at a time via the iterator protocol. Create
# walker = PageWalker(["page1-data", "page2-data", "page3-data"]) and
# use a for loop to collect every page into a list called pages_seen,
# then print pages_seen.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks you to
# explain, in plain language, what makes an object "iterable" versus
# what makes an object an "iterator", and how a for loop actually uses
# that distinction under the hood. Write a function
# explain_iterable_vs_iterator() that returns a string explaining that
# an iterable is any object with an __iter__ method that can produce an
# iterator (a list, a string, a custom class defining __iter__), while
# an iterator is the object actually doing the work -- it defines
# __next__, which returns the next value each time it's called and
# raises StopIteration when there's nothing left; a for loop calls
# iter() on the iterable once to get an iterator, then calls next() on
# that iterator over and over, catching StopIteration internally to
# know when to stop, which is exactly what the for loop hides from the
# programmer to make looping feel automatic. Call it and print the
# result.


# ============================================================
# Topic 2: Generator Functions
# ============================================================

# TODO 2.1: Write a generator function count_up_to(limit) that uses
# yield to produce every integer from 1 up to and including limit, one
# at a time, instead of building and returning a list all at once.
# Create gen = count_up_to(4) and use a for loop to print each value
# it yields -- showing that calling a generator function doesn't run
# its body immediately, it only starts running (and pauses at each
# yield) once you start iterating over it.


# TODO 2.2: Write a generator function squares_up_to(limit) that uses
# yield to produce n * n for every n from 1 up to and including limit.
# Create result = list(squares_up_to(5)) (converting the generator to a
# list directly) and print result -- showing that yield pauses and
# resumes the function's state between values instead of computing
# everything up front like a return-based function with a list would.


# TODO 2.3: Write a generator function alternating_signs(limit) that
# uses yield to produce n if n is even, or -n if n is odd, for every n
# from 1 up to and including limit -- demonstrating that a generator
# function can contain any logic a normal function can (if/else,
# loops), it just produces its results one yield at a time instead of
# building a list to return. Create gen = alternating_signs(6) and use
# a for loop to print each value.


# TODO 2.4: Write a generator function countdown_then_liftoff(start)
# that uses yield to produce every integer from start down to 1, then
# finally yields the string "Liftoff!" -- showing a generator can mix
# different kinds of values across multiple yield statements, pausing
# and resuming at each one in the order they're reached. Create
# gen = countdown_then_liftoff(3) and use a for loop to print each
# value (should print 3, 2, 1, "Liftoff!").


# TODO 2.5 (Debug the Code): this function is supposed to be a
# generator that yields each number in numbers after doubling it, but
# it uses return instead of yield inside the loop, so it exits and
# stops after producing only the very first doubled value instead of
# continuing to the next one on each call. Fix the return inside the
# loop to yield, so the function produces every doubled value across
# repeated calls to next() / iteration, one at a time.
def double_each(numbers):
    for n in numbers:
        return n * 2


# gen = double_each([1, 2, 3])
# print(list(gen))


# TODO 2.A (Scenario -- Streaming Sensor Readings One at a Time): a
# monitoring dashboard receives sensor readings that could keep coming
# indefinitely, so code that processes them shouldn't wait to collect
# them all into a list first. Write a generator function
# sensor_readings(readings, threshold) that uses yield to produce only
# the readings from readings that are greater than threshold, one at a
# time, in order -- modeling how a real streaming pipeline filters and
# forwards values as they arrive instead of loading everything into
# memory first. Create
# gen = sensor_readings([12, 45, 8, 99, 31], 20) and use a for loop to
# collect every yielded value into a list called alerts, then print
# alerts.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks you to
# explain the difference between a regular function that uses return
# and a generator function that uses yield, specifically around what
# happens to the function's local state between calls. Write a
# function explain_yield_vs_return() that returns a string explaining
# that a function using return runs from top to bottom exactly once
# and then its local state is gone -- calling it again starts over
# completely fresh -- while a function containing yield becomes a
# generator function: calling it doesn't run the body at all, it just
# creates a generator object, and each time next() is called on that
# generator (directly or via a for loop), the function's body runs
# until it hits a yield, hands back that one value, and then pauses
# with its local variables and position in the code frozen exactly
# where it left off, resuming from that exact point the next time
# next() is called, which is what makes generators memory-efficient
# for producing a long or even infinite sequence of values one at a
# time instead of building the whole thing in memory first. Call it
# and print the result.


# ============================================================
# Topic 3: Generator Expressions
# ============================================================

# TODO 3.1: Create a list comprehension squares_list = [n * n for n in
# range(1, 6)] and print it and print type(squares_list). Then create a
# generator expression squares_gen = (n * n for n in range(1, 6)) and
# print type(squares_gen) (should show <class 'generator'>) and print
# list(squares_gen) -- showing the syntax difference is just square
# brackets versus parentheses, but a list comprehension builds the
# whole list immediately while a generator expression builds nothing
# until you iterate over it.


# TODO 3.2: Create a generator expression
# evens_gen = (n for n in range(1, 21) if n % 2 == 0) that lazily
# produces every even number from 1 to 20, then print sum(evens_gen)
# (summing directly over the generator expression without ever
# converting it to a list first) -- showing generator expressions plug
# directly into functions like sum(), max(), and any() that only need
# to look at each value once.


# TODO 3.3: Create a list of words words = ["apple", "kiwi", "banana",
# "fig", "grapefruit"], then create a generator expression
# lengths_gen = (len(word) for word in words), and print
# max(lengths_gen) -- demonstrating that a generator expression is
# lazy: nothing is computed until max() actually starts pulling values
# from it one at a time.


# TODO 3.4: Create names = ["ann", "Bob", "carl", "Diana"], then use a
# generator expression inside any() to check
# any(name[0].isupper() for name in names), printing the result
# (should be True, since "Bob" and "Diana" start with an uppercase
# letter) -- showing any() stops pulling values from the generator
# expression the instant it finds a True, which a list comprehension
# built first could never do since it always computes every item up
# front.


# TODO 3.5 (Debug the Code): this line is supposed to create a
# generator expression (lazy, memory-efficient, one value produced at
# a time only when needed), but it uses square brackets instead of
# parentheses, which actually creates a full list comprehension
# instead -- building every value immediately in memory rather than
# lazily. Fix the square brackets to parentheses so cubes is a true
# generator expression, then confirm by printing type(cubes) (should
# now say <class 'generator'> instead of <class 'list'>).
cubes = [n ** 3 for n in range(1, 6)]
# print(type(cubes))


# TODO 3.A (Scenario -- Checking a Huge Log File for One Matching Line
# Without Loading It All): a log-processing tool needs to check
# whether any line in a very large list of log lines contains the word
# "ERROR", but building a full list of every matching line first would
# waste memory when all that's really needed is a yes/no answer. Write
# a function has_error_line(log_lines) that uses a generator
# expression -- any("ERROR" in line for line in log_lines) -- and
# returns its result directly, modeling how any() short-circuits the
# instant it finds a match instead of scanning (or storing) every
# remaining line. Create
# lines = ["INFO: ok", "INFO: ok", "ERROR: disk full", "INFO: ok"] and
# print has_error_line(lines) (should be True).


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks why you
# might choose a generator expression over a list comprehension when
# the two look so similar. Write a function
# explain_genexpr_memory_benefit() that returns a string explaining
# that a list comprehension builds and stores every single result in
# memory all at once, which is fine for a short list but wasteful (or
# even impossible) for a very large or effectively unbounded sequence,
# while a generator expression produces exactly one value at a time,
# on demand, and never holds the whole sequence in memory at once --
# this matters most when the calling code (sum(), max(), any(), a for
# loop that might stop early) only ever needs to look at one value at a
# time anyway, since a generator expression gets the same result with
# a fraction of the memory and can even represent a sequence too large
# to ever fit in a list at all. Call it and print the result.


# ============================================================
# Topic 4: The `with` Protocol Generalized (`__enter__`/`__exit__`)
# ============================================================

# TODO 4.1: Open this very idea without touching real files yet: write
# a class ManagedResource with __init__(self, name) storing self.name
# and self.is_open = False, an __enter__(self) that sets
# self.is_open = True, prints f"Opening {self.name}", and returns self,
# and an __exit__(self, exc_type, exc_value, traceback) that sets
# self.is_open = False and prints f"Closing {self.name}" -- showing the
# with statement is a general protocol, not something limited to
# files: any class defining __enter__ and __exit__ can be used with
# with. Use with ManagedResource("Database Connection") as resource:
# inside the block print resource.is_open (should be True), then after
# the block ends (outside the with) print resource.is_open again
# (should be False, proving __exit__ ran automatically).


# TODO 4.2: Write a class Timer with __init__(self) storing nothing
# needed yet, an __enter__(self) that sets self.start = 0 (a
# placeholder "start time") and returns self, and an
# __exit__(self, exc_type, exc_value, traceback) that prints
# "Timer stopped." -- then use with Timer() as timer: inside the block
# print "Timing something...", and note (in a comment, no need to
# print it) that __exit__ runs automatically the moment the with block
# ends, even though nothing inside the block raised an error.


# TODO 4.3: Write a class NoisyBlock with an __enter__(self) that
# prints "Entering block" and returns self, and an
# __exit__(self, exc_type, exc_value, traceback) that prints
# "Exiting block" and returns False (explicitly not suppressing any
# exception). Use with NoisyBlock(): as the block, and inside it print
# "Inside the block" -- observing the exact order things print:
# "Entering block", then "Inside the block", then "Exiting block".


# TODO 4.4: Write a class SuppressValueError with an __enter__(self)
# that returns self, and an __exit__(self, exc_type, exc_value,
# traceback) that returns True if exc_type is ValueError (telling
# Python "I handled it, don't propagate this exception"), otherwise
# returns False. Use with SuppressValueError(): and inside the block
# raise ValueError("boom"), then print "Program continues" right after
# the with block -- showing that "Program continues" still prints
# because __exit__ returning True suppressed the ValueError, letting
# execution continue normally past the with block instead of crashing.


# TODO 4.5 (Debug the Code): this class is supposed to work with a
# with statement, but it's missing an __exit__ method entirely, so
# Python raises a TypeError the moment the with block tries to run
# (an object used as a context manager must define both __enter__ and
# __exit__, not just one). Fix the class by adding an
# __exit__(self, exc_type, exc_value, traceback) method that simply
# prints "Cleaning up" and returns False.
class HalfManager:
    def __enter__(self):
        print("Starting up")
        return self


# with HalfManager():
#     print("Doing work")


# TODO 4.A (Scenario -- Guaranteeing a Lock Is Always Released): a
# multi-user system uses a lock object to make sure only one part of
# the program touches a shared resource at a time, and forgetting to
# release that lock (even if an error happens) would freeze out every
# other part of the program forever. Write a class SimpleLock with
# __init__(self) storing self.locked = False, an __enter__(self) that
# sets self.locked = True, prints "Lock acquired", and returns self,
# and an __exit__(self, exc_type, exc_value, traceback) that sets
# self.locked = False, prints "Lock released", and returns False --
# modeling how a with block guarantees release even if the code inside
# raises. Use with SimpleLock() as lock: inside the block, print
# lock.locked (True), then after the with block print lock.locked
# again (False).


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks you to
# explain what problem the with statement and the context-manager
# protocol are actually solving, using a concrete example. Write a
# function explain_with_protocol_purpose() that returns a string
# explaining that with is a general protocol built on two special
# methods, __enter__ and __exit__ -- __enter__ runs when the block
# starts and its return value is what gets bound after "as", while
# __exit__ is guaranteed to run when the block ends, whether it ended
# normally or an exception was raised inside it; this matters because
# cleanup code (closing a file, releasing a lock, closing a network
# connection) that lives inside __exit__ will always run, which removes
# an entire category of bugs where a raised exception skips past
# ordinary cleanup code that was only ever going to run "at the end" of
# a plain, non-with block. Call it and print the result.


# ============================================================
# Topic 5: Writing a Custom Context Manager Class
# ============================================================

# TODO 5.1: Write a class LoggingContext with __init__(self, label)
# storing self.label = label, an __enter__(self) that prints
# f"[{self.label}] start" and returns self, and an
# __exit__(self, exc_type, exc_value, traceback) that prints
# f"[{self.label}] end" and returns False. Use
# with LoggingContext("Task A") as ctx: inside the block print
# "Doing the task" -- writing your very first fully custom context
# manager class from scratch, with no starting template.


# TODO 5.2: Write a class CallCounter with __init__(self) storing
# self.count = 0, an __enter__(self) that increments self.count by 1
# and returns self, and an __exit__(self, exc_type, exc_value,
# traceback) that returns False -- tracking how many times the context
# manager has been entered across multiple with blocks reusing the
# same instance. Create counter = CallCounter(), then use
# with counter: (empty-ish block, just pass) three separate times in a
# row, and after all three, print counter.count (should be 3).


# TODO 5.3: Write a class ExceptionLogger with __init__(self) storing
# self.errors = [], an __enter__(self) that returns self, and an
# __exit__(self, exc_type, exc_value, traceback) that, if exc_type is
# not None, appends str(exc_value) to self.errors and returns True
# (suppressing the exception), otherwise returns False -- a reusable
# pattern for collecting errors instead of crashing the program. Create
# logger = ExceptionLogger(), then use with logger: and inside the
# block raise ValueError("bad input"), then after the with block print
# logger.errors (should be ["bad input"]).


# TODO 5.4: Write a class Transaction with __init__(self) storing
# self.committed = False, an __enter__(self) that returns self, and an
# __exit__(self, exc_type, exc_value, traceback) that sets
# self.committed = (exc_type is None) (True only if no exception
# occurred) and returns False -- modeling how a real database
# transaction commits on success and would roll back on failure.
# Create txn = Transaction(), use with txn: with a simple statement
# like x = 1 + 1 inside (no error), then print txn.committed (should
# be True).


# TODO 5.5 (Debug the Code): this custom context manager's __exit__
# method is supposed to return False so that any exception raised
# inside the with block still propagates normally (the intended
# behavior for a context manager that only logs, not suppresses), but
# it accidentally returns True instead -- which silently swallows every
# exception raised inside any with block using it, even ones the
# calling code needed to see and handle. Fix __exit__ to return False.
class AuditLog:
    def __init__(self):
        self.entries = []

    def __enter__(self):
        self.entries.append("entered")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.entries.append("exited")
        return True


# audit = AuditLog()
# with audit:
#     print(audit.entries)


# TODO 5.A (Scenario -- A Reusable Timing Context Manager for
# Performance Checks): a team wants to measure how many times a block
# of code runs inside a performance-sensitive section, without
# scattering counter += 1 lines everywhere by hand. Write a class
# StepTracker with __init__(self, label) storing self.label = label
# and self.steps = 0, an __enter__(self) that returns self, and an
# __exit__(self, exc_type, exc_value, traceback) that increments
# self.steps by 1 and returns False -- modeling a reusable context
# manager that tracks how many times a labeled block of work
# completed. Create tracker = StepTracker("batch-job"), then use
# with tracker: (pass) twice in a row, and print tracker.steps (should
# be 2).


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks you to
# walk through, step by step, exactly what Python does when it
# executes a with SomeClass() as x: block, in terms of which dunder
# methods get called and when. Write a function
# explain_context_manager_lifecycle() that returns a string explaining
# that Python first calls SomeClass() to create the instance, then
# immediately calls that instance's __enter__() method, binding
# whatever __enter__() returns to the name after "as"; the code inside
# the with block then runs normally; once the block finishes -- whether
# it completed normally or raised an exception -- Python calls the same
# instance's __exit__(exc_type, exc_value, traceback) method, passing
# exception details if one occurred (or None, None, None if not); if
# __exit__ returns a truthy value, Python treats the exception as
# handled and suppresses it, but if __exit__ returns a falsy value (or
# nothing at all, since a function with no return returns None), any
# exception that occurred continues propagating normally past the with
# block. Call it and print the result.


# ============================================================
# Topic 6: Bringing It Together -- Real-World Use
# ============================================================

# TODO 6.1: Write a generator function stream_lines(text) that uses
# yield to produce each line of text (splitting on "\n") one at a
# time, stripped of surrounding whitespace, without ever building the
# full list of lines first -- modeling how a real program streams a
# large file line-by-line via a for line in file: loop instead of
# calling file.readlines() and holding everything in memory at once.
# Create sample_text = "first line\nsecond line\nthird line" and use a
# for loop over stream_lines(sample_text) to print each line.


# TODO 6.2: Combine a generator expression with a custom context
# manager: write a class LineCounter with __init__(self) storing
# self.count = 0, an __enter__(self) that returns self, and an
# __exit__(self, exc_type, exc_value, traceback) that returns False.
# Write a generator function long_lines(lines, min_length) that uses
# yield to produce only the entries in lines whose length is greater
# than min_length, one at a time. Create
# lines = ["short", "a fairly long line here", "tiny", "another long one indeed"],
# then use with LineCounter() as counter: inside the block, loop over
# long_lines(lines, 10), incrementing counter.count for each one and
# collecting it into a list called kept -- after the with block, print
# kept and print counter.count.


# TODO 6.3: Write a generator function first_n_matching(items,
# predicate_threshold, limit) that uses yield to lazily produce values
# from items that are greater than predicate_threshold, stopping once
# it has yielded limit values (even if more of items remain unchecked)
# -- modeling how a generator can lazily produce just the first N
# matches from a huge stream without ever scanning past what's needed.
# Create
# gen = first_n_matching([5, 12, 3, 18, 25, 7, 30], 10, 3) and use a
# for loop (or list(gen)) to collect the results into a list called
# result, then print result (should stop after finding 3 matches:
# [12, 18, 25]).


# TODO 6.4: Write a class FileSimulator that acts as a custom context
# manager standing in for a real file (since no real filesystem is
# needed for the lesson): __init__(self, content) stores
# self.content = content and self.closed = True, __enter__(self) sets
# self.closed = False and returns self, __exit__(self, exc_type,
# exc_value, traceback) sets self.closed = True and returns False, and
# a method lines(self) that is a generator (uses yield) producing each
# line of self.content (split on "\n") one at a time -- modeling the
# combination real file objects use: with open(...) as f: opens and
# guarantees closing the file, while for line in f: streams its
# contents lazily. Create
# sim = FileSimulator("alpha\nbeta\ngamma"), use
# with sim as opened: inside the block, loop over opened.lines(),
# collecting each line into a list called collected, then after the
# with block print collected and print sim.closed (should be True).


# TODO 6.5 (Debug the Code): this generator function is supposed to
# lazily yield only the values in data that are even, but it builds
# and returns a full list comprehension with return instead of using
# yield inside a loop -- which still "works" in the sense that
# iterating over the result produces the right values, but it defeats
# the entire point of writing a generator (nothing is lazy anymore;
# the whole filtered list is built immediately in memory). Fix it to
# be a true generator: loop over data, and yield each number that's
# even one at a time instead of returning a list comprehension.
def even_numbers_from(data):
    return [n for n in data if n % 2 == 0]


# gen = even_numbers_from([1, 2, 3, 4, 5, 6])
# print(list(gen))
# print(type(gen))


# TODO 6.A (Scenario -- A Log-Processing Pipeline Combining Everything):
# a real log-processing tool streams lines from a (simulated) log file
# using a custom context manager, lazily filters them with a generator
# function, and reports a small summary -- combining every sub-topic
# from this chapter in one realistic pipeline. Write a class
# LogSource with __init__(self, content) storing self.content = content
# and self.opened = False, __enter__(self) setting self.opened = True
# and returning self, and __exit__(self, exc_type, exc_value,
# traceback) setting self.opened = False and returning False. Write a
# generator function error_lines(content) that uses yield to lazily
# produce only the lines (split on "\n") containing the substring
# "ERROR". Create
# log_text = "INFO: boot\nERROR: disk full\nINFO: ready\nERROR: timeout",
# then use with LogSource(log_text) as source: inside the block build
# errors = list(error_lines(source.content)), and after the with block
# print errors and print len(errors).


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks you to
# describe a real production system where generators, iterators, and
# context managers would all naturally show up together. Write a
# function explain_bringing_together() that returns a string
# explaining that a realistic example is a program processing a huge
# log or data file: with open("big_log.txt") as f: is a context
# manager guaranteeing the file handle gets closed no matter what
# happens while reading it, even if an error occurs partway through;
# for line in f: relies on the file object being an iterator under the
# hood, pulling one line at a time from disk instead of loading the
# entire file into memory first; and a generator function wrapping
# that loop (yielding only lines matching some condition, or
# transforming each line lazily) lets the rest of the program consume
# results one at a time without ever materializing the full, possibly
# enormous, result set in memory -- together, these three tools are
# exactly how real systems handle data that's too large, too slow, or
# too risky (in terms of needing guaranteed cleanup) to process any
# other way. Call it and print the result.
