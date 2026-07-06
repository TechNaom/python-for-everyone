# Chapter 14 Practice Bank: OOP Basics

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. This is the chapter
where general classes become allowed: everything from Chapters 1-13
(including custom exception classes) plus class definitions,
`__init__`, instance attributes, class attributes, instance methods,
and `__str__`/`__repr__`. No `@staticmethod`, `@classmethod`,
`@property` (Chapter 15), inheritance (Chapter 16), or any import
beyond `math`/`datetime`/`random`/`csv`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Classes & Objects

1. Write a `Book` class with just `pass`, create two separate instances, and confirm they're independent objects with `is`.
2. Write a `Dog` class with just `pass`, then set `.name`/`.breed` directly on an instance from outside the class.
3. Write `describe_instance(obj)`, showing an object's default string form alongside `type(obj).__name__`.
4. Write a `Wallet` class, set `.balance` on only one of two instances, and catch the `AttributeError` on the other.
5. **Debug the Code:** fix code that assigns the same `Ticket` object to two names instead of creating two separate instances.
6. **Scenario — Modeling Real-World "Things" as Objects:** create two independent `SupportTicket` instances with their own `.subject` values.
7. **Scenario — Interview Prep:** explain the difference between a class and an object.

## Topic 2: `__init__` and Instance Attributes

1. Write a `Book` class with `__init__(self, title, author)` storing both as instance attributes.
2. Write a `Point` class with `__init__(self, x, y)` storing both.
3. Write an `Employee` class with `__init__(self, name, salary=50000)`, using a default argument.
4. Write a `Rectangle` class with `__init__(self, width, height)` storing both.
5. **Debug the Code:** fix an `__init__` that assigns to a local variable `name` instead of `self.name`, losing the value.
6. **Scenario — Building a User Record at Signup:** write `UserAccount` with `__init__(self, username, email)`.
7. **Scenario — Interview Prep:** explain what `__init__` actually is and when Python calls it.

## Topic 3: Instance Methods & `self`

1. Write a `Counter` class with `increment(self)` that adds 1 to `self.value`.
2. Write a `BankAccount` class with `deposit(self, amount)` and `withdraw(self, amount)` methods.
3. Write a `Rectangle` class with an `area(self)` method returning `self.width * self.height`.
4. Write a `Greeter` class with a `greet(self)` method returning a personalized string.
5. **Debug the Code:** fix a method missing `self` as its first parameter.
6. **Scenario — A Shopping Cart's Running Total:** write `ShoppingCart` with `add_item(self, name, price)` updating a running list and total.
7. **Scenario — Interview Prep:** explain what `self` refers to and why every instance method needs it.

## Topic 4: Class Attributes vs. Instance Attributes

1. Write a `Circle` class with a shared class attribute `pi` and an `area(self)` method that uses it.
2. Write an `Employee` class with a shared class attribute `company_name`, confirmed identical across instances.
3. Write a `Product` class with a class attribute `total_products_created` incremented in `__init__`.
4. Write a `Vehicle` class with a class attribute `wheels`, then override it on one instance and show the class attribute is untouched.
5. **Debug the Code (the mutable class attribute gotcha):** fix a `Cart` class whose `items = []` was defined at the class level instead of inside `__init__`, causing every instance to share one list.
6. **Scenario — A Shared Interest Rate Across All Accounts:** write `SavingsAccount` with a class-level `interest_rate` applied in `apply_interest(self)`.
7. **Scenario — Interview Prep:** explain the mutable class attribute bug and why it happens.

## Topic 5: `__str__` and `__repr__`

1. Write a `Book` class with a `__str__(self)` method used automatically by `print()`.
2. Write a `Point` class with a `__repr__(self)` method used automatically by `repr()`.
3. Write a `Temperature` class with both `__str__` and `__repr__`, showing they can differ.
4. Write a `Money` class with a `__str__(self)` method formatting an amount to 2 decimal places.
5. **Debug the Code:** fix a class whose display method is misspelled `__string__` instead of `__str__`.
6. **Scenario — Friendly Logging Output:** write `OrderEvent` with a `__str__(self)` producing a clean log line.
7. **Scenario — Interview Prep:** explain the difference between `__str__` and `__repr__` and when each is used.

## Topic 6: Bringing It Together — OOP Basics in Production

1. Write an `InventoryItem` class combining an instance method, `__str__`, and a computed value.
2. Write a `Task` class using a class-attribute counter (`next_id`) to auto-assign unique ids.
3. Write a `Playlist` class with its own fresh instance list of songs and a method-based song count.
4. Write a `TemperatureLog` class with an `average(self)` method that safely handles an empty list.
5. **Debug the Code:** fix a `Team` class whose `members = []` was a shared class attribute instead of a per-instance list.
6. **Scenario — A Small Order-Processing System:** write `Order` combining line items, a running total, and a status change into one object.
7. **Scenario — Interview Prep:** describe why real production codebases organize data and behavior into classes instead of loose dicts and functions.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
