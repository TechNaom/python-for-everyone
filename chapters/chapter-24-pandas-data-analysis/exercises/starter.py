"""
Chapter 24 Exercises: Pandas for Data Analysis
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every task here uses pandas directly -- make sure it's installed first:
pip install pandas
"""

import pandas as pd


# TODO 1: Write make_sales_df(products, revenues). Given two plain
# Python lists (product names, revenues), return a DataFrame with
# columns "product" and "revenue".


# TODO 2: Write revenue_summary(df). Return a dict with keys "total",
# "average", "max" holding the "revenue" column's sum, mean, and max.


# TODO 3: Write big_sales(df, threshold=1000). Return only the rows
# where "revenue" is strictly greater than threshold, using boolean
# filtering (no loop).


# TODO 4: Write add_tax_column(df, tax_rate). Return a NEW DataFrame
# with an added "revenue_with_tax" column, computed as
# revenue * (1 + tax_rate).


# TODO 5: Write get_row_by_label(df, label) using .loc[], and
# get_row_by_position(df, position) using .iloc[].


# TODO 6: Write clean_revenue(df). Given a DataFrame whose "revenue"
# column may contain missing values, return a NEW DataFrame with those
# missing values filled in with 0.


# TODO 7: Write total_by_region(df). Given a DataFrame with "region"
# and "revenue" columns, return one total revenue per region using
# groupby().


# TODO 8: Write top_products(df, n=3). Given a DataFrame with "product"
# and "revenue" columns, return the top n rows by revenue, highest
# first.


# TODO 9 (Debug the Code): this is supposed to return each REGION's
# total revenue, but it groups by "product" instead of "region". Find
# and fix it.
def region_totals(df):
    return df.groupby("product")["revenue"].sum()


demo_df = pd.DataFrame({
    "region": ["East", "West", "East"],
    "product": ["Widget", "Gadget", "Gizmo"],
    "revenue": [1200, 950, 1830],
})
print(region_totals(demo_df))
