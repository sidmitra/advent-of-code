import sys


# python main.py input.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.readlines()
    lines = strip_newlines(lines)

    first(lines)

    # second(lines)
