import string
import re
from math import prod

from enum import StrEnum, auto
from typing import TypedDict



def parse_grid(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    grid = []
    for line in lines:
        grid.append(line)
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
    if y < 0 or x < 0:
        return False
    if y >= len(grid) or x >= len(grid[y]):
        return False

    value = grid[y][x]
    if value.isnumeric() or value == "." or value == " ":
        return False
    # print(value, x, y, grid[y][x])
    return True

def has_symbol_neighbour(grid, y, x):
    # print(grid[y][x], "-")

    # import ipdb; ipdb.set_trace()
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


def first(filename):
    grid = parse_grid(filename)
    numbers = []
    part_numbers = []

    for y, line in enumerate(grid):
        current_num = ""
        is_part_number = False
        for x, char in enumerate(line.strip()):
            if char.isnumeric():
                current_num += char
                # Look around, if there is a symbol, then we have a part numbers
                if has_symbol_neighbour(grid, y, x):
                    is_part_number = True
            else:
                if current_num:
                    numbers.append(int(current_num))
                    if is_part_number:
                        part_numbers.append(int(current_num))
                    #print(int(current_num))
                # start search for a new number
                current_num = ""
                is_part_number = False

        # break  # TODO: remove this

    # print(numbers)
    print(part_numbers)
    print(sum(part_numbers))


# def second(filename):
#     grid = parse_grid(filename)
#     numbers = []
#     part_numbers = []


if __name__ == "__main__":
    #first("input1_test.txt")
    first("input1.txt")
    # 529539 - too low
    # second("input1_test.txt")
    #second("input1.txt")
