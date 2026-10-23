#!/usr/bin/env python3
"""Build a practice exam paper for every Sunday test day.

Each paper draws its questions from the topics covered in that week's study
blocks, so it tests exactly what was revised. Every question carries its mark
value and a full marking scheme, plus a score tracker so weak topics are obvious.

Output: docs/test-1.html ... docs/test-7.html
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONTENT = ROOT / "content"

SUNDAY_DAYS = [3, 10, 17, 24, 31, 38, 45]
PAPER_TITLE = {1: "Week 1", 2: "Week 2", 3: "Week 3", 4: "Week 4",
               5: "Week 5", 6: "Week 6", 7: "Week 7"}

NAV = """<nav class="top"><div class="wrap">
  <a href="index.html">Home</a>
  <a href="plan.html">Plan</a>
  <a href="maths.html">Maths</a>
  <a href="physics.html">Physics</a>
  <a href="english.html">English</a>
  <a href="business-management.html">Business</a>
  <a href="design-manufacture.html">Design</a>
  <a href="pe.html">PE</a>
  <a href="practical-cookery.html">Cookery</a>
  <a href="flashcards.html">Flashcards</a>
  <a href="quizzes.html">Quizzes</a>
  <a href="tests.html">Tests</a>
  <a href="past-papers.html">Past papers</a>
</div></nav>"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def md_inline(s):
    import re
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def md_block(text):
    import re
    text = (text or "").strip()
    if not text:
        return ""
    out, buf, in_list = [], [], False

    def flush():
        if buf:
            out.append("<p>" + md_inline(" ".join(buf).strip()) + "</p>")
            buf.clear()

    for raw in text.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            flush()
            if in_list:
                out.append("</ul>"); in_list = False
            continue
        m = re.match(r"^[-*]\s+(.*)$", line)
        if m:
            flush()
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append("<li>" + md_inline(m.group(1)) + "</li>")
            continue
        if in_list:
            out.append("</ul>"); in_list = False
        buf.append(line.strip())
    flush()
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def load():
    sched = json.loads((DOCS / "schedule.json").read_text(encoding="utf-8"))
    content = {}
    for f in sorted(CONTENT.glob("*.json")):
        if f.name.startswith("_"):
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        content[d["subject"]] = d
    return sched, content


def week_topics(sched, week):
    """Topics studied in the study days of this week (excluding the test day)."""
    first = (week - 1) * 7 + 1
    last = min(week * 7, len(sched["days"]))
    out = []
    for d in sched["days"]:
        if not (first <= d["n"] <= last) or d["n"] in SUNDAY_DAYS:
            continue
        for b in d["blocks"]:
            if b["subject"] in ("review", "test"):
                continue
            for t in b["topics"]:
                if "past-paper" in t:
                    continue
                out.append((b["subject"], t))
    seen, uniq = set(), []
    for s, t in out:
        if (s, t) not in seen:
            seen.add((s, t)); uniq.append((s, t))
    return uniq


def build_paper(week, topics, content, sched):
    rows, marks_total, qn = [], 0, 0
    scheme = []
    tracker = []

    for subject, slug in topics:
        d = content.get(subject)
        if not d:
            continue
        meta = sched["subjects"].get(subject, {})
        topic = next((t for t in d["topics"] if t["slug"] == slug), None)
        if not topic:
            continue
        # one question per topic keeps the paper inside a realistic 55 minutes
        for p in topic.get("practice", [])[:1]:
            qn += 1
            marks = 2
            marks_total += marks
            rows.append(
                f'<div class="q"><div class="qhead"><span class="qnum">{qn}</span>'
                f'<span class="qmarks">{marks} marks</span></div>'
                f'<div class="qbody">{md_block(p["q"])}</div>'
                f'<div class="qsrc">{meta.get("icon","")} {esc(meta.get("name",""))} '
                f'&middot; {esc(topic["title"])}</div></div>'
            )
            scheme.append(
                f'<details><summary>Q{qn} — model answer</summary>'
                f'<div class="body">{md_block(p["a"])}</div></details>'
            )
        tracker.append(
            f'<tr><td>{meta.get("icon","")} {esc(topic["title"])}</td>'
            f'<td class="c">2</td><td class="c"></td><td class="c"></td></tr>'
        )
    return rows, scheme, tracker, marks_total, qn


def render(week, rows, scheme, tracker, marks_total, qn, subjects_used):
    subj_list = " &middot; ".join(subjects_used)
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Week {week} Practice Exam &mdash; N5 Prelim Revision</title>
<link rel="stylesheet" href="style.css">
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}},svg:{{fontCache:'global'}}}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
{NAV}
<main class="wrap">
<p class="crumb"><a href="plan.html">&larr; Back to the plan</a></p>
<h1>📝 Week {week} Practice Exam</h1>
<p class="lede">{subj_list}</p>

<div class="callout">
<strong>How to sit this paper.</strong>
<ol>
<li><strong>Block 1 (55 min):</strong> no notes, no phone, no looking ahead. Write your answers on paper.</li>
<li><strong>Block 2 (55 min):</strong> mark your own work using the marking scheme below. Be honest — an inflated
score tells you nothing useful.</li>
<li>Fill in the score tracker. Any topic where you scored <strong>under 70%</strong> goes back into next week's revision.</li>
</ol>
</div>

<div class="stats">
  <div><b>{qn}</b><span>questions</span></div>
  <div><b>{marks_total}</b><span>marks</span></div>
  <div><b>{len(tracker)}</b><span>topics</span></div>
  <div><b>55</b><span>minutes</span></div>
</div>

<h2>Paper</h2>
{''.join(rows)}

<hr>
<h2>Marking scheme</h2>
<p class="note">Mark strictly against these answers. Award a mark only where the required working or point is present.
For maths and physics, a correct answer with no working scores <strong>nothing</strong>.</p>
{''.join(scheme)}

<hr>
<h2>Score tracker</h2>
<p>Fill this in as you mark. Anything under 70% goes back on your revision list.</p>
<div class="tbl-wrap"><table>
<thead><tr><th>Topic</th><th>Available</th><th>Your score</th><th>%</th></tr></thead>
<tbody>{''.join(tracker)}</tbody></table></div>

<h2>What to do next</h2>
<ul>
<li>List every topic below 70% and redo its practice questions on the topic page.</li>
<li>Rewatch the video for that topic — the ▶ button is on the topic page.</li>
<li>Bring the weak topics forward into next week rather than leaving them to the end.</li>
</ul>

<footer>
<p><a href="plan.html">Back to the 45-day plan</a> &middot;
<a href="index.html">Revision hub home</a></p>
</footer>
</main>
</body>
</html>"""


def main():
    sched, content = load()
    made = 0
    prev = []
    for week in range(1, 8):
        topics = week_topics(sched, week)
        # a short week (like the 3-day taper) becomes cumulative with the previous
        if len(topics) < 8 and prev:
            seen = set(topics)
            topics = prev + [x for x in topics if x not in seen]
        prev = week_topics(sched, week)
        rows, scheme, tracker, marks_total, qn = build_paper(week, topics, content, sched)
        if not qn:
            print(f"week {week}: no questions"); continue
        used = []
        for s, _ in topics:
            n = sched["subjects"].get(s, {}).get("name", s)
            if n not in used:
                used.append(n)
        html = render(week, rows, scheme, tracker, marks_total, qn, used)
        (DOCS / f"test-{week}.html").write_text(html, encoding="utf-8")
        print(f"test-{week}.html  {qn:3} questions  {marks_total:4} marks  {len(tracker):2} topics")
        made += 1
    print("papers built:", made)


if __name__ == "__main__":
    main()
