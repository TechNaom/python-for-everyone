"""
Chapter 21 Exercises: Working with Databases -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
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


# TODO 1
connection = FakeConnection(STUDENTS_TABLE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM students WHERE grade > %s", (80,))
for row in cursor.fetchall():
    print(row["name"])

# TODO 2
cursor.execute("SELECT * FROM students WHERE name = %s", ("Ben Osei",))
print(cursor.fetchone())


# TODO 3
def build_unsafe_query(name):
    return f"SELECT * FROM students WHERE name = '{name}'"


print(build_unsafe_query("x' OR '1'='1"))


# TODO 4
def build_safe_query_and_params(name):
    return ("SELECT * FROM students WHERE name = %s", (name,))


print(build_safe_query_and_params("x' OR '1'='1"))


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


# TODO 5
collection = FakeCollection()
collection.insert_one({"name": "Dana Kim", "grade": 95, "clubs": ["debate"]})
collection.insert_one({"name": "Eli Frost", "grade": 70})
print(collection.find())

# TODO 6
collection.update_one({"name": "Eli Frost"}, {"$set": {"grade": 74}})
print(collection.find_one({"name": "Eli Frost"}))

# TODO 7
collection.delete_one({"name": "Dana Kim"})
print(collection.find())


# TODO 8
def build_connection_info():
    return {
        "host": os.environ["DB_HOST"],
        "user": os.environ["DB_USER"],
        "database": os.environ["DB_NAME"],
    }


os.environ["DB_HOST"] = "cloud.example.com"
os.environ["DB_USER"] = "app_reader"
os.environ["DB_NAME"] = "school_records"
print(build_connection_info())


# TODO 9 (Debug the Code)
# Bug: the SQL string was built with an f-string, gluing `name` directly
# into it -- the exact SQL injection risk from Sub-topic 4 (and here, it
# also just doesn't work correctly against FakeCursor, which only
# recognizes the %s-placeholder shape, so it silently falls back to
# returning every row instead of matching by name). Fix: use a
# parameterized query with a %s placeholder and a separate params tuple.
def safe_lookup(cursor, name):
    sql = "SELECT * FROM students WHERE name = %s"
    cursor.execute(sql, (name,))
    return cursor.fetchone()


debug_cursor = FakeConnection(STUDENTS_TABLE).cursor()
print(safe_lookup(debug_cursor, "Ben Osei"))
