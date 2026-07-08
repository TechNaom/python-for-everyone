"""
Chapter 24 Exercises: Pandas for Data Analysis -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

import pandas as pd


# TODO 1
def make_sales_df(products, revenues):
    return pd.DataFrame({"product": products, "revenue": revenues})


print(make_sales_df(["Widget", "Gadget"], [1200, 950]))


# TODO 2
def revenue_summary(df):
    return {
        "total": df["revenue"].sum(),
        "average": df["revenue"].mean(),
        "max": df["revenue"].max(),
    }


print(revenue_summary(pd.DataFrame({"revenue": [1200, 950, 1830]})))


# TODO 3
def big_sales(df, threshold=1000):
    return df[df["revenue"] > threshold]


print(big_sales(pd.DataFrame({"product": ["Widget", "Gadget"], "revenue": [1200, 950]})))


# TODO 4
def add_tax_column(df, tax_rate):
    result = df.copy()
    result["revenue_with_tax"] = result["revenue"] * (1 + tax_rate)
    return result


print(add_tax_column(pd.DataFrame({"revenue": [1000, 2000]}), 0.08))


# TODO 5
def get_row_by_label(df, label):
    return df.loc[label]


def get_row_by_position(df, position):
    return df.iloc[position]


sample = pd.DataFrame({"product": ["Widget", "Gadget"], "revenue": [1200, 950]}, index=["r1", "r2"])
print(get_row_by_label(sample, "r2"))
print(get_row_by_position(sample, 1))


# TODO 6
def clean_revenue(df):
    result = df.copy()
    result["revenue"] = result["revenue"].fillna(0)
    return result


print(clean_revenue(pd.DataFrame({"revenue": [1200.0, None, 700.0]})))


# TODO 7
def total_by_region(df):
    return df.groupby("region")["revenue"].sum()


print(total_by_region(pd.DataFrame({"region": ["East", "West", "East"], "revenue": [1200, 950, 1830]})))


# TODO 8
def top_products(df, n=3):
    return df.sort_values("revenue", ascending=False).head(n)


print(top_products(pd.DataFrame({"product": ["Widget", "Gadget", "Gizmo", "Thing"], "revenue": [1200, 950, 1830, 400]}), n=2))


# TODO 9 (Debug the Code)
# Bug: grouped by "product" when the task asked for per-REGION totals.
def region_totals(df):
    return df.groupby("region")["revenue"].sum()


demo_df = pd.DataFrame({
    "region": ["East", "West", "East"],
    "product": ["Widget", "Gadget", "Gizmo"],
    "revenue": [1200, 950, 1830],
})
print(region_totals(demo_df))
