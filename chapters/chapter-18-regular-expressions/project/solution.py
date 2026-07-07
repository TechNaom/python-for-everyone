"""
Chapter 18 Project: Resume Keyword Scanner -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tool: the `re` module.
A ResumeScanner class scans one resume's raw text for required-skill
keywords (using word-boundary-anchored, case-insensitive patterns so
"SQL" matches "sql" but not "MySQL"), and separately extracts contact
info (emails and phone numbers) using compiled patterns -- exactly the
"scan hundreds of resumes for a candidate's email and phone number"
scenario this chapter's lesson opened with.
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

# Compiled once at module load, since both patterns get reused across
# every scan -- exactly the re.compile() use case from Sub-topic 6.
EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}")
PHONE_PATTERN = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")


class ResumeScanner:
    """Scans one resume's raw text for required keywords and contact info."""

    def __init__(self, text):
        self.text = text

    def find_emails(self):
        """Return every email-shaped match found in the resume text."""
        return EMAIL_PATTERN.findall(self.text)

    def find_phones(self):
        """Return every phone-number-shaped match found in the resume text."""
        return PHONE_PATTERN.findall(self.text)

    def find_keyword_matches(self, keywords):
        """Return the subset of `keywords` that appear in the resume text as
        a standalone word, case-insensitively. Word boundaries (\\b) matter
        here -- without them, a keyword like "SQL" would also match as a
        substring of an unrelated word, which findall()/search() alone
        can't rule out."""
        found = []
        for keyword in keywords:
            pattern = re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE)
            if pattern.search(self.text):
                found.append(keyword)
        return found

    def match_report(self, keywords):
        """Return a dict summarizing which required keywords were found,
        which were missing, and the percentage matched."""
        found = self.find_keyword_matches(keywords)
        missing = [kw for kw in keywords if kw not in found]
        percent = (len(found) / len(keywords) * 100) if keywords else 0.0
        return {"found": found, "missing": missing, "percent": percent}


def generate_sample_resume(path=SAMPLE_RESUME_FILE):
    """Write the built-in sample resume to `path`, so the rest of the menu
    has something real to scan."""
    with open(path, "w") as f:
        f.write(SAMPLE_RESUME_TEXT)
    return path


def load_resume(path):
    """Read and return the full text of the resume file at `path`."""
    with open(path, "r") as f:
        return f.read()


def prompt_keywords():
    """Ask the user for a comma-separated list of required skills and
    return them as a clean list of strings, with blanks stripped out."""
    raw = input("Enter required skills, comma-separated (e.g. Python, SQL, Docker): ")
    return [kw.strip() for kw in raw.split(",") if kw.strip()]


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
        path = generate_sample_resume()
        resume_text = load_resume(path)
        resume_ready = True
        print(f"Wrote sample resume to {path}.")

    elif choice == "2":
        print()
        path = input("Path to resume .txt file: ").strip()
        try:
            resume_text = load_resume(path)
            resume_ready = True
            print(f"Loaded resume from {path}.")
        except FileNotFoundError:
            print(f"Could not find a file at '{path}'.")

    elif choice == "3":
        print()
        if not resume_ready:
            print("No resume loaded yet -- choose option 1 or 2 first.")
            continue
        keywords = prompt_keywords()
        if not keywords:
            print("Please enter at least one keyword.")
            continue
        scanner = ResumeScanner(resume_text)
        report = scanner.match_report(keywords)
        print(f"Matched {len(report['found'])}/{len(keywords)} required skills "
              f"({report['percent']:.0f}%).")
        print(f"  Found: {', '.join(report['found']) if report['found'] else 'none'}")
        print(f"  Missing: {', '.join(report['missing']) if report['missing'] else 'none'}")

    elif choice == "4":
        print()
        if not resume_ready:
            print("No resume loaded yet -- choose option 1 or 2 first.")
            continue
        scanner = ResumeScanner(resume_text)
        emails = scanner.find_emails()
        phones = scanner.find_phones()
        print(f"Emails found: {emails if emails else 'none'}")
        print(f"Phone numbers found: {phones if phones else 'none'}")

    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
