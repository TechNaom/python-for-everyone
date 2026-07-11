# Chapter 30 Practice Bank: CI/CD Pipelines

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews.

This chapter teaches GitHub Actions (YAML-based CI/CD), not Python
syntax — and this site's browser grader can't actually execute a real
GitHub Actions workflow. So every problem here is a Python function
that **parses, validates, or reasons about** a CI/CD concept using
plain data (lists of strings standing in for YAML lines, dicts,
booleans) instead of literally running a workflow. Every behavior
described in these problems was checked against real GitHub Actions
semantics before being written down here. Standard library only, no
installs needed — YAML lines are parsed with basic string operations,
not the `yaml` package, since pyyaml isn't available in this site's
browser Python sandbox.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Why CI/CD Matters

1. Count how many outages a manual deploy process caused.
2. Decide whether running tests on every push catches bugs before merge.
3. **Debug the Code:** fix a wrong claim that CI only benefits large teams.
4. **Scenario — Comparing Two Approaches:** write `choose_deploy_strategy()`.
5. **Scenario — Interview Prep:** explain why CI/CD matters.

## Topic 2: GitHub Actions Basics (workflow files, triggers, jobs, steps, runners)

1. Parse the top-level keys out of a workflow YAML file.
2. Determine whether a workflow triggers on `pull_request`.
3. **Debug the Code:** fix a wrong claim about where workflow files must live.
4. **Scenario — Comparing Two Approaches:** write `choose_trigger_for_scenario()`.
5. **Scenario — Interview Prep:** explain why a runner isn't the same as your local machine.

## Topic 3: Building a Lint + Test Workflow

1. Confirm steps run top to bottom, in the order written.
2. Decide whether a workflow is green (both lint and test passed).
3. **Debug the Code:** fix a wrong claim that the checkout step is optional.
4. **Scenario — Comparing Two Approaches:** write `choose_lint_or_test_first()`.
5. **Scenario — Interview Prep:** explain why teams run lint before tests.

## Topic 4: Matrix Strategy and Caching

1. Compute how many total job runs a matrix strategy produces.
2. Decide whether a dependency cache key matches, so the cache is reused.
3. **Debug the Code:** fix a wrong claim about how matrix job counts are computed.
4. **Scenario — Comparing Two Approaches:** write `prevents_version_mismatch()`.
5. **Scenario — Interview Prep:** explain how a matrix strategy prevents a "works on my machine" Python version bug.

## Topic 5: Status Checks and Branch Protection

1. Decide whether a PR can merge given required vs. passed checks.
2. Decide whether branch protection blocks direct pushes to main.
3. **Debug the Code:** fix a wrong claim that a pending check unblocks merging.
4. **Scenario — Comparing Two Approaches:** write `handle_urgent_broken_check()`.
5. **Scenario — Interview Prep:** explain why bypassing a required check to merge urgently is the wrong move.

## Topic 6: Beyond Tests (linting, type checking, security scanning, deployment stages)

1. Sort a pipeline's stages into their canonical execution order.
2. Decide whether it's safe to deploy to production (staging passed first).
3. **Debug the Code:** fix a wrong claim that staging deployments are unnecessary if tests pass.
4. **Scenario — Comparing Two Approaches:** write `choose_next_pipeline_addition()`.
5. **Scenario — Interview Prep:** explain why a pipeline with only tests still lets real issues through.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks. Every
data-driven task's output is exactly reproducible.
