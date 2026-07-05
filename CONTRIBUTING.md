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
├── practice/                   → deeper per-topic problem bank (see below)
│   ├── README.md
│   ├── index.html
│   ├── starter.py
│   └── solution.py
├── challenges.html             → HackerRank-style auto-graded coding challenges (see below;
│                                  standard from Chapter 6 onward, chapter root, not a subfolder)
└── project/
    ├── README.md                → plain-text version for repo browsing
    ├── index.html                → styled version linked from the live site
    ├── starter.py
    └── solution.py
```

**The `practice/` folder is a deeper problem bank, on top of `exercises/`.**
Where `exercises/` stays a short, guided 4-task intro, `practice/` groups
problems by the chapter's actual sub-topics (the same sections listed in
`lesson.html`'s page-toc) and gives each sub-topic **5-10 problems**,
following one `starter.py`/`solution.py` pair per chapter (same
multi-TODO-in-one-file convention as `exercises/`, just with numbered
TODOs like `2.1`, `2.2`, ... `2.A`, `2.B` per topic instead of one flat
sequence). Within each topic's problem set, include at least **two
scenario-based problems** — framed as a real workplace situation or an
actual interview question, not just "compute X" — since these are the
ones that carry over into interview prep. Mark those two with `.scenario-card`
(a `.scenario-tag` badge reading "💼 Scenario" or "💼 Interview Prep") instead
of `.task-card`, and combine `task-card debug-card` classes for any
"Debug the Code" problem within the practice set (same pattern
`exercises/` already uses for its one debug task). Every practice problem
must still obey "stick to what's been taught" — a scenario problem is
just a real-world framing, not a license to reach for un-taught syntax.
`practice/` slots into the chapter-nav chain right after `exercises/` and
before `challenges.html`/`interview-questions.html` (see below):
`quiz → exercises → practice → challenges → interview-questions → project`.
See `chapters/chapter-01-first-program/practice/` for a fully worked example.

**Chapters 6 onward are "deeper" chapters — more sub-topics, real-world
framing everywhere, a Challenges page, and a bigger project.** This
standard was piloted on Chapter 6 (Strings Deep Dive) and confirmed
working before being written down here:

- **More sub-topics than Chapters 1-5's flat 4.** Give a chapter as many
  sub-topics as the material actually needs (Chapter 6 used 6) rather than
  forcing everything into 4 — `lesson.html`'s page-toc, `quiz.html`,
  `exercises/`, and `practice/` all scale with however many sub-topics you
  pick.
- **Real-world software use cases belong IN the lesson, not bolted on.**
  Every sub-topic should open with or include a genuine production-flavored
  example (masking sensitive data, parsing log lines, cleaning form input,
  building a receipt/notification string) rather than an abstract "here's
  the syntax" demo. `practice/`'s scenario-tagged problems should lean the
  same way.
- **`interview-questions.html` gets a much bigger set** — aim for 12-14
  `.qa-item` accordions and a matching 12-14-item rapid-fire quiz, not the
  ~6-8 that Chapters 1-5 used. Cover the questions people actually get
  asked about this topic in real interviews, not just chapter-recap
  trivia. Verify every rapid-fire answer by actually running the
  corresponding Python before writing it into `data-answers`.
- **`project/` becomes a bigger, multi-feature mini-app** — still one
  Python file, still within that chapter's cumulative allowed features,
  but a menu-driven tool with several real operations and running session
  state, not a single-purpose script. Chapter 6's Password Strength &
  Policy Auditor is the reference example.
- **From Chapter 7 onward, `project/README.md` and `project/index.html`
  also list 4 more real-world project ideas**, on top of the one fully
  built project (starter.py/solution.py) — five real-world problems
  total per chapter, giving learners a genuine choice of what to build
  for their portfolio instead of everyone shipping the identical project.
  Each of the 4 extra ideas gets a short brief (problem statement, what
  it should do, a suggested approach/starting point) but **no provided
  starter.py/solution.py** — building it unassisted is the point. Keep
  every idea grounded in an actual real-world use case (not abstract
  practice) and solvable with only that chapter's cumulative allowed
  features. This does not apply retroactively to Chapters 1-6.
- **`challenges.html` is a new page: HackerRank-style, auto-graded,
  client-side.** It lives at the chapter root (`../../` asset depth, a
  sibling of `lesson.html`/`quiz.html`/`interview-questions.html`, NOT a
  subfolder), between `practice/` and `interview-questions.html` in the
  nav chain. It's powered by `assets/challenge-engine.js` — a Pyodide-based
  judge that actually executes a learner's function against real test
  cases and reports pass/fail per case, entirely in the browser, no
  backend. Read the doc comment at the top of `challenge-engine.js` for
  the exact HTML contract (`.challenge-card`, `data-challenge-code`
  textarea, `data-challenge-run` button, `data-challenge-results` div, and
  a `<script type="application/json" data-challenge-tests>` block per
  problem). Include `<script src="{prefix}assets/challenge-engine.js">`
  alongside the usual progress.js/chapters-data.js/sidebar.js includes.
  Aim for ~8 problems (Easy→Medium mix), 4-6 test cases each including
  edge cases, and a `<details class="qa-item"><summary>Show Solution</summary>`
  reveal per problem. **Before publishing, write every reference solution
  to a scratch script and actually run every one of its own test cases
  through it with `python3`** — a wrong `expected` value silently breaks
  the grader for a learner who wrote genuinely correct code. See
  `chapters/chapter-06-strings-deep-dive/challenges.html` for a fully
  worked example.

**Readability standard (applies to every chapter, retrofit and new,
2026-07-05):** early lesson prose read as one dense wall of paragraphs —
this is a hard "no" going forward. Concrete rules, not vibes:

- **No paragraph should explain more than one idea.** If a paragraph is
  listing 2+ rules back to back (e.g. "slicing works like X, a third
  number does Y, and a negative version does Z"), it must become a
  bulleted list instead — one `<li>` per rule.
- **Never stack two dense blocks back to back.** A long paragraph
  immediately followed by a long `.what-is` box (or another paragraph)
  is the exact failure mode to avoid — break it up with a code window,
  a visual, or just shorter sentences in between.
- **If a concept is inherently visual or spatial, show it before
  explaining it in prose.** String indexing, truth tables for logical
  operators, a number line for `range()`, a step-by-step trace of a
  loop's variables — these read far better as a small `.output-block`
  diagram (monospace `<pre>`, verified character-aligned by actually
  running a Python script to generate the spacing, never hand-typed —
  see the fix in `chapters/chapter-06-strings-deep-dive/lesson.html`'s
  indexing section for the exact pattern and why hand-typed alignment is
  a trap) than as a paragraph of positional description.
- **Trim "What is...?" boxes to the one distinction that actually
  matters**, not every tangential fact about the term.
- This is a formatting/prose pass, not a content rewrite — don't change
  what's technically taught, just how densely it's presented.

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
   practice bank → challenges (Ch6+) → interview questions → project →
   back to all chapters.
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
