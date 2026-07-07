"""
Chapter 19 Project: Weather & Quote-of-the-Day Fetcher -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: json and a
fetch -> parse -> format pipeline. Every "API call" here uses a mocked
JSON response embedded directly in this script -- no network access is
needed or used anywhere in this file, so it runs the same way for every
learner, every time.
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


def fetch_weather(city, simulate_error=False):
    """Stands in for a real requests.get(weather_url, params={"city": city}).text
    call. Returns a mocked "bad response" if simulate_error is True, so the
    error-handling path can be exercised without a real failing API."""
    if simulate_error:
        return MOCK_WEATHER_RESPONSE_BAD
    return MOCK_WEATHER_RESPONSE


def parse_weather(raw_text):
    """Parse the raw JSON text and pull out just the fields needed,
    returning None if the mocked response reports an error status."""
    data = json.loads(raw_text)
    if data.get("status") != "ok":
        return None
    return {
        "city": data["city"],
        "temp_f": data["current"]["temp_f"],
        "condition": data["current"]["condition"],
        "humidity": data["current"].get("humidity", "unknown"),
        "forecast": data.get("forecast", []),
    }


def format_weather(weather):
    """Turn the parsed weather dict into a readable, multi-line string."""
    if weather is None:
        return "Could not retrieve weather data."
    lines = [
        f"{weather['city']}: {weather['temp_f']}F, {weather['condition']} "
        f"(humidity {weather['humidity']}%)"
    ]
    for day in weather["forecast"]:
        lines.append(f"  {day['day']}: {day['high_f']}F, {day['condition']}")
    return "\n".join(lines)


def fetch_quote(index):
    """Stands in for a real requests.get(quote_url).text call. Returns an
    error-shaped mocked response for an out-of-range index."""
    if 0 <= index < len(MOCK_QUOTE_RESPONSES):
        return MOCK_QUOTE_RESPONSES[index]
    return json.dumps({"status": "error", "message": "No quote at that index"})


def parse_quote(raw_text):
    """Parse the raw JSON text, returning None if the response reports an
    error status."""
    data = json.loads(raw_text)
    if data.get("status") != "ok":
        return None
    return data["quote"]


def format_quote(quote):
    """Turn the parsed quote dict into a readable, printable string."""
    if quote is None:
        return "No quote available."
    return f'"{quote["text"]}"\n    -- {quote["author"]}'


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
        city = input("City name: ").strip()
        raw_text = fetch_weather(city)
        weather = parse_weather(raw_text)
        print(format_weather(weather))

    elif choice == "2":
        print()
        city = input("City name (this demo call will simulate an error): ").strip()
        raw_text = fetch_weather(city, simulate_error=True)
        weather = parse_weather(raw_text)
        print(format_weather(weather))

    elif choice == "3":
        print()
        raw_index = input("Quote index (0, 1, or 2): ").strip()
        try:
            index = int(raw_index)
        except ValueError:
            print(f"'{raw_index}' is not a valid index.")
            continue
        raw_text = fetch_quote(index)
        quote = parse_quote(raw_text)
        if quote is not None:
            quote_history.append(quote)
        print(format_quote(quote))

    elif choice == "4":
        print()
        if not quote_history:
            print("No quotes fetched yet -- choose option 3 first.")
        else:
            for i, q in enumerate(quote_history, 1):
                print(f'{i}. "{q["text"]}" -- {q["author"]}')

    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
