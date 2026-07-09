# Python for Everyone — Curriculum Map

This is the working roadmap, rebuilt from 10 years of real classroom
teaching material. Chapters are built one at a time; each is fully
piloted (lesson, quiz, exercises, interview questions, project) before
moving to the next. The rendered, always-current version lives at
[`docs/curriculum/index.html`](index.html) / the live roadmap page.

**As of Chapter 25, every new chapter is built GenAI-driven by
default:** each worked example gets a thought-process + prompt box (the
reasoning behind the code, then a space to write your own AI prompt and
compare it against a real one — see `CONTRIBUTING.md` for the full
spec), and each chapter project gets a paired "AI-paired" critique
exercise where a realistic AI-generated solution has genuine, subtle
bugs planted in it to find. Chapter 25 (Memory Management) is the first
chapter built this way and the reference to match against. Chapters
1-24 don't have it yet — retrofitting them is a planned, separate pass,
not yet started.

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
| 21 | Working with Databases | What a database connection is and why Python needs a driver library, connecting to MySQL with `mysql-connector-python` (`connect()`, `.cursor()`, `cursor.execute(sql, params)` with `%s` parameterized queries, `.fetchall()`/`.fetchone()`, `connection.commit()`), SQL injection (a concrete attack demonstration) and why parameterized queries close it structurally, MongoDB with `pymongo` (`MongoClient`, collections, documents as Python dicts) and CRUD (`insert_one`/`find`/`update_one`/`delete_one`), the relational-rows-vs-document-records tradeoff side by side, and cloud-hosted connections (the same driver code pointed at a remote host via a connection string, credentials read from `os.environ` instead of hardcoded, a TLS mention) — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. No real MySQL/MongoDB server is available or required: every executed example runs against a small `FakeConnection`/`FakeCursor`/`FakeCollection` class matching the real drivers' method names and call shapes, so nothing here needs a live database or an installed driver. Project: Student Record Management System |
| — | Module 4 Written Exam | covers Chapters 17-21 |
| 22 | Building Web Apps & APIs (Flask & FastAPI) | The request/response cycle and what a web framework is; Flask (`@app.route()`, `render_template()`, `request.args`/`request.form`/`request.json`) for server-rendered HTML; FastAPI (`@app.get()`/`@app.post()`, path/query params, Pydantic `BaseModel` request/response validation, automatic interactive docs at `/docs`) for typed JSON APIs, and why type hints are load-bearing there specifically (contrast with Flask's untyped-by-default style); a side-by-side Flask-vs-FastAPI comparison; and a conceptual "what's next" callout on server-rendered HTML vs. a JSON API meant for a separate frontend vs. where something like React would consume that JSON API — conceptual only, no React/JavaScript taught. No live server is available or required: every graded example is a plain Python function pulled out of its route decorator, testable without `app.run()`/`uvicorn.run()`, while complete, real, runnable Flask and FastAPI apps are shown too (verified against real Flask/FastAPI test clients) — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Project: Task Manager REST API, built once in Flask and once in FastAPI so the contrast is concrete. |
| 23 | NumPy for Data Analysis | The performance/ergonomics case for arrays over lists (a concrete loop-vs-`arr.sum()`/`arr.mean()` before/after); creating arrays (`np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`) and checking `.shape`/`.dtype`/`.ndim`; 1D/2D indexing and slicing, and boolean masking (`arr[arr > 5]`) as the single most important NumPy idiom; vectorized element-wise math and broadcasting (with a verified diagram of a genuine shape-mismatch error); aggregate functions (`.sum()`/`.mean()`/`.min()`/`.max()`/`.std()`) and the `axis=` parameter (with a character-aligned axis=0-vs-axis=1 diagram before any prose, per the readability standard); reshaping (`.reshape()`/`.flatten()`) and stacking (`np.concatenate()`/`np.vstack()`/`np.hstack()`). This is the first data-science-flavored chapter in the course — NumPy is the foundation nearly every other Python data tool (pandas, scikit-learn, TensorFlow, PyTorch) is built on top of. Every example verified against a real NumPy install; the in-browser playground and Challenges page both load NumPy into their Pyodide sandbox automatically — plus a Challenges page (8 auto-graded coding problems) and 4 extra real-world project ideas. Mid-module chapter (Module 5 = Chapters 22-27) — no module exam yet. Project: Grade & Statistics Analyzer, reporting overall/per-subject/per-student statistics from a 2D grades array and flagging above/below-average students via boolean masking. |
| 24 | Pandas for Data Analysis | What pandas is and why it exists on top of NumPy (labeled, heterogeneous-column DataFrames/Series vs. NumPy's homogeneous arrays); creating a DataFrame from a dict of lists and from a CSV with `pd.read_csv()` (with a measured before/after against Chapter 13's `csv` module); inspecting data (`.head()`/`.info()`/`.describe()`/`.shape`/`.columns`/`.dtypes`); selecting/filtering (`df['col']` vs. `df[['col1','col2']]`, boolean filtering) and `.loc[]` vs. `.iloc[]` (with a verified label-vs-position diagram before any prose, per the readability standard); adding/modifying columns and handling missing data (`.isna()`/`.dropna()`/`.fillna()`); grouping and aggregation (`.groupby()` + `.agg()`/`.sum()`/`.mean()`) and `.sort_values()`. Every example verified against a real pandas install; the in-browser playground and Challenges page both load pandas (alongside NumPy, in one `loadPackage()` call) into their Pyodide sandbox automatically — plus a Challenges page (8 auto-graded coding problems, every graded return value a plain Python type — list/dict/int/float/str, never a raw DataFrame/Series) and 4 extra real-world project ideas. Mid-module chapter (Module 5 = Chapters 22-27) — no module exam yet. Project: Sales-Data Dashboard (CSV in, insights out), computing total revenue, top products/regions via `.groupby()`, and flagging underperforming line items via boolean filtering. |
| 25 | Memory Management in Python | How Python actually manages memory — reference counting (every object's refcount, `sys.getrefcount()`) and what happens when an object is created; reference cycles and the cyclic garbage collector (`gc` module, why reference counting alone can't free a cycle, `gc.collect()`, `gc.get_count()`/generations at a beginner level, demonstrated with a concrete two-object cycle); the classic mutable-default-argument gotcha (`def f(x=[])`), built from first principles (default argument objects are created once, at function-definition time, and reused — a direct consequence of object/reference semantics, not a special-case rule) with a broken example and the `None`-sentinel fix; `__slots__` (what it saves — no per-instance `__dict__` — and what it costs — no dynamic attributes, no easy multi-inheritance with other slotted classes — measured with a real before/after byte comparison); and memory profiling basics (`sys.getsizeof()` for single objects, `tracemalloc` for tracking allocations across a code block, a genuine "which approach uses less memory" comparison). Ties back to Chapter 17's generators as "the memory-efficient alternative" once learners understand why materializing a full list is expensive, with a concrete side-by-side memory comparison — plus a Challenges page (8 auto-graded coding problems, memory-size challenges graded on relative comparison rather than exact byte counts so they stay portable across Python versions/platforms) and 4 extra real-world project ideas. Mid-module chapter (Module 5 = Chapters 22-27) — no module exam yet. Project: a memory profiler that instruments a function with `tracemalloc`, reporting peak memory use, top allocations, and a before/after comparison between a memory-heavy version and an optimized version (list vs. generator, or with/without `__slots__`) of the same logic. |

## Planned (in build order)

| # | Title | Project |
|---|---|---|
| 26 | Debugging Production Issues (100-Issue Playbook) | Production incident runbook |
| 27 | Testing Your Code (unittest/pytest) | Test suite for an earlier project |
| 28 | Git Fundamentals | Local git workflow (branching, merging, rebase, conflict resolution) on a sample repo |
| 29 | GitHub & Collaboration | An open-source-style collaboration workflow (remotes, forks, pull requests, issues) |
| 30 | CI/CD Pipelines | A GitHub Actions workflow that lints and tests on every push |
| 31 | Professional Python (git, venv, logging, argparse) | Packaged CLI tool |
| 32 | Capstone Projects | Combine 2-3 earlier projects into one portfolio piece |
| 33 | Interview & Career Prep | Mock interview + portfolio checklist |

**Chapter 26 scope note:** a catalog-style chapter, not a standard
hook-to-project lesson — `lesson.html` is restructured as a scannable
reference of roughly 100 short entries grouped by category (crashes/
exceptions, performance, memory leaks, concurrency/deadlocks, data
corruption, deployment & environment issues, database/API failures,
logging & observability gaps), each entry following symptom → root
cause → fix → minimal runnable repro, stated in real-world/production
language ("the service OOMs after 6 hours," "a deploy silently breaks
prod because of an env var mismatch") rather than abstract trivia. Every
category should draw on features/topics already taught by this point in
the course so entries feel earned, not name-dropped. Still gets a quiz,
challenges page, and project like every other chapter — the project is
a "production incident runbook" tool that classifies a described symptom
against the catalog and suggests likely root causes. Given the unusual
scale (~100 entries vs. the usual half-dozen sub-topics), pace this as
several build passes rather than one lesson.html sub-topic loop, and
verify every runnable repro actually reproduces (or is honestly labeled
conceptual/non-reproducible-in-browser where a real repro would need
infrastructure this course doesn't have, e.g. a real OOM kill or a real
multi-service deadlock).

**Chapter 28 scope note:** Git Fundamentals — local git only, no GitHub
yet: `git init`/`add`/`commit`, branching, merging, rebase basics, and
resolving merge conflicts, with real workflow-style examples throughout.
Project: a local git workflow (branching, merging, rebase, conflict
resolution) exercised on a sample repo.

**Chapter 29 scope note:** GitHub & Collaboration — remotes, `push`/
`pull`, forks, pull requests, issues, and a real open-source-style
collaboration workflow, building directly on Chapter 28's local git
skills. Project: an open-source-style collaboration workflow (remotes,
forks, pull requests, issues).

**Chapter 30 scope note:** CI/CD Pipelines — a plain-language "what is
CI/CD and why does it exist" framing, then a real, runnable GitHub
Actions workflow YAML (lint + test on every push, matching the pattern
this very repo's own `.github/workflows/pages.yml` deploy workflow
already uses, which makes a good real-world reference to point at),
environment/secrets handling in CI (never committing secrets, using
repo/CI secret stores), and where CI/CD fits relative to Ch27's testing
chapter (CI is what actually runs those tests on every push). Keep it
conceptual/example-driven rather than requiring a live GitHub Actions
run to grade anything — the workflow YAML is taught and shown working
via a real example, not executed by the auto-grader. Project: a GitHub
Actions workflow that lints and tests on every push.

**Chapter 31 scope note:** Professional Python — git, venv, logging,
argparse only. CI/CD is explicitly out of scope here since it now has
its own chapter (30); this chapter stays focused on packaging a
CLI tool professionally (virtual environments, structured logging,
`argparse` for a real command-line interface). Project: a packaged CLI
tool.

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
