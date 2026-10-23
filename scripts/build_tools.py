#!/usr/bin/env python3
"""Generate flashcards.html and quizzes.html from the topic content.

Flashcards: every topic produces a concept card (topic -> key rule) and a
question card (practice question -> full answer). Flip to reveal.

Quizzes: a self-marking multiple-choice quiz per subject, drawn from the topic
titles and rules, with instant scoring so weak areas are obvious.

Both are plain HTML+JS, no build step, no external dependencies.
"""
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONTENT = ROOT / "content"

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


def load():
    out = []
    for f in sorted(CONTENT.glob("*.json")):
        if f.name.startswith("_"):
            continue
        out.append(json.loads(f.read_text(encoding="utf-8")))
    return out


def head(title):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} &mdash; N5 Prelim Revision</title>
<link rel="stylesheet" href="style.css">
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}},svg:{{fontCache:'global'}}}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
<style>
.fcgrid{{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));margin:18px 0}}
.fc{{perspective:1000px;height:190px;cursor:pointer}}
.fcin{{position:relative;width:100%;height:100%;transition:transform .55s;transform-style:preserve-3d}}
.fc.on .fcin{{transform:rotateY(180deg)}}
.fcf,.fcb{{position:absolute;inset:0;backface-visibility:hidden;border-radius:13px;padding:16px 18px;
overflow:auto;border:1px solid var(--line);font-size:14px;line-height:1.5}}
.fcf{{background:var(--panel);display:flex;flex-direction:column;justify-content:center}}
.fcb{{background:#15251c;border-color:#2b4a37;transform:rotateY(180deg)}}
.fcl{{font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--dim);
font-weight:800;margin-bottom:8px}}
.fcb .fcl{{color:var(--acc2)}}
.fchint{{position:absolute;bottom:9px;right:12px;font-size:10.5px;color:var(--dim)}}
.qbox{{background:var(--panel);border:1px solid var(--line);border-radius:13px;padding:20px;margin:16px 0}}
.opt{{display:block;width:100%;text-align:left;margin:8px 0;padding:12px 15px;border-radius:10px;
background:var(--panel2);border:1px solid var(--line);color:var(--ink);font-size:14.5px;cursor:pointer;
font-family:inherit;transition:.12s}}
.opt:hover{{border-color:var(--acc);background:var(--chip)}}
.opt.right{{background:#1d3325;border-color:#3f7a55;color:#b7f0c8}}
.opt.wrong{{background:#331d20;border-color:#7a3f45;color:#f0b7b7}}
.score{{font-size:15px;font-weight:700;margin-top:14px}}
</style>
</head>
<body>
{NAV}
<main class="wrap">"""


def build_flashcards(data):
    cards = []
    for d in data:
        icon = d.get("icon", "")
        for t in d["topics"]:
            rule = t.get("rule", "").strip()
            first = rule.split("\n")[0][:420]
            cards.append((f'{icon} {t["title"]}',
                          f'<div class="fcl">Key rule</div>{esc(first)}'))
            for p in t.get("practice", [])[:1]:
                cards.append((f'{icon} {t["title"]}',
                              f'<div class="fcl">Question</div>{esc(p["q"])}',
                              f'<div class="fcl">Answer</div>{esc(p["a"])}'))

    html = [head("Flashcards")]
    html.append("<h1>🃏 Flashcards</h1>")
    html.append(f'<p class="lede">{len(cards)} cards across all 7 subjects. '
                "Click a card to flip it. Say the answer out loud before you flip — "
                "recognising an answer is not the same as recalling it.</p>")
    html.append('<div class="fcgrid">')
    LBL_ANSWER = '<div class="fcl">Answer</div>'
    for c in cards:
        if len(c) == 3:
            subject, front, back = c
            back = back.replace(LBL_ANSWER, "")
        else:
            subject, front = c[0], c[1]
            back = "<em>See the topic page for the full rule.</em>"
        onclk = "this.classList.toggle('on')"
        html.append(
            '<div class="fc" onclick="' + onclk + '">'
            '<div class="fcin">'
            '<div class="fcf"><div class="fcl">' + esc(subject) + '</div>'
            '<div>' + front + '</div><div class="fchint">tap to flip</div></div>'
            '<div class="fcb"><div class="fcl">Answer</div><div>' + back + '</div></div>'
            '</div></div>')
    html.append("</div>")
    html.append("<footer><p><a href='plan.html'>Back to the plan</a></p></footer></main></body></html>")
    return "\n".join(html)


def build_quizzes(data, per_subject=8):
    """Self-marking MCQ built from topic titles vs. the other subjects' topics."""
    blocks, total = [], 0
    for d in data:
        icon, name = d.get("icon", ""), d["title"]
        titles = [t["title"] for t in d["topics"]]
        qs = []
        rng = random.Random(42 + len(name))
        for t in d["topics"]:
            distractors = [x for x in titles if x != t["title"]]
            if len(distractors) < 3:
                continue
            wrong = rng.sample(distractors, 3)
            opts = wrong + [t["title"]]
            rng.shuffle(opts)
            rule = t.get("rule", "").strip().split("\n")[0][:260]
            qs.append((rule, t["title"], opts))
            if len(qs) >= per_subject:
                break
        if not qs:
            continue
        total += len(qs)
        blocks.append(f'<h2>{icon} {esc(name)}</h2><div class="qbox">')
        for i, (rule, ans, opts) in enumerate(qs, 1):
            blocks.append(f'<p><strong>{i}.</strong> Which topic is this the rule for?<br>'
                          f'<span style="color:var(--dim);font-size:14px">{esc(rule)}</span></p>')
            for o in opts:
                cls = "right" if o == ans else ""
                blocks.append(f'<button class="opt" data-ok="{1 if o==ans else 0}" '
                              f'onclick="pick(this)">{esc(o)}</button>')
            blocks.append('<hr style="margin:14px 0">')
        blocks.append('</div>')

    js = """
let score=0, asked=0;
function pick(btn){
  const box=btn.parentElement;
  if(box.dataset.done) return;
  box.dataset.done=1; asked++;
  box.querySelectorAll('.opt').forEach(b=>{ if(b.dataset.ok==='1') b.classList.add('right'); });
  if(btn.dataset.ok==='1'){ score++; } else { btn.classList.add('wrong'); }
  const s=document.getElementById('score');
  if(s) s.textContent='Score: '+score+' / '+asked;
}
"""
    html = [head("Quizzes")]
    html.append("<h1>✅ Topic quizzes</h1>")
    html.append(f'<p class="lede">{total} questions. Read the rule, pick the topic it belongs to. '
                "Instant marking — every wrong answer is a topic to revisit.</p>")
    html.append('<p class="score" id="score">Score: 0 / 0</p>')
    html.extend(blocks)
    html.append(f"<script>{js}</script>")
    html.append("<footer><p><a href='plan.html'>Back to the plan</a></p></footer></main></body></html>")
    return "\n".join(html)


def main():
    data = load()
    (DOCS / "flashcards.html").write_text(build_flashcards(data), encoding="utf-8")
    (DOCS / "quizzes.html").write_text(build_quizzes(data), encoding="utf-8")
    print("flashcards.html and quizzes.html written")


if __name__ == "__main__":
    main()
