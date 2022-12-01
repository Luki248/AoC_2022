# Advent of Code
# Day 1
# https://adventofcode.com/2022/day/1


file = open("input.txt", "r")
input = file.readlines()

calories = []
sum = 0
for line in input:
    if line == "\n":
        calories.append(sum)
        sum = 0
    else:
        sum += int(line.rstrip("\n"))

calories.sort()

print("First Puzzle:", calories[-1])


print("Second Puzzle:", calories[-1] + calories[-2] + calories[-3])
