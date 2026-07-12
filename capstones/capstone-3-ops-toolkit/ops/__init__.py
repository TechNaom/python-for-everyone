"""ops: a small, packaged ops toolkit combining log analysis, resume
scanning, and a mocked fetch pipeline behind one command-line interface."""

__version__ = "1.0.0"


class OpsError(Exception):
    """Raised for any user-facing "not found" / "bad input" condition
    across all three domains (logs, scan, fetch).

    Shared across ops/logs.py, ops/scan.py, and ops/fetch.py so that
    cli.py has exactly one exception-handling convention to deal with:
    engine modules raise either a plain FileNotFoundError (for a
    missing file, the natural exception open() already raises) or this
    OpsError (for anything else -- bad city, bad index, empty input,
    corrupt data) -- never a silent None return or a bespoke exception
    type per module.
    """
