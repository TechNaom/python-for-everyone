"""
Chapter 26 Project (Categories 1-2): Production Incident Runbook
Reference solution.
"""

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
    {
        "id": 11,
        "exception": "(no exception -- slow)",
        "keywords": ["quadratic", "gets slower as", "scales badly", "membership check slow"],
        "root_cause": "A membership check (`in`) against a list, done repeatedly inside a loop, is O(n) per check -- doing it n times makes the whole function O(n^2).",
        "fix": "Use a set instead of a list for repeated membership checks -- O(1) average case regardless of size.",
    },
    {
        "id": 12,
        "exception": "(no exception -- slow)",
        "keywords": ["insert(0", "insert at the front", "prepend slow"],
        "root_cause": "list.insert(0, x) shifts every existing element over by one -- O(n) per call, O(n^2) total when called n times in a loop.",
        "fix": "Append to the end instead (O(1) amortized), then call .reverse() once at the end if order matters.",
    },
    {
        "id": 13,
        "exception": "(no exception -- slow)",
        "keywords": ["recompute", "recalculating", "redundant work", "repeated lookup slow"],
        "root_cause": "The same expensive computation was repeated for every occurrence of the same input, instead of being computed once and reused.",
        "fix": "Cache results in a dict keyed by whatever determines the result, and only recompute for genuinely new inputs.",
    },
    {
        "id": 14,
        "exception": "(no exception -- slow)",
        "keywords": ["nested loop", "join two lists", "n times m", "times out"],
        "root_cause": "A nested loop scanned an entire second list once per item of the first -- O(n*m) instead of O(n+m).",
        "fix": "Build a dict mapping the join key to record once, up front, then look up each item in O(1) instead of scanning.",
    },
    {
        "id": 15,
        "exception": "(no exception -- slow)",
        "keywords": ["regex slow", "re.search slow", "recompiling"],
        "root_cause": "re.search(pattern, text) re-parses the pattern string internally on every call when the same pattern is reused repeatedly.",
        "fix": "Call re.compile(pattern) once, outside any loop, and reuse the compiled pattern object.",
    },
    {
        "id": 16,
        "exception": "(no exception -- slow)",
        "keywords": ["sorted()[-1]", "sorting just to get", "sort for max"],
        "root_cause": "sorted() is O(n log n) and orders the entire list, even when only the single largest or smallest value is actually needed.",
        "fix": "Use max() or min() for a single extreme value -- O(n), no sorting required.",
    },
    {
        "id": 17,
        "exception": "(no exception -- slow)",
        "keywords": ["len() in loop", "len(items) every iteration"],
        "root_cause": "Calling len() fresh on every iteration of a while loop repeats small, avoidable function-call overhead across every pass.",
        "fix": "Compute len(items) once, store it in a variable before the loop, and check against that instead.",
    },
    {
        "id": 18,
        "exception": "(no exception -- slow)",
        "keywords": ["re-reading the file", "reopening the file", "reading disk repeatedly"],
        "root_cause": "The same file was opened and read from disk once per search term, even though its contents never changed between calls.",
        "fix": "Read the file into memory exactly once, then run every search against that in-memory content.",
    },
    {
        "id": 19,
        "exception": "(no exception -- slow)",
        "keywords": ["materializes", "list comprehension slow", "builds the full list first"],
        "root_cause": "A list comprehension computed every value up front, even though the consuming loop could exit early after finding a match.",
        "fix": "Use a generator expression instead -- values are produced lazily, so unconsumed values are never computed at all.",
    },
    {
        "id": 20,
        "exception": "(no exception -- slow)",
        "keywords": ["dict.keys() slow", "in dict.keys()"],
        "root_cause": "key in some_dict.keys() adds an unnecessary view-object layer -- key in some_dict is already O(1) on its own.",
        "fix": "Drop the .keys() -- check membership directly against the dict.",
    },
]


# TODO 1
def classify_symptom(description):
    lowered = description.lower()
    matches = []
    for entry in CATALOG:
        if any(keyword in lowered for keyword in entry["keywords"]):
            matches.append(entry)
    return matches


# TODO 2
def format_runbook_entry(entry):
    return (
        f"Issue #{entry['id']}: {entry['exception']}\n"
        f"  Root cause: {entry['root_cause']}\n"
        f"  Fix: {entry['fix']}"
    )


# TODO 3
def diagnose(description):
    matches = classify_symptom(description)
    if not matches:
        return (
            "No matching catalog entry for this symptom yet -- "
            "check the lesson's catalog for the closest pattern."
        )
    return "\n\n".join(format_runbook_entry(entry) for entry in matches)


def run():
    sample_symptoms = [
        "Service crashes on startup with a KeyError for a missing config key",
        "Function looks like it works but silently returns the wrong value -- no error, just a bare except somewhere",
        "API call returns 503 but our code tries json.loads on it anyway and gets 'Expecting value'",
        "Report generator gets slower as the dataset grows -- looks quadratic",
        "Everything is fine, no crash at all",
    ]
    for symptom in sample_symptoms:
        print(f"SYMPTOM: {symptom}")
        print(diagnose(symptom))
        print()


if __name__ == "__main__":
    run()
