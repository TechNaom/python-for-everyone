# Chapter 15 Practice Bank: OOP Deeper

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. This is the chapter
where `@staticmethod`, `@classmethod` (alternative constructors), and
`@property` (getters and setters) become allowed, on top of everything
from Chapters 1-14 (including general classes, `__init__`, instance
attributes, instance methods, `__str__`/`__repr__`). No inheritance
(Chapter 16), or any import beyond `math`/`datetime`/`random`/`csv`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: `@staticmethod`

1. Write a `TemperatureConverter` class with a `@staticmethod` `celsius_to_fahrenheit(celsius)` callable directly on the class.
2. Write a `StringHelper` class with a `@staticmethod` `is_palindrome(text)`.
3. Write a `MathHelper` class with a `@staticmethod` `is_prime(number)`.
4. Write a `Validator` class with a `@staticmethod` `is_valid_email(email)`.
5. **Debug the Code:** fix a `@staticmethod` that mistakenly includes `self` as a parameter.
6. **Scenario — A Shared Tax Calculator Utility:** write `TaxCalculator` with a `@staticmethod` `calculate_tax(subtotal, tax_rate)`.
7. **Scenario — Interview Prep:** explain why you'd use `@staticmethod` instead of a plain standalone function.

## Topic 2: `@classmethod` and Alternative Constructors

1. Write a `Pizza` class with a `@classmethod` `margherita(cls)` alternative constructor.
2. Write a `Date` class with a `@classmethod` `from_string(cls, date_string)` that parses `"YYYY-MM-DD"`.
3. Write an `Employee` class with a `@classmethod` `entry_level(cls, name)`.
4. Write a `Rectangle` class with a `@classmethod` `square(cls, side_length)`.
5. **Debug the Code:** fix a `@classmethod` that hardcodes the class name instead of using `cls(...)`.
6. **Scenario — Building a User from an API Response:** write `UserProfile` with a `@classmethod` `from_api_response(cls, data)`.
7. **Scenario — Interview Prep:** explain why a class needs more than one way to construct an instance.

## Topic 3: Encapsulation & Privacy Conventions

1. Write a `BankAccount` class using a single-underscore `_balance` convention with a `get_balance(self)` method.
2. Write a `Config` class demonstrating double-underscore name-mangling with `__secret_key`.
3. Write a `Person` class showing that a single-underscore attribute is still reachable from outside ("consenting adults").
4. Write a `Wallet` class using `__balance`, fully usable from inside the class's own methods.
5. **Debug the Code:** fix code trying to read a mangled double-underscore attribute with the wrong name.
6. **Scenario — Protecting an Internal Cache:** write `ReportCache` hiding a `__cache` dict behind `store`/`get` methods.
7. **Scenario — Interview Prep:** explain Python's "consenting adults" philosophy around private attributes.

## Topic 4: `@property` Getters

1. Write a `Circle` class with a `@property` `radius` read like a plain attribute.
2. Write a `Rectangle` class with a computed `@property` `area`.
3. Write a `Person` class with a `@property` `full_name` combining two stored attributes.
4. Write a `Temperature` class with a computed `@property` `fahrenheit`.
5. **Debug the Code:** fix a print statement that wrongly calls a `@property` with parentheses.
6. **Scenario — A Read-Only Derived Field on a User Profile:** write `UserProfile` with a computed `@property` `age`.
7. **Scenario — Interview Prep:** explain why you'd use `@property` instead of a regular `get_area()` method.

## Topic 5: `@x.setter` and Validation on Assignment

1. Write a `Circle` class with a `radius` setter that rejects negative values.
2. Write a `Person` class with an `age` setter that rejects negative values.
3. Write a `Product` class with a `price` setter that rejects negative values.
4. Write an `Email` class with an `address` setter that validates the presence of `"@"`.
5. **Debug the Code:** fix a `Thermostat` setter whose absolute-zero validation condition is backwards.
6. **Scenario — Validating Signup Form Data:** write `UserAccount` with a `username` setter that rejects blank input.
7. **Scenario — Interview Prep:** explain why validation belongs in a `@property` setter instead of only in `__init__`.

## Topic 6: Bringing It Together — Deeper OOP in Production

1. Write a `Product` class combining a validated `price` property, a `@staticmethod` `apply_tax`, and a `@classmethod` `on_sale`.
2. Write an `Employee` class combining a private auto-incrementing `id`, a validated `salary` property, and a `@classmethod` `hire_intern`.
3. Write an `InventoryItem` class combining a validated `quantity` property, a `restock` method routed back through the setter, and a `@staticmethod` `reorder_threshold`.
4. Write a `BankAccount` class combining a validated `balance` property, a `withdraw` method routed through the setter, and a `@classmethod` `open_with_bonus`.
5. **Debug the Code:** fix a `Subscription` class whose `__init__` bypasses its own setter's validation.
6. **Scenario — A Small Payroll System:** write `Employee` combining a `@staticmethod` monthly-to-annual conversion with a `@classmethod` alternative constructor.
7. **Scenario — Interview Prep:** describe how `@staticmethod`, `@classmethod`, and `@property` work together in a well-designed class.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
