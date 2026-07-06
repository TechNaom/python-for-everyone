# Newsletter Automation — "New Chapter Shipped" Email

How to notify the mailing list after a chapter (or module exam) goes
live, via the `.github/workflows/send-newsletter.yml` GitHub Action.
This calls the [Buttondown](https://buttondown.email) API directly —
no manual dashboard login needed to send — but it's still triggered
by a human every time (`workflow_dispatch`), never automatically on
push, since sending to the whole list isn't reversible.

## One-time setup

1. Create a free [Buttondown](https://buttondown.email) account if you
   haven't already.
2. Get your API key from Buttondown's settings.
3. In this repo: **Settings → Secrets and variables → Actions → New
   repository secret**, name it `BUTTONDOWN_API_KEY`, paste the key.

## How to send an update

1. Go to the repo's **Actions** tab → **Send Chapter Newsletter** →
   **Run workflow**.
2. Fill in the inputs:
   - `chapter_number` — e.g. `12`
   - `chapter_title` — e.g. `Exception Handling`
   - `chapter_path` — the folder name, e.g. `chapter-12-exception-handling`
   - `project_name` — this chapter's project, e.g. `ATM Simulator`
   - `subtopics` — one line per subtopic, separated by `|`, e.g.
     `🎯 What exceptions are|🛡️ try/except/finally|🚨 Custom exception classes`
   - `hook_line` (optional but recommended) — one genuinely fresh
     sentence about what's interesting in this chapter. This is the
     one part worth writing by hand each time — it's what keeps the
     email feeling personal instead of templated.
   - `ps_teaser` (optional) — a line about what's coming next.
   - `dry_run` — leave as `true` first. This only prints the built
     email in the workflow log; nothing is sent.
3. **Check the workflow's log output** and read the printed email
   before doing anything else.
4. If it looks right, run the workflow again with `dry_run` set to
   `false` **and** `confirm_send` set to exactly `SEND` (case-sensitive
   — anything else is rejected on purpose). This is the only
   combination that actually calls the Buttondown API.

## Worked example (Chapter 11, for reference)

Inputs that would produce Chapter 11's announcement:

| Input | Value |
|---|---|
| `chapter_number` | `11` |
| `chapter_title` | `Modules & Packages` |
| `chapter_path` | `chapter-11-modules-packages` |
| `project_name` | `Expense Tracker` |
| `subtopics` | `📦 What a module actually is\|🔀 Every import variation\|🧮 The math module\|📅 The datetime module\|🎲 The random module` |
| `hook_line` | `This is also the first chapter where import is allowed at all — everything before this had to be built from scratch.` |
| `ps_teaser` | `Chapter 12 (Exception Handling) is already in progress.` |

Which builds:

```markdown
Subject: 🐍 Chapter 11 is live — Modules & Packages

Hey there,

**Chapter 11: Modules & Packages** just went live in Python for Everyone. 🎉

Here's what's in it:

📦 What a module actually is
🔀 Every import variation
🧮 The math module
📅 The datetime module
🎲 The random module

🧩 8 auto-graded coding challenges — runs your actual Python, right in your browser
💼 An interview-question bank with real "strong answer / red flag / follow-up" breakdowns
🛠️ A real project: Expense Tracker

This is also the first chapter where import is allowed at all — everything before this had to be built from scratch.

👉 **[Start Chapter 11 →](https://technaom.github.io/python-for-everyone/chapters/chapter-11-modules-packages/lesson.html)**

As always: no sign-up, no paywall, just the link.

— Manohar

P.S. Chapter 12 (Exception Handling) is already in progress.
```

## Important notes

- **First real send: verify what actually happened.** Buttondown's API
  behavior around drafts vs. immediate sending can depend on your plan.
  The first time you run this with `dry_run: false`, check your
  Buttondown dashboard right after to confirm the email actually went
  out (or didn't) before relying on it for future chapters.
- The two-input safety check (`dry_run: false` **and** `confirm_send:
  SEND`) is deliberate — a typo in either one blocks the send instead
  of silently doing nothing, so you always get a clear error rather
  than an ambiguous no-op.
- Buttondown auto-includes an unsubscribe link at the bottom of every
  email — don't add your own.
- If several chapters ship close together, it's fine to run this once
  covering multiple chapters rather than firing it once per chapter.
- The actual template logic lives in
  [`.github/scripts/send_newsletter.py`](../.github/scripts/send_newsletter.py)
  if you want to adjust the wording — the workflow file just passes
  your inputs through as environment variables.
