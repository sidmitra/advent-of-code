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
       points = 0

       card_num, num_s = line.strip().split(":")
       card_num = int(card_num.replace("Card ", "").strip())
       winning_s, have_s = num_s.split("|")
       winning = [x.strip() for x in winning_s.split(" ") if x.strip() != ""]
       have = [x.strip() for x in have_s.split(" ") if x.strip() != ""]

       for n in have:
           if n in winning:
               if points == 0:
                   points = 1
               else:
                   points = points * 2
       # print(card_num, winning, have, points)
       total += points
    print("points: ", total)


def second(lines):
    d = {}
    num_lines = len(lines)
    for i in range(1, num_lines+1):
        d[i] = 1

    for y, line in enumerate(lines):
        # Parse
        card_num, num_s = line.strip().split(":")
        card_num = int(card_num.replace("Card ", "").strip())
        winning_s, have_s = num_s.split("|")
        winning = [x.strip() for x in winning_s.split(" ") if x.strip() != ""]
        have = [x.strip() for x in have_s.split(" ") if x.strip() != ""]

        matching = len(
            set(have).intersection(set(winning))
        )
        #print(card_num, f"{matching=}")
        #print("before:", d.items())
        for i in range(1, matching+1):
            # check out of range
            if card_num+i <= num_lines:
                d[card_num+i]  =  (d[card_num+i] + d[card_num])  #d[card_num] # TODO:
            # print("++", y+i, "=",d[y+i])

        #print("after:", d.items())
        #print("===")

       # print(d.items())
    print("total scratchcards: ", sum(d.values()))


# python main.py input1.txt
# python main.py input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.readlines()

    first(lines)
    second(lines)
