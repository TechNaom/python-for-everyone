# Chapter 16 Practice Bank: Inheritance & Polymorphism

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. This is the chapter
where inheritance becomes allowed: `class Child(Parent):`,
`super().__init__(...)`, method overriding, polymorphism, and
`isinstance()`/`type()` checks, on top of everything from Chapters
1-15 (including general classes, `__init__`, instance/class
attributes, instance methods, dunder methods, `@staticmethod`,
`@classmethod`, and `@property`). No import beyond
`math`/`datetime`/`random`/`csv`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Basic Inheritance

1. Write an `Animal` class and a `Dog` class inheriting from it, showing what a subclass gets automatically.
2. Write a `Vehicle` class and a `Car` class that inherits its methods without redefining them.
3. Write an `Employee` class and a `Manager` class that inherits its attributes.
4. Write a `Shape` class and a `Square` class that inherits an unmodified method.
5. **Debug the Code:** fix a subclass definition that forgot to put the parent class in parentheses.
6. **Scenario — Modeling a Fleet of Vehicles:** write a `Vehicle` base class and a `Truck` subclass that reuses it without any new code.
7. **Scenario — Interview Prep:** explain what "inheritance" means and what a subclass gets for free.

## Topic 2: `super().__init__()`

1. Write an `Animal` class and a `Dog` subclass that uses `super().__init__()` to reuse the parent's setup and adds a breed attribute.
2. Write a `Person` class and a `Student` subclass that uses `super().__init__()` plus a school attribute.
3. Write a `Shape` class and a `Rectangle` subclass that uses `super().__init__()` plus extra attributes.
4. Write a `Vehicle` class and a `Motorcycle` subclass that uses `super().__init__()` plus a has_sidecar attribute.
5. **Debug the Code:** fix a subclass `__init__` that forgot to call `super().__init__()`, leaving a parent attribute unset.
6. **Scenario — Extending a Base Employee Record:** write an `Employee` class and a `Manager` subclass using `super().__init__()` plus a `direct_reports` attribute.
7. **Scenario — Interview Prep:** explain why `super().__init__()` is preferred over copy-pasting the parent's setup code.

## Topic 3: Method Overriding

1. Write an `Animal` class with a `speak` method and a `Cat` subclass that overrides it.
2. Write a `Shape` class with a `describe` method and a `Circle` subclass that overrides and extends it with `super().describe()`.
3. Write an `Employee` class with a `describe` method and a `Manager` subclass that overrides and extends it.
4. Write a `Notification` class with a `send` method and an `SMSNotification` subclass that overrides it.
5. **Debug the Code:** fix an overriding method that misspelled the parent method's name, so it defines a new method instead of overriding.
6. **Scenario — Customizing a Shared Receipt Formatter:** write a `Receipt` class with a `format_line` method and a `DiscountedReceipt` subclass that overrides and extends it with `super()`.
7. **Scenario — Interview Prep:** explain the difference between overriding a method and extending it with `super()`.

## Topic 4: Polymorphism

1. Write `Cat` and `Dog` subclasses of `Animal`, each overriding `speak`, then loop over a list of both and call `speak()` on each without checking type.
2. Write `Circle` and `Rectangle` subclasses of `Shape`, each overriding `area`, then loop over a list of both to total their areas.
3. Write `Manager` and `Developer` subclasses of `Employee`, each overriding `describe`, then loop over a list of both and print each description.
4. Write `EmailNotification` and `SMSNotification` subclasses of `Notification`, each overriding `send`, then loop over a list of both and collect each result.
5. **Debug the Code:** fix a loop that uses `if`/`elif` type-checks before calling a method, defeating the point of polymorphism.
6. **Scenario — A Payment Processor Supporting Multiple Payment Types:** write `CardPayment` and `PayPalPayment` subclasses of `Payment`, each overriding `process`, and process a mixed list polymorphically.
7. **Scenario — Interview Prep:** explain why polymorphism removes the need for type-checking `if`/`elif` chains.

## Topic 5: `isinstance()` vs `type()`

1. Write an `Animal` class and a `Dog` subclass, then compare what `isinstance(dog, Animal)` returns versus `type(dog) == Animal`.
2. Write a `Shape` class and a `Circle` subclass, then use `isinstance()` to safely check membership in a mixed list.
3. Write a `Vehicle` class and a `Car` subclass, then show `isinstance()` returning `True` for both `Car` and `Vehicle` while `type()` only matches the exact class.
4. Write an `Employee` class and a `Manager` subclass, then use `isinstance()` to filter a list down to only manager-type entries.
5. **Debug the Code:** fix code that uses `type(obj) == ParentClass` to check membership, which fails for subclass instances.
6. **Scenario — Validating Mixed Input Before Processing:** write a function that uses `isinstance()` to accept both a `Payment` and any of its subclasses safely.
7. **Scenario — Interview Prep:** explain when you'd reach for `isinstance()` over `type()`, and why `isinstance()` is usually the safer choice.

## Topic 6: Bringing It Together — Inheritance & Polymorphism in Production

1. Write a `Shape` base class and `Rectangle`/`Circle` subclasses combining `super().__init__()`, an overridden `area` method, and a polymorphic total.
2. Write an `Employee` base class and `Manager`/`Developer` subclasses combining `super().__init__()`, an overridden `describe` method, and `isinstance()` filtering.
3. Write a `Notification` base class and `EmailNotification`/`SMSNotification` subclasses combining `super().__init__()`, an overridden `send` method, and a polymorphic loop.
4. Write a `Vehicle` base class and `Car`/`Truck` subclasses combining `super().__init__()`, an overridden `describe` method, and `isinstance()`-based categorization.
5. **Debug the Code:** fix a subclass whose overriding method entirely skips calling `super()`, silently dropping shared parent behavior it was supposed to extend.
6. **Scenario — A Small Media Library:** write a `MediaItem` base class and `Book`/`Movie` subclasses combining `super().__init__()`, an overridden `summary` method, and a polymorphic report.
7. **Scenario — Interview Prep:** describe a real system where inheritance was the right tool, and a case where composition (an object holding another instead of inheriting from it) would have been the better choice.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
