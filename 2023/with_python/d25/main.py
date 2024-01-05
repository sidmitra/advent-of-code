import sys


def first(lines):
    print(lines)



# python main.py input.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.read().splitlines()

    first(lines)

    # second(lines)
