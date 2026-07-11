"""
Chapter 29 Project: Open-Source-Style Collaboration Workflow
See README.md in this folder for full instructions.
Run this from inside the project/ folder: python3 starter.py

Standard library only -- no installs needed. Requires a real `git`
executable on your PATH (this project runs real git commands via
subprocess -- nothing here is simulated or faked).

WHAT THIS SCRIPT DOES
----------------------
Real GitHub involves a server (github.com) this course can't reach from
a static, no-backend site. So this project builds a LOCAL stand-in for
"GitHub" using `git init --bare` -- a real Git repository that has no
working directory, exactly the kind of repo GitHub hosts on its own
servers. Every git command you run against it (clone, push, fetch) is
a genuine network-shaped operation, just pointed at a folder on your
own disk instead of github.com.

setup_scenario() (already written for you, TODO 1 is just wiring it up)
builds:
  - upstream.git   -- stands in for the "real" GitHub repo you don't own
  - my-fork.git    -- stands in for YOUR fork of it on GitHub

Your job is TODOs 2-7: drive the actual collaboration workflow through
that scenario with real git commands (via run_git()), the same commands
you'd run against a real GitHub fork.
"""

import subprocess
import shutil
import os

SCENARIO_DIR = "scenario"
WORKDIR = os.path.join(SCENARIO_DIR, "workdir")


def run_git(args, cwd=None, check=True):
    """Run a real git command and return the CompletedProcess.
    Prints the command so you can see exactly what's executing."""
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
    time. This part is provided -- your work starts after this returns."""
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


# TODO 1: Call setup_scenario() and store the returned dict in `paths`.
# This gives you paths["upstream"] and paths["fork"] to use below.


# TODO 2: Clone YOUR FORK (not upstream!) into WORKDIR -- this is the
# real-world first step: you never clone the original repo you don't
# own, you clone your own fork of it.
#   git clone <paths["fork"]> <WORKDIR>
# Then set a name/email in WORKDIR (git config user.email / user.name)
# so commits you make there have an author.


# TODO 3: Add upstream as a second remote inside WORKDIR, pointing at
# paths["upstream"]:
#   git remote add upstream <paths["upstream"]>
# Run `git remote -v` afterward and print it -- you should see two
# remotes: origin (your fork) and upstream (the original repo).


# TODO 4: Create a feature branch called "add-pancake-servings" and
# check it out (git checkout -b <name>). Then, inside WORKDIR, append
# this function to recipes.py:
#
#   def servings_for(recipe_name, people):
#       """Return a naive per-person ingredient scaling note."""
#       if recipe_name not in RECIPES:
#           return f"Unknown recipe: {recipe_name}"
#       return f"{recipe_name} for {people} people uses: " + ", ".join(RECIPES[recipe_name])
#
# Stage and commit it with a real, descriptive commit message.


# TODO 5: Push your feature branch to YOUR FORK (origin), not upstream:
#   git push -u origin add-pancake-servings
# This is the real point where, on actual GitHub, you'd go to
# github.com and click "Compare & pull request." That UI step can't be
# scripted -- see README.md/index.html for how to write that part up.


# TODO 6: Simulate what happens after a maintainer reviews and clicks
# "Merge pull request" on GitHub. Do this with a SEPARATE maintainer
# clone of upstream (not your WORKDIR) so it mirrors what actually
# happens server-side:
#   1. git clone <paths["upstream"]> into a "maintainer_clone" folder
#      inside SCENARIO_DIR, and set a user.name/user.email there too
#      (e.g. "Repo Owner" / "owner@example.com").
#   2. From maintainer_clone, fetch your feature branch directly from
#      your fork and merge it:
#        git fetch <paths["fork"]> add-pancake-servings:pr-1-add-pancake-servings
#        git merge --no-ff pr-1-add-pancake-servings -m "Merge pull request #1 from learner/add-pancake-servings"
#   3. Push the merge back to upstream: git push origin main
# Print the resulting `git log --oneline --graph --all` from upstream
# so you can see the real merge commit.


# TODO 7: Sync your fork now that upstream has moved ahead of it --
# this is the real "keep your fork in sync" workflow:
#   1. Back in WORKDIR, checkout main: git checkout main
#   2. git fetch upstream
#   3. git merge upstream/main   (brings the merged PR into your local main)
#   4. git push origin main      (pushes the sync up to your fork)
# Then clean up the now-merged feature branch:
#   5. git branch -d add-pancake-servings
#   6. git push origin --delete add-pancake-servings
# Print the final `git log --oneline --graph --all` from WORKDIR and
# from your fork to confirm both now show the merge commit and the
# feature branch is gone.


def run():
    print("=== Chapter 29 Project: GitHub Collaboration Workflow ===\n")
    # Your TODO 1-7 code runs here, in order, when you call this
    # function -- see the TODOs above for what each step does.
    pass


if __name__ == "__main__":
    run()
