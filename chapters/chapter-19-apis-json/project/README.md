# Chapter 19 Project: Weather & Quote-of-the-Day Fetcher

A menu-driven mini-app built **around this chapter's core pipeline** as
its organizing principle &mdash; fetch a mocked JSON "API response,"
parse it into Python data (handling a simulated bad response gracefully),
and format the result for a person to read. Every "API call" in this
project uses a JSON string embedded directly in the script, standing in
for what a real weather API and a real quote-of-the-day API would send
back &mdash; no network access is needed or used anywhere, so it runs
identically for every learner, every time.

## What you'll build

A `fetch` → `parse` → `format` pipeline (Sub-topic 7) for two different
mocked data sources, plus a menu loop offering five real operations:

1. Get weather for a city
2. Get weather for a city (simulate a bad response)
3. Get quote of the day
4. Show quote history
5. Quit

The pipeline is built from these pieces:

- `fetch_weather(city, simulate_error=False)` / `fetch_quote(index)` —
  stand in for `requests.get(...).text`, returning a hardcoded JSON
  string. `fetch_weather()` can be told to simulate a bad response
  (`{"status": "error", ...}`) instead of a good one, exactly to exercise
  the error-handling path from Sub-topic 5 without needing a real API to
  actually fail on demand.
- `parse_weather(raw_text)` / `parse_quote(raw_text)` — use
  `json.loads()` to parse the raw text, check `data.get("status")` before
  trusting the rest of the shape, and return `None` if the mocked
  response reports an error — exactly the defensive pattern Sub-topic 5
  covers. On success, they navigate the nested response (`data["current"]["temp_f"]`,
  `data["forecast"]`, `data["quote"]`) exactly as Sub-topic 4 covers.
- `format_weather(weather)` / `format_quote(quote)` — turn the parsed
  data (or `None`, on failure) into a readable string, never needing to
  know anything about JSON or the mocked "API" at all.

Every menu option calls its three-stage pipeline in order — fetch, then
parse, then format — mirroring exactly the shape Sub-topic 7 introduces.

Example run:

```
=== Weather & Quote-of-the-Day Fetcher ===

1. Get weather for a city
2. Get weather for a city (simulate a bad response)
3. Get quote of the day
4. Show quote history
5. Quit
Choose an option (1-5): 1

City name: Austin
Austin: 89F, Sunny (humidity 41%)
  Mon: 91F, Sunny
  Tue: 87F, Cloudy
  Wed: 78F, Rain

1. Get weather for a city
2. Get weather for a city (simulate a bad response)
3. Get quote of the day
4. Show quote history
5. Quit
Choose an option (1-5): 2

City name (this demo call will simulate an error): Nowhereville
Could not retrieve weather data.

1. Get weather for a city
2. Get weather for a city (simulate a bad response)
3. Get quote of the day
4. Show quote history
5. Quit
Choose an option (1-5): 3

Quote index (0, 1, or 2): 0
"Simple is better than complex."
    -- Tim Peters

1. Get weather for a city
2. Get weather for a city (simulate a bad response)
3. Get quote of the day
4. Show quote history
5. Quit
Choose an option (1-5): 4

1. "Simple is better than complex." -- Tim Peters

1. Get weather for a city
2. Get weather for a city (simulate a bad response)
3. Get quote of the day
4. Show quote history
5. Quit
Choose an option (1-5): 5

Goodbye!
```

Notice option 2 deliberately calls the same `fetch_weather()` function
with `simulate_error=True`, producing the exact "Could not retrieve
weather data." message a real failed API call would trigger — this is
the same error-handling path a real integration needs, exercised safely
and reproducibly without depending on a real API actually being down.

## How to run it

```bash
cd chapters/chapter-19-apis-json/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder).

## Ideas to make it your own (optional stretch goals)

- Add a "forecast only" menu option that prints just
  `weather["forecast"]`, formatted as a small table, without the current
  conditions line.
- Add a fourth mocked quote to `MOCK_QUOTE_RESPONSES` and a "random
  quote" menu option using `random.randint()` (from Chapter 11) to pick
  an index automatically instead of asking the user for one.
- Change `parse_weather()` to also return a `"forecast_high"` key (the
  maximum `high_f` across the whole forecast, using `max()` and a
  generator expression), and show it in `format_weather()`'s output.

## Why this project matters

Nearly every consumer app with a "current conditions" screen — weather,
stocks, sports scores, a system status page — runs exactly this same
fetch → parse → format pipeline behind the scenes, refreshed on a timer
or a pull-to-refresh gesture. The mocked-response technique used
throughout this project (a hardcoded JSON string standing in for "what
the API would return") is also the exact same technique real production
test suites use to test this kind of code without hitting a live network
on every test run — this project isn't just a simplified stand-in for the
real thing, it's built the way the real thing gets tested.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Weather & Quote-of-the-Day Fetcher above is fully built out with a
starter and reference solution — the four ideas below are not. Each is a
real, grounded use case solvable with only what's been taught through
Chapter 19 (everything through Chapter 18's regular expressions, plus
this chapter's `json` module and fetch-parse-format pipeline pattern —
`requests` itself is never actually called in graded code, only
referenced conceptually). No starter or solution files are provided on
purpose — building one of these unassisted is the point.

### 1. Currency Converter (Mocked Exchange-Rate Response)

**Problem:** A traveler needs to quickly convert an amount between two
currencies using a current exchange rate, without needing to know the
rate by heart.

**What it should do:** Build a mocked exchange-rate response, e.g.
`json.dumps({"base": "USD", "rates": {"EUR": 0.92, "GBP": 0.79, "JPY": 149.5}})`,
plus `fetch_rates()`, `parse_rates(raw_text)` (returning the `"rates"`
dict), and `convert(amount, rate)` (returning `round(amount * rate, 2)`).
Menu options: convert an amount to a chosen currency, show all available
rates, and quit.

**Suggested approach:** Keep the mocked rates as one dict of currency
code → rate, and use `.get(currency, None)` when looking up a
user-entered currency code, printing a friendly "not supported" message
if it's missing rather than crashing on a `KeyError`.

### 2. GitHub Repo Stats Summarizer (Mocked Repo JSON)

**Problem:** A developer wants a quick command-line summary of a
repository's stats (stars, open issues, primary language) without
opening a browser.

**What it should do:** Build a mocked repo JSON response resembling a
real `api.github.com/repos/...` response (a handful of realistic keys:
`"full_name"`, `"stargazers_count"`, `"open_issues_count"`,
`"language"`), plus `fetch_repo_data(repo_name)`,
`parse_repo_stats(raw_text)`, and `format_repo_summary(stats)`. Menu
options: look up a (mocked) repo by name from a small built-in
dictionary of 2-3 sample repos, and quit.

**Suggested approach:** Store the mocked repos as a dict of repo name →
JSON string, so `fetch_repo_data()` is a simple dict lookup with a
"repo not found" fallback for anything not in the mocked set — the same
`.get()`-with-a-default pattern from Sub-topic 5.

### 3. Joke/Trivia Fetcher

**Problem:** A small CLI tool needs to serve up a random joke or trivia
question from a fixed set, formatted consistently regardless of which
one is chosen.

**What it should do:** Build a list of several mocked joke/trivia JSON
responses (each with `"setup"`/`"punchline"` or `"question"`/`"answer"`
keys), plus `fetch_joke(index)`, `parse_joke(raw_text)`, and
`format_joke(joke)`. Menu options: get a specific joke by number, get a
random one (using `random.choice()` from Chapter 11), and quit.

**Suggested approach:** Reuse this project's exact `fetch`/`parse`/`format`
naming convention and structure for the joke pipeline — the shape doesn't
change based on what kind of content is being fetched, only the specific
fields being parsed and formatted.

### 4. JSON Config File Loader &amp; Validator

**Problem:** A small application needs to load a `config.json` file at
startup and validate that it has all the required settings before
running, rather than crashing partway through with a confusing error.

**What it should do:** Build a function `load_config(path)` using
`json.load()` (the file-based version, on an already-open file object
from Chapter 13's `with open(...) as f:`) to read a local
`.json` file. Build a function `validate_config(config, required_keys)`
that returns a list of any keys from `required_keys` missing from
`config`, using the same "collect what's missing" pattern from this
chapter's `.get()`/missing-key coverage. Menu options: generate a sample
`config.json` file, load and validate it (printing either "Config OK" or
the specific missing keys), and quit.

**Suggested approach:** This is the one idea in this list that uses
`json.load()`/`json.dump()` (file-based, no trailing "s" difference from
Sub-topic 3's Go Deeper box) instead of `loads()`/`dumps()`, since a
config file is a genuinely local file rather than an API response —
otherwise, the validation logic is the same "check what's expected
against what's actually there" pattern used throughout this chapter.
