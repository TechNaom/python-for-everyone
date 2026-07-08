"""
Chapter 24 Project: Sales-Data Dashboard (CSV In, Insights Out) -- reference solution.
Run this from inside the project/ folder: python3 solution.py
"""

import pandas as pd
from io import StringIO

SALES_CSV = """date,product,region,units_sold,unit_price
2026-01-05,Widget,East,40,30
2026-01-05,Gadget,West,25,38
2026-01-06,Gizmo,East,61,30
2026-01-06,Widget,West,18,30
2026-01-07,Gadget,East,33,38
2026-01-07,Gizmo,West,9,30
2026-01-08,Widget,East,52,30
2026-01-08,Gadget,West,15,38
2026-01-09,Gizmo,East,44,30
2026-01-09,Widget,West,27,30
"""


# TODO 1
def load_sales():
    df = pd.read_csv(StringIO(SALES_CSV))
    df["revenue"] = df["units_sold"] * df["unit_price"]
    return df


# TODO 2
def total_revenue(df):
    return int(df["revenue"].sum())


# TODO 3
def top_products(df):
    return df.groupby("product")["revenue"].sum().sort_values(ascending=False)


# TODO 4
def top_regions(df):
    return df.groupby("region")["revenue"].sum().sort_values(ascending=False)


# TODO 5
def underperforming_sales(df, threshold=600):
    return df[df["revenue"] < threshold]


# TODO 6
def format_report(df, threshold=600):
    lines = []

    lines.append("=== Total Revenue ===")
    lines.append(f"${total_revenue(df):,}")
    lines.append("")

    lines.append("=== Top Products by Revenue ===")
    for product, revenue in top_products(df).items():
        lines.append(f"{product}: ${int(revenue):,}")
    lines.append("")

    lines.append("=== Top Regions by Revenue ===")
    for region, revenue in top_regions(df).items():
        lines.append(f"{region}: ${int(revenue):,}")
    lines.append("")

    lines.append(f"=== Underperforming Line Items (revenue < ${threshold:,}) ===")
    weak = underperforming_sales(df, threshold)
    if len(weak) == 0:
        lines.append("(none)")
    else:
        for _, row in weak.iterrows():
            lines.append(f"{row['date']} {row['product']} {row['region']}: ${int(row['revenue']):,}")

    return "\n".join(lines)


def run():
    print("=== Sales-Data Dashboard ===")
    print()
    df = load_sales()
    print(format_report(df))


if __name__ == "__main__":
    run()
