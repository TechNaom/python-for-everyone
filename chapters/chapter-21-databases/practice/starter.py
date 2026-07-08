"""
Chapter 21 Practice Bank: Working with Databases
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Every "database" in this practice bank is a FakeConnection/FakeCursor or
FakeCollection class -- small stand-ins mimicking the real
mysql-connector-python / pymongo interfaces (same method names, same call
shape), so nothing here needs a live MySQL/MongoDB server or either
driver installed. No real network access happens anywhere in this file.
"""

import os

# ============================================================
# Shared fakes used across this practice bank
# ============================================================

class FakeCursor:
    def __init__(self, table):
        self.table = table
        self._last_result = []

    def execute(self, sql, params=None):
        params = params or ()
        if "grade > %s" in sql:
            threshold = params[0]
            self._last_result = [row for row in self.table if row["grade"] > threshold]
        elif "name = %s" in sql:
            name = params[0]
            self._last_result = [row for row in self.table if row["name"] == name]
        elif "id = %s" in sql:
            row_id = params[0]
            self._last_result = [row for row in self.table if row["id"] == row_id]
        else:
            self._last_result = list(self.table)

    def fetchall(self):
        return list(self._last_result)

    def fetchone(self):
        return self._last_result[0] if self._last_result else None


class FakeConnection:
    def __init__(self, table):
        self.table = table

    def cursor(self):
        return FakeCursor(self.table)

    def commit(self):
        pass


class FakeCollection:
    def __init__(self):
        self.documents = []

    def insert_one(self, document):
        self.documents.append(dict(document))
        return document

    def find(self, query=None):
        query = query or {}
        return [d for d in self.documents if all(d.get(k) == v for k, v in query.items())]

    def find_one(self, query=None):
        results = self.find(query)
        return results[0] if results else None

    def update_one(self, query, update):
        doc = self.find_one(query)
        if doc is not None:
            doc.update(update.get("$set", {}))
            return True
        return False

    def delete_one(self, query):
        doc = self.find_one(query)
        if doc is not None:
            self.documents.remove(doc)
            return True
        return False


STUDENTS_TABLE = [
    {"id": 1, "name": "Ana Torres", "grade": 91},
    {"id": 2, "name": "Ben Osei", "grade": 78},
    {"id": 3, "name": "Chen Wu", "grade": 88},
]


# ============================================================
# Topic 1: What a database connection is, and why a driver
# ============================================================

# TODO 1.1: Write a function needs_a_driver(system) that returns True if
# system is one of "MySQL", "MongoDB", or "PostgreSQL", and False for
# "CSV file" or "plain text file" (a driver library is needed to speak a
# real database's network protocol; a flat file needs no such driver).
# Loop over ["MySQL", "CSV file", "MongoDB"] and print
# f"{s}: needs a driver = {needs_a_driver(s)}" for each.


# TODO 1.2: Write a function connection_steps() that returns the list
# ["connect", "get a working object (cursor or collection)", "run a command", "read results back"]
# -- the shared shape both MySQL and MongoDB drivers follow. Call it and
# print the result.


# TODO 1.3 (Debug the Code): this is supposed to describe what a driver
# library does, but it claims the driver stores the ENTIRE database
# inside the Python program's own memory -- wrong; a driver just speaks
# the database's network protocol, the actual data stays on the database
# server. Find and fix it.
def explain_driver():
    return "A driver library stores the entire database inside the Python program's memory."


print(explain_driver())


# TODO 1.A (Scenario -- Choosing Whether a Driver Is Needed): a teammate
# is building a tool that only ever reads a local CSV file, never talks
# to MySQL or MongoDB. Write a function does_this_tool_need_a_driver(uses_csv_only)
# that returns "no driver needed -- Chapter 13's open() is enough" if
# uses_csv_only is True, and "needs a driver library for whichever
# database it talks to" otherwise. Call it with True and print the
# result.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks why Python
# can't just talk to MySQL or MongoDB directly, the way it opens a file
# with open(). Write a function explain_why_a_driver_is_needed() that
# returns a string explaining that a database is separate software
# reached over a network connection, speaking its own specific protocol,
# so Python needs a driver library (mysql-connector-python, pymongo)
# written to speak that exact protocol and translate results back into
# ordinary Python values. Call it and print the result.


# ============================================================
# Topic 2: Connecting to MySQL & cursors
# ============================================================

# TODO 2.1: Using FakeConnection(STUDENTS_TABLE), get a connection and a
# cursor, then print type(cursor).__name__.


# TODO 2.2: Write a function run_query(cursor, sql, params) that calls
# cursor.execute(sql, params) and returns cursor.fetchall(). Call it with
# a query matching students with grade > 85 and print the names from the
# result.


# TODO 2.3: Write a function count_matching_rows(cursor, sql, params) that
# calls cursor.execute(sql, params) and returns len(cursor.fetchall()).
# Call it with a query matching grade > 80 and print the result.


# TODO 2.4 (Debug the Code): this is supposed to get a cursor from a
# connection, but it calls FakeConnection(STUDENTS_TABLE) itself as if it
# were a cursor (calling .execute() directly on the connection object
# instead of on a cursor obtained via .cursor()) -- a real MySQL
# connection object has no .execute() method at all, so this raises an
# AttributeError (caught below just so this demo can keep running and
# show you the error, the same error a real mysql-connector-python
# connection would raise). Find and fix it by calling .cursor() first.
def broken_query_attempt():
    connection = FakeConnection(STUDENTS_TABLE)
    connection.execute("SELECT * FROM students WHERE grade > %s", (85,))
    return connection.fetchall()


try:
    print(broken_query_attempt())
except AttributeError as e:
    print(f"AttributeError (the bug): {e}")


# TODO 2.A (Scenario -- Reusable Query Helper): write a function
# fetch_students_above(cursor, threshold) that calls
# cursor.execute("SELECT * FROM students WHERE grade > %s", (threshold,))
# and returns cursor.fetchall(). Call it with a fresh cursor and threshold
# 90, printing the result.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks what a
# cursor is and why it's separate from the connection. Write a function
# explain_cursor_vs_connection() that returns a string explaining that
# the connection is the open line to the database, while the cursor is
# the object commands actually run through and results are read back
# from -- one connection can create multiple cursors for different
# concurrent queries. Call it and print the result.


# ============================================================
# Topic 3: Parameterized queries & SQL injection
# ============================================================

# TODO 3.1: Write a function build_parameterized_query(column, value)
# that returns the tuple (f"SELECT * FROM students WHERE {column} = %s", (value,)).
# Call it with ("name", "Ana Torres") and print the result.


# TODO 3.2: Write a function looks_like_injection_attempt(user_input)
# that returns True if "'" in user_input or " OR " in user_input.upper(),
# and False otherwise (a rough, illustrative check only -- NOT a real
# defense; the lesson's point is that parameterized queries, not input
# scanning, are the real fix). Loop over ["Ana Torres", "x' OR '1'='1"]
# and print f"{s}: {looks_like_injection_attempt(s)}" for each.


# TODO 3.3 (Debug the Code): this is supposed to safely build a query for
# a given name, but it uses an f-string to glue `name` directly into the
# SQL text -- the SQL injection risk from the lesson. Find and fix it by
# returning a parameterized (sql, params) tuple instead.
def build_query_unsafe(name):
    return f"SELECT * FROM students WHERE name = '{name}'"


print(build_query_unsafe("x' OR '1'='1"))


# TODO 3.A (Scenario -- Reviewing a Teammate's Query Code): a teammate
# wrote sql = f"SELECT * FROM orders WHERE customer = '{customer_name}'"
# for a search box on a public website. Write a function
# review_teammates_query() that returns a string explaining this is
# vulnerable to SQL injection because customer_name comes from
# user-controlled input and is glued directly into the SQL text, and that
# the fix is a parameterized query: "SELECT * FROM orders WHERE customer = %s"
# with customer_name passed separately as a params tuple. Call it and
# print the result.


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks why checking
# user input for quote characters isn't considered a real defense against
# SQL injection. Write a function explain_why_input_checking_isnt_enough()
# that returns a string explaining that attackers have many techniques
# beyond a simple quote character, so pattern-matching against known bad
# input is inherently incomplete, while parameterized queries close the
# entire class of attack structurally, by never letting substituted
# values touch the SQL command's syntax at all. Call it and print the
# result.


# ============================================================
# Topic 4: MongoDB & documents
# ============================================================

# TODO 4.1: Create a FakeCollection(). Insert {"name": "Priya Nair", "grade": 95, "tags": ["honors"]}
# and {"name": "Omar Haddad", "grade": 60} (no "tags" field at all). Print
# collection.find().


# TODO 4.2: Write a function has_field(document, field_name) that returns
# field_name in document. Call it with ({"name": "Priya Nair", "tags": ["honors"]}, "tags")
# and ({"name": "Omar Haddad"}, "tags"), printing both results.


# TODO 4.3 (Debug the Code): this is supposed to describe MongoDB
# documents accurately, but it claims every document in a collection MUST
# have the exact same fields, the way a SQL table's rows must share the
# same columns -- false, that's exactly what MongoDB's flexible schema
# does NOT require. Find and fix it.
def explain_mongo_schema():
    return "Every document in a MongoDB collection must have the exact same fields, like a SQL table's columns."


print(explain_mongo_schema())


# TODO 4.A (Scenario -- Modeling a Product Catalog): a product catalog
# has books (with an "author" field) and electronics (with a "warranty_years"
# field) in the same collection. Write a function
# explain_product_catalog_fit() that returns a string explaining that a
# document database fits this well because each product's document can
# have only the fields relevant to its own category, without needing a
# separate table (or a lot of unused NULL columns) for every possible
# category-specific field. Call it and print the result.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks when a
# document database's flexible schema is an advantage versus a risk.
# Write a function explain_flexible_schema_tradeoff() that returns a
# string explaining that flexible schema is an advantage when records
# genuinely vary in shape (different product categories, evolving user
# profiles), but a risk when an application actually needs every record
# to share the same required fields and types, since nothing in Mongo's
# default behavior enforces that automatically the way a SQL table would.
# Call it and print the result.


# ============================================================
# Topic 5: CRUD with pymongo
# ============================================================

# TODO 5.1: Create a FakeCollection(). Insert three documents:
# {"name": "Ana", "grade": 91}, {"name": "Ben", "grade": 78}, and
# {"name": "Chen", "grade": 88}. Print len(collection.find()).


# TODO 5.2: Using the same collection, call
# update_one({"name": "Ben"}, {"$set": {"grade": 85}}) and print
# find_one({"name": "Ben"}).


# TODO 5.3: Using the same collection, call delete_one({"name": "Chen"})
# and print sorted(d["name"] for d in collection.find()).


# TODO 5.4 (Debug the Code): this is supposed to update a student's
# grade, but it calls update_one with the update dict passed directly
# (not wrapped in "$set"), so it doesn't match this fake's expected
# {"$set": {...}} shape and the update silently does nothing. Find and
# fix it by wrapping the update in {"$set": ...}.
def broken_update(collection, name, new_grade):
    return collection.update_one({"name": name}, {"grade": new_grade})


fresh_collection = FakeCollection()
fresh_collection.insert_one({"name": "Dana", "grade": 70})
broken_update(fresh_collection, "Dana", 95)
print(fresh_collection.find_one({"name": "Dana"}))


# TODO 5.A (Scenario -- A Simple Inventory Tracker): write a function
# restock_item(collection, item_name, amount) that finds the document
# where "name" equals item_name, and if found, updates it by setting
# "quantity" to its current "quantity" value plus `amount` (using
# {"$set": {"quantity": new_value}}), returning True; returns False if no
# such document exists. Test it with a fresh FakeCollection() containing
# {"name": "widget", "quantity": 10}, calling restock_item(collection, "widget", 5),
# then print find_one({"name": "widget"}).


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks why
# update_one and delete_one only affect the FIRST matching document, and
# what to use instead for updating many at once. Write a function
# explain_update_one_vs_many() that returns a string explaining that
# update_one/delete_one intentionally touch only the first match, which
# is safer as a default, and that pymongo's update_many/delete_many exist
# specifically for applying the same change to every matching document at
# once, when that's genuinely the intent. Call it and print the result.


# ============================================================
# Topic 6: Relational vs. document data
# ============================================================

# TODO 6.1: Write a function fits_relational_better(has_fixed_shape, needs_joins)
# that returns has_fixed_shape and needs_joins. Call it with (True, True)
# and (False, False), printing both results.


# TODO 6.2: Write a function describe_join() that returns the string
# "Combines rows from related tables based on a shared value, into one result."
# Call it and print the result.


# TODO 6.3 (Debug the Code): this is supposed to accurately compare the
# two models, but it claims a relational database can NEVER represent
# data with varying shape at all -- overstated; the lesson's Go Deeper
# notes it CAN be modeled (e.g. with a text/JSON column), just less
# efficiently for certain queries than a document database. Find and fix
# it to state the real, more nuanced tradeoff.
def compare_models():
    return "A relational database can never represent data with a varying shape."


print(compare_models())


# TODO 6.A (Scenario -- Choosing a Model for a New Feature): a team is
# building a user-profile system where every user has a name and email,
# but optional profile fields vary wildly (some users add a bio, a
# portfolio link, social handles -- others add none of these). Write a
# function recommend_model_for_user_profiles() that returns a string
# recommending a document database specifically because the optional,
# varying fields fit a flexible schema well, while noting the required
# core fields (name, email) would still need validating at the
# application level, since MongoDB doesn't enforce them by default. Call
# it and print the result.


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks you to
# compare relational and document databases in under 30 seconds. Write a
# function elevator_pitch_relational_vs_document() that returns a string
# giving a concise comparison: relational databases use fixed-column
# tables and joins, suiting data with a stable, well-known shape and
# relationships queried in many different ways; document databases use
# flexible, self-contained documents, suiting data whose shape varies
# record to record or where related data naturally nests inside one
# record. Call it and print the result.


# ============================================================
# Topic 7: Cloud-hosted connections & environment variables
# ============================================================

# TODO 7.1: Write a function build_env_backed_config(keys) that returns a
# dict mapping each key in `keys` to os.environ[key]. Before calling it,
# set os.environ["DB_HOST"] = "cloud.example.com" and
# os.environ["DB_USER"] = "reader" (simulating a deployment environment).
# Call build_env_backed_config(["DB_HOST", "DB_USER"]) and print the
# result.


# TODO 7.2: Write a function is_hardcoded_secret(line_of_code) that
# returns True if "password" in line_of_code.lower() and "os.environ" not in line_of_code,
# and False otherwise (a rough, illustrative check for teaching purposes).
# Loop over ['password = "abc123"', 'password = os.environ["DB_PASSWORD"]']
# and print f"{line}: hardcoded = {is_hardcoded_secret(line)}" for each.


# TODO 7.3 (Debug the Code): this is supposed to safely build MySQL
# connection kwargs from the environment, but it hardcodes the password
# directly in the source instead of reading it from os.environ -- exactly
# the mistake this chapter warns against. Find and fix it.
def build_connection_kwargs_broken():
    return {
        "host": os.environ.get("DB_HOST", "localhost"),
        "user": os.environ.get("DB_USER", "app_user"),
        "password": "hardcoded-secret-123",
    }


print(build_connection_kwargs_broken())


# TODO 7.A (Scenario -- Reviewing a Deployment Config): a teammate's
# script has db_password = "letmein2024" written directly in a file that
# gets committed to a public GitHub repo. Write a function
# review_hardcoded_password() that returns a string explaining this leaks
# a real credential to anyone who can view the repository (including
# forever, in the git history, even if it's later removed from the latest
# version), and that the fix is to read the password from an environment
# variable via os.environ, setting the real value only in whatever
# platform actually deploys the code, never in a committed file. Call it
# and print the result.


# TODO 7.B (Scenario -- Interview Prep): an interviewer asks what TLS
# adds to a cloud database connection, beyond just using environment
# variables for credentials. Write a function explain_tls_role() that
# returns a string explaining that environment variables keep credentials
# out of source code, but TLS separately encrypts the actual network
# connection itself, so credentials and data can't be read by anyone able
# to intercept traffic between the program and the remote database server
# -- the two protections address different risks and both matter. Call
# it and print the result.
