# 📘 National 5 Learning Lab

A weekly, beginner-friendly learning journey for an S4 high-school student. Every session focuses on **one concept**, takes about **one hour**, and builds knowledge through explanations, solved problems, experiments, coding, simulations, or small projects.

## Weekly schedule

- **New session:** Saturday at 12:00 PM, Europe/London time
- **Publication:** committed to the `sessions/` folder in this repository
- **Reminder:** delivered to Sam on Telegram with the lesson link
- **Level:** approximately National 5, with advanced topics introduced gently and only after prerequisites

## The nine learning tracks

1. Mathematical reasoning
2. Physics and aerospace
3. Computer science
4. AI and data
5. Robotics and control
6. Product engineering
7. Business building
8. Communication and leadership
9. Portfolio challenges

See [CURRICULUM.md](CURRICULUM.md) for the full topic map and selection rules.

## What each session contains

Every weekly lesson includes:

- a 60-minute plan;
- 3–5 clear learning goals;
- a simple explanation with limited jargon;
- worked examples;
- one meaningful practice activity;
- a short quiz and answer key;
- optional video/book/further-learning resources;
- at least two checked sources, including an official or primary source;
- a link to how the concept connects to later study, engineering, business, or a portfolio project.

## Repository structure

```text
national-5-learning-lab/
├── README.md
├── CURRICULUM.md
├── SESSION_TEMPLATE.md
├── curriculum-ledger.json
├── progress.md
├── sessions/
│   └── week-001.md
├── scripts/
│   └── validate_session.py
└── tests/
    └── test_validate_session.py
```

## How to use a lesson

1. Open the newest file in `sessions/`.
2. Follow the lesson in order; do not rush the worked examples.
3. Complete the activity yourself before reading the quiz answers.
4. Mark your status in [progress.md](progress.md).
5. Save project work or reflections in your own folder or repository.

## Quality rules

A lesson is not published unless it:

- introduces a unique `concept_id`;
- passes `python3 scripts/validate_session.py --week N`;
- cites every source recorded in `curriculum-ledger.json`;
- has exactly one progress row;
- is committed, pushed, and verified on GitHub.

## Safety

Use simulations or low-risk household activities by default. Do not attempt mains electricity, pressure vessels, flames, dangerous chemicals, flight hardware, or power tools without qualified adult supervision. Never paste secrets or API keys into lessons, code, or Git.

## Licence

MIT — free to learn from, share, and adapt.
