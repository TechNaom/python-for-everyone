# Chapter 24 Practice Bank: Pandas for Data Analysis

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written in
the same style you'll see in real interviews. Every task here uses real
pandas directly — install it first: `pip install pandas`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: What Pandas Is & Why It Exists

1. Build a Series from a list.
2. Build a labeled table (DataFrame) from two lists.
3. **Debug the Code:** fix a wrong claim that DataFrames are unrelated to NumPy.
4. **Scenario — Comparing Two Approaches:** write `should_use_dataframe()`.
5. **Scenario — Interview Prep:** explain why pandas stays fast despite adding labels.

## Topic 2: Creating a DataFrame

1. Build a DataFrame from a dict.
2. Build a DataFrame from CSV-format text.
3. **Debug the Code:** fix code that passed a raw string to `read_csv()` instead of wrapping it in `StringIO`.
4. **Scenario — Reading a Real Export:** write `build_report_df()`.
5. **Scenario — Interview Prep:** explain what `read_csv()` replaces compared to the `csv` module.

## Topic 3: Inspecting Data

1. Get a DataFrame's shape.
2. Get a DataFrame's column names.
3. **Debug the Code:** fix code that called `.info()` where `.describe()` was needed.
4. **Scenario — Sanity-Checking a New Dataset:** write `quick_health_check()`.
5. **Scenario — Interview Prep:** explain what `.info()` and `.describe()` each tell you.

## Topic 4: Selecting, Filtering & `.loc[]` vs. `.iloc[]`

1. Select one column.
2. Filter rows above a threshold.
3. **Debug the Code:** fix code that used `.loc[]` where `.iloc[]` was needed.
4. **Scenario — Flagging Low Stock:** write `flag_low_stock()`.
5. **Scenario — Interview Prep:** explain the difference between `.loc[]` and `.iloc[]`.

## Topic 5: Adding Columns & Handling Missing Data

1. Add a computed column.
2. Fill in missing values.
3. **Debug the Code:** fix code that only checked one column for missing values instead of the whole DataFrame.
4. **Scenario — Cleaning a Messy Export:** write `clean_export()`.
5. **Scenario — Interview Prep:** explain `.isna()`, `.dropna()`, and `.fillna()`.

## Topic 6: Grouping, Aggregation & Sorting

1. Compute a total per group.
2. Sort a DataFrame descending.
3. **Debug the Code:** fix code that sorted ascending where descending was needed for a "top N" report.
4. **Scenario — Regional Sales Report:** write `regional_sales_report()`.
5. **Scenario — Interview Prep:** explain how `groupby()` + an aggregate + `sort_values()` combine into a "top N" report.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks. Every
numeric task's output is exactly reproducible, every time.
