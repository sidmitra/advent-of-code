import string
import re
from math import prod
import sys
from enum import StrEnum, auto
from typing import TypedDict
from collections import defaultdict



def default_map():
    d = {}
    # for i in range(0, 99):
    #     d[i] = i
    return d

"seeds -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location"
s2s = default_map()
s2f = default_map()
f2w = default_map()
w2l = default_map()
l2t= default_map()
t2h= default_map()
h2loc= default_map()


def first(content):
    sections = content.split("\n\n")
    sections[0]
    for section in sections:
        s = section.strip()
        print(s)
        print("-")
    # for y, line in enumerate(lines):
    #     print(line)


def second(lines):
    pass


# python main.py input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        content = infile.read()

    first(content)
    # second(lines)
