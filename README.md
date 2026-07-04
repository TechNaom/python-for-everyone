# Python for Everyone

Free, interactive Python course for everyone — from complete beginners to
working professionals. Mini HTML textbooks with instant-check
fill-in-the-blank quizzes, hands-on exercises, interview prep, and real
projects.

🔗 **Live course site:** https://technaom.github.io/python-for-everyone/

## What this is

A self-paced Python course built as a series of small, interactive HTML
"mini textbooks" — no sign-up, no cost, no assumed background. Every chapter
follows the same format:

1. A real-world hook before any syntax
2. The concept explained in plain language first
3. "What is...?" callout boxes for every new term, the moment it's introduced
4. Annotated code examples — what each line does, and why
5. An optional "Go Deeper" section for readers who want more rigor
6. Points to Remember
7. An interactive fill-in-the-blank quiz — each blank has its own **Check**
   button for instant ✅/❌ feedback, no backend, nothing leaves your browser
8. Exercises
9. Interview questions (strong answer / red flags / follow-up format)
10. A small real project that uses everything the chapter taught

## Status

This course is being built **one chapter at a time**, piloted and validated
before scaling. Currently live:

- ✅ Chapter 1: Your First Python Program (`print()`, variables, basic types, `input()`)

See [`docs/curriculum/CURRICULUM_MAP.md`](docs/curriculum/CURRICULUM_MAP.md)
for the full draft roadmap of chapters to come.

## Repo structure

```
python-for-everyone/
├── index.html                          → course landing page (GitHub Pages entry point)
├── docs/curriculum/CURRICULUM_MAP.md   → full draft course roadmap
├── assets/
│   ├── style.css                        → shared visual design, used by every chapter
│   └── quiz-engine.js                   → shared fill-in-the-blank quiz checking logic
├── chapters/
│   └── chapter-01-first-program/
│       ├── lesson.html                  → the interactive mini-textbook
│       ├── quiz.html                    → fill-in-the-blank quiz
│       ├── exercises/                   → starter.py, solution.py, README
│       ├── interview-questions.md
│       └── project/                     → a small real project (starter + solution)
└── .github/workflows/                   → GitHub Pages deploy workflow
```

## Running the Python exercises locally

```bash
git clone https://github.com/TechNaom/python-for-everyone.git
cd python-for-everyone
python3 --version   # confirm Python 3 is installed — no other dependencies needed
```

Each chapter's `exercises/` and `project/` folders are plain, dependency-free
Python scripts — just `python3 <file>.py`. The lesson pages and quizzes need
no installation at all; open them directly in a browser or read them via the
live Pages site above.

## Maintenance

This repo is solo-maintained (with AI assistance) and isn't open to external
contributions — issues and PRs from outside contributors aren't reviewed.
See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the maintainer's own workflow
notes.

## License

MIT — see [`LICENSE`](LICENSE). Free to use for your own learning, classroom,
or study group.
