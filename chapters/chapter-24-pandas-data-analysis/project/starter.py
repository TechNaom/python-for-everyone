"""
Chapter 24 Project: Sales-Data Dashboard (CSV In, Insights Out)
See README.md in this folder for full instructions.
Run this from inside the project/ folder: python3 starter.py

Install pandas first if you haven't: pip install pandas

This is a menu-driven mini-app, like Chapter 23's project, but built on
top of a pandas DataFrame loaded from CSV-format text instead of a
raw NumPy array.
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


# TODO 1: Write load_sales(). Parse SALES_CSV with pd.read_csv() on a
# StringIO wrapper, add a computed "revenue" column equal to
# units_sold * unit_price, and return the resulting DataFrame.


# TODO 2: Write total_revenue(df). Return the whole "revenue" column's
# sum as a plain Python int.


# TODO 3: Write top_products(df). Group by "product", sum "revenue",
# sort descending, and return the result (a pandas Series is fine).


# TODO 4: Write top_regions(df). Same as top_products(), but grouped by
# "region" instead of "product".


# TODO 5: Write underperforming_sales(df, threshold=600). Return only
# the rows (as a DataFrame) where "revenue" is strictly less than
# threshold, using boolean filtering.


# TODO 6: Write format_report(df, threshold=600). Build and return one
# multi-line string report combining:
#   - "=== Total Revenue ===" followed by "$X,XXX" (use an f-string
#     with a thousands separator: f"${total_revenue(df):,}")
#   - "=== Top Products by Revenue ===" followed by one line per
#     product from top_products(), formatted "Name: $X,XXX"
#   - "=== Top Regions by Revenue ===" followed by one line per region
#     from top_regions(), formatted "Name: $X,XXX"
#   - "=== Underperforming Line Items (revenue < $X) ===" followed by
#     one line per row from underperforming_sales(), formatted
#     "DATE PRODUCT REGION: $XXX" (or "(none)" if there are no rows)


def run():
    print("=== Sales-Data Dashboard ===")
    print()
    df = load_sales()
    print(format_report(df))


if __name__ == "__main__":
    run()
