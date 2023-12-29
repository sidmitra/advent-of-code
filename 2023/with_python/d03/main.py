import sys
import string
import re
from math import prod

from enum import StrEnum, auto
from typing import TypedDict



def strip_newlines(lines):
    """
    Return array of arrays
    """
    grid = []
    for line in lines:
        grid.append(line.strip())
    return grid

"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def is_symbol(grid, y, x):
    # Check for bounds
    if y < 0 or x < 0:
        return False
    if y >= len(grid) or x >= len(grid[y]):
        return False

    value = grid[y][x]
    if value.isnumeric() or value == ".":
        return False
    return True

def has_symbol_neighbour(grid, y, x):
    up = is_symbol(grid, y-1, x)
    down = is_symbol(grid, y+1, x)
    left = is_symbol(grid, y, x-1)
    right = is_symbol(grid, y, x+1)
    left_top_diag = is_symbol(grid, y-1, x-1)
    right_top_diag = is_symbol(grid, y-1, x+1)
    right_bottom_diag = is_symbol(grid, y+1, x-1)
    left_bottom_diag = is_symbol(grid, y+1, x+1)
    has_symbol = up or down or left or right or left_top_diag or right_top_diag or right_bottom_diag or left_bottom_diag
    # print(has_symbol, "|", up, down, left, right, left_top_diag, right_top_diag, right_bottom_diag, left_bottom_diag)
    return has_symbol


def first(lines):
    numbers = []
    part_numbers = []

    for y, row in enumerate(lines):
        current_num = ""
        is_part_number = False
        width = len(row)
        for x, char in enumerate(row):
            if char.isnumeric():
                current_num += char
                # Look around, if there is a symbol, then we have a part numbers
                if has_symbol_neighbour(lines, y, x):
                    is_part_number = True
                # If the row ends with a number, ensure we add it to parts
                # F*CK: This took a long time to figure out, had to look up hints on reddit
                if x == width-1:
                    numbers.append(int(current_num))
                    if is_part_number:
                        part_numbers.append(int(current_num))
                    current_num = ""
                    is_part_number = False

            else:
                if current_num:
                    numbers.append(int(current_num))
                    if is_part_number:
                        part_numbers.append(int(current_num))


                # start search for a new number
                current_num = ""
                is_part_number = False

        # break  # TODO: remove this

    # print(numbers)
    # print(part_numbers)
    print(sum((part_numbers)))


# --------
def has_two_part_numbers(lines, x, y):
    part_numbers = [] # only for current line

    current_line = lines[y]
    # ------ left
    ix = x
    current_num = ""
    for ix in range(x-1, -1, -1):
        if ch:= current_line[ix]:
            if ch.isnumeric():
                current_num += ch
            else:
                break
    if current_num:
        current_num = int(current_num[::-1]) # reverse
        part_numbers.append(current_num)
        # print(current_num, "=", current_line)
    # print(part_numbers)
    # ------ left


    # ------ right
    current_num = ""
    for ix in range(x+1, len(current_line), 1):
        if ch:= current_line[ix]:
            if ch.isnumeric():
                current_num += ch
            else:
                break
    if current_num:
        current_num = int(current_num)
        part_numbers.append(current_num)
        # print(current_num, "=", current_line)
    # ------ right


    # ------ up
    if y > 0:
        line_above = lines[y-1]

        right_num = ""
        for ix in range(x+1, len(line_above), 1):
            if ch:= line_above[ix]:
                if ch.isnumeric():
                    right_num += ch
                else:
                    break

        left_num = ""
        for ix in range(x-1, -1, -1):
            if ch:= line_above[ix]:
                if ch.isnumeric():
                    left_num += ch
                else:
                    break

        combined = left_num[::-1] + line_above[x] + right_num
        combined = [el for el in combined.strip(".").split(".") if el]
        if combined:
            combined = [int(x) for x in combined]
            part_numbers.extend(combined)
    # ------ up


    # ------- down
    if y < len(lines)-1:
        line_below = lines[y+1]

        right_num = ""
        for ix in range(x+1, len(line_below), 1):
            if ch:= line_below[ix]:
                if ch.isnumeric():
                    right_num += ch
                else:
                    break

        left_num = ""
        for ix in range(x-1, -1, -1):
            if ch:= line_below[ix]:
                if ch.isnumeric():
                    left_num += ch
                else:
                    break

        combined = left_num[::-1] + line_below[x] + right_num
        combined = [el for el in combined.strip(".").split(".") if el]
        if combined:
            combined = [int(x) for x in combined]
            part_numbers.extend(combined)
    # -------- down


    print(part_numbers)
    if len(part_numbers) == 2:
        return prod(part_numbers)
    return None



def second(lines):
    """
    A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.
    """
    gear_ratios = []
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "*":
                if gear_ratio := has_two_part_numbers(lines, x, y):
                    gear_ratios.append(gear_ratio)

    print("Done.")
    #print(gear_ratios)
    print(sum(gear_ratios))


# python main.py input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.readlines()
    lines = strip_newlines(lines)

    #first(lines)
    # 529539 - too low
    # 332836 - incorrect

    second(lines)
