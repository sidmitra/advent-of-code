import string
import re


def first(filename):
    lines = open(filename, 'r').readlines()

    calibrations = []
    for line in lines:
        value = re.sub(r"[a-zA-Z]", r"", line).strip()
        value = f"{value[0]}{value[-1]}"
        # print(value, "->", line)
        calibrations.append(int(value))
    print(sum(calibrations))


mapper = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",

    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def second(filename):
    lines = open(filename, 'r').readlines()

    calibrations = []
    for line in lines:
        value = line
        for k, v in mapper.items():
            value = value.replace(k, str(v))
        #    if line.strip() == "eightwothree":
        #        print(value, "-", line)

        value = re.sub(r"[a-zA-Z]", r"", value).strip()
        value = f"{value[0]}{value[-1]}"
        print(value, "->", line)
        calibrations.append(int(value))
    print(sum(calibrations))



if __name__ == "__main__":
    # first("input1.txt")
    # second("input2_test.txt")
    #second("input2_test2.txt")
    second("input2.txt")
