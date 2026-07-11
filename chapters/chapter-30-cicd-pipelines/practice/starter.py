"""
Chapter 30 Practice Bank: CI/CD Pipelines
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Standard library only -- no installs needed. This chapter teaches GitHub
Actions (YAML-based CI/CD), not Python syntax -- and this site's browser
grader (Pyodide) can't actually run a GitHub Actions workflow. So every
problem here is a Python function that PARSES, VALIDATES, or REASONS
ABOUT a CI/CD concept using plain data (lists of strings standing in for
YAML lines, dicts, booleans) instead of literally executing a workflow.
Every behavior described was checked against real GitHub Actions
semantics before being written into this file. This intentionally uses
basic string/structural parsing instead of the `yaml` package, since
pyyaml isn't available in this site's browser Python sandbox.
"""

# ============================================================
# Topic 1: Why CI/CD Matters
# ============================================================

# TODO 1.1: Write count_broken_by_manual_deploys(deploy_log). Given a
# list of strings describing past deploys, like ["deploy A ok", "manual
# deploy broke prod", "manual deploy fine"], return how many entries
# contain BOTH "manual" and "broke" (case-insensitive) -- a stand-in for
# "how many outages did this team's manual deploy process cause."


# TODO 1.2: Write catches_bug_before_merge(runs_tests_on_every_push).
# Return True if runs_tests_on_every_push is True (CI catches problems
# before they reach main), else False.


# TODO 1.3 (Debug the Code): explain_what_ci_does() below wrongly
# claims CI only matters for large teams and does nothing useful for a
# solo developer. Fix its return value to describe what CI actually
# does: automatically build/test every change, catching problems before
# they reach main, regardless of team size.
def explain_what_ci_does():
    return "CI is a nice-to-have that only large teams need -- a solo developer gets no real benefit from it."


print(explain_what_ci_does())


# TODO 1.A (Scenario -- Comparing Two Approaches): write
# choose_deploy_strategy(team_size, deploys_per_week). Return "CI/CD" if
# team_size > 1 or deploys_per_week > 1, else "manual is survivable, but
# CI/CD still recommended".


# TODO 1.B (Scenario -- Interview Prep): write
# explain_why_cicd_matters() describing, in your own words, what problem
# CI/CD solves (not just "it runs tests" -- mention catching bugs early
# and removing manual, error-prone deploy steps).


# ============================================================
# Topic 2: GitHub Actions Basics (workflow files, triggers, jobs,
# steps, runners)
# ============================================================

# TODO 2.1: Write parse_top_level_keys(yaml_lines). Given a list of
# strings representing lines of a workflow YAML file, return the list of
# top-level keys in order -- lines that do NOT start with whitespace or
# "#" and contain ":" (e.g. "name:", "on:", "jobs:"). Strip the trailing
# ":" and any value after it, keeping just the key name.


# TODO 2.2: Write triggers_on_pull_request(yaml_lines). Given workflow
# YAML lines, return True if the "on:" trigger includes pull_request --
# either as a single-line value ("on: pull_request") or as one of several
# indented trigger keys under a multi-line "on:" block. Return False
# otherwise.


# TODO 2.3 (Debug the Code): explain_workflow_file_location() below
# gives the wrong folder path. Fix it: GitHub only discovers and runs
# workflow files placed in .github/workflows/.
def explain_workflow_file_location():
    return "GitHub Actions workflow files can live in any folder in the repo, GitHub scans the whole project for them."


print(explain_workflow_file_location())


# TODO 2.A (Scenario -- Comparing Two Approaches): write
# choose_trigger_for_scenario(scenario). Support exactly these mappings:
# "run tests on every push to any branch" -> "push";
# "run tests before merging a pull request" -> "pull_request";
# "run a nightly cleanup job" -> "schedule";
# "let a developer manually kick off a deploy" -> "workflow_dispatch".
# Return "unknown scenario" for anything else.


# TODO 2.B (Scenario -- Interview Prep): write explain_runner_vs_local()
# describing why a GitHub Actions runner is NOT the same as a
# developer's local machine (fresh/ephemeral VM, no cached installs, no
# local env vars or uncommitted files -- so a workflow must explicitly
# check out the repo and install every dependency).


# ============================================================
# Topic 3: Building a Lint + Test Workflow
# ============================================================

# TODO 3.1: Write steps_in_order(step_names). Given a list of step
# names, return them unchanged, in the same order -- this models that a
# job's steps always run top to bottom, in the order they're written.


# TODO 3.2: Write workflow_fails_fast(lint_passed, test_passed). A
# lint+test workflow should only be considered green if BOTH steps
# passed. Return True only if both lint_passed and test_passed are True.


# TODO 3.3 (Debug the Code): explain_checkout_step_bug() below wrongly
# claims the checkout step is optional. Fix its return value: every job
# needs an actions/checkout step before running commands against repo
# files, or the runner's workspace is empty.
def explain_checkout_step_bug():
    return "The actions/checkout step is optional -- a job can run pytest against repo files even without it, since GitHub automatically provides the code."


print(explain_checkout_step_bug())


# TODO 3.A (Scenario -- Comparing Two Approaches): write
# choose_lint_or_test_first(lint_is_fast, tests_are_slow). Return "lint
# first" if both lint_is_fast and tests_are_slow are True, else "either
# order is reasonable".


# TODO 3.B (Scenario -- Interview Prep): write
# explain_why_lint_before_test() describing why teams often run lint
# before the test suite (fast, cheap signal first -- saves CI time by
# not running a slow suite against code with obvious style/syntax
# problems).


# ============================================================
# Topic 4: Matrix Strategy and Caching
# ============================================================

# TODO 4.1: Write matrix_job_count(dimensions). Given a dict like
# {"python-version": ["3.9", "3.10", "3.11"], "os": ["ubuntu-latest",
# "windows-latest"]}, return the total number of job runs a matrix
# strategy produces -- the product of the lengths of every dimension's
# value list (every combination runs once).


# TODO 4.2: Write cache_key_matches(current_key, cached_key). A
# dependency cache is only reused when its key exactly matches the
# current run's computed key (commonly built from the OS, Python
# version, and a hash of the lockfile). Return True if current_key ==
# cached_key, else False.


# TODO 4.3 (Debug the Code): explain_matrix_bug() below wrongly claims a
# matrix strategy runs the job once per dimension, added together. Fix
# it: a matrix runs the job once for EVERY COMBINATION across all
# dimensions (a full cross product) -- e.g. 3 Python versions x 2
# operating systems means 6 separate runs, not 5.
def explain_matrix_bug():
    return "A matrix strategy with 3 Python versions and 2 operating systems runs the job 5 times total -- add the two dimensions together."


print(explain_matrix_bug())


# TODO 4.A (Scenario -- Comparing Two Approaches): write
# prevents_version_mismatch(uses_matrix_strategy). Return True if
# uses_matrix_strategy is True, else False -- a stand-in for "does this
# setup catch a bug that only shows up on a Python version different
# from what the developer tested locally."


# TODO 4.B (Scenario -- Interview Prep): write
# explain_matrix_prevents_version_bugs() describing this real scenario:
# "your CI passes locally but fails in the pipeline because of a Python
# version mismatch" -- explain how a matrix strategy prevents this by
# testing every listed version in CI instead of just the one version a
# developer happens to have locally.


# ============================================================
# Topic 5: Status Checks and Branch Protection
# ============================================================

# TODO 5.1: Write can_merge_pr(required_checks, passed_checks). Given a
# list of required check names and a list of checks that have actually
# passed, return True only if every required check is present in
# passed_checks.


# TODO 5.2: Write blocks_direct_push_to_main(branch_protection_enabled,
# requires_pr). Return True (direct pushes to main are blocked) only if
# both branch_protection_enabled and requires_pr are True.


# TODO 5.3 (Debug the Code): explain_required_check_bug() below wrongly
# claims a required check merely needs to exist/start running to unblock
# a merge. Fix it: a required check must actually COMPLETE and PASS --
# a pending or failed check still blocks merging.
def explain_required_check_bug():
    return "As soon as a required status check starts running, GitHub allows the merge button to be used, even before the check finishes."


print(explain_required_check_bug())


# TODO 5.A (Scenario -- Comparing Two Approaches): write
# handle_urgent_broken_check(check_is_flaky_confirmed, has_admin_override).
# A teammate wants to merge urgently but a required check is failing.
# Return "re-run the check" if check_is_flaky_confirmed is True, else
# "fix the failure, do not bypass the check" (regardless of
# has_admin_override -- having override power isn't a reason to use it).


# TODO 5.B (Scenario -- Interview Prep): write
# explain_skip_check_temptation() describing why bypassing a required
# status check to merge urgently is the wrong move -- it just moves a
# real failure from CI (cheap to catch) into main/production (expensive
# to catch), and the right move is to fix the failure or get a
# confirmed-flaky check re-run, not grant yourself an exception.


# ============================================================
# Topic 6: Beyond Tests (linting, type checking, security scanning,
# deployment stages)
# ============================================================

# TODO 6.1: Write pipeline_stage_order(stage_names). Given a list of
# stage names present in a pipeline (in any order), return them
# filtered and sorted into this canonical order: "lint", "type_check",
# "test", "security_scan", "build", "deploy_staging",
# "deploy_production" -- drop any stage name not in this canonical list.


# TODO 6.2: Write deploy_requires_staging_first(deploys_to_production,
# passed_staging). Return True if it's safe to proceed -- either the
# pipeline isn't deploying to production at all (deploys_to_production
# is False), or it is deploying to production AND staging already
# passed (passed_staging is True).


# TODO 6.3 (Debug the Code): explain_deploy_stage_bug() below wrongly
# claims deploying straight to production without a staging step is
# fine as long as tests passed. Fix it: staging catches
# environment-specific problems (config, migrations, integration) that
# unit/integration tests run locally or in CI can't -- deploy_staging
# should run and pass before deploy_production runs.
def explain_deploy_stage_bug():
    return "If the test suite passes, it's fine to deploy straight to production -- a separate staging deployment step adds nothing tests don't already cover."


print(explain_deploy_stage_bug())


# TODO 6.A (Scenario -- Comparing Two Approaches): write
# choose_next_pipeline_addition(has_tests, has_lint, has_type_check,
# has_security_scan). A team is incrementally building out their
# pipeline. Return, in this priority order, the first missing piece:
# "add linting" if not has_lint, else "add type checking" if not
# has_type_check, else "add security scanning" if not
# has_security_scan, else "add staged deployments".


# TODO 6.B (Scenario -- Interview Prep): write
# explain_defense_in_depth_pipeline() describing why a CI/CD pipeline
# with only tests still lets real issues through -- linting, type
# checking, security scanning, and staged deployment each catch a
# different category of problem the others miss.
