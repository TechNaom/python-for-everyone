"""
Chapter 26 Exercises: Debugging Production Issues (Categories 1-8)
Reference solution.
"""

import copy
import json
import math
from collections import deque


# TODO 1
def safe_lookup(config, key, default):
    return config.get(key, default)


# TODO 2
def safe_top_n(scores, n):
    total = 0
    for i in range(min(n, len(scores))):
        total += scores[i]
    return total


# TODO 3
def safe_int_lookup(raw, key, default):
    try:
        return int(raw[key])
    except KeyError:
        return default


# TODO 4
def safe_discount(price, percent_off):
    percent_off = float(percent_off)
    return price - (price * percent_off / 100)


# TODO 5
def find_user_or_raise(users, name):
    for u in users:
        if u["name"] == name:
            return u
    raise ValueError(f"No user found with name {name!r}")


# TODO 6
def average_or_none(total, count):
    if count == 0:
        return None
    return total / count


# TODO 7
def parse_json_safe(raw_text):
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return None


# TODO 8
def load_timeout(raw):
    try:
        return int(raw["timeout"])
    except KeyError:
        return 30


raw_config = {"timeoout": "45"}
print("load_timeout result:", load_timeout(raw_config))
print("raw_config keys:", list(raw_config.keys()))


# TODO 9
def has_duplicate(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False


# TODO 10
def dedupe_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# TODO 11
def index_by_key(records, key_name):
    return {r[key_name]: r for r in records}


# TODO 12
def smallest_and_largest(numbers):
    return (min(numbers), max(numbers))


# TODO 13
def first_match_or_none(items, predicate):
    for item in items:
        if predicate(item):
            return item
    return None


# TODO 14
def reversed_list(items):
    result = []
    for item in items:
        result.append(item)
    result.reverse()
    return result


print(reversed_list([1, 2, 3]))


# TODO 15
def bounded_recent_events(events, maxlen):
    d = deque(maxlen=maxlen)
    for event in events:
        d.append(event)
    return list(d)


# TODO 16
class SharedCounter:
    def __init__(self, name):
        self.name = name
        self.count = []

    def record(self, value):
        self.count.append(value)


counter_a = SharedCounter("a")
counter_b = SharedCounter("b")
counter_a.record(1)
counter_b.record(2)
print(f"counter_a.count: {counter_a.count}")
print(f"same list object: {counter_a.count is counter_b.count}")


# TODO 17
def independent_copy(original):
    return copy.deepcopy(original)


# TODO 18
def floats_equal(a, b):
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)


# TODO 19
def round_quantity(value):
    return round(value)


# TODO 20
def get_page(records, page_number, page_size):
    start = (page_number - 1) * page_size
    return records[start:start + page_size]


print(get_page([10, 20, 30, 40, 50], 1, 2))


# TODO 21
def row_from_fixed_columns(record, column_order):
    return [record[col] for col in column_order]


# TODO 22
def missing_env_keys(env, required_keys):
    return sorted(k for k in required_keys if k not in env)


# TODO 23
def charge_once(processed, idempotency_key, amount):
    if idempotency_key in processed:
        return processed[idempotency_key]
    processed[idempotency_key] = amount
    return amount


# TODO 24
def attach_names(records, lookup_table):
    return [
        {**record, "name": lookup_table.get(record["ref_id"])}
        for record in records
    ]


# TODO 25
def build_log_record(order_id, amount, status):
    return {"order_id": order_id, "amount": amount, "status": status}


# TODO 26
def redact_password(request):
    redacted = dict(request)
    redacted["password"] = "***"
    return redacted


print(redact_password({"user": "ana", "password": "hunter2"}))


if __name__ == "__main__":
    print(safe_lookup({"HOST": "localhost"}, "DATABASE_URL", "not set"))
    print(safe_top_n([88, 92, 79, 95], 5))
    print(safe_int_lookup({"timeoout": "45"}, "timeout", 30))
    print(safe_discount(100, "10"))
    try:
        find_user_or_raise([{"name": "Ana"}], "Carla")
    except ValueError as e:
        print(e)
    print(average_or_none(47, 0))
    print(parse_json_safe("<html>Service Unavailable</html>"))
    print(has_duplicate([1, 2, 3, 2]))
    print(dedupe_preserve_order([1, 2, 1, 3, 2]))
    print(index_by_key([{"id": 1}, {"id": 2}], "id"))
    print(smallest_and_largest([5, 1, 9, 3]))
    print(first_match_or_none([1, 2, 3, 4], lambda x: x > 2))
    print(bounded_recent_events([1, 2, 3, 4, 5], 3))
    print(independent_copy({"items": [1, 2]}))
    print(floats_equal(0.1 + 0.2, 0.3))
    print(round_quantity(4.9))
    print(row_from_fixed_columns({"b": 2, "a": 1}, ["a", "b"]))
    print(missing_env_keys({"A": "1"}, ["A", "B"]))
    print(charge_once({}, "req-1", 50))
    print(attach_names([{"ref_id": 1}], {1: "Ana"}))
    print(build_log_record(102, 599.0, "failed"))
