# Module 3 Written Exam — OOP & Robust Code

Covers Chapters 11-16: Modules & Packages, Exception Handling, File
Handling & CSV, OOP Basics, OOP Deeper, and Inheritance & Polymorphism.

**Format:** 8 short-answer + 3 scenario questions + 1 synthesis question.
Suggested time: 60 minutes. Closed notes recommended for the first
attempt; open notes is fine for self-paced learners checking their own
understanding.

---

## Section A — Short Answer (2 points each, 16 points)

**A1.** What's the difference between `import math` and
`from math import sqrt`, in terms of how you then call the function?

**A2.** Why does `except Exception:` (with no more specific exception
type) usually make debugging harder, even though it "works"?

**A3.** What's wrong with opening a file using `f = open("data.txt")`
without a `with` block, even if you remember to call `f.close()` at the
end?

**A4.** Give one real reason you'd define a custom exception class
(like `InsufficientFundsError`) instead of just raising a generic
`ValueError`.

**A5.** What's the difference between a class attribute and an instance
attribute, and why can a class attribute that's a mutable object (like
a list) cause a subtle bug?

**A6.** What does `@staticmethod` receive as its first parameter,
compared to what a regular instance method receives?

**A7.** Why is `@property` usually preferred over writing an explicit
`get_balance()` method?

**A8.** What does `isinstance(obj, Vehicle)` check that `type(obj) ==
Vehicle` does not, when `obj` is an instance of a subclass of `Vehicle`?

---

## Section B — Scenario Questions (6 points each, 18 points)

**B1.** A `Car` class inherits from a `Vehicle` class. Its `__init__`
sets `self.brand = brand` but never calls `super().__init__(...)`. Later
code tries to read `car.make` (an attribute that `Vehicle.__init__` was
supposed to set) and crashes. Explain exactly what's happening and how
to fix it.

**B2.** A `BankAccount` class has a `balance` implemented as a
`@property` with a `@balance.setter` that rejects negative values. A
caller writes `account.balance = -50` expecting an error, but the
program instead silently sets `account._balance` directly to `-50`,
bypassing the check entirely. Explain how this is possible in Python
and what it says about "private" attributes.

**B3.** A CSV file is being read with `csv.reader(open("data.csv"))`
(no `with`, no explicit close) inside a function that gets called
thousands of times in a loop. After a while, the program crashes with
an OS-level "too many open files" error. Explain what's actually going
wrong.

---

## Section C — Synthesis (6 points)

**C1.** Write a small class hierarchy: a base class `Employee` with an
`__init__(self, name, base_salary)` and a method `calculate_pay(self)`
that returns `base_salary`, and a subclass `Manager` that calls
`super().__init__(...)` and overrides `calculate_pay()` to return
`base_salary` plus a fixed `bonus` passed into its own `__init__`. Then
write a loop that takes a list containing both `Employee` and `Manager`
instances and prints `f"{obj.name} earns {obj.calculate_pay()}"` for
each — using polymorphism, with no `if isinstance(...)` branching
inside the loop itself. Your answer should correctly use concepts from
at least three different chapters in this module (inheritance,
`super()`, and method overriding/polymorphism).

---

## Answer Key

**A1.** `import math` requires calling `math.sqrt(x)` — the function
must be accessed through the module name. `from math import sqrt` pulls
the function directly into the current namespace, so it's called just
as `sqrt(x)`, with no module prefix.

**A2.** A bare `except Exception:` catches *everything* — including
bugs you didn't anticipate (like a `TypeError` from a typo) — and
silently treats them the same as the specific error you meant to
handle. That hides real bugs instead of surfacing them, since the
program keeps running as if nothing unusual happened.

**A3.** If an exception is raised between `open()` and `f.close()`, the
`close()` call is skipped entirely and the file is left open — leaking
a file handle. A `with` block guarantees the file is closed automatically
even if an exception occurs inside it.

**A4.** Any reasonable real use case is acceptable — e.g. a custom
exception lets calling code catch that *specific* problem
(`except InsufficientFundsError:`) without accidentally also catching
unrelated `ValueError`s elsewhere in the same `try` block, and the
exception's name itself documents exactly what went wrong.

**A5.** A class attribute is shared by every instance of the class
(defined directly in the class body, outside `__init__`); an instance
attribute belongs to one specific object (usually set via
`self.attr = ...` inside `__init__`). If a class attribute is a mutable
object like a list, mutating it through one instance (e.g.
`instance.shared_list.append(...)`) changes it for *every* instance,
since they're all pointing at the exact same list in memory.

**A6.** `@staticmethod` receives no automatic first parameter at all —
it's called with only the arguments you explicitly pass. A regular
instance method automatically receives the instance itself as `self`.

**A7.** `@property` lets a method be accessed like a plain attribute
(`account.balance` instead of `account.get_balance()`), which reads more
naturally and means a class can start with a plain public attribute and
later upgrade it to a validated property without changing how any
calling code accesses it.

**A8.** `isinstance(obj, Vehicle)` returns `True` for an object of any
subclass of `Vehicle` too (since a `Car` *is a* `Vehicle`), while
`type(obj) == Vehicle` only returns `True` if `obj` is *exactly* a
`Vehicle` and `False` for any subclass instance — even though that
subclass instance is genuinely a kind of `Vehicle`.

---

**B1.** Because `Car.__init__` never calls `super().__init__(...)`, the
parent class's `__init__` code never runs — so any attribute that
`Vehicle.__init__` was responsible for setting (like `self.make`) was
simply never created on this instance. Reading `car.make` afterward
raises `AttributeError` because the attribute genuinely doesn't exist.
Fix: call `super().__init__(make, ...)` as the first line of
`Car.__init__`, passing along whatever the parent needs.

**B2.** Python has no true enforced privacy — a single-underscore name
like `_balance` is only a naming *convention* signaling "please treat
this as internal," not a technical restriction. Nothing stops calling
code from reaching in and setting `account._balance` directly,
completely bypassing the `@balance.setter`'s validation logic. This is
Python's "we're all consenting adults" philosophy: the property exists
to make the *intended* path convenient and safe, not to make the
underlying attribute physically unreachable.

**B3.** Every call to the function opens a new file handle and never
explicitly closes it (no `with`, no `.close()`). Each of those open
file objects lingers until Python's garbage collector happens to clean
it up, which isn't guaranteed to happen promptly. Across thousands of
calls, open file handles accumulate faster than they're reclaimed until
the operating system's per-process limit on open files is exceeded.
Fix: wrap the open call in a `with open("data.csv") as f:` block so
each file is deterministically closed as soon as the block exits.

**C1.** A correct answer defines the inheritance relationship, calls
`super().__init__()` in `Manager`, overrides `calculate_pay()`, and
loops polymorphically — for example:

```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.base_salary + self.bonus


staff = [Employee("Priya", 70000), Manager("Sam", 90000, 15000)]
for person in staff:
    print(f"{person.name} earns {person.calculate_pay()}")
```

---

## Grading Guidance

| Section | Points | Notes |
|---|---|---|
| A (8 x 2) | 16 | Award partial credit (1 pt) for a mostly-correct answer missing precise terminology. |
| B (3 x 6) | 18 | Full credit requires both identifying the cause AND stating the fix. |
| C (1 x 6) | 6 | Award full credit for any correct approach; code doesn't need to match the sample exactly, but must avoid `isinstance`/type-checking branches inside the print loop itself. |
| **Total** | **40** | 34+ = strong grasp of Module 3; 24-33 = solid but revisit weak areas; below 24 = re-read the relevant chapters before Module 4. |
