"""
Chapter 26 Exercises: Debugging Production Issues (Category 1)
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every task here uses only the standard library -- no installs needed.
"""

import json


# TODO 1: Write safe_lookup(config, key, default). Return config[key] if
# key is present, otherwise return default -- never raise KeyError.


# TODO 2: Write safe_top_n(scores, n). Return the sum of the first n
# items of scores, but never index past the end of the list -- if n is
# larger than len(scores), just sum everything available.


# TODO 3: Write safe_int_lookup(raw, key, default). Try to return
# int(raw[key]). If the key is missing, return default. Catch ONLY
# KeyError -- not a bare except: -- so any other kind of error (e.g. the
# value not being convertible to int) still raises normally.


# TODO 4: Write safe_discount(price, percent_off). percent_off might
# arrive as a string (e.g. "10") instead of a number. Convert it to a
# float before using it, so the function works whether it's called with
# apply_discount(100, "10") or apply_discount(100, 10).


# TODO 5: Write find_user_or_raise(users, name). Same idea as a lookup
# that might fail to find a match, but instead of implicitly returning
# None when nothing matches, raise a ValueError with a clear message
# naming which user wasn't found.


# TODO 6: Write average_or_none(total, count). Return total / count, but
# return None instead of crashing if count is 0.


# TODO 7: Write parse_json_safe(raw_text). Try to return json.loads(raw_text).
# If it's not valid JSON, catch json.JSONDecodeError specifically and
# return None instead of letting the exception propagate.


# TODO 8 (Debug the Code): load_timeout() below is supposed to return 30
# if the "timeout" key is missing, but its bare except: also hides a
# real typo in the dict below (the key is "timeoout", not "timeout").
# Fix the except clause so it only catches KeyError, then notice (by
# printing raw.keys()) that the typo is a separate bug worth fixing too.
def load_timeout(raw):
    try:
        return int(raw["timeout"])
    except:
        return 30


raw_config = {"timeoout": "45"}
print("load_timeout result:", load_timeout(raw_config))
print("raw_config keys:", list(raw_config.keys()))
