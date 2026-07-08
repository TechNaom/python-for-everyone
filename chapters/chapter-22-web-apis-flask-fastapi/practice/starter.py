"""
Chapter 22 Practice Bank: Building Web Apps & APIs -- Flask & FastAPI
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py
"""

# ============================================================
# Topic 1: What a Web Framework Is & the Request/Response Cycle
# ============================================================

# TODO 1.1: Write identify_method_and_path(request_line). Given a string
# like "GET /tasks", split it on the first space and return
# {"method": method, "path": path}.


# TODO 1.2: Write request_response_cycle_steps() returning a list of 4
# strings describing, in order: the client sends a request, the framework
# runs the matching view function, the view function decides what to
# send back, the framework sends the response.


# TODO 1.3 (Debug the Code): describe_web_framework() below wrongly
# claims a web framework compiles Python to machine code. Fix its return
# value to correctly describe what a web framework actually does.
def describe_web_framework():
    return "A web framework compiles your Python code into machine code for speed."


print(describe_web_framework())


# TODO 1.A (Scenario -- Choosing a Status Code): write
# choose_status_code(outcome), mapping "success"->200, "created"->201,
# "not_found"->404, "validation_failed"->422, "server_error"->500, and
# anything else -> 400.


# TODO 1.B (Scenario -- Interview Prep): write
# explain_localhost_still_networked() returning a short explanation of
# why even a "localhost" connection still goes through the same
# client-server protocol a remote connection would.


# ============================================================
# Topic 2: Flask Routes & render_template
# ============================================================

# TODO 2.1: Write build_route_map() returning a dict mapping "/" ->
# "home", "/about" -> "about", "/tasks" -> "list_tasks".


# TODO 2.2: Write render_context(template_name, **context) returning
# {"template": template_name, "context": context}.


# TODO 2.3 (Debug the Code): home_view() below builds a list of titles
# but never returns it -- Flask needs a real return value to send back
# as the response. Fix it.
def home_view(tasks):
    lines = [t["title"] for t in tasks]


print(home_view([{"title": "Write the report"}, {"title": "Review PR"}]))


# TODO 2.A (Scenario -- Building a Dashboard Context): write
# build_dashboard_context(users, tasks) returning
# {"user_count": ..., "task_count": ..., "completed_count": ...} where
# completed_count counts tasks with a truthy "done" field.


# TODO 2.B (Scenario -- Interview Prep): write
# explain_view_function_return_value() describing what a Flask view
# function's return value becomes (a string, a dict, or a tuple with a
# status code).


# ============================================================
# Topic 3: The Flask Request Object
# ============================================================

# TODO 3.1: Write read_query_param(simulated_args, key, default="")
# returning simulated_args.get(key, default).


# TODO 3.2: Write read_json_field(simulated_json_body, key, default=None)
# returning simulated_json_body.get(key, default).


# TODO 3.3 (Debug the Code): get_submitted_title() below is supposed to
# read a "title" field from a JSON request body, but it's written as if
# reading a Flask FORM submission (request.form) rather than a JSON body
# (request.json) -- this simulated dict below only has the field
# available directly, via .get(). Fix the function so it actually reads
# it correctly (hint: the bug here is calling a method that doesn't exist
# on a plain dict -- .getlist() is a request.form-only method, not
# available on request.json's plain dict).
def get_submitted_title(simulated_json_body):
    return simulated_json_body.getlist("title")


print(get_submitted_title({"title": "Buy groceries"}))


# TODO 3.A (Scenario -- Handling a Search Form): write
# handle_search_form(simulated_args) reading "q" (required, stripped of
# whitespace) and "category" (default "all") from simulated_args. Return
# {"error": "a search term is required"} if q is empty after stripping,
# otherwise {"query": q, "category": category}.


# TODO 3.B (Scenario -- Interview Prep): write explain_args_vs_form()
# describing the difference between request.args and request.form.


# ============================================================
# Topic 4: FastAPI Path & Query Params
# ============================================================

# TODO 4.1: Write convert_path_param(raw_value, target_type) returning
# target_type(raw_value) -- the same conversion FastAPI performs
# automatically based on a path parameter's type hint.


# TODO 4.2: Write classify_param(has_default, in_path_string) returning
# "path parameter" if in_path_string is True, "query parameter" if
# has_default is True (and in_path_string is False), otherwise "unclear".


# TODO 4.3 (Debug the Code): list_tasks_filtered() below treats `done`
# as required (it crashes if done isn't passed), but the task said it
# should be an OPTIONAL query parameter with a default of None, returning
# every task unfiltered when not given. Fix it.
def list_tasks_filtered(tasks, done):
    return [t for t in tasks if t["done"] == done]


sample_tasks = [{"title": "A", "done": True}, {"title": "B", "done": False}]
print(list_tasks_filtered(sample_tasks, done=None))
print(list_tasks_filtered(sample_tasks, done=True))


# TODO 4.A (Scenario -- Building a Filtering Endpoint): write
# filter_by_status(orders, status=None) returning every order if status
# is None, otherwise only orders whose "status" field matches.


# TODO 4.B (Scenario -- Interview Prep): write
# explain_path_param_conversion_failure() describing what FastAPI does
# automatically when a path parameter can't convert to its type hint.


# ============================================================
# Topic 5: Pydantic Models & Automatic Docs
# ============================================================

# TODO 5.1: Write has_required_fields(body, required_fields) returning
# True if every field in required_fields is a key in body.


# TODO 5.2: Write apply_default(body, field, default_value) returning a
# NEW dict equal to body, with default_value set for field only if field
# isn't already present (hint: dict.setdefault()).


# TODO 5.3 (Debug the Code): validate_boolean_field() below accepts ANY
# truthy value as if it were a valid boolean field (e.g. it wrongly
# accepts the string "yes") -- a real Pydantic model would reject
# anything that isn't actually a bool. Fix it.
def validate_boolean_field(body, field):
    if field not in body:
        return True
    return bool(body[field])


print(validate_boolean_field({"done": True}, "done"))
print(validate_boolean_field({"done": "yes"}, "done"))
print(validate_boolean_field({}, "done"))


# TODO 5.A (Scenario -- Designing a Signup Model): write
# validate_signup_data(body). Require "email" to be present and a str.
# If "age" is present, it must be an int. Return (True, None) if valid,
# otherwise (False, "<a clear message>").


# TODO 5.B (Scenario -- Interview Prep): write explain_docs_generation()
# describing what FastAPI's /docs page is generated from.


# ============================================================
# Topic 6: Flask vs. FastAPI, Side by Side
# ============================================================

# TODO 6.1: Write recommend_framework_for(project_description). Return
# "Flask" if the description (case-insensitive) mentions "server-rendered"
# or "html page"; "FastAPI" if it mentions "json api" or "mobile app
# backend"; otherwise "either could work".


# TODO 6.2: Write describe_validation_style(framework_name). Return
# "manual, with if statements and try/except" for "Flask", "automatic,
# driven by Pydantic model type hints" for "FastAPI", "unknown framework"
# otherwise.


# TODO 6.3 (Debug the Code): can_flask_return_json() below wrongly
# claims Flask CANNOT return JSON. Flask CAN return a dict, which it
# automatically converts to a JSON response. Fix the return value.
def can_flask_return_json():
    return False


print(can_flask_return_json())


# TODO 6.A (Scenario -- Picking a Framework for a New Feature): write
# recommend_framework(needs_html_page, needs_automatic_docs). Return
# "Flask" if needs_html_page and not needs_automatic_docs; "FastAPI" if
# needs_automatic_docs and not needs_html_page; otherwise "either could
# work, depending on team preference".


# TODO 6.B (Scenario -- Interview Prep): write
# elevator_pitch_flask_vs_fastapi() giving a short (2-3 sentence)
# Flask-vs-FastAPI comparison.


# ============================================================
# Topic 7: What's Next -- HTML, JSON, and Where React Fits
# ============================================================

# TODO 7.1: Write classify_response_body(response_body). Return "HTML" if
# it's a str, "JSON-shaped data" if it's a dict or list, "unknown"
# otherwise.


# TODO 7.2: Write needs_something_else_to_render(response_body) returning
# True if response_body is a dict or list, False otherwise.


# TODO 7.3 (Debug the Code): is_json_api_a_complete_website() below
# wrongly claims a JSON API IS a complete website by itself. It isn't --
# it's deliberately meant to be consumed by something else that renders
# the actual screen. Fix the return value.
def is_json_api_a_complete_website():
    return True


print(is_json_api_a_complete_website())


# TODO 7.A (Scenario -- Planning a New Product's Architecture): write
# recommend_architecture(needs_mobile_app, needs_multiple_frontends).
# Return "JSON API (FastAPI) + separate frontend(s)" if either argument
# is True, otherwise "server-rendered HTML (Flask) is simplest".


# TODO 7.B (Scenario -- Interview Prep): write
# explain_frontend_role_conceptually() describing, WITHOUT teaching any
# React/JavaScript syntax, what a frontend like React does with a JSON
# API's response.

