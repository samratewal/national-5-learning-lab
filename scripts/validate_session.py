#!/usr/bin/env python3
"""Validate one weekly learning session before publication."""

import argparse
import json
import re
from pathlib import Path


def validate_session(repo: Path, week: int):
    ledger = json.loads((repo / "curriculum-ledger.json").read_text())
    entries = [entry for entry in ledger.get("entries", []) if entry.get("week") == week]
    if len(entries) != 1:
        return [f"week {week:03} must occur exactly once in curriculum-ledger.json"]

    errors = []
    candidate = entries[0]
    for entry in ledger.get("entries", []):
        if entry.get("week") == week:
            continue
        if entry.get("concept_id") == candidate.get("concept_id"):
            errors.append(
                f"concept_id {candidate.get('concept_id')} is already used by week {entry['week']:03}"
            )
    sources = candidate.get("sources", [])
    if len(sources) < 2:
        errors.append(f"week {week:03} requires at least two credible sources")
    if not any(source.get("official") is True for source in sources):
        errors.append(f"week {week:03} requires at least one official or primary source")

    lesson_path = repo / "sessions" / f"week-{week:03}.md"
    lesson_text = lesson_path.read_text() if lesson_path.exists() else ""
    if not lesson_text:
        errors.append(f"week {week:03} lesson file is missing or empty")
    required_sections = {
        "60-minute plan": ("60-minute plan", "60 minute plan"),
        "learning goals": ("learning goals",),
        "simple explanation": ("simple explanation",),
        "worked examples": ("worked examples",),
        "practice activity": ("practice activity", "experiment", "coding activity", "project activity"),
        "quiz": ("quiz", "knowledge check"),
        "answers": ("answers", "answer key"),
        "sources and further learning": ("sources and further learning", "sources"),
    }
    headings = [
        re.sub(r"^#+\s*", "", line).strip().lower()
        for line in lesson_text.splitlines()
        if line.startswith("##")
    ]
    for label, alternatives in required_sections.items():
        if not any(any(term in heading for term in alternatives) for heading in headings):
            errors.append(f"week {week:03} missing {label} section")
    for source in sources:
        url = str(source.get("url", "")).rstrip("/")
        if url and url not in lesson_text:
            errors.append(f"source URL is absent from lesson: {url}")
    progress_text = (repo / "progress.md").read_text()
    progress_rows = re.findall(rf"^\|\s*{week:03}\s*\|", progress_text, flags=re.MULTILINE)
    if len(progress_rows) != 1:
        errors.append(f"progress row for week {week:03} must occur exactly once")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--week", type=int, required=True)
    args = parser.parse_args()
    errors = validate_session(args.repo.resolve(), args.week)
    if errors:
        for error in errors:
            print("ERROR:", error)
        raise SystemExit(1)
    print(f"SESSION VALID: week {args.week:03}")


if __name__ == "__main__":
    main()
