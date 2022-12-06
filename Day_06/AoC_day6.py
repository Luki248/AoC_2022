# Advent of Code
# Day 6
# https://adventofcode.com/2022/day/6


file = open("input.txt", "r")
input = file.readlines()[0]


def marker():
    for i in range(len(input) - 4):
        at_pos = input[i : i + 4]
        if (
            at_pos[0] != at_pos[1]
            and at_pos[0] != at_pos[2]
            and at_pos[0] != at_pos[3]
            and at_pos[1] != at_pos[2]
            and at_pos[1] != at_pos[3]
            and at_pos[2] != at_pos[3]
        ):
            return i + 4


print("First Puzzle:", marker())


def message():
    for i in range(len(input) - 14):
        at_pos = input[i : i + 14]
        is_the_same = True
        for m in range(0, len(at_pos) - 1):
            for n in range(m + 1, len(at_pos)):
                if at_pos[m] == at_pos[n]:
                    is_the_same = False
        if is_the_same:
            return i + 14


print("Second Puzzle:", message())
