"""
Chapter 13 Practice Bank: File Handling & CSV -- reference solution.
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py
"""

import csv

# ============================================================
# Topic 1: Opening & Reading Files
# ============================================================

# TODO 1.1
def read_whole_file(filename):
    with open(filename) as file:
        return file.read()


print(read_whole_file("notes.txt"))


# TODO 1.2
def count_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
    return len(lines)


print(count_lines("notes.txt"))


# TODO 1.3
def first_line(filename):
    with open(filename) as file:
        return file.readline().strip()


print(first_line("notes.txt"))


# TODO 1.4
def lines_as_list(filename):
    stripped = []
    with open(filename) as file:
        for line in file:
            stripped.append(line.strip())
    return stripped


print(lines_as_list("notes.txt"))


# TODO 1.5 (Debug the Code)
def read_report(filename):
    with open(filename) as file:
        return file.read()


print(read_report("notes.txt"))


# TODO 1.A (Scenario -- Loading a Config File at Startup)
def load_startup_settings(filename):
    with open(filename) as file:
        return file.readlines()


print(load_startup_settings("settings.txt"))


# TODO 1.B (Scenario -- Interview Prep)
def explain_read_vs_readlines():
    return (
        ".read() returns the entire file as one single string, newlines "
        "and all, which is simplest when a program just needs the whole "
        "text at once. .readlines() (or looping over the file object "
        "directly) instead returns the content split into separate "
        "lines, which is what a program actually wants when each line "
        "represents its own record -- a task, a log entry, a row of "
        "data -- rather than one undifferentiated blob of text."
    )


print(explain_read_vs_readlines())


# ============================================================
# Topic 2: Writing to Files
# ============================================================

# TODO 2.1
def save_lines(filename, lines):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


save_lines("saved_notes.txt", ["Buy milk", "Call the bank"])
with open("saved_notes.txt") as file:
    print(file.read())


# TODO 2.2
def append_line(filename, line):
    with open(filename, "a") as file:
        file.write(line + "\n")


append_line("saved_notes.txt", "Finish the report")
with open("saved_notes.txt") as file:
    print(file.read())


# TODO 2.3
def overwrite_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)


overwrite_file("saved_notes.txt", "Only this line survives now\n")
with open("saved_notes.txt") as file:
    print(file.read())


# TODO 2.4
def write_numbered_lines(filename, items):
    with open(filename, "w") as file:
        for index, item in enumerate(items, start=1):
            file.write(f"{index}. {item}\n")


write_numbered_lines("checklist.txt", ["Pack bags", "Charge phone"])
with open("checklist.txt") as file:
    print(file.read())


# TODO 2.5 (Debug the Code)
def log_message(filename, message):
    with open(filename, "a") as file:
        file.write(message + "\n")


log_message("app_events.txt", "started")
log_message("app_events.txt", "processed request")
with open("app_events.txt") as file:
    print(file.read())


# TODO 2.A (Scenario -- Appending to a Shared Audit Log)
def record_audit_event(filename, username, action):
    with open(filename, "a") as file:
        file.write(f"{username}: {action}\n")


record_audit_event("audit_log.txt", "alice", "logged in")
record_audit_event("audit_log.txt", "bob", "updated profile")
with open("audit_log.txt") as file:
    print(file.read())


# TODO 2.B (Scenario -- Interview Prep)
def explain_w_vs_a_risk():
    return (
        "'w' mode erases a file's existing content the instant it's "
        "opened, before a single new byte is written, while 'a' mode "
        "adds new content after whatever is already there. The real "
        "risk in production code is opening a file that's meant to "
        "accumulate data -- a log, a running history -- in 'w' mode by "
        "mistake, which silently and permanently destroys every prior "
        "entry with no undo, often without the program raising any "
        "error at all."
    )


print(explain_w_vs_a_risk())


# ============================================================
# Topic 3: File Modes & Paths
# ============================================================

# TODO 3.1
def make_mode_summary():
    return {
        "r": "read only, the default",
        "w": "write only, erases existing content",
        "a": "append only, adds after existing content",
        "r+": "read and write, without erasing first",
    }


print(make_mode_summary())


# TODO 3.2
def increment_counter_file(filename):
    with open(filename, "r+") as file:
        value = int(file.read())
        file.seek(0)
        file.write(str(value + 1))


with open("counter.txt", "w") as file:
    file.write("5")
increment_counter_file("counter.txt")
with open("counter.txt") as file:
    print(file.read())


# TODO 3.3
def describe_path_kind(path):
    if path.startswith("/") or (len(path) > 1 and path[1] == ":"):
        return "absolute"
    return "relative"


print(describe_path_kind("notes.txt"))
print(describe_path_kind("/home/user/notes.txt"))


# TODO 3.4
def read_with_explicit_mode(filename):
    with open(filename, "r") as file:
        return file.read()


print(read_with_explicit_mode("notes.txt"))


# TODO 3.5 (Debug the Code)
def top_up_balance(filename, amount):
    with open(filename, "r+") as file:
        value = int(file.read())
        file.seek(0)
        file.write(str(value + amount))


with open("balance.txt", "w") as file:
    file.write("100")
top_up_balance("balance.txt", 25)
with open("balance.txt") as file:
    print(file.read())


# TODO 3.A (Scenario -- "It Works on My Machine")
def explain_relative_path_bug(cwd, script_folder):
    if cwd != script_folder:
        return (
            f"Running from '{cwd}' while the script and its data file "
            f"live in '{script_folder}' means a relative path like "
            f"'notes.txt' resolves against '{cwd}' instead, so Python "
            "looks in the wrong folder and raises FileNotFoundError -- "
            "even though the file genuinely exists right next to the "
            "script."
        )
    return (
        f"Running from '{cwd}', which matches the script's own folder, "
        "means a relative path like 'notes.txt' resolves correctly."
    )


print(explain_relative_path_bug("/home/alice", "/home/alice/project"))
print(explain_relative_path_bug("/home/alice/project", "/home/alice/project"))


# TODO 3.B (Scenario -- Interview Prep)
def explain_absolute_path_tradeoff():
    return (
        "An absolute path always points to the exact same file no "
        "matter where a program is launched from, which sounds like the "
        "safer choice -- but it hard-codes one specific location on one "
        "specific machine, so the program breaks the moment the project "
        "moves to a different folder or a different computer. Real "
        "projects usually prefer relative paths run from a known, "
        "consistent working directory instead of hard-coding an "
        "absolute one everywhere."
    )


print(explain_absolute_path_tradeoff())


# ============================================================
# Topic 4: The csv Module
# ============================================================

# TODO 4.1
def read_csv_rows(filename):
    rows = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows


print(read_csv_rows("sales.csv"))


# TODO 4.2
def read_csv_as_dicts(filename):
    records = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
    return records


print(read_csv_as_dicts("sales.csv"))


# TODO 4.3
def total_sales_value(filename):
    total = 0.0
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["price"])
    return round(total, 2)


print(total_sales_value("sales.csv"))


# TODO 4.4
def write_products_csv(filename, products):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["product", "price"])
        for product, price in products:
            writer.writerow([product, price])


write_products_csv("new_products.csv", [("Widget", 19.99), ("Gadget", 34.50)])
with open("new_products.csv") as file:
    print(file.read())


# TODO 4.5 (Debug the Code)
def write_records_csv(filename, records):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["product", "quantity"])
        writer.writeheader()
        writer.writerows(records)


write_records_csv(
    "restock.csv",
    [{"product": "Widget", "quantity": 4}, {"product": "Gadget", "quantity": 2}],
)
with open("restock.csv") as file:
    print(file.read())


# TODO 4.A (Scenario -- Importing a Spreadsheet Export)
def find_expensive_products(filename, minimum_price):
    expensive = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if float(row["price"]) >= minimum_price:
                expensive.append(row["product"])
    return expensive


print(find_expensive_products("sales.csv", 20))


# TODO 4.B (Scenario -- Interview Prep)
def explain_csv_module_value():
    return (
        "Hand-splitting a line with .split(',') breaks the instant a "
        "field itself contains a comma, like a quoted company name -- "
        "one row silently becomes the wrong number of fields. The csv "
        "module understands quoting rules and parses every row "
        "correctly regardless, which is exactly why production code "
        "never hand-parses CSV: a subtly wrong field count can corrupt "
        "downstream data without ever raising an error to notice."
    )


print(explain_csv_module_value())


# ============================================================
# Topic 5: Handling File-Related Exceptions
# ============================================================

# TODO 5.1
def read_safely(filename):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        return None


print(read_safely("does_not_exist.txt"))


# TODO 5.2
def read_safely_with_message(filename):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError as e:
        return f"Could not open file: {e}"


print(read_safely_with_message("does_not_exist.txt"))


# TODO 5.3
def load_or_default(filename, default_text):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        return default_text


print(load_or_default("does_not_exist.txt", "default content"))


# TODO 5.4
def open_for_either_error(filename):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        return "not found"
    except PermissionError:
        return "not permitted"


print(open_for_either_error("does_not_exist.txt"))


# TODO 5.5 (Debug the Code)
def load_config(filename):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        return ""


print(load_config("missing_config.txt"))


# TODO 5.A (Scenario -- Defensive Startup Loader)
def load_user_preferences(filename):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        print(f"'{filename}' doesn't exist yet -- using default preferences.")
        return "theme=light\n"
    except PermissionError:
        print(f"Not allowed to read '{filename}' -- using default preferences.")
        return "theme=light\n"


print(load_user_preferences("preferences.txt"))


# TODO 5.B (Scenario -- Interview Prep)
def explain_check_first_vs_try_it():
    return (
        "Checking 'does this file exist?' before calling open() leaves "
        "a timing gap between the check and the actual open -- the file "
        "could be deleted, moved, or have its permissions changed in "
        "between, however unlikely that sounds. Catching "
        "FileNotFoundError directly around the open() call itself is "
        "both simpler and immune to that gap, which is why Python code "
        "almost always prefers 'try it and catch the failure' over "
        "'check first, then act'."
    )


print(explain_check_first_vs_try_it())


# ============================================================
# Topic 6: Bringing It Together -- File & CSV Processing in Production
# ============================================================

# TODO 6.1
def count_error_lines(log_filename):
    try:
        count = 0
        with open(log_filename) as file:
            for line in file:
                if "ERROR" in line:
                    count += 1
        return count
    except FileNotFoundError:
        return 0


print(count_error_lines("app.log"))


# TODO 6.2
def export_summary_csv(counts, report_filename):
    with open(report_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["level", "count"])
        for level, count in counts.items():
            writer.writerow([level, count])


export_summary_csv({"ERROR": 3, "WARNING": 1, "INFO": 3}, "level_summary.csv")
with open("level_summary.csv") as file:
    print(file.read())


# TODO 6.3
def count_log_levels(log_filename):
    counts = {}
    try:
        with open(log_filename) as file:
            for line in file:
                for level in ("ERROR", "WARNING", "INFO"):
                    if level in line:
                        counts[level] = counts.get(level, 0) + 1
                        break
    except FileNotFoundError:
        return {}
    return counts


print(count_log_levels("app.log"))


# TODO 6.4
def merge_csv_reports(filenames, output_filename):
    all_rows = []
    fieldnames = None
    for filename in filenames:
        try:
            with open(filename) as file:
                reader = csv.DictReader(file)
                if fieldnames is None:
                    fieldnames = reader.fieldnames
                for row in reader:
                    all_rows.append(row)
        except FileNotFoundError:
            continue
    with open(output_filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)


merge_csv_reports(["sales.csv", "sales_extra.csv"], "combined_sales.csv")
with open("combined_sales.csv") as file:
    print(file.read())


# TODO 6.5 (Debug the Code)
def process_orders_file(filename):
    try:
        total = 0.0
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                total += float(row["amount"])
        return round(total, 2)
    except FileNotFoundError:
        return 0.0


print(process_orders_file("orders.csv"))


# TODO 6.A (Scenario -- Nightly Batch Report Job)
def run_nightly_report(log_filename, report_filename):
    counts = {}
    try:
        with open(log_filename) as file:
            for line in file:
                if "ERROR" in line:
                    message = line.strip().split("ERROR", 1)[1].strip()
                    counts[message] = counts.get(message, 0) + 1
    except FileNotFoundError:
        print(f"Log file '{log_filename}' not found -- skipping tonight's report.")
        return False

    with open(report_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["error_message", "occurrences"])
        for message, occurrences in counts.items():
            writer.writerow([message, occurrences])
    return True


print(run_nightly_report("app.log", "nightly_report.csv"))
with open("nightly_report.csv") as file:
    print(file.read())


# TODO 6.B (Scenario -- Interview Prep)
def explain_production_file_pattern():
    return (
        "Real production file processing follows one repeated shape: "
        "read defensively with try/except so a missing or unreadable "
        "input file can't crash an entire batch job, process the data "
        "with plain Python logic, and write the result back out with "
        "the csv module so another tool or a spreadsheet can consume it "
        "-- all of it wrapped in with so every file handle, on both the "
        "read side and the write side, gets closed automatically even "
        "if something above it fails."
    )


print(explain_production_file_pattern())
