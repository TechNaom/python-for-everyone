"""
Chapter 26 Exercises: Debugging Production Issues (Categories 1-8)
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every task here uses only the standard library -- no installs needed.
"""

import copy
import json
import math
from collections import deque


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


# TODO 9: Write has_duplicate(items). Return True if any value appears
# more than once, using a set for the membership check (not repeated
# `in` checks against a list).


# TODO 10: Write dedupe_preserve_order(items). Return a new list with
# duplicates removed, keeping only the first occurrence of each value,
# in original order. Use a set to track what's been seen so far.


# TODO 11: Write index_by_key(records, key_name). Return a dict mapping
# each record's record[key_name] value to the record itself -- the
# one-time setup step that turns a slow nested-loop lookup into an O(1)
# dict lookup.


# TODO 12: Write smallest_and_largest(numbers). Return a tuple
# (min(numbers), max(numbers)) -- without calling sorted().


# TODO 13: Write first_match_or_none(items, predicate). Loop through
# items and return the first one where predicate(item) is True,
# stopping immediately once found. Return None if nothing matches.


# TODO 14 (Debug the Code): reversed_list() below is supposed to
# return items in reverse order, but it uses list.insert(0, x) in a
# loop, which is O(n) per call. Fix it to use .append() followed by
# one .reverse() call instead.
def reversed_list(items):
    result = []
    for item in items:
        result.insert(0, item)
    return result


print(reversed_list([1, 2, 3]))


# TODO 15: Write bounded_recent_events(events, maxlen). Add every item in
# events to a collections.deque(maxlen=maxlen), then return it as a plain
# list -- the deque automatically drops the oldest entry once full, so
# the result never holds more than maxlen items even if events is huge.


# TODO 16 (Debug the Code): SharedCounter below is supposed to give
# each instance its OWN independent count, but "count = []" is written
# at the CLASS level, so every instance shares the exact same list.
# Fix it by moving the list creation into __init__ as self.count.
class SharedCounter:
    count = []  # BUG: class attribute, shared by every instance

    def __init__(self, name):
        self.name = name

    def record(self, value):
        self.count.append(value)


counter_a = SharedCounter("a")
counter_b = SharedCounter("b")
counter_a.record(1)
counter_b.record(2)
print(f"counter_a.count: {counter_a.count}")  # should be [1], not [1, 2]
print(f"same list object: {counter_a.count is counter_b.count}")  # should be False


# TODO 17: Write independent_copy(original). original is a dict that may
# contain nested lists/dicts. Return a copy where mutating any nested
# value on the copy (e.g. copy["items"].append(...)) never affects
# original -- use copy.deepcopy(), not .copy() or dict(original).


# TODO 18: Write floats_equal(a, b). Return True if a and b are close
# enough to count as equal despite floating-point rounding error, using
# math.isclose() -- never a plain == comparison.


# TODO 19: Write round_quantity(value). Return value rounded to the
# nearest whole number as an int, using round() -- not int(), which
# would silently truncate toward zero instead of rounding.


# TODO 20 (Debug the Code): get_page() below is supposed to return the
# 1-based page_number's slice of records, but it treats page_number as
# if it were already a 0-based offset -- for page 1 it actually returns
# what should be page 2's records, silently dropping the first page
# entirely. Fix it by converting to a 0-based offset before slicing:
# start = (page_number - 1) * page_size.
def get_page(records, page_number, page_size):
    start = page_number * page_size  # BUG: should be (page_number - 1) * page_size
    return records[start:start + page_size]


print(get_page([10, 20, 30, 40, 50], 1, 2))  # should be [10, 20], the FIRST page


# TODO 21: Write row_from_fixed_columns(record, column_order). Return a
# list of record's values looked up in column_order's order -- never
# rely on the dict's own key insertion order, since two records built
# from different sources can end up with different key orders even with
# identical fields.


# TODO 22: Write missing_env_keys(env, required_keys). Return a sorted
# list of every key in required_keys that's NOT present in env -- the
# same "list every missing key at once" pattern as issue #1's KeyError
# fix, applied to environment variables instead of a plain config dict.


# TODO 23: Write charge_once(processed, idempotency_key, amount).
# processed is a dict mapping idempotency keys already charged to their
# amount. If idempotency_key is already in processed, return its
# existing stored amount WITHOUT changing anything (a safe retry).
# Otherwise, store amount under that key in processed and return it.


# TODO 24: Write attach_names(records, lookup_table). records is a list
# of dicts each with a "ref_id" key; lookup_table is a dict mapping id
# to name. Return a new list of dicts, each with an added "name" key
# looked up from lookup_table -- build the lookup once, no per-record
# scan through a second list (avoiding the N+1 pattern).


# TODO 25: Write build_log_record(order_id, amount, status). Return a
# dict (not a free-form string) with keys "order_id", "amount", and
# "status" -- structured data a log aggregator can filter on directly,
# instead of a message that needs a fragile regex to parse back out.


# TODO 26 (Debug the Code): redact_password() below is supposed to hide
# a password before logging a request, but it returns the ORIGINAL dict
# unchanged -- the redacted copy it builds is thrown away. Fix it to
# actually return the redacted copy.
def redact_password(request):
    redacted = dict(request)
    redacted["password"] = "***"
    return request  # BUG: returns the original, not the redacted copy


print(redact_password({"user": "ana", "password": "hunter2"}))  # should show "***"
