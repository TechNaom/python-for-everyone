# Chapter 5 Practice Bank: Loops (while / for)

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder -- including scenario-based problems written
in the same style you'll see in real interviews. Loops are a classic
interview area, so several of these lean directly into that. Uses only
what Chapters 1-5 covered: `print()`, variables, `input()`, basic types,
arithmetic/relational/logical operators, `if`/`elif`/`else`, `while`
loops, `for` loops with `range()`, the accumulator pattern, and
`break`/`continue`.

## How to run

```bash
python3 starter.py
```

## Topic 1: `while` loops

1. Print the numbers 1 through 5 with a `while` loop.
2. Count down from 10 to 1 with a `while` loop.
3. Print every even number from 2 to 20 with a `while` loop, stepping by 2.
4. Start a variable at 1 and keep doubling it while it's `<= 100`, printing each value.
5. **Debug the Code:** fix a `while` loop that never updates its loop variable and would otherwise run forever.
6. **Scenario -- Launch Sequence:** count down from 5 to 1, then print `"Liftoff! 🚀"`.
7. **Scenario -- Interview Prep:** explain why `while True:` never stops on its own, then write a safe, bounded while loop as contrast.

## Topic 2: `for` loops and `range()`

1. Print the numbers 1 through 5 with `for` + `range()`.
2. Print every multiple of 5 from 0 to 45 using `range()`'s start/stop/step form.
3. Count down from 10 to 1 using `range()`'s negative step form.
4. Print "even"/"odd" for every number 1-20 using `for` + `if`/`else`.
5. **Debug the Code:** fix an off-by-one `range()` bound that stops one short of 10.
6. **Scenario -- Multiplication Table:** print the multiplication table of 12, from `12 x 1` to `12 x 10`.
7. **Scenario -- Interview Prep:** print only even numbers 1-20 using `range()`'s step, without checking each number with `%`.

## Topic 3: Common loop patterns (the accumulator pattern)

1. Sum the numbers 1 through 10 with a `while` loop and the accumulator pattern.
2. Sum the numbers 1 through 100 with a `for` loop and the accumulator pattern.
3. Count how many numbers from 1 to 50 are divisible by 3, using a count accumulator.
4. **Debug the Code:** fix an accumulator that gets reset to 0 inside the loop instead of before it.
5. Compute 5 factorial (5!) using a product accumulator (started at 1, not 0).
6. **Scenario -- Daily Transactions:** sum three hard-coded transaction amounts, picked with a counter and `if`/`elif`, inside a `while` loop.
7. **Scenario -- Interview Prep -- Palindrome Check:** reverse a number's digits with the `%`/`//` pattern and check if it's a palindrome.

## Topic 4: `break` & `continue`

1. Use `break` to stop a `for` loop over `range(1, 21)` the moment it reaches 15.
2. Use `continue` to skip printing multiples of 3 in a `for` loop over `range(1, 11)`.
3. Combine `break` and `continue`: print only the even numbers up to 20, stopping after 20.
4. **Debug the Code:** fix a loop that uses `break` where it should use `continue`, so it stops instead of just skipping one number.
5. Use a `while` loop with `break` to find the first number over 100 divisible by both 7 and 3.
6. **Scenario -- Retry Attempt Simulator (Interview Prep):** simulate a 3-attempt login check with a `while` loop and `break`.
7. **Scenario -- Sensor Data Cleanup:** skip negative (glitched) sensor readings with `continue` while summing the valid ones.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match -- the goal is that your program runs without errors and
does what each TODO asks.
