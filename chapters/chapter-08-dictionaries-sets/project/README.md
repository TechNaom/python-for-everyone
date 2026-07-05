# Chapter 8 Project: Inventory Tracker

A menu-driven mini-app that manages a running store inventory for the
whole session &mdash; built entirely out of dictionaries: a dict-of-dicts,
nested lookups, `.items()` loops, and in-place field updates. Every item
lives together inside one master dictionary called `inventory`, mapping
the item's name to its own details dictionary, e.g.
`{"quantity": 10, "price": 4.99}`.

## What you'll build

A script with a `while True` menu loop offering eight options:

1. Add a new item
2. Update stock quantity
3. Remove an item
4. View full inventory
5. Search for an item
6. View low-stock report
7. View total inventory value
8. Quit

Adding an item rejects a blank name and refuses to overwrite an item
that already exists (pointing the user to option 2 instead), then
validates the quantity is a whole number and the price is a number
before storing `inventory[name] = {"quantity": ..., "price": ...}`.
Updating stock and removing an item both look the name up in
`inventory` first and print a "not found" message if it's missing.
Viewing the full inventory loops over `inventory.items()` and prints
each item's quantity, price, and computed line value
(`quantity * price`), aligned into columns with f-strings. Searching
looks up a single name and prints its quantity and price. The
low-stock report loops over every item and flags any whose quantity is
below `LOW_STOCK_THRESHOLD` (5 units). Total inventory value and the
quit summary both use the accumulator pattern from Chapter 5, looping
over `inventory.items()` and summing `quantity * price` into a running
total.

Example run:

```
=== Inventory Tracker ===

1. Add a new item
2. Update stock quantity
3. Remove an item
4. View full inventory
5. Search for an item
6. View low-stock report
7. View total inventory value
8. Quit
Choose an option (1-8): 1
Enter the item name: Widget
Enter starting quantity: 10
Enter unit price: 4.99
Added: 'Widget' (qty 10, price $4.99)

1. Add a new item
2. Update stock quantity
3. Remove an item
4. View full inventory
5. Search for an item
6. View low-stock report
7. View total inventory value
8. Quit
Choose an option (1-8): 1
Enter the item name: Gadget
Enter starting quantity: 3
Enter unit price: 19.5
Added: 'Gadget' (qty 3, price $19.50)

1. Add a new item
2. Update stock quantity
3. Remove an item
4. View full inventory
5. Search for an item
6. View low-stock report
7. View total inventory value
8. Quit
Choose an option (1-8): 4

--- Full Inventory ---
Item                Quantity    Price     Line Value
Widget              10          $4.99     $49.90
Gadget              3           $19.50    $58.50

1. Add a new item
2. Update stock quantity
3. Remove an item
4. View full inventory
5. Search for an item
6. View low-stock report
7. View total inventory value
8. Quit
Choose an option (1-8): 6

--- Low-Stock Report (below 5 units) ---
Gadget: only 3 left

1. Add a new item
2. Update stock quantity
3. Remove an item
4. View full inventory
5. Search for an item
6. View low-stock report
7. View total inventory value
8. Quit
Choose an option (1-8): 7

Total inventory value across 2 item(s): $158.30

1. Add a new item
2. Update stock quantity
3. Remove an item
4. View full inventory
5. Search for an item
6. View low-stock report
7. View total inventory value
8. Quit
Choose an option (1-8): 8

Session summary: 2 item(s) tracked, total value $158.30.
Goodbye!
```

## How to run it

```bash
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Add a "restock all low-stock items to threshold" option that loops
  over `inventory` and tops up every item below `LOW_STOCK_THRESHOLD`
  in one pass.
- Track which item has the highest total line value (quantity times
  price) across the whole inventory.
- Let the user update an item's price, not just its quantity, using
  the same "look it up, validate, update in place" pattern as option 2.

## Why this project matters

Every point-of-sale system, warehouse tool, and e-commerce back office
keeps some version of this exact shape: a collection of named records,
each holding a small bundle of fields, that gets looked up by key,
updated in place, and rolled up into summary numbers. A dict-of-dicts
is precisely how that maps onto code &mdash; the item name is the key,
its `{"quantity": ..., "price": ...}` bundle is the value, and every
operation here (add, update, remove, search, report, total) is just a
dictionary lookup or a loop over `.items()`. The logic is small on
purpose, but it's the same shape as real inventory and billing systems
in production.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Inventory Tracker above is fully built out with a starter and reference
solution &mdash; the four ideas below are not. Each is a real, grounded
use case solvable with only what's been taught through Chapter 8
(variables, operators, `if`/`elif`/`else`, loops, strings, lists,
tuples, dictionaries, and sets). No starter or solution files are
provided on purpose &mdash; building one of these unassisted, menu loop
and all, is the point.

### 1. Word Frequency Counter

**Problem:** Given a block of text, figure out which words show up
most and least often &mdash; the same basic step behind spam filters,
search engines, and writing-style tools.

**What it should do:** Ask the user to paste in a block of text (or
type several lines), split it into words, and build a dictionary
mapping each word to how many times it appears. Menu options: enter/add
more text, show the word count dictionary, report the most common
word(s), report the least common word(s), and reset the counts.

**Suggested approach:** Use `text.lower().split()` to break the input
into a list of lowercase words (this also sidesteps "Word" vs. "word"
being counted separately). Loop over that list and for each word do
`counts[word] = counts.get(word, 0) + 1` to build the frequency dict.
For "most common," loop over `counts.items()` tracking a "highest count
so far" variable and its word, the same manual-max pattern from
Chapter 5 &mdash; do the mirror image for least common.

### 2. Student Grade Book

**Problem:** A teacher needs one place to record every student's
scores across several subjects and quickly see class-wide standouts,
without a spreadsheet.

**What it should do:** Keep one master dictionary mapping each
student's name to their own dictionary of `{subject: score}`. Menu
options: add or update a student's grade for a subject, view a single
student's full record and average, view every student's average, and
find the class topper for a given subject (the student with the
highest score in that subject).

**Suggested approach:** Adding a grade is `gradebook[name][subject] =
score` &mdash; check if `name` is already a key first, and if not,
start it off as `gradebook[name] = {}` before setting the subject.
A student's average is the accumulator pattern over
`gradebook[name].values()`. For the class topper in one subject, loop
over every student in `gradebook`, skip anyone who doesn't have that
subject recorded (`subject in gradebook[name]`), and keep the
highest-scoring name seen so far.

### 3. Unique Visitor & Tag Tracker

**Problem:** A website session needs to know how many *distinct*
visitors showed up and which content tags were used, plus how two
days' worth of tags overlap &mdash; the kind of question analytics
dashboards answer constantly.

**What it should do:** Keep two sets: one of unique visitor IDs seen
this session, one of unique tags seen this session. Menu options: log a
visitor ID, log a tag, show the count of unique visitors and unique
tags so far, and compare this session's tag set against a second
"previous session" tag set to report which tags are shared, which are
new, and which disappeared.

**Suggested approach:** `.add()` onto a set is naturally safe against
duplicates &mdash; logging the same visitor ID twice just leaves the
set unchanged, which is exactly the "unique" behavior wanted. For the
comparison feature, keep a second set for the previous session's tags
and use `&` (intersection) for shared tags, `-` (difference) in each
direction for "new this session" and "missing from this session."

### 4. Simple Phonebook / Contact Directory

**Problem:** Store contacts with more than one field each (phone *and*
email) and be able to look any of them up by name instantly.

**What it should do:** Keep one master dictionary mapping each
contact's name to a dictionary of `{"phone": ..., "email": ...}`. Menu
options: add a contact, update a contact's phone or email, remove a
contact by name, search for a contact by name, and list every contact
alphabetically by name.

**Suggested approach:** This is the same dict-of-dicts shape as the
Inventory Tracker above, just with `phone`/`email` fields instead of
`quantity`/`price` &mdash; reuse that "look up the key, check it
exists, read/update its nested dict" pattern directly. For "list
alphabetically," `sorted(directory.keys())` gives you the names in
order to loop over and print one by one.
