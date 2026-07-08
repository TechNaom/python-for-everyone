# Chapter 24 Exercises: Pandas for Data Analysis

These exercises use what Chapter 24 covered: creating DataFrames,
inspecting them, selecting/filtering, `.loc[]`/`.iloc[]`, handling
missing data, and `groupby()`/`sort_values()`. Every task here uses
real pandas -- make sure it's installed first: `pip install pandas`.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — Building a sales DataFrame

Find `# TODO 1`. Write `make_sales_df(products, revenues)` — given two
plain Python lists (product names, revenues), return a DataFrame with
columns `"product"` and `"revenue"`.

## Task 2 — Summarizing a DataFrame

Find `# TODO 2`. Write `revenue_summary(df)` — return a dict with keys
`"total"`, `"average"`, `"max"` holding the `revenue` column's sum,
mean, and max.

## Task 3 — Filtering with a boolean condition

Find `# TODO 3`. Write `big_sales(df, threshold=1000)` — return only
the rows where `revenue` is greater than `threshold`, using boolean
filtering.

## Task 4 — Adding a computed column

Find `# TODO 4`. Write `add_tax_column(df, tax_rate)` — return a new
DataFrame with a `revenue_with_tax` column, computed as
`revenue * (1 + tax_rate)`.

## Task 5 — `.loc[]` vs. `.iloc[]`

Find `# TODO 5`. Write `get_row_by_label(df, label)` and
`get_row_by_position(df, position)` — the first uses `.loc[]`, the
second uses `.iloc[]`.

## Task 6 — Handling missing data

Find `# TODO 6`. Write `clean_revenue(df)` — given a DataFrame whose
`revenue` column may contain missing values, return a new DataFrame
with those missing values filled in with `0`.

## Task 7 — Grouping and aggregating

Find `# TODO 7`. Write `total_by_region(df)` — given a DataFrame with
`region` and `revenue` columns, return one total revenue per region
using `groupby()`.

## Task 8 — Sorting

Find `# TODO 8`. Write `top_products(df, n=3)` — given a DataFrame with
`product` and `revenue` columns, return the top `n` rows by revenue,
highest first.

## Task 9 — Debug the Code

Find `# TODO 9`. This is supposed to return each region's total
revenue, but it groups by the wrong column. Find and fix it.

## Checking your work

Compare your output against `solution.py`. Every task's output is
exactly reproducible, every time.
