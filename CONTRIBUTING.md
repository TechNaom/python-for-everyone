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
├── lesson.html               → page-meta (badge/difficulty/reading time) → page-toc →
│                                hook → then, PER SUB-TOPIC: a .subtopic section with a
│                                .subtopic-label, plain-language concept, "What is...?"
│                                boxes, code-window annotated code (+ a .playground "Run
│                                Code" box if the example doesn't need input()), optional
│                                Go Deeper, and a short .quick-recap box — repeat this
│                                whole unit for each sub-topic in the chapter, then finish
│                                with one .real-world callout (3 bullets tying the whole
│                                chapter to genuine production/industry use) and one full
│                                .points-to-remember summarizing everything
├── quiz.html                  → fill-in-the-blank quiz covering every sub-topic, using
│                                 assets/quiz-engine.js (.fib-row, data-answers,
│                                 quiz-progress-fill, quiz-celebration); <body> needs
│                                 data-chapter-id="chapter-{NN}" so a perfect score marks
│                                 the chapter complete via assets/progress.js
├── interview-questions.html   → .qa-item accordions (strong answer / red flags /
│                                 follow-up), plus a rapid-fire fill-in-the-blank
│                                 review using the same quiz-engine.js pattern
├── exercises/
│   ├── README.md               → plain-text version for repo browsing / local cloning
│   ├── index.html              → styled version linked from the live site: task-card
│   │                              per TODO, code-window for starter code, download-links
│   │                              to the raw .py files, and at least one .debug-card
│   │                              ("Debug the Code") task with intentionally broken code
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

**Include `assets/progress.js` on every quiz page and every chapter-list
page** (index.html, docs/curriculum/index.html), and give each chapter-list
entry a `data-chapter-link="chapter-{NN}"` attribute so completed chapters
get a "✓ Completed" badge automatically. Only wire `assets/playground.js`
into examples that don't call `input()` — Pyodide's sandbox has no stdin.

**Every page needs the persistent chapter sidebar.** Right after the
opening `<body>` tag, include:

```html
<button id="sidebar-toggle" class="sidebar-toggle" aria-label="Toggle chapter list" aria-expanded="false">☰ Chapters</button>
<aside id="chapter-sidebar" class="sidebar" data-root="{prefix}" aria-label="Chapter navigation"></aside>
<div class="sidebar-scrim" id="sidebar-scrim"></div>
```

where `{prefix}` is the same relative-path-to-root prefix already used for
`assets/style.css` on that page. Set `data-active-chapter="chapter-{NN}"`
on `<body>` (a separate attribute from `data-chapter-id`, which
`quiz-engine.js` uses for progress-marking) so the sidebar highlights the
current chapter. Include `assets/chapters-data.js` and `assets/sidebar.js`
(after `assets/progress.js`) before `</body>`. When a new chapter is
built, update its entry in `assets/chapters-data.js` (`path: null` →
the real lesson.html path) — the sidebar picks it up automatically
everywhere, no per-page edits needed.

**Visual language is glassmorphic.** Card-style components use
`var(--color-card-bg)` (translucent) plus `backdrop-filter: var(--glass-blur)`
against the fixed gradient-mesh backdrop on `body::before` — match this
pattern for any new callout box rather than using a flat opaque background.

Then:

1. Add the new chapter as a link in `index.html`'s chapter list (move it out
   of "coming soon") **and** as a new `.roadmap-list` entry in
   `docs/curriculum/index.html` (move it from "Planned" to "Built").
2. Update `docs/curriculum/CURRICULUM_MAP.md` to match.
3. Verify every Python solution actually runs: `python3 solution.py` (pipe
   sample answers via `echo`/`printf` if it uses `input()`).
4. Open every `.html` page for the chapter directly in a browser (or via the
   local Pages preview) and click through every quiz Check button, every
   `chapter-nav` link, and every top-bar nav link before pushing — the whole
   chapter should form one connected loop: lesson → quiz → exercises →
   interview questions → project → back to all chapters.
5. **Every module (a group of 4-6 chapters shown as one section in the
   roadmap) ends with a written exam** at
   `assessments/written-exams/module-{N}-exam.md` — short-answer + scenario
   questions covering every chapter in that module, plus a full answer key
   (same style as the genai-for-everyone repo's exams). Write it once the
   module's last chapter is done.

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
