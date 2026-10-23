#!/usr/bin/env python3
"""Make every Sunday a practice-exam day.

Sundays become: Block 1 = sit the week's practice exam under timed conditions,
Block 2 = mark it against the scheme and list weak topics.

Any new-content topics that were sitting on a Sunday are redistributed
round-robin across that week's remaining study blocks, so nothing is lost.
Run once; it rewrites the SCHEDULE block structure in place.
"""
import re
import pathlib

P = pathlib.Path(__file__).resolve().parent / "schedule.py"
src = P.read_text(encoding="utf-8")

# 1) add TEST + the transform right after PAST_PAPERS is defined
anchor = "# --------------------------------------------------------------------------\n# The 45-day schedule."
addition = '''TEST = "test"
SUNDAY_DAYS = [3, 10, 17, 24, 31, 38, 45]
WEEK_OF_TEST = {3: 1, 10: 2, 17: 3, 24: 4, 31: 5, 38: 6, 45: 7}


def apply_sunday_tests(schedule):
    """Return a new schedule where each Sunday is a test day.

    Topics found on a Sunday are spread across that week's other blocks so the
    full topic inventory is still covered.
    """
    sched = [dict(b) for b in schedule]
    for day in SUNDAY_DAYS:
        i = (day - 1) * 2
        week = WEEK_OF_TEST[day]
        week_days = [d for d in range((week - 1) * 7 + 1, week * 7 + 1) if d not in SUNDAY_DAYS]

        # harvest topics that would otherwise be lost
        orphans = []
        for blk in sched[i:i + 2]:
            if blk["subject"] in (REVIEW, TEST):
                continue
            keep = [t for t in blk["topics"]]
            if keep and not all(t in PAST_PAPERS for t in keep):
                orphans.extend([t for t in keep if t not in PAST_PAPERS])

        # round-robin them into the week's other blocks
        slots = [(d - 1) * 2 + k for d in week_days for k in (0, 1)]
        for n, topic in enumerate(orphans):
            target = sched[slots[n % len(slots)]]
            if topic not in target["topics"]:
                target["topics"].append(topic)

        # Sunday becomes the test day
        sched[i] = dict(subject=TEST, topics=[], label=f"Sit the Week {week} practice exam — timed", mins=55)
        sched[i + 1] = dict(subject=TEST, topics=[], label=f"Mark the Week {week} test and list what to revise", mins=55)
    return sched


# --------------------------------------------------------------------------
# The 45-day schedule.'''

assert anchor in src
src = src.replace(anchor, addition, 1)
P.write_text(src, encoding="utf-8")
print("added TEST + apply_sunday_tests()")
