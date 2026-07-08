"""
Chapter 21 Project: Student Record Management System -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: a mock database
layer (FakeConnection/FakeCursor) implementing the real
mysql-connector-python interface (cursor(), execute(sql, params),
fetchall(), fetchone(), commit()), demonstrating parameterized-query
safety and CRUD reporting. No real network access or database connection
happens anywhere in this file, so it runs the same way for every learner,
every time.
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


def add_student(connection, name, grade):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)", (name, grade))
    connection.commit()


def list_students(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


def find_student(connection, student_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    return cursor.fetchone()


def update_grade(connection, student_id, new_grade):
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (new_grade, student_id))
    connection.commit()
    return find_student(connection, student_id)


def delete_student(connection, student_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    connection.commit()


def class_average(connection):
    students = list_students(connection)
    if not students:
        return 0
    return round(sum(s["grade"] for s in students) / len(students), 2)


def honor_roll(connection, threshold=90):
    students = list_students(connection)
    return sorted(s["name"] for s in students if s["grade"] >= threshold)


def export_to_json(connection):
    students = list_students(connection)
    return json.dumps(students, indent=2)


def build_unsafe_search_query(name):
    return f"SELECT * FROM students WHERE name = '{name}'"


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
        add_student(connection, name, int(raw_grade))
        print(f"Added {name}.")

    elif choice == "4":
        print()
        raw_id = input("Student ID to update: ").strip()
        raw_grade = input("New grade: ").strip()
        if not raw_id.isdigit() or not raw_grade.isdigit():
            print("Please enter numeric values.")
            continue
        updated = update_grade(connection, int(raw_id), int(raw_grade))
        if updated is None:
            print("No student with that ID.")
        else:
            print(f"Updated: [{updated['id']}] {updated['name']}: {updated['grade']}")

    elif choice == "5":
        print()
        raw_id = input("Student ID to delete: ").strip()
        if not raw_id.isdigit():
            print("Please enter a numeric ID.")
            continue
        delete_student(connection, int(raw_id))
        print("Deleted (if that ID existed).")

    elif choice == "6":
        print()
        print(f"Class average: {class_average(connection)}")

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
