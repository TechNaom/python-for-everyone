"""
Chapter 5 Practice Bank: Loops (while / for)
See README.md in this folder for full instructions.

Only uses what Chapters 1-5 covered: print(), variables, input(), basic
types, arithmetic/relational/logical operators, if/elif/else, while
loops, for loops with range(), the accumulator pattern, and
break/continue. No functions, no list/dict literals, no comprehensions,
no f-strings.
"""

# ============================================================
# Topic 1: while loops
# ============================================================

# TODO 1.1: Use a while loop to print the numbers 1 through 5, one per
# line.


# TODO 1.2: Use a while loop to count down from 10 to 1, one number per
# line (no message after the loop yet -- that comes in the scenario
# below).


# TODO 1.3: Use a while loop to print every even number from 2 to 20
# (inclusive), stepping by 2 each time.


# TODO 1.4: Use a while loop that starts a variable `value` at 1 and
# keeps doubling it (value = value * 2) and printing it, for as long as
# value is less than or equal to 100.


# TODO 1.5 (Debug the Code): The while loop below is supposed to print 1
# through 5, but it's missing the step that updates the loop variable --
# running it as-is would loop forever. It's commented out here so this
# file doesn't hang when you run it. Uncomment it, add the missing step,
# and confirm it now prints 1 through 5 and stops.
# i = 1
# while i <= 5:
#     print(i)


# TODO 1.A (Scenario -- Launch Sequence): Mission control needs a
# countdown script. Use a while loop to count down from 5 to 1, one
# number per line, then print "Liftoff! \U0001F680" after the loop ends.


# TODO 1.B (Scenario -- Interview Prep): An interviewer asks why
# `while True:` with no `break` and no changing condition never stops on
# its own. Add a comment answering in your own words, then write a SAFE,
# bounded while loop (not `while True`) that counts from 1 to 3, to show
# you know how to avoid the trap.


# ============================================================
# Topic 2: for loops and range()
# ============================================================

# TODO 2.1: Use a for loop with range() to print the numbers 1 through
# 5.


# TODO 2.2: Use a for loop with range()'s start/stop/step form to print
# every multiple of 5 from 0 to 45 (inclusive).


# TODO 2.3: Use a for loop with range()'s negative step form to count
# down from 10 to 1.


# TODO 2.4: Use a for loop over range(1, 21) and, for each number, print
# whether it's "even" or "odd" using an if/else check with %.


# TODO 2.5 (Debug the Code): This loop is supposed to print 1 through 10
# inclusive, but it stops at 9 because of an off-by-one error in the
# range() bounds. Fix it.
for i in range(1, 10):
    print(i)


# TODO 2.A (Scenario -- Multiplication Table): Your manager wants a
# quick reference sheet for order quantities of 12 units. Use a for loop
# with range() to print the multiplication table of 12, from 12 x 1 to
# 12 x 10.


# TODO 2.B (Scenario -- Interview Prep): An interviewer asks you to
# print only the even numbers from 1 to 20 -- but without checking each
# number with % 2. Use range()'s step argument so it only ever generates
# even numbers in the first place.


# ============================================================
# Topic 3: Common loop patterns (the accumulator pattern)
# ============================================================

# TODO 3.1: Use a while loop and the accumulator pattern to compute the
# sum of the numbers 1 through 10 (start total at 0), then print the
# final total.


# TODO 3.2: Use a for loop over range() and the accumulator pattern to
# compute the sum of the numbers 1 through 100, then print the total.


# TODO 3.3: Use a for loop over range(1, 51) and a count accumulator
# (started at 0) to count how many numbers from 1 to 50 are evenly
# divisible by 3, then print the count.


# TODO 3.4 (Debug the Code): This loop is supposed to add up 1 through 5
# into `total`, but `total` gets reset to 0 INSIDE the loop on every
# iteration instead of once before it starts, so the final total is
# wrong. Fix it by moving the initialization outside the loop.
for i in range(1, 6):
    total = 0
    total += i
print(total)


# TODO 3.5: Use a for loop over range(1, 6) and a product accumulator
# (started at 1, not 0!) to compute 5 factorial (5! = 1*2*3*4*5), then
# print the result.


# TODO 3.A (Scenario -- Daily Transactions): Three transactions came in
# today: $19.99, $45.50, and $12.25. Using a while loop (a counter from
# 1 to 3) and an if/elif chain to pick the right amount each time, add
# each transaction to a running total, then print the day's total.


# TODO 3.B (Scenario -- Interview Prep -- Palindrome Check): A classic
# interview warm-up. Given n = 1221, use a while loop and the
# digit-peeling pattern (% and //) to build the reversed number, then
# compare it to the original and print whether n is a palindrome.


# ============================================================
# Topic 4: break & continue
# ============================================================

# TODO 4.1: Use a for loop over range(1, 21) that breaks out immediately
# when the loop variable reaches 15 -- printing every number before that
# point, then stopping (nothing from 15 onward should print).


# TODO 4.2: Use a for loop over range(1, 11) that uses continue to skip
# printing any multiple of 3, while still printing every other number.


# TODO 4.3: Use a for loop over range(1, 31) that breaks once the loop
# variable exceeds 20, and uses continue to skip odd numbers -- so it
# ends up printing only the even numbers from 1 up to 20.


# TODO 4.4 (Debug the Code): This loop is supposed to SKIP multiples of
# 4 (using continue) while printing every other number from 1 to 20, but
# it uses break instead of continue, so it stops completely at the
# first multiple of 4 instead of skipping just that one number. Fix it.
for i in range(1, 21):
    if i % 4 == 0:
        break
    print(i)


# TODO 4.5: Use a while loop with break to find the first number greater
# than 100 that's evenly divisible by both 7 and 3, then print it and
# stop the loop with break as soon as it's found.


# TODO 4.A (Scenario -- Retry Attempt Simulator -- Interview Prep): A
# login system allows at most 3 attempts. The correct code is "1234".
# The simulated attempts (in order) are "0000", "9999", and "1234" --
# picked with a counter and if/elif (no lists yet!). Use a while loop
# with break: if an attempt matches, print "Access granted" and break;
# otherwise print "Incorrect, try again." If all 3 attempts are used
# without a match, print "Account locked" (track this with a plain
# True/False flag variable, checked after the loop ends).


# TODO 4.B (Scenario -- Sensor Data Cleanup): A weather station logs 5
# temperature readings using the formula reading = (i * 10) - 25 for i
# in range(1, 6) -- giving -15, -5, 5, 15, 25. Negative readings are
# sensor glitches and should be skipped (not counted) using continue.
# Use a for loop to sum only the non-negative readings, then print the
# total.
