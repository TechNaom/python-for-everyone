"""
Chapter 16 Project: Vehicle Rental System
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools. A base Vehicle
class holds shared attributes and a shared __init__. Car, Motorcycle, and
Truck each call super().__init__() and then override calculate_rental_cost()
and/or describe() with genuinely different behavior per subclass. The menu
loop treats every vehicle the same way -- looping over a list of mixed
subclasses and calling describe()/calculate_rental_cost() polymorphically,
never checking type(vehicle) == ... to decide what to do. Fill in the
numbered TODOs below.
"""


class Vehicle:
    """Base class for anything in the rental fleet. Shared attributes and
    a shared rental-cost formula every subclass can reuse or override."""

    def __init__(self, make, model, daily_rate):
        # TODO 1: Set self.make = make, self.model = model, and
        # self.daily_rate = daily_rate. Also set self.rented_days = 0 (a
        # running total of days rented this session, used by the fleet
        # summary later).
        pass

    def describe(self):
        """Base description -- subclasses extend this via super().describe()."""
        # TODO 2: Return an f-string like:
        # f"{self.make} {self.model} (${self.daily_rate:,.2f}/day)"
        pass

    def calculate_rental_cost(self, days):
        """Base rental cost formula: just daily_rate * days. Subclasses may
        override this with their own pricing rules."""
        # TODO 3: Return self.daily_rate * days.
        pass

    def rent(self, days):
        """Record a rental of `days` days and return its cost."""
        # TODO 4: Compute cost = self.calculate_rental_cost(days) (this
        # calls whichever subclass's version actually applies -- that's
        # polymorphism). Add days to self.rented_days. Return cost.
        pass


class Car(Vehicle):
    """A car: shares Vehicle's setup, adds a passenger-door count, and
    extends describe() rather than fully replacing it."""

    def __init__(self, make, model, daily_rate, num_doors):
        # TODO 5: Call super().__init__(make, model, daily_rate) first, so
        # the shared attributes get set up. Then set self.num_doors = num_doors.
        pass

    def describe(self):
        # TODO 6: Get base = super().describe() (reuses the parent's
        # string instead of rewriting it), then return
        # f"{base} -- Car, {self.num_doors} doors".
        pass


class Motorcycle(Vehicle):
    """A motorcycle: overrides calculate_rental_cost() with a genuinely
    different formula (a discount for week-long-or-longer rentals)."""

    def __init__(self, make, model, daily_rate, has_sidecar=False):
        # TODO 7: Call super().__init__(make, model, daily_rate), then set
        # self.has_sidecar = has_sidecar.
        pass

    def describe(self):
        # TODO 8: Get base = super().describe(). Build extra as
        # "with sidecar" if self.has_sidecar else "no sidecar". Return
        # f"{base} -- Motorcycle, {extra}".
        pass

    def calculate_rental_cost(self, days):
        # TODO 9: Get cost = super().calculate_rental_cost(days) (reuses
        # the base formula instead of rewriting daily_rate * days). If
        # days >= 7, multiply cost by 0.9 (a 10% discount for week-long
        # rentals or longer). Return cost.
        pass


class Truck(Vehicle):
    """A truck: overrides calculate_rental_cost() with a flat per-day
    surcharge on top of the base daily rate, reflecting cargo capacity."""

    SURCHARGE_PER_DAY = 25

    def __init__(self, make, model, daily_rate, cargo_capacity_tons):
        # TODO 10: Call super().__init__(make, model, daily_rate), then set
        # self.cargo_capacity_tons = cargo_capacity_tons.
        pass

    def describe(self):
        # TODO 11: Get base = super().describe(). Return
        # f"{base} -- Truck, {self.cargo_capacity_tons} ton capacity".
        pass

    def calculate_rental_cost(self, days):
        # TODO 12: Get base_cost = super().calculate_rental_cost(days).
        # Return base_cost + (self.SURCHARGE_PER_DAY * days).
        pass


VEHICLE_TYPES = {"1": ("Car", Car), "2": ("Motorcycle", Motorcycle), "3": ("Truck", Truck)}


def find_vehicle(fleet, index):
    """Look up a vehicle by its 1-based display index in the fleet list.
    Returns the vehicle, or None if the index is out of range."""
    # TODO 13: If index < 1 or index > len(fleet), return None. Otherwise
    # return fleet[index - 1].
    pass


def build_seed_fleet():
    """A couple of starting vehicles so the menu has something to work
    with right away -- one of each subclass, built polymorphically."""
    # TODO 14: Return a list containing one Car(...), one Motorcycle(...),
    # and one Truck(...) with any reasonable sample values (see solution.py
    # or README.md for an example fleet).
    pass


# --- Session state ---
print("=== Vehicle Rental System ===")
fleet = build_seed_fleet()
print(f"Loaded {len(fleet)} vehicle(s).")

while True:
    print()
    print("1. Register a new vehicle")
    print("2. List all vehicles")
    print("3. Rent a vehicle / calculate cost")
    print("4. View fleet summary")
    print("5. Quit")
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print()
        print("Vehicle type: 1) Car  2) Motorcycle  3) Truck")
        type_choice = input("Choose a type (1-3): ").strip()
        # TODO 15: Look up type_choice in VEHICLE_TYPES with .get(). If
        # it's None (invalid choice), print "Please choose 1-3." and
        # continue. Otherwise unpack (type_name, vehicle_class) from it.
        #
        # Then prompt for make, model, and daily_rate (as in earlier
        # chapters' menu patterns): strip() each, require make and model
        # to be non-empty, convert daily_rate to float (catching
        # ValueError), and require daily_rate > 0 -- printing a message
        # and continuing on any failure.
        #
        # Then branch on which vehicle_class was chosen (use `is`, e.g.
        # `if vehicle_class is Car:`) and prompt for that subclass's extra
        # field(s): Car needs num_doors (int), Motorcycle needs
        # has_sidecar (y/n prompt converted to a bool), Truck needs
        # cargo_capacity_tons (float). Construct the right subclass with
        # all its arguments, append it to fleet, and print
        # f"Registered: {vehicle.describe()}".
        pass

    elif choice == "2":
        print()
        # TODO 16: If fleet is empty, print "No vehicles in the fleet."
        # Otherwise print f"All vehicles ({len(fleet)}):" and loop over
        # fleet with enumerate(fleet, start=1), printing
        # f"  {i}. {vehicle.describe()}" for each one. This describe()
        # call is polymorphic -- no type checking needed here at all.
        pass

    elif choice == "3":
        print()
        # TODO 17: If fleet is empty, print "No vehicles in the fleet."
        # and continue. Otherwise print the numbered fleet list again (same
        # pattern as TODO 16), then prompt "Rent which vehicle number? ",
        # convert it to an int (catching ValueError), and look it up with
        # find_vehicle(fleet, index) -- printing an error and continuing on
        # any failure. Then prompt for the number of rental days, convert
        # to int (catching ValueError), require it to be positive, and
        # call vehicle.rent(days) (polymorphic -- runs whichever
        # subclass's calculate_rental_cost() actually applies). Print the
        # resulting cost.
        pass

    elif choice == "4":
        print()
        # TODO 18: If fleet is empty, print "No vehicles in the fleet."
        # Otherwise compute: total_value as the sum of every vehicle's
        # daily_rate, total_rented_days as the sum of every vehicle's
        # rented_days, and counts of each subclass using isinstance() (not
        # type()!) -- e.g. sum(1 for v in fleet if isinstance(v, Car)).
        # Print a summary: how many vehicles total, the count of each
        # subclass, the combined daily rate, and the total rental-days
        # booked this session.
        pass

    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
