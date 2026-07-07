"""
Chapter 19 Exercises: Working with APIs & JSON -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

import json

# TODO 1
mock_response_text = '{"city": "Denver", "temp_f": 72, "condition": "Clear"}'
weather = json.loads(mock_response_text)
print(weather["city"])
print(weather["temp_f"])


# TODO 2
profile = {"username": "cleo", "followers": 1204}
pretty = json.dumps(profile, indent=2)
print(pretty)


# TODO 3
mock_nested_text = """
{
  "repo": "sample-project",
  "contributors": [
    {"name": "Ada", "commits": 58},
    {"name": "Grace", "commits": 122}
  ]
}
"""
data = json.loads(mock_nested_text)
print(data["repo"])
for person in data["contributors"]:
    print(f"{person['name']}: {person['commits']}")


# TODO 4
status_code = 404
if status_code == 200:
    print("Success!")
else:
    print(f"Request failed with status {status_code}")


# TODO 5
quote_data = {"text": "Simplicity is the ultimate sophistication."}
author = quote_data.get("author", "Unknown")
print(f'"{quote_data["text"]}" -- {author}')


# TODO 6
params = {"q": "python jobs", "page": 1}
query_string = "&".join(f"{k}={v}" for k, v in params.items())
print(f"https://api.example.com/search?{query_string}")


# TODO 7 (Debug the Code)
# Bug: mock_text was assigned directly to `data` without ever calling
# json.loads() on it, so `data` was still a plain string -- indexing it
# with ["city"] raised a TypeError. Fix: parse it first.
mock_text = '{"city": "Seattle", "temp_f": 61}'
data = json.loads(mock_text)
print(data["city"])


# TODO 8 (Debug the Code)
# Bug: weather_data["condition"] uses square-bracket indexing on a key
# that genuinely isn't present, raising a KeyError. Fix: use .get() with
# a default so a missing key doesn't crash the program.
weather_data = {"city": "Miami", "temp_f": 90}
condition = weather_data.get("condition", "unknown")
print(f"Condition: {condition}")
