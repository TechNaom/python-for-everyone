"""
Chapter 21 Practice Bank: Working with Databases -- reference solution.
Run this from inside the practice/ folder: python3 solution.py
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

# TODO 1.1
def needs_a_driver(system):
    driver_needed = {"MySQL", "MongoDB", "PostgreSQL"}
    return system in driver_needed


for s in ["MySQL", "CSV file", "MongoDB"]:
    print(f"{s}: needs a driver = {needs_a_driver(s)}")

# TODO 1.2
def connection_steps():
    return ["connect", "get a working object (cursor or collection)", "run a command", "read results back"]


print(connection_steps())

# TODO 1.3 (Debug the Code)
# Bug: claimed the driver stores the entire database inside the Python
# program's memory -- wrong; the driver just speaks the protocol, data
# stays on the server. Fix: describe the driver accurately.
def explain_driver_right():
    return "A driver library speaks the database's network protocol on Python's behalf; the actual data stays on the database server, not in the Python program's memory."


print(explain_driver_right())

# TODO 1.A (Scenario)
def does_this_tool_need_a_driver(uses_csv_only):
    if uses_csv_only:
        return "no driver needed -- Chapter 13's open() is enough"
    return "needs a driver library for whichever database it talks to"


print(does_this_tool_need_a_driver(True))

# TODO 1.B (Scenario -- Interview Prep)
def explain_why_a_driver_is_needed():
    return (
        "A database is separate software reached over a network "
        "connection, speaking its own specific protocol -- unlike a "
        "flat file, Python can't just open() it directly. A driver "
        "library (mysql-connector-python, pymongo) is written specifically "
        "to speak that protocol and translate results back into "
        "ordinary Python values."
    )


print(explain_why_a_driver_is_needed())


# ============================================================
# Topic 2: Connecting to MySQL & cursors
# ============================================================

# TODO 2.1
connection = FakeConnection(STUDENTS_TABLE)
cursor = connection.cursor()
print(type(cursor).__name__)

# TODO 2.2
def run_query(cursor, sql, params):
    cursor.execute(sql, params)
    return cursor.fetchall()


for row in run_query(cursor, "SELECT * FROM students WHERE grade > %s", (85,)):
    print(row["name"])

# TODO 2.3
def count_matching_rows(cursor, sql, params):
    cursor.execute(sql, params)
    return len(cursor.fetchall())


print(count_matching_rows(cursor, "SELECT * FROM students WHERE grade > %s", (80,)))

# TODO 2.4 (Debug the Code)
# Bug: called .execute()/.fetchall() directly on the CONNECTION instead
# of getting a cursor first -- a real connection object has no .execute()
# method. Fix: call .cursor() first, then use the cursor.
def fixed_query_attempt():
    connection = FakeConnection(STUDENTS_TABLE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE grade > %s", (85,))
    return cursor.fetchall()


print(fixed_query_attempt())

# TODO 2.A (Scenario)
def fetch_students_above(cursor, threshold):
    cursor.execute("SELECT * FROM students WHERE grade > %s", (threshold,))
    return cursor.fetchall()


fresh_cursor = FakeConnection(STUDENTS_TABLE).cursor()
print(fetch_students_above(fresh_cursor, 90))

# TODO 2.B (Scenario -- Interview Prep)
def explain_cursor_vs_connection():
    return (
        "The connection is the open line to the database. The cursor is "
        "the object commands actually run through and results are read "
        "back from -- one connection can create multiple cursors, for "
        "example to run different concurrent queries."
    )


print(explain_cursor_vs_connection())


# ============================================================
# Topic 3: Parameterized queries & SQL injection
# ============================================================

# TODO 3.1
def build_parameterized_query(column, value):
    return (f"SELECT * FROM students WHERE {column} = %s", (value,))


print(build_parameterized_query("name", "Ana Torres"))

# TODO 3.2
def looks_like_injection_attempt(user_input):
    return "'" in user_input or " OR " in user_input.upper()


for s in ["Ana Torres", "x' OR '1'='1"]:
    print(f"{s}: {looks_like_injection_attempt(s)}")

# TODO 3.3 (Debug the Code)
# Bug: used an f-string to glue `name` directly into the SQL text --
# the SQL injection risk. Fix: return a parameterized (sql, params) tuple.
def build_query_safe(name):
    return ("SELECT * FROM students WHERE name = %s", (name,))


print(build_query_safe("x' OR '1'='1"))

# TODO 3.A (Scenario)
def review_teammates_query():
    return (
        "This is vulnerable to SQL injection: customer_name comes from "
        "user-controlled input and is glued directly into the SQL text "
        "with an f-string. The fix is a parameterized query -- "
        "\"SELECT * FROM orders WHERE customer = %s\" -- with "
        "customer_name passed separately as a params tuple, so it's "
        "always treated as data, never as SQL syntax."
    )


print(review_teammates_query())

# TODO 3.B (Scenario -- Interview Prep)
def explain_why_input_checking_isnt_enough():
    return (
        "Attackers have many techniques beyond a simple quote character, "
        "so pattern-matching against known bad input is inherently "
        "incomplete -- there's always another trick a checklist misses. "
        "Parameterized queries close the entire class of attack "
        "structurally, by never letting substituted values touch the SQL "
        "command's syntax at all, regardless of what characters they contain."
    )


print(explain_why_input_checking_isnt_enough())


# ============================================================
# Topic 4: MongoDB & documents
# ============================================================

# TODO 4.1
collection_41 = FakeCollection()
collection_41.insert_one({"name": "Priya Nair", "grade": 95, "tags": ["honors"]})
collection_41.insert_one({"name": "Omar Haddad", "grade": 60})
print(collection_41.find())

# TODO 4.2
def has_field(document, field_name):
    return field_name in document


print(has_field({"name": "Priya Nair", "tags": ["honors"]}, "tags"))
print(has_field({"name": "Omar Haddad"}, "tags"))

# TODO 4.3 (Debug the Code)
# Bug: claimed every document in a collection must share the exact same
# fields, like SQL columns -- false, that's what Mongo's flexible schema
# does NOT require. Fix: describe it accurately.
def explain_mongo_schema_right():
    return "MongoDB documents in the same collection can have different fields entirely -- there's no requirement that they all share the same shape, unlike a SQL table's fixed columns."


print(explain_mongo_schema_right())

# TODO 4.A (Scenario)
def explain_product_catalog_fit():
    return (
        "A document database fits this well because each product's "
        "document can have only the fields relevant to its own category "
        "(books get 'author', electronics get 'warranty_years'), without "
        "needing a separate table -- or a lot of unused NULL columns -- "
        "for every possible category-specific field."
    )


print(explain_product_catalog_fit())

# TODO 4.B (Scenario -- Interview Prep)
def explain_flexible_schema_tradeoff():
    return (
        "Flexible schema is an advantage when records genuinely vary in "
        "shape -- different product categories, evolving user profiles -- "
        "but it's a risk when an application actually needs every record "
        "to share the same required fields and types, since nothing in "
        "MongoDB's default behavior enforces that automatically the way a "
        "SQL table's fixed columns would."
    )


print(explain_flexible_schema_tradeoff())


# ============================================================
# Topic 5: CRUD with pymongo
# ============================================================

# TODO 5.1
collection_51 = FakeCollection()
collection_51.insert_one({"name": "Ana", "grade": 91})
collection_51.insert_one({"name": "Ben", "grade": 78})
collection_51.insert_one({"name": "Chen", "grade": 88})
print(len(collection_51.find()))

# TODO 5.2
collection_51.update_one({"name": "Ben"}, {"$set": {"grade": 85}})
print(collection_51.find_one({"name": "Ben"}))

# TODO 5.3
collection_51.delete_one({"name": "Chen"})
print(sorted(d["name"] for d in collection_51.find()))

# TODO 5.4 (Debug the Code)
# Bug: the update dict was passed directly instead of wrapped in "$set",
# so it doesn't match the expected {"$set": {...}} shape and silently does
# nothing. Fix: wrap it in {"$set": ...}.
def fixed_update(collection, name, new_grade):
    return collection.update_one({"name": name}, {"$set": {"grade": new_grade}})


fresh_collection = FakeCollection()
fresh_collection.insert_one({"name": "Dana", "grade": 70})
fixed_update(fresh_collection, "Dana", 95)
print(fresh_collection.find_one({"name": "Dana"}))

# TODO 5.A (Scenario)
def restock_item(collection, item_name, amount):
    doc = collection.find_one({"name": item_name})
    if doc is None:
        return False
    new_quantity = doc["quantity"] + amount
    collection.update_one({"name": item_name}, {"$set": {"quantity": new_quantity}})
    return True


inventory = FakeCollection()
inventory.insert_one({"name": "widget", "quantity": 10})
restock_item(inventory, "widget", 5)
print(inventory.find_one({"name": "widget"}))

# TODO 5.B (Scenario -- Interview Prep)
def explain_update_one_vs_many():
    return (
        "update_one/delete_one intentionally touch only the first "
        "matching document, which is a safer default. pymongo's "
        "update_many/delete_many exist specifically for applying the "
        "same change to every matching document at once, when that's "
        "genuinely the intent."
    )


print(explain_update_one_vs_many())


# ============================================================
# Topic 6: Relational vs. document data
# ============================================================

# TODO 6.1
def fits_relational_better(has_fixed_shape, needs_joins):
    return has_fixed_shape and needs_joins


print(fits_relational_better(True, True))
print(fits_relational_better(False, False))

# TODO 6.2
def describe_join():
    return "Combines rows from related tables based on a shared value, into one result."


print(describe_join())

# TODO 6.3 (Debug the Code)
# Bug: claimed a relational database can NEVER represent varying-shape
# data -- overstated; it CAN (e.g. a text/JSON column), just less
# efficiently for certain queries. Fix: state the real tradeoff.
def compare_models_right():
    return "A relational database CAN represent varying-shape data (e.g. with a text or JSON column), but a document database does it more naturally and more efficiently for certain queries, like finding all documents with a specific nested value."


print(compare_models_right())

# TODO 6.A (Scenario)
def recommend_model_for_user_profiles():
    return (
        "A document database fits well here, specifically because the "
        "optional, widely-varying profile fields (bio, portfolio link, "
        "social handles) suit a flexible schema. The required core "
        "fields (name, email) would still need validating at the "
        "application level, since MongoDB doesn't enforce required "
        "fields by default the way a SQL table's NOT NULL columns would."
    )


print(recommend_model_for_user_profiles())

# TODO 6.B (Scenario -- Interview Prep)
def elevator_pitch_relational_vs_document():
    return (
        "Relational databases use fixed-column tables and joins, suiting "
        "data with a stable, well-known shape and relationships queried "
        "in many different ways. Document databases use flexible, "
        "self-contained documents, suiting data whose shape varies "
        "record to record, or where related data naturally nests inside "
        "one record instead of living in a separate table."
    )


print(elevator_pitch_relational_vs_document())


# ============================================================
# Topic 7: Cloud-hosted connections & environment variables
# ============================================================

# TODO 7.1
def build_env_backed_config(keys):
    return {key: os.environ[key] for key in keys}


os.environ["DB_HOST"] = "cloud.example.com"
os.environ["DB_USER"] = "reader"
print(build_env_backed_config(["DB_HOST", "DB_USER"]))

# TODO 7.2
def is_hardcoded_secret(line_of_code):
    return "password" in line_of_code.lower() and "os.environ" not in line_of_code


for line in ['password = "abc123"', 'password = os.environ["DB_PASSWORD"]']:
    print(f"{line}: hardcoded = {is_hardcoded_secret(line)}")

# TODO 7.3 (Debug the Code)
# Bug: hardcoded the password directly in the source instead of reading
# it from os.environ -- exactly the mistake this chapter warns against.
# Fix: read it from an environment variable too.
def build_connection_kwargs_fixed():
    return {
        "host": os.environ.get("DB_HOST", "localhost"),
        "user": os.environ.get("DB_USER", "app_user"),
        "password": os.environ.get("DB_PASSWORD", ""),
    }


print(build_connection_kwargs_fixed())

# TODO 7.A (Scenario)
def review_hardcoded_password():
    return (
        "This leaks a real credential to anyone who can view the "
        "repository -- including forever, in the git history, even if "
        "it's later removed from the latest version. The fix is to read "
        "the password from an environment variable via os.environ, "
        "setting the real value only in whatever platform actually "
        "deploys the code, never in a committed file."
    )


print(review_hardcoded_password())

# TODO 7.B (Scenario -- Interview Prep)
def explain_tls_role():
    return (
        "Environment variables keep credentials out of source code, but "
        "TLS separately encrypts the actual network connection itself, "
        "so credentials and data can't be read by anyone able to "
        "intercept traffic between the program and the remote database "
        "server. The two protections address different risks, and both "
        "matter for a real cloud connection."
    )


print(explain_tls_role())
