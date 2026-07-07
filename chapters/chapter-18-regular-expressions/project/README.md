# Chapter 18 Project: Resume Keyword Scanner

A menu-driven resume scanner built **around this chapter's core tool** as
its organizing principle &mdash; a `ResumeScanner` class scans one resume's
raw text for required-skill keywords using word-boundary-anchored,
case-insensitive patterns (so `"SQL"` matches `"sql"` but not the `"SQL"`
hiding inside `"MySQL"`), and separately extracts contact info (emails and
phone numbers) using two module-level compiled patterns &mdash; exactly the
"scan hundreds of resumes for a candidate's email and phone number"
scenario this chapter's lesson opened with.

## What you'll build

A `ResumeScanner` class plus a menu loop offering five real operations:

1. Generate sample resume file
2. Load resume from file
3. Scan resume for required skills
4. Extract contact info (email & phone)
5. Quit

The scanner itself is built from these pieces:

- `EMAIL_PATTERN` / `PHONE_PATTERN` &mdash; two patterns compiled once at
  module load with `re.compile()`, since both get reused across every
  scan (exactly the `re.compile()` use case from Sub-topic 6).
  `EMAIL_PATTERN` matches `r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}"` (an
  email shape); `PHONE_PATTERN` matches
  `r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"` (a phone number, with or
  without parentheses, dashes, dots, or spaces).
- `ResumeScanner.find_emails()` / `.find_phones()` &mdash; call
  `.findall()` on the two compiled patterns against the resume's raw
  text, returning every email-shaped and phone-shaped match found.
- `ResumeScanner.find_keyword_matches(keywords)` &mdash; for each
  required keyword, compiles a fresh pattern
  `r"\b" + re.escape(keyword) + r"\b"` with the `re.IGNORECASE` flag,
  and checks whether it `.search()`es the resume text. The word
  boundaries (`\b`) matter here: without them, a keyword like `"SQL"`
  would also match as a substring of an unrelated word like `"MySQL"`,
  something plain `in`/`.find()` on the text can't rule out. `re.escape()`
  keeps a keyword containing regex-special characters (like `"C++"`)
  from accidentally being interpreted as pattern syntax.
- `ResumeScanner.match_report(keywords)` &mdash; calls
  `find_keyword_matches()` to get the found list, computes the missing
  list as everything in `keywords` not found, and the match percentage,
  returning all three as one dict.

Every menu option that needs a resume loaded first checks `resume_ready`
and prints a friendly message instead of crashing if nothing has been
loaded yet.

Example run:

```
=== Resume Keyword Scanner ===

1. Generate sample resume file
2. Load resume from file
3. Scan resume for required skills
4. Extract contact info (email & phone)
5. Quit
Choose an option (1-5): 1

Wrote sample resume to sample_resume.txt.

1. Generate sample resume file
2. Load resume from file
3. Scan resume for required skills
4. Extract contact info (email & phone)
5. Quit
Choose an option (1-5): 3

Enter required skills, comma-separated (e.g. Python, SQL, Docker): Python, SQL, Docker, Kubernetes
Matched 3/4 required skills (75%).
  Found: Python, SQL, Docker
  Missing: Kubernetes

1. Generate sample resume file
2. Load resume from file
3. Scan resume for required skills
4. Extract contact info (email & phone)
5. Quit
Choose an option (1-5): 4

Emails found: ['jordan.alvarez@example.com', 'jordan.a.alvarez@gmail.com']
Phone numbers found: ['555-241-8890', '(555) 903-2214']

1. Generate sample resume file
2. Load resume from file
3. Scan resume for required skills
4. Extract contact info (email & phone)
5. Quit
Choose an option (1-5): 5

Goodbye!
```

Notice that the sample resume deliberately has *two* email addresses and
*two* phone numbers, in two different formats each (`555-241-8890` vs.
`(555) 903-2214`) &mdash; `PHONE_PATTERN`'s optional parentheses and mixed
separator characters are exactly what let a single pattern catch both
formats in one pass, instead of needing a separate pattern per format.

## How to run it

```bash
cd chapters/chapter-18-regular-expressions/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder) &mdash; option 1 will (re)generate `sample_resume.txt` for you.

## Ideas to make it your own (optional stretch goals)

- Add a "batch scan" menu option that loads every `.txt` file in a folder
  and prints a one-line match-percentage summary per resume, so several
  candidates can be compared against the same required-skills list at
  once.
- Add a `find_years_of_experience()` method using a pattern like
  `r"(\d+)\+?\s+years?"` to pull a stated years-of-experience number out
  of the resume text, if present.
- Change `find_keyword_matches()` to also return *where* each matched
  keyword was found (via `finditer()` and `.start()`) instead of just
  whether it matched at all, so a caller could highlight matches in
  context.

## Why this project matters

Applicant Tracking Systems (ATS) &mdash; the software behind most large
companies' hiring pipelines &mdash; do almost exactly what this project
does at industrial scale: scan thousands of resumes for required
keywords and structured contact info before a human recruiter ever opens
one. Regex is the actual tool behind a large share of that scanning,
specifically because job requirements and resume formatting are never
perfectly consistent &mdash; a fixed-string search for `"5 years"` would
miss `"5+ years"` or `"five years"`, but a pattern can describe the whole
shape at once. The word-boundary technique in `find_keyword_matches()`
(`\bSQL\b` instead of a bare `SQL`) mirrors a genuinely common ATS
correctness bug in the wild: naive substring keyword-matching that
falsely credits a resume mentioning `"MySQL"` with the separate skill
`"SQL"`, or `"Java"` with a match against `"JavaScript"`.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Resume Keyword Scanner above is fully built out with a starter and
reference solution &mdash; the four ideas below are not. Each is a real,
grounded use case solvable with only what's been taught through Chapter 18
(everything through Chapter 17's generators/iterators/context managers,
plus this chapter's `re` module: `match()`/`search()`/`fullmatch()`,
`findall()`/`finditer()`, character classes, quantifiers, anchors, groups
& named groups, `re.sub()`/`re.split()`, and `re.compile()`). No starter
or solution files are provided on purpose &mdash; building one of these
unassisted is the point.

### 1. Log-File Anomaly Extractor

**Problem:** An operations engineer needs to scan a server's log file and
pull out every line that looks like a genuine problem &mdash; an error
level, a stack-trace-shaped line, or a request that took unusually long
&mdash; without manually reading every line of a file that could have
tens of thousands of entries.

**What it should do:** Build a function that streams a log file (reusing
Chapter 17's `stream_lines()`-style generator, one line at a time) and,
for each line, checks it against a compiled pattern like
`r"\[(ERROR|CRITICAL)\]"` using `.search()`, plus a second pattern that
pulls out a request duration like `r"(\d+)ms"` and flags any line where
that number exceeds a threshold. Menu options: generate a sample log
file, scan for error/critical lines, scan for slow requests over a
user-given millisecond threshold, and quit.

**Suggested approach:** Keep the two anomaly checks as two separately
compiled patterns (one for log level, one for duration) rather than
trying to cram both conditions into a single giant pattern &mdash; small,
named, purpose-specific patterns read far more clearly than one pattern
trying to do everything at once.

### 2. CSV/Text Data Cleaner

**Problem:** A dataset exported from an old system has inconsistent
formatting &mdash; phone numbers in five different formats, extra
whitespace, mismatched date separators (`/` vs. `-`) &mdash; and needs to
be normalized into one consistent shape before it can be loaded anywhere
else.

**What it should do:** Build a function that takes a raw string field and
normalizes it: strip and collapse repeated whitespace with
`re.sub(r"\s+", " ", text)`, normalize any phone number found (using
`PHONE_PATTERN`-style matching plus `re.sub()` to rewrite it into one
consistent `XXX-XXX-XXXX` shape), and normalize date separators with
`re.sub(r"[/-]", "-", date_text)`. Menu options: generate a sample messy
CSV file (via Chapter 13's `csv` module) with a few inconsistent fields,
clean it and write out a normalized version, show a before/after diff for
one row, and quit.

**Suggested approach:** Write one cleaning function per field type
(`clean_phone()`, `clean_date()`, `clean_whitespace()`) rather than one
do-everything function, then apply each to the right column while reading
rows with `csv.DictReader` &mdash; the same per-field, single-purpose
approach the log anomaly extractor above uses for its two separate
pattern checks.

### 3. Simple Form Validator

**Problem:** A signup form needs to validate several different field
types &mdash; username, email, password strength, phone number &mdash;
each with its own shape rules, before accepting the submission.

**What it should do:** Build a `FormValidator` class with one method per
field type, each using `re.fullmatch()` against a purpose-built pattern:
a username pattern (letters/digits/underscore, 3-20 characters,
`r"^\w{3,20}$"`), an email pattern (reusing this chapter's
`EMAIL_PATTERN`), and a password-strength check built from several
smaller `re.search()` calls (at least one digit, at least one uppercase
letter, minimum length) rather than one unreadable giant pattern. Menu
options: validate a username, validate an email, validate a password and
report which specific rule(s) it failed, and quit.

**Suggested approach:** For the password check specifically, resist the
urge to write one pattern that enforces every rule at once &mdash; several
separate `re.search()` calls, each checking one rule and reporting which
one failed, gives far more useful feedback to a real user than a single
opaque pass/fail from one dense pattern.

### 4. URL & Hashtag Extractor from Social Text

**Problem:** A social-media analytics tool needs to pull every URL and
every hashtag out of a batch of posts, to build a simple "most-mentioned
hashtag" or "most-linked domain" report.

**What it should do:** Build two functions, `extract_urls(text)` (pattern
along the lines of `r"https?://[^\s]+"`) and `extract_hashtags(text)`
(reusing this chapter's `r"#\w+"` pattern from the Coding Challenges),
plus a `extract_domain(url)` helper using a named group
(`r"https?://(?P<domain>[^/\s]+)"`) to pull just the domain out of a full
URL. Menu options: paste in a batch of sample post text, extract and
count every hashtag (most-mentioned first), extract and count every
domain linked, and quit.

**Suggested approach:** Build the hashtag/domain counts with a plain
dictionary (keyword or domain as the key, running count as the value),
the same accumulate-and-count pattern used throughout earlier chapters
&mdash; the new part here is only how the raw hashtags/URLs get pulled
out of the text in the first place, not how they get counted afterward.
