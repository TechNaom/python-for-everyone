"""
Chapter 26 Practice Bank (Category 1): Debugging Production Issues
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Standard library only -- no installs needed.
"""

import json

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
