# Chapter 6 Exercises: Strings Deep Dive

These exercises use what Chapter 6 covered: indexing & slicing, common
string methods, f-strings, string immutability, and searching/validating
strings.

## How to run

```bash
python3 starter.py
```

## Task 1 — File extension extractor

Find `# TODO 1`. Given `filename = "vacation_photo.jpeg"`, use slicing to
extract just the file extension (`".jpeg"`) and print it.

## Task 2 — Email match checker

Find `# TODO 2`. Given `email1 = "  Bob@Example.COM  "` and
`email2 = "bob@example.com"`, normalize both (strip whitespace, lowercase)
and print whether they match.

## Task 3 — Receipt line with an f-string

Find `# TODO 3`. Given `item = "Desk Lamp"`, `price = 18.5`, and
`qty = 3`, use an f-string to print a receipt line in the form:
`"Desk Lamp x3 = $55.50"`.

## Task 4 — Username validator

Find `# TODO 4`. Given `username = "sky walker 99"`, check whether it
contains a space. Print `"Invalid username: no spaces allowed."` if it
does, or `"Username OK."` if it doesn't.

## Task 5 — Debug the Code

Find `# TODO 5`. This is supposed to print `"HELLO"`, but it prints
`"hello"` instead. Find and fix the bug (hint: think about what
`.upper()` actually returns, and what strings being immutable means for
this line).

## Task 6 — Word tally

Find `# TODO 6`. Given the `text` and `target` word, count how many
times `target` appears in `text` (using `.split()` and an accumulator),
then print the result in the form: `"to" appeared 2 times`.

## Checking your work

Compare your output against `solution.py`.
