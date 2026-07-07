"""
Chapter 18 Practice Bank: Regular Expressions
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py
"""

import re

# ============================================================
# Topic 1: match() / search() / fullmatch()
# ============================================================

# TODO 1.1: Use re.match() with the pattern r"\d+" on the string
# "42 apples" and print the resulting match's .group().


# TODO 1.2: Use re.search() with the pattern r"\d+" on the string
# "there are 42 apples" and print the resulting match's .group().


# TODO 1.3: Use re.fullmatch() with the pattern r"\d+" on both "42" (should
# succeed) and "42 apples" (should fail). Print both results.


# TODO 1.4: Loop over ["cat", "concatenate", "category"] and use re.match()
# with the pattern r"cat" on each word, printing
# f"{word}: starts with cat" if it matches or
# f"{word}: does not start with cat" if it doesn't.


# TODO 1.5 (Debug the Code): this is supposed to find the number in
# "total: 99 items", but re.match() only checks the very start of the
# string, and the digits aren't at position 0 here, so it raises an
# AttributeError when .group() is called on the None result. Fix it by
# using the right function for finding a pattern anywhere in the string.
result = re.match(r"\d+", "total: 99 items")
print(result.group())


# TODO 1.A (Scenario -- Validating a Username Field on a Signup Form): a
# signup form needs to check that a username is 3 to 16 characters long and
# contains only letters, digits, or underscores -- and it needs to check the
# ENTIRE input, not just find a valid-looking piece somewhere inside a
# longer string. Write a function is_valid_username(username) that returns
# whether re.fullmatch(r"[A-Za-z0-9_]{3,16}", username) is not None. Loop
# over ["ann23", "a", "way_too_long_for_a_username_field", "bad!name",
# "ok_name_1"] and print f"{name}: {is_valid_username(name)}" for each.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks you to explain
# the actual difference between re.match() and re.search(), and when each
# one is the right choice. Write a function explain_match_vs_search() that
# returns a string explaining that re.match() only checks whether the
# pattern matches starting at position 0 of the string -- if the target
# text appears anywhere else, match() returns None even though the text is
# genuinely there -- while re.search() scans the entire string and succeeds
# on the first match found anywhere, which is why search() is almost always
# the right default when looking for a pattern that could appear anywhere
# in real, messy text; match() is really only appropriate when the pattern
# is specifically expected to be at the very beginning, like checking a
# string's prefix. Call it and print the result.


# ============================================================
# Topic 2: findall() & finditer()
# ============================================================

# TODO 2.1: Use re.findall() with the pattern r"\$\d+" on the string
# "Items cost $5, $12, and $100" and print the result.


# TODO 2.2: Use re.finditer() with the pattern r"\w+at" on the string
# "cat hat bat mat", looping over the results and printing each match's
# .group() and .start() (e.g. print(match.group(), match.start())).


# TODO 2.3: Use re.findall() with the pattern r"\b\w+\b" on the string
# "one two three" to find every word, then print len(...) of the result.


# TODO 2.4: Use re.findall() with the pattern r"#\w+" on the string
# "Loving this #sunset and #beachlife today" to extract every hashtag, and
# print the result.


# TODO 2.5 (Debug the Code): this is supposed to find every whole number in
# "order 7, then 22, then 100", but the pattern r"\d" only matches ONE digit
# at a time, so "100" incorrectly splits into three separate single-digit
# matches instead of being found as one number. Fix the pattern so runs of
# digits are matched as a whole.
numbers = re.findall(r"\d", "order 7, then 22, then 100")
print(numbers)


# TODO 2.A (Scenario -- Extracting Every Error Code From a Support Ticket):
# a support ticketing system logs error codes in the format "ERR-" followed
# by exactly 4 digits, and a report needs every one pulled out of a block of
# free-text notes. Write a function extract_error_codes(ticket_text) that
# returns re.findall(r"ERR-\d{4}", ticket_text). Create
# ticket = "User reported ERR-4021 twice, then ERR-9987 once." and print
# extract_error_codes(ticket).


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks why Python
# offers both findall() and finditer() when they seem to do almost the same
# thing. Write a function explain_findall_vs_finditer() that returns a
# string explaining that re.findall() returns every match as a plain list
# of strings -- simple and usually exactly what's needed when only the
# matched text itself matters -- while re.finditer() returns every match as
# an iterator of Match objects instead, which costs one extra step (looping
# over it rather than getting a ready-made list) but pays it back with each
# match's position in the original string via .start()/.end(), plus access
# to any groups the pattern defined; reach for finditer() specifically when
# position or per-match group data is needed, and findall() when only the
# matched text itself is needed. Call it and print the result.


# ============================================================
# Topic 3: Character Classes, Quantifiers & Anchors
# ============================================================

# TODO 3.1: Use re.findall() with the pattern r"[aeiouAEIOU]" on the string
# "The Quick Brown Fox" to find every vowel, and print len(...) of the
# result (the vowel count).


# TODO 3.2: Use re.findall() with the pattern r"colou?r" (the ? makes the u
# optional) on the string "favorite color and favourite colour", and print
# the result (should find both spellings).


# TODO 3.3: Use re.findall() with the pattern r"[A-Z]{2}\d{3}" on the string
# "Codes AB123 and CD456 and E78 are listed" and print the result (should
# only find the two codes that are exactly 2 uppercase letters followed by
# exactly 3 digits).


# TODO 3.4: Loop over ["12345", "abc12", "999999", "42"] and use
# re.fullmatch() with the pattern r"^\d{3,5}$" on each one, printing
# f"{line}: valid" or f"{line}: invalid" depending on the result.


# TODO 3.5 (Debug the Code): this pattern is supposed to only match the
# literal decimal value "3.14", but the period between 3 and 14 is
# unescaped, so it matches ANY character in that position (like the "x" and
# "y" in "3x14" and "3y14"), which is wrong. Fix it so only an actual
# period counts.
matches = re.findall(r"3.14", "the value is 3.14 not 3x14 or 3y14")
print(matches)


# TODO 3.A (Scenario -- Validating a Simple Password Policy): a signup form
# requires a password to be at least 8 characters long, using only letters,
# digits, or underscores (no spaces or other symbols). Write a function
# is_strong_password(password) that returns whether
# re.fullmatch(r"\w{8,}", password) is not None. Loop over
# ["short", "longenoughpassword", "12345678"] and print
# f"{pw}: {is_strong_password(pw)}" for each.


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks you to explain
# quantifiers and anchors and how they work together in a validation
# pattern. Write a function explain_quantifiers_and_anchors() that returns
# a string explaining that a quantifier controls how many times the piece
# right before it can repeat -- * for zero or more, + for one or more, ?
# for zero or one (optional), and {m,n} for a specific range -- while an
# anchor like ^ or $ matches a position in the string rather than an actual
# character, specifically the start or end; combining both, ^\d+$ only
# matches a string that is nothing but digits from its very first
# character to its very last, which is exactly why a validation pattern
# almost always needs both anchors, since without them a pattern like \d+
# would happily match a string that has valid digits buried inside
# otherwise invalid text. Call it and print the result.


# ============================================================
# Topic 4: Groups & Named Groups
# ============================================================

# TODO 4.1: Use re.match() with the pattern r"(\w+)@(\w+)\.com" on the
# string "alice@example.com", printing match.group(1) and match.group(2).


# TODO 4.2: Use re.match() with the pattern
# r"(?P<user>\w+)@(?P<domain>\w+)\.com" on the string "bob@company.com".
# Print match.group("user"), match.group("domain"), and match.groupdict().


# TODO 4.3: Use re.match() with the pattern r"(\d{2}):(\d{2}):(\d{2})" on
# the string "14:22:10" and print match.groups().


# TODO 4.4: Use re.finditer() with the pattern
# r"(?P<code>[A-Z]{3})-(?P<num>\d{3})" on the string
# "REF-101 and REF-202", looping over the matches and printing each one's
# .groupdict().


# TODO 4.5 (Debug the Code): this named group is written with the wrong
# syntax -- (?<year>...) instead of the correct (?P<year>...) -- Python's
# re module specifically requires the "P" right after the question mark for
# a named group. Fix the syntax so match.group("year") works.
match = re.match(r"(?<year>\d{4})-(?P<month>\d{2})", "2026-07")
print(match.group("year"))


# TODO 4.A (Scenario -- Parsing a "Last, First" Name Field): a data-entry
# system stores names as "Last, First" in one text field, and a report
# needs both parts split out separately. Write a function
# split_last_first(full_name) that uses re.match() with the pattern
# r"(?P<last>\w+),\s*(?P<first>\w+)" on full_name, and returns
# match.groupdict(). Call split_last_first("Papasani, Manohar") and print
# the result.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks what problem
# groups actually solve in a regex pattern. Write a function
# explain_groups_purpose() that returns a string explaining that groups let
# a single match be broken into labeled, individually retrievable pieces
# instead of just one undivided blob of matched text; wrapping part of a
# pattern in parentheses, (...), doesn't change what gets matched at all --
# it just makes that specific piece separately accessible afterward via
# .group(n), numbered left to right starting at 1; named groups,
# (?P<name>...), do the exact same thing but let that piece be retrieved by
# a meaningful name via .group('name') instead of a position number, which
# reads far more clearly and survives a pattern being reordered later
# without breaking. Call it and print the result.


# ============================================================
# Topic 5: re.sub() & re.split()
# ============================================================

# TODO 5.1: Use re.sub() with the pattern r"\d{4}-\d{4}-\d{4}-\d{4}" to
# replace the credit card number in "Card: 1234-5678-9012-3456" with
# "XXXX-XXXX-XXXX-XXXX". Print the result.


# TODO 5.2: Use re.sub() with the pattern r"[^a-zA-Z0-9\s]" (anything that
# is NOT a letter, digit, or whitespace) to strip all punctuation/symbols
# out of "Hello!!! World??? #Python$$$", replacing matches with an empty
# string "". Print the result.


# TODO 5.3: Use re.split() with the pattern r"\s*;\s*" (a semicolon,
# optionally surrounded by whitespace) to split
# "apple; banana ;cherry;  date" into a list of items. Print the result.


# TODO 5.4: Use re.sub() with the pattern r"-{2,}" (two or more dashes in a
# row) to collapse "too---many----dashes" down to single dashes. Print the
# result.


# TODO 5.5 (Debug the Code): this call to re.sub() has its arguments in the
# wrong order -- it's supposed to be re.sub(pattern, replacement, text), but
# the replacement string and the pattern got swapped, which raises an error
# (or does the wrong thing) instead of replacing every run of digits with
# "#". Fix the argument order.
result = re.sub("#", r"\d+", "Item 7 and item 42")
print(result)


# TODO 5.A (Scenario -- Redacting Social Security Numbers From a Document):
# a document-processing tool needs to redact any Social Security Number
# (format ###-##-####) before a document can be shared externally. Write a
# function redact_ssns(document_text) that returns
# re.sub(r"\d{3}-\d{2}-\d{4}", "XXX-XX-XXXX", document_text). Call it on
# "SSN on file: 123-45-6789 for this applicant." and print the result.


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks why anyone
# would use re.sub()/re.split() instead of the plain str.replace()/
# str.split() methods already known from earlier chapters. Write a
# function explain_sub_split_benefit() that returns a string explaining
# that str.replace() and str.split() only recognize one fixed, exact target
# string or separator -- they can't describe "any run of digits" or "a
# comma or one or more spaces, in any mix" as a single rule -- while
# re.sub() and re.split() accept a full pattern instead of a fixed string,
# so re.sub() can mask or replace an entire category of matching text in
# one call (every phone number, every SSN), and re.split() can break text
# apart on multiple different separator styles in a single call, which is
# exactly the kind of messy, inconsistent real-world text a fixed-string
# method could never fully handle. Call it and print the result.


# ============================================================
# Topic 6: Compiled Patterns
# ============================================================

# TODO 6.1: Use re.compile() to build digit_pattern from r"\d+", then call
# digit_pattern.findall() on "a1 b22 c333" and print the result.


# TODO 6.2: Use re.compile() to build email_pattern from
# r"[\w.+-]+@[\w-]+\.[\w.]+". Loop over
# ["contact: ann@example.com", "no email here", "reach bob@company.org"],
# and for each line, call email_pattern.search(line); if it matches, print
# match.group().


# TODO 6.3: Use re.compile() to build word_pattern from r"\b\w{5,}\b" (any
# standalone word of 5 or more characters). Call word_pattern.findall() on
# "short words versus longer words here" and print the result.


# TODO 6.4: Use re.compile() to build ip_pattern from
# r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}". Loop over
# ["request from 192.168.1.1 succeeded", "no ip in this line"], collecting
# every line's matched IP address (using ip_pattern.search(line).group() --
# skip lines with no match) into a list called found, then print found.


# TODO 6.5 (Debug the Code): this code correctly builds a compiled_pattern
# with re.compile(), but then calls the old module-level
# re.search(pattern_string, text) again instead of using the compiled
# object's own .search() method, which defeats the entire point of
# compiling it first. Fix the call to use compiled_pattern.search(text).
compiled_pattern = re.compile(r"\d+")
result = re.search(r"\d+", "value: 88")
print(result.group())


# TODO 6.A (Scenario -- Scanning Many Log Lines for the Same Error
# Pattern): a monitoring tool needs to scan through potentially thousands of
# log lines checking each one for an "[ERROR]" tag, which means the same
# pattern gets applied over and over -- exactly the case re.compile() is
# built for. Write a function count_error_lines(log_lines) that builds
# error_pattern = re.compile(r"\[ERROR\]") and returns
# sum(1 for line in log_lines if error_pattern.search(line)). Create
# sample_lines = ["[INFO] ok", "[ERROR] failed", "[INFO] ok",
# "[ERROR] failed again"] and print count_error_lines(sample_lines).


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks when compiling
# a pattern with re.compile() is actually worth doing. Write a function
# explain_compile_benefit() that returns a string explaining that
# re.compile(pattern) processes a pattern string once into a reusable
# compiled pattern object, which then has its own .search()/.match()/
# .findall() methods that behave exactly like the module-level
# re.search(pattern, text) versions, just without needing to pass (and
# re-parse) the raw pattern string on every single call; for a pattern used
# only once, compiling first adds little value, but for a pattern applied
# across many lines of a file or many calls in a loop -- exactly the
# log-scanning and resume-scanning cases this chapter keeps coming back to
# -- compiling it once and reusing the compiled object is both more
# efficient and clearer about the fact that the same pattern is meant to be
# reused. Call it and print the result.


# ============================================================
# Topic 7: Bringing It Together -- Greedy Matching, Raw Strings & Flags
# ============================================================

# TODO 7.1: Use re.findall() with the greedy pattern r'".*"' on
# 'She said "hello" and then "goodbye"' and print the result. Then use
# re.findall() with the non-greedy pattern r'".*?"' on the same string and
# print that result too -- comparing one giant match against two separate
# ones.


# TODO 7.2: Create raw_pattern = r"\d+\.\d+" and use re.findall() with it on
# "version 3.14 and 2.7", printing the result.


# TODO 7.3: Use re.findall() with the pattern r"error" and the re.IGNORECASE
# flag on the string "Error: ERROR: error occurred", and print the result
# (should find all three, regardless of capitalization).


# TODO 7.4: Create multiline_text = "line one\nline two\nline three" and use
# re.findall() with the pattern r"^line" and the re.MULTILINE flag, printing
# len(...) of the result (should be 3, one per line).


# TODO 7.5 (Debug the Code): this pattern uses a greedy .* between quotes,
# so on a string with TWO separate quoted phrases, it grabs everything from
# the FIRST quote all the way to the LAST quote as one giant match instead
# of finding each quoted phrase separately. Fix the greedy .* to the
# non-greedy .*? so each quoted phrase is matched on its own.
quoted = re.findall(r'"(.*)"', 'The signs said "stop" and "go" clearly')
print(quoted)


# TODO 7.A (Scenario -- A Log-Scanning Tool Combining Everything): a
# real monitoring tool needs to scan multi-line log text, case-insensitively
# find every ERROR-level line, and pull out both the timestamp and the
# message using named groups -- combining compiled patterns, named groups,
# and flags from across this whole chapter. Write a function
# scan_log_for_errors(log_text) that builds
# error_pattern = re.compile(r"(?P<time>\d{2}:\d{2}:\d{2})\s+\[ERROR\]\s+(?P<message>.+)", re.IGNORECASE),
# then loops over log_text.split("\n"), and for each line, if
# error_pattern.search(line) matches, appends match.groupdict() to a
# results list, finally returning results. Create
# sample_log = "10:15:00 [INFO] all good\n10:15:05 [error] disk full\n10:15:10 [ERROR] timeout"
# and print scan_log_for_errors(sample_log).


# TODO 7.B (Scenario -- Interview Prep): an interviewer asks you to name
# the most common regex mistakes beginners make. Write a function
# explain_regex_gotchas() that returns a string explaining that three
# specific things trip up almost every regex beginner at least once: first,
# quantifiers are greedy by default, matching as much text as possible -- a
# pattern meant to grab the shortest text between two delimiters needs the
# non-greedy versions, *? or +?, or it will stretch from the first
# delimiter all the way to the very last one instead of stopping at the
# nearest one; second, a pattern string should almost always be written as
# a raw string, r'...', since without it Python's own escape-sequence rules
# can silently corrupt backslash sequences like \d or \b before re ever
# sees them; third, matching is case-sensitive by default and ^/$ only
# anchor to the whole string by default, not each line -- re.IGNORECASE and
# re.MULTILINE exist specifically to change those two defaults when the
# situation calls for it. Call it and print the result.
