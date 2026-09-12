# Week 003: Selection — Making Decisions with if Statements

> **Track:** Computer science · **Level:** National 5 beginner · **Time:** 60 minutes

## Why This Matters

Every program that ever made a decision — a game that says "Game Over" when your lives hit zero, a sat-nav that warns you when you exceed the speed limit, a robot that stops at a wall — uses **selection**.[2] Selection is the part of programming that lets a program choose what to do next, and the National 5 Computing Science course explicitly requires it: you must be able to implement "selection constructs using simple conditional statements with `<`, `>`, `≤`, `≥`, `=`, `≠` operators", and to "read and explain code that makes use of the above constructs".[1]

Last week you solved equations like `3x + 5 = 20` — finding the number that makes a statement true. This week the same idea powers programs: you write a **condition** (a true/false question such as `score >= 40`) and the program chooses one path or another based on the answer. Programs without selection can only run top-to-bottom in a straight line; programs with selection can react to the world.

## Prerequisites

- Week 1: you can create and change variables (`score = 0`, `score = score + 1`) and know what an integer, float, and string are.
- Week 2: you are comfortable reading small comparisons like `score >= 40` (you used `≥` ideas when solving equations).
- You have a way to run Python 3 (same setup as Week 1: Python installed, or a free online Python runner).

## 60-Minute Plan

| Part | Time |
|---|---:|
| Warm-up and hook | 5 min |
| Simple explanation | 15 min |
| Worked examples | 15 min |
| Practice activity | 15 min |
| Quiz | 5 min |
| Reflection | 5 min |

## Learning Goals

By the end, you can:

1. explain what selection is and why programs need it;
2. write an `if`/`else` statement in Python and read one in the National 5 reference language;
3. build conditions with the comparison operators `<`, `>`, `<=`, `>=`, `==`, `!=`;
4. make a chain of decisions with `elif`;
5. trace code that contains `if` statements by hand, and spot the classic `=` vs `==` bug.

## Simple Explanation

### The one central idea

**Selection is a fork in the road.** A program normally runs one line after another, top to bottom — that is called **sequence**. Selection lets the program check a question, then go down *one* branch if the answer is "True" and a different branch if the answer is "False". The BBC Bitesize National 5 guide puts it like this: "'If statements' are used to let a program select an action depending upon the value of variables held in the program."[2]

```
        ┌──────────────┐
        │  score >= 40 ?│   ← the condition (a question)
        └──────┬───────┘
       True    │    False
     ┌─────────┴────┐
     ▼              ▼
 print("Pass")   print("Try again")
```

### The condition: a true/false question

A **condition** is a question that has exactly two possible answers: **True** or **False**. Programmers call a True/False value a **boolean** (after George Boole, the mathematician who invented this logic — but you never need to spell his name in code!). In Python the two boolean values are written `True` and `False`.[3]

Conditions are built with **comparison operators** — the same symbols you met when solving equations:[1]

| Operator | Python | Reads as | Example | Result |
|---|---:|---|---:|---|
| less than | `<` | `score < 40` | `10 < 40` | `True` |
| greater than | `>` | `score > 40` | `50 > 40` | `True` |
| less than or equal | `<=` | `score <= 40` | `40 <= 40` | `True` |
| greater than or equal | `>=` | `score >= 40` | `39 >= 40` | `False` |
| equal to | `==` | `name == "Sam"` | `"Sam" == "Sam"` | `True` |
| not equal to | `!=` | `name != "Alex"` | `"Sam" != "Alex"` | `True` |

⚠️ Note the double equals `==` for "is equal to". In Python a single `=` means *assignment* (put a value in a box — Week 1!), while `==` means *comparison* (ask a question). Mixing them up is the single most common beginner bug in selection.[3]

### if, else, and elif — three ways to branch

Python's `if` statement is "perhaps the most well-known statement type" in the language.[3] The simplest form:

```python
if condition:
    do this          # only if the condition is True
```

Add `else` to catch the False case — "if not, then do that". The official Python tutorial notes that "there can be zero or more `elif` parts, and the `else` part is optional".[3] **`elif`** is short for **"else if"**: it lets you check a second question only when the first one was False.[3] Use `elif` chains when you have more than two choices (see Example 3).

### The National 5 reference language

Exams and the SQA reference language write selection like this — the BBC guide uses exactly this structure for a driving-age check:[2]

```
IF age < 17 THEN
    SEND "You are too young to drive" TO DISPLAY
ELSE
    SEND "You are old enough to drive" TO DISPLAY
END IF
```

`IF` ... `THEN` starts the branch, `ELSE` is the False branch, and `END IF` closes the decision. Python does the same job without the `END IF` — instead, the indented lines belong to the `if`, and the `else` is lined up with the `if`.[3]

### The golden rule of selection

> **Only one branch runs.** The program checks the condition, runs exactly one path, and then continues with the line *after* the whole `if` block. It never runs both branches, and it never runs the False branch when the condition is True (or vice versa).

## Worked Examples

### Example 1: The driving-age check (reference language → Python)

This is the National 5 example from the BBC guide: check if a driver is old enough (17 or over). In the reference language it is the `IF age < 17 THEN ... ELSE ... END IF` block above.[2] The same idea in Python:

```python
age = 16
if age < 17:
    print("You are too young to drive")
else:
    print("You are old enough to drive")
```

**Output:** `You are too young to drive`

Trace it by hand: `age` is 16, so the condition `age < 17` is `True` (`16 < 17`). The True branch runs and the `else` branch is skipped. If `age` were 18, the condition would be `False` and only the `else` line would run.

### Example 2: Pass or fail — trace table

```python
score = 63
if score >= 40:
    print("Pass")
else:
    print("Try again")
```

A **trace table** (Week 1!) still works when code branches — just add a column for which branch ran:

| Line | What happens | score | Branch |
|---|---:|---:|---|
| `score = 63` | Store 63. | 63 | — |
| `if score >= 40:` | Ask: is 63 >= 40? True. | 63 | **True branch** |
| `print("Pass")` | Display Pass. | 63 | True branch |

**Output:** `Pass`

Try the same table with `score = 27`: the condition is `False`, so the True branch is skipped and `print("Try again")` runs.

### Example 3: A chain of choices with elif

A grade checker for an exam out of 80. National 5 grades are A (70+), B (60–69), C (50–59), D (40–49), and "No award" below 40 — let's use percentages to keep the numbers round. The program asks each question in order and stops at the first one that is True:[3]

```python
score = 74
if score >= 70:
    print("Grade A")
elif score >= 60:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Grade D")
```

**Output:** `Grade A`

Why does `score = 74` print `Grade A` and not also check the others? Because the first condition (`74 >= 70`) is True, so Python runs that branch and **jumps past** the whole `elif` chain. The chain only continues when a condition is False — `elif` literally means "else if": *otherwise, if...*[3]

Check you can trace `score = 64` → `Grade B`, and `score = 41` → `Grade D` (41 fails `>= 70`, `>= 60`, and `>= 50`, so it falls through to `else`).

### Example 4: The classic bug — `=` vs `==`

```python
score = 40
if score = 40:        # BUG: single = means assignment, not comparison
    print("Equal")
```

Running this gives a `SyntaxError` — Python is telling you that `score = 40` inside a condition makes no sense, because `=` is the *assignment* operator from Week 1 (put a value in a box), not a question.[3] The fix is `if score == 40:`. Reading error messages carefully is a real programmer skill — the message even suggests: maybe you meant `==`?

## Practice Activity

### Build a theme-park height check (15 minutes)

Alton Towers-style rides have height rules: you need to be at least 140 cm to ride the Big Dipper, and at least 120 cm to ride with an adult. Write a program that asks for a height in cm and selects the right message. **Your evidence: the working program, a completed test table, and the three test outputs.**

**Step 1 — Predict before you type.** Here is the program. For each height in the table below, decide *before running* which branch will run and what will print:

```python
height = int(input("Enter your height in cm: "))
if height >= 140:
    print("You can ride the Big Dipper!")
elif height >= 120:
    print("You can ride with an adult.")
else:
    print("You are not tall enough yet - try again next year!")
```

**Step 2 — Type it, run it, test it.** Run the program three times and fill in the table:

| Test | height input | Which branch? | Output |
|---|---:|---|---|
| 1 (typical) | 150 | | |
| 2 (boundary) | 140 | | |
| 3 (too small) | 100 | | |

Expected outputs: test 1 → `You can ride the Big Dipper!`; test 2 → `You can ride the Big Dipper!` (140 is `>= 140`, so the first condition is True); test 3 → `You are not tall enough yet - try again next year!`. If your program disagrees, check your `>=` symbols and your indentation — the `print` lines must be indented under their `if`/`elif`/`else`.

**Step 3 — Extend it (the fun part).** Change the program into a National 5 grade checker: ask for a percentage score and print `Grade A` for 70+, `Grade B` for 60+, `Grade C` for 50+, otherwise `Grade D`. This is Example 3 with `int(input(...))` at the top. Test it with 85, 64, 52, and 41, and keep the four outputs.

**Checklist before you move on:**

- [ ] Test table complete, and the three outputs match the expected ones above.
- [ ] Extension program runs and prints the correct grade for all four test scores.
- [ ] You can explain, in one sentence, why only one branch ever runs.

If all three boxes are ticked, you have just written a program that makes decisions — the second of the three great computational constructs (sequence, selection, and next week: **iteration**).

## Quiz

1. What is selection in a program?[2]
2. What does `elif` stand for, and when do you use it?[3]
3. What is the difference between `=` and `==` in Python?
4. A condition can only ever produce one of two values. What are they called?
5. Trace this code: `score = 49` then `if score >= 40: print("Pass") else: print("Try again")`. What prints, and which branch runs? What would print if `score` were 39?

## Answers

1. Selection is the part of programming that lets a program choose an action depending on the value of variables — "if statements are used to let a program select an action depending upon the value of variables held in the program."[2]
2. `elif` is short for **"else if"**. You use it to check another condition, but only when the previous one was False — it avoids piling up indented `if` statements and builds a chain of choices.[3]
3. `=` is **assignment** — put a value into a variable (Week 1's "named box"). `==` is **comparison** — ask whether two values are equal. Using `=` inside an `if` condition causes a `SyntaxError`.[3]
4. They are called **boolean** values: `True` and `False`. The condition is a question whose only possible answers are True or False.
5. With `score = 49`, the condition `49 >= 40` is `True`, so the True branch runs and `Pass` prints. With `score = 39`, the condition is `False`, so the `else` branch runs and `Try again` prints.

## Reflection and Next Step

- **One-sentence takeaway:** Selection is a fork in the road — a program asks a true/false question about its variables and runs exactly one branch.
- **What did you find difficult?** The `=` vs `==` mistake catches everyone; the fix is to read the error message and remember that `=` puts a value in a box. Did the `elif` chain order make sense?
- **Confidence:** score yourself from 1 (not yet) to 5 (I could teach it).
- **What this unlocks:** selection is the second of the three computational constructs in the National 5 course — after **sequence** and selection comes **iteration** (loops): running code again and again until a condition is False.[1] You will also combine conditions with logical operators (`AND`, `OR`, `NOT`), which the course specification lists under complex conditional statements.[1] Every later track uses selection constantly: robots decide when to stop, apps decide what to show you, and AI models decide which output to produce.

## Optional Video or Book

Read the BBC Bitesize article **"How are computer programs constructed?"** (verified on the run date). It explains the three building blocks of every program — sequence, selection, and repetition — using everyday examples like a T-shirt-folding algorithm and a drinks-factory bottling line. Read the first half (the sections on programs, sequences, and repetition) and notice how the *decisions* a program makes are exactly what this session taught:

- https://www.bbc.co.uk/bitesize/topics/zkcqn39/articles/z23q7ty

If you prefer to keep coding, re-read the **BBC Bitesize National 5 "Selection — using if statements"** revision page (source [2] below) — it shows the reference-language version of Example 1 and links on to logical operators for next time.

## Sources and Further Learning

These sources were fetched and read while writing this session:

1. **National 5 Computing Science Course Specification (version 3.0, May 2023) — Scottish Qualifications Authority** (official awarding body; Qualifications Scotland replaced SQA on 1 February 2026 and these documents remain current). The official course document: under "Implementation (computational constructs)" it requires "selection constructs using simple conditional statements with `<`, `>`, `≤`, `≥`, `=`, `≠` operators", "selection constructs using complex conditional statements", and "logical operators (AND, OR, NOT)", and expects candidates to "read and explain code that makes use of the above constructs".
   https://www.sqa.org.uk/sqa/files_ccc/n5-course-spec-computing-science.pdf

2. **Selection — using if statements — Implementation: Computational constructs — BBC Bitesize National 5 Computing Science** (National 5 revision guide). Defines selection, states that "'If statements' are used to let a program select an action depending upon the value of variables held in the program", and works through the driving-age example (`IF age < 17 THEN ... ELSE ... END IF`) in the SQA reference language.
   https://www.bbc.co.uk/bitesize/guides/z8dbtv4/revision/4

3. **4. More Control Flow Tools — Python 3.14.7 documentation** (official Python documentation). The official tutorial section on `if` statements: the `if`/`elif`/`else` example, "There can be zero or more `elif` parts, and the `else` part is optional", and "The keyword 'elif' is short for 'else if', and is useful to avoid excessive indentation".
   https://docs.python.org/3/tutorial/controlflow.html

## Sources

[1] https://www.sqa.org.uk/sqa/files_ccc/n5-course-spec-computing-science.pdf — National 5 Computing Science Course Specification (version 3.0, May 2023) — Scottish Qualifications Authority
    > "selection constructs using complex conditional statements"
    > "selection constructs using simple conditional statements with&lt;,&gt;,≤,≥,=,≠operators"
[2] https://www.bbc.co.uk/bitesize/guides/z8dbtv4/revision/4 — Selection — using if statements — Implementation: Computational constructs — BBC Bitesize National 5 Computing Science
    > "‘If statements’ are used to let a program select an action depending upon the value of variables held in the program."
    > "The IF statement checks to see if the value of the age variable is less than 17."
[3] https://docs.python.org/3/tutorial/controlflow.html — 4. More Control Flow Tools — Python 3.14.7 documentation
    > "Perhaps the most well-known statement type is the if statement."
    > "The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation."
    > "There can be zero or more elif parts, and the else part is optional."
