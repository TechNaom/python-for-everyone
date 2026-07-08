"""
Chapter 22 Exercises: Building Web Apps & APIs -- Flask & FastAPI
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every task here is a plain Python function modeling exactly what a real
Flask or FastAPI route function does with its inputs. No live server
starts anywhere in this file, and no real HTTP request is ever made --
this sandbox has no way to run one, so every task is written as testable,
isolated logic instead.
"""


# TODO 1: Write build_task_lines(tasks). Given a list of dicts like
# {"title": "Write the report", "done": False}, return a list of strings
# "TITLE -- Pending" or "TITLE -- Done" for each task, in order. This is
# the same context-building logic a Flask route would hand to
# render_template().


# TODO 2: Write handle_search(simulated_args). simulated_args is a dict
# standing in for Flask's request.args. If it has a non-empty "q" key,
# return f"Searching for: {q}". Otherwise return "No search term provided."


# TODO 3: Write handle_create_task(simulated_json_body). simulated_json_body
# is a dict standing in for Flask's request.json. If it has a non-empty
# "title" key, return ({"created": title}, 201). Otherwise return
# ({"error": "title is required"}, 400).


# TODO 4: Write get_task(tasks, task_id). tasks is a dict of {id: task_dict}
# (like FastAPI's TASKS in the lesson). Return tasks.get(task_id), or
# {"error": "not found"} if task_id isn't a key in tasks.


# TODO 5: Write list_tasks(tasks, done=None). tasks is the same dict of
# {id: task_dict}. If done is None, return tasks unchanged. Otherwise
# return a new dict containing only the tasks whose "done" field equals
# the done argument -- the same filtering FastAPI's query-parameter
# version does.


# TODO 6: Write validate_task_shape(body). body is a dict. Return
# (True, None) if body has a "title" key whose value is a str, AND (if
# "done" is present at all) "done"'s value is a bool. Otherwise return
# (False, "title is required and must be a string") or
# (False, "done must be a boolean") as appropriate -- the same shape
# Pydantic's automatic validation checks.


# TODO 7: Write default_response_shape(framework_name). Return "HTML" for
# "Flask", "JSON" for "FastAPI", and "unknown" for anything else.


# TODO 8: Write is_consumable_by_a_frontend(response_body). Return True if
# response_body is a dict or a list (JSON-shaped data a frontend like
# React could parse), False if it's a str (already-rendered HTML, with
# nothing left for a frontend to parse and render itself).


# TODO 9 (Debug the Code): this is supposed to look up a query parameter
# the way FastAPI would -- returning a default value if the key isn't
# present -- but it crashes with a KeyError on any missing key instead.
# Find and fix it (hint: dicts have a safe .get(key, default) method,
# the same one Chapter 8 introduced).
def get_query_param(simulated_query_params, key, default=None):
    return simulated_query_params[key]


debug_params = {"limit": "10"}
print(get_query_param(debug_params, "limit"))
print(get_query_param(debug_params, "offset", default="0"))

