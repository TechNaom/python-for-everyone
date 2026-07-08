"""
Chapter 22 Exercises: Building Web Apps & APIs -- Flask & FastAPI -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""


# TODO 1
def build_task_lines(tasks):
    lines = []
    for task in tasks:
        status = "Done" if task["done"] else "Pending"
        lines.append(f"{task['title']} -- {status}")
    return lines


tasks_1 = [
    {"title": "Write the report", "done": False},
    {"title": "Review pull request", "done": True},
]
for line in build_task_lines(tasks_1):
    print(line)


# TODO 2
def handle_search(simulated_args):
    query = simulated_args.get("q", "")
    return f"Searching for: {query}" if query else "No search term provided."


print(handle_search({"q": "python"}))
print(handle_search({}))


# TODO 3
def handle_create_task(simulated_json_body):
    title = simulated_json_body.get("title", "")
    if not title:
        return {"error": "title is required"}, 400
    return {"created": title}, 201


print(handle_create_task({"title": "Water the plants"}))
print(handle_create_task({}))


# TODO 4
def get_task(tasks, task_id):
    return tasks.get(task_id, {"error": "not found"})


TASKS = {
    1: {"title": "Write the report", "done": False},
    2: {"title": "Review pull request", "done": True},
}
print(get_task(TASKS, 2))
print(get_task(TASKS, 99))


# TODO 5
def list_tasks(tasks, done=None):
    if done is None:
        return tasks
    return {tid: t for tid, t in tasks.items() if t["done"] == done}


print(list_tasks(TASKS))
print(list_tasks(TASKS, done=True))


# TODO 6
def validate_task_shape(body):
    if "title" not in body or not isinstance(body["title"], str):
        return False, "title is required and must be a string"
    if "done" in body and not isinstance(body["done"], bool):
        return False, "done must be a boolean"
    return True, None


print(validate_task_shape({"title": "Water the plants"}))
print(validate_task_shape({"done": True}))
print(validate_task_shape({"title": "Water the plants", "done": "yes"}))


# TODO 7
def default_response_shape(framework_name):
    if framework_name == "Flask":
        return "HTML"
    if framework_name == "FastAPI":
        return "JSON"
    return "unknown"


print(default_response_shape("Flask"))
print(default_response_shape("FastAPI"))
print(default_response_shape("Django"))


# TODO 8
def is_consumable_by_a_frontend(response_body):
    return isinstance(response_body, (dict, list))


print(is_consumable_by_a_frontend({"title": "Water the plants"}))
print(is_consumable_by_a_frontend(["a", "b"]))
print(is_consumable_by_a_frontend("<html>...</html>"))


# TODO 9 (Debug the Code)
# Bug: simulated_query_params[key] raises KeyError for any missing key.
# Fix: use .get(key, default), the safe dict-lookup pattern.
def get_query_param(simulated_query_params, key, default=None):
    return simulated_query_params.get(key, default)


debug_params = {"limit": "10"}
print(get_query_param(debug_params, "limit"))
print(get_query_param(debug_params, "offset", default="0"))

