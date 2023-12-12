import sys



def first(lines):
    pass



def second(lines):
    pass


# python main.py input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.readlines()

    first(lines)
    # second(lines)
