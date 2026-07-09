"""
Chapter 26 Exercises: Debugging Production Issues (Category 1)
Reference solution.
"""

import json


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
