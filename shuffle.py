# Shuffle the paragraphs separated by empty lines in a text file.
# Usage: python shuffle.py <filename>

import sys
import random
import os


def shuffle(filename):
    if not os.path.isfile(filename):
        print("Input file not found.", file=sys.stderr)
        sys.exit(1)
    with open(filename, "r") as f:
        paragraphs = f.read().split("\n\n")
        random.shuffle(paragraphs)
        print("\n\n".join(paragraphs))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python shuffle.py <filename>", file=sys.stderr)
        sys.exit(1)
    shuffle(sys.argv[1])
