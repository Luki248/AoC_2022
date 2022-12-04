# Advent of Code
# Day 4
# https://adventofcode.com/2022/day/4


file = open("input.txt", "r")
input = file.readlines()

sections = []
for line in input:
    line = line.strip("\n").split(",")
    first = line[0].split("-")
    second = line[1].split("-")
    sections.append([int(first[0]), int(first[1]), int(second[0]), int(second[1])])

sum = 0
for section in sections:
    if section[0] <= section[2] and section[1] >= section[3]:
        sum += 1
    elif section[0] >= section[2] and section[1] <= section[3]:
        sum += 1

print("First Puzzle:", sum)


sum = 0
for section in sections:
    if section[0] <= section[2] and section[1] >= section[3]:
        sum += 1
    elif section[0] >= section[2] and section[1] <= section[3]:
        sum += 1
    elif section[0] <= section[2] and section[1] <= section[3] and section[1] >= section[2]:
        sum += 1
    elif section[0] >= section[2] and section[1] >= section[3] and section[0] <= section[3]:
        sum += 1

print("Second Puzzle:", sum)
