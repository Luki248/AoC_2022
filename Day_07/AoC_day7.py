# Advent of Code
# Day 7
# https://adventofcode.com/2022/day/7


file = open("input.txt", "r")
input = file.readlines()

files = []
pwd = ""
for line in input:
    line = line.strip("\n")
    if line[0:5] == "$ cd ":
        pwd += pwd + line[6:]
    elif line[0:4] == "$ ls":
        None
    else:
        if line[0:4] == "dir ":
            files.append(pwd + "/" + line[4:])
        else:
            files.append(pwd + "/" + line)


print("First Puzzle:")




print("Second Puzzle:")
