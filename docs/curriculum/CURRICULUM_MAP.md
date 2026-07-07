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
| 18 | Regular Expressions | `re.match()`/`re.search()`/`re.fullmatch()`, `findall()`/`finditer()`, character classes/quantifiers/anchors, groups & named groups, `re.sub()`/`re.split()`, `re.compile()`, greedy-vs-non-greedy, raw strings & flags (`IGNORECASE`/`MULTILINE`), real-world pattern matching — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Project: Resume Keyword Scanner |
| 19 | Working with APIs & JSON | What an API is and why JSON is the shared data format, `requests.get()`/`response.status_code`/`.text`/`.json()`, the `json` module (`loads()`/`dumps()`, `indent=`), navigating nested JSON (dicts of lists of dicts), handling bad responses and missing keys (`requests.exceptions.RequestException`, status-code checks, `dict.get()`), query params & headers (including the API-key-via-environment-variable pattern), and a real, keyless public API to try locally — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Every graded example uses a mocked JSON response, so nothing here requires live network access or an API key. Project: Weather & Quote-of-the-Day Fetcher |
| 20 | Multithreading | What a thread is and why it helps (I/O-bound vs. CPU-bound work), creating and starting threads (`threading.Thread`, `.start()`, `.join()`), the GIL (why it helps I/O-bound work but not CPU-bound work), race conditions (a concrete shared-counter demonstration), `threading.Lock` (the `with lock:` pattern), thread safety patterns (avoiding shared mutable state, `threading.local()`), and `concurrent.futures.ThreadPoolExecutor` (`.map()`, `.submit()`, `as_completed()`) as the modern higher-level alternative to raw `Thread` objects — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Every timing example uses `time.sleep()` to simulate I/O-bound waits, so nothing here requires a real network call or file write, and every graded example is designed so its final result is deterministic even though thread interleaving isn't. Project: Concurrent File-Download Simulator |

## Planned (in build order)

| # | Title | Project |
|---|---|---|
| 21 | Working with Databases (MySQL, MongoDB & Cloud-Hosted DBs) | Student record management system |
| 22 | Building Web Apps & APIs (Flask & FastAPI) | Task-manager web app with a REST API |
| 23 | NumPy for Data Analysis | Grade/statistics analyzer |
| 24 | Pandas for Data Analysis | Sales-data dashboard (CSV in, insights out) |
| 25 | Testing Your Code (unittest/pytest) | Test suite for an earlier project |
| 26 | Professional Python (git, venv, logging, argparse) | CLI tool with proper packaging |
| 27 | Capstone Projects | Combine 2-3 earlier projects into one portfolio piece |
| 28 | Interview & Career Prep | Mock interview + portfolio checklist |

**Chapter 22 scope note:** Python-only web framework chapter — no
JavaScript/React is taught step-by-step (out of scope for a Python
course), but the lesson should explicitly acknowledge where a real
frontend (e.g. React) would plug into the API being built, so learners
know what's next. Covers (1) **Flask**: routes, `render_template`,
request/response basics, serving a simple server-rendered HTML page
(ties back to templating concepts, reuses Ch13 file-handling instincts);
(2) **FastAPI**: path/query params, Pydantic request/response models,
automatic interactive docs (`/docs`), and why type hints matter here
specifically (contrast with Flask's untyped-by-default style); (3) a
short "what's next" callout comparing server-rendered HTML (Flask) vs.
a JSON API meant for a separate frontend (FastAPI) vs. where something
like React would consume that JSON API — conceptual only, no React code.
Project: a task-manager web app exposing a REST API (CRUD on tasks),
built once in Flask and once in FastAPI so the contrast is concrete,
optionally persisting to the DB layer from Ch21.

**Chapter 21 scope note:** covers three connection scenarios, not just
MySQL — (1) MySQL via `mysql-connector-python` (cursors, parameterized
queries, avoiding SQL injection), (2) MongoDB via `pymongo` (collections,
documents-as-dicts, basic CRUD, contrasting relational rows vs. JSON-like
documents), and (3) connecting to a cloud-hosted instance of either
(connection strings/URIs, credentials via environment variables instead of
hardcoding, TLS basics) rather than a local database — framed as "the same
`pymongo`/`mysql-connector` code, pointed at a remote host." Keep the
relational-vs-document contrast explicit throughout, since it's the
conceptual payoff of covering both.

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
