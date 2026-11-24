"""One-star cat review: the human is a very slow doorman.

Writes exactly one line to /output/entry.txt (no trailing newline).
Python stdlib only.
"""

import os

LINE = (
    "★☆☆☆☆ I waited 40 seconds at the door while my human located his legs. "
    "I own this house; he is the doorman, and I am already interviewing his replacement."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
