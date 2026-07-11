"""
Chapter 29 Project: Open-Source-Style Collaboration Workflow -- reference solution.
Run this from inside the project/ folder: python3 solution.py

Requires a real `git` executable on your PATH. Every git command below
is real and actually executes -- nothing is faked or simulated as text.
The one thing that IS simulated is "GitHub itself": since this is a
static, no-backend site, there's no real github.com to push to, so
`git init --bare` stands in for it -- a real bare Git repository with
no working directory, structurally identical to what GitHub hosts on
its own servers. Every clone/push/fetch below is a genuine operation
against that stand-in, not a description of one.

WHAT'S REAL vs. WHAT'S DOCUMENTED-ONLY
---------------------------------------
Real, executed here: remotes, cloning a fork, branching, committing,
pushing, fetching, merging, and syncing a fork with upstream.
Documented-only (can't be scripted, see README.md/index.html): opening
a PR on github.com's UI, a reviewer leaving comments, clicking
"Approve," and clicking "Merge pull request." This script simulates
the RESULT of that review+merge (a real merge commit, built with real
git commands) without simulating the web UI itself.
"""

import subprocess
import shutil
import os

SCENARIO_DIR = "scenario"
WORKDIR = os.path.join(SCENARIO_DIR, "workdir")
MAINTAINER_CLONE = os.path.join(SCENARIO_DIR, "maintainer_clone")


def run_git(args, cwd=None, check=True):
    """Run a real git command and return the CompletedProcess."""
    print(f"$ git {' '.join(args)}" + (f"   (in {cwd})" if cwd else ""))
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        check=check,
        capture_output=True,
        text=True,
    )
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())
    return result


def setup_scenario(base_dir=SCENARIO_DIR):
    """Builds the local 'GitHub stand-in': a bare upstream repo with one
    seed commit, plus a bare fork repo cloned from it at that point in
    time."""
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)

    upstream_path = os.path.abspath(os.path.join(base_dir, "upstream.git"))
    seed_path = os.path.join(base_dir, "_seed_owner")
    fork_path = os.path.abspath(os.path.join(base_dir, "my-fork.git"))

    run_git(["init", "--bare", "-b", "main", upstream_path])

    run_git(["clone", upstream_path, seed_path])
    run_git(["config", "user.email", "owner@example.com"], cwd=seed_path)
    run_git(["config", "user.name", "Repo Owner"], cwd=seed_path)

    with open(os.path.join(seed_path, "README.md"), "w") as f:
        f.write("# Recipe Box\nA tiny shared collection of recipes.\n")
    with open(os.path.join(seed_path, "recipes.py"), "w") as f:
        f.write(
            'RECIPES = {\n'
            '    "pancakes": ["flour", "egg", "milk"],\n'
            '}\n\n'
            'def list_recipes():\n'
            '    return list(RECIPES.keys())\n'
        )

    run_git(["add", "README.md", "recipes.py"], cwd=seed_path)
    run_git(["commit", "-m", "Initial commit: recipe box skeleton"], cwd=seed_path)
    run_git(["push", "-u", "origin", "main"], cwd=seed_path)

    run_git(["clone", "--bare", upstream_path, fork_path])
    shutil.rmtree(seed_path)

    print(f"\nScenario ready.")
    print(f"  upstream (stands in for the real GitHub repo you don't own): {upstream_path}")
    print(f"  my-fork  (stands in for YOUR fork of it on GitHub):          {fork_path}\n")
    return {"base_dir": base_dir, "upstream": upstream_path, "fork": fork_path}


def run():
    print("=== Chapter 29 Project: GitHub Collaboration Workflow ===\n")

    # TODO 1
    paths = setup_scenario()

    # TODO 2: clone YOUR FORK (not upstream) into WORKDIR
    print("--- Step 1: clone your fork (not upstream) ---")
    run_git(["clone", paths["fork"], WORKDIR])
    run_git(["config", "user.email", "learner@example.com"], cwd=WORKDIR)
    run_git(["config", "user.name", "Learner"], cwd=WORKDIR)

    # TODO 3: add upstream as a second remote
    print("\n--- Step 2: add upstream as a second remote ---")
    run_git(["remote", "add", "upstream", paths["upstream"]], cwd=WORKDIR)
    run_git(["remote", "-v"], cwd=WORKDIR)

    # TODO 4: feature branch + commit
    print("\n--- Step 3: create a feature branch and commit real work ---")
    run_git(["checkout", "-b", "add-pancake-servings"], cwd=WORKDIR)
    recipes_path = os.path.join(WORKDIR, "recipes.py")
    with open(recipes_path, "a") as f:
        f.write(
            "\n\n"
            "def servings_for(recipe_name, people):\n"
            '    """Return a naive per-person ingredient scaling note."""\n'
            "    if recipe_name not in RECIPES:\n"
            '        return f"Unknown recipe: {recipe_name}"\n'
            '    return f"{recipe_name} for {people} people uses: " + ", ".join(RECIPES[recipe_name])\n'
        )
    run_git(["add", "recipes.py"], cwd=WORKDIR)
    run_git(
        ["commit", "-m", "Add servings_for() to scale a recipe by number of people"],
        cwd=WORKDIR,
    )

    # TODO 5: push feature branch to fork
    print("\n--- Step 4: push the feature branch to your fork (origin) ---")
    run_git(["push", "-u", "origin", "add-pancake-servings"], cwd=WORKDIR)
    print(
        "\n[On real GitHub: you'd now open github.com/your-username/recipe-box, "
        "see the 'Compare & pull request' banner for this branch, and open a PR "
        "against the upstream repo's main branch. See README.md / index.html for "
        "that step written up in full -- it can't be scripted from here.]"
    )

    # TODO 6: simulate the approved-and-merged PR via a maintainer clone
    print("\n--- Step 5: simulate the maintainer merging the approved PR ---")
    run_git(["clone", paths["upstream"], MAINTAINER_CLONE])
    run_git(["config", "user.email", "owner@example.com"], cwd=MAINTAINER_CLONE)
    run_git(["config", "user.name", "Repo Owner"], cwd=MAINTAINER_CLONE)
    run_git(
        ["fetch", paths["fork"], "add-pancake-servings:pr-1-add-pancake-servings"],
        cwd=MAINTAINER_CLONE,
    )
    run_git(
        [
            "merge", "--no-ff", "pr-1-add-pancake-servings",
            "-m", "Merge pull request #1 from learner/add-pancake-servings",
        ],
        cwd=MAINTAINER_CLONE,
    )
    run_git(["push", "origin", "main"], cwd=MAINTAINER_CLONE)
    print("\nUpstream history after the merge:")
    run_git(["log", "--oneline", "--graph", "--all"], cwd=MAINTAINER_CLONE)

    # TODO 7: sync the fork
    print("\n--- Step 6: sync your fork now that upstream has moved ahead ---")
    run_git(["checkout", "main"], cwd=WORKDIR)
    run_git(["fetch", "upstream"], cwd=WORKDIR)
    run_git(["merge", "upstream/main"], cwd=WORKDIR)
    run_git(["push", "origin", "main"], cwd=WORKDIR)

    print("\n--- Step 7: clean up the merged feature branch ---")
    run_git(["branch", "-d", "add-pancake-servings"], cwd=WORKDIR)
    run_git(["push", "origin", "--delete", "add-pancake-servings"], cwd=WORKDIR)

    print("\nFinal local (fork-tracking) history:")
    run_git(["log", "--oneline", "--graph", "--all"], cwd=WORKDIR)

    print(
        "\n=== Done. Your fork's main branch now matches upstream's main, "
        "including the merge commit, and the feature branch is gone from "
        "both your local clone and your fork. ==="
    )


if __name__ == "__main__":
    run()
