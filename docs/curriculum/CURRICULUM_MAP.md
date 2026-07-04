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

## Planned (in build order)

| # | Title | Project |
|---|---|---|
| 7 | Lists & Tuples | To-do list manager |
| 8 | Dictionaries & Sets | Inventory tracker |
| 9 | Comprehensions, Lambda & Functional Tools | Data-cleaning one-liners kit |
| 10 | Functions Deep Dive (params & defaults, `*args`/`**kwargs`, scope & `global`/`nonlocal`, recursion, closures, decorators) | Tip / bill-split calculator library |
| 11 | Modules & Packages | Expense tracker (`datetime`, `math`) |
| 12 | Exception Handling | ATM simulator (custom exceptions) |
| 13 | File Handling & CSV | Log-file analyzer |
| 14 | OOP Basics | Library management system |
| 15 | OOP Deeper (static/class methods, encapsulation, properties) | Bank account system |
| 16 | Inheritance & Polymorphism | Vehicle rental system |
| 17 | Generators, Iterators & Context Managers | Large-file streaming reader |
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
