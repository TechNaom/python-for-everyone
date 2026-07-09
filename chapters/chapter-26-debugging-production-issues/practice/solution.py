"""
Chapter 26 Practice Bank (Categories 1-8): Debugging Production Issues
Reference solution.
"""

import copy
import json
import math
from collections import deque

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


# ============================================================
# Topic 6: Unbounded Growth & Shared State
# ============================================================

# TODO 6.1
def bounded_history(events, maxlen):
    d = deque(maxlen=maxlen)
    for event in events:
        d.append(event)
    return list(d)


# TODO 6.2
def evict_oldest(cache, maxsize):
    cache["new"] = "value"
    if len(cache) > maxsize:
        oldest_key = next(iter(cache))
        del cache[oldest_key]
    return cache


# TODO 6.3
class Logger:
    def __init__(self, name):
        self.name = name
        self.history = []

    def log(self, message):
        self.history.append(message)


logger_x = Logger("x")
logger_y = Logger("y")
logger_x.log("hello from x")
logger_y.log("hello from y")
print(f"logger_x.history: {logger_x.history}")


# TODO 6.A
def should_use_weakref_registry(purpose_is_tracking_not_owning):
    return purpose_is_tracking_not_owning is True


# TODO 6.B
def explain_reachable_vs_leaked():
    return (
        "Python's garbage collector reclaims anything genuinely "
        "unreachable -- a memory leak in Python almost always means "
        "something is still reachable that shouldn't be: an unbounded "
        "module-level cache, a closure capturing a list it never trims, "
        "a registry holding strong references to values it only meant "
        "to look up. It's a solvable, mechanical search for a reference "
        "that outlives its intended purpose, not a language failure."
    )


# ============================================================
# Topic 7: Concurrency Shapes (Modeled Without Real Threads)
# ============================================================

# TODO 7.1
def simulate_lost_updates(reads_before_writes):
    return max(reads_before_writes) + 1


# TODO 7.2
def acquisition_order_is_consistent(lock_orders):
    seen_orders = set()
    for first, second in lock_orders:
        if (second, first) in seen_orders:
            return False
        seen_orders.add((first, second))
    return True


# TODO 7.3
def pop_if_any(shared_list):
    try:
        return shared_list.pop()
    except IndexError:
        return None


print(pop_if_any([1, 2, 3]))


# TODO 7.A
def should_use_multiprocessing(is_cpu_bound):
    return is_cpu_bound is True


# TODO 7.B
def explain_gil_and_threading():
    return (
        "The GIL allows only one thread to execute Python bytecode at "
        "a time, no matter how many CPU cores exist. Threading helps "
        "I/O-bound work because the GIL is released while a thread "
        "waits on a network response or disk I/O -- other threads can "
        "run during that wait. A CPU-bound loop never waits for "
        "anything, so the GIL keeps threads running one at a time "
        "regardless of core count, and multiprocessing (separate "
        "processes, separate GILs) is the right tool instead."
    )


# ============================================================
# Topic 8: Data Corruption & Precision
# ============================================================

# TODO 8.1
def deep_independent_copy(original):
    return copy.deepcopy(original)


# TODO 8.2
def floats_close(a, b):
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)


# TODO 8.3
def page_slice(records, page_number, page_size):
    start = (page_number - 1) * page_size
    return records[start:start + page_size]


print(page_slice([10, 20, 30, 40], 1, 2))


# TODO 8.A
def explain_mutable_default_argument_trap():
    return (
        "A default argument value is evaluated exactly once, when the "
        "def statement runs, not fresh on every call. cart=[] creates "
        "one single list object at function-definition time; every "
        "call that doesn't pass its own cart argument gets that same "
        "object, and any mutation persists onto the next such call. "
        "The fix is cart=None as the default, creating a fresh list "
        "inside the function body when cart is None."
    )


# TODO 8.B
def explain_shallow_vs_deep_copy():
    return (
        "dict.copy() creates a new dict, but every value inside it is "
        "the same object as in the original, not a new copy of that "
        "value -- mutating a shared nested list or dict in place still "
        "affects the original. copy.deepcopy() recursively copies "
        "every mutable value nested inside, so the copy is fully "
        "independent all the way down."
    )


# ============================================================
# Topic 9: Deployment & Environment
# ============================================================

# TODO 9.1
def missing_required_env(env, required_keys):
    return sorted(k for k in required_keys if k not in env)


# TODO 9.2
def resolve_config_value(env, key, default):
    return env.get(key, default)


# TODO 9.3
def startup_check(env):
    try:
        return env["DATABASE_URL"]
    except KeyError:
        raise RuntimeError("Missing required environment variable: DATABASE_URL")


try:
    print(startup_check({}))
except RuntimeError as e:
    print(e)


# TODO 9.A
def explain_works_on_my_machine():
    return (
        "A developer's machine accumulates local setup over time -- "
        "environment variables exported by a shell profile, an "
        "up-to-date Python version, a working directory that always "
        "happens to line up -- none of which a freshly provisioned "
        "production server has unless it was explicitly configured. "
        "Code that implicitly depends on any of that runs fine locally "
        "and fails immediately in a clean environment."
    )


# TODO 9.B
def explain_pinning_dependencies():
    return (
        "An unpinned requirements.txt line doesn't mean 'the version I "
        "tested with' -- it means whatever the newest compatible "
        "version is at the exact moment pip install runs. A new "
        "release can change default behavior or pull in an "
        "incompatible sub-dependency, breaking a deployment with zero "
        "code changes. Pinning exact versions (or using a lockfile) "
        "makes every install reproduce the same environment."
    )


# ============================================================
# Topic 10: Database & API Reliability, and Observability
# ============================================================

# TODO 10.1
def join_without_n_plus_1(records, lookup_table, key_name):
    return [
        {**record, "looked_up": lookup_table.get(record[key_name])}
        for record in records
    ]


# TODO 10.2
def charge_idempotently(processed, idempotency_key, amount):
    if idempotency_key in processed:
        return processed[idempotency_key]
    processed[idempotency_key] = amount
    return amount


# TODO 10.3
def summarize_log(order_id, amount, status):
    return {"order_id": order_id, "amount": amount, "status": status}


print(summarize_log(102, 599.0, "failed"))


# TODO 10.A
def explain_unknown_vs_no():
    return (
        "Catching a broad exception around a dependency call and "
        "returning a definitive-looking result (like 'not in stock') "
        "on any failure conflates two different situations: a genuine "
        "answer from the dependency, and a failure to get an answer at "
        "all. They need different handling -- a cached last-known "
        "value, an 'unknown' state, or a loud failure -- rather than "
        "silently reinterpreting 'unreachable' as a real answer."
    )


# TODO 10.B
def explain_log_exception_vs_str_e():
    return (
        "str(e) converts an exception to just its message text -- "
        "everything else (which file, which line, the full call stack) "
        "is discarded. logger.exception(), called from inside an "
        "except block, automatically attaches the full traceback to "
        "the log record, giving anyone reading the log the same "
        "information they'd have seen if the exception had crashed the "
        "program uncaught."
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
    print(bounded_history([1, 2, 3, 4, 5], 3))
    print(evict_oldest({"a": 1, "b": 2}, 2))
    print(should_use_weakref_registry(True))
    print(simulate_lost_updates([0, 0, 1]))
    print(acquisition_order_is_consistent([("a", "b"), ("a", "b")]))
    print(acquisition_order_is_consistent([("a", "b"), ("b", "a")]))
    print(deep_independent_copy({"items": [1, 2]}))
    print(floats_close(0.1 + 0.2, 0.3))
    print(missing_required_env({"A": "1"}, ["A", "B"]))
    print(resolve_config_value({}, "DATABASE_URL", "localhost"))
    print(charge_idempotently({}, "req-1", 50))
    print(join_without_n_plus_1([{"id": 1}], {1: "Ana"}, "id"))
