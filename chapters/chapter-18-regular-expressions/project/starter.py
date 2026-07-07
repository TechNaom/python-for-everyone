"""
Chapter 18 Project: Resume Keyword Scanner -- starter.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tool: the `re` module.
Fill in the numbered TODOs below. Want to see one finished version first?
Run solution.py (also from inside this folder).
"""

import re

SAMPLE_RESUME_FILE = "sample_resume.txt"

SAMPLE_RESUME_TEXT = """Jordan Alvarez
Email: jordan.alvarez@example.com
Phone: 555-241-8890

SUMMARY
Backend-focused software engineer with 4 years of experience building
Python services and REST APIs. Comfortable with SQL, Git, and automated
testing.

SKILLS
Python, SQL, Git, Docker, REST APIs, Unit Testing, AWS, Linux

EXPERIENCE
Backend Engineer, Northwind Logistics (2022-2026)
- Built internal REST APIs in Python and Flask.
- Wrote unit tests with pytest, raising coverage from 40% to 85%.
- Automated deployment scripts using Git hooks and Docker.

Junior Developer, Cascade Software (2020-2022)
- Maintained SQL reporting scripts for the finance team.
- Contributed to a Linux-based build pipeline.

EDUCATION
B.S. Computer Science, State University, 2020

You can also reach me at jordan.a.alvarez@gmail.com or by cell at
(555) 903-2214 if the number above doesn't work.
"""

# TODO 1: Compile two module-level patterns, EMAIL_PATTERN and
# PHONE_PATTERN, with re.compile(). EMAIL_PATTERN should match
# r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}" (an email shape). PHONE_PATTERN should
# match r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}" (a phone number, with or
# without parentheses/dashes/dots/spaces).
EMAIL_PATTERN = None
PHONE_PATTERN = None


class ResumeScanner:
    """Scans one resume's raw text for required keywords and contact info."""

    def __init__(self, text):
        self.text = text

    def find_emails(self):
        """Return every email-shaped match found in the resume text."""
        # TODO 2: Return EMAIL_PATTERN.findall(self.text).
        pass

    def find_phones(self):
        """Return every phone-number-shaped match found in the resume text."""
        # TODO 3: Return PHONE_PATTERN.findall(self.text).
        pass

    def find_keyword_matches(self, keywords):
        """Return the subset of `keywords` that appear in the resume text as
        a standalone word, case-insensitively."""
        # TODO 4: Build an empty `found` list. Loop over `keywords`; for each
        # one, compile a pattern with re.compile(r"\b" + re.escape(keyword) +
        # r"\b", re.IGNORECASE) and, if pattern.search(self.text) finds a
        # match, append the original keyword to `found`. Return `found`.
        pass

    def match_report(self, keywords):
        """Return a dict summarizing which required keywords were found,
        which were missing, and the percentage matched."""
        # TODO 5: Call self.find_keyword_matches(keywords) to get `found`.
        # Build `missing` as every keyword in `keywords` not in `found`.
        # Compute `percent` as len(found) / len(keywords) * 100 (guard
        # against an empty `keywords` list to avoid dividing by zero).
        # Return {"found": found, "missing": missing, "percent": percent}.
        pass


def generate_sample_resume(path=SAMPLE_RESUME_FILE):
    """Write the built-in sample resume to `path`."""
    # TODO 6: Open `path` for writing using a `with` statement (as f), and
    # write SAMPLE_RESUME_TEXT to it. Return `path`.
    pass


def load_resume(path):
    """Read and return the full text of the resume file at `path`."""
    # TODO 7: Open `path` for reading using a `with` statement (as f), and
    # return f.read().
    pass


def prompt_keywords():
    """Ask the user for a comma-separated list of required skills and
    return them as a clean list of strings, with blanks stripped out."""
    # TODO 8: input() a prompt asking for comma-separated skills. Split the
    # result on "," and return a list of each piece .strip()'d, skipping
    # any piece that's empty after stripping.
    pass


# --- Session state ---
print("=== Resume Keyword Scanner ===")
resume_ready = False
resume_text = ""

while True:
    print()
    print("1. Generate sample resume file")
    print("2. Load resume from file")
    print("3. Scan resume for required skills")
    print("4. Extract contact info (email & phone)")
    print("5. Quit")
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print()
        # TODO 9: Call generate_sample_resume() to get `path`, call
        # load_resume(path) to set `resume_text`, set `resume_ready = True`,
        # and print a confirmation message including `path`.
        pass

    elif choice == "2":
        print()
        if not resume_ready:
            pass
        # TODO 10: input() a prompt for a file path. In a try/except
        # FileNotFoundError block, call load_resume(path) to set
        # `resume_text`, set `resume_ready = True`, and print a confirmation
        # -- in the except block, print a friendly "could not find" message.

    elif choice == "3":
        print()
        if not resume_ready:
            print("No resume loaded yet -- choose option 1 or 2 first.")
            continue
        # TODO 11: Call prompt_keywords() to get `keywords`. If it's empty,
        # print a message and `continue`. Otherwise build a ResumeScanner
        # with `resume_text`, call .match_report(keywords) to get `report`,
        # and print the found/missing skills and the percentage matched.
        pass

    elif choice == "4":
        print()
        if not resume_ready:
            print("No resume loaded yet -- choose option 1 or 2 first.")
            continue
        # TODO 12: Build a ResumeScanner with `resume_text`, call
        # .find_emails() and .find_phones(), and print both results.
        pass

    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
