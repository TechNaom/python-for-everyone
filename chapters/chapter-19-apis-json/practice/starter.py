"""
Chapter 19 Practice Bank: Working with APIs & JSON
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Every "response" in this practice bank is a hardcoded JSON string standing
in for what a real API would send back -- no network access is needed or
used anywhere in this file.
"""

import json
import os

# ============================================================
# Topic 1: What an API is, and why JSON
# ============================================================

# TODO 1.1: Given json_text = '{"a": 1, "b": 2}', use json.loads() to
# parse it into a variable named `data`, then print type(data) and data.


# TODO 1.2: Build a Python dict named `person` with keys "name" ("Nadia")
# and "age" (28). Use json.dumps() to convert it to a string named
# `as_json`, and print type(as_json) and as_json.


# TODO 1.3: Given raw = '{"active": true, "score": null}', use
# json.loads() to parse it into `data`, then print data["active"] and
# type(data["active"]), followed by data["score"] and type(data["score"])
# (confirming JSON's true/null became Python's True/None).


# TODO 1.4 (Debug the Code): this is supposed to print the parsed value of
# raw_text, but it prints raw_text itself without ever calling
# json.loads() on it, so it prints the literal, unparsed string instead of
# a dict. Fix it.
raw_text = '{"city": "Boston"}'
print(raw_text)


# TODO 1.A (Scenario -- Explaining Why an App Needs an API Instead of
# Hardcoded Data): a teammate asks why a currency-converter app can't just
# hardcode "1 USD = 0.92 EUR" instead of calling an API every time. Write
# a function explain_why_use_an_api() that returns a string explaining
# that exchange rates change constantly, so a hardcoded value would
# quickly become wrong -- calling an API each time means the app always
# uses whatever rate is current at that moment, without needing its own
# code updated every time the real-world rate changes. Call it and print
# the result.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks why JSON
# specifically became the standard format for web APIs, instead of some
# other text format. Write a function explain_why_json() that returns a
# string explaining that JSON maps almost directly onto data structures
# that already exist in nearly every programming language (objects/dicts,
# arrays/lists), so nearly every language can parse and produce it with
# just a couple of built-in function calls, without needing a custom
# parser written for each new format that comes along. Call it and print
# the result.


# ============================================================
# Topic 2: The requests library basics
# ============================================================

# TODO 2.1: Given status_code = 200, write an if/else that prints
# "Request succeeded." if status_code == 200, otherwise prints
# f"Request failed with status code {status_code}."


# TODO 2.2: Given mock_text = '{"joke": "Why do programmers prefer dark
# mode? Because light attracts bugs."}', this stands in for
# response.text. Print type(mock_text), then use json.loads() to parse it
# into `data` and print data["joke"].


# TODO 2.3: Write a function classify_status(code) that returns "success"
# if 200 <= code < 300, "client error" if 400 <= code < 500, "server
# error" if 500 <= code < 600, and "other" otherwise. Loop over
# [200, 404, 500, 301] and print f"{code}: {classify_status(code)}" for
# each.


# TODO 2.4 (Debug the Code): this is supposed to check whether a request
# succeeded, but it compares status_code to the string "200" instead of
# the integer 200, so the comparison is always False even for a real
# success. Fix it.
status_code = 200
if status_code == "200":
    print("Success")
else:
    print("Failure")


# TODO 2.A (Scenario -- Explaining requests.get() to a Teammate): a
# teammate new to Python asks what requests.get(url) actually returns.
# Write a function explain_requests_get() that returns a string
# explaining that it sends a request to url and returns a Response
# object, which has a .status_code (a number reporting success or
# failure), a .text (the raw response body as a plain string), and a
# .json() method that parses that body into Python data automatically,
# assuming the body is actually JSON. Call it and print the result.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks what the
# difference is between response.text and response.json(). Write a
# function explain_text_vs_json() that returns a string explaining that
# .text always returns the raw response body as a plain string, no
# matter what format it's actually in, while .json() reads that same body
# and immediately parses it as JSON, handing back a ready-to-use Python
# dict or list -- .json() only works correctly if the body is genuinely
# valid JSON, while .text always works regardless of format. Call it and
# print the result.


# ============================================================
# Topic 3: The json module: loads() & dumps()
# ============================================================

# TODO 3.1: Given nested = {"user": {"name": "Priya"}, "tags": ["a", "b"]},
# use json.dumps() with indent=2 to build a variable named `pretty`, and
# print it.


# TODO 3.2: Given compact_text = '{"x":1,"y":2,"z":3}', use json.loads()
# to parse it into `data`, then print sum(data.values()).


# TODO 3.3: Build a list of dicts named `items`:
# [{"name": "pen", "price": 1.5}, {"name": "book", "price": 12.0}]. Use
# json.dumps() to convert it into a string named `as_json`, then use
# json.loads() on that same string to convert it back into a variable
# named `round_trip`. Print items == round_trip (should be True, since
# converting to JSON and back recovers the same data).


# TODO 3.4: Given raw = '{"title": "Chapter 19", "pages": 42}', parse it
# with json.loads() into `data`. Print f"{data['title']} has {data['pages']}
# pages."


# TODO 3.5 (Debug the Code): this is supposed to pretty-print `payload`
# with 2-space indentation, but it passed the indent value as a string
# "2" instead of the integer 2, which raises a TypeError. Fix it.
payload = {"status": "ok", "code": 200}
pretty = json.dumps(payload, indent="2")
print(pretty)


# TODO 3.A (Scenario -- Saving an API Response to a Readable Log File): a
# monitoring tool wants to save every API response it receives to a log
# file in a human-readable format, for later debugging. Write a function
# format_for_log(data) that returns json.dumps(data, indent=2). Call
# format_for_log({"endpoint": "/health", "status": 200}) and print the
# result.


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks when
# json.dumps()'s indent= argument is actually useful, versus when it
# isn't. Write a function explain_indent_tradeoff() that returns a string
# explaining that indent= is purely a human-readability feature -- it
# adds no new information, only whitespace and newlines -- so it's useful
# when printing JSON to a terminal, writing it to a log file a person
# will read, or debugging what an API sent back; it's the wrong choice
# when sending JSON over a real network connection, since the extra
# whitespace adds bytes with no benefit once nothing is going to visually
# inspect it before a program parses it back. Call it and print the
# result.


# ============================================================
# Topic 4: Navigating nested JSON
# ============================================================

# TODO 4.1: Given data = {"store": {"name": "Corner Cafe", "open": True}},
# print data["store"]["name"] and data["store"]["open"].


# TODO 4.2: Given orders = {"orders": [{"id": 1, "total": 9.5},
# {"id": 2, "total": 22.0}]}, print orders["orders"][1]["total"].


# TODO 4.3: Given the same `orders` dict from 4.2, loop over
# orders["orders"] and print f"Order {o['id']}: ${o['total']}" for each
# one.


# TODO 4.4: Given deeply_nested = {"a": {"b": {"c": [1, 2, 3]}}}, print
# deeply_nested["a"]["b"]["c"][2].


# TODO 4.5 (Debug the Code): this is supposed to print the second
# contributor's name from repo_data, but it only indexes one level deep
# ["contributors"] without also indexing into the list with [1] before
# grabbing ["name"], so it raises a TypeError (a list has no key
# "name"). Fix it.
repo_data = {"contributors": [{"name": "Ada"}, {"name": "Grace"}]}
print(repo_data["contributors"]["name"])


# TODO 4.A (Scenario -- Summing Every Line Item on an Invoice API
# Response): a billing system needs the total of every line item in an
# invoice API response. Write a function invoice_total(invoice) that
# returns sum(item["amount"] for item in invoice["line_items"]). Call it
# on
# invoice = {"invoice_id": "INV-100", "line_items": [{"desc": "Widget", "amount": 10.0}, {"desc": "Gadget", "amount": 25.5}]}
# and print the result.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks how to
# approach navigating an unfamiliar, deeply nested JSON response for the
# first time. Write a function explain_nested_navigation_approach() that
# returns a string explaining that the fastest approach is to
# pretty-print a sample of the actual response with
# json.dumps(data, indent=2) and read the shape from the outside in --
# is the top level a dict or a list, what's inside each key -- then chain
# ordinary [key]/[index] lookups one level at a time to reach a specific
# value, reserving a loop for the moment a list of several similar
# records appears anywhere in the structure. Call it and print the
# result.


# ============================================================
# Topic 5: Handling errors: bad responses & missing keys
# ============================================================

# TODO 5.1: Write a function safe_get_response(status_code, mock_body)
# that returns mock_body if status_code == 200, otherwise returns None.
# Call it with (200, {"ok": True}) and with (500, None), printing both
# results.


# TODO 5.2: Given data = {"city": "Reno"}, use .get() to read "state" with
# a default of "N/A" into a variable named `state`, and print state.


# TODO 5.3: Write a function classify_failure(status_code) that returns
# "client error" if 400 <= status_code < 500, "server error" if
# 500 <= status_code < 600, and "unknown failure" otherwise. Loop over
# [401, 503, 999] and print f"{code}: {classify_failure(code)}" for each.


# TODO 5.4: Given a custom exception class NetworkError(Exception) (write
# it), write a function simulated_fetch(should_fail) that raises
# NetworkError("timed out") if should_fail is True, otherwise returns
# "ok". Wrap a call to simulated_fetch(True) in a try/except NetworkError
# and print f"Caught: {e}" in the except block.


# TODO 5.5 (Debug the Code): this is supposed to safely read the
# "discount" key with a default of 0 if it's missing, but it used .get()
# with only one argument (no default), so a missing key returns None
# instead of 0, and the later arithmetic (price * discount) then fails
# with a TypeError. Fix it by adding the default argument.
cart_item = {"price": 20.0}
discount = cart_item.get("discount")
print(cart_item["price"] * discount)


# TODO 5.A (Scenario -- Building a Resilient Weather Summary): a weather
# dashboard needs to display a summary even if some optional fields
# (like "humidity" or "wind_mph") are missing from a given response, while
# "city" and "temp_f" are always guaranteed present by the API's
# documentation. Write a function summarize_weather(data) that returns
# f"{data['city']}: {data['temp_f']}F, humidity {data.get('humidity', 'unknown')}".
# Call it on {"city": "Tampa", "temp_f": 91} (no "humidity" key) and print
# the result.


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks what the two
# genuinely different ways a real API request can fail are. Write a
# function explain_two_failure_modes() that returns a string explaining
# that a request can fail at the network level (no connection, a
# timeout, a broken URL -- caught with
# try/except requests.exceptions.RequestException, before any status
# code even exists), or it can complete successfully at the network level
# but come back with a bad status code (checked with
# response.status_code, or the response.raise_for_status() shortcut) --
# these are different failure modes, and defensive code has to check for
# both rather than assuming one check covers everything. Call it and
# print the result.


# ============================================================
# Topic 6: Query parameters & headers
# ============================================================

# TODO 6.1: Given base_url = "https://api.example.com/books" and
# params = {"author": "Orwell", "year": 1949}, build query_string using
# "&".join(f"{k}={v}" for k, v in params.items()), then print
# f"{base_url}?{query_string}".


# TODO 6.2: Write a function build_auth_header(api_key) that returns
# {"Authorization": f"Bearer {api_key}"}. Call it with "abc123" and print
# the result.


# TODO 6.3: Use os.environ.get("SOME_UNSET_VAR", "fallback-value") to read
# an environment variable that doesn't exist, storing the result in a
# variable named `value`, and print value (should print the fallback,
# since the variable was never set).


# TODO 6.4: Given params = {"category": "fiction", "in_stock": True},
# build and print the query string the same way as TODO 6.1.


# TODO 6.5 (Debug the Code): this is supposed to build an Authorization
# header using an API key read from an environment variable, but it
# hardcodes the key directly as a string literal instead of reading it
# from os.environ -- exactly the "never hardcode a real key" mistake this
# chapter warns against. Fix it to read from
# os.environ.get("DEMO_API_KEY", "no-key-set") instead.
api_key = "sk-real-secret-key-12345"
headers = {"Authorization": f"Bearer {api_key}"}
print(headers)


# TODO 6.A (Scenario -- Building a Search Request URL): a search feature
# needs to build the correct URL for a search API given a search term and
# a result limit. Write a function build_search_url(query, limit) that
# returns f"https://api.example.com/search?q={query}&limit={limit}". Call
# it with ("python jobs", 10) and print the result.


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks why an API
# key should never be hardcoded directly in a script. Write a function
# explain_api_key_safety() that returns a string explaining that a
# hardcoded key becomes part of the file's contents, and if that file is
# ever committed to a public repository (even briefly, even if deleted in
# a later commit), the key is visible in that commit's history forever --
# automated bots specifically scan public repos for exposed keys within
# minutes of a push. Reading the key from an environment variable at
# runtime with os.environ.get() keeps it out of the source code entirely,
# so it's never at risk from a commit. Call it and print the result.


# ============================================================
# Topic 7: Building a pipeline: API -> data -> output
# ============================================================

# TODO 7.1: Write a function fetch_mock_joke() that returns the string
# '{"setup": "Why do Python programmers wear glasses?", "punchline": "Because they cannot C."}'.
# Call it and print the result (still a raw string at this point).


# TODO 7.2: Write a function parse_joke(raw_text) that uses json.loads()
# and returns a tuple (data["setup"], data["punchline"]). Call it on the
# result of fetch_mock_joke() from 7.1, unpacking into `setup` and
# `punchline`, then print both.


# TODO 7.3: Write a function format_joke(setup, punchline) that returns
# f"{setup}\n... {punchline}". Call it with the setup/punchline from 7.2
# and print the result.


# TODO 7.4: Combine 7.1-7.3 into one pipeline: call fetch_mock_joke(),
# pass the result to parse_joke(), unpack into setup/punchline, pass both
# to format_joke(), and print the final formatted string.


# TODO 7.5 (Debug the Code): this pipeline is supposed to fetch, parse,
# and format a mocked quote, but the parse step was called on the wrong
# variable -- it parses raw_text before fetch_data() is ever called,
# using a variable that doesn't exist yet, which raises a NameError. Fix
# the order so fetch_data() runs first and its result is what gets
# parsed.
def fetch_data():
    return '{"quote": "Simple is better than complex."}'


def parse_data(text):
    return json.loads(text)["quote"]


parsed = parse_data(raw_text)
raw_text = fetch_data()
print(parsed)


# TODO 7.A (Scenario -- A Currency Converter Pipeline): a currency
# converter needs to turn a mocked exchange-rate API response into a
# formatted conversion result. Write three functions: fetch_rate_data(),
# returning '{"base": "USD", "target": "EUR", "rate": 0.92}';
# parse_rate(raw_text), returning a tuple (data["base"], data["target"],
# data["rate"]) using json.loads(); and format_conversion(base, target,
# rate, amount), returning
# f"{amount} {base} = {round(amount * rate, 2)} {target}". Call all three
# together for amount = 100 and print the final formatted string.


# TODO 7.B (Scenario -- Interview Prep): an interviewer asks why splitting
# a program into separate fetch/parse/format functions matters, beyond
# just organizing the code. Write a function
# explain_pipeline_testability() that returns a string explaining that
# the real benefit is testability without a network connection -- a parse
# function can be tested directly against any number of hand-written mock
# JSON strings (covering success, a bad status, a missing key) without
# ever calling the real fetch function or touching a live server, and a
# format function can be tested with plain Python values with no
# dependency on JSON or networking at all; only the fetch function itself
# would ever need a real network call, and it's the smallest, simplest
# piece of the whole pipeline. Call it and print the result.
