"""
Chapter 24 Practice Bank: Pandas for Data Analysis
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Real pandas is used throughout -- install it first: pip install pandas
"""

import pandas as pd
import numpy as np
from io import StringIO

# ============================================================
# Topic 1: What Pandas Is & Why It Exists
# ============================================================

# TODO 1.1: Write make_series(values). Given a plain Python list of
# numbers, return it as a pandas Series.


# TODO 1.2: Write make_labeled_table(names, scores). Given two plain
# Python lists, return a DataFrame with columns "name" and "score" --
# the "after" side of a NumPy-vs-pandas comparison, since a plain
# NumPy array couldn't hold both a name (text) and a score (number)
# in the same structure.


# TODO 1.3 (Debug the Code): describe_dataframe_vs_array() below
# wrongly claims a DataFrame can't use any NumPy functionality at all.
# Fix its return value to correctly explain that a DataFrame column IS
# backed by a NumPy array underneath.
def describe_dataframe_vs_array():
    return "A DataFrame has nothing to do with NumPy -- they are completely unrelated libraries."


print(describe_dataframe_vs_array())


# TODO 1.A (Scenario -- Comparing Two Approaches): write
# should_use_dataframe(has_mixed_types, needs_column_labels). Return
# True if EITHER has_mixed_types OR needs_column_labels is True
# (either condition alone is a good reason to reach for a DataFrame
# over a plain NumPy array), otherwise False.


# TODO 1.B (Scenario -- Interview Prep): write
# explain_why_pandas_is_built_on_numpy() describing why pandas can add
# labels and mixed column types while still staying fast.


# ============================================================
# Topic 2: Creating a DataFrame
# ============================================================

# TODO 2.1: Write df_from_dict(data_dict). Return pd.DataFrame(data_dict).


# TODO 2.2: Write df_from_csv_text(csv_text). Given CSV-format text
# (a plain Python string), return pd.read_csv() applied to it wrapped
# in a StringIO.


# TODO 2.3 (Debug the Code): load_sales() below is supposed to build a
# DataFrame from CSV-format text using pd.read_csv(), but it passes the
# raw string directly instead of wrapping it in StringIO first. Fix it.
def load_sales():
    csv_text = "product,revenue\nWidget,1200\nGadget,950\n"
    return pd.read_csv(csv_text)


try:
    print(load_sales())
except Exception as e:
    print("Error:", e)


# TODO 2.A (Scenario -- Reading a Real Export): write
# build_report_df(products, regions, revenues). Given three plain
# Python lists of equal length, return a DataFrame with columns
# "product", "region", "revenue" -- a stand-in for a report just
# exported from another system.


# TODO 2.B (Scenario -- Interview Prep): write
# explain_read_csv_vs_csv_module() describing what pd.read_csv()
# replaces compared to Chapter 13's csv module.


# ============================================================
# Topic 3: Inspecting Data
# ============================================================

# TODO 3.1: Write row_and_column_count(df). Return df.shape.


# TODO 3.2: Write column_names(df). Return list(df.columns).


# TODO 3.3 (Debug the Code): describe_columns() below is supposed to
# return summary statistics (mean, min, max, etc.) for every numeric
# column, but it calls .info() (which only shows structure/dtypes) when
# .describe() was needed. Fix it.
def describe_columns(df):
    return df.info()


sample_inspect_df = pd.DataFrame({"revenue": [100, 200, 300]})
print(describe_columns(sample_inspect_df))


# TODO 3.A (Scenario -- Sanity-Checking a New Dataset): write
# quick_health_check(df). Return a dict with keys "shape", "columns",
# "any_missing" holding df.shape, list(df.columns), and whether
# df.isna().any().any() is True (there is at least one missing value
# anywhere in the DataFrame).


# TODO 3.B (Scenario -- Interview Prep): write
# explain_info_vs_describe() describing what .info() and .describe()
# each tell you about a DataFrame.


# ============================================================
# Topic 4: Selecting, Filtering & .loc[] vs .iloc[]
# ============================================================

# TODO 4.1: Write select_column(df, col_name). Return df[col_name].


# TODO 4.2: Write filter_above(df, col_name, threshold). Return only
# the rows where df[col_name] is strictly greater than threshold, using
# boolean filtering (no loop).


# TODO 4.3 (Debug the Code): get_by_position() below is supposed to
# return the row at POSITION 1 regardless of its label, but it uses
# .loc[1] (by LABEL) instead of .iloc[1] (by POSITION). Fix it.
def get_by_position(df):
    return df.loc[1]


sample_loc_df = pd.DataFrame({"product": ["Widget", "Gadget"], "revenue": [1200, 950]}, index=["r1", "r2"])
try:
    print(get_by_position(sample_loc_df))
except KeyError as e:
    print("KeyError:", e)


# TODO 4.A (Scenario -- Flagging Low Stock): write
# flag_low_stock(df, threshold=10). Given a DataFrame with a
# "quantity" column, return only the rows where quantity is strictly
# less than threshold, using boolean filtering.


# TODO 4.B (Scenario -- Interview Prep): write
# explain_loc_vs_iloc() describing the difference between .loc[] and
# .iloc[], and why they can look interchangeable on a freshly loaded
# DataFrame.


# ============================================================
# Topic 5: Adding Columns & Handling Missing Data
# ============================================================

# TODO 5.1: Write add_computed_column(df, new_col, col_a, col_b).
# Return a NEW DataFrame with new_col added, equal to df[col_a] *
# df[col_b] (do not modify df in place -- use df.copy()).


# TODO 5.2: Write fill_missing(df, col_name, fill_value). Return a NEW
# DataFrame with missing values in col_name replaced by fill_value.


# TODO 5.3 (Debug the Code): count_missing() below is supposed to
# return the TOTAL number of missing values in the whole DataFrame, but
# it only checks the first column instead of every column. Fix it.
def count_missing(df):
    return int(df.iloc[:, 0].isna().sum())


sample_missing_df = pd.DataFrame({"a": [1, None, 3], "b": [None, 2, 3]})
print(count_missing(sample_missing_df))


# TODO 5.A (Scenario -- Cleaning a Messy Export): write
# clean_export(df). Given a DataFrame that may have missing values in
# a "region" column, return a NEW DataFrame with those missing values
# filled in with the string "Unknown".


# TODO 5.B (Scenario -- Interview Prep): write
# explain_missing_data_tools() describing what .isna(), .dropna(), and
# .fillna() each do.


# ============================================================
# Topic 6: Grouping, Aggregation & Sorting
# ============================================================

# TODO 6.1: Write total_per_group(df, group_col, value_col). Return
# df.groupby(group_col)[value_col].sum().


# TODO 6.2: Write sorted_descending(df, col_name). Return df sorted by
# col_name, highest values first.


# TODO 6.3 (Debug the Code): top_two() below is supposed to return the
# TOP 2 rows by revenue (highest first), but it sorts ascending instead
# of descending. Fix it.
def top_two(df):
    return df.sort_values("revenue").head(2)


sample_top_df = pd.DataFrame({"product": ["Widget", "Gadget", "Gizmo"], "revenue": [1200, 950, 1830]})
print(top_two(sample_top_df))


# TODO 6.A (Scenario -- Regional Sales Report): write
# regional_sales_report(df). Given a DataFrame with "region" and
# "revenue" columns, return a Series of total revenue per region,
# sorted highest first.


# TODO 6.B (Scenario -- Interview Prep): write
# explain_groupby_pipeline() describing, in plain language, how
# groupby() + an aggregate + sort_values() combine to build a "top N"
# report.
