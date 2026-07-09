"""
Chapter 26 Practice Bank (Categories 1-8): Debugging Production Issues
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Standard library only -- no installs needed.
"""

import copy
import json
import math
from collections import deque

# ============================================================
# Topic 1: Missing Keys & Out-of-Range Access
# ============================================================

# TODO 1.1: Write required_config_or_raise(config, required_keys).
# Check config against the list required_keys. If ANY are missing,
# raise a RuntimeError listing every missing key at once (not just the
# first one found), e.g. "Missing required config keys: ['A', 'B']".
# If nothing is missing, return config unchanged.


# TODO 1.2: Write safe_slice_sum(values, n). Return the sum of the
# first n items of values, but never raise IndexError -- if n is
# larger than len(values), sum everything available instead.


# TODO 1.3 (Debug the Code): last_n_scores() below is supposed to
# return the LAST n scores, but it wrongly uses range(n) to index from
# the FRONT -- for n=2 on [88, 92, 79] it silently returns the wrong
# two scores ([88, 92] instead of [92, 79]) with no crash at all, and
# for a larger n it also raises IndexError. Fix it to use slicing
# instead (scores[-n:]), which returns the right values AND can never
# go out of range.
def last_n_scores(scores, n):
    result = []
    for i in range(n):
        result.append(scores[i])
    return result


print(last_n_scores([88, 92, 79], 2))  # should be [92, 79], not [88, 92]


# TODO 1.A (Scenario -- Comparing Two Approaches): write
# should_use_get(key_always_present). Return True (use plain [] access)
# only if key_always_present is True; otherwise return False (use
# .get() with a default) since the key might be missing.


# TODO 1.B (Scenario -- Interview Prep): write
# explain_keyerror_vs_get() describing when dict[key] is the right
# choice vs. when dict.get(key, default) is.


# ============================================================
# Topic 2: Exception Handling That Hides Bugs
# ============================================================

# TODO 2.1: Write divide_or_none(a, b). Return a / b, or None if b is
# 0 -- catch ZeroDivisionError specifically, not a bare except.


# TODO 2.2: Write parse_int_or_default(raw, default). Try int(raw). If
# raw can't be converted (ValueError), return default. Any OTHER kind
# of exception should NOT be caught -- only catch ValueError.


# TODO 2.3 (Debug the Code): get_setting() below uses a bare except:
# that would hide a real bug (e.g. a NameError from a typo) just as
# easily as the KeyError it's meant to catch. Fix it to catch only
# KeyError.
def get_setting(settings, name):
    try:
        return settings[name]
    except:
        return None


print(get_setting({"debug": True}, "verbose"))


# TODO 2.A (Scenario -- Cleaning Up a Legacy Function): write
# explain_why_bare_except_is_risky() describing, in your own words,
# a realistic scenario where a bare except: hid a real bug for months.


# TODO 2.B (Scenario -- Interview Prep): write
# explain_specific_vs_broad_except() describing why except KeyError:
# is safer than except Exception: even though both "work."


# ============================================================
# Topic 3: None, Zero, and Other Quiet Failure Values
# ============================================================

# TODO 3.1: Write find_or_none(items, predicate_key, predicate_value).
# Loop through items (a list of dicts) and return the first dict where
# item[predicate_key] == predicate_value, or None if nothing matches.
# (This function returning None on no-match is fine -- TODO 3.2 is
# about the CALLER handling that None safely.)


# TODO 3.2: Write get_email_safe(items, name). Use find_or_none() to
# look up a user dict by name (predicate_key="name",
# predicate_value=name). If nothing was found (None), return
# "no email on file" instead of crashing with AttributeError.


# TODO 3.3 (Debug the Code): average_price() below crashes with
# ZeroDivisionError when given an empty list. Fix it to return None
# for an empty list instead.
def average_price(prices):
    return sum(prices) / len(prices)


print(average_price([10, 20, 30]))


# TODO 3.A (Scenario -- Streaming API Data): write
# parse_api_results(raw_text). Try json.loads(raw_text) and return
# data.get("results", []) if it succeeds. If raw_text isn't valid
# JSON (json.JSONDecodeError), return an empty list instead of
# crashing.


# TODO 3.B (Scenario -- Interview Prep): write
# explain_none_vs_exception() describing when a function returning
# None for "not found" is the right design, vs. when raising a named
# exception is better.


# ============================================================
# Topic 4: Accidental O(n^2) Patterns
# ============================================================

# TODO 4.1: Write has_common_element(list_a, list_b). Return True if
# any value appears in both lists. Convert one list to a set first so
# the membership check against it is O(1), not O(n).


# TODO 4.2: Write unique_in_order(items). Return a new list with
# duplicates removed, preserving the order of first occurrence. Use a
# set to track what's already been seen.


# TODO 4.3 (Debug the Code): merge_prepend() below is supposed to
# build a combined list with new_items placed BEFORE existing_items,
# but it does so by calling list.insert(0, x) once per item in a loop
# -- O(n^2) for building an n-item result. Fix it to build the result
# with list concatenation or slicing instead (new_items + existing_items),
# which is O(n) total.
def merge_prepend(existing_items, new_items):
    result = list(existing_items)
    for item in reversed(new_items):
        result.insert(0, item)
    return result


print(merge_prepend([3, 4], [1, 2]))


# TODO 4.A (Scenario -- Comparing Two Approaches): write
# should_use_set_for_lookup(collection_size, checked_repeatedly).
# Return True (use a set) if collection_size is greater than 100 AND
# checked_repeatedly is True, else False (a list is fine for a small
# or one-off check).


# TODO 4.B (Scenario -- Interview Prep): write
# explain_quadratic_pattern() describing the general shape of an
# accidental O(n^2) bug: an O(n) operation performed inside a loop
# that runs n times.


# ============================================================
# Topic 5: Caching & Redundant Work
# ============================================================

# TODO 5.1: Write memoized_calls(keys, compute_fn). Return a list of
# compute_fn(key) for each key in keys, calling compute_fn at most
# once per distinct key (cache repeated keys).


# TODO 5.2: Write count_distinct_calls(keys). Using the same caching
# idea as 5.1 but without actually needing compute_fn, return how many
# DISTINCT values are in keys -- the number of times a "real"
# computation would have been needed if each distinct key were
# computed once.


# TODO 5.3 (Debug the Code): tax_totals() below recomputes
# slow_tax_lookup(region) for every single item, even when many items
# share the same region. Fix it to cache the result per region.
def slow_tax_lookup(region):
    total = 0
    for _ in range(1000):
        total += 1
    return 0.08

def tax_totals(cart):
    total = 0
    for item in cart:
        rate = slow_tax_lookup(item["region"])
        total += item["price"] * (1 + rate)
    return total


print(tax_totals([{"price": 10, "region": "CA"}, {"price": 20, "region": "CA"}]))


# TODO 5.A (Scenario -- A Slow Report Generator): write
# should_cache_by_region(num_items, num_distinct_regions). Return True
# if num_distinct_regions is meaningfully smaller than num_items (say,
# less than half), since that's when caching by region actually saves
# real work.


# TODO 5.B (Scenario -- Interview Prep): write
# explain_when_caching_is_safe() describing the one condition that
# must hold for caching a function's result to be correct, not just
# fast.


# ============================================================
# Topic 6: Unbounded Growth & Shared State
# ============================================================

# TODO 6.1: Write bounded_history(events, maxlen). Add every item in
# events to a collections.deque(maxlen=maxlen), then return it as a
# plain list -- the deque automatically drops the oldest entry once
# full, so the result never holds more than maxlen items.


# TODO 6.2: Write evict_oldest(cache, maxsize). cache is a dict; insert
# key "new" with value "value" (a placeholder single insertion), and
# if that pushes len(cache) over maxsize, remove the FIRST key in
# cache's iteration order (the oldest-inserted, since dicts preserve
# insertion order) before returning the updated cache.


# TODO 6.3 (Debug the Code): Logger below uses a class-level
# history = [], which is shared by every instance instead of being
# unique per instance. Fix it by creating self.history = [] inside
# __init__.
class Logger:
    history = []  # BUG: class attribute, shared by every instance

    def __init__(self, name):
        self.name = name

    def log(self, message):
        self.history.append(message)


logger_x = Logger("x")
logger_y = Logger("y")
logger_x.log("hello from x")
logger_y.log("hello from y")
print(f"logger_x.history: {logger_x.history}")  # should be ["hello from x"] only


# TODO 6.A (Scenario -- Interview Prep): write
# should_use_weakref_registry(purpose_is_tracking_not_owning). Return
# True if purpose_is_tracking_not_owning is True (a registry meant only
# to look things up, not to keep them alive, should use weakrefs).


# TODO 6.B (Scenario -- Interview Prep): write
# explain_reachable_vs_leaked() describing, in your own words, why a
# Python memory leak almost always means "something is still reachable
# that shouldn't be," not a language failure.


# ============================================================
# Topic 7: Concurrency Shapes (Modeled Without Real Threads)
# ============================================================

# TODO 7.1: Write simulate_lost_updates(reads_before_writes).
# reads_before_writes is a list of ints -- the counter value each
# "thread" read just before writing back read_value + 1. Simulate the
# race: the final counter value is simply the LAST write applied
# (max(reads_before_writes) + 1), since every earlier read's increment
# got overwritten by a later thread that read the same stale value.
# Return that final counter value.


# TODO 7.2: Write acquisition_order_is_consistent(lock_orders).
# lock_orders is a list of (first, second) tuples, each naming which
# lock a function acquires first and second. Return True only if every
# pair agrees on the same relative order for any two lock names that
# appear together (no pair has both (a, b) and (b, a) present) --
# False if a conflicting order exists anywhere, which is exactly the
# shape of a lock-ordering deadlock.


# TODO 7.3 (Debug the Code): pop_if_any() below checks "if shared_list"
# and then pops in a separate step -- unsafe under concurrency, since
# another "thread" could empty the list in between (modeled here by
# calling it twice in a row on the same list without the bug actually
# racing, just to exercise the fixed, atomic version). Fix it to do
# the check and pop as a single try/except IndexError instead.
def pop_if_any(shared_list):
    if shared_list:  # BUG: check and act are two separate steps
        return shared_list.pop()
    return None


print(pop_if_any([1, 2, 3]))  # should be 3


# TODO 7.A (Scenario -- Interview Prep): write
# should_use_multiprocessing(is_cpu_bound). Return True if
# is_cpu_bound is True (CPU-bound work needs multiprocessing to
# actually parallelize, since threading is blocked by the GIL).


# TODO 7.B (Scenario -- Interview Prep): write explain_gil_and_threading()
# describing why threading helps I/O-bound work but not CPU-bound work.


# ============================================================
# Topic 8: Data Corruption & Precision
# ============================================================

# TODO 8.1: Write deep_independent_copy(original). Return a copy of
# original (a dict that may contain nested lists/dicts) using
# copy.deepcopy(), so mutating a nested value on the copy never
# affects original.


# TODO 8.2: Write floats_close(a, b). Return True if a and b are close
# enough to count as equal despite floating-point rounding error, using
# math.isclose() -- never a plain == comparison.


# TODO 8.3 (Debug the Code): page_slice() below treats a 1-based
# page_number as if it were already a 0-based offset, silently
# dropping the first page's records. Fix it to convert with
# (page_number - 1) * page_size before slicing.
def page_slice(records, page_number, page_size):
    start = page_number * page_size  # BUG: off-by-one
    return records[start:start + page_size]


print(page_slice([10, 20, 30, 40], 1, 2))  # should be [10, 20]


# TODO 8.A (Scenario -- Interview Prep): write
# explain_mutable_default_argument_trap() describing why a default
# argument value like cart=[] is evaluated once, at function-definition
# time, and shared across every call that doesn't pass its own cart.


# TODO 8.B (Scenario -- Interview Prep): write
# explain_shallow_vs_deep_copy() describing the difference between
# dict.copy() and copy.deepcopy() for a dict containing nested lists.


# ============================================================
# Topic 9: Deployment & Environment
# ============================================================

# TODO 9.1: Write missing_required_env(env, required_keys). Return a
# sorted list of every key in required_keys that's NOT present in env.


# TODO 9.2: Write resolve_config_value(env, key, default). Return
# env[key] if present, otherwise default -- reading from configuration
# instead of ever hardcoding a value like "localhost" into source code.


# TODO 9.3 (Debug the Code): startup_check() below uses a bare except:
# that silently swallows a missing environment variable instead of
# failing loudly with a clear message. Fix it to catch only KeyError
# and raise a RuntimeError naming exactly which variable is missing.
def startup_check(env):
    try:
        return env["DATABASE_URL"]
    except:
        return None  # BUG: silently returns None instead of failing loudly


print(startup_check({}))  # should raise RuntimeError once fixed, not return None


# TODO 9.A (Scenario -- Interview Prep): write
# explain_works_on_my_machine() describing why code that runs fine on
# a developer's machine can fail at startup in production (missing env
# vars, a different Python version, a different working directory).


# TODO 9.B (Scenario -- Interview Prep): write
# explain_pinning_dependencies() describing why an unpinned
# requirements.txt line can break a deployment with no code changes at
# all.


# ============================================================
# Topic 10: Database & API Reliability, and Observability
# ============================================================

# TODO 10.1: Write join_without_n_plus_1(records, lookup_table, key_name).
# records is a list of dicts; lookup_table is a dict mapping some id to
# a value. Return a new list of dicts, each with an added "looked_up"
# key set to lookup_table.get(record[key_name]) -- using the dict
# that's already built, never a per-record scan through a second list.


# TODO 10.2: Write charge_idempotently(processed, idempotency_key, amount).
# processed is a dict mapping idempotency keys already charged to their
# amount. If idempotency_key is already in processed, return its
# existing amount unchanged. Otherwise store amount under that key and
# return it.


# TODO 10.3 (Debug the Code): summarize_log() below builds a free-text
# message that's hard to query at scale. Fix it to return a structured
# dict instead, with keys "order_id", "amount", and "status".
def summarize_log(order_id, amount, status):
    return f"Order {order_id}: ${amount} - {status}"  # BUG: unstructured


print(summarize_log(102, 599.0, "failed"))


# TODO 10.A (Scenario -- Interview Prep): write explain_unknown_vs_no()
# describing why "the API call failed" and "the resource doesn't
# exist" need to be treated as different outcomes, not conflated.


# TODO 10.B (Scenario -- Interview Prep): write
# explain_log_exception_vs_str_e() describing why logger.exception()
# preserves more diagnostic information than logger.error(str(e)).
