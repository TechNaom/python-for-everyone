"""
Chapter 26 Practice Bank (Category 1): Debugging Production Issues
Reference solution.
"""

import json

# ============================================================
# Topic 1: Missing Keys & Out-of-Range Access
# ============================================================

# TODO 1.1
def required_config_or_raise(config, required_keys):
    missing = [k for k in required_keys if k not in config]
    if missing:
        raise RuntimeError(f"Missing required config keys: {missing}")
    return config


# TODO 1.2
def safe_slice_sum(values, n):
    total = 0
    for i in range(min(n, len(values))):
        total += values[i]
    return total


# TODO 1.3
def last_n_scores(scores, n):
    return scores[-n:]


print(last_n_scores([88, 92, 79], 2))


# TODO 1.A
def should_use_get(key_always_present):
    return key_always_present is True


# TODO 1.B
def explain_keyerror_vs_get():
    return (
        "Use dict[key] when the key is guaranteed to exist -- a missing "
        "key means a real bug, and you want it to crash loudly right "
        "there. Use dict.get(key, default) when the key is genuinely "
        "optional, so a missing key is expected, normal input, not an "
        "error."
    )


# ============================================================
# Topic 2: Exception Handling That Hides Bugs
# ============================================================

# TODO 2.1
def divide_or_none(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# TODO 2.2
def parse_int_or_default(raw, default):
    try:
        return int(raw)
    except ValueError:
        return default


# TODO 2.3
def get_setting(settings, name):
    try:
        return settings[name]
    except KeyError:
        return None


print(get_setting({"debug": True}, "verbose"))


# TODO 2.A
def explain_why_bare_except_is_risky():
    return (
        "A config loader used a bare except: to fall back to a default "
        "timeout when a key was missing. Months later someone typo'd "
        "the key name while refactoring -- the bare except: caught that "
        "KeyError too and silently returned the default, so the typo "
        "was never noticed and the intended timeout was never actually "
        "applied in production."
    )


# TODO 2.B
def explain_specific_vs_broad_except():
    return (
        "except KeyError: only catches the exact failure you anticipated. "
        "except Exception: (or a bare except:) also catches everything "
        "else -- a typo, a NameError, a totally unrelated bug -- and "
        "silently treats it the same as the expected case, hiding real "
        "problems instead of surfacing them."
    )


# ============================================================
# Topic 3: None, Zero, and Other Quiet Failure Values
# ============================================================

# TODO 3.1
def find_or_none(items, predicate_key, predicate_value):
    for item in items:
        if item.get(predicate_key) == predicate_value:
            return item
    return None


# TODO 3.2
def get_email_safe(items, name):
    user = find_or_none(items, "name", name)
    if user is None:
        return "no email on file"
    return user.get("email", "no email on file")


# TODO 3.3
def average_price(prices):
    if not prices:
        return None
    return sum(prices) / len(prices)


print(average_price([10, 20, 30]))


# TODO 3.A
def parse_api_results(raw_text):
    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        return []
    return data.get("results", [])


# TODO 3.B
def explain_none_vs_exception():
    return (
        "Returning None for 'not found' fits when not-found is a normal, "
        "expected outcome the caller should handle inline -- like looking "
        "up an optional setting. Raising a named exception fits when "
        "not-found means something is actually wrong and should stop "
        "execution or be handled explicitly further up -- like a required "
        "user record that must exist for the rest of the function to make "
        "sense."
    )


# ============================================================
# Topic 4: Accidental O(n^2) Patterns
# ============================================================

# TODO 4.1
def has_common_element(list_a, list_b):
    set_b = set(list_b)
    for item in list_a:
        if item in set_b:
            return True
    return False


# TODO 4.2
def unique_in_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# TODO 4.3
def merge_prepend(existing_items, new_items):
    return list(new_items) + list(existing_items)


print(merge_prepend([3, 4], [1, 2]))


# TODO 4.A
def should_use_set_for_lookup(collection_size, checked_repeatedly):
    return collection_size > 100 and checked_repeatedly is True


# TODO 4.B
def explain_quadratic_pattern():
    return (
        "An accidental O(n^2) bug is almost always the same shape: an "
        "operation that's O(n) on its own (a list membership check, an "
        "insert at the front, a scan through a second list) gets placed "
        "inside a loop that runs n times. Each individual operation "
        "looks fine -- it's only the multiplication of n times an O(n) "
        "cost that produces O(n^2) overall, and that only becomes "
        "visible once the input is large enough."
    )


# ============================================================
# Topic 5: Caching & Redundant Work
# ============================================================

# TODO 5.1
def memoized_calls(keys, compute_fn):
    cache = {}
    results = []
    for key in keys:
        if key not in cache:
            cache[key] = compute_fn(key)
        results.append(cache[key])
    return results


# TODO 5.2
def count_distinct_calls(keys):
    return len(set(keys))


# TODO 5.3
def slow_tax_lookup(region):
    total = 0
    for _ in range(1000):
        total += 1
    return 0.08


def tax_totals(cart):
    total = 0
    cache = {}
    for item in cart:
        region = item["region"]
        if region not in cache:
            cache[region] = slow_tax_lookup(region)
        total += item["price"] * (1 + cache[region])
    return total


print(tax_totals([{"price": 10, "region": "CA"}, {"price": 20, "region": "CA"}]))


# TODO 5.A
def should_cache_by_region(num_items, num_distinct_regions):
    return num_distinct_regions < num_items / 2


# TODO 5.B
def explain_when_caching_is_safe():
    return (
        "Caching a function's result is only correct when the same "
        "input reliably produces the same output every time, with no "
        "dependency on anything that changes between calls -- no live "
        "external state, no randomness, no time-dependence. A tax rate "
        "for a fixed region during checkout is safe to cache; a live "
        "stock price or a random value is not, since caching either "
        "would silently return a stale or wrong result instead of just "
        "being slower."
    )


if __name__ == "__main__":
    print(required_config_or_raise({"A": 1, "B": 2}, ["A", "B"]))
    print(safe_slice_sum([1, 2, 3], 10))
    print(should_use_get(True))
    print(divide_or_none(10, 0))
    print(parse_int_or_default("abc", -1))
    print(find_or_none([{"name": "Ana"}], "name", "Beto"))
    print(get_email_safe([{"name": "Ana"}], "Beto"))
    print(parse_api_results("<html>Down</html>"))
    print(has_common_element([1, 2, 3], [3, 4, 5]))
    print(unique_in_order([1, 2, 1, 3, 2]))
    print(memoized_calls(["a", "b", "a"], str.upper))
    print(count_distinct_calls(["a", "b", "a"]))
    print(should_cache_by_region(100, 5))
