# Chapter 7 Project: To-Do List Manager

A menu-driven mini-app that manages a running list of tasks for the
whole session &mdash; a genuinely useful, portfolio-worthy tool built
entirely out of lists, indexing, mutation, and the accumulator pattern.
Each task is stored as a small two-item list, `[task_text, is_done]`,
and every task lives together inside one master list called `tasks`.

## What you'll build

A script with a `while True` menu loop offering six options:

1. Add a task
2. View all tasks
3. Mark a task complete
4. Remove a task
5. View session stats
6. Quit

Adding a task appends a new `[task_text, False]` pair onto the master
`tasks` list (blank input is rejected). Viewing all tasks loops over
the list by index and prints each task numbered, with `[x]` for done
and `[ ]` for pending. Marking complete and removing both work "by
number" &mdash; the user enters the displayed task number, which gets
converted back to a list index (subtracting 1), validated against the
current length of `tasks`, and then either flips that task's `is_done`
flag to `True` or removes it entirely with `.pop()`.

Session stats (option 5) use the accumulator pattern from Chapter 5:
looping over every task to count how many are done, then deriving
pending and a completion rate from that running total.

Example run:

```
=== To-Do List Manager ===

1. Add a task
2. View all tasks
3. Mark a task complete
4. Remove a task
5. View session stats
6. Quit
Choose an option (1-6): 1
Enter the new task: Buy milk
Added: 'Buy milk'

1. Add a task
2. View all tasks
3. Mark a task complete
4. Remove a task
5. View session stats
6. Quit
Choose an option (1-6): 1
Enter the new task: Walk the dog
Added: 'Walk the dog'

1. Add a task
2. View all tasks
3. Mark a task complete
4. Remove a task
5. View session stats
6. Quit
Choose an option (1-6): 2

--- Your Tasks ---
1. [ ] Buy milk
2. [ ] Walk the dog

1. Add a task
2. View all tasks
3. Mark a task complete
4. Remove a task
5. View session stats
6. Quit
Choose an option (1-6): 3
Enter the task number to mark complete: 1
Marked complete: 'Buy milk'

1. Add a task
2. View all tasks
3. Mark a task complete
4. Remove a task
5. View session stats
6. Quit
Choose an option (1-6): 5

--- Session Stats ---
Total tasks: 2
Completed: 1
Pending: 1
Completion rate: 50.0%

1. Add a task
2. View all tasks
3. Mark a task complete
4. Remove a task
5. View session stats
6. Quit
Choose an option (1-6): 6

Session summary: 2 task(s) total, 1 completed.
Goodbye!
```

## How to run it

```bash
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Add a "clear all completed tasks" option that removes every task
  whose `is_done` flag is `True` in one pass.
- Track the longest-pending task (the earliest-added task still marked
  incomplete).
- Let the user edit a task's text by number instead of only removing
  and re-adding it.

## Why this project matters

To-do apps are one of the most common "starter portfolio project"
shapes in software &mdash; every task tracker, project board, and
reminders app is built from the same core idea: a running collection
of records, each with its own status, that gets added to, updated, and
trimmed over time. The logic here is small on purpose, but it's the
same shape as production task-management code: a shared collection,
operations that mutate it safely by validated position, and a running
tally of where things stand.

## More project ideas (build one of these instead, or after)

Chapter 7 is the first chapter where you get a genuine choice of what
to build. The To-Do List Manager above is fully built out with a
starter and reference solution &mdash; the four ideas below are not.
Each is a real, grounded use case solvable with only what's been taught
through Chapter 7 (variables, operators, `if`/`elif`/`else`, loops,
strings, lists, and tuples). No starter or solution files are provided
on purpose &mdash; building one of these unassisted, menu loop and all,
is the point.

### 1. Contact Book

**Problem:** Store a small address book of contacts and be able to
find, list, and remove them without a phonebook app.

**What it should do:** Keep one master list of contacts, where each
contact is a tuple `(name, phone, email)` (a tuple fits well here since
a single contact's three fields don't need to change shape once
entered). Menu options: add a contact, search for a contact by name
(a linear scan through the list, case-insensitive), remove a contact
by name, and list all contacts sorted alphabetically by name.

**Suggested approach:** Start with `contacts = []`. For "list all,
sorted," look at `sorted()` from this chapter &mdash; since contacts
are tuples, sorting a list of tuples sorts by the first element
(name) by default. For "search by name," loop over `contacts` with a
plain `for` loop and compare `contact[0].lower()` against the search
term.

### 2. Grade Roster & Class Average

**Problem:** A teacher needs a quick way to record each student's
score and see class-wide stats without a spreadsheet.

**What it should do:** Keep one master list of `[student_name, score]`
pairs. Menu options: add a student and their score, compute the class
average, find the highest and lowest scorer, and list every student
below a passing threshold (e.g. 60).

**Suggested approach:** Use the accumulator pattern from Chapter 5 to
sum every score and divide by `len(roster)` for the average. For
highest/lowest, loop through the roster tracking a "best so far"
variable and compare as you go &mdash; the same pattern as finding a
maximum manually. For "below threshold," loop and build a filtered
list of students whose score is under the cutoff.

### 3. Playlist Queue Manager

**Problem:** Manage the "up next" queue for a music player &mdash; songs
join the back of the line and play from the front, in order.

**What it should do:** Keep one master list acting as a queue of song
names. Menu options: add a song to the end of the queue, "play next"
(remove and display the song at the front of the queue), view the
upcoming queue in order, and manually shuffle the queue's order.

**Suggested approach:** `.append()` adds to the back; `.pop(0)` removes
and returns the front item (that's exactly what a queue needs). For
"manually shuffle" without the `random` module (not taught until later),
loop through the queue and swap pairs of songs at picked positions using
the tuple-swap idiom from this chapter: `queue[i], queue[j] = queue[j], queue[i]`.

### 4. Shopping Cart Total

**Problem:** Track items in a shopping cart and compute a checkout
total, the way an e-commerce site's cart page does.

**What it should do:** Keep one master list of cart items, where each
item is a tuple `(item_name, price, quantity)`. Menu options: add an
item to the cart, remove an item by name, view the cart with a
computed line total per item (`price * quantity`), and compute the
grand total across the whole cart.

**Suggested approach:** Loop over the cart list to print each line
item, computing `price * quantity` on the fly for display. For the
grand total, use an accumulator variable that adds each item's line
total as you loop. Since tuples are immutable, "removing an item" means
building a new cart list (or using `.pop()` by index) rather than
editing an item's fields in place &mdash; if you need to change a
quantity, replace the whole tuple at that index instead.
