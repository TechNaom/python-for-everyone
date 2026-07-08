"""
Chapter 21 Exercises: Working with Databases
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every "database" in these exercises is a FakeConnection/FakeCursor or
FakeCollection class -- small stand-ins that mimic the real
mysql-connector-python / pymongo interfaces (same method names, same call
shape) so this file runs without a live MySQL or MongoDB server, and
without installing either driver. No real network access or database
connection happens anywhere in this file.
"""

import os

# --- Shared fakes, mimicking mysql-connector-python's real interface ---

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


STUDENTS_TABLE = [
    {"id": 1, "name": "Ana Torres", "grade": 91},
    {"id": 2, "name": "Ben Osei", "grade": 78},
    {"id": 3, "name": "Chen Wu", "grade": 88},
]


# TODO 1: Using FakeConnection(STUDENTS_TABLE), get a connection, get a
# cursor from it, call cursor.execute("SELECT * FROM students WHERE grade > %s", (80,)),
# then print each row's "name" from cursor.fetchall().


# TODO 2: Using the same pattern, call
# cursor.execute("SELECT * FROM students WHERE name = %s", ("Ben Osei",))
# and print cursor.fetchone().


# TODO 3 (SQL injection): Write a function build_unsafe_query(name) that
# returns f"SELECT * FROM students WHERE name = '{name}'" (the VULNERABLE
# f-string style -- do not execute this against anything, just build and
# print the string, to show what an attacker's input would turn the query
# into). Call it with the malicious input "x' OR '1'='1" and print the
# result -- notice the closing quote in the attacker's input ends the
# string early, and OR '1'='1' would match every row on a real server.


# TODO 4 (the fix): Write a function build_safe_query_and_params(name)
# that returns the tuple ("SELECT * FROM students WHERE name = %s", (name,))
# -- the parameterized version, where `name` is never glued into the SQL
# string at all. Call it with "x' OR '1'='1" and print the result -- the
# malicious text is now just an ordinary (harmless) params value.


# --- Shared fake, mimicking pymongo's real Collection interface ---

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


# TODO 5: Create a FakeCollection(). Insert two documents:
# {"name": "Dana Kim", "grade": 95, "clubs": ["debate"]} and
# {"name": "Eli Frost", "grade": 70}. Print collection.find() (every
# document currently stored).


# TODO 6: Using the same collection from TODO 5, call
# update_one({"name": "Eli Frost"}, {"$set": {"grade": 74}}), then print
# find_one({"name": "Eli Frost"}) to confirm the grade changed.


# TODO 7: Using the same collection, call
# delete_one({"name": "Dana Kim"}), then print find() to confirm only
# Eli Frost remains.


# TODO 8 (cloud connection & environment variables): Write a function
# build_connection_info() that reads "DB_HOST", "DB_USER", and "DB_NAME"
# from os.environ and returns a dict {"host": ..., "user": ..., "database": ...}.
# Before calling it, set os.environ["DB_HOST"] = "cloud.example.com",
# os.environ["DB_USER"] = "app_reader", and os.environ["DB_NAME"] = "school_records"
# (simulating a deployment environment that already has these set). Call
# build_connection_info() and print the result.


# TODO 9 (Debug the Code): this is supposed to safely look up "Ben Osei"
# by name, but it builds the SQL string with an f-string instead of using
# a parameterized query -- the exact SQL injection risk from Sub-topic 4.
# It also just returns the WRONG result here: FakeCursor only recognizes
# the %s-placeholder shape, so this f-string version falls through to its
# "return everything" fallback, and fetchone() grabs the FIRST row
# (Ana Torres) instead of the row that was actually asked for
# (Ben Osei). Find and fix it by switching to
# cursor.execute(sql, params) with a %s placeholder, instead of gluing
# `name` directly into the string.
def unsafe_lookup(cursor, name):
    sql = f"SELECT * FROM students WHERE name = '{name}'"
    cursor.execute(sql)
    return cursor.fetchone()


debug_cursor = FakeConnection(STUDENTS_TABLE).cursor()
print(unsafe_lookup(debug_cursor, "Ben Osei"))
