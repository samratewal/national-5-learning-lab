#!/usr/bin/env python3
"""Render one styled HTML page per subject from content/<subject>.json.

Each JSON file:
{
  "subject": "maths",
  "title": "Mathematics",
  "icon": "📐",
  "assessment": "Paper 1 ... | Paper 2 ...",
  "intro": "markdown paragraph",
  "topics": [
    {"slug": "...", "title": "...", "paper": "calc|noncalc|either",
     "rule": "markdown", "example": "markdown", "trap": "markdown",
     "practice": [{"q": "markdown", "a": "markdown"}]}
  ]
}

Run: python3 scripts/build_pages.py [subject ...]
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONTENT = ROOT / "content"

PAPER_BADGE = {
    "calc": ('🧮', "Calculator"),
    "noncalc": ('✋', "Non-calculator"),
    "either": ('⚖️', "Either paper"),
}

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
</div></nav>"""


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def md_inline(s):
    """Very small inline markdown: **bold**, *em*, `code`, $math$ passthrough."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def md_block(text):
    """Render a small markdown subset to HTML blocks."""
    text = text.strip()
    if not text:
        return ""
    out = []
    lines = text.split("\n")
    buf = []

    def flush():
        if buf:
            out.append("<p>" + md_inline(" ".join(buf).strip()) + "</p>")
            buf.clear()

    in_list = False
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush()
            if in_list:
                out.append("</ul>")
                in_list = False
            continue
        m = re.match(r"^[-*]\s+(.*)$", line)
        if m:
            flush()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>" + md_inline(m.group(1)) + "</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        buf.append(line.strip())
    flush()
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def render_topic(t, n):
    badge, label = PAPER_BADGE.get(t.get("paper", "either"), PAPER_BADGE["either"])
    prac = []
    for i, p in enumerate(t.get("practice", []), 1):
        prac.append(
            f'<div class="pq"><div class="q"><span class="qnum">{i}</span>'
            f'{md_block(p["q"])}</div>'
            f'<details><summary>Show answer</summary>'
            f'<div class="body">{md_block(p["a"])}</div></details></div>'
        )
    prac_html = "".join(prac)
    if prac_html:
        prac_html = f'<div class="prac"><h4>Practice</h4>{prac_html}</div>'

    return f"""
<section class="topic" id="{t['slug']}">
  <h3><span class="num">{n}</span>{esc(t['title'])}</h3>
  <div class="badges"><span class="tag paper">{badge} {label}</span></div>

  <div class="rule"><h4>💡 The rule</h4>{md_block(t['rule'])}</div>
  <div class="ex"><h4>📝 Worked example</h4>{md_block(t['example'])}</div>
  <div class="trap"><h4>🚨 Exam trap</h4>{md_block(t['trap'])}</div>
  {prac_html}
</section>"""


def render_page(data):
    slug = data["subject"]
    topics = data.get("topics", [])

    index_rows = "".join(
        f'<tr><td><a href="#{t["slug"]}">{esc(t["title"])}</a></td>'
        f'<td>{PAPER_BADGE.get(t.get("paper","either"), PAPER_BADGE["either"])[0]} '
        f'{PAPER_BADGE.get(t.get("paper","either"), PAPER_BADGE["either"])[1]}</td></tr>'
        for t in topics
    )
    body = "".join(render_topic(t, i) for i, t in enumerate(topics, 1))

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(data['title'])} &mdash; N5 Prelim Revision</title>
<link rel="stylesheet" href="style.css">
<script>
window.MathJax = {{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$']]}},svg:{{fontCache:'global'}}}};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
{NAV}
<main class="wrap">
<p class="crumb"><a href="plan.html">&larr; Back to the plan</a></p>
<h1>{data.get('icon','')} {esc(data['title'])}</h1>
<p class="lede">{esc(data.get('assessment',''))}</p>
{md_block(data.get('intro',''))}

<div class="callout">
<strong>How to revise each topic.</strong> Read the rule, cover the worked example and try it
yourself, then read the exam trap &mdash; that is where most marks are lost. Finish with the
practice questions before you move on. If you cannot do the practice without looking, the topic
is not secure yet.
</div>

<h2>Topic index</h2>
<div class="tbl-wrap"><table><thead><tr><th>Topic</th><th>Paper</th></tr></thead>
<tbody>{index_rows}</tbody></table></div>

<h2>All topics</h2>
{body}

<footer>
<p>Content aligned to the official SQA National 5 course specification for
{esc(data['title'])}. Past papers and marking instructions:
<a href="https://www.sqa.org.uk/pastpapers/">sqa.org.uk/pastpapers</a>.</p>
</footer>
</main>
</body>
</html>"""


SUBJECT_PAGES = {
    "maths": "maths.html",
    "physics": "physics.html",
    "english": "english.html",
    "bm": "business-management.html",
    "dm": "design-manufacture.html",
    "pe": "pe.html",
    "cook": "practical-cookery.html",
}


def main():
    DOCS.mkdir(exist_ok=True)
    wanted = sys.argv[1:]
    files = sorted(CONTENT.glob("*.json"))
    if wanted:
        files = [f for f in files if f.stem in wanted]
    if not files:
        print("No content files found in", CONTENT)
        return 1
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        html = render_page(data)
        fname = SUBJECT_PAGES.get(data["subject"], f"{data['subject']}.html")
        out = DOCS / fname
        out.write_text(html, encoding="utf-8")
        print(f"{out.name:28} {len(data.get('topics', [])):3} topics  {len(html):>7,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
