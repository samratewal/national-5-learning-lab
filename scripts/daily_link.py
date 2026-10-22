#!/usr/bin/env python3
"""Emit tonight's revision message for the Discord daily drop.

Reads docs/schedule.json, finds today's entry, and prints a Discord-ready
message with direct links to the exact topics for tonight.

Used two ways:
  1. As a cron --no-agent job  -> stdout is delivered verbatim to Discord.
  2. Manually: python3 scripts/daily_link.py [YYYY-MM-DD]

Exit code 1 (with no output) if today is outside the plan window, so the
cron stays silent on days the plan is finished.
"""
import datetime
import json
import os
import pathlib
import sys

REPO = pathlib.Path("/Users/Sam/national-5-learning-lab")

def _find_schedule():
    """Locate schedule.json. This script is copied into ~/.hermes/scripts/ for
    the scheduler, so __file__-relative resolution is not reliable."""
    candidates = [
        pathlib.Path(os.environ.get("N5_REPO", "")) / "docs" / "schedule.json"
        if os.environ.get("N5_REPO") else None,
        REPO / "docs" / "schedule.json",
        pathlib.Path(__file__).resolve().parent.parent / "docs" / "schedule.json",
        pathlib.Path(__file__).resolve().parent / "schedule.json",
    ]
    for c in candidates:
        if c and c.exists():
            return c
    return REPO / "docs" / "schedule.json"


SCHEDULE = _find_schedule()
BASE = "https://samratewal.github.io/national-5-learning-lab"

WEEKDAY = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def load():
    if not SCHEDULE.exists():
        sys.exit(1)
    return json.loads(SCHEDULE.read_text(encoding="utf-8"))


def find_day(data, when):
    for d in data["days"]:
        if d["date"] == when.isoformat():
            return d
    return None


def link_for(subject_meta, topic_slug):
    return f"{BASE}/{subject_meta['page']}#{topic_slug}"


def render(data, day, when):
    subjects = data["subjects"]
    lines = []

    # header
    lines.append(f"**📚 Tonight's revision — Day {day['n']}**")
    lines.append(f"_{WEEKDAY[when.weekday()]} {when.strftime('%d %B')} · 2 hours · 2 blocks_")
    lines.append("")

    for i, b in enumerate(day["blocks"], 1):
        if b["subject"] == "review":
            lines.append(f"**Block {i} — 🔁 {b['label']}**")
            lines.append("No new topic. Redo questions you got wrong this week, from memory.")
            lines.append("")
            continue

        meta = subjects[b["subject"]]
        topics = b.get("topics", [])
        title_bits = []
        links = []
        for t in topics:
            if t in _past_papers():
                title_bits.append("timed past paper")
            else:
                title_bits.append(_topic_title(data, b["subject"], t))
                links.append(f"[{_topic_title(data, b['subject'], t)}]({link_for(meta, t)})")

        head = f"**Block {i} — {meta['icon']} {meta['name']}** ({b.get('min', 55)} min)"
        lines.append(head)
        if links:
            lines.append(" · ".join(links))
        if title_bits and not links:
            lines.append(f"⏱ {', '.join(title_bits)} — exam conditions, no notes.")
        lines.append(f"_{b.get('label', '')}_")
        lines.append("")

    lines.append(f"**Plan:** {BASE}/plan.html")
    lines.append("**Tick it off** when both blocks are done. Missed a night? Do not skip the topic —")
    lines.append("move it into the next night's break slot instead.")

    return "\n".join(lines)


def _past_papers():
    return {
        "maths-past-paper-1", "maths-past-paper-2", "maths-past-paper-3",
        "maths-past-paper-4", "maths-past-paper-5",
        "physics-past-paper-1", "physics-past-paper-2",
        "physics-past-paper-3", "physics-past-paper-4",
        "english-past-paper-1", "english-past-paper-2", "english-past-paper-3",
        "ruae-past-paper", "bm-past-paper-1", "dm-past-paper-1",
    }


def _topic_title(data, subject, slug):
    for t in data["topics"].get(subject, []):
        if t["slug"] == slug:
            return t["title"]
    return slug.replace("-", " ").title()


def main():
    if len(sys.argv) > 1:
        when = datetime.date.fromisoformat(sys.argv[1])
    else:
        when = datetime.date.today()

    data = load()
    day = find_day(data, when)
    if day is None:
        # Outside the plan window: stay silent, exit cleanly. A non-zero exit
        # would be reported as a failure by the scheduler every single day.
        return 0
    print(render(data, day, when))
    return 0


if __name__ == "__main__":
    sys.exit(main())
