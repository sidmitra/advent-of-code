import sys
from itertools import cycle

graph = {}


def first(lines):
    dirs = lines[0].strip()
    start = "AAA" # ARGGGG! "Starting at AAA,...". If you don't you're going to wait a long time
    for (line, dir) in zip(lines[2:], cycle(dirs)):
        curr, tup = line.split("=")
        # print(curr)
        curr = curr.strip()
        # Not needed anymore, since we start at AAA
        # if start is None:
        #     start = curr

        left, right = tup.split(",")
        left = left.replace("(", "")
        right = right.replace(")", "").replace("\n", "")
        graph[curr] = [left.strip(), right.strip()]

    # print(f"{dirs=}")
    # print(f"{start=}")
    # print(f"{graph=}")

    # print("=======")
    # Traverse
    now = start
    for (steps, dir) in enumerate(cycle(dirs)):
        L, R = graph[now]
        print(dir, now, L, R)
        now = L if dir == "L" else R
        if now == "ZZZ":
            # print("Found.", steps)
            break

    # 1-based ordering
    print("Steps=", steps+1)


def second(lines):
    pass


# python main.py input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.readlines()

    first(lines)
    # second(lines)
