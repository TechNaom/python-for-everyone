"""
Chapter 19 Practice Bank: Working with APIs & JSON -- reference solution.
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py
"""

import json
import os

# ============================================================
# Topic 1: What an API is, and why JSON
# ============================================================

# TODO 1.1
json_text = '{"a": 1, "b": 2}'
data = json.loads(json_text)
print(type(data))
print(data)

# TODO 1.2
person = {"name": "Nadia", "age": 28}
as_json = json.dumps(person)
print(type(as_json))
print(as_json)

# TODO 1.3
raw = '{"active": true, "score": null}'
data = json.loads(raw)
print(data["active"], type(data["active"]))
print(data["score"], type(data["score"]))

# TODO 1.4 (Debug the Code)
# Bug: raw_text was printed directly without ever being parsed with
# json.loads(), so it printed the literal unparsed string. Fix: parse it
# first.
raw_text = '{"city": "Boston"}'
print(json.loads(raw_text))

# TODO 1.A (Scenario -- Explaining Why an App Needs an API Instead of Hardcoded Data)
def explain_why_use_an_api():
    return (
        "Exchange rates change constantly, so a hardcoded value would "
        "quickly become wrong. Calling an API each time means the app "
        "always uses whatever rate is current at that moment, without "
        "needing its own code updated every time the real-world rate "
        "changes."
    )


print(explain_why_use_an_api())

# TODO 1.B (Scenario -- Interview Prep)
def explain_why_json():
    return (
        "JSON maps almost directly onto data structures that already "
        "exist in nearly every programming language (objects/dicts, "
        "arrays/lists), so nearly every language can parse and produce "
        "it with just a couple of built-in function calls, without "
        "needing a custom parser written for each new format that comes "
        "along."
    )


print(explain_why_json())


# ============================================================
# Topic 2: The requests library basics
# ============================================================

# TODO 2.1
status_code = 200
if status_code == 200:
    print("Request succeeded.")
else:
    print(f"Request failed with status code {status_code}.")

# TODO 2.2
mock_text = '{"joke": "Why do programmers prefer dark mode? Because light attracts bugs."}'
print(type(mock_text))
data = json.loads(mock_text)
print(data["joke"])

# TODO 2.3
def classify_status(code):
    if 200 <= code < 300:
        return "success"
    elif 400 <= code < 500:
        return "client error"
    elif 500 <= code < 600:
        return "server error"
    else:
        return "other"


for code in [200, 404, 500, 301]:
    print(f"{code}: {classify_status(code)}")

# TODO 2.4 (Debug the Code)
# Bug: status_code (an int) was compared to "200" (a string), so the
# comparison is always False. Fix: compare to the integer 200.
status_code = 200
if status_code == 200:
    print("Success")
else:
    print("Failure")

# TODO 2.A (Scenario -- Explaining requests.get() to a Teammate)
def explain_requests_get():
    return (
        "requests.get(url) sends a request to url and returns a Response "
        "object, which has a .status_code (a number reporting success or "
        "failure), a .text (the raw response body as a plain string), "
        "and a .json() method that parses that body into Python data "
        "automatically, assuming the body is actually JSON."
    )


print(explain_requests_get())

# TODO 2.B (Scenario -- Interview Prep)
def explain_text_vs_json():
    return (
        ".text always returns the raw response body as a plain string, "
        "no matter what format it's actually in, while .json() reads "
        "that same body and immediately parses it as JSON, handing back "
        "a ready-to-use Python dict or list -- .json() only works "
        "correctly if the body is genuinely valid JSON, while .text "
        "always works regardless of format."
    )


print(explain_text_vs_json())


# ============================================================
# Topic 3: The json module: loads() & dumps()
# ============================================================

# TODO 3.1
nested = {"user": {"name": "Priya"}, "tags": ["a", "b"]}
pretty = json.dumps(nested, indent=2)
print(pretty)

# TODO 3.2
compact_text = '{"x":1,"y":2,"z":3}'
data = json.loads(compact_text)
print(sum(data.values()))

# TODO 3.3
items = [{"name": "pen", "price": 1.5}, {"name": "book", "price": 12.0}]
as_json = json.dumps(items)
round_trip = json.loads(as_json)
print(items == round_trip)

# TODO 3.4
raw = '{"title": "Chapter 19", "pages": 42}'
data = json.loads(raw)
print(f"{data['title']} has {data['pages']} pages.")

# TODO 3.5 (Debug the Code)
# Bug: indent="2" passed a string instead of the integer 2, raising a
# TypeError. Fix: pass the integer 2.
payload = {"status": "ok", "code": 200}
pretty = json.dumps(payload, indent=2)
print(pretty)

# TODO 3.A (Scenario -- Saving an API Response to a Readable Log File)
def format_for_log(data):
    return json.dumps(data, indent=2)


print(format_for_log({"endpoint": "/health", "status": 200}))

# TODO 3.B (Scenario -- Interview Prep)
def explain_indent_tradeoff():
    return (
        "indent= is purely a human-readability feature -- it adds no "
        "new information, only whitespace and newlines -- so it's "
        "useful when printing JSON to a terminal, writing it to a log "
        "file a person will read, or debugging what an API sent back. "
        "It's the wrong choice when sending JSON over a real network "
        "connection, since the extra whitespace adds bytes with no "
        "benefit once nothing is going to visually inspect it before a "
        "program parses it back."
    )


print(explain_indent_tradeoff())


# ============================================================
# Topic 4: Navigating nested JSON
# ============================================================

# TODO 4.1
data = {"store": {"name": "Corner Cafe", "open": True}}
print(data["store"]["name"])
print(data["store"]["open"])

# TODO 4.2
orders = {"orders": [{"id": 1, "total": 9.5}, {"id": 2, "total": 22.0}]}
print(orders["orders"][1]["total"])

# TODO 4.3
for o in orders["orders"]:
    print(f"Order {o['id']}: ${o['total']}")

# TODO 4.4
deeply_nested = {"a": {"b": {"c": [1, 2, 3]}}}
print(deeply_nested["a"]["b"]["c"][2])

# TODO 4.5 (Debug the Code)
# Bug: repo_data["contributors"] is a list, so ["name"] right after it
# raises a TypeError (a list has no string keys). Fix: index into the
# list first (e.g. [1] for the second contributor), then get "name".
repo_data = {"contributors": [{"name": "Ada"}, {"name": "Grace"}]}
print(repo_data["contributors"][1]["name"])

# TODO 4.A (Scenario -- Summing Every Line Item on an Invoice API Response)
def invoice_total(invoice):
    return sum(item["amount"] for item in invoice["line_items"])


invoice = {
    "invoice_id": "INV-100",
    "line_items": [
        {"desc": "Widget", "amount": 10.0},
        {"desc": "Gadget", "amount": 25.5},
    ],
}
print(invoice_total(invoice))

# TODO 4.B (Scenario -- Interview Prep)
def explain_nested_navigation_approach():
    return (
        "The fastest approach is to pretty-print a sample of the actual "
        "response with json.dumps(data, indent=2) and read the shape "
        "from the outside in -- is the top level a dict or a list, "
        "what's inside each key -- then chain ordinary [key]/[index] "
        "lookups one level at a time to reach a specific value, "
        "reserving a loop for the moment a list of several similar "
        "records appears anywhere in the structure."
    )


print(explain_nested_navigation_approach())


# ============================================================
# Topic 5: Handling errors: bad responses & missing keys
# ============================================================

# TODO 5.1
def safe_get_response(status_code, mock_body):
    return mock_body if status_code == 200 else None


print(safe_get_response(200, {"ok": True}))
print(safe_get_response(500, None))

# TODO 5.2
data = {"city": "Reno"}
state = data.get("state", "N/A")
print(state)

# TODO 5.3
def classify_failure(status_code):
    if 400 <= status_code < 500:
        return "client error"
    elif 500 <= status_code < 600:
        return "server error"
    else:
        return "unknown failure"


for code in [401, 503, 999]:
    print(f"{code}: {classify_failure(code)}")

# TODO 5.4
class NetworkError(Exception):
    pass


def simulated_fetch(should_fail):
    if should_fail:
        raise NetworkError("timed out")
    return "ok"


try:
    simulated_fetch(True)
except NetworkError as e:
    print(f"Caught: {e}")

# TODO 5.5 (Debug the Code)
# Bug: .get("discount") with no default returns None for a missing key,
# and price * None then raises a TypeError. Fix: add a default of 0.
cart_item = {"price": 20.0}
discount = cart_item.get("discount", 0)
print(cart_item["price"] * discount)

# TODO 5.A (Scenario -- Building a Resilient Weather Summary)
def summarize_weather(data):
    return f"{data['city']}: {data['temp_f']}F, humidity {data.get('humidity', 'unknown')}"


print(summarize_weather({"city": "Tampa", "temp_f": 91}))

# TODO 5.B (Scenario -- Interview Prep)
def explain_two_failure_modes():
    return (
        "A request can fail at the network level (no connection, a "
        "timeout, a broken URL -- caught with try/except "
        "requests.exceptions.RequestException, before any status code "
        "even exists), or it can complete successfully at the network "
        "level but come back with a bad status code (checked with "
        "response.status_code, or the response.raise_for_status() "
        "shortcut). These are different failure modes, and defensive "
        "code has to check for both rather than assuming one check "
        "covers everything."
    )


print(explain_two_failure_modes())


# ============================================================
# Topic 6: Query parameters & headers
# ============================================================

# TODO 6.1
base_url = "https://api.example.com/books"
params = {"author": "Orwell", "year": 1949}
query_string = "&".join(f"{k}={v}" for k, v in params.items())
print(f"{base_url}?{query_string}")

# TODO 6.2
def build_auth_header(api_key):
    return {"Authorization": f"Bearer {api_key}"}


print(build_auth_header("abc123"))

# TODO 6.3
value = os.environ.get("SOME_UNSET_VAR", "fallback-value")
print(value)

# TODO 6.4
params = {"category": "fiction", "in_stock": True}
query_string = "&".join(f"{k}={v}" for k, v in params.items())
print(query_string)

# TODO 6.5 (Debug the Code)
# Bug: the API key was hardcoded directly as a string literal, exactly
# the "never hardcode a real key" mistake this chapter warns against.
# Fix: read it from an environment variable instead.
api_key = os.environ.get("DEMO_API_KEY", "no-key-set")
headers = {"Authorization": f"Bearer {api_key}"}
print(headers)

# TODO 6.A (Scenario -- Building a Search Request URL)
def build_search_url(query, limit):
    return f"https://api.example.com/search?q={query}&limit={limit}"


print(build_search_url("python jobs", 10))

# TODO 6.B (Scenario -- Interview Prep)
def explain_api_key_safety():
    return (
        "A hardcoded key becomes part of the file's contents, and if "
        "that file is ever committed to a public repository (even "
        "briefly, even if deleted in a later commit), the key is "
        "visible in that commit's history forever -- automated bots "
        "specifically scan public repos for exposed keys within minutes "
        "of a push. Reading the key from an environment variable at "
        "runtime with os.environ.get() keeps it out of the source code "
        "entirely, so it's never at risk from a commit."
    )


print(explain_api_key_safety())


# ============================================================
# Topic 7: Building a pipeline: API -> data -> output
# ============================================================

# TODO 7.1
def fetch_mock_joke():
    return '{"setup": "Why do Python programmers wear glasses?", "punchline": "Because they cannot C."}'


print(fetch_mock_joke())

# TODO 7.2
def parse_joke(raw_text):
    data = json.loads(raw_text)
    return data["setup"], data["punchline"]


setup, punchline = parse_joke(fetch_mock_joke())
print(setup)
print(punchline)

# TODO 7.3
def format_joke(setup, punchline):
    return f"{setup}\n... {punchline}"


print(format_joke(setup, punchline))

# TODO 7.4
raw = fetch_mock_joke()
setup, punchline = parse_joke(raw)
print(format_joke(setup, punchline))

# TODO 7.5 (Debug the Code)
# Bug: parse_data(raw_text) was called before raw_text was ever assigned
# from fetch_data(), raising a NameError. Fix: call fetch_data() first,
# then parse its result.
def fetch_data():
    return '{"quote": "Simple is better than complex."}'


def parse_data(text):
    return json.loads(text)["quote"]


raw_text = fetch_data()
parsed = parse_data(raw_text)
print(parsed)

# TODO 7.A (Scenario -- A Currency Converter Pipeline)
def fetch_rate_data():
    return '{"base": "USD", "target": "EUR", "rate": 0.92}'


def parse_rate(raw_text):
    data = json.loads(raw_text)
    return data["base"], data["target"], data["rate"]


def format_conversion(base, target, rate, amount):
    return f"{amount} {base} = {round(amount * rate, 2)} {target}"


base, target, rate = parse_rate(fetch_rate_data())
print(format_conversion(base, target, rate, 100))

# TODO 7.B (Scenario -- Interview Prep)
def explain_pipeline_testability():
    return (
        "The real benefit is testability without a network connection "
        "-- a parse function can be tested directly against any number "
        "of hand-written mock JSON strings (covering success, a bad "
        "status, a missing key) without ever calling the real fetch "
        "function or touching a live server, and a format function can "
        "be tested with plain Python values with no dependency on JSON "
        "or networking at all. Only the fetch function itself would "
        "ever need a real network call, and it's the smallest, simplest "
        "piece of the whole pipeline."
    )


print(explain_pipeline_testability())
