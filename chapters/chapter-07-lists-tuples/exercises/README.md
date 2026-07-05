# Chapter 7 Exercises: Lists & Tuples

These exercises use what Chapter 7 covered: creating & accessing lists,
list methods, tuples & unpacking, nested lists, copying vs. aliasing, and
real-world batch/record processing.

## How to run

```bash
python3 starter.py
```

## Task 1 — Playlist slicing

Find `# TODO 1`. Given
`playlist = ["Intro", "Song A", "Song B", "Song C", "Outro"]`, use slicing
to print the first 3 songs, then the last 2 songs.

## Task 2 — Cart methods

Find `# TODO 2`. Given `cart = ["notebook", "pen"]`, append `"eraser"`,
then insert `"ruler"` at position 1, then remove `"pen"`. Print the cart
after each step.

## Task 3 — Tuple unpacking

Find `# TODO 3`. Given `location = ("Austin", "TX", 78701)`, unpack it
into `city`, `state`, and `zip_code`, then print: `"Austin, TX 78701"`.

## Task 4 — Nested list grid

Find `# TODO 4`. Given a 3x3 `grid` of numbers, print the value at row 1,
column 2, then change row 0, column 0 to `100` and print the whole grid.

## Task 5 — Debug the Code

Find `# TODO 5`. This is supposed to leave `original` untouched and only
change `backup`, but it changes both. Find and fix the bug (hint: think
about what actually makes a list a copy, versus just another name for the
same list).

## Task 6 — Order report

Find `# TODO 6`. Given a list of orders (each one
`[order_id, amount, status]`), loop through them, and for every order with
status `"shipped"`, print its id and add its amount to a running total.
Print the total in the form: `"Total shipped: $107.25"`.

## Checking your work

Compare your output against `solution.py`.
