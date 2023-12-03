import string
import re
from math import prod

from enum import StrEnum, auto
from typing import TypedDict


class Color(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE  = auto()

class Hand(TypedDict):
    color: Color
    count: int

max_counts = {
    Color.RED: 12,
    Color.GREEN: 13,
    Color.BLUE: 14,
}


def is_game_possible(game_id, game):
    turns = game.strip().split(";")
    hands = []
    for turn in turns:
        for h in turn.strip().split(","):
            hands.append(
                Hand(
                    color=h.strip().split(" ")[1],
                    count=int(h.strip().split(" ")[0])
                )
            )

    for hand in hands:
        # print(hand)
        if hand["count"] > max_counts[hand["color"]]:
            color = hand["color"]
            count = hand["count"]
            # print(count, max_counts[color], color, "|", game)
            return False
    return True


def first(filename):
    lines = open(filename, 'r').readlines()

    possibilities = []
    for line in lines:
        game_id, game = line.split(":")
        game_id = int(game_id.replace("Game ", "").strip(""))

        if is_game_possible(game_id, game):
            possibilities.append(game_id)
        else:
            pass
            #print(f"{game_id}: {game}")

    # print(possibilities)
    print(sum(possibilities))


def power_of_min_set(game_id, game):
    turns = game.strip().split(";")
    hands = []

    mins = {}
    mins[Color.RED] = None
    mins[Color.GREEN] = None
    mins[Color.BLUE] = None

    for turn in turns:
        for h in turn.strip().split(","):
            hands.append(
                Hand(
                    color=h.strip().split(" ")[1],
                    count=int(h.strip().split(" ")[0])
                )
            )

    for hand in hands:
        count = hand["count"]
        color = hand["color"]
        if mins[color] is None or count > mins[color]:
            mins[color] = count
    # print(game_id, mins.values(), "| ", game)
    # print(power)
    power = prod(mins.values())
    return power


def second(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()

    powers = []
    for line in lines:
        game_id, game = line.split(":")
        game_id = int(game_id.replace("Game ", "").strip(""))
        power = power_of_min_set(game_id, game)
        powers.append(power)

    print(sum(powers))




if __name__ == "__main__":
    #first("input1_test.txt")
    first("input1.txt")

    # second("input1_test.txt")
    second("input1.txt")
