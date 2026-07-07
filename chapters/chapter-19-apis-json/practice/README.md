# Chapter 19 Practice Bank: Working with APIs & JSON

A deeper set of practice problems, organized by topic, on top of the main
`exercises/` folder — including scenario-based problems written in the
same style you'll see in real interviews. This is the chapter where APIs,
JSON, `requests` concepts, and the `json` module become allowed, on top
of everything from Chapters 1-18 (including regex, generators, iterators,
context managers, all OOP, exceptions, and file/CSV handling). Every
"response" here is a hardcoded JSON string standing in for what a real
API would send back — no network access is needed or used anywhere in
this folder. No import beyond
`json`/`os`/`re`/`math`/`datetime`/`random`/`csv`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: What an API Is, and Why JSON

1. Parse a JSON string with `json.loads()` and inspect its type.
2. Build a Python dict and convert it to a JSON string with `json.dumps()`.
3. Confirm JSON's `true`/`null` become Python's `True`/`None` after parsing.
4. **Debug the Code:** fix code that printed unparsed JSON text instead of parsing it first.
5. **Scenario — Explaining Why an App Needs an API Instead of Hardcoded Data:** write `explain_why_use_an_api()`.
6. **Scenario — Interview Prep:** explain why JSON became the standard API data format.

## Topic 2: The `requests` Library Basics

1. Check a status code with a simple if/else.
2. Parse a mocked `response.text` string into usable data.
3. Classify a status code into success/client error/server error/other.
4. **Debug the Code:** fix a status-code comparison against the wrong type (string vs. int).
5. **Scenario — Explaining `requests.get()` to a Teammate:** write `explain_requests_get()`.
6. **Scenario — Interview Prep:** explain the difference between `response.text` and `response.json()`.

## Topic 3: The `json` Module: `loads()` & `dumps()`

1. Pretty-print nested data with `indent=2`.
2. Parse compact JSON text and sum its values.
3. Confirm a dumps/loads round trip recovers the original data.
4. **Debug the Code:** fix `indent="2"` (a string) instead of `indent=2` (an integer).
5. **Scenario — Saving an API Response to a Readable Log File:** write `format_for_log(data)`.
6. **Scenario — Interview Prep:** explain when `indent=` helps and when it doesn't.

## Topic 4: Navigating Nested JSON

1. Read a value from a one-level-nested dict.
2. Read a value from a list nested inside a dict.
3. Loop over a nested list of dicts.
4. Chain lookups three levels deep.
5. **Debug the Code:** fix a lookup that skipped a required list-index step.
6. **Scenario — Summing Every Line Item on an Invoice API Response:** write `invoice_total(invoice)`.
7. **Scenario — Interview Prep:** explain how to approach navigating an unfamiliar nested response.

## Topic 5: Handling Errors: Bad Responses & Missing Keys

1. Return `None` for a non-200 status code.
2. Use `.get()` with a default for a possibly-missing key.
3. Classify a failing status code.
4. Catch a custom `NetworkError` exception.
5. **Debug the Code:** fix a missing `.get()` default causing a `TypeError` in later arithmetic.
6. **Scenario — Building a Resilient Weather Summary:** write `summarize_weather(data)`.
7. **Scenario — Interview Prep:** explain the two genuinely different request failure modes.

## Topic 6: Query Parameters & Headers

1. Build a query string from a `params`-style dict.
2. Build an `Authorization` header dict.
3. Read a missing environment variable with a fallback.
4. Build a query string with a boolean value.
5. **Debug the Code:** fix a hardcoded API key that should be read from an environment variable.
6. **Scenario — Building a Search Request URL:** write `build_search_url(query, limit)`.
7. **Scenario — Interview Prep:** explain why an API key should never be hardcoded.

## Topic 7: Building a Pipeline: API &rarr; Data &rarr; Output

1. Write a `fetch_*()` function returning mocked raw JSON text.
2. Write a `parse_*()` function turning that text into usable values.
3. Write a `format_*()` function turning those values into readable output.
4. Combine all three into one pipeline call.
5. **Debug the Code:** fix a pipeline that parsed data before fetching it.
6. **Scenario — A Currency Converter Pipeline:** write `fetch_rate_data()`/`parse_rate()`/`format_conversion()`.
7. **Scenario — Interview Prep:** explain why the fetch/parse/format split matters for testability.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
