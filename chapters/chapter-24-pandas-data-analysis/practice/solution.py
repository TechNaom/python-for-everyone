"""
Chapter 24 Practice Bank: Pandas for Data Analysis -- reference solution.
Run this from inside the practice/ folder: python3 solution.py
"""

import pandas as pd
import numpy as np
from io import StringIO

# ============================================================
# Topic 1: What Pandas Is & Why It Exists
# ============================================================

# TODO 1.1
def make_series(values):
    return pd.Series(values)


print(make_series([1, 2, 3]))


# TODO 1.2
def make_labeled_table(names, scores):
    return pd.DataFrame({"name": names, "score": scores})


print(make_labeled_table(["Ana", "Ben"], [88, 92]))


# TODO 1.3 (Debug the Code)
# Bug: claimed a DataFrame is unrelated to NumPy -- in fact every
# DataFrame column IS backed by a NumPy array underneath.
def describe_dataframe_vs_array():
    return (
        "A DataFrame is built directly on top of NumPy -- each column is "
        "backed by its own NumPy array, so pandas keeps NumPy's speed while "
        "adding row/column labels and mixed dtypes across columns."
    )


print(describe_dataframe_vs_array())


# TODO 1.A (Scenario -- Comparing Two Approaches)
def should_use_dataframe(has_mixed_types, needs_column_labels):
    return has_mixed_types or needs_column_labels


print(should_use_dataframe(True, False))
print(should_use_dataframe(False, False))


# TODO 1.B (Scenario -- Interview Prep)
def explain_why_pandas_is_built_on_numpy():
    return (
        "Each DataFrame column is its own homogeneous NumPy array, so "
        "column-level operations (sums, filters, aggregates) still run as "
        "fast, vectorized NumPy code -- the labeling and mixed-dtype-across- "
        "columns structure pandas adds sits on top, at the DataFrame level."
    )


print(explain_why_pandas_is_built_on_numpy())


# ============================================================
# Topic 2: Creating a DataFrame
# ============================================================

# TODO 2.1
def df_from_dict(data_dict):
    return pd.DataFrame(data_dict)


print(df_from_dict({"product": ["Widget"], "revenue": [1200]}))


# TODO 2.2
def df_from_csv_text(csv_text):
    return pd.read_csv(StringIO(csv_text))


print(df_from_csv_text("product,revenue\nWidget,1200\nGadget,950\n"))


# TODO 2.3 (Debug the Code)
# Bug: passed the raw CSV string directly to read_csv(), which tries to
# treat it as a file PATH instead of file CONTENT -- fixed by wrapping
# it in StringIO first.
def load_sales():
    csv_text = "product,revenue\nWidget,1200\nGadget,950\n"
    return pd.read_csv(StringIO(csv_text))


print(load_sales())


# TODO 2.A (Scenario -- Reading a Real Export)
def build_report_df(products, regions, revenues):
    return pd.DataFrame({"product": products, "region": regions, "revenue": revenues})


print(build_report_df(["Widget", "Gadget"], ["East", "West"], [1200, 950]))


# TODO 2.B (Scenario -- Interview Prep)
def explain_read_csv_vs_csv_module():
    return (
        "pd.read_csv() replaces the entire manual open-file/loop-rows/parse- "
        "values pattern the csv module needs, returning a full DataFrame "
        "with column types already inferred -- one call instead of a hand- "
        "written accumulator loop."
    )


print(explain_read_csv_vs_csv_module())


# ============================================================
# Topic 3: Inspecting Data
# ============================================================

# TODO 3.1
def row_and_column_count(df):
    return df.shape


print(row_and_column_count(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})))


# TODO 3.2
def column_names(df):
    return list(df.columns)


print(column_names(pd.DataFrame({"product": ["Widget"], "revenue": [1200]})))


# TODO 3.3 (Debug the Code)
# Bug: called .info() (structure/dtypes only, prints and returns None)
# when .describe() (numeric summary statistics) was actually needed.
def describe_columns(df):
    return df.describe()


sample_inspect_df = pd.DataFrame({"revenue": [100, 200, 300]})
print(describe_columns(sample_inspect_df))


# TODO 3.A (Scenario -- Sanity-Checking a New Dataset)
def quick_health_check(df):
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "any_missing": bool(df.isna().any().any()),
    }


print(quick_health_check(pd.DataFrame({"revenue": [100, None, 300]})))


# TODO 3.B (Scenario -- Interview Prep)
def explain_info_vs_describe():
    return (
        ".info() summarizes structure: column names, non-null counts, and "
        "dtypes -- the fastest way to spot missing data or a wrong type. "
        ".describe() summarizes numeric VALUES: count, mean, std, min, max, "
        "and quartiles for every numeric column."
    )


print(explain_info_vs_describe())


# ============================================================
# Topic 4: Selecting, Filtering & .loc[] vs .iloc[]
# ============================================================

# TODO 4.1
def select_column(df, col_name):
    return df[col_name]


print(select_column(pd.DataFrame({"revenue": [1200, 950]}), "revenue"))


# TODO 4.2
def filter_above(df, col_name, threshold):
    return df[df[col_name] > threshold]


print(filter_above(pd.DataFrame({"revenue": [500, 1500, 300]}), "revenue", 1000))


# TODO 4.3 (Debug the Code)
# Bug: used .loc[1] (look up the row LABELED 1) when POSITION 1 was
# asked for -- fixed with .iloc[1].
def get_by_position(df):
    return df.iloc[1]


sample_loc_df = pd.DataFrame({"product": ["Widget", "Gadget"], "revenue": [1200, 950]}, index=["r1", "r2"])
print(get_by_position(sample_loc_df))


# TODO 4.A (Scenario -- Flagging Low Stock)
def flag_low_stock(df, threshold=10):
    return df[df["quantity"] < threshold]


print(flag_low_stock(pd.DataFrame({"product": ["Widget", "Gadget"], "quantity": [5, 20]})))


# TODO 4.B (Scenario -- Interview Prep)
def explain_loc_vs_iloc():
    return (
        ".loc[] selects by label (the actual row index value or column "
        "name); .iloc[] selects by integer position, regardless of what "
        "the labels are. They agree on a freshly loaded DataFrame because "
        "the default index IS 0, 1, 2, ... -- once the index becomes "
        "something else (names, dates, or rows reordered after a filter/ "
        "sort), the two can return completely different rows."
    )


print(explain_loc_vs_iloc())


# ============================================================
# Topic 5: Adding Columns & Handling Missing Data
# ============================================================

# TODO 5.1
def add_computed_column(df, new_col, col_a, col_b):
    result = df.copy()
    result[new_col] = result[col_a] * result[col_b]
    return result


print(add_computed_column(pd.DataFrame({"units": [10, 20], "price": [2, 3]}), "revenue", "units", "price"))


# TODO 5.2
def fill_missing(df, col_name, fill_value):
    result = df.copy()
    result[col_name] = result[col_name].fillna(fill_value)
    return result


print(fill_missing(pd.DataFrame({"revenue": [1200.0, None, 700.0]}), "revenue", 0))


# TODO 5.3 (Debug the Code)
# Bug: only checked the first column (.iloc[:, 0]) instead of every
# column in the DataFrame.
def count_missing(df):
    return int(df.isna().sum().sum())


sample_missing_df = pd.DataFrame({"a": [1, None, 3], "b": [None, 2, 3]})
print(count_missing(sample_missing_df))


# TODO 5.A (Scenario -- Cleaning a Messy Export)
def clean_export(df):
    result = df.copy()
    result["region"] = result["region"].fillna("Unknown")
    return result


print(clean_export(pd.DataFrame({"product": ["Widget", "Gadget"], "region": ["East", None]})))


# TODO 5.B (Scenario -- Interview Prep)
def explain_missing_data_tools():
    return (
        ".isna() returns a same-shape True/False table showing which "
        "values are missing. .dropna() removes rows containing any "
        "missing value. .fillna(value) replaces missing values with a "
        "chosen default, either one flat value or per-column via a dict."
    )


print(explain_missing_data_tools())


# ============================================================
# Topic 6: Grouping, Aggregation & Sorting
# ============================================================

# TODO 6.1
def total_per_group(df, group_col, value_col):
    return df.groupby(group_col)[value_col].sum()


print(total_per_group(pd.DataFrame({"region": ["East", "West", "East"], "revenue": [1200, 950, 1830]}), "region", "revenue"))


# TODO 6.2
def sorted_descending(df, col_name):
    return df.sort_values(col_name, ascending=False)


print(sorted_descending(pd.DataFrame({"product": ["Widget", "Gadget"], "revenue": [1200, 1830]}), "revenue"))


# TODO 6.3 (Debug the Code)
# Bug: sorted ascending (default) when the task asked for the TOP 2
# (highest first) -- fixed with ascending=False.
def top_two(df):
    return df.sort_values("revenue", ascending=False).head(2)


sample_top_df = pd.DataFrame({"product": ["Widget", "Gadget", "Gizmo"], "revenue": [1200, 950, 1830]})
print(top_two(sample_top_df))


# TODO 6.A (Scenario -- Regional Sales Report)
def regional_sales_report(df):
    return df.groupby("region")["revenue"].sum().sort_values(ascending=False)


print(regional_sales_report(pd.DataFrame({"region": ["East", "West", "East"], "revenue": [1200, 950, 1830]})))


# TODO 6.B (Scenario -- Interview Prep)
def explain_groupby_pipeline():
    return (
        "groupby(col) splits rows into groups by that column's unique "
        "values; an aggregate call like .sum() collapses each group to one "
        "number; sort_values(ascending=False) then reorders those results "
        "highest-first, and .head(n) keeps only the top n -- chaining all "
        "three builds a 'top N' report in one line."
    )


print(explain_groupby_pipeline())
