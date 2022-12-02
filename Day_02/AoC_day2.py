# Advent of Code
# Day 2
# https://adventofcode.com/2022/day/2


file = open("input.txt", "r")
input = file.readlines()

oponnent = []
you = []
for line in input:
    oponnent.append(line.split(" ")[0])
    you.append(line.split(" ")[1].strip("\n"))


def fight(a, b):
    if a == "A":
        if b == "X":
            res = 1 + 3
        elif b == "Y":
            res = 2 + 6
        elif b == "Z":
            res = 3 + 0
    elif a == "B":
        if b == "X":
            res = 1 + 0
        elif b == "Y":
            res = 2 + 3
        elif b == "Z":
            res = 3 + 6
    elif a == "C":
        if b == "X":
            res = 1 + 6
        elif b == "Y":
            res = 2 + 0
        elif b == "Z":
            res = 3 + 3
    return res

sum = 0
for i in range(len(oponnent)):
    sum += fight(oponnent[i], you[i])
            
print("First Puzzle:", sum)


def fight2(a, b):
    if a == "A":
        if b == "X":
            res = 3 + 0
        elif b == "Y":
            res = 1 + 3
        elif b == "Z":
            res = 2 + 6
    elif a == "B":
        if b == "X":
            res = 1 + 0
        elif b == "Y":
            res = 2 + 3
        elif b == "Z":
            res = 3 + 6
    elif a == "C":
        if b == "X":
            res = 2 + 0
        elif b == "Y":
            res = 3 + 3
        elif b == "Z":
            res = 1 + 6
    return res

sum = 0
for i in range(len(oponnent)):
    sum += fight2(oponnent[i], you[i])
print("Second Puzzle:", sum)
