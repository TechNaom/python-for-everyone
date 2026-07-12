# datacli

A command-line tool that turns **any** CSV file into a report: a grand
total, a top-N breakdown by group, summary statistics, and flagged
outlier rows — without being hardcoded to any one dataset's column
names.

This is Capstone 2 of the Python for Everyone course. It repackages
the analysis logic from [Chapter 24's Sales-Data
Dashboard](../../chapters/chapter-24-pandas-data-analysis/project/)
(pandas `groupby`/`sum`/`sort_values`/boolean filtering) and
[Chapter 23's NumPy statistics](../../chapters/chapter-23-numpy-data-analysis/project/)
patterns, using the exact `core.py`/`cli.py` package split and
`pyproject.toml` packaging pattern from [Chapter 31's
`taskbox`](../../chapters/chapter-31-professional-python/project/solution/taskbox/).

## Architecture decision: how does it know which columns to use?

Chapter 24's dashboard was hardwired to one dataset's exact column
names (`product`, `region`, `units_sold`, `unit_price`). A real CSV a
user downloads will almost never match those names — it might call the
equivalent columns `Category`, `Territory`, `Qty`, `Price`, or anything
else.

**`datacli` solves this with required `--group-by` and `--value-column`
flags on every subcommand, instead of a hardcoded naming convention.**
The user tells the tool which column to group by and which numeric
column to total, on every run:

```bash
datacli analyze mydata.csv --group-by Territory --value-column Price
```

I chose required flags over "smart" auto-detection (e.g. guessing the
first text column is the group and the first numeric column is the
value) because auto-detection fails silently and confusingly on a CSV
with several plausible candidate columns — a wrong guess produces a
report that *looks* right but analyzes the wrong column. Explicit flags
are a little more typing, but they're honest about what's about to be
computed, and they make `core.py`'s functions genuinely dataset-agnostic:
nothing in `core.py` contains a hardcoded column name like `'product'`
or `'revenue'` — every function that needs one takes it as a parameter.

When a requested column doesn't exist in the file, `datacli` catches it
explicitly (see [Error handling](#error-handling-missing-columns)
below) instead of letting a raw pandas `KeyError` reach the user.

## Install

```bash
cd capstones/capstone-2-data-cli
python3 -m venv .venv
source .venv/bin/activate      # .venv\Scripts\activate on Windows
pip install -e .
datacli --help
```

```text
usage: datacli [-h] [-v] {analyze,report,export} ...

Turn any CSV file into totals, top-N breakdowns, and flagged outliers.

positional arguments:
  {analyze,report,export}
    analyze             print the total and per-group breakdown for a value
                        column
    report              print the full report: total, top-N groups, summary
                        stats, and flagged rows
    export              write the computed summary (total + per-group
                        breakdown) to a file

options:
  -h, --help            show this help message and exit
  -v, --verbose         show debug-level logging (file paths, row counts,
                        column checks, etc.)
```

## Usage

### `analyze` — total + per-group breakdown

```bash
datacli analyze <csv_path> --group-by COLUMN --value-column COLUMN
```

### `report` — total + top-N + summary statistics + flagged rows

```bash
datacli report <csv_path> --group-by COLUMN --value-column COLUMN [--top N] [--threshold X]
```

`--top` defaults to 5. `--threshold` defaults to the value column's
mean if not given — rows below it are flagged as underperforming.

### `export` — write the summary to a file

```bash
datacli export <csv_path> --group-by COLUMN --value-column COLUMN --format json|csv -o OUTPUT_PATH
```

### `-v` / `--verbose`

Add before the subcommand to see DEBUG-level diagnostics (file paths,
row counts, which columns were checked) in addition to normal INFO
messages. All diagnostic output goes through Python's `logging` module,
never `print()`, and only `cli.py` touches the terminal — `core.py` is
plain, reusable logic.

## Real example run #1: the original sales dataset

[`sample_data/sales.csv`](sample_data/sales.csv) is the same dataset
from Chapter 24's Sales-Data Dashboard, saved to a real file with the
`revenue = units_sold * unit_price` column pre-computed (Chapter 24 computed
it in memory from an embedded string; `datacli` reads real files off disk,
so the computed column lives in the CSV itself).

```bash
$ datacli analyze sample_data/sales.csv --group-by product --value-column revenue
```

```text
=== Total revenue ===
10,304.00

=== product breakdown by revenue ===
Widget: 4,110.00
Gizmo: 3,420.00
Gadget: 2,774.00
```

```bash
$ datacli report sample_data/sales.csv --group-by region --value-column revenue --top 3
```

```text
=== Total revenue ===
10,304.00

=== Top 3 region by revenue ===
East: 7,164.00
West: 3,140.00

=== Summary Statistics for revenue ===
count=10, mean=1,030.40, median=1,075.00, std=490.82, min=270.00, max=1,830.00

=== Flagged Rows (revenue < 1,030.40) ===
date=2026-01-05, product=Gadget, region=West, units_sold=25, unit_price=38, revenue=950
date=2026-01-06, product=Widget, region=West, units_sold=18, unit_price=30, revenue=540
date=2026-01-07, product=Gizmo, region=West, units_sold=9, unit_price=30, revenue=270
date=2026-01-08, product=Gadget, region=West, units_sold=15, unit_price=38, revenue=570
date=2026-01-09, product=Widget, region=West, units_sold=27, unit_price=30, revenue=810
```

```bash
$ datacli export sample_data/sales.csv --group-by product --value-column revenue --format json -o out_sales.json
```

```text
INFO: Wrote json summary to out_sales.json
Exported json summary to out_sales.json
```

```json
{
  "source_csv": "sample_data/sales.csv",
  "group_by": "product",
  "value_column": "revenue",
  "total": 10304.0,
  "breakdown": {
    "Widget": 4110,
    "Gizmo": 3420,
    "Gadget": 2774
  },
  "summary_stats": {
    "count": 10,
    "mean": 1030.4,
    "median": 1075.0,
    "std": 490.82406895614514,
    "min": 270.0,
    "max": 1830.0
  }
}
```

The totals ($10,304 grand total, Widget $4,110 / Gizmo $3,420 / Gadget
$2,774, East $7,164 / West $3,140) match Chapter 24's original
dashboard output exactly — same math, generalized column handling.

## Real example run #2: a genuinely different CSV (personal expenses)

[`sample_data/expenses.csv`](sample_data/expenses.csv) is a hand-written
expense-tracking dataset — a completely different domain with different
column names (`expense_date`, `category`, `description`, `amount_usd`
instead of `date`, `product`, `region`, `revenue`). No code changes,
just different flag values:

```bash
$ datacli analyze sample_data/expenses.csv --group-by category --value-column amount_usd
```

```text
=== Total amount_usd ===
2,154.01

=== category breakdown by amount_usd ===
Rent: 1,450.00
Groceries: 292.82
Entertainment: 164.49
Utilities: 134.50
Transportation: 112.20
```

```bash
$ datacli report sample_data/expenses.csv --group-by category --value-column amount_usd --top 4
```

```text
=== Total amount_usd ===
2,154.01

=== Top 4 category by amount_usd ===
Rent: 1,450.00
Groceries: 292.82
Entertainment: 164.49
Utilities: 134.50

=== Summary Statistics for amount_usd ===
count=12, mean=179.50, median=68.80, std=401.27, min=15.99, max=1,450.00

=== Flagged Rows (amount_usd < 179.50) ===
expense_date=2026-02-01, category=Groceries, description=Weekly shop, amount_usd=84.32
expense_date=2026-02-03, category=Entertainment, description=Movie tickets, amount_usd=28.5
expense_date=2026-02-04, category=Groceries, description=Farmers market, amount_usd=41.75
expense_date=2026-02-05, category=Utilities, description=Electric bill, amount_usd=96.1
expense_date=2026-02-06, category=Entertainment, description=Streaming subscription, amount_usd=15.99
expense_date=2026-02-07, category=Groceries, description=Weekly shop, amount_usd=77.6
expense_date=2026-02-08, category=Transportation, description=Gas fill-up, amount_usd=52.2
expense_date=2026-02-09, category=Utilities, description=Water bill, amount_usd=38.4
expense_date=2026-02-10, category=Entertainment, description=Concert ticket, amount_usd=120.0
expense_date=2026-02-11, category=Transportation, description=Bus pass, amount_usd=60.0
expense_date=2026-02-12, category=Groceries, description=Weekly shop, amount_usd=89.15
```

```bash
$ datacli export sample_data/expenses.csv --group-by category --value-column amount_usd --format json -o out_expenses.json
```

```json
{
  "source_csv": "sample_data/expenses.csv",
  "group_by": "category",
  "value_column": "amount_usd",
  "total": 2154.01,
  "breakdown": {
    "Rent": 1450.0,
    "Groceries": 292.82,
    "Entertainment": 164.49,
    "Utilities": 134.5,
    "Transportation": 112.2
  },
  "summary_stats": {
    "count": 12,
    "mean": 179.50083333333336,
    "median": 68.8,
    "std": 401.2682573010532,
    "min": 15.99,
    "max": 1450.0
  }
}
```

Note the (naturally) high standard deviation — Rent at $1,450 dwarfs
every other line item, which is exactly the kind of thing this tool is
meant to surface, on a dataset it has never seen and with no code
changes.

## Error handling: missing columns

Pointing the tool at a column that doesn't exist (a typo, a wrong
dataset) produces a clear, custom error naming both what was requested
and what's actually in the file — not a raw pandas traceback:

```bash
$ datacli analyze sample_data/sales.csv --group-by Regoin --value-column revenue
```

```text
ERROR: Column(s) 'Regoin' not found in sample_data/sales.csv. Available columns are: 'date', 'product', 'region', 'units_sold', 'unit_price', 'revenue'.
```

Exit code `1`. The same check applies to `--value-column`:

```bash
$ datacli analyze sample_data/expenses.csv --group-by category --value-column price
```

```text
ERROR: Column(s) 'price' not found in sample_data/expenses.csv. Available columns are: 'expense_date', 'category', 'description', 'amount_usd'.
```

A missing *required flag* (rather than a wrong column name) is left to
argparse itself, which already produces a clear usage message and a
non-zero exit code without any hand-rolled validation:

```bash
$ datacli analyze sample_data/sales.csv --group-by product
```

```text
usage: datacli analyze [-h] --group-by GROUP_BY --value-column VALUE_COLUMN csv_path
datacli analyze: error: the following arguments are required: --value-column
```

## The `--verbose` flag in action

Without `-v`, only INFO-level messages show (e.g. `export` confirming a
file was written). With `-v`, DEBUG-level diagnostics are added:

```text
$ datacli -v export sample_data/sales.csv --group-by product --value-column revenue --format json -o out.json
DEBUG: Loading CSV from sample_data/sales.csv
DEBUG: Loaded 10 row(s), columns: ['date', 'product', 'region', 'units_sold', 'unit_price', 'revenue']
DEBUG: Computed grand total for revenue: 10304.0
DEBUG: Computed 3 group total(s) for revenue by product
INFO: Wrote json summary to out.json
Exported json summary to out.json
```

## Limitations (honest disclosure)

- **No support for files that don't fit in memory.** `load_csv()` uses
  `pd.read_csv()`, which loads the entire file into memory at once —
  there's no chunked/streaming reading. A CSV of a few tens of
  thousands of rows is fine; a multi-gigabyte file will not be.
- **Malformed numeric columns are rejected, not silently cleaned.**
  If `--value-column` points at a column containing values pandas can't
  parse as numbers (stray text, a currency-formatted string like
  `"$1,234.56"` that hasn't been stripped of `$`/`,`), `datacli` raises
  a clear `DataCliError` naming the column rather than letting pandas
  silently turn it into `NaN` and quietly corrupt totals. It does not
  attempt to auto-clean currency formatting for you — clean the source
  CSV first.
- **Blank/missing cells (`NaN`) in the value column are included in
  pandas' default `.sum()`/`.mean()` behavior**, which treats `NaN` as
  0 for `.sum()` and excludes it from `.mean()`/`.median()`/`.std()`.
  `datacli` does not warn separately when a column contains blank
  cells — it relies on pandas' default numeric handling.
- **Single-file input only.** There's no glob/batch mode to analyze
  multiple CSVs at once or combine them.
- **The `flag_outliers` direction in `report` is always "below
  threshold."** Chapter 23/24-style "above threshold" flagging (e.g. a
  heat-warning threshold) is supported in `core.py`'s `flag_outliers(mode="above")`
  but not exposed as a CLI flag on `report` in this MVP.
- **Exported totals are rounded to 2 decimal places** before being
  written to JSON/CSV, matching the console report's `.2f` display.
  Without this, raw floating-point sums occasionally produce noise
  like `63.99999999999999` instead of `64.0` in the exported file even
  though the on-screen report always looked clean — this was caught in
  review and fixed by rounding at export time, not hidden.

## Project layout

```text
capstone-2-data-cli/
  datacli/
    __init__.py
    core.py     # analysis logic only -- zero argparse imports, zero print()
    cli.py      # argparse + logging + terminal/file output -- the only file that touches the terminal
  sample_data/
    sales.csv       # Chapter 24's dataset, saved to a real file
    expenses.csv    # a second, unrelated dataset for proving generalization
  pyproject.toml
  README.md
```

## Stretch goals not built in this MVP

- `.xlsx` input support via `pd.read_excel()`.
- A `--config` flag for default column names.
- A second console-script alias (e.g. `dcli`).
- A `--chart` flag on `report` for a matplotlib bar chart.
- An `--above`/`--below` flag on `report` to control outlier direction
  (the underlying `core.flag_outliers(mode=...)` already supports it).
