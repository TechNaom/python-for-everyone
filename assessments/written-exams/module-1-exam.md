# Module 1 Written Exam — Foundations

Covers Chapters 1-5: Your First Python Program, Variables & Data Types,
Operators, Control Flow, and Loops.

**Format:** 8 short-answer + 3 scenario questions + 1 synthesis question.
Suggested time: 45 minutes. Closed notes recommended for the first
attempt; open notes is fine for self-paced learners checking their own
understanding.

---

## Section A — Short Answer (2 points each, 16 points)

**A1.** What does `print()` do, and what does `input()` do differently?

**A2.** Why is Python described as "dynamically typed"?

**A3.** What's the difference between `type()` and `id()`?

**A4.** Name the five basic data types covered so far.

**A5.** What does `bool("False")` (the string) evaluate to, and why?

**A6.** What's the difference between `/` and `//`?

**A7.** Why doesn't Python have a `++` operator?

**A8.** What is short-circuit evaluation?

---

## Section B — Scenario Questions (6 points each, 18 points)

**B1.** You write `if age = 18:` and Python raises a `SyntaxError`. What's
wrong, and what should the line be?

**B2.** A grading elif chain always outputs "D" no matter the score, even
for a 95. The chain checks `score >= 40` before `score >= 75`. Explain the
bug and how to fix it.

**B3.** A while loop meant to print 1 to 10 never stops running. What is
the most likely missing piece, and how would you fix it?

---

## Section C — Synthesis (6 points)

**C1.** Write a short program (pseudocode or real Python) that asks the
user for a number, converts it to an integer, and prints whether it's
even or odd. Your answer should correctly use concepts from at least
three different chapters in this module.

---

## Answer Key

**A1.** `print()` displays a value to the screen (output). `input()`
displays a prompt and pauses execution to receive typed text from the
user (input) — it always returns a string.

**A2.** Because a variable's type is determined automatically from the
value assigned to it at runtime, rather than being declared upfront by
the programmer — and the same variable name can hold different types at
different points in the program.

**A3.** `type()` returns a value's data type (str, int, etc.). `id()`
returns a value's memory address — where it lives, not what it is.

**A4.** `str`, `int`, `float`, `bool`, `complex`.

**A5.** It evaluates to `True`. `bool()` on a string only checks whether
the string is empty, not what the text says — any non-empty string
(including the literal text `"False"`) converts to `True`.

**A6.** `/` is true division and always returns a float, even when the
result is a whole number. `//` is floor division — it divides and rounds
the result down to the nearest whole number.

**A7.** It was a deliberate design choice: `++` in other languages secretly
has two different behaviors (pre- vs. post-increment) depending on
position, which causes subtle bugs. Python requires the unambiguous
`x += 1` instead.

**A8.** Python stops evaluating a logical expression (`and`/`or`) as soon
as the final result is already determined, without checking the remaining
operands. This lets you safely write guard conditions like
`x != 0 and 10 / x > 1`.

**B1.** A single `=` is assignment, not comparison, and Python does not
allow assignment inside an `if` condition. It should be
`if age == 18:` (double equals).

**B2.** In an elif chain, Python stops at the first condition that's
true, checking top to bottom. Since `score >= 40` is checked first, a
score of 95 matches it immediately and never reaches the `>= 75` check.
Fix: reorder the conditions from highest threshold to lowest
(`>= 75` first, then `>= 60`, `>= 50`, `>= 40`, then `else`).

**B3.** Almost certainly a missing (or misplaced) increment/step —
without something like `i += 1` inside the loop body, the loop's
condition variable never changes and the condition never becomes false.
Fix: make sure the loop variable is updated inside the loop body, in a
way that eventually makes the condition false.

**C1.** A correct answer converts input with `int()` (Chapter 2), uses
the `%` operator (Chapter 3), and an if-else (Chapter 4) — for example:

```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
```

---

## Grading Guidance

| Section | Points | Notes |
|---|---|---|
| A (8 x 2) | 16 | Award partial credit (1 pt) for a mostly-correct answer missing precise terminology. |
| B (3 x 6) | 18 | Full credit requires both identifying the bug AND stating the fix. |
| C (1 x 6) | 6 | Award full credit for any correct approach; code doesn't need to match the sample exactly. |
| **Total** | **40** | 34+ = strong grasp of Module 1; 24-33 = solid but revisit weak areas; below 24 = re-read the relevant chapters before Module 2. |
