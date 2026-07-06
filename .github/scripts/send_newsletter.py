"""
Builds a "new chapter shipped" email from the template in
docs/newsletter-template.md and, if explicitly confirmed, sends it to
every subscriber via the Buttondown API.

This is deliberately conservative because sending is not reversible:
  - dry_run defaults to "true" in the workflow -- this script always
    prints the built email either way, so you can review it.
  - When dry_run is "false", it ALSO requires confirm_send to be the
    exact string "SEND" (case-sensitive) before it will call the API.
    Any other value -- including a typo -- blocks the send and exits
    with an error instead of silently doing nothing.

NOTE ON BUTTONDOWN'S API BEHAVIOR: creating an email via POST /v1/emails
sends it immediately on most Buttondown plans (there is no separate
"confirm" step server-side once the API call succeeds) -- treat a
successful API response as "this has gone out," not as a draft. The
first time you use this for a real send, check your Buttondown
dashboard right after to confirm what actually happened on your plan
before trusting it for future chapters.
"""

import os
import sys
import urllib.request
import urllib.error
import json

SITE_URL = "https://technaom.github.io/python-for-everyone"
BUTTONDOWN_API_URL = "https://api.buttondown.email/v1/emails"


def build_email(chapter_number, chapter_title, chapter_path, project_name,
                 subtopics, hook_line, ps_teaser):
    chapter_url = f"{SITE_URL}/chapters/{chapter_path}/lesson.html"

    subtopic_lines = [line.strip() for line in subtopics.split("|") if line.strip()]
    subtopics_block = "\n".join(subtopic_lines)

    subject = f"🐍 Chapter {chapter_number} is live — {chapter_title}"

    body_parts = [
        "Hey there,",
        "",
        f"**Chapter {chapter_number}: {chapter_title}** just went live in Python for Everyone. 🎉",
        "",
        "Here's what's in it:",
        "",
        subtopics_block,
        "",
        "🧩 8 auto-graded coding challenges — runs your actual Python, right in your browser",
        '💼 An interview-question bank with real "strong answer / red flag / follow-up" breakdowns',
        f"🛠️ A real project: {project_name}",
        "",
    ]

    if hook_line:
        body_parts.append(hook_line)
        body_parts.append("")

    body_parts.extend([
        f"👉 **[Start Chapter {chapter_number} →]({chapter_url})**",
        "",
        "As always: no sign-up, no paywall, just the link.",
        "",
        "— Manohar",
    ])

    if ps_teaser:
        body_parts.append("")
        body_parts.append(f"P.S. {ps_teaser}")

    body = "\n".join(body_parts)
    return subject, body


def main():
    chapter_number = os.environ["CHAPTER_NUMBER"]
    chapter_title = os.environ["CHAPTER_TITLE"]
    chapter_path = os.environ["CHAPTER_PATH"]
    project_name = os.environ["PROJECT_NAME"]
    subtopics = os.environ["SUBTOPICS"]
    hook_line = os.environ.get("HOOK_LINE", "")
    ps_teaser = os.environ.get("PS_TEASER", "")
    dry_run = os.environ.get("DRY_RUN", "true").strip().lower()
    confirm_send = os.environ.get("CONFIRM_SEND", "")

    subject, body = build_email(
        chapter_number, chapter_title, chapter_path, project_name,
        subtopics, hook_line, ps_teaser,
    )

    print("=" * 60)
    print("SUBJECT:", subject)
    print("=" * 60)
    print(body)
    print("=" * 60)

    if dry_run != "false":
        print("\nDRY RUN -- nothing was sent. Set dry_run to \"false\" and "
              "confirm_send to \"SEND\" to actually send this.")
        return

    if confirm_send != "SEND":
        print(
            "\nERROR: dry_run is false but confirm_send was not exactly "
            "\"SEND\" (case-sensitive). Refusing to send. This is a "
            "safety check, not a bug -- re-run with confirm_send set to "
            "SEND if you really mean to send this to your whole list."
        )
        sys.exit(1)

    api_key = os.environ.get("BUTTONDOWN_API_KEY")
    if not api_key:
        print(
            "\nERROR: BUTTONDOWN_API_KEY secret is not set on this repo. "
            "Add it under Settings > Secrets and variables > Actions."
        )
        sys.exit(1)

    payload = json.dumps({"subject": subject, "body": body}).encode("utf-8")
    request = urllib.request.Request(
        BUTTONDOWN_API_URL,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Token {api_key}",
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = response.read().decode("utf-8")
            print("\nSENT. Buttondown API response:")
            print(result)
    except urllib.error.HTTPError as e:
        print(f"\nERROR: Buttondown API returned {e.code}: {e.read().decode('utf-8')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
