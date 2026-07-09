"""
Chapter 26 Project (Category 1): Production Incident Runbook
See README.md in this folder for full instructions.
Run this from inside the project/ folder: python3 starter.py

Standard library only -- no installs needed.
"""

# The catalog: each entry mirrors one issue card from the Category 1
# lesson. "keywords" are lowercase substrings the classifier looks for
# in a symptom description.
CATALOG = [
    {
        "id": 1,
        "exception": "KeyError",
        "keywords": ["keyerror", "missing key", "config key", "no such key"],
        "root_cause": "A dict was accessed with [] on a key that isn't present -- often a config/env var missing in this environment.",
        "fix": "Use .get(key, default) for optional keys, or validate all required keys explicitly at startup and fail with a clear message.",
    },
    {
        "id": 2,
        "exception": "IndexError",
        "keywords": ["indexerror", "index out of range", "list index"],
        "root_cause": "A loop bound (often range(n)) assumed a list was at least as long as n, and it wasn't.",
        "fix": "Bound the loop by the list's own length, e.g. range(min(n, len(items))), or slice instead of indexing.",
    },
    {
        "id": 3,
        "exception": "(silent -- no exception)",
        "keywords": ["bare except", "silently returns", "wrong value returned", "no error but wrong"],
        "root_cause": "A bare except: (or overly broad except Exception:) caught an unrelated bug and silently returned a fallback value.",
        "fix": "Catch only the specific exception you expect (e.g. except KeyError:), never a bare except:.",
    },
    {
        "id": 4,
        "exception": "TypeError",
        "keywords": ["typeerror", "unsupported operand", "str and int", "wrong type"],
        "root_cause": "External input (form data, query params) arrived as a string and was passed through several calls before arithmetic failed.",
        "fix": "Convert and validate external input at the boundary where it enters the system, not deep inside business logic.",
    },
    {
        "id": 5,
        "exception": "AttributeError",
        "keywords": ["attributeerror", "nonetype", "has no attribute"],
        "root_cause": "A function implicitly returned None on some code path (no explicit return), and a caller called a method on the result without checking.",
        "fix": "Check for `is None` right where the value comes back, before calling any method on it, or raise a named exception instead of returning None.",
    },
    {
        "id": 6,
        "exception": "(silent -- no exception)",
        "keywords": ["swallowed", "custom exception", "except exception", "insufficientfunds"],
        "root_cause": "A caller's except Exception: caught a specific custom exception too, treating a meaningful failure like a generic one.",
        "fix": "Catch the specific custom exception type and handle it deliberately, instead of catching Exception broadly.",
    },
    {
        "id": 7,
        "exception": "RecursionError",
        "keywords": ["recursionerror", "maximum recursion depth"],
        "root_cause": "A recursive function's base case can be stepped over (e.g. `!= 0` with a starting value that skips past 0) instead of reliably reached.",
        "fix": "Use a base case that can't be skipped, like `<= 0` instead of `!= 0`, or validate input before recursion begins.",
    },
    {
        "id": 8,
        "exception": "ZeroDivisionError",
        "keywords": ["zerodivisionerror", "division by zero"],
        "root_cause": "A denominator sourced from external/variable data (e.g. a count of reviews) was a legitimate 0 that the code never checked for.",
        "fix": "Check the denominator before dividing and return a sensible value (0, None, or a message) for the zero case.",
    },
    {
        "id": 9,
        "exception": "PermissionError",
        "keywords": ["permissionerror", "permission denied"],
        "root_cause": "Code only caught FileNotFoundError, but the file exists and the process lacks OS-level permission to read it -- a different exception entirely.",
        "fix": "Catch FileNotFoundError and PermissionError separately, and handle each differently (missing vs. misconfigured access).",
    },
    {
        "id": 10,
        "exception": "JSONDecodeError",
        "keywords": ["jsondecodeerror", "expecting value", "not valid json"],
        "root_cause": "Code assumed an API response body was always JSON without checking the status code first -- an outage/redirect returned HTML instead.",
        "fix": "Check response.status_code before parsing, and wrap json.loads() in its own try/except for a clear error on non-JSON bodies.",
    },
]


# TODO 1: Write classify_symptom(description). Lowercase `description`,
# then return a list of every CATALOG entry whose "keywords" list has
# at least one keyword that's a substring of the lowercased
# description -- most-specific-match-first isn't required, just
# preserve CATALOG order. Return an empty list if nothing matches.


# TODO 2: Write format_runbook_entry(entry). Return a multi-line string:
#   "Issue #{id}: {exception}"
#   "  Root cause: {root_cause}"
#   "  Fix: {fix}"


# TODO 3: Write diagnose(description). Call classify_symptom(). If no
# matches, return "No matching catalog entry for this symptom yet --
# check Category 1 in the lesson for the closest pattern." If there
# are matches, return format_runbook_entry() for each match, joined by
# a blank line between entries.


def run():
    sample_symptoms = [
        "Service crashes on startup with a KeyError for a missing config key",
        "Function looks like it works but silently returns the wrong value -- no error, just a bare except somewhere",
        "API call returns 503 but our code tries json.loads on it anyway and gets 'Expecting value'",
        "Everything is fine, no crash at all",
    ]
    for symptom in sample_symptoms:
        print(f"SYMPTOM: {symptom}")
        print(diagnose(symptom))
        print()


if __name__ == "__main__":
    run()
