"""
ops.scan -- the resume-scanning engine, ported from Chapter 18's Resume
Keyword Scanner (ResumeScanner class, EMAIL_PATTERN, PHONE_PATTERN,
word-boundary-anchored keyword matching, match_report).

Deliberately kept separate from cli.py: no argparse, no print(). The
word-boundary anchoring (r"\\b" + re.escape(keyword) + r"\\b") is the
single most important detail carried over unchanged from Chapter 18 --
it's what stops a keyword like "SQL" from false-positive-matching
inside "MySQL". Losing it during a port like this one is exactly the
pitfall the capstone roadmap calls out, so it is preserved verbatim.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

from ops import OpsError

logger = logging.getLogger(__name__)

# Compiled once at module load, since both patterns get reused across
# every scan.
EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}")
PHONE_PATTERN = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")


class ResumeScanner:
    """Scans one resume's raw text for required keywords and contact info."""

    def __init__(self, text: str):
        self.text = text

    def find_emails(self) -> list[str]:
        """Return every email-shaped match found in the resume text."""
        return EMAIL_PATTERN.findall(self.text)

    def find_phones(self) -> list[str]:
        """Return every phone-number-shaped match found in the resume text."""
        return PHONE_PATTERN.findall(self.text)

    def find_keyword_matches(self, keywords: list[str]) -> list[str]:
        """Return the subset of `keywords` that appear in the resume text as
        a standalone word, case-insensitively. Word boundaries (\\b) matter
        here -- without them, a keyword like "SQL" would also match as a
        substring of an unrelated word like "MySQL", which findall()/
        search() alone can't rule out.
        """
        found = []
        for keyword in keywords:
            pattern = re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE)
            if pattern.search(self.text):
                found.append(keyword)
        return found

    def match_report(self, keywords: list[str]) -> dict:
        """Return a dict summarizing which required keywords were found,
        which were missing, and the percentage matched.

        Raises OpsError if `keywords` is empty -- an empty keyword list
        can't produce a meaningful match report.
        """
        if not keywords:
            raise OpsError("Please provide at least one keyword to scan for.")
        found = self.find_keyword_matches(keywords)
        missing = [kw for kw in keywords if kw not in found]
        percent = (len(found) / len(keywords) * 100) if keywords else 0.0
        return {"found": found, "missing": missing, "percent": percent}


def load_resume(path: str | Path) -> str:
    """Read and return the full text of the resume file at `path`.

    Raises FileNotFoundError if the file doesn't exist -- callers
    (cli.py) are expected to catch it themselves.
    """
    logger.debug("Loading resume text from %s", path)
    with open(path, "r") as f:
        text = f.read()
    logger.debug("Loaded %d character(s) of resume text", len(text))
    return text
