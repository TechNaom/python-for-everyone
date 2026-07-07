# Chapter 19 Exercises: Working with APIs & JSON

These exercises use what Chapter 19 covered: what an API is and why JSON
is the shared data format, `requests`/status codes conceptually,
`json.loads()`/`json.dumps()` (including `indent=`), navigating nested
JSON, `dict.get()` for missing keys, and building a query string from a
`params`-style dict. Every "response" here is a hardcoded JSON string
standing in for what a real API would send back -- no network access is
needed or used anywhere in this folder.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — `json.loads()` on a mocked response

Find `# TODO 1`. Parse `mock_response_text` (a JSON string standing in for
`response.text`) with `json.loads()` into a dict named `weather`. Print
`weather["city"]` and `weather["temp_f"]`.

## Task 2 — `json.dumps()` with `indent=`

Find `# TODO 2`. Build a dict named `profile` with keys `"username"`
(`"cleo"`) and `"followers"` (`1204`). Convert it to a pretty-printed JSON
string named `pretty` using `json.dumps(profile, indent=2)`, and print it.

## Task 3 — Navigating nested JSON

Find `# TODO 3`. Parse `mock_nested_text` into `data`. Print
`data["repo"]`, then loop over `data["contributors"]` (a list of dicts),
printing each contributor's name and commit count.

## Task 4 — Checking a status code

Find `# TODO 4`. Given `status_code = 404`, print `"Success!"` if it's
`200`, otherwise print a message including the actual status code.

## Task 5 — `.get()` with a default

Find `# TODO 5`. Read `quote_data`'s `"author"` key with `.get()` and a
default of `"Unknown"` (the dict deliberately has no `"author"` key), then
print the quote with its author.

## Task 6 — Building a query string

Find `# TODO 6`. Build a query string from the `params` dict in the form
`"key1=value1&key2=value2"`, and print the full URL it would produce.

## Task 7 — Debug the Code

Find `# TODO 7`. This is supposed to parse `mock_text` and print its
`"city"` key, but it forgot to actually call `json.loads()` first, so
it's indexing into a plain string instead of a dict, which raises a
`TypeError`. Find and fix it.

## Task 8 — Debug the Code

Find `# TODO 8`. This is supposed to safely handle a response that's
missing the `"condition"` key using `.get()` with a default, but it used
square-bracket indexing instead, which raises a `KeyError` since
`"condition"` genuinely isn't present. Find and fix it.

## Checking your work

Compare your output against `solution.py`. Every example here uses fixed,
explicit values, so your output should match `solution.py` exactly.
