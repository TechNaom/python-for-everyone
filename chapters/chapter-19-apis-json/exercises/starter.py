"""
Chapter 19 Exercises: Working with APIs & JSON
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every "response" in these exercises is a hardcoded JSON string standing in
for what a real API would send back -- no network access is needed or used
anywhere in this file.
"""

import json

# TODO 1: Given mock_response_text below (a JSON string, exactly like
# response.text on a real Response object), use json.loads() to parse it
# into a dict named `weather`. Print weather["city"] and
# weather["temp_f"].
mock_response_text = '{"city": "Denver", "temp_f": 72, "condition": "Clear"}'


# TODO 2: Build a dict named `profile` with keys "username" (value "cleo")
# and "followers" (value 1204). Use json.dumps() with indent=2 to convert
# it to a pretty-printed JSON string named `pretty`, and print `pretty`.


# TODO 3: Parse mock_nested_text below with json.loads() into a variable
# named `data`. Print data["repo"], then loop over data["contributors"]
# (a list of dicts), printing f"{person['name']}: {person['commits']}"
# for each one.
mock_nested_text = """
{
  "repo": "sample-project",
  "contributors": [
    {"name": "Ada", "commits": 58},
    {"name": "Grace", "commits": 122}
  ]
}
"""


# TODO 4: Given status_code = 404, write an if/else that prints
# "Success!" if status_code == 200, otherwise prints
# f"Request failed with status {status_code}".
status_code = 404


# TODO 5: Given the dict quote_data below, use .get() to read the "author"
# key with a default of "Unknown" into a variable named `author`, and
# print f'"{quote_data["text"]}" -- {author}'. (quote_data has no
# "author" key on purpose -- the .get() default should be used.)
quote_data = {"text": "Simplicity is the ultimate sophistication."}


# TODO 6: Build a query string from the params dict below, in the form
# "key1=value1&key2=value2", then print
# f"https://api.example.com/search?{query_string}". Use
# "&".join(f"{k}={v}" for k, v in params.items()) to build the query
# string.
params = {"q": "python jobs", "page": 1}


# TODO 7 (Debug the Code): this is supposed to parse mock_text and print
# the "city" key, but it forgot to actually call json.loads() first, so
# it's trying to index into a plain string instead of a dict, which
# raises a TypeError. Find and fix it.
mock_text = '{"city": "Seattle", "temp_f": 61}'
data = mock_text
print(data["city"])


# TODO 8 (Debug the Code): this is supposed to safely handle a response
# that might be missing the "condition" key, using .get() with a default
# of "unknown" -- but it used square-bracket indexing instead, which
# raises a KeyError since "condition" genuinely isn't present. Find and
# fix it.
weather_data = {"city": "Miami", "temp_f": 90}
condition = weather_data["condition"]
print(f"Condition: {condition}")
