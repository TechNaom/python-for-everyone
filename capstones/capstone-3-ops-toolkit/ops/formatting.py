"""
ops.formatting -- shared, terminal-agnostic string-building helpers.

Every domain (logs, scan, fetch) hands its results to cli.py, and cli.py
turns them into strings using *these* helpers before printing -- so
`ops logs analyze`, `ops scan resume`, and `ops fetch weather` all share
one alignment/spacing convention instead of each inventing its own.

Nothing in this module calls print() -- it only returns strings. That
keeps it consistent with the "engine modules never touch the terminal"
rule; cli.py is still the only place an actual print() happens.
"""

from __future__ import annotations


def format_table(rows: list[list], headers: list[str]) -> str:
    """Return rows formatted as a simple, left-aligned, space-padded table.

    `rows` is a list of row tuples/lists; every cell is converted with
    str(). If `rows` is empty, returns a "(no rows)" placeholder line
    under the header so callers don't need a separate empty-state check.
    """
    str_rows = [[str(cell) for cell in row] for row in rows]
    widths = [len(h) for h in headers]
    for row in str_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    lines = []
    header_line = "  ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    lines.append(header_line)
    lines.append("  ".join("-" * w for w in widths))

    if not str_rows:
        lines.append("(no rows)")
    else:
        for row in str_rows:
            lines.append("  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))

    return "\n".join(lines)


def format_kv(pairs: list[tuple[str, object]]) -> str:
    """Return a list of (label, value) pairs as aligned "label: value" lines."""
    if not pairs:
        return "(nothing to show)"
    width = max(len(str(label)) for label, _ in pairs)
    return "\n".join(f"{str(label).ljust(width)} : {value}" for label, value in pairs)


def format_list(items: list, empty_message: str = "(none)") -> str:
    """Return a bulleted list of items, or `empty_message` if items is empty."""
    if not items:
        return empty_message
    return "\n".join(f"  - {item}" for item in items)
