"""
Chapter 17 Exercises: Generators, Iterators & Context Managers
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py
"""

# TODO 1: Write a class Countdown whose __init__ takes start and
# stores it as self.current. Give it __iter__(self) that returns
# self, and __next__(self) that raises StopIteration once
# self.current is 0 or less, otherwise returns the current value and
# decrements it by 1. Create a Countdown(4) and loop over it with a
# for loop, printing each value.


# TODO 2: Write a generator function evens_up_to(n) that starts a
# counter at 0 and, while the counter is less than or equal to n,
# yields the counter and then increases it by 2. Loop over
# evens_up_to(10) with a for loop and print each value.


# TODO 3: Use sum() with a generator expression (not a list
# comprehension) to add up the cubes (n ** 3) of every number from 1
# to 5 inclusive. Store the result in total and print it.


# TODO 4: Use with open(...) as f: to write the three lines "1", "2",
# and "3" (each on its own line) to a file named "numbers.txt". Then
# use a second with open(...) as f: block to read all the lines back
# with .readlines() into a variable lines. Print len(lines), then
# print f.closed right after the block ends.


# TODO 5: Write a class Timer with __enter__(self) that sets
# self.entered = True and returns self, and
# __exit__(self, exc_type, exc_value, traceback) that sets
# self.exited = True and returns False. Use with Timer() as t: pass
# and then print t.entered and t.exited.


# TODO 6: Write a generator function read_lines(filename) that opens
# the file with with, loops over it with for line in f:, and yields
# each line with .strip() applied. First, write the three lines
# "alpha", "beta", and "gamma" to a file named "stream.txt" using
# with open(...) as f:. Then loop over read_lines("stream.txt") with
# a for loop and print each line.


# TODO 7 (Debug the Code): this generator function accidentally uses
# return count instead of yield count inside its loop, so calling it
# and looping over it only ever produces the very first value before
# the generator ends -- the caller never sees the rest of the count.
# Find and fix it.
def broken_counter(n):
    count = 0
    while count < n:
        return count
        count += 1

for value in broken_counter(3):
    print(value)


# TODO 8 (Debug the Code): this custom context manager's __exit__
# method handles a ZeroDivisionError by printing a message, but it
# mistakenly returns True at the end no matter what -- silently
# swallowing the exception so the code that called it never finds out
# anything went wrong. Find and fix it so the exception still
# propagates after being logged.
class SafeDivider:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Handled: {exc_value}")
        return True

with SafeDivider():
    result = 10 / 0
print("This should never print, since the exception should propagate.")
