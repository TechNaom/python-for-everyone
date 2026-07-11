"""
Chapter 31 Practice Bank: Professional Python (venv, project structure,
logging, argparse, packaging, shippable CLI)
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Standard library only -- no installs needed. Topics 1, 2, and 5 (venv,
project structure, packaging) are command-line/config-file skills, not
Python logic -- those problems are Python functions that REASON ABOUT a
described venv/pip/pyproject state using plain data (strings, lists,
dicts) standing in for real terminal output or file contents, the same
way chapter 28's git problems worked. Every claim was checked against
real venv/pip/python behavior in a scratch directory before being
written into this file. Topics 3 and 4 (logging, argparse) are real,
runnable Python using the standard library's logging and argparse
modules.
"""

import argparse
import logging

# ============================================================
# Topic 1: Virtual Environments
# ============================================================

# TODO 1.1: Write is_running_in_venv(sys_prefix, sys_base_prefix). Python
# sets sys.prefix to the venv's own directory when a virtual environment
# is active, while sys.base_prefix stays the system Python's directory.
# Outside any venv, the two are equal. Return True if sys_prefix !=
# sys_base_prefix (i.e. a venv is active), else False.


# TODO 1.2: Write parse_pip_freeze(freeze_output). Given the multi-line
# string output of `pip freeze` (one "package==version" per line, e.g.
# "requests==2.34.2\nidna==3.18"), return a dict mapping each package
# name to its version string, e.g. {"requests": "2.34.2", "idna":
# "3.18"}. Ignore blank lines.


# TODO 1.3 (Debug the Code): explain_global_installs() below wrongly
# claims installing packages globally (outside any venv) is always the
# faster, simpler choice with no downsides for team projects. Fix its
# return value -- global installs mean every project on the machine
# shares one set of package versions, so two projects needing different
# versions of the same library will conflict, and a teammate's machine
# won't reproducibly match yours.
def explain_global_installs():
    return "Installing packages globally is always fine for a team project -- there are no downsides, and it's faster than making a venv."


print(explain_global_installs())


# TODO 1.A (Scenario -- Comparing Two Approaches): write
# recommended_venv_command(venv_already_exists). A teammate is starting
# work on a project. Return "python3 -m venv venv" if venv_already_exists
# is False (create a new one), else return "source venv/bin/activate"
# (just activate the existing one).


# TODO 1.B (Scenario -- Interview Prep): write
# explain_why_venv_per_project() describing, in your own words, why
# professional Python projects use a separate virtual environment per
# project instead of one shared global environment (mention version
# conflicts between projects and reproducibility for teammates).


# ============================================================
# Topic 2: Project Structure
# ============================================================

# TODO 2.1: Write has_required_layout(file_paths). Given a list of
# relative file path strings for a project, return True only if the
# list contains at least one file starting with "tests/" AND at least
# one of "README.md" or "pyproject.toml" is present -- a minimal check
# that the project separates tests from source and has some form of
# project metadata. Otherwise return False.


# TODO 2.2: Write needs_init_file(directory_contains_python_files,
# uses_namespace_package). A regular (non-namespace) Python package
# needs an __init__.py file in each directory that should be importable
# as a package. Return True only if directory_contains_python_files is
# True and uses_namespace_package is False (namespace packages,
# introduced in Python 3.3, deliberately omit __init__.py).


# TODO 2.3 (Debug the Code): explain_tests_location() below wrongly
# claims test files should live mixed directly alongside source files
# with no separation. Fix its return value -- professional layouts keep
# a dedicated tests/ directory (or src/ + tests/ split) so test code
# never ships inside the installed package and is easy to find.
def explain_tests_location():
    return "Test files should always be saved in the exact same folder as the source code they test, mixed in together, with no separate tests directory."


print(explain_tests_location())


# TODO 2.A (Scenario -- Comparing Two Approaches): write
# choose_layout(package_will_be_published_to_pypi). A team is starting a
# new project. Return "src-layout" if package_will_be_published_to_pypi
# is True (src-layout avoids accidentally importing the uninstalled
# local copy during testing, a common publishing bug), else
# "flat-layout" (simpler, fine for an internal script/app that's never
# pip-installed by others).


# TODO 2.B (Scenario -- Interview Prep): write
# explain_why_structure_matters() describing why a consistent project
# structure (README, tests/, source package, pyproject.toml) matters
# once more than one person works on a codebase, beyond "it looks
# organized."


# ============================================================
# Topic 3: Logging
# ============================================================

# TODO 3.1: Write level_name_for_number(level_number). Python's logging
# module maps numeric severity levels to names: 10 -> "DEBUG", 20 ->
# "INFO", 30 -> "WARNING", 40 -> "ERROR", 50 -> "CRITICAL". Return the
# name for the given level_number using logging.getLevelName().


# TODO 3.2: Write would_message_be_emitted(logger_level, message_level).
# A logger only emits (handles) a message if the message's level is
# greater than or equal to the logger's configured threshold level --
# e.g. a logger set to logging.WARNING (30) will emit a WARNING (30) or
# ERROR (40) message but suppress an INFO (20) message. Return True if
# message_level >= logger_level, else False. Use the numeric levels
# directly (both arguments are ints, e.g. logging.INFO).


# TODO 3.3 (Debug the Code): build_log_format() below returns a format
# string with the fields in the wrong order and a typo in the attribute
# name for the logger's name. Fix it to return the standard format
# "%(asctime)s - %(name)s - %(levelname)s - %(message)s" (timestamp,
# then logger name, then level name, then the message).
def build_log_format():
    return "%(levelname)s - %(loggername)s - %(message)s - %(asctime)s"


print(build_log_format())


# TODO 3.4: Write default_root_level(). When no configuration is applied
# at all, Python's root logger defaults to a threshold of WARNING.
# Return logging.WARNING.


# TODO 3.5: Write count_emitted_messages(logger_level, message_levels).
# Given a logger's threshold level and a list of message levels (ints)
# that code attempted to log, return how many of those messages would
# actually be emitted (i.e. how many have message_level >= logger_level).


# TODO 3.A (Scenario -- Comparing Two Approaches): write
# choose_log_level_for_environment(is_production). A team is deciding
# what logging level to configure by default. Return logging.INFO if
# is_production is True (avoid flooding production logs with DEBUG
# noise, but still capture normal operational events), else
# logging.DEBUG (see everything while developing locally).


# TODO 3.B (Scenario -- Interview Prep): write
# explain_why_silent_failure_needs_logging() describing what should
# change about a script that "silently fails in production with no
# output" -- specifically, why using the logging module (with an
# appropriate level and a handler that writes somewhere durable, like a
# file) instead of bare print() statements would have caught the
# failure (mention that print() output is easy to lose, has no severity
# levels, and isn't easy to route to a file/log aggregator in
# production).


# ============================================================
# Topic 4: argparse
# ============================================================

# TODO 4.1: Write build_parser_arg_count(positional_names,
# optional_flag_names). Given a list of positional argument names and a
# list of optional flag names (e.g. ["--verbose", "--output"]), return
# the total number of arguments (len of both lists combined) that
# add_argument() would need to be called for when building an
# argparse.ArgumentParser for a command with this signature.


# TODO 4.2: Write parse_greeting_args(argv). Build an
# argparse.ArgumentParser with one required positional argument "name"
# and one optional flag "--shout" (action="store_true"). Parse argv
# (a list of strings, e.g. ["Ada", "--shout"]) with it and return a dict
# with keys "name" and "shout" holding the parsed values.


# TODO 4.3 (Debug the Code): describe_default_required() below wrongly
# claims every argparse argument is optional by default, matching
# neither positional nor --flag argparse conventions. Fix its return
# value -- a plain name (no leading dashes) passed to add_argument() is
# a REQUIRED positional argument by default, while a name starting with
# -- (or -) is optional by default (unless required=True is passed).
def describe_default_required():
    return "Every argument added with add_argument() is optional by default, whether or not its name starts with --."


print(describe_default_required())


# TODO 4.4: Write exit_code_for_missing_required_arg(). When a required
# positional argument is missing, argparse prints a usage error to
# stderr and calls sys.exit() with a nonzero status code -- specifically
# 2. Return 2.


# TODO 4.5: Write build_count_flag_value(argv). Build an
# argparse.ArgumentParser with one optional flag "--verbose" using
# action="count" and default=0 (so passing it multiple times increases
# a count, e.g. ["--verbose", "--verbose", "--verbose"] -> 3). Parse
# argv with it and return the resulting verbose count as an int.


# TODO 4.A (Scenario -- Comparing Two Approaches): write
# choose_argparse_action(flag_takes_a_value). A teammate is adding a new
# command-line flag. Return "store_true" if flag_takes_a_value is False
# (a simple on/off switch like --verbose needs no value), else "store"
# (the flag needs an accompanying value, like --output filename.txt).


# TODO 4.B (Scenario -- Interview Prep): write
# explain_argparse_vs_manual_sys_argv() describing why professional CLI
# tools use argparse instead of manually indexing into sys.argv (mention
# automatic --help generation, type conversion/validation, and clear
# error messages for missing/invalid arguments).


# ============================================================
# Topic 5: Packaging Basics (pyproject.toml)
# ============================================================

# TODO 5.1: Write has_minimum_pyproject_fields(toml_keys). Given a list
# of top-level key names found under a pyproject.toml's [project] table
# (e.g. ["name", "version", "dependencies"]), return True only if both
# "name" and "version" are present -- the two fields every installable
# package's [project] table must define at minimum.


# TODO 5.2: Write dependency_pin_style(version_spec). Given a dependency
# version specifier string, classify its pin style: return "exact" if
# it contains "==", "minimum" if it contains ">=" (and not "=="),
# "compatible" if it contains "~=", or "unpinned" if it's an empty
# string (no version constraint at all, just the bare package name).


# TODO 5.3 (Debug the Code): explain_pyproject_purpose() below wrongly
# claims pyproject.toml is just an optional style preference with no
# real effect on installing the package. Fix its return value --
# pyproject.toml is what tools like pip actually read to know the
# package's name, version, dependencies, and how to build it; without
# it (or the older setup.py), `pip install .` has nothing to install
# from.
def explain_pyproject_purpose():
    return "pyproject.toml is purely a style preference some developers like -- pip does not actually read it, and a package installs the exact same with or without one."


print(explain_pyproject_purpose())


# TODO 5.A (Scenario -- Comparing Two Approaches): write
# choose_dependency_pin(library_is_your_own_stable_api,
# library_changes_often). A team is writing dependency version
# specifiers for pyproject.toml. Return "exact" if library_changes_often
# is True (pin tightly to avoid a surprise breaking release), else
# "minimum" if library_is_your_own_stable_api is True (loose pin is
# fine, you control the API), else "compatible" (a reasonable safe
# default for most third-party libraries).


# TODO 5.B (Scenario -- Interview Prep): write
# explain_why_pin_dependencies() describing why professional projects
# pin dependency versions (in pyproject.toml or requirements.txt)
# instead of always installing "whatever the latest version is" (mention
# reproducible builds and avoiding a breaking change in a dependency
# silently breaking the project).


# ============================================================
# Topic 6: Putting It Together -- A Shippable CLI Tool
# ============================================================

# TODO 6.1: Write minimum_files_for_shippable_cli(file_names). Given a
# list of filenames present in a project directory, return True only if
# ALL of "pyproject.toml", "README.md", and at least one file ending in
# ".py" are present -- treat this as the minimum bar for a CLI tool
# someone else could actually install and run.


# TODO 6.2: Write cli_entry_point_line(package_name, module_name,
# function_name). Packaging a CLI tool with pyproject.toml's
# [project.scripts] table maps a command name to a "module:function"
# target. Return the string
# f"{package_name} = \"{module_name}:{function_name}\"" -- the exact
# line format used inside a [project.scripts] table (e.g.
# 'mycli = "mycli.cli:main"').


# TODO 6.3 (Debug the Code): explain_pip_install_editable() below
# wrongly claims `pip install -e .` copies the project's files into
# site-packages, same as a normal install, so edits to the source
# afterward have no effect. Fix its return value -- an editable install
# links to the project's source directory in place, so edits to the
# source take effect immediately without reinstalling, which is why
# it's used during development.
def explain_pip_install_editable():
    return "'pip install -e .' copies your project files into site-packages just like a normal install, so editing your source code afterward has no effect until you reinstall."


print(explain_pip_install_editable())


# TODO 6.A (Scenario -- Comparing Two Approaches): write
# choose_install_mode(actively_developing_the_package). A developer is
# about to install their own CLI package locally. Return "pip install
# -e ." if actively_developing_the_package is True (edits should take
# effect immediately, no reinstall needed), else "pip install ." (a
# normal, final install for actually using the finished tool).


# TODO 6.B (Scenario -- Interview Prep): write
# explain_shippable_checklist() describing, in your own words, what
# turns a personal script into something you could hand a teammate to
# install and run (mention: a virtual environment for isolated
# dependencies, a pyproject.toml declaring the package and its
# dependencies, structured logging instead of stray print() debugging,
# and argparse for a real command-line interface instead of hardcoded
# values).
