#!/usr/bin/env python3
"""Single source of truth for the National 5 prelim revision plan.

Generates:
  docs/plan.html      - the week-by-week plan page
  docs/schedule.json  - machine-readable schedule (used by the daily Discord job)

Run:  python3 scripts/schedule.py [--check]
"""
import json, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# --------------------------------------------------------------------------
# Subjects
# --------------------------------------------------------------------------
SUBJECTS = {
    "maths":   dict(name="Mathematics",             page="maths.html",                cls="maths",   icon="📐"),
    "physics": dict(name="Physics",                 page="physics.html",              cls="physics", icon="⚛️"),
    "bm":      dict(name="Business Management",     page="business-management.html",  cls="bm",      icon="💼"),
    "english": dict(name="English",                 page="english.html",              cls="english", icon="📖"),
    "dm":      dict(name="Design & Manufacture",    page="design-manufacture.html",   cls="dm",      icon="🔧"),
    "cook":    dict(name="Practical Cookery",       page="cookery.html",              cls="cook",    icon="🍳"),
    "pe":      dict(name="Physical Education",      page="pe.html",                   cls="pe",      icon="🏃"),
}

# --------------------------------------------------------------------------
# Topic inventory - every examinable topic, in teaching order.
# (slug, title, anchor-title)
# --------------------------------------------------------------------------
TOPICS = {
"maths": [
 ("fractions-percentages", "Fractions & percentages"),
 ("surds-indices",         "Surds & indices"),
 ("scientific-notation",   "Scientific notation"),
 ("expanding-brackets",    "Expanding brackets"),
 ("factorising",           "Factorising"),
 ("completing-square",     "Completing the square"),
 ("algebraic-fractions",   "Algebraic fractions"),
 ("changing-subject",      "Changing the subject"),
 ("equations-inequations", "Equations & inequations"),
 ("simultaneous",          "Simultaneous equations"),
 ("straight-line",         "The straight line"),
 ("functions",             "Function notation"),
 ("quadratic-graphs",      "Quadratic graphs & equations"),
 ("pythagoras",            "Pythagoras (incl. 3D & converse)"),
 ("arcs-sectors",          "Arcs & sectors"),
 ("circle-angles",         "Circle angle properties"),
 ("similar-shapes",        "Similar shapes"),
 ("trig-bearings",         "Trigonometry & bearings"),
 ("sine-cosine-rule",      "Sine rule, cosine rule & triangle area"),
 ("vectors",               "Vectors"),
 ("volume-surface-area",   "Volume & surface area"),
 ("statistics",            "Statistics & standard deviation"),
 ("probability",           "Probability"),
 ("tolerance-bounds",      "Tolerance & bounds"),
 ("ratio-proportion",      "Ratio & proportion"),
],
"physics": [
 ("vectors-scalars",   "Vectors & scalars"),
 ("velocity-time",     "Velocity–time graphs"),
 ("acceleration",      "Acceleration"),
 ("newtons-laws",      "Newton's laws"),
 ("energy",            "Energy"),
 ("projectile",        "Projectile motion"),
 ("space-exploration", "Space exploration"),
 ("cosmology",         "Cosmology"),
 ("charge-carriers",   "Charge carriers & current"),
 ("potential-difference","Potential difference"),
 ("ohms-law",          "Ohm's law"),
 ("circuits",          "Series & parallel circuits"),
 ("electrical-power",  "Electrical power"),
 ("shc",               "Specific heat capacity"),
 ("latent-heat",       "Specific latent heat"),
 ("gas-laws",          "Gas laws & the kinetic model"),
 ("wave-parameters",   "Wave parameters & behaviour"),
 ("em-spectrum",       "The electromagnetic spectrum"),
 ("refraction",        "Refraction of light"),
 ("nuclear-radiation", "Nuclear radiation"),
 ("half-life",         "Half-life"),
 ("dosimetry",         "Dose, equivalent dose & safety"),
],
"bm": [
 ("role-of-business",  "Role of business in society"),
 ("factors-production","Factors of production"),
 ("sectors",           "Sectors of industry & economy"),
 ("stakeholders",      "Stakeholders"),
 ("environments",      "Internal & external environments"),
 ("marketing-mix",     "The marketing mix"),
 ("market-research",   "Market research"),
 ("segmentation",      "Market segmentation"),
 ("product-life-cycle","Product life cycle"),
 ("branding-promotion","Branding & promotion"),
 ("pricing-distribution","Pricing & distribution"),
 ("suppliers",         "Suppliers & supply chain"),
 ("inventory",         "Inventory management"),
 ("production-methods","Methods of production"),
 ("quality",           "Quality management"),
 ("hr-planning",       "Human resource planning"),
 ("recruitment",       "Recruitment & selection"),
 ("training",          "Training"),
 ("motivation",        "Motivation"),
 ("sources-finance",   "Sources of finance"),
 ("break-even",        "Break-even"),
 ("cash-flow",         "Cash flow forecasting"),
 ("income-statement",  "Income statement"),
 ("ratios",            "Ratio analysis"),
],
"english": [
 ("ruae-understanding", "RUAE: Understanding"),
 ("ruae-word-choice",   "RUAE: Word choice"),
 ("ruae-imagery",       "RUAE: Imagery"),
 ("ruae-structure-tone","RUAE: Sentence structure & tone"),
 ("ruae-evaluation",    "RUAE: Evaluation"),
 ("scottish-text",      "Scottish text (Critical Reading §1)"),
 ("critical-essay",     "Critical essay (Critical Reading §2)"),
 ("portfolio-creative", "Portfolio: creative writing"),
 ("portfolio-discursive","Portfolio: discursive writing"),
],
"dm": [
 ("design-process",       "The design process"),
 ("research-techniques",  "Research techniques"),
 ("specification",        "The product specification"),
 ("idea-generation",      "Idea-generation techniques"),
 ("modelling",            "Modelling"),
 ("graphics",             "Graphics in design"),
 ("function-performance", "Function & performance"),
 ("market-aesthetics",    "Market, aesthetics & ergonomics"),
 ("people-influence",     "People who influence design"),
 ("materials-woods",      "Woods & manufactured boards"),
 ("materials-metals",     "Metals & plastics"),
 ("measuring-tools",      "Measuring & marking-out tools"),
 ("hand-tools",           "Hand tools"),
 ("machine-tools",        "Machine tools"),
 ("joining",              "Joining & assembly"),
 ("finishing",            "Finishing"),
 ("commercial-manufacture","Commercial manufacture"),
 ("impact-sustainability","Impact & sustainability"),
 ("planning-evaluation",  "Planning for manufacture & evaluation"),
],
"cook": [
 ("food-prep",        "Food preparation techniques"),
 ("cookery-processes","Cookery processes"),
 ("dietary-advice",   "Current dietary advice"),
 ("ingredient-categories","Categories of ingredients"),
 ("understanding-ingredients","Understanding ingredients"),
 ("planning-meals",   "Planning meals"),
 ("cooking-finishing","Cooking & finishing dishes"),
 ("safety-hygiene",   "Safety & hygiene"),
],
"pe": [
 ("performance-skills","Performance skills"),
 ("mental-factors",   "Mental factors"),
 ("emotional-factors","Emotional factors"),
 ("social-factors",   "Social factors"),
 ("physical-factors", "Physical factors"),
 ("approaches",       "Approaches to development"),
 ("monitoring",       "Monitoring, recording & evaluating"),
 ("portfolio",        "The portfolio (60 marks)"),
],
}

# Past-paper blocks are pseudo-topics: they render as practice sessions,
# not content topics, and are excluded from coverage validation.
PAST_PAPERS = {
    "maths-past-paper-1", "maths-past-paper-2", "maths-past-paper-3",
    "maths-past-paper-4", "maths-past-paper-5",
    "physics-past-paper-1", "physics-past-paper-2",
    "physics-past-paper-3", "physics-past-paper-4",
    "english-past-paper-1", "english-past-paper-2", "english-past-paper-3",
    "ruae-past-paper", "bm-past-paper-1", "dm-past-paper-1",
}

# --------------------------------------------------------------------------
# The 45-day schedule. Each day = 2 x ~55 min blocks (+10 min break).
# (subject, [topic slugs], block label, minutes)
# --------------------------------------------------------------------------
def d(subject, slugs, label, mins):
    return dict(subject=subject, topics=slugs, label=label, mins=mins)

REVIEW = "review"

SCHEDULE = [
# ---------------- WEEK 1 ----------------
d("maths",   ["fractions-percentages","surds-indices"], "Fractions & percentages · Surds & indices", 55),
d("physics", ["vectors-scalars"], "Vectors & scalars", 55),
# day 2
d("maths",   ["scientific-notation","expanding-brackets"], "Scientific notation · Expanding brackets", 55),
d("physics", ["velocity-time"], "Velocity–time graphs", 55),
# day 3
d(REVIEW, [], "Active recall: Maths mixed set + Physics mixed set (no new content)", 55),
d("english", ["ruae-understanding"], "RUAE — Understanding questions", 55),
# day 4
d("maths",   ["factorising","completing-square"], "Factorising · Completing the square", 55),
d("physics", ["acceleration"], "Acceleration", 55),
# day 5
d("maths",   ["algebraic-fractions","changing-subject"], "Algebraic fractions · Changing the subject", 55),
d("physics", ["newtons-laws"], "Newton's laws", 55),
# day 6
d("maths",   ["equations-inequations"], "Equations & inequations", 55),
d("bm",      ["role-of-business","factors-production"], "Role of business · Factors of production", 55),
# day 7
d("physics", ["energy","projectile"], "Energy · Projectile motion", 55),
d("pe",      ["performance-skills"], "Performance skills — portfolio sheet 1", 55),

# ---------------- WEEK 2 ----------------
d("maths",   ["simultaneous","straight-line"], "Simultaneous equations · The straight line", 55),
d("english", ["ruae-word-choice"], "RUAE — Word choice", 55),
d("maths",   ["functions","quadratic-graphs"], "Function notation · Quadratic graphs & equations", 55),
d("bm",      ["sectors","stakeholders"], "Sectors · Stakeholders", 55),
d(REVIEW, [], "Active recall: Maths mixed set + Business mixed set", 55),
d("dm",      ["design-process","research-techniques"], "Design process · Research techniques", 55),
d("maths",   ["pythagoras"], "Pythagoras (incl. 3D & converse)", 55),
d("physics", ["space-exploration","cosmology"], "Space exploration · Cosmology", 55),
d("maths",   ["arcs-sectors","circle-angles"], "Arcs & sectors · Circle angle properties", 55),
d("english", ["ruae-imagery"], "RUAE — Imagery", 55),
d("dm",      ["specification","idea-generation"], "Specification · Idea generation", 55),
d("bm",      ["environments","marketing-mix"], "Environments · Marketing mix", 55),
d("cook",    ["food-prep"], "Food preparation techniques", 55),
d("pe",      ["mental-factors"], "Mental factors — portfolio sheet 2", 55),

# ---------------- WEEK 3 ----------------
d("maths",   ["similar-shapes"], "Similar shapes", 55),
d("physics", ["charge-carriers","potential-difference"], "Charge carriers · Potential difference", 55),
d("maths",   ["trig-bearings"], "Trigonometry & bearings", 55),
d("english", ["ruae-structure-tone"], "RUAE — Sentence structure & tone", 55),
d("dm",      ["modelling","graphics"], "Modelling · Graphics", 55),
d("bm",      ["market-research","segmentation"], "Market research · Segmentation", 55),
d("maths",   ["sine-cosine-rule"], "Sine rule, cosine rule & triangle area", 55),
d("physics", ["ohms-law","circuits"], "Ohm's law · Series & parallel circuits", 55),
d(REVIEW, [], "Active recall: Maths + Physics mixed set", 55),
d("cook",    ["cookery-processes"], "Cookery processes", 55),
d("maths",   ["vectors"], "Vectors", 55),
d("english", ["ruae-evaluation"], "RUAE — Evaluation", 55),
d("dm",      ["function-performance","market-aesthetics"], "Function & performance · Market, aesthetics & ergonomics", 55),
d("pe",      ["emotional-factors"], "Emotional factors — portfolio sheet 3", 55),

# ---------------- WEEK 4 ----------------
d("maths",   ["volume-surface-area"], "Volume & surface area", 55),
d("physics", ["electrical-power","shc"], "Electrical power · Specific heat capacity", 55),
d("maths",   ["statistics"], "Statistics & standard deviation", 55),
d("bm",      ["product-life-cycle","branding-promotion"], "Product life cycle · Branding & promotion", 55),
d("english", ["scottish-text"], "Scottish text — poem/short story 1", 55),
d("dm",      ["people-influence","materials-woods"], "People who influence design · Woods & boards", 55),
d("maths",   ["probability"], "Probability", 55),
d("physics", ["latent-heat","gas-laws"], "Latent heat · Gas laws", 55),
d("cook",    ["dietary-advice","ingredient-categories"], "Dietary advice · Ingredient categories", 55),
d("maths",   ["tolerance-bounds","ratio-proportion"], "Tolerance & bounds · Ratio & proportion", 55),
d("english", ["critical-essay"], "Critical essay — planning & structure", 55),
d("bm",      ["pricing-distribution","suppliers"], "Pricing & distribution · Suppliers", 55),
d("dm",      ["materials-metals","measuring-tools"], "Metals & plastics · Measuring tools", 55),
d("pe",      ["social-factors"], "Social factors — portfolio sheet 4", 55),

# ---------------- WEEK 5 ----------------
d("physics", ["wave-parameters","em-spectrum"], "Wave parameters · EM spectrum", 55),
d("english", ["portfolio-creative"], "Portfolio — creative writing draft", 55),
d("maths",   ["maths-past-paper-1"], "Maths past paper: non-calculator, Paper 1", 55),
d("bm",      ["inventory","production-methods"], "Inventory · Methods of production", 55),
d("dm",      ["hand-tools","machine-tools"], "Hand tools · Machine tools", 55),
d("physics", ["refraction"], "Refraction of light", 55),
d("english", ["portfolio-discursive"], "Portfolio — discursive writing draft", 55),
d("maths",   ["maths-past-paper-2"], "Maths past paper: calculator, Paper 2", 55),
d("cook",    ["understanding-ingredients"], "Understanding ingredients", 55),
d("bm",      ["quality","hr-planning"], "Quality · HR planning", 55),
d("dm",      ["joining","finishing"], "Joining & assembly · Finishing", 55),
d("physics", ["nuclear-radiation","half-life"], "Nuclear radiation · Half-life", 55),
d("pe",      ["physical-factors"], "Physical factors — portfolio sheet 5", 55),
d("english", ["ruae-past-paper"], "RUAE past paper under timed conditions", 55),

# ---------------- WEEK 6 ----------------
d("maths",   ["maths-past-paper-3"], "Maths past paper: non-calculator, timed", 55),
d("physics", ["dosimetry","physics-past-paper-1"], "Dosimetry · Physics past paper (Dynamics)", 55),
d("bm",      ["recruitment","training","motivation"], "Recruitment · Training · Motivation", 55),
d("cook",    ["planning-meals","cooking-finishing"], "Planning meals · Cooking & finishing", 55),
d("dm",      ["commercial-manufacture","impact-sustainability"], "Commercial manufacture · Impact", 55),
d("english", ["english-past-paper-1"], "Critical Reading past paper — Scottish text", 55),
d("physics", ["physics-past-paper-4"], "Physics past paper: full paper, timed", 55),
d("physics", ["physics-past-paper-2"], "Physics past paper (Electricity & Matter)", 55),
d("bm",      ["sources-finance","break-even"], "Sources of finance · Break-even", 55),
d("dm",      ["planning-evaluation"], "Planning for manufacture & evaluation", 55),
d("cook",    ["safety-hygiene"], "Safety & hygiene", 55),
d("pe",      ["approaches","monitoring"], "Approaches to development · Monitoring", 55),
d("english", ["english-past-paper-2"], "Critical Reading past paper — critical essay", 55),
d("maths",   ["maths-past-paper-4"], "Maths past paper: calculator, timed", 55),

# ---------------- WEEK 7 (taper) ----------------
d("bm",      ["cash-flow","income-statement","ratios"], "Cash flow · Income statement · Ratios", 55),
d("bm",      ["bm-past-paper-1"], "Business Management past paper — Section 1", 55),
d("physics", ["physics-past-paper-3"], "Physics past paper (Waves, Radiation, Space)", 55),
d("dm",      ["dm-past-paper-1"], "Design & Manufacture past paper — full QP", 55),
d("english", ["english-past-paper-3"], "English: full Critical Reading under time", 55),
d("pe",      ["portfolio"], "PE portfolio — final check against mark scheme", 55),
]

# --------------------------------------------------------------------------
# Day/date scaffolding
# --------------------------------------------------------------------------
START = datetime.date(2026, 10, 23)   # Friday
DAYS = len(SCHEDULE) // 2             # 45


def build_days():
    days = []
    for i in range(DAYS):
        date = START + datetime.timedelta(days=i)
        blocks = SCHEDULE[i * 2: i * 2 + 2]
        days.append(dict(n=i + 1, date=date.isoformat(),
                         weekday=date.strftime("%a"), pretty=date.strftime("%d %b"),
                         blocks=blocks))
    return days


def week_of(day):
    return (day - 1) // 7 + 1


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------
def check():
    days = build_days()
    hours = {}
    unknown = []
    seen = set()
    for day in days:
        for b in day["blocks"]:
            s = b["subject"]
            if s == REVIEW:
                continue
            if s not in SUBJECTS:
                unknown.append(s)
                continue
            hours[s] = hours.get(s, 0) + b["mins"] / 60
            for t in b["topics"]:
                seen.add((s, t))

    all_topics = {(s, t[0]) for s, lst in TOPICS.items() for t in lst}
    missing = sorted(all_topics - seen)
    stale = sorted(t for t in seen - all_topics if t[1] not in PAST_PAPERS)

    total = sum(hours.values())
    print(f"Days: {len(days)}   Blocks: {len(SCHEDULE)}   Total hours: {total:.1f}")
    print("\nHours by subject:")
    for s, h in sorted(hours.items(), key=lambda x: -x[1]):
        print(f"  {SUBJECTS[s]['name']:<24} {h:5.1f} h")
    if unknown:
        print("\n!! Unknown subjects:", sorted(set(unknown)))
    if missing:
        print("\n!! Topics never scheduled:")
        for s, t in missing:
            print(f"   {s}/{t}")
    if stale:
        print("\n!! Scheduled topics not in TOPICS:")
        for s, t in stale:
            print(f"   {s}/{t}")
    if not (unknown or missing or stale):
        print("\nOK - every topic scheduled, no unknown slugs.")
    return days


# --------------------------------------------------------------------------
# HTML rendering
# --------------------------------------------------------------------------
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def anchor(slug):
    return f"{SUBJECTS['maths']['page']}" if False else slug


def render_plan(days):
    out = []
    cur_week = 0
    for day in days:
        w = week_of(day["n"])
        if w != cur_week:
            if cur_week:
                out.append("</tbody></table></div>")
            cur_week = w
            first = day["date"]
            last = (datetime.date.fromisoformat(day["date"]) + datetime.timedelta(days=6)).isoformat()
            label = f"Week {w}"
            out.append(f'<div class="week"><div class="week-h"><h2>{label}</h2>'
                       f'<span class="meta">{esc(first)} → {esc(last)}</span></div>'
                       '<div class="tbl-wrap"><table><thead><tr>'
                       '<th>Day</th><th>Date</th><th>Session 1 — 55 min</th><th>Session 2 — 55 min</th>'
                       '</tr></thead><tbody>')
        cells = []
        for b in day["blocks"]:
            s = b["subject"]
            if s == REVIEW:
                cells.append(f'<td class="sess">🔁 {esc(b["label"])}</td>')
            else:
                meta = SUBJECTS[s]
                titles = {x[0]: x[1] for x in TOPICS[s]}
                parts = []
                for t in b["topics"]:
                    if t in PAST_PAPERS:
                        parts.append('<em>past paper</em>')
                    else:
                        parts.append(f'<a href="{meta["page"]}#{t}">{esc(titles[t])}</a>')
                links = " ".join(parts)
                cells.append(f'<td class="sess"><span class="tag" style="background:var(--chip);color:var(--dim)">'
                             f'{meta["icon"]} {esc(meta["name"])}</span><br>{links}</td>')
        while len(cells) < 2:
            cells.append('<td class="sess">—</td>')
        out.append(f'<tr><td class="date">{day["n"]}</td>'
                   f'<td class="date">{day["weekday"]} {esc(day["pretty"])}</td>'
                   + "".join(cells) + "</tr>")
    out.append("</tbody></table></div></div>")
    return "\n".join(out)


def wrap_plan(body, days):
    """Wrap the schedule table fragment in a complete styled HTML document."""
    hours = {}
    for day in days:
        for b in day["blocks"]:
            if b["subject"] != REVIEW:
                hours[b["subject"]] = hours.get(b["subject"], 0) + b.get("min", 55)
    total_h = sum(hours.values()) / 60

    cards = []
    for k, meta in SUBJECTS.items():
        mins = hours.get(k, 0)
        cards.append(
            f'<a class="card" href="{meta["page"]}">'
            f'<div class="ico">{meta["icon"]}</div>'
            f'<div class="ttl">{esc(meta["name"])}</div>'
            f'<div class="sub">{len(TOPICS[k])} topics &middot; {mins/60:.1f} h</div>'
            f'</a>'
        )

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>S4 Prelim Revision Plan &mdash; 7 Subjects</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="top"><div class="wrap">
  <a href="index.html">Home</a>
  <a href="plan.html" class="on">Plan</a>
  <a href="maths.html">Maths</a>
  <a href="physics.html">Physics</a>
  <a href="english.html">English</a>
  <a href="business-management.html">Business</a>
  <a href="design-manufacture.html">Design</a>
  <a href="pe.html">PE</a>
  <a href="practical-cookery.html">Cookery</a>
</div></nav>

<main class="wrap">
<h1>S4 Prelim Revision Plan</h1>
<p class="lede">45 days &middot; 7 subjects &middot; 2 hours every night &middot; every examinable topic</p>

<div class="callout">
<strong>How to use this.</strong> Each night is two 55-minute blocks with a 10-minute break between
them &mdash; about 2 hours total. Every topic listed links straight to its explanation, worked
example and practice questions. Work down the table in order. Tick each day off as you finish it.
</div>

<div class="stats">
  <div><b>{len(days)}</b><span>days</span></div>
  <div><b>{len(SCHEDULE)}</b><span>study blocks</span></div>
  <div><b>{total_h:.0f}</b><span>hours</span></div>
  <div><b>{sum(len(v) for v in TOPICS.values())}</b><span>topics</span></div>
</div>

<h2>Jump to a subject</h2>
<div class="cards">
{chr(10).join(cards)}
</div>

<h2>The 45-day schedule</h2>
<p class="note">Blocks marked <em>past paper</em> are timed practice under exam conditions &mdash;
no notes, no phone. Use the official SQA marking instructions to mark your own work afterwards.</p>

{body}

<footer>
  <p>Built from the official SQA course specifications. SQA past papers and marking instructions
  are free at <a href="https://www.sqa.org.uk/pastpapers/">sqa.org.uk/pastpapers</a>.</p>
</footer>
</main>
</body>
</html>"""


def main():
    days = check()
    if "--check" in sys.argv:
        return
    DOCS.mkdir(exist_ok=True)
    payload = dict(
        start=START.isoformat(),
        days=[dict(n=x["n"], date=x["date"], weekday=x["weekday"], blocks=x["blocks"]) for x in days],
        subjects={k: dict(name=v["name"], page=v["page"], icon=v["icon"]) for k, v in SUBJECTS.items()},
        topics={k: [dict(slug=t[0], title=t[1]) for t in lst] for k, lst in TOPICS.items()},
    )
    (DOCS / "schedule.json").write_text(json.dumps(payload, indent=1), encoding="utf-8")
    print(f"Wrote {DOCS/'schedule.json'}")

    page = wrap_plan(render_plan(days), days)
    (DOCS / "plan.html").write_text(page, encoding="utf-8")
    print(f"Wrote {DOCS/'plan.html'}  ({len(page):,} bytes)")


if __name__ == "__main__":
    main()
