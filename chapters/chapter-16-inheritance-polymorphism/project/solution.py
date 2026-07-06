"""
Chapter 16 Project: Vehicle Rental System -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: a base Vehicle
class with a shared __init__ and shared methods, at least two subclasses
(Car, Motorcycle, Truck) that call super().__init__() and override
calculate_rental_cost() and describe() with genuinely different behavior
per subclass, and a menu loop that treats every vehicle the same way --
looping over a list of mixed subclasses and calling describe() and
calculate_rental_cost() polymorphically, with no type(v) == ... chain
anywhere. isinstance() is used (not type()) wherever a type check is
genuinely needed, since isinstance() respects the whole Car/Motorcycle/
Truck family under Vehicle.

No composition-over-inheritance callout is needed in code -- it's covered
in README.md/index.html as brief context per the chapter brief.
"""


class Vehicle:
    """Base class for anything in the rental fleet. Shared attributes and
    a shared rental-cost formula every subclass can reuse or override."""

    def __init__(self, make, model, daily_rate):
        self.make = make
        self.model = model
        self.daily_rate = daily_rate
        self.rented_days = 0  # total days rented across this session, for the fleet summary

    def describe(self):
        """Base description -- subclasses extend this via super().describe()."""
        return f"{self.make} {self.model} (${self.daily_rate:,.2f}/day)"

    def calculate_rental_cost(self, days):
        """Base rental cost formula: just daily_rate * days. Subclasses may
        override this with their own pricing rules."""
        return self.daily_rate * days

    def rent(self, days):
        """Record a rental of `days` days and return its cost."""
        cost = self.calculate_rental_cost(days)
        self.rented_days += days
        return cost


class Car(Vehicle):
    """A car: shares Vehicle's setup, adds a passenger-door count, and
    extends describe() rather than fully replacing it."""

    def __init__(self, make, model, daily_rate, num_doors):
        super().__init__(make, model, daily_rate)
        self.num_doors = num_doors

    def describe(self):
        base = super().describe()
        return f"{base} -- Car, {self.num_doors} doors"


class Motorcycle(Vehicle):
    """A motorcycle: overrides calculate_rental_cost() with a genuinely
    different formula (a discount for week-long-or-longer rentals)."""

    def __init__(self, make, model, daily_rate, has_sidecar=False):
        super().__init__(make, model, daily_rate)
        self.has_sidecar = has_sidecar

    def describe(self):
        base = super().describe()
        extra = "with sidecar" if self.has_sidecar else "no sidecar"
        return f"{base} -- Motorcycle, {extra}"

    def calculate_rental_cost(self, days):
        # Motorcycles get a 10% discount for rentals of a week or longer.
        cost = super().calculate_rental_cost(days)
        if days >= 7:
            cost *= 0.9
        return cost


class Truck(Vehicle):
    """A truck: overrides calculate_rental_cost() with a flat per-day
    surcharge on top of the base daily rate, reflecting cargo capacity."""

    SURCHARGE_PER_DAY = 25

    def __init__(self, make, model, daily_rate, cargo_capacity_tons):
        super().__init__(make, model, daily_rate)
        self.cargo_capacity_tons = cargo_capacity_tons

    def describe(self):
        base = super().describe()
        return f"{base} -- Truck, {self.cargo_capacity_tons} ton capacity"

    def calculate_rental_cost(self, days):
        # Trucks add a flat per-day surcharge on top of the base formula.
        base_cost = super().calculate_rental_cost(days)
        return base_cost + (self.SURCHARGE_PER_DAY * days)


VEHICLE_TYPES = {"1": ("Car", Car), "2": ("Motorcycle", Motorcycle), "3": ("Truck", Truck)}


def find_vehicle(fleet, index):
    """Look up a vehicle by its 1-based display index in the fleet list.
    Returns the vehicle, or None if the index is out of range."""
    if index < 1 or index > len(fleet):
        return None
    return fleet[index - 1]


def build_seed_fleet():
    """A couple of starting vehicles so the menu has something to work
    with right away -- one of each subclass, built polymorphically."""
    return [
        Car("Toyota", "Camry", 55, 4),
        Motorcycle("Harley-Davidson", "Street 750", 40, has_sidecar=False),
        Truck("Ford", "F-150", 90, 2.5),
    ]


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
        type_info = VEHICLE_TYPES.get(type_choice)
        if type_info is None:
            print("Please choose 1-3.")
            continue

        type_name, vehicle_class = type_info
        make = input("Make: ").strip()
        model = input("Model: ").strip()
        rate_str = input("Daily rate: ").strip()
        if not make or not model:
            print("Make and model are required.")
            continue
        try:
            daily_rate = float(rate_str)
        except ValueError:
            print("Daily rate must be a number.")
            continue
        if daily_rate <= 0:
            print("Daily rate must be positive.")
            continue

        if vehicle_class is Car:
            doors_str = input("Number of doors: ").strip()
            try:
                num_doors = int(doors_str)
            except ValueError:
                print("Number of doors must be a whole number.")
                continue
            vehicle = Car(make, model, daily_rate, num_doors)
        elif vehicle_class is Motorcycle:
            sidecar_str = input("Has sidecar? (y/n): ").strip().lower()
            vehicle = Motorcycle(make, model, daily_rate, has_sidecar=(sidecar_str == "y"))
        else:  # Truck
            cargo_str = input("Cargo capacity (tons): ").strip()
            try:
                cargo_capacity_tons = float(cargo_str)
            except ValueError:
                print("Cargo capacity must be a number.")
                continue
            vehicle = Truck(make, model, daily_rate, cargo_capacity_tons)

        fleet.append(vehicle)
        print(f"Registered: {vehicle.describe()}")

    elif choice == "2":
        print()
        if not fleet:
            print("No vehicles in the fleet.")
        else:
            print(f"All vehicles ({len(fleet)}):")
            for i, vehicle in enumerate(fleet, start=1):
                # Polymorphic call: every vehicle answers describe() its own
                # way, no matter its actual subclass -- no type checking here.
                print(f"  {i}. {vehicle.describe()}")

    elif choice == "3":
        print()
        if not fleet:
            print("No vehicles in the fleet.")
            continue
        print(f"All vehicles ({len(fleet)}):")
        for i, vehicle in enumerate(fleet, start=1):
            print(f"  {i}. {vehicle.describe()}")
        index_str = input("Rent which vehicle number? ").strip()
        try:
            index = int(index_str)
        except ValueError:
            print("Please enter a valid vehicle number.")
            continue
        vehicle = find_vehicle(fleet, index)
        if vehicle is None:
            print("No vehicle at that number.")
            continue
        days_str = input("Number of rental days: ").strip()
        try:
            days = int(days_str)
        except ValueError:
            print("Number of days must be a whole number.")
            continue
        if days <= 0:
            print("Number of days must be positive.")
            continue
        # Polymorphic call: each subclass's own calculate_rental_cost() runs.
        cost = vehicle.rent(days)
        print(f"Rental cost for {days} day(s): ${cost:,.2f}")

    elif choice == "4":
        print()
        if not fleet:
            print("No vehicles in the fleet.")
        else:
            total_value = sum(v.daily_rate for v in fleet)
            total_rented_days = sum(v.rented_days for v in fleet)
            num_cars = sum(1 for v in fleet if isinstance(v, Car))
            num_motorcycles = sum(1 for v in fleet if isinstance(v, Motorcycle))
            num_trucks = sum(1 for v in fleet if isinstance(v, Truck))
            print(f"Fleet summary ({len(fleet)} vehicle(s)):")
            print(f"  Cars: {num_cars}  Motorcycles: {num_motorcycles}  Trucks: {num_trucks}")
            print(f"  Combined daily rate: ${total_value:,.2f}")
            print(f"  Total rental-days booked this session: {total_rented_days}")

    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
