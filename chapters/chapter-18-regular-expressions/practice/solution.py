"""
Chapter 18 Practice Bank: Regular Expressions -- reference solution.
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py
"""

import re

# ============================================================
# Topic 1: match() / search() / fullmatch()
# ============================================================

# TODO 1.1
result = re.match(r"\d+", "42 apples")
print(result.group())

# TODO 1.2
result = re.search(r"\d+", "there are 42 apples")
print(result.group())

# TODO 1.3
valid = re.fullmatch(r"\d+", "42")
invalid = re.fullmatch(r"\d+", "42 apples")
print(valid)
print(invalid)

# TODO 1.4
for word in ["cat", "concatenate", "category"]:
    if re.match(r"cat", word):
        print(f"{word}: starts with cat")
    else:
        print(f"{word}: does not start with cat")

# TODO 1.5 (Debug the Code)
# Bug: re.match() only checks the start of the string, but the digits in
# "total: 99 items" don't start at position 0. Fix: use re.search() instead,
# which scans the whole string.
result = re.search(r"\d+", "total: 99 items")
print(result.group())

# TODO 1.A (Scenario -- Validating a Username Field on a Signup Form)
def is_valid_username(username):
    return re.fullmatch(r"[A-Za-z0-9_]{3,16}", username) is not None


for name in ["ann23", "a", "way_too_long_for_a_username_field", "bad!name", "ok_name_1"]:
    print(f"{name}: {is_valid_username(name)}")

# TODO 1.B (Scenario -- Interview Prep)
def explain_match_vs_search():
    return (
        "re.match() only checks whether the pattern matches starting at "
        "position 0 of the string -- if the target text appears anywhere "
        "else, match() returns None even though the text is genuinely "
        "there. re.search() scans the entire string and succeeds on the "
        "first match found anywhere, which is why search() is almost "
        "always the right default when looking for a pattern that could "
        "appear anywhere in real, messy text -- match() is really only "
        "appropriate when the pattern is specifically expected to be at "
        "the very beginning, like checking a string's prefix."
    )


print(explain_match_vs_search())


# ============================================================
# Topic 2: findall() & finditer()
# ============================================================

# TODO 2.1
prices = re.findall(r"\$\d+", "Items cost $5, $12, and $100")
print(prices)

# TODO 2.2
text = "cat hat bat mat"
for match in re.finditer(r"\w+at", text):
    print(match.group(), match.start())

# TODO 2.3
words = re.findall(r"\b\w+\b", "one two three")
print(len(words))

# TODO 2.4
hashtags = re.findall(r"#\w+", "Loving this #sunset and #beachlife today")
print(hashtags)

# TODO 2.5 (Debug the Code)
# Bug: the pattern r"\d" only matches ONE digit at a time, so "100" splits
# into three separate single-digit matches instead of one number. Fix: add
# a + quantifier, r"\d+", so runs of digits are matched as a whole.
numbers = re.findall(r"\d+", "order 7, then 22, then 100")
print(numbers)

# TODO 2.A (Scenario -- Extracting Every Error Code From a Support Ticket)
def extract_error_codes(ticket_text):
    return re.findall(r"ERR-\d{4}", ticket_text)


ticket = "User reported ERR-4021 twice, then ERR-9987 once."
print(extract_error_codes(ticket))

# TODO 2.B (Scenario -- Interview Prep)
def explain_findall_vs_finditer():
    return (
        "re.findall() returns every match as a plain list of strings -- "
        "simple and usually exactly what's needed when only the matched "
        "text itself matters. re.finditer() returns every match as an "
        "iterator of Match objects instead, which costs one extra step "
        "(looping over it rather than getting a ready-made list) but pays "
        "it back with each match's position in the original string via "
        ".start()/.end(), plus access to any groups the pattern defined -- "
        "reach for finditer() specifically when position or per-match "
        "group data is needed, and findall() when only the matched text "
        "itself is needed."
    )


print(explain_findall_vs_finditer())


# ============================================================
# Topic 3: Character Classes, Quantifiers & Anchors
# ============================================================

# TODO 3.1
vowel_count = len(re.findall(r"[aeiouAEIOU]", "The Quick Brown Fox"))
print(vowel_count)

# TODO 3.2
optional_matches = re.findall(r"colou?r", "favorite color and favourite colour")
print(optional_matches)

# TODO 3.3
codes = re.findall(r"[A-Z]{2}\d{3}", "Codes AB123 and CD456 and E78 are listed")
print(codes)

# TODO 3.4
full_lines = ["12345", "abc12", "999999", "42"]
for line in full_lines:
    if re.fullmatch(r"^\d{3,5}$", line):
        print(f"{line}: valid")
    else:
        print(f"{line}: invalid")

# TODO 3.5 (Debug the Code)
# Bug: the period between "3" and "14" is unescaped, so it matches ANY
# character in that position, not just a literal decimal point. Fix: escape
# it as \. so only an actual period counts.
matches = re.findall(r"3\.14", "the value is 3.14 not 3x14 or 3y14")
print(matches)

# TODO 3.A (Scenario -- Validating a Simple Password Policy)
def is_strong_password(password):
    return re.fullmatch(r"\w{8,}", password) is not None


for pw in ["short", "longenoughpassword", "12345678"]:
    print(f"{pw}: {is_strong_password(pw)}")

# TODO 3.B (Scenario -- Interview Prep)
def explain_quantifiers_and_anchors():
    return (
        "A quantifier controls how many times the piece right before it "
        "can repeat -- * for zero or more, + for one or more, ? for zero "
        "or one (optional), and {m,n} for a specific range -- while an "
        "anchor like ^ or $ matches a position in the string rather than "
        "an actual character, specifically the start or end. Combining "
        "both, ^\\d+$ only matches a string that is nothing but digits "
        "from its very first character to its very last, which is exactly "
        "why a validation pattern almost always needs both anchors -- "
        "without them, a pattern like \\d+ would happily match a string "
        "that has valid digits buried inside otherwise invalid text."
    )


print(explain_quantifiers_and_anchors())


# ============================================================
# Topic 4: Groups & Named Groups
# ============================================================

# TODO 4.1
match = re.match(r"(\w+)@(\w+)\.com", "alice@example.com")
print(match.group(1))
print(match.group(2))

# TODO 4.2
match = re.match(r"(?P<user>\w+)@(?P<domain>\w+)\.com", "bob@company.com")
print(match.group("user"))
print(match.group("domain"))
print(match.groupdict())

# TODO 4.3
match = re.match(r"(\d{2}):(\d{2}):(\d{2})", "14:22:10")
print(match.groups())

# TODO 4.4
matches = re.finditer(r"(?P<code>[A-Z]{3})-(?P<num>\d{3})", "REF-101 and REF-202")
for m in matches:
    print(m.groupdict())

# TODO 4.5 (Debug the Code)
# Bug: the named group is written (?<year>...) instead of the correct
# (?P<year>...) syntax -- Python's re module requires the P. Fix: add the P.
match = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})", "2026-07")
print(match.group("year"))

# TODO 4.A (Scenario -- Parsing a "Last, First" Name Field)
def split_last_first(full_name):
    match = re.match(r"(?P<last>\w+),\s*(?P<first>\w+)", full_name)
    return match.groupdict()


print(split_last_first("Papasani, Manohar"))

# TODO 4.B (Scenario -- Interview Prep)
def explain_groups_purpose():
    return (
        "Groups let a single match be broken into labeled, individually "
        "retrievable pieces instead of just one undivided blob of matched "
        "text. Wrapping part of a pattern in parentheses, (...), doesn't "
        "change what gets matched at all -- it just makes that specific "
        "piece separately accessible afterward via .group(n), numbered "
        "left to right starting at 1. Named groups, (?P<name>...), do the "
        "exact same thing but let that piece be retrieved by a meaningful "
        "name via .group('name') instead of a position number, which "
        "reads far more clearly and survives a pattern being reordered "
        "later without breaking."
    )


print(explain_groups_purpose())


# ============================================================
# Topic 5: re.sub() & re.split()
# ============================================================

# TODO 5.1
masked = re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", "XXXX-XXXX-XXXX-XXXX", "Card: 1234-5678-9012-3456")
print(masked)

# TODO 5.2
cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", "Hello!!! World??? #Python$$$")
print(cleaned)

# TODO 5.3
parts = re.split(r"\s*;\s*", "apple; banana ;cherry;  date")
print(parts)

# TODO 5.4
compact = re.sub(r"-{2,}", "-", "too---many----dashes")
print(compact)

# TODO 5.5 (Debug the Code)
# Bug: the arguments to re.sub() are in the wrong order -- it's supposed to
# be re.sub(pattern, replacement, text), but replacement and text were
# swapped, replacing occurrences of the ORIGINAL text with the pattern
# string, which is backwards. Fix: put the pattern first, then the
# replacement, then the text.
result = re.sub(r"\d+", "#", "Item 7 and item 42")
print(result)

# TODO 5.A (Scenario -- Redacting Social Security Numbers From a Document)
def redact_ssns(document_text):
    return re.sub(r"\d{3}-\d{2}-\d{4}", "XXX-XX-XXXX", document_text)


print(redact_ssns("SSN on file: 123-45-6789 for this applicant."))

# TODO 5.B (Scenario -- Interview Prep)
def explain_sub_split_benefit():
    return (
        "str.replace() and str.split() only recognize one fixed, exact "
        "target string or separator -- they can't describe 'any run of "
        "digits' or 'a comma or one or more spaces, in any mix' as a "
        "single rule. re.sub() and re.split() accept a full pattern "
        "instead of a fixed string, so re.sub() can mask or replace an "
        "entire category of matching text in one call (every phone number, "
        "every SSN), and re.split() can break text apart on multiple "
        "different separator styles in a single call, which is exactly "
        "the kind of messy, inconsistent real-world text a fixed-string "
        "method could never fully handle."
    )


print(explain_sub_split_benefit())


# ============================================================
# Topic 6: Compiled Patterns
# ============================================================

# TODO 6.1
digit_pattern = re.compile(r"\d+")
print(digit_pattern.findall("a1 b22 c333"))

# TODO 6.2
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
lines = ["contact: ann@example.com", "no email here", "reach bob@company.org"]
for line in lines:
    match = email_pattern.search(line)
    if match:
        print(match.group())

# TODO 6.3
word_pattern = re.compile(r"\b\w{5,}\b")
print(word_pattern.findall("short words versus longer words here"))

# TODO 6.4
ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
log_lines = ["request from 192.168.1.1 succeeded", "no ip in this line"]
found = [ip_pattern.search(line).group() for line in log_lines if ip_pattern.search(line)]
print(found)

# TODO 6.5 (Debug the Code)
# Bug: the code calls re.compile() correctly, but then calls the old
# module-level re.search(pattern_string, text) instead of using the
# compiled object's own .search() method, defeating the point of
# compiling. Fix: call compiled_pattern.search(text) instead.
compiled_pattern = re.compile(r"\d+")
result = compiled_pattern.search("value: 88")
print(result.group())

# TODO 6.A (Scenario -- Scanning Many Log Lines for the Same Error Pattern)
def count_error_lines(log_lines):
    error_pattern = re.compile(r"\[ERROR\]")
    return sum(1 for line in log_lines if error_pattern.search(line))


sample_lines = ["[INFO] ok", "[ERROR] failed", "[INFO] ok", "[ERROR] failed again"]
print(count_error_lines(sample_lines))

# TODO 6.B (Scenario -- Interview Prep)
def explain_compile_benefit():
    return (
        "re.compile(pattern) processes a pattern string once into a "
        "reusable compiled pattern object, which then has its own "
        ".search()/.match()/.findall() methods that behave exactly like "
        "the module-level re.search(pattern, text) versions, just without "
        "needing to pass (and re-parse) the raw pattern string on every "
        "single call. For a pattern used only once, compiling first adds "
        "little value, but for a pattern applied across many lines of a "
        "file or many calls in a loop -- exactly the log-scanning and "
        "resume-scanning cases this chapter keeps coming back to -- "
        "compiling it once and reusing the compiled object is both more "
        "efficient and clearer about the fact that the same pattern is "
        "meant to be reused."
    )


print(explain_compile_benefit())


# ============================================================
# Topic 7: Bringing It Together -- Greedy Matching, Raw Strings & Flags
# ============================================================

# TODO 7.1
greedy = re.findall(r'".*"', 'She said "hello" and then "goodbye"')
non_greedy = re.findall(r'".*?"', 'She said "hello" and then "goodbye"')
print(greedy)
print(non_greedy)

# TODO 7.2
raw_pattern = r"\d+\.\d+"
print(re.findall(raw_pattern, "version 3.14 and 2.7"))

# TODO 7.3
case_insensitive = re.findall(r"error", "Error: ERROR: error occurred", re.IGNORECASE)
print(case_insensitive)

# TODO 7.4
multiline_text = "line one\nline two\nline three"
line_starts = re.findall(r"^line", multiline_text, re.MULTILINE)
print(len(line_starts))

# TODO 7.5 (Debug the Code)
# Bug: the pattern used a greedy .* between quotes, so it grabbed everything
# from the FIRST quote to the LAST quote as one giant match instead of two
# separate quoted phrases. Fix: change .* to .*? to make it non-greedy.
quoted = re.findall(r'"(.*?)"', 'The signs said "stop" and "go" clearly')
print(quoted)

# TODO 7.A (Scenario -- A Log-Scanning Tool Combining Everything)
def scan_log_for_errors(log_text):
    error_pattern = re.compile(r"(?P<time>\d{2}:\d{2}:\d{2})\s+\[ERROR\]\s+(?P<message>.+)", re.IGNORECASE)
    results = []
    for line in log_text.split("\n"):
        match = error_pattern.search(line)
        if match:
            results.append(match.groupdict())
    return results


sample_log = "10:15:00 [INFO] all good\n10:15:05 [error] disk full\n10:15:10 [ERROR] timeout"
print(scan_log_for_errors(sample_log))

# TODO 7.B (Scenario -- Interview Prep)
def explain_regex_gotchas():
    return (
        "Three specific things trip up almost every regex beginner at "
        "least once. First, quantifiers are greedy by default, matching "
        "as much text as possible -- a pattern meant to grab the shortest "
        "text between two delimiters needs the non-greedy versions, *? "
        "or +?, or it will stretch from the first delimiter all the way "
        "to the very last one instead of stopping at the nearest one. "
        "Second, a pattern string should almost always be written as a "
        "raw string, r'...', since without it Python's own "
        "escape-sequence rules can silently corrupt backslash sequences "
        "like \\d or \\b before re ever sees them. Third, matching is "
        "case-sensitive by default and ^/$ only anchor to the whole "
        "string by default, not each line -- re.IGNORECASE and "
        "re.MULTILINE exist specifically to change those two defaults "
        "when the situation calls for it."
    )


print(explain_regex_gotchas())
