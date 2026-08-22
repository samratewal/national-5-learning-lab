import importlib.util
import json
from pathlib import Path


def load_validator():
    path = Path(__file__).parents[1] / "scripts" / "validate_session.py"
    spec = importlib.util.spec_from_file_location("validate_session", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_repo(tmp_path: Path, official: bool = True):
    (tmp_path / "sessions").mkdir()
    lesson = (
        "# Week 001: Algebra Foundations\n\n"
        "## 60-Minute Plan\n\nPlan.\n\n"
        "## Learning Goals\n\nGoals.\n\n"
        "## Simple Explanation\n\nExplain.\n\n"
        "## Worked Examples\n\nExamples.\n\n"
        "## Practice Activity\n\nPractice.\n\n"
        "## Quiz\n\nQuestions.\n\n"
        "## Answers\n\nAnswers.\n\n"
        "## Sources and Further Learning\n\n"
        "- https://education.gov.scot/source\n"
        "- https://example.edu/source\n"
    )
    (tmp_path / "sessions" / "week-001.md").write_text(lesson)
    ledger = {
        "version": 1,
        "entries": [{
            "week": 1,
            "concept_id": "math-algebra-foundations",
            "track": "mathematical-reasoning",
            "level": "National 5 beginner",
            "core_concepts": ["variables", "equations"],
            "builds_on": [],
            "sources": [
                {"url": "https://education.gov.scot/source", "official": official},
                {"url": "https://example.edu/source", "official": False},
            ],
        }],
    }
    (tmp_path / "curriculum-ledger.json").write_text(json.dumps(ledger))
    (tmp_path / "progress.md").write_text("| 001 | Algebra Foundations | ⬜ Not started |\n")


def test_rejects_session_without_official_source(tmp_path):
    make_repo(tmp_path, official=False)
    validator = load_validator()
    errors = validator.validate_session(tmp_path, 1)
    assert any("at least one official or primary source" in error for error in errors)


def test_rejects_reused_concept_id(tmp_path):
    make_repo(tmp_path)
    ledger_path = tmp_path / "curriculum-ledger.json"
    ledger = json.loads(ledger_path.read_text())
    duplicate = dict(ledger["entries"][0])
    duplicate["week"] = 2
    ledger["entries"].append(duplicate)
    ledger_path.write_text(json.dumps(ledger))
    (tmp_path / "sessions" / "week-002.md").write_text(
        (tmp_path / "sessions" / "week-001.md").read_text().replace("Week 001", "Week 002")
    )
    with (tmp_path / "progress.md").open("a") as progress:
        progress.write("| 002 | Algebra Again | ⬜ Not started |\n")

    validator = load_validator()
    errors = validator.validate_session(tmp_path, 2)
    assert any("concept_id math-algebra-foundations is already used by week 001" in error for error in errors)


def test_rejects_missing_required_lesson_section(tmp_path):
    make_repo(tmp_path)
    lesson = tmp_path / "sessions" / "week-001.md"
    lesson.write_text(lesson.read_text().replace("## Practice Activity", "## Reading"))
    validator = load_validator()
    errors = validator.validate_session(tmp_path, 1)
    assert any("missing practice activity section" in error for error in errors)


def test_rejects_ledger_source_missing_from_lesson(tmp_path):
    make_repo(tmp_path)
    lesson = tmp_path / "sessions" / "week-001.md"
    lesson.write_text(lesson.read_text().replace("https://example.edu/source", ""))
    validator = load_validator()
    errors = validator.validate_session(tmp_path, 1)
    assert any("source URL is absent from lesson" in error for error in errors)


def test_rejects_missing_progress_row(tmp_path):
    make_repo(tmp_path)
    (tmp_path / "progress.md").write_text("| Week | Topic | Status |\n")
    validator = load_validator()
    errors = validator.validate_session(tmp_path, 1)
    assert any("progress row for week 001 must occur exactly once" in error for error in errors)
