"""
Chapter 22 Practice Bank: Building Web Apps & APIs -- Flask & FastAPI -- reference solution.
Run this from inside the practice/ folder: python3 solution.py
"""

# ============================================================
# Topic 1: What a Web Framework Is & the Request/Response Cycle
# ============================================================

# TODO 1.1
def identify_method_and_path(request_line):
    method, path = request_line.split(" ", 1)
    return {"method": method, "path": path}


print(identify_method_and_path("GET /tasks"))
print(identify_method_and_path("POST /tasks"))


# TODO 1.2
def request_response_cycle_steps():
    return [
        "client sends an HTTP request (method + path)",
        "the web framework runs the matching view function",
        "the view function decides what to send back",
        "the framework sends an HTTP response (status code + body)",
    ]


for step in request_response_cycle_steps():
    print(step)


# TODO 1.3 (Debug the Code)
# Bug: claims a web framework compiles Python to machine code -- that's
# not what a web framework does at all; it listens for requests and lets
# your code decide what to respond with.
def describe_web_framework():
    return "A web framework listens for HTTP requests and lets your code decide what response to send back."


print(describe_web_framework())


# TODO 1.A (Scenario -- Choosing a Status Code)
def choose_status_code(outcome):
    codes = {
        "success": 200,
        "created": 201,
        "not_found": 404,
        "validation_failed": 422,
        "server_error": 500,
    }
    return codes.get(outcome, 400)


print(choose_status_code("success"))
print(choose_status_code("created"))
print(choose_status_code("not_found"))
print(choose_status_code("mystery"))


# TODO 1.B (Scenario -- Interview Prep)
def explain_localhost_still_networked():
    return (
        "Even a request to localhost goes through the same client-server "
        "HTTP protocol a remote request would -- the driver/framework still "
        "opens a network connection, just one that never leaves the machine."
    )


print(explain_localhost_still_networked())


# ============================================================
# Topic 2: Flask Routes & render_template
# ============================================================

# TODO 2.1
def build_route_map():
    return {
        "/": "home",
        "/about": "about",
        "/tasks": "list_tasks",
    }


print(build_route_map())


# TODO 2.2
def render_context(template_name, **context):
    return {"template": template_name, "context": context}


print(render_context("tasks.html", tasks=["a", "b"]))


# TODO 2.3 (Debug the Code)
# Bug: the view function builds a result but never returns it -- Flask
# needs a real return value to send back as the response.
def home_view(tasks):
    lines = [t["title"] for t in tasks]
    return lines


print(home_view([{"title": "Write the report"}, {"title": "Review PR"}]))


# TODO 2.A (Scenario -- Building a Dashboard Context)
def build_dashboard_context(users, tasks):
    return {
        "user_count": len(users),
        "task_count": len(tasks),
        "completed_count": sum(1 for t in tasks if t.get("done")),
    }


print(build_dashboard_context(["ana", "ben"], [{"done": True}, {"done": False}]))


# TODO 2.B (Scenario -- Interview Prep)
def explain_view_function_return_value():
    return (
        "A Flask view function's return value becomes the HTTP response body "
        "-- a string becomes a plain text/HTML response, a dict is "
        "automatically converted to JSON, and a tuple like (body, status) "
        "sets a specific status code."
    )


print(explain_view_function_return_value())


# ============================================================
# Topic 3: The Flask Request Object
# ============================================================

# TODO 3.1
def read_query_param(simulated_args, key, default=""):
    return simulated_args.get(key, default)


print(read_query_param({"q": "python"}, "q"))
print(read_query_param({}, "q", default="none"))


# TODO 3.2
def read_json_field(simulated_json_body, key, default=None):
    return simulated_json_body.get(key, default)


print(read_json_field({"title": "Water the plants"}, "title"))
print(read_json_field({}, "title", default="Untitled"))


# TODO 3.3 (Debug the Code)
# Bug: reads from a simulated request.form when the task said the data
# arrives as a JSON body (request.json) -- form and json are two
# different sources of request data.
def get_submitted_title(simulated_json_body):
    return simulated_json_body.get("title", "")


print(get_submitted_title({"title": "Buy groceries"}))


# TODO 3.A (Scenario -- Handling a Search Form)
def handle_search_form(simulated_args):
    query = simulated_args.get("q", "").strip()
    category = simulated_args.get("category", "all")
    if not query:
        return {"error": "a search term is required"}
    return {"query": query, "category": category}


print(handle_search_form({"q": "python", "category": "books"}))
print(handle_search_form({}))


# TODO 3.B (Scenario -- Interview Prep)
def explain_args_vs_form():
    return (
        "request.args reads query-string parameters from the URL itself "
        "(?key=value); request.form reads data submitted from an HTML form "
        "as a POST request's body -- both behave like a dict with .get(), "
        "but they read from two different parts of the request."
    )


print(explain_args_vs_form())


# ============================================================
# Topic 4: FastAPI Path & Query Params
# ============================================================

# TODO 4.1
def convert_path_param(raw_value, target_type):
    return target_type(raw_value)


print(convert_path_param("42", int))
print(convert_path_param("true", str))


# TODO 4.2
def classify_param(has_default, in_path_string):
    if in_path_string:
        return "path parameter"
    if has_default:
        return "query parameter"
    return "unclear"


print(classify_param(has_default=False, in_path_string=True))
print(classify_param(has_default=True, in_path_string=False))


# TODO 4.3 (Debug the Code)
# Bug: treats a query parameter (has a default) as if it were required --
# a query parameter with a default should be optional, not enforced.
def list_tasks_filtered(tasks, done=None):
    if done is None:
        return tasks
    return [t for t in tasks if t["done"] == done]


sample_tasks = [{"title": "A", "done": True}, {"title": "B", "done": False}]
print(list_tasks_filtered(sample_tasks))
print(list_tasks_filtered(sample_tasks, done=True))


# TODO 4.A (Scenario -- Building a Filtering Endpoint)
def filter_by_status(orders, status=None):
    if status is None:
        return orders
    return [o for o in orders if o.get("status") == status]


sample_orders = [{"id": 1, "status": "shipped"}, {"id": 2, "status": "pending"}]
print(filter_by_status(sample_orders))
print(filter_by_status(sample_orders, status="pending"))


# TODO 4.B (Scenario -- Interview Prep)
def explain_path_param_conversion_failure():
    return (
        "If a path parameter can't convert to its type hint (e.g. "
        "'/tasks/abc' against task_id: int), FastAPI automatically responds "
        "with a 422 error describing the problem -- the route function "
        "never even runs."
    )


print(explain_path_param_conversion_failure())


# ============================================================
# Topic 5: Pydantic Models & Automatic Docs
# ============================================================

# TODO 5.1
def has_required_fields(body, required_fields):
    return all(field in body for field in required_fields)


print(has_required_fields({"title": "X", "done": False}, ["title"]))
print(has_required_fields({"done": False}, ["title"]))


# TODO 5.2
def apply_default(body, field, default_value):
    result = dict(body)
    result.setdefault(field, default_value)
    return result


print(apply_default({"title": "X"}, "done", False))
print(apply_default({"title": "X", "done": True}, "done", False))


# TODO 5.3 (Debug the Code)
# Bug: accepted any truthy value for a boolean field instead of checking
# isinstance(value, bool) -- a Pydantic model would reject a string like
# "yes" for a bool field, not silently treat it as True.
def validate_boolean_field(body, field):
    if field not in body:
        return True
    return isinstance(body[field], bool)


print(validate_boolean_field({"done": True}, "done"))
print(validate_boolean_field({"done": "yes"}, "done"))
print(validate_boolean_field({}, "done"))


# TODO 5.A (Scenario -- Designing a Signup Model)
def validate_signup_data(body):
    if "email" not in body or not isinstance(body["email"], str):
        return False, "email is required and must be a string"
    if "age" in body and not isinstance(body["age"], int):
        return False, "age must be an integer"
    return True, None


print(validate_signup_data({"email": "a@example.com"}))
print(validate_signup_data({"email": "a@example.com", "age": 30}))
print(validate_signup_data({"age": 30}))
print(validate_signup_data({"email": "a@example.com", "age": "thirty"}))


# TODO 5.B (Scenario -- Interview Prep)
def explain_docs_generation():
    return (
        "FastAPI's /docs page is generated automatically from route "
        "signatures and Pydantic models -- every parameter, type hint, and "
        "model field is already real, checked information, so the docs "
        "page is built directly from it with nothing written by hand."
    )


print(explain_docs_generation())


# ============================================================
# Topic 6: Flask vs. FastAPI, Side by Side
# ============================================================

# TODO 6.1
def recommend_framework_for(project_description):
    if "server-rendered" in project_description or "html page" in project_description.lower():
        return "Flask"
    if "json api" in project_description.lower() or "mobile app backend" in project_description.lower():
        return "FastAPI"
    return "either could work"


print(recommend_framework_for("A simple server-rendered admin dashboard"))
print(recommend_framework_for("A JSON API for a mobile app backend"))


# TODO 6.2
def describe_validation_style(framework_name):
    if framework_name == "Flask":
        return "manual, with if statements and try/except"
    if framework_name == "FastAPI":
        return "automatic, driven by Pydantic model type hints"
    return "unknown framework"


print(describe_validation_style("Flask"))
print(describe_validation_style("FastAPI"))


# TODO 6.3 (Debug the Code)
# Bug: overstates that Flask "cannot" return JSON -- Flask CAN return a
# dict (auto-converted to JSON), it's just not its idiomatic default the
# way it is for FastAPI.
def can_flask_return_json():
    return True  # Flask can return a dict, auto-converted to JSON


print(can_flask_return_json())


# TODO 6.A (Scenario -- Picking a Framework for a New Feature)
def recommend_framework(needs_html_page, needs_automatic_docs):
    if needs_html_page and not needs_automatic_docs:
        return "Flask"
    if needs_automatic_docs and not needs_html_page:
        return "FastAPI"
    return "either could work, depending on team preference"


print(recommend_framework(True, False))
print(recommend_framework(False, True))


# TODO 6.B (Scenario -- Interview Prep)
def elevator_pitch_flask_vs_fastapi():
    return (
        "Flask is the simpler, classic choice for server-rendered HTML "
        "pages with untyped-by-default request handling; FastAPI is built "
        "for typed JSON APIs, using Pydantic models to drive automatic "
        "validation and interactive docs -- pick based on whether the app "
        "mainly renders pages or mainly serves data to something else."
    )


print(elevator_pitch_flask_vs_fastapi())


# ============================================================
# Topic 7: What's Next -- HTML, JSON, and Where React Fits
# ============================================================

# TODO 7.1
def classify_response_body(response_body):
    if isinstance(response_body, str):
        return "HTML"
    if isinstance(response_body, (dict, list)):
        return "JSON-shaped data"
    return "unknown"


print(classify_response_body("<html>...</html>"))
print(classify_response_body({"title": "X"}))


# TODO 7.2
def needs_something_else_to_render(response_body):
    return isinstance(response_body, (dict, list))


print(needs_something_else_to_render({"title": "X"}))
print(needs_something_else_to_render("<html>...</html>"))


# TODO 7.3 (Debug the Code)
# Bug: claims a JSON API is a complete website by itself -- it isn't; it's
# deliberately meant to be consumed by something else (a frontend, mobile
# app, or script) that renders the actual screen.
def is_json_api_a_complete_website():
    return False  # it needs a separate consumer to render anything visual


print(is_json_api_a_complete_website())


# TODO 7.A (Scenario -- Planning a New Product's Architecture)
def recommend_architecture(needs_mobile_app, needs_multiple_frontends):
    if needs_mobile_app or needs_multiple_frontends:
        return "JSON API (FastAPI) + separate frontend(s)"
    return "server-rendered HTML (Flask) is simplest"


print(recommend_architecture(needs_mobile_app=True, needs_multiple_frontends=False))
print(recommend_architecture(needs_mobile_app=False, needs_multiple_frontends=False))


# TODO 7.B (Scenario -- Interview Prep)
def explain_frontend_role_conceptually():
    return (
        "A frontend like React runs in the browser and makes HTTP requests "
        "to a JSON API, the same kind of request Chapter 19's requests "
        "library made from Python -- it then uses the JSON response to "
        "decide what to display, without this course teaching any "
        "React/JavaScript syntax itself."
    )


print(explain_frontend_role_conceptually())

