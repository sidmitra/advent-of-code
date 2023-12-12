import string
import re
from math import prod
import sys
from enum import StrEnum, auto
from typing import TypedDict
from collections import defaultdict


def first(lines):
    total = 0
    for y, line in enumerate(lines):
      print(line)


def second(lines):
    pass


# python main.py input1.txt
# python main.py input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.readlines()

    first(lines)
    # second(lines)
