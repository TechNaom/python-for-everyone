# Chapter 15 Exercises: OOP Deeper

These exercises use what Chapter 15 covered: `@staticmethod`,
`@classmethod` and alternative constructors, encapsulation naming
conventions (`_name`, `__name`), and `@property` getters and setters.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — `@staticmethod`

Find `# TODO 1`. Write a class `TemperatureTools` with a static method
`is_valid_celsius(value)` that returns `True` if `value` is an `int` or
`float` and is greater than or equal to `-273.15` (absolute zero), and
`False` otherwise. Call it with `25` and with `-500` and print both
results.

## Task 2 — `@classmethod` & an alternative constructor

Find `# TODO 2`. Write a class `Employee` whose `__init__` takes `name`
and `salary`, storing both as instance attributes. Add a class method
`from_string(cls, employee_data)` that takes one comma-separated string
like `"Alice,60000"`, splits it, and returns a new `Employee` built with
`cls(...)`. Create one `Employee` with `Employee("Priya", 72000)` and
one with `Employee.from_string("Sam,58000")`, then print each one's
`name` and `salary`.

## Task 3 — Encapsulation with a single underscore

Find `# TODO 3`. Write a class `Vault` whose `__init__` takes `contents`
and stores it as `self._contents` (single underscore, by convention).
Give it an instance method `peek(self)` that returns `self._contents`.
Create a `Vault` with `"gold bars"` and print the result of calling
`peek()`.

## Task 4 — `@property` getter

Find `# TODO 4`. Write a class `Circle` whose `__init__` takes `radius`
and stores it as `self._radius`. Add a read-only property `radius` that
returns `self._radius`. Create a `Circle` with radius `4` and print
`circle.radius` (no parentheses).

## Task 5 — Property setter with validation

Find `# TODO 5`. Write a class `Thermostat` whose `__init__` takes
`temperature` and stores it as `self._temperature`. Add a `temperature`
property with a getter that returns `self._temperature`, and a setter
that raises `ValueError` if the new value is below `-50` or above
`150`, otherwise stores it. Create a `Thermostat` at `70`, set its
`temperature` to `72` and print it, then try setting it to `200` inside
a `try`/`except ValueError` block and print the caught error message.

## Task 6 — Bringing it together

Find `# TODO 6`. Write a class `Product` that combines this chapter's
tools: a class attribute `store_name = "Downtown Market"`; `__init__`
taking `name` and `price`, storing `price` through the property (not
directly as `self._price`) so validation runs immediately; a static
method `is_valid_price(value)` returning `True` only for a positive
`int`/`float`; a `price` property with a getter and a setter that
raises `ValueError` for any non-positive value using
`is_valid_price`; and a `__str__` returning
`f"{self.name}: ${self.price:.2f}"`. Create a `Product` named
`"Notebook"` priced at `2.5`, print it, then try setting its `price` to
`-1` inside a `try`/`except ValueError` block and print the caught
error message.

## Task 7 — Debug the Code

Find `# TODO 7`. This code defines a `Circle` class meant to expose
`area` as a property, but the method is missing its `@property`
decorator — so `circle.area` (accessed like an attribute) raises a
`TypeError` instead of returning the computed area. Find and fix it.

## Task 8 — Debug the Code: a setter that doesn't validate

Find `# TODO 8`. This code defines an `Account` class with a `balance`
property and a `@balance.setter`, but the setter accepts any value
at all — including negative numbers — defeating the entire point of
wrapping `_balance` in a property. Find and fix the setter so it raises
`ValueError` for any negative value instead of silently accepting it.

## Checking your work

Compare your output against `solution.py`. Every example here uses
fixed, explicit values, so your output should match `solution.py`
exactly.
