"""
Chapter 11 Practice Bank: Modules & Packages -- reference solution.
See README.md in this folder for full instructions.
"""

import math
import datetime
import random

# ============================================================
# Topic 1: What Is a Module?
# ============================================================

# TODO 1.1
def pi_times_two():
    return math.pi * 2


print(pi_times_two())


# TODO 1.2
def describe_module(name, purpose):
    return f"The {name} module is useful for {purpose}."


print(describe_module("math", "numeric calculations"))
print(describe_module("random", "generating randomness"))


# TODO 1.3
def without_module_pi():
    return 3.14159


def with_module_pi():
    return math.pi


print(without_module_pi())
print(with_module_pi())


# TODO 1.4
def circle_circumference(radius):
    return 2 * math.pi * radius


print(circle_circumference(5))
print(circle_circumference(1))


# TODO 1.5 (Debug the Code)
def circle_area(radius):
    return math.pi * radius ** 2


print(circle_area(3))


# TODO 1.A (Scenario -- Why Real Projects Use Modules)
def explain_module_reuse():
    return (
        "A module is a single .py file that groups related, tested code "
        "so it can be imported and reused across many programs instead of "
        "being rewritten from scratch every time -- math, random, and "
        "datetime are all modules that ship with Python itself."
    )


print(explain_module_reuse())


# TODO 1.B (Scenario -- Interview Prep)
def why_not_reinvent_pi():
    return (
        "Using math.pi instead of a hand-typed 3.14159 gives more decimal "
        "precision, is instantly recognizable to any other Python "
        "developer reading the code, and can't be mistyped -- reaching "
        "for a well-tested standard library module beats reinventing "
        "constants or algorithms that already exist and are already "
        "battle-tested."
    )


print(why_not_reinvent_pi())


# ============================================================
# Topic 2: Import Variations
# ============================================================

# TODO 2.1
def sqrt_via_plain_import(n):
    return math.sqrt(n)


print(sqrt_via_plain_import(16))


from math import sqrt


# TODO 2.2
def sqrt_via_from_import(n):
    return sqrt(n)


print(sqrt_via_from_import(25))


import math as m


# TODO 2.3
def pi_via_aliased_import():
    return m.pi


print(pi_via_aliased_import())


from random import randint as ri


# TODO 2.4
def dice_roll_via_aliased_from_import():
    return ri(1, 6)


roll = dice_roll_via_aliased_from_import()
print(1 <= roll <= 6)


# TODO 2.5 (Debug the Code)
def ceil_via_plain_import(n):
    return math.ceil(n)


print(ceil_via_plain_import(4.1))


# TODO 2.A (Scenario -- Picking the Right Import Style)
def compare_import_styles():
    return (
        "import math keeps every name behind the math. prefix, which is "
        "clearest in a large file with many modules; from math import "
        "sqrt is shorter for a name used constantly; import math as m or "
        "from math import sqrt as square_root just renames the module or "
        "name, which is handy for long names or avoiding a clash with a "
        "variable you already have."
    )


print(compare_import_styles())


# TODO 2.B (Scenario -- Interview Prep)
def explain_import_variations():
    return (
        "import x loads the whole module and every name inside it must be "
        "reached through x.name; from x import y pulls just y into the "
        "current namespace so it's used directly as y(); the `as` form in "
        "either style only renames what you just imported, it doesn't "
        "change what the module actually contains."
    )


print(explain_import_variations())


# ============================================================
# Topic 3: The math Module
# ============================================================

# TODO 3.1
def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


print(hypotenuse(3, 4))


# TODO 3.2
def round_down_and_up(n):
    return (math.floor(n), math.ceil(n))


print(round_down_and_up(4.3))
print(round_down_and_up(4.7))


# TODO 3.3
def power_of(base, exponent):
    return math.pow(base, exponent)


print(power_of(2, 10))


# TODO 3.4
def circle_area(radius):
    return math.pi * radius ** 2


print(round(circle_area(2), 2))


# TODO 3.5 (Debug the Code)
def containers_needed(total_items, capacity):
    return math.ceil(total_items / capacity)


print(containers_needed(23, 5))


# TODO 3.A (Scenario -- Shipping Box Calculator)
def boxes_required(num_items, items_per_box):
    return math.ceil(num_items / items_per_box)


print(boxes_required(100, 12))
print(boxes_required(12, 12))


# TODO 3.B (Scenario -- Interview Prep)
def explain_floor_vs_ceil_vs_round():
    return (
        "math.floor always rounds down toward negative infinity, "
        "math.ceil always rounds up toward positive infinity, and the "
        "built-in round() rounds to the *nearest* whole number (or nearest "
        "given decimal place) -- floor(4.1) is 4 and ceil(4.1) is 5, "
        "while round(4.1) is also 4 but round(4.6) is 5, so round is the "
        "only one of the three that can go either direction depending on "
        "the fractional part."
    )


print(explain_floor_vs_ceil_vs_round())


# ============================================================
# Topic 4: The datetime Module
# ============================================================

# TODO 4.1
def make_date(year, month, day):
    return datetime.date(year, month, day)


launch_date = make_date(2026, 7, 5)
print(launch_date)


# TODO 4.2
def format_date_long(a_date):
    return a_date.strftime("%B %d, %Y")


print(format_date_long(datetime.date(2026, 7, 5)))


# TODO 4.3
def days_between(date_a, date_b):
    return (date_b - date_a).days


print(days_between(datetime.date(2026, 1, 1), datetime.date(2026, 7, 5)))


# TODO 4.4
def days_since_today():
    today = datetime.date.today()
    return (today - today).days


print(days_since_today())


# TODO 4.5 (Debug the Code)
def days_until_deadline(deadline):
    today = datetime.date.today()
    return (deadline - today).days


print(days_until_deadline(datetime.date(2027, 1, 1)) >= 0)


# TODO 4.A (Scenario -- Subscription Renewal Countdown)
def days_until_renewal(signup_date, renewal_days=365):
    renewal_date = signup_date + datetime.timedelta(days=renewal_days)
    return (renewal_date - signup_date).days


print(days_until_renewal(datetime.date(2026, 1, 1)))
print(days_until_renewal(datetime.date(2026, 1, 1), renewal_days=30))


# TODO 4.B (Scenario -- Interview Prep)
def explain_date_arithmetic():
    return (
        "Subtracting one datetime.date from another gives a timedelta "
        "object (not a plain number), and that timedelta's .days "
        "attribute is the whole number of days between them -- this is "
        "why date_b - date_a works directly in Python without manually "
        "counting days in each month, and it's the same reason you add a "
        "timedelta (not a raw int) to a date to shift it forward or "
        "backward."
    )


print(explain_date_arithmetic())


# ============================================================
# Topic 5: The random Module
# ============================================================

# TODO 5.1
def roll_die():
    return random.randint(1, 6)


die_result = roll_die()
print(1 <= die_result <= 6)


# TODO 5.2
def pick_random_name(names):
    return random.choice(names)


team = ["Asha", "Ravi", "Meera"]
picked = pick_random_name(team)
print(picked in team)


# TODO 5.3
def shuffled_copy(items):
    copy_of_items = items[:]
    random.shuffle(copy_of_items)
    return copy_of_items


original = [1, 2, 3, 4, 5]
shuffled = shuffled_copy(original)
print(sorted(shuffled) == sorted(original))
print(original)


# TODO 5.4
def random_percentage():
    return random.randint(0, 100)


pct = random_percentage()
print(0 <= pct <= 100)


# TODO 5.5 (Debug the Code)
def pick_a_card(cards):
    return random.choice(cards)


deck = ["Ace", "King", "Queen", "Jack"]
card = pick_a_card(deck)
print(card in deck)


# TODO 5.A (Scenario -- Randomized A/B Test Assignment)
def assign_ab_group():
    return random.choice(["A", "B"])


group = assign_ab_group()
print(group in ("A", "B"))


# TODO 5.B (Scenario -- Interview Prep)
def explain_random_vs_deterministic():
    return (
        "random.randint/choice/shuffle all rely on a pseudo-random number "
        "generator, so their exact output is unpredictable and different "
        "on every run -- that's why tests around random code should check "
        "a *property* of the result (like 'is it in range' or 'does it "
        "still contain the same elements') rather than asserting one "
        "exact value, which would fail most of the time by design."
    )


print(explain_random_vs_deterministic())


# ============================================================
# Topic 6: Bringing It Together -- Modules in Production
# ============================================================

# TODO 6.1
def generate_order_id(order_number):
    today_str = datetime.date.today().strftime("%Y%m%d")
    return f"ORD-{today_str}-{order_number:04d}"


print(generate_order_id(7))


# TODO 6.2
def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print(distance_between_points(0, 0, 3, 4))


# TODO 6.3
def pick_daily_special(menu_items):
    return random.choice(menu_items)


menu = ["Pasta", "Salad", "Soup", "Sandwich"]
special = pick_daily_special(menu)
print(special in menu)


# TODO 6.4
def subscription_status(start_date, length_days=30):
    end_date = start_date + datetime.timedelta(days=length_days)
    today = datetime.date.today()
    return "active" if today <= end_date else "expired"


print(subscription_status(datetime.date(2020, 1, 1)))


# TODO 6.5 (Debug the Code)
def price_after_random_discount(price, discount_percent):
    discounted = price - price * discount_percent / 100
    return round(discounted, 2)


final_price = price_after_random_discount(200, random.randint(5, 25))
print(final_price < 200)


# TODO 6.A (Scenario -- Production Order Confirmation Builder)
def build_order_confirmation(order_number, price_per_item, quantity):
    total = round(price_per_item * quantity, 2)
    order_id = generate_order_id(order_number)
    processing_days = math.ceil(quantity / 10)
    ship_by = datetime.date.today() + datetime.timedelta(days=processing_days)
    return {
        "order_id": order_id,
        "total": total,
        "ship_by": ship_by.strftime("%Y-%m-%d"),
    }


confirmation = build_order_confirmation(42, 9.99, 23)
print(confirmation["order_id"])
print(confirmation["total"])
print("ship_by" in confirmation)


# TODO 6.B (Scenario -- Interview Prep)
def explain_stdlib_value():
    return (
        "Real production code leans on math, random, and datetime "
        "constantly: math for pricing/geometry/rounding logic, datetime "
        "for order timestamps/subscription windows/deadlines, and random "
        "for A/B test assignment, sampling, or generating test data -- "
        "using the standard library instead of hand-rolling this logic "
        "means fewer bugs, since these modules are already tested by "
        "millions of other programs, and any other Python developer "
        "instantly recognizes what math.sqrt or datetime.date is doing."
    )


print(explain_stdlib_value())
