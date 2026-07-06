"""
Chapter 17 Exercises: Generators, Iterators & Context Managers -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

# TODO 1: Write a class Countdown whose __init__ takes start and
# stores it as self.current. Give it __iter__(self) that returns
# self, and __next__(self) that raises StopIteration once
# self.current is 0 or less, otherwise returns the current value and
# decrements it by 1. Create a Countdown(4) and loop over it with a
# for loop, printing each value.
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for number in Countdown(4):
    print(number)


# TODO 2: Write a generator function evens_up_to(n) that starts a
# counter at 0 and, while the counter is less than or equal to n,
# yields the counter and then increases it by 2. Loop over
# evens_up_to(10) with a for loop and print each value.
def evens_up_to(n):
    current = 0
    while current <= n:
        yield current
        current += 2

for number in evens_up_to(10):
    print(number)


# TODO 3: Use sum() with a generator expression (not a list
# comprehension) to add up the cubes (n ** 3) of every number from 1
# to 5 inclusive. Store the result in total and print it.
total = sum(n ** 3 for n in range(1, 6))
print(total)


# TODO 4: Use with open(...) as f: to write the three lines "1", "2",
# and "3" (each on its own line) to a file named "numbers.txt". Then
# use a second with open(...) as f: block to read all the lines back
# with .readlines() into a variable lines. Print len(lines), then
# print f.closed right after the block ends.
with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n")

with open("numbers.txt", "r") as f:
    lines = f.readlines()
print(len(lines))
print(f.closed)


# TODO 5: Write a class Timer with __enter__(self) that sets
# self.entered = True and returns self, and
# __exit__(self, exc_type, exc_value, traceback) that sets
# self.exited = True and returns False. Use with Timer() as t: pass
# and then print t.entered and t.exited.
class Timer:
    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.exited = True
        return False

with Timer() as t:
    pass
print(t.entered, t.exited)


# TODO 6: Write a generator function read_lines(filename) that opens
# the file with with, loops over it with for line in f:, and yields
# each line with .strip() applied. First, write the three lines
# "alpha", "beta", and "gamma" to a file named "stream.txt" using
# with open(...) as f:. Then loop over read_lines("stream.txt") with
# a for loop and print each line.
def read_lines(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

with open("stream.txt", "w") as f:
    f.write("alpha\nbeta\ngamma\n")

for line in read_lines("stream.txt"):
    print(line)


# TODO 7 (Debug the Code): this generator function accidentally uses
# return count instead of yield count inside its loop, so calling it
# and looping over it only ever produces the very first value before
# the generator ends -- the caller never sees the rest of the count.
# Find and fix it.
# Bug: `return count` immediately ends the generator on the first
# pass through the loop, so only one value is ever produced (and a
# bare `return` inside a generator would actually raise StopIteration
# with no value at all, but here it returns a value from the loop
# body, which is invalid inside a generator's flow -- the fix is to
# use `yield` instead of `return` so the function pauses and resumes.
def fixed_counter(n):
    count = 0
    while count < n:
        yield count
        count += 1

for value in fixed_counter(3):
    print(value)


# TODO 8 (Debug the Code): this custom context manager's __exit__
# method handles a ZeroDivisionError by printing a message, but it
# mistakenly returns True at the end no matter what -- silently
# swallowing the exception so the code that called it never finds out
# anything went wrong. Find and fix it so the exception still
# propagates after being logged.
# Bug: __exit__ returns True unconditionally, which tells Python the
# exception was fully handled and should not propagate further. Fix:
# return False (or nothing) so the exception keeps propagating after
# being logged.
class SafeDivider:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Handled: {exc_value}")
        return False

try:
    with SafeDivider():
        result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError correctly propagated")
