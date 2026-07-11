"""
Chapter 31 Practice Bank: Professional Python -- SOLUTION
See README.md for instructions. Run: python3 solution.py
"""

import argparse
import logging

# ============================================================
# Topic 1: Virtual Environments
# ============================================================


def is_running_in_venv(sys_prefix, sys_base_prefix):
    return sys_prefix != sys_base_prefix


def parse_pip_freeze(freeze_output):
    result = {}
    for line in freeze_output.splitlines():
        line = line.strip()
        if not line:
            continue
        name, version = line.split("==")
        result[name] = version
    return result


def explain_global_installs():
    return (
        "Installing packages globally means every project on the machine shares "
        "one set of versions -- two projects needing different versions of the "
        "same library will conflict, and a teammate's global environment may not "
        "match yours, breaking reproducibility. A per-project venv avoids both problems."
    )


print(explain_global_installs())


def recommended_venv_command(venv_already_exists):
    return "source venv/bin/activate" if venv_already_exists else "python3 -m venv venv"


def explain_why_venv_per_project():
    return (
        "Each project gets its own isolated set of installed package versions, so "
        "two projects needing different versions of the same library never conflict, "
        "and a requirements.txt/pyproject.toml plus a fresh venv lets any teammate "
        "reproduce the exact same environment on their own machine."
    )


# ============================================================
# Topic 2: Project Structure
# ============================================================


def has_required_layout(file_paths):
    has_tests = any(p.startswith("tests/") for p in file_paths)
    has_metadata = "README.md" in file_paths or "pyproject.toml" in file_paths
    return has_tests and has_metadata


def needs_init_file(directory_contains_python_files, uses_namespace_package):
    return directory_contains_python_files and not uses_namespace_package


def explain_tests_location():
    return (
        "Test files should live in a dedicated tests/ directory (or a src/ + tests/ "
        "split), separate from the source package, so test code never ships inside "
        "the installed package and is easy to find and run independently."
    )


print(explain_tests_location())


def choose_layout(package_will_be_published_to_pypi):
    return "src-layout" if package_will_be_published_to_pypi else "flat-layout"


def explain_why_structure_matters():
    return (
        "A consistent structure means anyone joining the project already knows where "
        "to find tests, source, and metadata without a tour -- it also prevents subtle "
        "bugs like accidentally testing against an uninstalled local copy, and it's what "
        "packaging tools expect when building/publishing the project."
    )


# ============================================================
# Topic 3: Logging
# ============================================================


def level_name_for_number(level_number):
    return logging.getLevelName(level_number)


def would_message_be_emitted(logger_level, message_level):
    return message_level >= logger_level


def build_log_format():
    return "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


print(build_log_format())


def default_root_level():
    return logging.WARNING


def count_emitted_messages(logger_level, message_levels):
    return sum(1 for lvl in message_levels if lvl >= logger_level)


def choose_log_level_for_environment(is_production):
    return logging.INFO if is_production else logging.DEBUG


def explain_why_silent_failure_needs_logging():
    return (
        "A script relying on print() has no severity levels, is easy to lose (stdout "
        "may not be captured or redirected anywhere durable in production), and can't "
        "easily be routed to a file or log aggregator. Using the logging module with an "
        "appropriate level (e.g. ERROR for a failure) and a handler that writes to a file "
        "means the failure leaves a durable, searchable record instead of vanishing."
    )


# ============================================================
# Topic 4: argparse
# ============================================================


def build_parser_arg_count(positional_names, optional_flag_names):
    return len(positional_names) + len(optional_flag_names)


def parse_greeting_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--shout", action="store_true")
    ns = parser.parse_args(argv)
    return {"name": ns.name, "shout": ns.shout}


def describe_default_required():
    return (
        "A plain name with no leading dashes (a positional argument) is REQUIRED by "
        "default. A name starting with -- (or -) is an optional argument by default, "
        "unless required=True is explicitly passed to add_argument()."
    )


print(describe_default_required())


def exit_code_for_missing_required_arg():
    return 2


def build_count_flag_value(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="count", default=0)
    ns = parser.parse_args(argv)
    return ns.verbose


def choose_argparse_action(flag_takes_a_value):
    return "store" if flag_takes_a_value else "store_true"


def explain_argparse_vs_manual_sys_argv():
    return (
        "argparse automatically generates a --help message, converts and validates "
        "argument types, and produces clear, consistent error messages for missing or "
        "invalid arguments -- manually indexing into sys.argv gives none of that for "
        "free and means reimplementing all of it by hand, badly, for every script."
    )


# ============================================================
# Topic 5: Packaging Basics (pyproject.toml)
# ============================================================


def has_minimum_pyproject_fields(toml_keys):
    return "name" in toml_keys and "version" in toml_keys


def dependency_pin_style(version_spec):
    if version_spec == "":
        return "unpinned"
    if "==" in version_spec:
        return "exact"
    if "~=" in version_spec:
        return "compatible"
    if ">=" in version_spec:
        return "minimum"
    return "unpinned"


def explain_pyproject_purpose():
    return (
        "pyproject.toml is what tools like pip actually read to know the package's "
        "name, version, dependencies, and how to build it -- without it (or the older "
        "setup.py), `pip install .` has nothing to install from. It is not just a style preference."
    )


print(explain_pyproject_purpose())


def choose_dependency_pin(library_is_your_own_stable_api, library_changes_often):
    if library_changes_often:
        return "exact"
    if library_is_your_own_stable_api:
        return "minimum"
    return "compatible"


def explain_why_pin_dependencies():
    return (
        "Pinning dependency versions means every install (yours, a teammate's, CI, "
        "production) resolves to the exact same code, so a build that worked yesterday "
        "still works today -- without pins, a dependency's new release could introduce a "
        "breaking change that silently breaks the project the next time someone installs it."
    )


# ============================================================
# Topic 6: Putting It Together -- A Shippable CLI Tool
# ============================================================


def minimum_files_for_shippable_cli(file_names):
    has_pyproject = "pyproject.toml" in file_names
    has_readme = "README.md" in file_names
    has_py_file = any(f.endswith(".py") for f in file_names)
    return has_pyproject and has_readme and has_py_file


def cli_entry_point_line(package_name, module_name, function_name):
    return f'{package_name} = "{module_name}:{function_name}"'


def explain_pip_install_editable():
    return (
        "'pip install -e .' links to the project's source directory in place instead of "
        "copying files into site-packages, so edits to the source take effect immediately "
        "without reinstalling -- that's exactly why it's used during development."
    )


print(explain_pip_install_editable())


def choose_install_mode(actively_developing_the_package):
    return "pip install -e ." if actively_developing_the_package else "pip install ."


def explain_shippable_checklist():
    return (
        "A shippable CLI tool has: a virtual environment so its dependencies are isolated "
        "from other projects; a pyproject.toml declaring the package's name, version, and "
        "dependencies so `pip install` knows what to do; structured logging (not stray "
        "print() calls) so failures leave a durable record; and argparse for a real "
        "command-line interface with --help, validated arguments, and clear errors instead "
        "of hardcoded values a user has to edit the source to change."
    )


if __name__ == "__main__":
    # Quick sanity checks for Topics 1-2 and 5-6 (reasoning-based).
    assert is_running_in_venv("/venv", "/usr") is True
    assert is_running_in_venv("/usr", "/usr") is False
    assert parse_pip_freeze("requests==2.34.2\nidna==3.18\n") == {"requests": "2.34.2", "idna": "3.18"}
    assert recommended_venv_command(False) == "python3 -m venv venv"
    assert recommended_venv_command(True) == "source venv/bin/activate"

    assert has_required_layout(["tests/test_x.py", "README.md"]) is True
    assert has_required_layout(["main.py"]) is False
    assert needs_init_file(True, False) is True
    assert needs_init_file(True, True) is False
    assert choose_layout(True) == "src-layout"
    assert choose_layout(False) == "flat-layout"

    assert has_minimum_pyproject_fields(["name", "version", "dependencies"]) is True
    assert has_minimum_pyproject_fields(["name"]) is False
    assert dependency_pin_style("==2.34.2") == "exact"
    assert dependency_pin_style(">=2.0") == "minimum"
    assert dependency_pin_style("~=2.0") == "compatible"
    assert dependency_pin_style("") == "unpinned"
    assert choose_dependency_pin(False, True) == "exact"
    assert choose_dependency_pin(True, False) == "minimum"
    assert choose_dependency_pin(False, False) == "compatible"

    assert minimum_files_for_shippable_cli(["pyproject.toml", "README.md", "cli.py"]) is True
    assert minimum_files_for_shippable_cli(["cli.py"]) is False
    assert cli_entry_point_line("mycli", "mycli.cli", "main") == 'mycli = "mycli.cli:main"'
    assert choose_install_mode(True) == "pip install -e ."
    assert choose_install_mode(False) == "pip install ."

    # Logging (Topic 3)
    assert level_name_for_number(10) == "DEBUG"
    assert level_name_for_number(20) == "INFO"
    assert level_name_for_number(30) == "WARNING"
    assert level_name_for_number(40) == "ERROR"
    assert level_name_for_number(50) == "CRITICAL"
    assert would_message_be_emitted(logging.WARNING, logging.INFO) is False
    assert would_message_be_emitted(logging.WARNING, logging.ERROR) is True
    assert default_root_level() == logging.WARNING
    assert count_emitted_messages(logging.WARNING, [10, 20, 30, 40, 50]) == 3

    # argparse (Topic 4)
    assert build_parser_arg_count(["name"], ["--verbose", "--output"]) == 3
    assert parse_greeting_args(["Ada", "--shout"]) == {"name": "Ada", "shout": True}
    assert parse_greeting_args(["Ada"]) == {"name": "Ada", "shout": False}
    assert exit_code_for_missing_required_arg() == 2
    assert build_count_flag_value(["--verbose", "--verbose", "--verbose"]) == 3
    assert build_count_flag_value([]) == 0
    assert choose_argparse_action(False) == "store_true"
    assert choose_argparse_action(True) == "store"

    print("\nAll sanity checks passed.")
