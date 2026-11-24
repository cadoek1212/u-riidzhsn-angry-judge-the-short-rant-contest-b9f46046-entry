#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — v1.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt. Deterministic: same output on every run, stdlib only,
no network.
"""

import os

RANT = (
    "Self-checkout just screamed \"UNEXPECTED ITEM IN BAGGING AREA\" at me. "
    "I haven't moved. I haven't touched a thing. "
    "It watched me put that bag down five seconds ago, "
    "and now it glares at me like I smuggled in a watermelon. "
    "The attendant sighs like I'm the problem. "
    "I am a hostage of a machine that cannot count to one bag."
)


def main() -> None:
    text = RANT
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    assert text.strip(), "rant must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
