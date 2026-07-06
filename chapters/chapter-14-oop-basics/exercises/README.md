# Chapter 14 Exercises: OOP Basics

These exercises use what Chapter 14 covered: defining classes,
`__init__` and instance attributes, instance methods, class attributes
vs. instance attributes (including the mutable class-attribute
gotcha), and the `__str__` dunder method.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — Classes & objects

Find `# TODO 1`. Write a class `Book` with an `__init__` that takes
`title` and `author` and stores them as instance attributes. Create two
`Book` objects with different titles/authors and print each one's
`title` and `author`.

## Task 2 — The `__init__` method & instance attributes

Find `# TODO 2`. Write a class `Movie` whose `__init__` takes `title`,
`year`, and `rating`, storing all three as instance attributes. Create
a `Movie` object for `"Arrival"`, `2016`, `8.0` and print its three
attributes.

## Task 3 — Instance methods

Find `# TODO 3`. Write a class `Counter` whose `__init__` takes no
arguments (besides `self`) and sets an instance attribute `count` to
`0`. Give it an instance method `increment(self, amount=1)` that adds
`amount` to `self.count`. Create a `Counter`, call
`increment()` once with no argument and once with `5`, then print
`count`.

## Task 4 — Class attributes vs. instance attributes

Find `# TODO 4`. Write a class `Employee` with a class attribute
`company_name = "Acme Corp"`, and an `__init__` that takes `name` and
`salary` and stores them as instance attributes. Create two `Employee`
objects and print each one's `company_name`, `name`, and `salary` to
show `company_name` is shared while `name`/`salary` are not.

## Task 5 — The mutable class-attribute gotcha

Find `# TODO 5`. Write a class `Playlist` whose `__init__` takes
`owner` and sets `self.owner`, and sets `self.songs` to a **new empty
list created inside `__init__`** (not a class attribute). Give it an
instance method `add_song(self, song)` that appends to `self.songs`.
Create two `Playlist` objects, add a different song to each, then print
both owners and their song lists to show they stay independent.

## Task 6 — Common dunder methods

Find `# TODO 6`. Write a class `Product` with an `__init__` that takes
`name` and `price`, and a `__str__` that returns
`f"{self.name}: ${self.price:.2f}"`. Create a `Product` for
`"Notebook"`, `2.5` and `print()` it directly to show `__str__` is used
automatically.

## Task 7 — Debug the Code

Find `# TODO 7`. This code defines a `Timer` class whose `tick` method
is missing `self` as its first parameter, so calling `timer.tick()`
raises a `TypeError`. Find and fix the method definition.

## Task 8 — Debug the Code: shared mutable class attribute

Find `# TODO 8`. This code defines a `Team` class with `members = []`
declared as a **class attribute**, so every `Team` object ends up
sharing and mutating the exact same list. Find and fix it so each
`Team` gets its own independent `members` list, set up inside
`__init__`.

## Checking your work

Compare your output against `solution.py`. Every example here uses
fixed, explicit values, so your output should match `solution.py`
exactly.
