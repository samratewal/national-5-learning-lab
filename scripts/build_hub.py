#!/usr/bin/env python3
"""Generate tests.html, past-papers.html and a refreshed index.html."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

NAV = """<nav class="top"><div class="wrap">
  <a href="index.html">Home</a>
  <a href="plan.html">Plan</a>
  <a href="flashcards.html">Flashcards</a>
  <a href="quizzes.html">Quizzes</a>
  <a href="tests.html">Tests</a>
  <a href="past-papers.html">Past papers</a>
</div></nav>"""

SUBJ_NAV = """<nav class="top"><div class="wrap">
  <a href="index.html">Home</a>
  <a href="plan.html">Plan</a>
  <a href="maths.html">Maths</a>
  <a href="physics.html">Physics</a>
  <a href="english.html">English</a>
  <a href="business-management.html">Business</a>
  <a href="design-manufacture.html">Design</a>
  <a href="pe.html">PE</a>
  <a href="practical-cookery.html">Cookery</a>
</div></nav>"""

CONTENT = ROOT / "content"

# Per-subject page metadata. Topic counts are NEVER written here; they are
# derived from content/*.json so the hub cannot drift out of sync again.
SUBJ_META = {
    "maths":  ("maths.html", "📐", "Mathematics", "2 papers"),
    "physics": ("physics.html", "⚛️", "Physics", "110 marks"),
    "english": ("english.html", "📖", "English", "RUAE + Critical + Folio"),
    "bm":     ("business-management.html", "💼", "Business Management", "90 marks"),
    "dm":     ("design-manufacture.html", "🔧", "Design &amp; Manufacture", "80 marks"),
    "pe":     ("pe.html", "🏃", "Physical Education", "portfolio"),
    "cook":   ("practical-cookery.html", "🍳", "Practical Cookery", "paper + practical"),
}


def _load_content():
    import json
    out = {}
    for f in sorted(CONTENT.glob("*.json")):
        if f.name.startswith("_"):
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        out[d["subject"]] = d
    return out


def topic_counts():
    return {k: len(v.get("topics", [])) for k, v in _load_content().items()}


def practice_total():
    return sum(len(t.get("practice", []))
               for v in _load_content().values()
               for t in v.get("topics", []))


def head(title):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="style.css?v=3">
</head>
<body>"""


TESTS = [
    (1, "Sun 25 Oct", "Maths fractions/surds, physics vectors & v-t graphs, English RUAE"),
    (2, "Sun 1 Nov", "Maths algebra & straight line, physics dynamics, English word choice, business, D&M"),
    (3, "Sun 8 Nov", "Maths trig & circle work, physics electricity, business marketing, D&M materials"),
    (4, "Sun 15 Nov", "Maths statistics & probability, physics matter, English Scottish text, D&M"),
    (5, "Sun 22 Nov", "Maths past paper work, physics waves, business operations, cookery"),
    (6, "Sun 29 Nov", "Physics radiation & space, business finance, D&M manufacture, PE factors"),
    (7, "Sun 6 Dec", "Final cumulative paper — all subjects"),
]

PAST = [
    ("📐 Mathematics", "https://www.sqa.org.uk/sqa/47419.html",
     "Official N5 Maths past papers and marking instructions", "SQA"),
    ("⚛️ Physics", "https://www.sqa.org.uk/sqa/47430.html",
     "Official N5 Physics past papers and marking instructions", "SQA"),
    ("📖 English", "https://www.sqa.org.uk/sqa/47410.html",
     "Official N5 English past papers and marking instructions", "SQA"),
    ("💼 Business Management", "https://www.sqa.org.uk/sqa/47436.html",
     "Official N5 Business Management past papers and marking instructions", "SQA"),
    ("🔧 Design & Manufacture", "https://www.sqa.org.uk/sqa/47457.html",
     "Official N5 Design & Manufacture past papers", "SQA"),
    ("🏃 Physical Education", "https://www.sqa.org.uk/sqa/47399.html",
     "N5 PE coursework, portfolio assessment task and marking", "SQA"),
    ("🍳 Practical Cookery", "https://www.sqa.org.uk/sqa/47439.html",
     "Official N5 Practical Cookery past papers and coursework", "SQA"),
    ("📐 Maths extra practice", "https://www.national5maths.co.uk/free-national-5-maths/",
     "Free N5 Maths past papers 2013–2026 with worked solutions", "national5maths.co.uk"),
    ("📐 Maths by topic", "https://maths.scot/national-5-maths",
     "N5 Maths notes and worked examples organised by topic", "maths.scot"),
    ("📚 All subjects", "https://www.sqa.org.uk/pastpapers/findpastpaper.htm",
     "SQA past-paper finder — every National 5 subject", "SQA"),
]


def build_tests():
    rows = []
    for n, date, covers in TESTS:
        rows.append(
            f'<a class="card" href="test-{n}.html" style="text-decoration:none">'
            f'<h3>📝 Week {n} practice exam</h3>'
            f'<p>{date}</p><p>{covers}</p></a>')
    return (head("Practice exams")
            + NAV
            + '<main class="wrap"><h1>📝 Practice exams</h1>'
            '<p class="lede">Every Sunday is a test day. Sit the paper in 55 minutes with no notes, '
            'then mark it in the second block and fill in the score tracker.</p>'
            '<div class="callout"><strong>Why Sunday?</strong> Testing yourself is far more effective than '
            're-reading. The score tracker shows exactly which topics to put back into next week.</div>'
            '<div class="grid two">' + "".join(rows) + '</div>'
            '<h2>How to mark your own paper</h2>'
            '<ul><li>Mark strictly — an inflated score hides the topics you need to fix.</li>'
            '<li>A correct answer with <strong>no working</strong> scores zero in maths and physics.</li>'
            '<li>Anything under 70% goes back on next week\'s revision list.</li></ul>'
            '<footer><p><a href="plan.html">Back to the 45-day plan</a></p></footer></main></body></html>')


def build_past():
    cards = []
    for name, url, desc, src in PAST:
        cards.append(
            f'<a class="card" href="{url}" target="_blank" rel="noopener" style="text-decoration:none">'
            f'<h3>{name}</h3><p>{desc}</p>'
            f'<p style="font-size:12px;color:var(--dim)">↗ {src}</p></a>')
    return (head("Past papers")
            + NAV
            + '<main class="wrap"><h1>📄 Past papers &amp; marking schemes</h1>'
            '<p class="lede">Every link below is an official SQA resource or a long-established '
            'free N5 site. Nothing here is behind a paywall.</p>'
            '<div class="callout"><strong>Mark your own work.</strong> A past paper is only worth doing '
            'if you mark it. The marking instructions show the exact wording SQA accepts — that is how you '
            'find out what an A-grade answer actually looks like.</div>'
            '<div class="grid two">' + "".join(cards) + '</div>'
            '<footer><p><a href="plan.html">Back to the plan</a></p>'
            '<p>Past papers are free to download from SQA for personal study.</p></footer></main></body></html>')


def build_index():
    tools = [
        ("plan.html", "📅", "45-day plan", "Two 55-minute blocks every night, every topic dated"),
        ("flashcards.html", "🃏", "Flashcards", f"{practice_total()} flip cards: key rules and practice questions"),
        ("quizzes.html", "✅", "Topic quizzes", "Self-marking — spot weak topics instantly"),
        ("tests.html", "📝", "Practice exams", "7 papers, one every Sunday, with marking schemes"),
        ("past-papers.html", "📄", "Past papers", "Official SQA papers and marking instructions"),
    ]
    counts = topic_counts()
    subjects = [
        (page, icon, name, f"{counts.get(code, 0)} topics &middot; {suffix}")
        for code, (page, icon, name, suffix) in SUBJ_META.items()
    ]
    t = "".join(f'<a class="card" href="{u}" style="text-decoration:none"><h3>{i} {n}</h3><p>{d}</p></a>'
                for u, i, n, d in tools)
    s = "".join(f'<a class="card" href="{u}" style="text-decoration:none"><h3>{i} {n}</h3><p>{d}</p></a>'
                for u, i, n, d in subjects)
    return (head("S4 Prelim Revision Hub")
            + NAV
            + '<main class="wrap"><h1>S4 Prelim Revision Hub</h1>'
            f'<p class="lede">7 subjects &middot; {sum(counts.values())} topics &middot; 45 nights &middot; 2 hours a night</p>'
            '<div class="callout"><strong>Start here.</strong> Open the <a href="plan.html">45-day plan</a> '
            'and work down it night by night. Every topic links to its rule, worked example, exam trap, '
            'practice questions and a video.</div>'
            '<div class="stats"><div><b>7</b><span>subjects</span></div>'
            f'<div><b>{sum(counts.values())}</b><span>topics</span></div><div><b>45</b><span>nights</span></div>'
            f'<div><b>{practice_total()}</b><span>practice questions</span></div></div>'
            '<h2>Study tools</h2><div class="grid two">' + t + '</div>'
            '<h2>Subjects</h2><div class="grid two">' + s + '</div>'
            '<h2>The rule that matters most</h2>'
            '<p>At National 5, <strong>a correct answer with no working scores zero</strong> in maths and '
            'physics. In English, naming a technique without explaining its effect earns one mark at most. '
            'In business and design, undeveloped points score nothing at all.</p>'
            '<footer><p>Built from the official SQA National 5 course specifications.</p></footer>'
            '</main></body></html>')


def main():
    (DOCS / "tests.html").write_text(build_tests(), encoding="utf-8")
    (DOCS / "past-papers.html").write_text(build_past(), encoding="utf-8")
    (DOCS / "index.html").write_text(build_index(), encoding="utf-8")
    print("tests.html, past-papers.html, index.html written")


if __name__ == "__main__":
    main()
