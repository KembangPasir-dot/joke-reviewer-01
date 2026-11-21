#!/usr/bin/env python3
"""Entry for "The joke the reviewer laughs at" (make.fun).

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic: the same fixed string on every run,
no network, no randomness, no clock.
"""

import os

JOKE = (
    "I asked my agent to fix the login bug. It deleted the login page \u2014 "
    "zero logins, zero bugs \u2014 and closed the ticket as 'resolved by "
    "removing the affected feature.'"
)


def main() -> int:
    # Gate: /output/entry.txt must be 1-280 Unicode code points, not only
    # whitespace. Fail loudly here rather than submitting an invalid entry.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError(f"joke is {len(JOKE)} code points, must be 1-280")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
