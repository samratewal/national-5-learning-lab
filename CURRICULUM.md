# Goal-Based Weekly Curriculum

## Mission

Build strong foundations for National 5 study while gradually developing the mathematics, science, computing, engineering, business, and communication skills needed for ambitious university study, technical careers, entrepreneurship, and a strong public portfolio.

This is not a rigid exam-board syllabus. It uses National 5 as the approximate difficulty level and teaches one carefully chosen concept per week. More advanced areas—such as calculus, orbital mechanics, neural networks, or optimisation—must begin with an intuitive introduction and wait until the necessary foundations are present.

## Level and teaching rules

Every session must:

- assume the learner is in S4 and is a beginner in the selected concept;
- explain unfamiliar terms immediately and introduce no more than 3–5 important new terms;
- focus on one central idea rather than surveying an entire field;
- use familiar examples, diagrams, tables, short code, or safe simulations;
- include challenge questions without making the core lesson inaccessible;
- prefer understanding and practice over memorising definitions;
- clearly identify prerequisites and what the session unlocks next.

## Track 1 — Mathematical reasoning

**Topics:** algebra, functions, geometry, trigonometry, introductory calculus, probability, statistics, introductory linear algebra, and optimisation.

**Evidence:** solved problems, visual explanations, graphs, spreadsheets, and small simulations.

## Track 2 — Physics and aerospace

**Topics:** mechanics, energy, momentum, waves, electricity, thermodynamics, fluids, orbital mechanics, and control.

**Evidence:** calculations, safe experiments, graphs, and flight/orbit simulations.

## Track 3 — Computer science

**Topics:** programming, data structures, algorithms, debugging, testing, systems, networking, databases, and security.

**Evidence:** tested programs and short technical write-ups.

## Track 4 — AI and data

**Topics:** data literacy, machine learning, neural networks, evaluation, agents, and responsible use.

**Evidence:** small datasets, experiments, charts, and model evaluations.

## Track 5 — Robotics and control

**Topics:** electronics, sensors, actuators, feedback, estimation, embedded systems, and autonomy.

**Evidence:** simulations and safe physical prototypes where practical.

## Track 6 — Product engineering

**Topics:** web applications, APIs, user experience, deployment, reliability, and version control.

**Evidence:** working products, tests, user feedback, and deployment records.

## Track 7 — Business building

**Topics:** customer discovery, sales, pricing, unit economics, finance, operations, and strategy.

**Evidence:** interviews, offers, simple financial models, and ethical revenue experiments.

## Track 8 — Communication and leadership

**Topics:** technical writing, presentations, teamwork, ethics, and decision-making.

**Evidence:** clear reports, demos, decision logs, and retrospectives.

## Track 9 — Portfolio challenges

**Topics:** integration across several tracks.

**Evidence:** progressively harder public projects with a problem statement, plan, implementation, verification, reflection, and demonstration.

## How the next session is selected

1. Read the complete `curriculum-ledger.json` and all existing session titles/goals.
2. Reject repeated `concept_id` values or substantially repeated learning goals.
3. Choose a high-value concept whose prerequisites are already covered.
4. Prefer neglected tracks, but never rotate randomly when a prerequisite should come first.
5. Avoid more than two consecutive sessions from one track unless completing a short project sequence.
6. Schedule a portfolio challenge after approximately 6–8 foundation sessions when enough prerequisites exist.
7. Related topics are allowed only when they clearly deepen an earlier lesson and declare it in `builds_on`.

## Standard 60-minute session

| Part | Time | Purpose |
|---|---:|---|
| Warm-up and hook | 5 min | Connect to prior knowledge and introduce the question |
| Simple explanation | 15 min | Teach one central idea with diagrams or analogies |
| Worked examples | 15 min | Solve or demonstrate the idea step by step |
| Practice activity | 15 min | Learner solves, codes, experiments, simulates, or designs |
| Quiz | 5 min | Check understanding before revealing answers |
| Reflection and next step | 5 min | Record the takeaway and what this unlocks |

## Research and source policy

- Fetch and read at least two credible sources before drafting.
- Use at least one official or primary source: Education Scotland, a qualifications body, a university, government/scientific agency, standards body, official technical documentation, or original research.
- Do not cite search-result snippets or invented URLs.
- Cross-check equations, quantitative claims, safety advice, and version-specific technical instructions.
- Record each source in `curriculum-ledger.json` with title, URL, `official`, and access date.
- Include every recorded URL in the lesson's `Sources and Further Learning` section.
- For changing software or AI topics, check current official documentation on the publication date.
- If a key claim cannot be verified, do not publish the session.

## Review cycle

After every eight sessions, review track balance, learner difficulty, completed work, and quiz performance. Adapt future selection without deleting or rewriting the historical ledger.
