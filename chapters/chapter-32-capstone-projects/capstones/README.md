# Chapter 32 Capstones — Index

Chapter 32 is different from every other chapter in this course: instead of
one guided project, it's five full capstone projects. Each one combines
skills from several earlier chapters into a single, real, portfolio-worthy
build. Pick one to start with, or work through all five — each has its own
roadmap doc with the full build plan, milestones, and stretch goals.

If you're not sure where to start, or you want help talking about whichever
one you build in an interview, see [`../interview-questions.html`](../interview-questions.html)
first — it's framed around explaining a real project, not syntax trivia.

---

## 1. Full-Stack Task API

A real, deployable REST API for managing tasks — with persistent storage,
an actual test suite, and a CI pipeline that runs on every push. This is
the "can you ship a backend service, not just a script" capstone: routes
that create, read, update, and delete tasks against a real database, a
`pytest` suite that exercises those routes instead of just eyeballing
manual requests, and a GitHub Actions workflow that runs the suite
automatically so a broken change gets caught before it's merged, not
after.

**Combines:** Chapter 21 (Databases), Chapter 22 (Flask/FastAPI),
Chapter 27 (Testing Your Code), Chapter 30 (CI/CD Pipelines)

**Roadmap:** [`capstone-1-task-api.md`](capstone-1-task-api.md)

## 2. Data Insights CLI

Turns a one-off, notebook-style data analysis into a real, installable
command-line tool other people can run without touching your source code.
Instead of a script you re-run and re-edit by hand each time you want a
different view of a dataset, this capstone packages the analysis — load,
clean, summarize, chart-ready output — behind proper `argparse` flags
and ships it as a real console command, the same way `taskbox` did in
Chapter 31.

**Combines:** Chapter 23 (NumPy), Chapter 24 (Pandas),
Chapter 31 (Packaging/argparse)

**Roadmap:** [`capstone-2-data-cli.md`](capstone-2-data-cli.md)

## 3. Ops Toolkit

A single multi-subcommand CLI that bundles three genuinely useful,
independent ops-flavored tools into one installable package: a log
analyzer that parses and summarizes log files, a resume/keyword scanner
that checks a document against a target list of terms, and an API data
fetcher that pulls and processes JSON from a live endpoint. The three
tools don't share business logic — the point of this capstone is
learning to bundle unrelated-but-useful utilities behind one clean,
discoverable command-line interface.

**Combines:** Chapter 13 (File/CSV Handling), Chapter 18 (Regex),
Chapter 19 (APIs/JSON)

**Roadmap:** [`capstone-3-ops-toolkit.md`](capstone-3-ops-toolkit.md)

## 4. Personal Finance Tracker

A new-domain capstone: a real, OOP-modeled personal finance tracker with
accounts, transactions, and categories built as proper classes (not bare
dictionaries), persistent storage so your data survives between runs, a
test suite covering the logic that actually matters (balance math,
validation), and packaging so it installs and runs as a real command,
same as the other capstones. This is the one that most directly tests
whether Chapters 14-16's object-oriented design lessons actually stuck,
applied to a domain the course hasn't built a project around before.

**Combines:** Chapters 14-16 (OOP/Inheritance), Chapter 21 (Databases),
Chapter 27 (Testing), Chapter 31 (Packaging)

**Roadmap:** [`capstone-4-finance-tracker.md`](capstone-4-finance-tracker.md)

## 5. Open-Source Contribution Simulation

Not a new codebase — a structured exercise in the real fork → branch →
pull request → review workflow, applied to meaningfully extending one of
your own earlier capstones or chapter projects. Instead of practicing Git
and GitHub mechanics on a toy repo, you pick a real project you already
built, scope a genuine new feature or fix for it, and carry that change
through the same process a real open-source contribution goes through:
a focused branch, a clear PR description, and a self-review of your own
diff before calling it done. This is the capstone that tests
collaboration workflow, not new code.

**Combines:** Chapter 28 (Git Fundamentals),
Chapter 29 (GitHub/Collaboration)

**Roadmap:** [`capstone-5-oss-simulation.md`](capstone-5-oss-simulation.md)

---

## Choosing a capstone

You don't have to build all five to get value from this chapter, but each
one exercises a different combination of earlier chapters — building more
than one is what makes your portfolio show breadth instead of one deep
skill repeated five times. See [`../interview-questions.html`](../interview-questions.html)
for guidance on how to talk about whichever one(s) you build, including
how to pick which capstone to lead with in an actual interview.
