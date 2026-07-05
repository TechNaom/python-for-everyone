# Chapter 8 Exercises: Dictionaries & Sets

These exercises use what Chapter 8 covered: creating & accessing
dictionaries, dictionary methods, looping over dictionaries, sets & set
operations, nested dictionaries, and real-world tallying/lookup patterns.

## How to run

```bash
python3 starter.py
```

## Task 1 — Creating & accessing a dictionary

Find `# TODO 1`. Given
`student = {"name": "Maria", "age": 20, "major": "Biology"}`, print the
student's name and major. Then use `.get()` to safely print the student's
`"gpa"` with a fallback of `"N/A"`, since `"gpa"` isn't a key here.

## Task 2 — Dictionary methods

Find `# TODO 2`. Given `inventory = {"pens": 40, "notebooks": 25}`, add a
new key `"erasers"` set to `15`. Then use `.update()` to add
`"markers": 10` and change `"pens"` to `35`, both in one call. Print the
inventory after each step.

## Task 3 — Looping over a dictionary

Find `# TODO 3`. Given
`scores = {"Maria": 88, "Jae": 95, "Tomas": 71}`, loop over the
dictionary with `.items()` and print each name and score. Also build a
running total of every score and print the average score.

## Task 4 — Set operations

Find `# TODO 4`. Given
`weekday_class = {"Maria", "Jae", "Tomas"}` and
`weekend_class = {"Jae", "Priya"}`, print the union, the intersection,
and the difference (people in `weekday_class` but not `weekend_class`).

## Task 5 — Nested dictionaries

Find `# TODO 5`. Given a nested dictionary of student records, print
Jae's major, then add a new `"gpa"` field to Tomas's record set to
`3.4`, then print Tomas's whole record.

## Task 6 — Debug the Code

Find `# TODO 6`. This is supposed to tally how many times each fruit
appears in a list, but it crashes with a `KeyError`. Find and fix the
bug (hint: think about what happens the *first* time a fruit is seen,
before it has an entry in `tally` yet).

## Task 7 — Order report

Find `# TODO 7`. Given a list of orders (each one a dictionary with
`"id"`, `"amount"`, and `"status"` keys), loop through them, and for
every order with status `"shipped"`, print its id and add its amount to
a running total. Print the total in the form: `"Total shipped: $107.25"`.

## Checking your work

Compare your output against `solution.py`.
