# Python for Everyone — Curriculum Map

This is the working roadmap, rebuilt from 10 years of real classroom
teaching material. Chapters are built one at a time; each is fully
piloted (lesson, quiz, exercises, interview questions, project) before
moving to the next. The rendered, always-current version lives at
[`docs/curriculum/index.html`](index.html) / the live roadmap page.

## Built

| Chapter | Title | Covers |
|---|---|---|
| 1 | Your First Python Program | `print()`, variables, basic types, `input()` |
| 2 | Variables & Data Types | naming rules, dynamic typing, `type()`/`id()`, conversion |
| 3 | Operators | arithmetic, relational/logical, bitwise, `is`/`in` |
| 4 | Control Flow (if / elif / else) | simple if, if-else, elif chains, nested if |
| 5 | Loops (while / for) | while, for + range(), accumulator pattern, break/continue |
| — | Module 1 Written Exam | covers Chapters 1-5 |
| 6 | Strings Deep Dive | indexing/slicing, string methods, f-strings, immutability, validation, real-world text processing — plus a Challenges page (8 auto-graded coding problems, HackerRank-style) |
| 7 | Lists & Tuples | indexing/slicing/mutation, list methods, tuples & packing/unpacking, nested lists, shallow copies & the is-vs-== trap, real-world record processing — plus a Challenges page (8 auto-graded coding problems) and, from this chapter onward, 4 extra real-world project ideas alongside the one fully built project |
| 8 | Dictionaries & Sets | creating/accessing dicts, dict methods, looping, sets & set operations, nested dicts, real-world lookup/frequency use — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas |
| 9 | Comprehensions, Lambda & Functional Tools | list/dict/set comprehensions, nested comprehensions & readability limits, lambda functions, `map()`/`filter()`/`sorted(key=lambda)`, real-world data-cleaning use — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. `lambda` is introduced here as a narrow exception ahead of `def` (Chapter 10) |
| 10 | Functions Deep Dive | `def`/parameters/`return`, default arguments, `*args`/`**kwargs`, scope (`global`/`nonlocal`), recursion, closures, decorators, real-world function-library use — 8 sub-topics (broader than the usual 6), plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas |
| — | Module 2 Written Exam | covers Chapters 6-10 |
| 11 | Modules & Packages | what a module is, `import` variations, the `math`/`datetime`/`random` modules, real-world module use — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. First chapter where `import` is allowed |
| 12 | Exception Handling | try/except basics, multiple except/else/finally, the exception object, raising exceptions, custom exception classes, real-world error handling — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Custom exception classes are a narrow exception to the "no classes until Chapter 14" rule |
| 13 | File Handling & CSV | opening/reading/writing files, `with`, file modes & paths, the `csv` module (reader/writer/DictReader/DictWriter), file-related exceptions, real-world file/CSV processing — plus a Challenges page (8 auto-graded coding problems, using string-content inputs since the browser sandbox has no real filesystem) and 4 extra real-world project ideas |
| 14 | OOP Basics | classes & objects, `__init__` & instance attributes, instance methods, class vs. instance attributes (incl. the mutable-class-attribute gotcha), dunder methods (`__str__`/`__repr__`), real-world OOP basics — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. This is the chapter where general classes (not just custom exceptions) finally become allowed |
| 15 | OOP Deeper | `@staticmethod`, `@classmethod` & alternative constructors, encapsulation/privacy conventions (`_x`/`__x`, name mangling), `@property` getters, property setters with validation, real-world deeper OOP — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Quiz introduces the new multiple-choice question type (16 MCQ + 5 fill-in-the-blank) alongside fill-in-the-blank. Project: Bank Account System |
| 16 | Inheritance & Polymorphism | `class Child(Parent):` and what's inherited automatically, `super().__init__()`, method overriding & extending with `super()`, polymorphism, `isinstance()` vs `type()`, real-world inheritance & polymorphism (with a caution on composition-over-inheritance) — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Quiz: 15 MCQ + 5 fill-in-the-blank. This is the chapter where inheritance finally becomes allowed. Project: Vehicle Rental System |
| 17 | Generators, Iterators & Context Managers | Iterables vs. iterators (`__iter__`/`__next__`/`StopIteration`), generator functions (`yield`), generator expressions & lazy evaluation, the `with` protocol (`__enter__`/`__exit__`), writing custom context managers, real-world use in streaming large files — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Quiz: 15 MCQ + 5 fill-in-the-blank. Project: Large-File Streaming Log Analyzer |

## Planned (in build order)

| # | Title | Project |
|---|---|---|
| 18 | Regular Expressions | Resume keyword scanner |
| 19 | Working with APIs & JSON | Weather/quote-of-the-day fetcher |
| 20 | Multithreading | Concurrent file-download simulator |
| 21 | Working with Databases (MySQL) | Student record management system |
| 22 | NumPy for Data Analysis | Grade/statistics analyzer |
| 23 | Pandas for Data Analysis | Sales-data dashboard (CSV in, insights out) |
| 24 | Testing Your Code (unittest/pytest) | Test suite for an earlier project |
| 25 | Professional Python (git, venv, logging, argparse) | CLI tool with proper packaging |
| 26 | Capstone Projects | Combine 2-3 earlier projects into one portfolio piece |
| 27 | Interview & Career Prep | Mock interview + portfolio checklist |

## Format every chapter follows

Hook → plain-language concept → "What is...?" callouts → annotated
code (in a terminal-style code window, with a live in-browser "Run
Code" playground where the example doesn't need `input()`) → optional
"Go Deeper" box → Points to Remember → interactive fill-in-the-blank
quiz (progress bar + celebration banner, marks the chapter complete in
this browser's local progress tracker) → exercises (including at least
one "Debug the Code" task) → interview questions (Q&A accordion + a
rapid-fire recall quiz) → a real, resume-worthy project.

See [`CONTRIBUTING.md`](../../CONTRIBUTING.md) for the exact file
structure and content standards each new chapter must match.
