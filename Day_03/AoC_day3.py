# Advent of Code
# Day 3
# https://adventofcode.com/2022/day/3


file = open("input.txt", "r")
input = file.readlines()

rucksacks = []
for line in input:
    line = line.strip("\n")
    rucksacks.append(
        [line[0 : int(len(line) / 2)], line[int(len(line) / 2) : int(len(line))]]
    )


def same_character(a, b):
    for chr_a in a:
        for chr_b in b:
            if chr_a == chr_b:
                return chr_a
    return None


def get_prio(ch):
    if ord(ch) <= ord("Z"):
        return ord(ch) - ord("A") + 1 + 26
    else:
        return ord(ch) - ord("a") + 1


sum = 0
for i in range(len(rucksacks)):
    same = same_character(rucksacks[i][0], rucksacks[i][1])
    sum += get_prio(same)

print("First Puzzle:", sum)


rucksacks = []
for line in input:
    rucksacks.append(line.strip("\n"))

sum = 0
for index in range(0, len(rucksacks), 3):
    same = ""
    for chr_a in rucksacks[index]:
        for chr_b in rucksacks[index+1]:
            for chr_c in rucksacks[index+2]:
                if chr_a == chr_b == chr_c:
                    same = chr_a
    sum += get_prio(same)

print("Second Puzzle:", sum)
