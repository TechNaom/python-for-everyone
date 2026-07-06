# Chapter 13 Practice Bank: File Handling & CSV

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses everything from
Chapters 1-12 plus this chapter's own toolkit: `open()`/file I/O with
`with`, `.read()`/`.readline()`/`.readlines()`, write (`"w"`) and
append (`"a"`) modes, `"r+"`, relative vs. absolute paths, the `csv`
module (`csv.reader`/`csv.writer`/`csv.DictReader`/`csv.DictWriter`),
and `FileNotFoundError`/`PermissionError` handling. No other class
besides a custom exception subclassing `Exception`, and no import
beyond `math`/`datetime`/`random`/`csv`.

Every sample data file these problems read from (`notes.txt`,
`settings.txt`, `sales.csv`, `sales_extra.csv`, `app.log`,
`orders.csv`) lives in this same `practice/` folder, so run
`starter.py`/`solution.py` from inside this folder — a plain relative
filename like `"notes.txt"` only resolves correctly when Python is
run from the same folder the file lives in.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Opening & Reading Files

1. Write `read_whole_file(filename)`, opening with `with` and returning `file.read()`.
2. Write `count_lines(filename)`, returning how many lines `.readlines()` found.
3. Write `first_line(filename)`, returning just `file.readline().strip()`.
4. Write `lines_as_list(filename)`, looping over the file object directly and returning a stripped list.
5. **Debug the Code:** fix a function that opens a file the manual way with no `with` statement and no `.close()` — a file handle leak.
6. **Scenario — Loading a Config File at Startup:** write `load_startup_settings(filename)` that reads a settings file's lines the moment a program starts.
7. **Scenario — Interview Prep:** explain the difference between `.read()` and `.readlines()`.

## Topic 2: Writing to Files

1. Write `save_lines(filename, lines)`, opening in `"w"` mode and writing each line with its own `"\n"`.
2. Write `append_line(filename, line)`, opening in `"a"` mode to add one more line without erasing what's there.
3. Write `overwrite_file(filename, text)`, opening in `"w"` mode to erase existing content and write new text.
4. Write `write_numbered_lines(filename, items)`, writing each item prefixed with its 1-based position.
5. **Debug the Code:** fix a function meant to accumulate a log across multiple calls, but that opens in `"w"` mode instead of `"a"` mode each time.
6. **Scenario — Appending to a Shared Audit Log:** write `record_audit_event(filename, username, action)` for a security log that must never lose a prior entry.
7. **Scenario — Interview Prep:** explain the real-world risk of mixing up `"w"` and `"a"` mode.

## Topic 3: File Modes & Paths

1. Write `make_mode_summary()`, returning a dict describing all four core modes: `"r"`, `"w"`, `"a"`, `"r+"`.
2. Write `increment_counter_file(filename)`, using `"r+"` mode and `file.seek(0)` to read-then-overwrite a stored number.
3. Write `describe_path_kind(path)`, returning `"absolute"` or `"relative"` based on the path's shape.
4. Write `read_with_explicit_mode(filename)`, opening with the explicit `"r"` mode instead of relying on the default.
5. **Debug the Code:** fix a function that opens a file in `"w"` mode when it needed `"r+"` to read-then-update without erasing first.
6. **Scenario — "It Works on My Machine":** write `explain_relative_path_bug(cwd, script_folder)`, explaining why a relative path can fail depending on where a script is run from.
7. **Scenario — Interview Prep:** explain why absolute paths aren't just "the safer default".

## Topic 4: The `csv` Module

1. Write `read_csv_rows(filename)`, using `csv.reader` to return a list of row-lists.
2. Write `read_csv_as_dicts(filename)`, using `csv.DictReader` to return a list of row-dictionaries.
3. Write `total_sales_value(filename)`, summing a numeric column with `csv.DictReader`.
4. Write `write_products_csv(filename, products)`, using `csv.writer` with `newline=""` to export rows.
5. **Debug the Code:** fix a `csv.DictWriter` call that forgot to pass `newline=""` when opening the file.
6. **Scenario — Importing a Spreadsheet Export:** write `find_expensive_products(filename, minimum_price)`, filtering an exported CSV by a price threshold.
7. **Scenario — Interview Prep:** explain why production code uses the `csv` module instead of hand-splitting lines with `.split(",")`.

## Topic 5: Handling File-Related Exceptions

1. Write `read_safely(filename)`, catching `FileNotFoundError` and returning `None`.
2. Write `read_safely_with_message(filename)`, catching `FileNotFoundError as e` and returning a message built from `e`.
3. Write `load_or_default(filename, default_text)`, catching `FileNotFoundError` and returning a fallback value.
4. Write `open_for_either_error(filename)`, using separate `except FileNotFoundError` and `except PermissionError` blocks.
5. **Debug the Code:** fix a function whose `except` clause catches the wrong exception type entirely, so a genuinely missing file still crashes the program.
6. **Scenario — Defensive Startup Loader:** write `load_user_preferences(filename)` for an app that must never crash just because a settings file doesn't exist yet.
7. **Scenario — Interview Prep:** explain why Python code usually prefers catching `FileNotFoundError` over checking if a file exists first.

## Topic 6: Bringing It Together — File & CSV Processing in Production

1. Write `count_error_lines(log_filename)`, defensively counting `"ERROR"` lines in a log file.
2. Write `export_summary_csv(counts, report_filename)`, exporting a dict of counts as a CSV report.
3. Write `count_log_levels(log_filename)`, counting how many lines match each of several log levels.
4. Write `merge_csv_reports(filenames, output_filename)`, defensively merging multiple CSV files that might not all exist into one combined report.
5. **Debug the Code:** fix a function that never actually catches `FileNotFoundError` at all, so a missing input file crashes the whole function instead of returning a safe fallback.
6. **Scenario — Nightly Batch Report Job:** write `run_nightly_report(log_filename, report_filename)`, combining defensive reading, log processing, and a CSV export into one real batch-job pattern.
7. **Scenario — Interview Prep:** describe the overall pattern real production code uses for file and CSV processing.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks. A few TODOs (like Topic 3.2 and 3.5) write to
small helper files in this same folder — that's expected, and running
the script again should still produce correct results.
