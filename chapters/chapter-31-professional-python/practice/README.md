# Chapter 31 Practice Bank: Professional Python

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews.

This chapter covers venv, project structure, logging, argparse,
packaging basics, and shipping a CLI tool. Topics 1, 2, and 5 (virtual
environments, project structure, packaging) are command-line and
config-file skills, not Python logic — so those problems are Python
functions that **simulate or reason about** a described venv/pip/
pyproject state using plain data (strings, lists, dicts) standing in
for real terminal output or file contents, the same way Chapter 28's
git problems worked. Every claim in those problems was checked against
real `venv`/`pip`/Python behavior in a scratch directory before being
written down here. Topics 3 and 4 (logging, argparse) are real,
runnable Python using the standard library's `logging` and `argparse`
modules. Standard library only, no installs needed.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Virtual Environments

1. Detect whether code is running inside an active venv.
2. Parse `pip freeze` output into a dict of package -> version.
3. **Debug the Code:** fix a wrong claim that global installs have no downsides.
4. **Scenario — Comparing Two Approaches:** write `recommended_venv_command()`.
5. **Scenario — Interview Prep:** explain why venv per project matters.

## Topic 2: Project Structure

1. Check a file list for a minimal professional layout.
2. Decide whether a directory needs an `__init__.py`.
3. **Debug the Code:** fix a wrong claim about where tests should live.
4. **Scenario — Comparing Two Approaches:** write `choose_layout()`.
5. **Scenario — Interview Prep:** explain why structure matters on a team.

## Topic 3: Logging

1. Map a numeric log level to its name.
2. Decide whether a message would be emitted given a logger's threshold.
3. **Debug the Code:** fix a broken log format string.
4. Return the root logger's default level.
5. Count how many of a batch of messages would actually be emitted.
6. **Scenario — Comparing Two Approaches:** write `choose_log_level_for_environment()`.
7. **Scenario — Interview Prep:** explain why silent production failures need logging, not `print()`.

## Topic 4: argparse

1. Count how many `add_argument()` calls a parser needs.
2. Build and parse a real parser with a positional argument and a flag.
3. **Debug the Code:** fix a wrong claim about which arguments are required by default.
4. Return the exit code argparse uses for a missing required argument.
5. Build and parse a real parser using a `count` action.
6. **Scenario — Comparing Two Approaches:** write `choose_argparse_action()`.
7. **Scenario — Interview Prep:** explain why argparse beats manually indexing `sys.argv`.

## Topic 5: Packaging Basics (pyproject.toml)

1. Check whether a `[project]` table has the minimum required fields.
2. Classify a dependency version specifier's pin style.
3. **Debug the Code:** fix a wrong claim that pyproject.toml is purely style.
4. **Scenario — Comparing Two Approaches:** write `choose_dependency_pin()`.
5. **Scenario — Interview Prep:** explain why professional projects pin dependencies.

## Topic 6: Putting It Together — A Shippable CLI Tool

1. Check a file list against the minimum bar for a shippable CLI.
2. Build a `[project.scripts]` entry-point line.
3. **Debug the Code:** fix a wrong claim about `pip install -e .`.
4. **Scenario — Comparing Two Approaches:** write `choose_install_mode()`.
5. **Scenario — Interview Prep:** explain the full checklist that turns a script into a shippable tool.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks. Every
data-driven and real-Python task's output is exactly reproducible.
