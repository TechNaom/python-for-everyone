# Chapter 4 Project: Grade Calculator

A report-card generator built entirely from if/elif/else — the exact
kind of grading logic used by real school and university systems.

## What you'll build

A script that asks for marks in 5 subjects, calculates the average, and
assigns a letter grade using this scale:

| Average | Grade |
|---|---|
| 75 and above | A |
| 60 - 74 | B |
| 50 - 59 | C |
| 40 - 49 | D |
| below 40 | Fail |

Example run:

```
Enter marks in Math: 80
Enter marks in Science: 70
Enter marks in English: 65
Enter marks in History: 90
Enter marks in Computer Science: 85

=== Report Card ===
Average: 78.0
Grade: A
```

## How to run it

```bash
python3 starter.py
```

Fill in the `# TODO` sections in `starter.py`. Want to see one finished
version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Add a check that rejects marks above 100 or below 0 (a peek ahead —
  this is easy once you've seen more of `if`, which you already have!).
- Print which subject was the strongest and weakest.
- Add a "Distinction" grade for averages above 90.

## Why this project matters

Grading logic like this appears constantly in real systems: eligibility
checks, pricing tiers, risk scoring, access levels. The elif-chain
ordering skill you practiced here — most specific or highest threshold
first — is a genuinely transferable skill, not just a school exercise.
