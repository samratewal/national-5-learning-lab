# Week 002: Solving Linear Equations — Undoing Operations Step by Step

> **Track:** Mathematical reasoning · **Level:** National 5 beginner · **Time:** 60 minutes

## Why This Matters

An **equation** is a mathematical sentence that says two things are equal, like `3x + 5 = 20`. **Solving** it means finding the mystery number — the **unknown**, called `x` here — that makes the sentence true. This is one of the most-used skills in all of mathematics and engineering: engineers solve equations to work out forces on a bridge, app developers solve them to figure out costs and prices, and physicists solve and rearrange them constantly. At National 5, algebra is worth roughly **30–45% of the marks** in the exam, and "Working with linear equations and inequations" is one of the assessed algebraic skills in the course specification.[1]

Last week you met **variables** — named boxes in a computer's memory that store values. This week the same idea appears in maths: a letter stands for a number, but this time you must *find* the number. Once you can solve a linear equation, you can rearrange physics formulas, turn word problems into equations, and later tackle simultaneous and quadratic equations.

## Prerequisites

- You can do arithmetic with negative numbers (for example `-3 + 5 = 2` and `-2 × 3 = -6`).
- You know from Week 1 that a letter (like `x`) stands for a value — here it stands for a number we do not know yet.
- You can multiply and divide small numbers.
- A calculator is not needed for the core lesson; you may use one to check your answers.

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

1. explain what an equation is and what "solving" it means;
2. undo `+`, `-`, `×` and `÷` with their **inverse operations**;
3. keep an equation balanced by doing the same thing to **both sides**;
4. solve a linear equation even when the unknown appears on both sides;
5. check your answer by substituting it back into the original equation.

## Simple Explanation

### The one central idea

**An equation is a balance scale that is level.** The left side and the right side weigh exactly the same. The unknown is a mystery weight on the scale, and your job is to find its value.

```
   ┌────────────┐        ┌────────────┐
   │  3x + 5    │        │    20      │
   └────────────┘        └────────────┘
      left pan              right pan
         └──────────┬──────────┘
                    │  level: both sides
                    │  weigh the same
```

The golden rule of equations:[3]

> **Whatever you do to one side, you must do to the other side.**

If you add a 2 kg weight to the left pan only, the scale tips over. Add the same weight to *both* pans and it stays level. Numbers work the same way: you may add, subtract, multiply, or divide — but only if you do it to **both sides**.[3]

### Inverse operations: the undo button

Every operation has an **inverse** — the operation that undoes it:[3]

| Operation | Inverse | Example |
|---|---|---|
| `+ 5` | `- 5` | `x + 5 = 12` → `x = 7` |
| `- 3` | `+ 3` | `x - 3 = 10` → `x = 13` |
| `× 4` | `÷ 4` | `4x = 20` → `x = 5` |
| `÷ 2` | `× 2` | `x ÷ 2 = 6` → `x = 12` |

The BBC Bitesize National 5 guide sums it up in one memorable rule: **change side, change operation** — when a term moves across the equals sign, `+` becomes `-` and `×` becomes `÷`.[2] That shortcut is really the golden rule in disguise: "moving a term across" is just doing the inverse operation to both sides and writing the result in one short step.[2]

### The order of undoing

To solve `3x + 5 = 20`, first think about what happened to `x` on the left side:

1. start with `x`;
2. multiply by 3 → `3x`;
3. add 5 → `3x + 5`.

To undo, go **backwards through that list**:

1. undo `+ 5` first: subtract 5 from both sides → `3x = 15`;
2. undo `× 3` next: divide both sides by 3 → `x = 5`.

Undo in reverse order — like taking off your coat before the jumper underneath it. That is why two-step equations always deal with the added or subtracted number first, and the multiplier second.[3]

### Linear means "no squares"

A **linear** equation has the unknown only to the power 1: `x`, never `x²`.[3] `2x + 7 = 13` is linear; `x² = 9` is not. Linear equations always have exactly one answer, which makes them the friendliest equations to solve.

## Worked Examples

### Example 1: One step

Solve `x + 5 = 12`.

| Step | Working | Why |
|---|---|---|
| 1 | `x + 5 - 5 = 12 - 5` | Subtract 5 from **both sides** to undo `+ 5` |
| 2 | `x = 7` | Simplify |

**Check:** put 7 back in: `7 + 5 = 12` ✓

### Example 2: Two steps (reverse order)

Solve `3x + 4 = 19`.

| Step | Working | Why |
|---|---|---|
| 1 | `3x + 4 - 4 = 19 - 4` | Undo `+ 4` first (reverse order) |
| 2 | `3x = 15` | Simplify |
| 3 | `3x ÷ 3 = 15 ÷ 3` | Now undo `× 3`: divide both sides |
| 4 | `x = 5` | Simplify |

**Check:** `3(5) + 4 = 15 + 4 = 19` ✓

### Example 3: Unknown on both sides

Solve `2x + 7 = 5x - 2`.

| Step | Working | Why |
|---|---|---|
| 1 | `2x + 7 - 2x = 5x - 2 - 2x` | Subtract `2x` from both sides so all unknowns sit on the left |
| 2 | `7 = 3x - 2` | Simplify: `2x - 2x = 0`, `5x - 2x = 3x` |
| 3 | `7 + 2 = 3x - 2 + 2` | Add 2 to both sides to undo `- 2` |
| 4 | `9 = 3x` | Simplify |
| 5 | `9 ÷ 3 = 3x ÷ 3` | Divide both sides by 3 |
| 6 | `x = 3` | Simplify |

**Check:** left side `2(3) + 7 = 13`; right side `5(3) - 2 = 13` ✓ — both sides match, so the scale is level.

### Example 4: Unknown with a minus sign (BBC style)

Solve `35 = 5 - 6m`.[2]

| Step | Working | Why |
|---|---|---|
| 1 | `35 + 6m = 5 - 6m + 6m` | Add `6m` to both sides so `m` is no longer stuck behind a minus sign |
| 2 | `35 + 6m = 5` | Simplify |
| 3 | `35 + 6m - 35 = 5 - 35` | Subtract 35 from both sides |
| 4 | `6m = -30` | Simplify |
| 5 | `6m ÷ 6 = -30 ÷ 6` | Divide both sides by 6 |
| 6 | `m = -5` | Simplify |

**Check:** `5 - 6(-5) = 5 + 30 = 35` ✓

**Note:** the BBC guide writes step 1 as "move the `-6m` over to the left hand side, changing it to `+6m`" — that is exactly the same as adding `6m` to both sides, just written in a shorter way.[2]

## Practice Activity

### The Mystery Number Mission (15 minutes)

Solve each equation on paper (or in a text file), writing down every step. **Your evidence: six fully-worked solutions with checks, plus the Python output.**

1. `x - 8 = 3`
2. `3x + 1 = 10`
3. `5x - 2 = 3x + 8`
4. `4 - 3x = 13`
5. `2x + 5 = 4` — challenge: the answer is a fraction. That is perfectly fine at National 5.[3]
6. **Word problem:** "I think of a number, double it, then subtract 3. The result is 11." Let the mystery number be `n`. Write the equation, then solve it.

**Step 2 — Check every answer by substitution:** for each equation, put your answer back in and confirm both sides match. If a side does not match, find the step where you went wrong — do not just change the answer.

**Step 3 — Check the word problem with Python (from Week 1!):** type this program in and run it. It uses variables and assignment, exactly like last week:

```python
n = 7
result = 2 * n - 3
print("2n - 3 =", result)   # expected output: 2n - 3 = 11
```

If it prints `2n - 3 = 11`, your `n` is right.

**Answers (check only after you are done):** 1) 11  2) 3  3) 5  4) -3  5) -1/2  6) 7

**Checklist before you move on:**

- [ ] All six problems solved with every step written down.
- [ ] Each answer substituted back and confirmed on both sides.
- [ ] Python program prints `2n - 3 = 11`.

## Quiz

1. What does it mean to "solve" the equation `3x + 5 = 20`?
2. What is the inverse of `× 4`? What is the inverse of `+ 3`?
3. Solve `x - 7 = 2`.
4. Solve `3x + 1 = 10`.
5. Solve `2x + 3 = x + 8`.

## Answers

1. Find the value of `x` that makes both sides equal — the mystery number that balances the scale (here `x = 5`).
2. `÷ 4` undoes `× 4`; `- 3` undoes `+ 3`.[3]
3. Add 7 to both sides: `x = 9`. Check: `9 - 7 = 2` ✓
4. Subtract 1 from both sides, then divide by 3: `3x = 9`, so `x = 3`. Check: `3(3) + 1 = 10` ✓
5. Subtract `x` from both sides: `x + 3 = 8`, so `x = 5`. Check: `2(5) + 3 = 13` and `5 + 8 = 13` ✓

## Reflection and Next Step

- **One-sentence takeaway:** An equation is a balanced scale, and solving it means undoing operations — with the same move on both sides — until the unknown stands alone.
- **What did you find difficult?** The most common struggle is choosing the *order* of steps. Remember: undo in reverse order, and always do the same thing to both sides.
- **Confidence:** score yourself from 1 (not yet) to 5 (I could teach it).
- **What this unlocks:** solving equations is the engine behind **changing the subject of a formula** (turning `v = d ÷ t` into `t = d ÷ v`), **simultaneous equations**, and later **quadratic equations**. In the physics track you will solve equations every week, and in coding you can write programs that solve them for you.

## Optional Video or Book

Watch **"The Whole Of Solving Equations In National 5 Maths"** by Clelland Maths (verified to exist on YouTube, about 20 minutes). Watch the first 10 minutes, which cover one-step and two-step equations; pause before each example and try it yourself first:
- https://www.youtube.com/watch?v=Nw6MwxfxLak

For reading, the **BBC Bitesize National 5 guide "Solving equations and inequations"** (source [2] below) is the revision page for everything in this session — it works through the same `35 = 5 - 6m` example with the "change side, change operation" rule.

## Sources and Further Learning

These sources were fetched and read while writing this session:

1. **National 5 Mathematics Course Specification, version 3.0 (May 2023) — Scottish Qualifications Authority** (official awarding body). The official course document: it lists "Working with linear equations and inequations" under Algebraic skills (with rational-number coefficients and rational-number solutions) and states that approximately 30–45% of the marks in the question papers relate to algebra.
   https://www.sqa.org.uk/sqa/files_ccc/n5-course-spec-mathematics.pdf

2. **Solving equations and inequations — Working with linear equations and inequations — BBC Bitesize National 5 Maths** (National 5 revision guide). Teaches the "change side, change operation" rule and works through `-2 - 3y = 11` and `35 = 5 - 6m` → `m = -5`.
   https://www.bbc.co.uk/bitesize/guides/zwgdb82/revision/1

3. **Linear Equations — National 5 Maths — Free Resources (Maths.scot)** (free N5 revision website). Key ideas: linear means the unknown appears to the power 1, equations are solved using inverse operations, the same operation must be applied to both sides, and solutions may be fractions.
   https://maths.scot/nat5/linear-equations
## Sources

[1] https://www.sqa.org.uk/sqa/files_ccc/n5-course-spec-mathematics.pdf — National 5 Mathematics Course Specification (version 3.0, May 2023) — Scottish Qualifications Authority
    > "Where numerical coefficients are rational numbers"
    > "Where numerical solutions are rational numbers"
    > "Approximately 30-45% of the overall marks relate to algebra."
[2] https://www.bbc.co.uk/bitesize/guides/zwgdb82/revision/1 — Solving equations and inequations — Working with linear equations and inequations — BBC Bitesize National 5 Maths
    > "Change side, change operation"
    > "Move the -2 over to the right hand side changes it to +2"
[3] https://maths.scot/nat5/linear-equations — Linear Equations — National 5 Maths — Free Resources (Maths.scot)
    > "We use inverse operations to solve equations."
    > "We must always perform the same operation to both sides of the equation."
