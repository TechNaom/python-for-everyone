"""
ops.fetch -- the mocked fetch engine, ported from Chapter 19's Weather &
Quote-of-the-Day Fetcher (fetch_weather/parse_weather/format_weather,
fetch_quote/parse_quote/format_quote).

Deliberately kept separate from cli.py: no argparse, no print(). Every
"API call" here uses a mocked JSON response embedded directly in this
module -- no network access is used anywhere, exactly like the original
project. The only change from the original is that a "bad" response
(status != "ok") now raises OpsError instead of the parse_* functions
returning None -- that keeps this module on the same "raise, don't
return None/error strings" convention as ops.logs and ops.scan.
"""

from __future__ import annotations

import json
import logging

from ops import OpsError
from ops.formatting import format_kv, format_list

logger = logging.getLogger(__name__)

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


def fetch_weather(city: str, simulate_error: bool = False) -> str:
    """Stands in for a real requests.get(weather_url, params={"city": city}).text
    call. Returns a mocked "bad response" if simulate_error is True, so the
    error-handling path can be exercised without a real failing API."""
    logger.debug("Fetching mocked weather for city=%r simulate_error=%s", city, simulate_error)
    if simulate_error:
        return MOCK_WEATHER_RESPONSE_BAD
    return MOCK_WEATHER_RESPONSE


def parse_weather(raw_text: str) -> dict:
    """Parse the raw JSON text and pull out just the fields needed.

    Raises OpsError if the mocked response reports an error status
    (rather than returning None, so cli.py has one place to catch it).
    """
    data = json.loads(raw_text)
    if data.get("status") != "ok":
        message = data.get("message", "Unknown error fetching weather.")
        raise OpsError(f"Could not retrieve weather data: {message}")
    return {
        "city": data["city"],
        "temp_f": data["current"]["temp_f"],
        "condition": data["current"]["condition"],
        "humidity": data["current"].get("humidity", "unknown"),
        "forecast": data.get("forecast", []),
    }


def format_weather(weather: dict) -> str:
    """Turn the parsed weather dict into a readable, multi-line string.

    Routes through ops.formatting's shared helpers (format_kv for the
    current-conditions fields, format_list for the forecast days) so
    fetch's output follows the same convention as logs.format_table and
    scan.format_kv, instead of hand-rolling its own string building.
    """
    current = format_kv(
        [
            ("City", weather["city"]),
            ("Temp", f"{weather['temp_f']}F"),
            ("Condition", weather["condition"]),
            ("Humidity", f"{weather['humidity']}%"),
        ]
    )
    forecast_items = [
        f"{day['day']}: {day['high_f']}F, {day['condition']}" for day in weather["forecast"]
    ]
    forecast = format_list(forecast_items, empty_message="(no forecast available)")
    return f"{current}\n\nForecast:\n{forecast}"


def fetch_quote(index: int) -> str:
    """Stands in for a real requests.get(quote_url).text call. Returns an
    error-shaped mocked response for an out-of-range index."""
    logger.debug("Fetching mocked quote at index=%d", index)
    if 0 <= index < len(MOCK_QUOTE_RESPONSES):
        return MOCK_QUOTE_RESPONSES[index]
    return json.dumps({"status": "error", "message": "No quote at that index"})


def parse_quote(raw_text: str) -> dict:
    """Parse the raw JSON text.

    Raises OpsError if the response reports an error status.
    """
    data = json.loads(raw_text)
    if data.get("status") != "ok":
        message = data.get("message", "Unknown error fetching quote.")
        raise OpsError(f"Could not retrieve a quote: {message}")
    return data["quote"]


def format_quote(quote: dict) -> str:
    """Turn the parsed quote dict into a readable, printable string."""
    return f'"{quote["text"]}"\n    -- {quote["author"]}'
