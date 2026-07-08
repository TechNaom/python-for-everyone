# Chapter 24 Project: Sales-Data Dashboard (CSV In, Insights Out)

A **menu-driven mini-app** (one Python file, like Chapter 23's project)
that loads a sales dataset with pandas and turns it into a real
business report: total revenue, top products and regions, and a list
of underperforming line items.

## What you'll build

A CSV-format sales dataset (embedded as a Python string, parsed with
`pd.read_csv()` on a `StringIO` — no real file I/O required beyond
what Chapter 13 already taught, kept as a string here purely so the
project runs standalone with no extra file to download). The dashboard
computes and reports:

1. **Total revenue** — summed across every sale.
2. **Top products by revenue** — using `.groupby()` + `.sum()` +
   `.sort_values()`.
3. **Top regions by revenue** — the same pipeline, grouped by region
   instead of product.
4. **Underperforming line items** — individual sales below a revenue
   threshold, found with boolean filtering.
5. **A formatted report** combining all four sections into one
   readable, multi-line string.

## Example run

```text
=== Sales-Data Dashboard ===

=== Total Revenue ===
$10,304

=== Top Products by Revenue ===
Widget: $4,110
Gizmo: $3,420
Gadget: $2,774

=== Top Regions by Revenue ===
East: $7,164
West: $3,140

=== Underperforming Line Items (revenue < $600) ===
2026-01-06 Widget West: $540
2026-01-07 Gizmo West: $270
2026-01-08 Gadget West: $570
```

## How to run

```bash
cd chapters/chapter-24-pandas-data-analysis/project
pip install pandas   # if you haven't already
python3 starter.py
```

Fill in the numbered `# TODO` sections. Want to see a finished version?
Run `python3 solution.py`.

## The pieces

- **`SALES_CSV`** — a CSV-format string, parsed with `pd.read_csv()` on a `StringIO` wrapper.
- **`load_sales()`** — parses `SALES_CSV` into a DataFrame and adds a computed `revenue` column (`units_sold * unit_price`).
- **`total_revenue()`** — `.sum()` across the whole `revenue` column.
- **`top_products()`** / **`top_regions()`** — `.groupby()` + `.sum()` + `.sort_values(ascending=False)`, returning the ranked totals.
- **`underperforming_sales()`** — boolean filtering (`df[df['revenue'] < threshold]`) to find individual weak line items.
- **`format_report()`** — combines every section into one readable report string.

## Ideas to make it your own

- Add a "best single day" callout — the date with the highest total revenue across all products/regions.
- Add a per-product-per-region breakdown using `df.groupby(['product', 'region'])['revenue'].sum()`.
- Load `SALES_CSV` from a real `.csv` file on disk with `pd.read_csv("sales.csv")` instead of a hardcoded string (Chapter 13 already taught real file I/O).

## Why this project matters

Nearly every real "turn this spreadsheet into a report" task — sales,
donations, survey responses, expenses — follows this exact shape: load
tabular data, compute totals, break totals down by group, and flag
outliers with a condition. This project builds that entire pattern
once, on business data concrete enough to reason about intuitively.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Sales-Data Dashboard above is fully built out with a starter and
reference solution — the four ideas below are not. Each is a real,
grounded use case solvable with only what's been taught through
Chapter 24. No starter or solution files are provided on purpose —
building one of these unassisted is the point.

### 1. A Student-Grades Gradebook Analyzer

**Problem:** A teacher has a CSV of student names, subjects, and
scores, and wants a per-student and per-subject breakdown.

**What it should do:** Load the data into a DataFrame, report each
student's average score (`groupby('student')`), each subject's class
average (`groupby('subject')`), and flag students below a passing
threshold using boolean filtering.

**Suggested approach:** This is almost a direct re-skin of Chapter 23's
Grade & Statistics Analyzer, but built on a DataFrame instead of a raw
NumPy grid — a good chance to feel the difference directly.

### 2. A Simple Expense Tracker

**Problem:** Someone wants to track personal expenses by category
(groceries, rent, entertainment) and see where their money is going.

**What it should do:** Load a CSV of `date, category, amount` rows,
report total spending per category (`groupby('category')`), the
single largest expense, and total spending for the month.

**Suggested approach:** Nearly identical structure to this project's
`top_products()`/`top_regions()` pattern, just with "category" instead
of "product."

### 3. A Weather-Data Trend Summarizer

**Problem:** Someone has a CSV of daily temperature readings across
several cities and wants a quick trend summary.

**What it should do:** Load the data, report each city's average
temperature (`groupby('city')`), the single hottest and coldest
reading overall, and flag any reading above a heat-warning threshold
using boolean filtering.

**Suggested approach:** Directly reuses this project's
groupby-then-filter structure — "city" instead of "product," "reading"
instead of "sale."

### 4. A Survey-Response Analyzer

**Problem:** A CSV of survey responses (respondent, question,
rating 1-5) needs summarizing into an average rating per question.

**What it should do:** Load the data, report the average rating per
question (`groupby('question')`), the count of each rating value per
question, and flag any question whose average rating is below a
"needs attention" threshold.

**Suggested approach:** `.groupby('question')['rating'].mean()` is the
core operation; `.value_counts()` (a new but simple method — one line,
similar in spirit to `.groupby().size()`) handles the per-rating
counts.
