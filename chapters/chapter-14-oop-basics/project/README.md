# Chapter 14 Project: Library Management System

A menu-driven library management system built **around general classes** as
its core organizing principle -- a `Book` class (with `__init__`, instance
attributes like `title`/`author`/`isbn`/`is_checked_out`, `check_out()`/
`return_book()` instance methods, and a `__str__` for readable printing) is
the real centerpiece, and every menu operation works with real `Book`
objects instead of a pile of separate dicts and functions. A `Library` class
holds the running list of `Book` objects for the session and the operations
that act on that collection (add, check out, return, search, list all),
matching Chapter 10's function-library pattern -- just now organized around
a class instead of loose functions.

## What you'll build

A small object model covering this chapter's core tools -- **classes,
`__init__`, instance attributes, instance methods, and `__str__`** -- plus a
menu loop offering six real operations:

1. Add a book
2. Check out a book
3. Return a book
4. Search by title
5. Search by author
6. List all books
7. Quit

The object model itself is built from these pieces:

- `Book.__init__(self, title, author, isbn, is_checked_out=False)` -- sets
  every book's instance attributes. `is_checked_out` defaults to `False`
  since a newly added book is available in essentially every real case.
- `Book.check_out(self)` -- marks the book checked out and returns `True`,
  or returns `False` if it was already checked out (no double checkout).
- `Book.return_book(self)` -- marks the book returned and returns `True`,
  or returns `False` if it wasn't checked out in the first place.
- `Book.__str__(self)` -- returns a readable one-line string like
  `"Dune" by Frank Herbert (ISBN 0001) -- available`, so listing books
  reads naturally instead of showing raw memory addresses.
- `Library.__init__(self)` -- sets `self.books = []` **inside `__init__`**,
  not as a class attribute, so every `Library` instance gets its own
  independent list instead of accidentally sharing one (the classic
  mutable-class-attribute bug this chapter's interview questions cover).
- `Library.add_book`, `find_by_isbn`, `search_by_title`, `search_by_author`,
  `all_books` -- the operations that act on the running collection of
  `Book` objects.
- `print_books(books)` -- prints a list of `Book` objects, one per line,
  relying on each book's own `__str__` for readable output.

Three books are seeded into the library when the program starts, so the
menu has something to work with right away.

Example run:

```
=== Library Management System ===
Loaded 3 book(s) into the library.

1. Add a book
2. Check out a book
3. Return a book
4. Search by title
5. Search by author
6. List all books
7. Quit
Choose an option (1-7): 2

ISBN of the book to check out: 0001
Checked out: "Dune" by Frank Herbert (ISBN 0001) -- checked out

1. Add a book
2. Check out a book
3. Return a book
4. Search by title
5. Search by author
6. List all books
7. Quit
Choose an option (1-7): 6

All books (3):
  "Dune" by Frank Herbert (ISBN 0001) -- checked out
  "The Hobbit" by J.R.R. Tolkien (ISBN 0002) -- available
  "Foundation" by Isaac Asimov (ISBN 0003) -- available

1. Add a book
2. Check out a book
3. Return a book
4. Search by title
5. Search by author
6. List all books
7. Quit
Choose an option (1-7): 7

Goodbye!
```

Notice how much of this chapter shows up in one small program: a `Book`
class bundling data (title, author, ISBN, checked-out status) with the
behavior that makes sense on it (`check_out`, `return_book`), a `Library`
class managing a running collection of those objects with its list correctly
created inside `__init__` (not as a shared class attribute), and a `__str__`
method turning every book into a clean, readable line instead of Python's
default `<__main__.Book object at 0x...>` output. That's the entire point of
this project -- once related data and behavior are bundled into a class,
the rest of the program (the menu loop, the session logic) barely needs to
know how a `Book` works internally at all; it just calls `book.check_out()`
or prints `book` and trusts the class to handle the rest.

## How to run it

```bash
cd chapters/chapter-14-oop-basics/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder).

## Ideas to make it your own (optional stretch goals)

- Add a "remove a book" option that only allows removing a book if it isn't
  currently checked out, reusing `Library.find_by_isbn`.
- Add a `Library.checked_out_books()` method (a list comprehension filtering
  `self.books` on `.is_checked_out`) and a matching menu option to show only
  what's currently out.
- Give `Book` a `due_date` instance attribute (using the `datetime` module
  from Chapter 8) that gets set when a book is checked out, and print it as
  part of `__str__` whenever a book is checked out.

## Why this project matters

A public library's catalog system, a small bookstore's inventory tracker, a
company's internal equipment checkout log -- all of these are, underneath,
the exact same shape as this project: real-world "things" (books, laptops,
tools) that have a consistent shape (a title, an owner, a status) and clear
behavior attached to them (checking something out, returning it, searching
for it). That's the real skill this project practices -- once a program has
more than a handful of related pieces of data with recurring behavior
attached, bundling them into a class keeps the code self-documenting and
organized in a way a pile of separate dicts and functions never quite
manages once a program grows past a few screens of code.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Library Management System above is fully built out with a starter and
reference solution -- the four ideas below are not. Each is a real,
grounded use case solvable with only what's been taught through Chapter 14
(everything through Chapter 13's file-handling material, plus general class
definitions, `__init__`, instance/class attributes, instance methods, and
`__str__`/`__repr__` -- no `@staticmethod`/`@classmethod`/`@property` and no
inheritance, since those are Chapters 15 and 16). No starter or solution
files are provided on purpose -- building one of these unassisted is the
point.

### 1. Student Grade Tracker

**Problem:** A teacher or tutor needs a simple way to track several
students' scores across assignments and quickly see who's doing well and
who needs help, without re-deriving each student's average by hand every
time a new score comes in.

**What it should do:** Build a `Student` class with instance attributes for
name and a list of scores, an `add_score(score)` instance method, an
`average()` instance method, and a `__str__` that shows the student's name
and current average. Menu options: add a student, record a score for a
student, show one student's average, list all students sorted by average
(highest first), and quit.

**Suggested approach:** Keep a plain list of `Student` objects as the
running session state (the same pattern this chapter's `Library` class
uses for `Book` objects), and use `sorted(students, key=lambda s:
s.average(), reverse=True)` for the sorted listing -- `lambda` and `sorted`
with a `key` were both covered in earlier chapters.

### 2. Inventory Management System

**Problem:** A small shop or warehouse needs to track how many units of
each product it has on hand, flag items running low, and update quantities
as stock comes in or gets sold -- doing this with loose variables gets
unmanageable past a handful of products.

**What it should do:** Build a `Product` class with instance attributes for
name, price, and quantity-on-hand, a `restock(amount)` instance method, a
`sell(amount)` instance method that refuses to sell more than what's in
stock, and a `__str__` showing name, price, and current quantity. Menu
options: add a product, restock a product, record a sale, list all
products, list products below a low-stock threshold, and quit.

**Suggested approach:** Store products in a plain list (or a dict keyed by
product name, if you want lookups by name to be more direct), and have
`sell(amount)` return `True`/`False` the same way this chapter's
`Book.check_out()` does, so the menu code can react to a failed sale
(not enough stock) without needing to know the class's internals.

### 3. To-Do List with Priority Levels

**Problem:** A plain flat to-do list treats every task as equally urgent,
which doesn't match how real work actually gets prioritized -- some tasks
are genuinely more time-sensitive than others.

**What it should do:** Build a `Task` class with instance attributes for
description, priority (e.g. `"High"`/`"Medium"`/`"Low"`), and a
`done`/`pending` status, a `mark_done()` instance method, and a `__str__`
that shows the description, priority, and status together. Menu options:
add a task with a priority, list all tasks grouped or sorted by priority,
mark a task done by number, remove a task by number, and quit.

**Suggested approach:** Keep tasks in a list of `Task` objects, and for the
priority-sorted listing, map each priority string to a number (e.g.
`{"High": 0, "Medium": 1, "Low": 2}`) and pass that mapping into `sorted(...,
key=...)` -- the same dict-based lookup pattern from Chapter 11.

### 4. Music Playlist Manager

**Problem:** A music app needs to represent individual songs and the
playlists that group them, and let a user build, browse, and reorder those
playlists -- a plain list of song-title strings loses useful details like
artist and duration.

**What it should do:** Build a `Song` class with instance attributes for
title, artist, and duration (in seconds), plus a `__str__` that formats
duration as `mm:ss`. Build a `Playlist` class holding a list of `Song`
objects with an `add_song(song)` instance method and a `total_duration()`
instance method that sums every song's duration. Menu options: add a song
to the playlist, list all songs with their formatted duration, show the
playlist's total duration, remove a song by title, and quit.

**Suggested approach:** Formatting `mm:ss` inside `Song.__str__` just needs
integer division and modulo on the stored seconds
(`f"{duration // 60}:{duration % 60:02d}"`), both covered in Chapter 2/9 --
no new math tools needed, just applying them inside a dunder method instead
of a loose function.
