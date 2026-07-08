"""
Chapter 21 Project: Student Record Management System -- starter.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: a mock database
layer (FakeConnection/FakeCursor) implementing the real
mysql-connector-python interface (cursor(), execute(sql, params),
fetchall(), fetchone(), commit()), demonstrating parameterized-query
safety and CRUD reporting. No real network access or database connection
happens anywhere in this file, so it runs the same way for every learner,
every time.

Fill in the numbered TODOs below. Want to see one finished version first?
Run solution.py (also from inside this folder).
"""

import json


# --- Mock database layer, mimicking mysql-connector-python's real
# interface (cursor(), execute(sql, params), fetchall(), fetchone(),
# commit()) closely enough to demonstrate the pattern, without needing a
# live MySQL server. ---

class FakeCursor:
    def __init__(self, table):
        self.table = table  # a list of dicts, standing in for SQL rows
        self._last_result = []

    def execute(self, sql, params=None):
        """Supports the small subset of SQL shapes this project needs:
        SELECT * FROM students [WHERE id = %s], INSERT INTO students ...,
        UPDATE students SET grade = %s WHERE id = %s, and
        DELETE FROM students WHERE id = %s."""
        params = params or ()

        if sql.startswith("SELECT"):
            if "WHERE id = %s" in sql:
                student_id = params[0]
                self._last_result = [row for row in self.table if row["id"] == student_id]
            else:
                self._last_result = list(self.table)

        elif sql.startswith("INSERT"):
            new_id = (max((row["id"] for row in self.table), default=0)) + 1
            name, grade = params
            self.table.append({"id": new_id, "name": name, "grade": grade})
            self._last_result = []

        elif sql.startswith("UPDATE"):
            new_grade, student_id = params
            for row in self.table:
                if row["id"] == student_id:
                    row["grade"] = new_grade
            self._last_result = []

        elif sql.startswith("DELETE"):
            student_id = params[0]
            self.table[:] = [row for row in self.table if row["id"] != student_id]
            self._last_result = []

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
        pass  # a real connection would persist changes; nothing to persist here


# --- Seed data: this program's "database", held in memory for the
# session (a real version would connect to a live MySQL server instead,
# using the exact same cursor/execute/fetchall/commit calls below). ---

STUDENTS_TABLE = [
    {"id": 1, "name": "Ana Torres", "grade": 91},
    {"id": 2, "name": "Ben Osei", "grade": 78},
    {"id": 3, "name": "Chen Wu", "grade": 88},
]


# TODO 1: Write a function add_student(connection, name, grade) that gets
# a cursor from `connection`, calls
# cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)", (name, grade)),
# calls connection.commit(), and returns None. (The mock's INSERT handler
# above ignores the exact column list text and just reads params, so the
# SQL string only needs to start with "INSERT".)
def add_student(connection, name, grade):
    pass


# TODO 2: Write a function list_students(connection) that gets a cursor,
# calls cursor.execute("SELECT * FROM students"), and returns
# cursor.fetchall().
def list_students(connection):
    pass


# TODO 3: Write a function find_student(connection, student_id) that gets
# a cursor, calls
# cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,)),
# and returns cursor.fetchone().
def find_student(connection, student_id):
    pass


# TODO 4: Write a function update_grade(connection, student_id, new_grade)
# that gets a cursor, calls
# cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (new_grade, student_id)),
# calls connection.commit(), and returns find_student(connection, student_id)
# (to confirm and return the updated row, or None if no such student).
def update_grade(connection, student_id, new_grade):
    pass


# TODO 5: Write a function delete_student(connection, student_id) that
# gets a cursor, calls
# cursor.execute("DELETE FROM students WHERE id = %s", (student_id,)),
# calls connection.commit(), and returns None.
def delete_student(connection, student_id):
    pass


# TODO 6: Write a function class_average(connection) that calls
# list_students(connection), and returns
# round(sum(s["grade"] for s in students) / len(students), 2) if the list
# is non-empty, or 0 if it's empty (avoiding a divide-by-zero).
def class_average(connection):
    pass


# TODO 7: Write a function honor_roll(connection, threshold=90) that
# calls list_students(connection) and returns a list of names (strings)
# for every student whose grade is >= threshold, sorted alphabetically.
def honor_roll(connection, threshold=90):
    pass


# TODO 8: Write a function export_to_json(connection) that calls
# list_students(connection) and returns json.dumps(students, indent=2)
# -- a JSON export of every student record, tying back to Chapter 19's
# json module.
def export_to_json(connection):
    pass


# TODO 9: Write a function build_unsafe_search_query(name) that returns
# the VULNERABLE f-string version: f"SELECT * FROM students WHERE name = '{name}'"
# -- this function only builds and returns the string for demonstration;
# it is never executed against anything in this project.
def build_unsafe_search_query(name):
    pass


# --- Session state ---
print("=== Student Record Management System ===")
connection = FakeConnection(STUDENTS_TABLE)

while True:
    print()
    print("1. List all students")
    print("2. Find a student by ID")
    print("3. Add a new student")
    print("4. Update a student's grade")
    print("5. Delete a student")
    print("6. Show class average")
    print("7. Show honor roll (grade >= 90)")
    print("8. Export all students as JSON")
    print("9. Show why SQL injection matters (safe demo, no execution)")
    print("10. Quit")
    choice = input("Choose an option (1-10): ").strip()

    if choice == "1":
        print()
        for student in list_students(connection):
            print(f"  [{student['id']}] {student['name']}: {student['grade']}")

    elif choice == "2":
        print()
        raw_id = input("Student ID: ").strip()
        if not raw_id.isdigit():
            print("Please enter a numeric ID.")
            continue
        student = find_student(connection, int(raw_id))
        if student is None:
            print("No student with that ID.")
        else:
            print(f"[{student['id']}] {student['name']}: {student['grade']}")

    elif choice == "3":
        print()
        name = input("New student's name: ").strip()
        raw_grade = input("New student's grade: ").strip()
        if not name or not raw_grade.isdigit():
            print("Please enter a name and a numeric grade.")
            continue
        # TODO 10: call add_student(connection, name, int(raw_grade)),
        # then print "Added {name}."
        pass

    elif choice == "4":
        print()
        raw_id = input("Student ID to update: ").strip()
        raw_grade = input("New grade: ").strip()
        if not raw_id.isdigit() or not raw_grade.isdigit():
            print("Please enter numeric values.")
            continue
        # TODO 11: call update_grade(connection, int(raw_id), int(raw_grade))
        # to get `updated`. If updated is None, print "No student with
        # that ID." Otherwise print
        # f"Updated: [{updated['id']}] {updated['name']}: {updated['grade']}".
        pass

    elif choice == "5":
        print()
        raw_id = input("Student ID to delete: ").strip()
        if not raw_id.isdigit():
            print("Please enter a numeric ID.")
            continue
        # TODO 12: call delete_student(connection, int(raw_id)), then
        # print "Deleted (if that ID existed)."
        pass

    elif choice == "6":
        print()
        # TODO 13: print f"Class average: {class_average(connection)}".
        pass

    elif choice == "7":
        print()
        names = honor_roll(connection)
        if not names:
            print("No students currently meet the honor roll threshold.")
        else:
            for name in names:
                print(f"  {name}")

    elif choice == "8":
        print()
        print(export_to_json(connection))

    elif choice == "9":
        print()
        print("If a search were built like this (VULNERABLE, never run):")
        print(build_unsafe_search_query("x' OR '1'='1"))
        print("A real server would match EVERY row -- the safe version")
        print("this project actually uses instead is:")
        print('cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))')

    elif choice == "10":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-10.")
