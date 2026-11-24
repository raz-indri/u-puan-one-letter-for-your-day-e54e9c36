"""One Letter for Your Day.

Writes exactly one letter to the output file: H.

H stands for Hope -- the one word worth carrying into any day.
Whatever today holds, hope is the quiet decision to begin anyway:
to open the curtains, take the first small step, and trust that
even this ordinary day can still turn toward something good.
"""

import os

LETTER = "H"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
