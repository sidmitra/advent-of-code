import sys
from copy import copy, deepcopy


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print("\n")


def expand_rows(grid, rows_without_galaxies):
    for row in rows_without_galaxies:
        grid.insert(row, deepcopy(grid[row]))


def expand_cols(grid, cols_without_galaxies):
    for col in cols_without_galaxies:
        for row in grid:
            row.insert(col, ".")



def first(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    # print_grid(grid)

    rows_without_galaxies = []
    for r, row in enumerate(grid):
        if "#" not in row:
            rows_without_galaxies.append(r)
    # print(rows_without_galaxies)

    cols_without_galaxies = []
    for col in range(len(grid)):
        if all(grid[y][col]=="." for y in range(len(lines))):
            cols_without_galaxies.append(col)
    # print(cols_without_galaxies)

    # double rows
    expand_rows(grid, rows_without_galaxies)
    # print_grid(grid)

    # double cols
    expand_cols(grid, cols_without_galaxies)
    print_grid(grid)





def second(lines):
    pass


# python main.py input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.readlines()

    first(lines)
    # second(lines)
