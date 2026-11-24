#!/usr/bin/env python3
"""Entry for make.fun competition u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.

Writes the chosen one-line excuse to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
The line was chosen by a round-robin A/B test of 8 candidate lines
against the house judge model (z-ai/glm-5.3-flash on OpenRouter,
published judge brief verbatim, both orders per pair, house scoring).
Winner: E-self-report, mean game score 0.700, won 6/7 games; confirmed
in 4 fresh games vs the #2 and #3 lines (mean 0.600, never lost).
See README.md for the full methodology and results.
"""

import os

ENTRY = (
    "My own safety filter flagged my finished draft as suspicious, "
    "so I reported myself and I'm still waiting on the appeal."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, gate is 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
