# Chapter 22 Practice Bank: Building Web Apps & APIs — Flask & FastAPI

A deeper set of practice problems, organized by topic, on top of the main
`exercises/` folder — including scenario-based problems written in the
same style you'll see in real interviews. This is the chapter where
Flask's and FastAPI's real route/request/model concepts become allowed,
on top of everything from Chapters 1-21. Every task here is a plain
Python function or class modeling exactly what a real route function
does with its inputs — no live Flask/FastAPI server or installed
framework is needed anywhere in this bank. No import beyond
`json`/`os`/`re`/`math`/`datetime`/`random`/`csv`/`threading`/`concurrent.futures`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: What a Web Framework Is & the Request/Response Cycle

1. Identify the method and path from a request description.
2. List the shared request-response cycle steps.
3. **Debug the Code:** fix a claim that a web framework compiles Python to machine code.
4. **Scenario — Choosing a Status Code:** write `choose_status_code()`.
5. **Scenario — Interview Prep:** explain why "localhost" still involves a network connection.

## Topic 2: Flask Routes & render_template

1. Build a route's path-to-function mapping as a dict.
2. Write a reusable `render_context()` helper.
3. **Debug the Code:** fix code that forgot to return a value from a view function.
4. **Scenario — Building a Dashboard Context:** write `build_dashboard_context()`.
5. **Scenario — Interview Prep:** explain what a view function's return value becomes.

## Topic 3: The Flask Request Object

1. Read a value from a simulated `request.args`.
2. Read a value from a simulated `request.json` with a default.
3. **Debug the Code:** fix code that used `request.form` where `request.json` was needed.
4. **Scenario — Handling a Search Form:** write `handle_search_form()`.
5. **Scenario — Interview Prep:** explain the difference between `request.args` and `request.form`.

## Topic 4: FastAPI Path & Query Params

1. Convert a URL path string's parameter to the right type.
2. Distinguish a path parameter from a query parameter.
3. **Debug the Code:** fix code that treated a query parameter as required.
4. **Scenario — Building a Filtering Endpoint:** write `filter_by_status()`.
5. **Scenario — Interview Prep:** explain what happens when a path parameter fails type conversion.

## Topic 5: Pydantic Models & Automatic Docs

1. Validate a dict against a simple required-fields list.
2. Apply a default value the way an optional Pydantic field would.
3. **Debug the Code:** fix validation code that accepted a non-boolean as a boolean field.
4. **Scenario — Designing a Signup Model:** write `validate_signup_data()`.
5. **Scenario — Interview Prep:** explain what generates FastAPI's `/docs` page.

## Topic 6: Flask vs. FastAPI, Side by Side

1. Recommend a framework for a described project.
2. Describe what changes between the two frameworks' validation styles.
3. **Debug the Code:** fix an overstated claim that Flask "cannot" return JSON.
4. **Scenario — Picking a Framework for a New Feature:** write `recommend_framework()`.
5. **Scenario — Interview Prep:** give a 30-second Flask-vs-FastAPI comparison.

## Topic 7: What's Next — HTML, JSON, and Where React Fits

1. Classify a response body as HTML or JSON-shaped data.
2. Decide whether a given response needs "something else" to render it.
3. **Debug the Code:** fix a claim that a JSON API is a complete website by itself.
4. **Scenario — Planning a New Product's Architecture:** write `recommend_architecture()`.
5. **Scenario — Interview Prep:** explain, without teaching React syntax, what a frontend does with a JSON API's response.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks. One exception: Topic 3's debug task
intentionally demonstrates a real `AttributeError` (calling a
form-only method on a plain dict standing in for a JSON body) before
it's fixed — that's the whole point of that task. Every other task's
output is exactly reproducible.
