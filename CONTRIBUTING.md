# Maintenance Guide (Solo-Maintained Project)

This repo is maintained solely by its owner (with AI assistance) — it is
**not open to external contributions**. Issues and pull requests from outside
contributors are not reviewed or merged. If you found this course useful,
feel free to fork it for your own study group or classroom per the MIT
license, but please don't open issues or PRs here.

This doc is my own working reference for how content gets added, so nothing
drifts as the course grows chapter by chapter.

## Adding a new chapter

Each chapter lives at `chapters/chapter-{NN}-{slug}/` and needs, at minimum:

```text
chapters/chapter-{NN}-{slug}/
├── lesson.html               → follow the exact section order used in Chapter 1:
│                                page-meta (badge/difficulty/reading time) → page-toc →
│                                hook → plain-language concept → "What is...?" boxes →
│                                code-window annotated code → optional Go Deeper →
│                                Points to Remember
├── quiz.html                  → fill-in-the-blank quiz using assets/quiz-engine.js;
│                                 reuse the same markup pattern (.fib-row, data-answers,
│                                 quiz-progress-fill, quiz-celebration)
├── interview-questions.html   → .qa-item accordions (strong answer / red flags /
│                                 follow-up), plus a rapid-fire fill-in-the-blank
│                                 review using the same quiz-engine.js pattern
├── exercises/
│   ├── README.md               → plain-text version for repo browsing / local cloning
│   ├── index.html              → styled version linked from the live site (task-card
│   │                              per TODO, code-window for starter code, download-links
│   │                              pointing at the raw .py files)
│   ├── starter.py
│   └── solution.py
└── project/
    ├── README.md                → plain-text version for repo browsing
    ├── index.html                → styled version linked from the live site
    ├── starter.py
    └── solution.py
```

**Every chapter page needs both a `.md` and an `.html` version** where noted
above: the `.md` is what a `git clone` / repo browser sees; the `.html` is
what the live GitHub Pages site serves (our deploy workflow uploads the raw
repo as-is, with no Jekyll/markdown rendering, so an un-styled `.md` file
looks broken if linked directly from the site). Keep both in sync when
content changes.

Then:

1. Add the new chapter as a link in `index.html`'s chapter list (move it out
   of "coming soon") **and** as a new `.roadmap-list` entry in
   `docs/curriculum/index.html` (move it from "Planned" to "Built").
2. Update `docs/curriculum/CURRICULUM_MAP.md` (the plain-text draft) to match.
3. Verify every Python solution actually runs: `python3 solution.py` (pipe
   sample answers via `echo`/`printf` if it uses `input()`).
4. Open every `.html` page for the chapter directly in a browser (or via the
   local Pages preview) and click through every quiz Check button, every
   `chapter-nav` link, and every top-bar nav link before pushing — the whole
   chapter should form one connected loop: lesson → quiz → exercises →
   interview questions → project → back to all chapters.

## Content standards

- **Stick to what's been taught.** A chapter should only use Python features
  introduced in that chapter or earlier ones — don't reach for a method or
  concept from three chapters ahead just because it's more concise.
- **Every new term gets a "What is...?" box** the first time it appears, not
  buried in a paragraph.
- **No placeholder text** in anything merged to `main` — no `TODO`, `Lorem
  ipsum`, `[insert X]` outside of the intentional exercise `# TODO` comments.
- **No API keys or secrets** committed anywhere, ever.
- **Before declaring a chapter "done," read it end-to-end as a first-time
  learner** — check that no jargon is introduced without a "What is...?" box
  first, and that every quiz question has a working Check button.

## Workflow for pushing a new/updated chapter

```bash
git add .
git commit -m "Add Chapter N: <title>"
git push
```

No branch/PR ceremony needed for a solo-maintained repo — manual verification
(above) is the safety net, since there's no CI pipeline for this repo yet.

## Deploying

Pushing to `main` triggers `.github/workflows/pages.yml`, which publishes the
whole repo to GitHub Pages at `https://technaom.github.io/python-for-everyone/`.
No separate build step — it's plain HTML/CSS/JS served as-is.
