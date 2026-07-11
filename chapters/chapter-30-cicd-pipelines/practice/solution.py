"""
Chapter 30 Practice Bank: CI/CD Pipelines -- REFERENCE SOLUTION
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py

Standard library only -- no installs needed.
"""

# ============================================================
# Topic 1: Why CI/CD Matters
# ============================================================

# TODO 1.1
def count_broken_by_manual_deploys(deploy_log):
    return sum(
        1 for entry in deploy_log
        if "manual" in entry.lower() and "broke" in entry.lower()
    )


# TODO 1.2
def catches_bug_before_merge(runs_tests_on_every_push):
    return True if runs_tests_on_every_push else False


# TODO 1.3 (Debug the Code)
def explain_what_ci_does():
    return (
        "CI automatically builds and tests every change (e.g. on every push "
        "or pull request), catching problems before they reach main, instead "
        "of only running tests when a developer remembers to -- this helps "
        "teams of any size, including a solo developer."
    )


print(explain_what_ci_does())


# TODO 1.A
def choose_deploy_strategy(team_size, deploys_per_week):
    return "CI/CD" if team_size > 1 or deploys_per_week > 1 else "manual is survivable, but CI/CD still recommended"


# TODO 1.B
def explain_why_cicd_matters():
    return (
        "CI/CD matters because it automates building, testing, and deploying "
        "code on every change, catching bugs immediately instead of after "
        "they reach production, and removing slow, error-prone manual deploy "
        "steps so a team can ship changes frequently and with confidence."
    )


# ============================================================
# Topic 2: GitHub Actions Basics (workflow files, triggers, jobs,
# steps, runners)
# ============================================================

# TODO 2.1
def parse_top_level_keys(yaml_lines):
    keys = []
    for line in yaml_lines:
        if line and not line.startswith((" ", "\t", "#")) and ":" in line:
            key = line.split(":", 1)[0].strip()
            keys.append(key)
    return keys


# TODO 2.2
def triggers_on_pull_request(yaml_lines):
    in_on_block = False
    for line in yaml_lines:
        if line.startswith("on:"):
            rest = line.split(":", 1)[1].strip()
            if rest == "pull_request":
                return True
            in_on_block = True
            continue
        if in_on_block:
            stripped = line.strip()
            if line.startswith((" ", "\t")):
                if stripped in ("pull_request:", "pull_request"):
                    return True
                continue
            else:
                in_on_block = False
    return False


# TODO 2.3 (Debug the Code)
def explain_workflow_file_location():
    return (
        "GitHub Actions workflow files must live in .github/workflows/, not "
        "any other folder, or GitHub won't discover and run them."
    )


print(explain_workflow_file_location())


# TODO 2.A
def choose_trigger_for_scenario(scenario):
    mapping = {
        "run tests on every push to any branch": "push",
        "run tests before merging a pull request": "pull_request",
        "run a nightly cleanup job": "schedule",
        "let a developer manually kick off a deploy": "workflow_dispatch",
    }
    return mapping.get(scenario, "unknown scenario")


# TODO 2.B
def explain_runner_vs_local():
    return (
        "A GitHub Actions runner is a fresh, ephemeral virtual machine GitHub "
        "spins up for each workflow run -- it starts with none of your local "
        "environment (no cached installs, no local env vars, no uncommitted "
        "files), so a workflow must explicitly check out the repo and install "
        "every dependency it needs, rather than relying on state that only "
        "exists on your machine."
    )


# ============================================================
# Topic 3: Building a Lint + Test Workflow
# ============================================================

# TODO 3.1
def steps_in_order(step_names):
    return list(step_names)


# TODO 3.2
def workflow_fails_fast(lint_passed, test_passed):
    return lint_passed and test_passed


# TODO 3.3 (Debug the Code)
def explain_checkout_step_bug():
    return (
        "Every job needs an actions/checkout step before running any "
        "commands against the repo's files -- without it, the runner's "
        "workspace is empty and later steps (like running pytest) fail "
        "because there's no code to test."
    )


print(explain_checkout_step_bug())


# TODO 3.A
def choose_lint_or_test_first(lint_is_fast, tests_are_slow):
    return "lint first" if lint_is_fast and tests_are_slow else "either order is reasonable"


# TODO 3.B
def explain_why_lint_before_test():
    return (
        "Running lint before the test suite gives a fast, cheap signal first "
        "-- lint checks are quick and catch obvious style/syntax issues, so a "
        "team saves the CI minutes and wait time of running a slower test "
        "suite against code that's already known to have basic problems."
    )


# ============================================================
# Topic 4: Matrix Strategy and Caching
# ============================================================

# TODO 4.1
def matrix_job_count(dimensions):
    total = 1
    for values in dimensions.values():
        total *= len(values)
    return total


# TODO 4.2
def cache_key_matches(current_key, cached_key):
    return current_key == cached_key


# TODO 4.3 (Debug the Code)
def explain_matrix_bug():
    return (
        "A matrix strategy runs the job once for EVERY combination of the "
        "listed values across all dimensions (a full cross product), not "
        "just once per dimension -- e.g. 3 Python versions x 2 operating "
        "systems means 6 separate job runs, not 5."
    )


print(explain_matrix_bug())


# TODO 4.A
def prevents_version_mismatch(uses_matrix_strategy):
    return True if uses_matrix_strategy else False


# TODO 4.B
def explain_matrix_prevents_version_bugs():
    return (
        "Your CI passing locally but failing in the pipeline on a different "
        "Python version happens because your machine only tested one "
        "version. A matrix strategy runs the same job across every listed "
        "Python version (and OS) in parallel, so a version-specific bug is "
        "caught in CI before merge instead of surfacing later for a user on "
        "a different version."
    )


# ============================================================
# Topic 5: Status Checks and Branch Protection
# ============================================================

# TODO 5.1
def can_merge_pr(required_checks, passed_checks):
    return all(check in passed_checks for check in required_checks)


# TODO 5.2
def blocks_direct_push_to_main(branch_protection_enabled, requires_pr):
    return branch_protection_enabled and requires_pr


# TODO 5.3 (Debug the Code)
def explain_required_check_bug():
    return (
        "A required status check that is still running (pending) or has "
        "failed BLOCKS merging -- only a required check that has actually "
        "completed and passed allows the merge button to become available, "
        "it isn't enough for the check to simply exist or have started."
    )


print(explain_required_check_bug())


# TODO 5.A
def handle_urgent_broken_check(check_is_flaky_confirmed, has_admin_override):
    if check_is_flaky_confirmed:
        return "re-run the check"
    return "fix the failure, do not bypass the check"


# TODO 5.B
def explain_skip_check_temptation():
    return (
        "Bypassing a required status check to merge urgently is the wrong "
        "move even under deadline pressure -- the check exists to catch real "
        "problems (like a broken test or failed build), and skipping it just "
        "moves the failure from CI, where it's cheap to catch, into main or "
        "production, where it's expensive to catch. The right move is to fix "
        "the actual failure, or if the check itself is flaky/broken, get it "
        "re-run or fixed -- not to grant yourself an exception."
    )


# ============================================================
# Topic 6: Beyond Tests (linting, type checking, security scanning,
# deployment stages)
# ============================================================

# TODO 6.1
def pipeline_stage_order(stage_names):
    order = ["lint", "type_check", "test", "security_scan", "build", "deploy_staging", "deploy_production"]
    return [s for s in order if s in stage_names]


# TODO 6.2
def deploy_requires_staging_first(deploys_to_production, passed_staging):
    return not deploys_to_production or passed_staging


# TODO 6.3 (Debug the Code)
def explain_deploy_stage_bug():
    return (
        "Deploying straight to production without a staging step first skips "
        "the chance to catch environment-specific problems (config, "
        "migrations, integration issues) in a safe environment -- "
        "deploy_staging should run and pass before deploy_production runs, "
        "not the reverse or neither."
    )


print(explain_deploy_stage_bug())


# TODO 6.A
def choose_next_pipeline_addition(has_tests, has_lint, has_type_check, has_security_scan):
    if not has_lint:
        return "add linting"
    if not has_type_check:
        return "add type checking"
    if not has_security_scan:
        return "add security scanning"
    return "add staged deployments"


# TODO 6.B
def explain_defense_in_depth_pipeline():
    return (
        "A CI/CD pipeline is more than just running tests -- linting catches "
        "style and obvious bugs, type checking catches whole classes of "
        "errors before runtime, security scanning catches known-vulnerable "
        "dependencies or leaked secrets, and staged deployment (staging "
        "before production) catches environment-specific problems -- each "
        "stage catches a different category of problem the others miss, so "
        "a pipeline with only tests still lets real issues through."
    )


if __name__ == "__main__":
    # Topic 1
    assert count_broken_by_manual_deploys(["deploy A ok", "manual deploy broke prod", "manual deploy fine", "manual deploy broke staging"]) == 2
    assert catches_bug_before_merge(True) is True
    assert catches_bug_before_merge(False) is False
    assert choose_deploy_strategy(1, 1) == "manual is survivable, but CI/CD still recommended"
    assert choose_deploy_strategy(5, 1) == "CI/CD"

    # Topic 2
    assert parse_top_level_keys(["name: CI", "on: pull_request", "jobs:", "  build:"]) == ["name", "on", "jobs"]
    assert triggers_on_pull_request(["name: CI", "on: pull_request", "jobs:"]) is True
    assert triggers_on_pull_request(["name: CI", "on: push", "jobs:"]) is False
    assert choose_trigger_for_scenario("run a nightly cleanup job") == "schedule"

    # Topic 3
    assert steps_in_order(["a", "b"]) == ["a", "b"]
    assert workflow_fails_fast(True, True) is True

    # Topic 4
    assert matrix_job_count({"python-version": ["3.9", "3.10", "3.11"], "os": ["ubuntu-latest", "windows-latest"]}) == 6
    assert cache_key_matches("k1", "k1") is True

    # Topic 5
    assert can_merge_pr(["lint", "test"], ["lint", "test"]) is True
    assert blocks_direct_push_to_main(True, True) is True

    # Topic 6
    assert pipeline_stage_order(["test", "lint", "deploy_production", "deploy_staging"]) == ["lint", "test", "deploy_staging", "deploy_production"]
    assert deploy_requires_staging_first(True, True) is True

    print("\nAll solution.py self-checks passed.")
