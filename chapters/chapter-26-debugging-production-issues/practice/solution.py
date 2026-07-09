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


if __name__ == "__main__":
    print(required_config_or_raise({"A": 1, "B": 2}, ["A", "B"]))
    print(safe_slice_sum([1, 2, 3], 10))
    print(should_use_get(True))
    print(divide_or_none(10, 0))
    print(parse_int_or_default("abc", -1))
    print(find_or_none([{"name": "Ana"}], "name", "Beto"))
    print(get_email_safe([{"name": "Ana"}], "Beto"))
    print(parse_api_results("<html>Down</html>"))
