# Chapter 22 Exercises: Building Web Apps & APIs — Flask & FastAPI

These exercises use what Chapter 22 covered: the logic behind a Flask
route (`render_template`-style context building, reading `request.args`/
`request.json`-shaped data), and the logic behind a FastAPI route (path
parameter type conversion, query parameters, and Pydantic-style
validation). Every task here is a **plain Python function** modeling
exactly what a real route function does with its inputs -- nothing in
this folder starts a live Flask/FastAPI server or makes a real HTTP
request, since this sandbox has no way to run one.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — Building a Flask template's context

Find `# TODO 1`. Write `build_task_lines(tasks)` — given a list of task
dicts (each with `"title"` and `"done"`), return a list of strings like
`"Write the report -- Pending"`, the same content a `render_template()`
call would receive as its context.

## Task 2 — Reading a Flask query parameter

Find `# TODO 2`. Write `handle_search(simulated_args)` — given a
dict standing in for `request.args`, return `f"Searching for: {q}"` if a
`"q"` key is present and non-empty, otherwise `"No search term
provided."`.

## Task 3 — Reading a Flask JSON body

Find `# TODO 3`. Write `handle_create_task(simulated_json_body)` — given
a dict standing in for `request.json`, return `({"created": title}, 201)`
if `"title"` is present and non-empty, otherwise
`({"error": "title is required"}, 400)`.

## Task 4 — A FastAPI-style path parameter lookup

Find `# TODO 4`. Write `get_task(tasks, task_id)` — given a dict of
`{id: task_dict}` and an int `task_id`, return the matching task dict, or
`{"error": "not found"}` if no task has that ID.

## Task 5 — A FastAPI-style query parameter filter

Find `# TODO 5`. Write `list_tasks(tasks, done=None)` — given the same
dict of tasks, return every task if `done` is `None`, otherwise only
tasks whose `"done"` field matches `done`.

## Task 6 — Pydantic-style validation

Find `# TODO 6`. Write `validate_task_shape(body)` — given a dict, return
`(True, None)` if it has a string `"title"` and (if present) a boolean
`"done"`; otherwise return `(False, <a message describing what's wrong>)`.

## Task 7 — Comparing Flask vs. FastAPI defaults

Find `# TODO 7`. Write `default_response_shape(framework_name)` —
return `"HTML"` for `"Flask"`, `"JSON"` for `"FastAPI"`, and `"unknown"`
otherwise.

## Task 8 — Recognizing what React would need

Find `# TODO 8`. Write `is_consumable_by_a_frontend(response_body)` —
return `True` if `response_body` is a `dict` or `list` (JSON-shaped data
a frontend like React could parse and render), `False` if it's a `str`
(already-rendered HTML, nothing left for a frontend to do).

## Task 9 — Debug the Code

Find `# TODO 9`. This is supposed to build a query-parameter dict lookup
the way FastAPI would, but it crashes on a missing key instead of
returning a sensible default. Find and fix it.

## Checking your work

Compare your output against `solution.py`. Every task's output is exactly
reproducible, every time -- nothing in this chapter's exercises depends on
timing or a live server.
