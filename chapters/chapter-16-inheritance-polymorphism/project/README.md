# Chapter 16 Project: Vehicle Rental System

A menu-driven vehicle rental system built **around this chapter's core
tools** as its organizing principle -- a base `Vehicle` class holds shared
attributes (`make`, `model`, `daily_rate`) and a shared `__init__`, plus a
base `calculate_rental_cost()` formula and a base `describe()` method. Three
subclasses -- `Car`, `Motorcycle`, and `Truck` -- each call
`super().__init__()` to reuse the parent's setup instead of duplicating it,
and each overrides `calculate_rental_cost()` and/or `describe()` with
genuinely different behavior: a `Motorcycle` gets a 10% discount on
week-long-or-longer rentals, a `Truck` adds a flat per-day surcharge for its
cargo capacity, and every subclass's `describe()` extends the base string
with its own specific detail rather than replacing it outright. The menu
loop treats every vehicle the same way -- looping over a list of mixed
subclasses and calling `describe()`/`calculate_rental_cost()`
**polymorphically**, with no `if type(vehicle) == Car: ... elif ...` chain
anywhere. `isinstance()` (not `type()`) is used for the one place a real
type check is needed -- counting vehicles by subclass in the fleet summary
-- specifically because `isinstance()` respects the whole `Vehicle` family.

## What you'll build

An object model covering this chapter's core tools -- **basic inheritance,
`super().__init__()`, method overriding, polymorphism, and `isinstance()`**
-- plus a menu loop offering four real operations:

1. Register a new vehicle
2. List all vehicles
3. Rent a vehicle / calculate cost
4. View fleet summary
5. Quit

The object model itself is built from these pieces:

- `Vehicle.__init__(self, make, model, daily_rate)` -- sets `self.make`,
  `self.model`, `self.daily_rate`, and `self.rented_days = 0` (a running
  total used by the fleet summary).
- `Vehicle.describe()` -- returns a base description string like
  `Toyota Camry ($55.00/day)`. Every subclass calls `super().describe()`
  inside its own override and extends that string, rather than rewriting it
  from scratch.
- `Vehicle.calculate_rental_cost(days)` -- the base formula, just
  `daily_rate * days`. `Car` doesn't override this at all (it inherits the
  base formula unchanged); `Motorcycle` and `Truck` do, each with a
  genuinely different rule.
- `Vehicle.rent(days)` -- calls `self.calculate_rental_cost(days)`
  (polymorphic -- runs whichever subclass's version actually applies),
  updates `self.rented_days`, and returns the cost.
- `Car(Vehicle)` -- adds `num_doors`. `__init__` calls
  `super().__init__(make, model, daily_rate)` first, then sets
  `self.num_doors`. Overrides `describe()` to add
  `"-- Car, {num_doors} doors"`.
- `Motorcycle(Vehicle)` -- adds `has_sidecar`. Overrides
  `calculate_rental_cost()`: gets the base cost via
  `super().calculate_rental_cost(days)`, then applies a 10% discount if
  `days >= 7`. Overrides `describe()` to mention the sidecar.
- `Truck(Vehicle)` -- adds `cargo_capacity_tons`. Overrides
  `calculate_rental_cost()`: gets the base cost via `super()`, then adds a
  flat `SURCHARGE_PER_DAY * days` on top. Overrides `describe()` to mention
  cargo capacity.
- `find_vehicle(fleet, index)` -- looks up a vehicle by its 1-based display
  position in the fleet list, returning `None` if the index is out of
  range.

Three vehicles -- one of each subclass -- are seeded into the session when
the program starts, so the menu has something to work with right away.

Example run:

```
=== Vehicle Rental System ===
Loaded 3 vehicle(s).

1. Register a new vehicle
2. List all vehicles
3. Rent a vehicle / calculate cost
4. View fleet summary
5. Quit
Choose an option (1-5): 2

All vehicles (3):
  1. Toyota Camry ($55.00/day) -- Car, 4 doors
  2. Harley-Davidson Street 750 ($40.00/day) -- Motorcycle, no sidecar
  3. Ford F-150 ($90.00/day) -- Truck, 2.5 ton capacity

1. Register a new vehicle
2. List all vehicles
3. Rent a vehicle / calculate cost
4. View fleet summary
5. Quit
Choose an option (1-5): 3

All vehicles (3):
  1. Toyota Camry ($55.00/day) -- Car, 4 doors
  2. Harley-Davidson Street 750 ($40.00/day) -- Motorcycle, no sidecar
  3. Ford F-150 ($90.00/day) -- Truck, 2.5 ton capacity
Rent which vehicle number? 2
Number of rental days: 10
Rental cost for 10 day(s): $360.00

1. Register a new vehicle
2. List all vehicles
3. Rent a vehicle / calculate cost
4. View fleet summary
5. Quit
Choose an option (1-5): 4

Fleet summary (3 vehicle(s)):
  Cars: 1  Motorcycles: 1  Trucks: 1
  Combined daily rate: $185.00
  Total rental-days booked this session: 10

1. Register a new vehicle
2. List all vehicles
3. Rent a vehicle / calculate cost
4. View fleet summary
5. Quit
Choose an option (1-5): 5

Goodbye!
```

Notice the motorcycle's rental cost above: `$40/day * 10 days = $400`, then
a 10% discount for the 10-day rental brings it to `$360.00` -- a rule that
lives entirely inside `Motorcycle.calculate_rental_cost()` and nowhere else.
The "List all vehicles" and fleet-summary options never ask "is this a Car,
a Motorcycle, or a Truck?" before deciding what to print -- each vehicle
already knows how to describe itself and price its own rental through its
own overridden methods, and the calling code just calls `describe()` /
`calculate_rental_cost()` the same way on every single object in the list.
That's the whole point of polymorphism: the loop is written once, and stays
correct even if a fourth subclass gets added later.

## How to run it

```bash
cd chapters/chapter-16-inheritance-polymorphism/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder).

## Ideas to make it your own (optional stretch goals)

- Add a `return_vehicle()` menu option and an `is_rented` flag on `Vehicle`
  so a vehicle can't be rented twice at once -- notice this only needs to
  be added to the base `Vehicle` class, since every subclass inherits it
  automatically.
- Add a fourth subclass, `Van(Vehicle)`, with its own passenger-capacity
  attribute and its own `calculate_rental_cost()` rule -- confirm the
  existing "list all vehicles" and "fleet summary" menu code needs zero
  changes to support it, since both already work polymorphically.
- Add a `late_fee(days_late)` method on `Vehicle` that every subclass
  inherits unchanged (no override needed), to see that not every method has
  to be overridden just because a subclass exists.

## Why this project matters

Real rental, logistics, and fleet-management platforms (car rental chains,
equipment rental yards, delivery fleets) all model exactly this kind of
hierarchy: a shared base concept (`Vehicle`, `Asset`, `Equipment`) with
several distinct categories underneath it that each need their own pricing
rules, capacity rules, or maintenance schedules, but that the rest of the
system should be able to treat uniformly wherever possible. A checkout
screen, a search results page, or a billing report in a real system loops
over a list of mixed items and calls the same handful of methods on every
one of them -- exactly like this project's fleet list -- without needing a
type-check chain that has to be manually updated every time a new category
of item is introduced. That's precisely what inheritance and polymorphism
buy a real codebase: new categories slot in by writing one new subclass,
not by hunting down and editing every place that already handles the
existing ones.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Vehicle Rental System above is fully built out with a starter and
reference solution -- the four ideas below are not. Each is a real,
grounded use case solvable with only what's been taught through Chapter 16
(everything through Chapter 15's `@staticmethod`/`@classmethod`/`@property`,
plus this chapter's inheritance, `super()`, method overriding,
polymorphism, and `isinstance()`). No starter or solution files are
provided on purpose -- building one of these unassisted is the point.

### 1. Shape Area Calculator

**Problem:** A drawing tool, CAD program, or geometry teaching app needs to
work with many different kinds of shapes, computing each one's area with
its own correct formula, while still being able to treat "a list of shapes"
generically anywhere the program needs to sum or display areas.

**What it should do:** Build a base `Shape` class (perhaps with a `name`
attribute and a placeholder `area()` that isn't meant to be called directly
on the base class itself), then `Circle`, `Rectangle`, and `Triangle`
subclasses that each call `super().__init__()` for shared setup and
override `area()` with their own correct formula (`pi * radius ** 2`,
`width * height`, and `0.5 * base * height` respectively). Menu options:
add a circle, add a rectangle, add a triangle, list all shapes with their
computed areas (polymorphic -- no `type()` checks), view the total area of
every shape combined, and quit.

**Suggested approach:** Loop over a single mixed list of `Shape` objects for
both the listing and total-area options, calling `.area()` the same way on
every one regardless of its actual subclass -- exactly the pattern this
chapter's Vehicle project uses for `describe()`/`calculate_rental_cost()`.

### 2. Employee Payroll System

**Problem:** A payroll or HR system needs to calculate pay correctly for
very different kinds of employees -- a salaried employee's pay doesn't
depend on hours worked, while an hourly employee's does, and the payroll
run needs to process every employee the same way regardless of which kind
they are.

**What it should do:** Build a base `Employee` class with shared attributes
(`name`, plus whatever each employee type needs) and a placeholder
`calculate_pay()`, then `SalariedEmployee` and `HourlyEmployee` subclasses
that each override `calculate_pay()` with their own formula (a fixed
monthly/annual amount divided appropriately, versus `hours_worked *
hourly_rate`, with an overtime multiplier above 40 hours a reasonable
stretch addition). Menu options: add a salaried employee, add an hourly
employee, run payroll (looping polymorphically over every employee and
printing/summing each one's pay), list all employees, and quit.

**Suggested approach:** Keep `calculate_pay()` as the one method every
subclass must override with genuinely different logic, and make sure the
"run payroll" menu option never checks `isinstance()` or `type()` at all --
it should just call `.calculate_pay()` on every employee in the list.

### 3. Notification Delivery System

**Problem:** A real application (an e-commerce site, a banking app, a
scheduling tool) often needs to send the same logical notification through
several different channels -- email, SMS, push -- each with its own actual
delivery mechanism, formatting rules, and character limits, while the rest
of the app just wants to say "notify this user" without caring which
channel handles it.

**What it should do:** Build a base `Notification` class with a shared
`recipient` and `message` attribute and a placeholder `send()` method, then
`EmailNotification` and `SMSNotification` subclasses that each override
`send()` with channel-appropriate behavior -- an email version might print
a formatted "From/To/Subject/Body" block, while an SMS version might
truncate the message to a fixed character limit (e.g. 160 characters)
before printing it. Menu options: queue an email notification, queue an
SMS notification, send all queued notifications (polymorphic loop calling
`.send()` on each), list queued notifications, and quit.

**Suggested approach:** Have `send()` on each subclass simply `print()` a
realistic-looking representation of what would actually be sent (this
project doesn't need real email/SMS APIs) -- the point is the shared
interface and the different formatting/validation logic underneath it, not
actual delivery.

### 4. Media Library Cataloger

**Problem:** A media library, streaming catalog, or personal collection
tracker (books, movies, songs) needs to store very different kinds of
media with different relevant attributes (a book has a page count, a movie
has a runtime, a song has a duration and an artist), while still listing
and searching the whole collection as one uniform list.

**What it should do:** Build a base `Media` class with shared attributes
(`title`, `year`) and a placeholder `get_info()` method, then `Book`,
`Movie`, and `Song` subclasses that each add their own extra attribute(s)
and override `get_info()` to return a description appropriate to that kind
of media (a book's info mentions its page count and author, a movie's
mentions its runtime and director, a song's mentions its artist and
duration). Menu options: add a book, add a movie, add a song, list the
whole library (polymorphic -- prints each item's own `get_info()` output),
search the library by year, and quit.

**Suggested approach:** Store every item in one shared `library` list
regardless of its actual subclass, and make sure both "list the library"
and "search by year" loop over that one list calling shared methods
(`get_info()`, and comparing a shared `year` attribute) without ever
checking which specific subclass an item is.
