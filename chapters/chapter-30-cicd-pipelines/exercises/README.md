# Chapter 30 Exercises: CI/CD Pipelines

These exercises use what Chapter 30 covered: GitHub Actions workflow
structure (`on` / `jobs` / `steps`), what makes a workflow file
actually valid, and reading a broken workflow closely enough to spot
a real structural bug. Unlike Chapters 28-29, there's no live git
remote or GitHub server involved here -- instead, you'll validate real
workflow YAML files with Python's `yaml` module (`pyyaml`), the same
way a maintainer sanity-checks a workflow before ever pushing it.

## Setup

This chapter's exercises need `pyyaml`, which isn't in the Python
standard library:

```bash
pip install pyyaml
```

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

This builds a `scenario/` folder containing:

- `scenario/sample_project/` -- a tiny sample Python project
  (`app.py`, `test_app.py`, `requirements.txt`) with its own
  `.github/workflows/` folder:
  - `ci.yml` -- a real, valid lint + test workflow, structured exactly
    like Sub-topic 3/4 of the lesson (checkout, setup-python with a
    matrix, install, lint, test).
  - `ci-broken.yml` -- **Task 4's Debug the Code file**: it looks
    almost identical, but has a genuine structural bug.

`scenario/` is gitignored -- it's a disposable scratch environment.
Delete it and re-run `python3 starter.py` any time to reset it to a
clean starting state.

## Task 1 — Parse a workflow file for real

Open `starter.py` and find `load_workflow()` (already implemented for
you). Call it directly against `scenario/sample_project/.github/workflows/ci.yml`
and print the result:

```python
from starter import load_workflow
workflow = load_workflow("scenario/sample_project/.github/workflows/ci.yml")
print(workflow["jobs"].keys())
```

Confirm it parses into a normal Python dict, with `workflow["jobs"]`
containing one job, `lint-and-test`.

## Task 2 — TODO 1: `validate_workflow_structure()`

Fill in `validate_workflow_structure(workflow)` in `starter.py`. Given
an already-parsed workflow dict, it should return a list of problem
strings describing anything structurally wrong (an empty list means
the workflow is valid). Specifically check:

- a truthy `on` key is present (watch out: PyYAML's YAML 1.1 parser
  reads the bare key `on:` as the *boolean* `True`, not the string
  `"on"` -- so check for either key)
- a non-empty `jobs` dict is present
- every job has **both** `runs-on` and `steps`
- every job's `steps` is a non-empty list

## Task 3 — TODO 2: `validate_workflow_file()`

Fill in `validate_workflow_file(path)` to combine `load_workflow()`
and `validate_workflow_structure()` into one function returning
`(is_valid, problems)`. If the file isn't even valid YAML at all (a
genuine syntax error), catch `yaml.YAMLError` and return
`(False, ["not valid YAML: ..."])` instead of crashing.

Run it against `ci.yml` -- it should report `(True, [])`.

## Task 4 — Debug the Code: `ci-broken.yml`

This is the `.debug-card` task -- see `index.html` for the full
scenario. `ci-broken.yml` looks nearly identical to `ci.yml`, but one
required key is missing from its one job.

**Diagnose it, then fix it for real:**

1. Open `scenario/sample_project/.github/workflows/ci-broken.yml`
   directly and read it against Sub-topic 2 of the lesson (a job needs
   both `runs-on` and `steps`).
2. Run your `validate_workflow_file()` from Task 3 against it and
   confirm it reports the exact missing key.
3. Fix the file by hand (add the missing `runs-on: ubuntu-latest`
   line back in) and re-validate -- it should now report `(True, [])`.

## Checking your work

`solution.py` builds the same scenario and runs the full, working
validator against both files, printing the real result of each:

```bash
python3 solution.py
```

Its output should show `ci.yml` validating cleanly, and
`ci-broken.yml` failing with exactly one problem: a missing `runs-on`
key on the `lint-and-test` job. Compare your own `starter.py`
implementation's output against this.
