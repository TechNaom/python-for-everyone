"""
Chapter 19 Project: Weather & Quote-of-the-Day Fetcher -- starter.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: json and a
fetch -> parse -> format pipeline. Every "API call" here uses a mocked
JSON response embedded directly in this script -- no network access is
needed or used anywhere in this file, so it runs the same way for every
learner, every time.

Fill in the numbered TODOs below. Want to see one finished version first?
Run solution.py (also from inside this folder).
"""

import json

# --- Mocked "API responses", standing in for what a real weather API and
# a real quote-of-the-day API would send back as response.text ---

MOCK_WEATHER_RESPONSE = json.dumps({
    "status": "ok",
    "city": "Austin",
    "current": {"temp_f": 89, "condition": "Sunny", "humidity": 41},
    "forecast": [
        {"day": "Mon", "high_f": 91, "condition": "Sunny"},
        {"day": "Tue", "high_f": 87, "condition": "Cloudy"},
        {"day": "Wed", "high_f": 78, "condition": "Rain"},
    ],
})

MOCK_WEATHER_RESPONSE_BAD = json.dumps({
    "status": "error",
    "message": "City not found",
})

MOCK_QUOTE_RESPONSES = [
    json.dumps({"status": "ok", "quote": {"text": "Simple is better than complex.", "author": "Tim Peters"}}),
    json.dumps({"status": "ok", "quote": {"text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"}}),
    json.dumps({"status": "ok", "quote": {"text": "Simplicity is the ultimate sophistication.", "author": "Leonardo da Vinci"}}),
]


# TODO 1: Write a function fetch_weather(city, simulate_error=False). If
# simulate_error is True, return MOCK_WEATHER_RESPONSE_BAD. Otherwise,
# return MOCK_WEATHER_RESPONSE. (A real version of this function would
# call requests.get() with `city` as a query parameter -- here it's
# mocked so the project runs identically for everyone, every time.)
def fetch_weather(city, simulate_error=False):
    pass


# TODO 2: Write a function parse_weather(raw_text). Use json.loads() to
# parse raw_text into `data`. If data.get("status") != "ok", return None.
# Otherwise return a dict with keys "city" (data["city"]), "temp_f"
# (data["current"]["temp_f"]), "condition" (data["current"]["condition"]),
# "humidity" (data["current"].get("humidity", "unknown")), and "forecast"
# (data.get("forecast", [])).
def parse_weather(raw_text):
    pass


# TODO 3: Write a function format_weather(weather). If weather is None,
# return "Could not retrieve weather data.". Otherwise, build and return
# a multi-line string: a header line
# f"{weather['city']}: {weather['temp_f']}F, {weather['condition']} (humidity {weather['humidity']}%)",
# followed by one line per day in weather["forecast"], each formatted as
# f"  {day['day']}: {day['high_f']}F, {day['condition']}". Join every
# line with "\n".
def format_weather(weather):
    pass


# TODO 4: Write a function fetch_quote(index). Return
# MOCK_QUOTE_RESPONSES[index] if index is a valid index into that list,
# otherwise return json.dumps({"status": "error", "message": "No quote at that index"}).
def fetch_quote(index):
    pass


# TODO 5: Write a function parse_quote(raw_text). Use json.loads() to
# parse raw_text into `data`. If data.get("status") != "ok", return None.
# Otherwise return data["quote"] (a dict with "text" and "author" keys).
def parse_quote(raw_text):
    pass


# TODO 6: Write a function format_quote(quote). If quote is None, return
# "No quote available.". Otherwise return f'"{quote["text"]}"\n    -- {quote["author"]}'.
def format_quote(quote):
    pass


# --- Session state ---
print("=== Weather & Quote-of-the-Day Fetcher ===")
quote_history = []

while True:
    print()
    print("1. Get weather for a city")
    print("2. Get weather for a city (simulate a bad response)")
    print("3. Get quote of the day")
    print("4. Show quote history")
    print("5. Quit")
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print()
        # TODO 7: input() a prompt for a city name. Call
        # fetch_weather(city) to get `raw_text`, call parse_weather(raw_text)
        # to get `weather`, and print format_weather(weather).
        pass

    elif choice == "2":
        print()
        # TODO 8: input() a prompt for a city name (it will be ignored by
        # the mock). Call fetch_weather(city, simulate_error=True) to get
        # `raw_text`, call parse_weather(raw_text) to get `weather`, and
        # print format_weather(weather) -- this should print the
        # "Could not retrieve weather data." message, since the mocked
        # response reports an error status.
        pass

    elif choice == "3":
        print()
        # TODO 9: input() a prompt asking for an index (0, 1, or 2) into
        # MOCK_QUOTE_RESPONSES. Convert it to an int. Call
        # fetch_quote(index) to get `raw_text`, call parse_quote(raw_text)
        # to get `quote`. If quote is not None, append it to
        # quote_history. Print format_quote(quote).
        pass

    elif choice == "4":
        print()
        # TODO 10: If quote_history is empty, print a friendly message.
        # Otherwise, loop over quote_history with enumerate(quote_history, 1)
        # and print f"{i}. \"{q['text']}\" -- {q['author']}" for each one.
        pass

    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
