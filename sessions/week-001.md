# Week 001: Variables and Assignment — Named Boxes in Memory

> **Track:** Computer science · **Level:** National 5 beginner · **Time:** 60 minutes

## Why This Matters

Almost every program you have ever used — a game keeping your score, an app remembering your name, a robot storing how many steps it has taken — works by storing values in **variables**. A variable is simply a named box in the computer's memory that holds a value, and **assignment** is the action of putting a value into that box. If you understand variables and assignment, you understand the single most-used idea in all of programming, and it is the first thing the National 5 Computing Science course expects you to master under **Software design and development**.[1]

This session also gives you your first real tool: by the end you will have written, run, and tested a small Python program — a skill you will reuse in later tracks on AI, data, and robotics.

## Prerequisites

- No previous programming experience is needed.
- You should be comfortable with basic arithmetic (adding and multiplying small numbers).
- You need a way to run Python 3: either Python installed on your computer (free, from python.org) or any free online Python runner in your browser. The examples in this session use Python 3.

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

1. explain what a variable is and what assignment means;
2. create a variable, give it a value, and change that value with `=`;
3. predict what `score = score + 1` does, step by step;
4. name variables clearly so a human can understand the program;
5. use a trace table to check your program's logic by hand.

## Simple Explanation

### The one central idea

**A variable is a named box in the computer's memory that stores a value. Assignment is putting a value into that box.**[2][3]

The box has two parts:

- a **name** (the label on the box), and
- a **value** (what is inside the box right now).

```
┌──────────────┐
│  score       │  ← name (identifier)
│     = 0      │
│    ┌─────┐   │
│    │  0  │   │  ← value stored in memory
│    └─────┘   │
└──────────────┘
```

The word "variable" means the value can **change** as the program runs. The box stays the same; the contents get swapped.

### Assignment with `=`

In Python, you put a value into a variable with a single equals sign:[3]

```python
score = 0
```

Read this as **"store the value 0 in the box called score"** — not as "score equals 0". The `=` symbol here means **assignment**, which is different from "is equal to". This is the most common beginner confusion in programming.[3]

### The mystery of `score = score + 1`

This line confuses everyone the first time. It is read in two steps:

1. Work out the **right side** first: look inside `score`, add 1.
2. Store the **result** into the box on the left: `score`.

So if `score` held 0 before the line, after the line it holds 1. The box is like a counter being ticked up by one. In the SQA reference language the same assignment is written `SET score TO score + 1`.[2]

### Three things to know about data types

Every value stored in a variable has a **data type** — the kind of value it is.[3] National 5 beginners need three:

| Data type | Kind of value | Example |
|---|---|---|
| **Integer** | whole numbers | `7`, `-3`, `0` |
| **Float** | numbers with a decimal point | `3.5`, `9.99` |
| **String** | text, always in quotes | `"Sam"`, `"Hello"` |

Some languages make you state the type when you declare the variable, as in the SQA reference language: `DECLARE score AS INTEGER INITIALLY 0`.[2] Python sets the type automatically from the value you assign, so you just write `score = 0` and Python knows `score` holds an integer.[3]

### Give variables meaningful names

Name boxes by **what they mean**, not by what letter they start with. `score` is a great name; `s` is a mystery.[2] Rules to remember:

- no spaces in names — use `total_score` or `score1`;
- start with a letter (or underscore);
- use a name that says what the value means.

### The trace table: your by-hand checker

A **trace table** is a table where you run a program one line at a time with a pencil and record what each variable holds after each line. Programmers use trace tables to find logic errors, and National 5 exams ask for them. You will make one in the practice activity.

## Worked Examples

### Example 1: A score that increases

```python
score = 0
score = score + 3
score = score + 2
print(score)
```

Step by step:

| Line | What happens | score now |
|---|---:|---:|
| `score = 0` | Store 0 in the box `score`. | 0 |
| `score = score + 3` | Right side: 0 + 3 = 3. Store 3 in `score`. | 3 |
| `score = score + 2` | Right side: 3 + 2 = 5. Store 5 in `score`. | 5 |
| `print(score)` | Display what is inside `score`. | 5 |

**Output: `5`**

This is exactly how a game adds points to your score.

### Example 2: Two variables and a swap

```python
first = 2
second = 5
temp = first
first = second
second = temp
print(first, second)
```

| Line | What happens | first | second | temp |
|---|---:|---:|---:|---:|
| `first = 2` | Store 2. | 2 | — | — |
| `second = 5` | Store 5. | 2 | 5 | — |
| `temp = first` | Copy 2 into `temp`. | 2 | 5 | 2 |
| `first = second` | Copy 5 into `first`. | 5 | 5 | 2 |
| `second = temp` | Copy 2 into `second`. | 5 | 2 | 2 |

**Output: `5 2`**

The swap works because `temp` holds the old value while `first` is being overwritten. Without `temp`, one value would be lost.

### Example 3: Strings and a friendly message

```python
player = "Sam"
level = 4
print("Player:", player)
print("Level:", level)
```

**Output:**

```
Player: Sam
Level: 4
```

Notice the string `"Sam"` is in quotes, while the integer `4` is not. `print()` can show both, side by side.

### A common error worth knowing

Using a variable you have never assigned a value to gives a `NameError` — Python does not know which box you mean.[3] For example:

```python
print(total)
```

before any `total = ...` line gives:

```
NameError: name 'total' is not defined
```

The fix is to assign a value to `total` before you use it.

## Practice Activity

### Build a pocket-money tracker (15 minutes)

You will write a small program that tracks how much pocket money you save each week, using variables and assignment. **Your evidence is the working program, its output, and a completed trace table.**

**Step 1 — On paper, before any code:** complete this trace table for the program below. Run it line by line with a pencil.

```python
saved = 0
weekly = 5
saved = saved + weekly
saved = saved + weekly
print(saved)
```

| Line | What happens | saved | weekly |
|---|---|---:|---:|
| `saved = 0` | Store 0. | 0 | — |
| `weekly = 5` | Store 5. | 0 | 5 |
| `saved = saved + weekly` | Right side: 0 + 5 = 5. | 5 | 5 |
| `saved = saved + weekly` | Right side: 5 + 5 = 10. | 10 | 5 |
| `print(saved)` | Display 10. | 10 | 5 |

**Step 2 — In Python:** type the program in, run it, and confirm the output is `10`, matching your trace table. If it does not, find the line where your trace and the program disagree.

**Step 3 — Extend it (the fun part):** change the program so it saves pocket money for **four** weeks instead of two, and adds a string variable `name = "Sam"` that is printed first. Expected final output:

```
Sam
20
```

Run it and keep a note of what you changed and the new output.

**Checklist before you move on:**

- [ ] Trace table complete and matches the program's output (10).
- [ ] Program runs with no errors.
- [ ] Extended version prints `Sam` then `20`.

If all three boxes are ticked, you have written, run, and verified your first real program. Save your code and trace table — this is your first portfolio-style artifact.

## Quiz

1. What is a variable?
2. In Python, what does `score = score + 1` do?
3. Which of these is a string: `5` or `"5"`? Explain why.
4. Why is `s` a worse variable name than `score`?
5. A program has `total = 10`, then later `total = total + 3`. What is `total` at the end?

## Answers

1. A variable is a named box in the computer's memory that stores a value. The value can change as the program runs.[2]
2. It looks inside `score`, adds 1, and stores the result back into `score` — like ticking a counter up by one.[2][3]
3. `"5"` is a string because it is in quotes; `5` is an integer (a whole number). Quotes are what make text a string.[3]
4. `s` does not say what the value means, so a reader (or you, next week) cannot guess its purpose. `score` is meaningful and relevant.[2]
5. `total` starts at 10, then 10 + 3 = 13, so `total` is **13**.

## Reflection and Next Step

- **One-sentence takeaway:** A variable is a named box in memory, and assignment (`=`) puts a new value into that box.
- **What did you find difficult?** The `score = score + 1` line is the most common struggle — did reading the right side first make sense to you?
- **Confidence:** give yourself a score from 1 (not yet) to 5 (I could teach it).
- **What this unlocks:** variables and assignment are the foundation for **selection** (`if` statements) and **iteration** (loops) — the next big computational constructs in National 5. Every later track in this lab, from AI to robotics, will use variables on the very first day.

## Optional Video or Book

Watch the **BBC Bitesize video "What are variables?"** (1 minute 25 seconds), which shows variables as "a special box where computers keep useful information" using the example of a squirrel keeping track of where its nuts are buried. It is a friendly, quick visual for the exact idea in this session:

- https://www.bbc.co.uk/bitesize/topics/zkcqn39/watch/zgbw7ty

If you prefer reading, the **BBC Bitesize "Variables" revision page** (listed in the sources below) explains the National 5 reference-language version of everything in this session.

## Sources and Further Learning

These sources were fetched and read while writing this session:

1. **National 5 Computing Science — Course overview and resources — Qualifications Scotland** (official awarding body; note that on 1 February 2026 Qualifications Scotland replaced SQA as Scotland's national awarding body, and the documents on this page remain current). This page confirms that Software design and development — which includes variables and assignment — is part of the National 5 Computing Science course, and links to the course specification and reference language.
   https://www.sqa.org.uk/sqa/56923.html

2. **Variables — Implementation: Computational constructs — BBC Bitesize National 5 Computing Science**. This is the National 5 revision guide for variables: how a variable names a storage location in RAM, how to declare it (including `DECLARE score AS INTEGER INITIALLY 0`), how assignment changes the stored value (`SET score TO score + 1`), and why meaningful names matter.
   https://www.bbc.co.uk/bitesize/guides/z8dbtv4/revision/1

3. **3. An Informal Introduction to Python — Python 3.14.7 documentation** (official Python documentation). This is the official tutorial for the Python side: "The equal sign (=) is used to assign a value to a variable", examples of using variables as a calculator, and the `NameError` you get when a variable has not been defined.
   https://docs.python.org/3/tutorial/introduction.html

Optional video (verified to exist on the run date): **"What are variables?" — BBC Bitesize Computing science video playlist** (1:25).
https://www.bbc.co.uk/bitesize/topics/zkcqn39/watch/zgbw7ty

## Sources

[1] https://www.sqa.org.uk/sqa/56923.html — National 5 Computing Science - Course overview and resources - Qualifications Scotland
    > "On 1 February 2026, Qualifications Scotland replaced SQA and became Scotland’s new national awarding body. The documents on this page remain current and you can continue to use them."
[2] https://www.bbc.co.uk/bitesize/guides/z8dbtv4/revision/1 — Variables - Implementation: Computational constructs - BBC Bitesize National 5 Computing Science
    > "Variables are used to identify storage locations in RAM (main memory) that will store the values used by a program."
    > "When variables are declared they are usually given an initial value, like the value 0 in the example above. It is also possible to assign values to variables when a program is running."
    > "It is important to give variables meaningful and relevant names so that we can understand and remember their purpose."
    > "The code above is an example of assignment. The programmer has assigned a new value to the score variable. In this case, they have added 1 onto the score. As the score started at 0 it would now be 1. The value in memory would change from 0 to 1."
[3] https://docs.python.org/3/tutorial/introduction.html — 3. An Informal Introduction to Python - Python 3.14.7 documentation
    > "The equal sign (=) is used to assign a value to a variable."
    > "If a variable is not “defined” (assigned a value), trying to use it will give you an error:"
