"""One-Line Laugh-Off entry.

Writes exactly one original joke to /output/entry.txt.
"""

import os

JOKE = "I told my GPS to avoid tolls; it routed me through my childhood trauma instead."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the competition gate: 1-200 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
