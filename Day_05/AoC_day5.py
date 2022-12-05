# Advent of Code
# Day 5
# https://adventofcode.com/2022/day/5


file = open("input.txt", "r")
input = file.readlines()

stack_temp = []
i = 0
while input[i] != "\n":
    line = input[i].strip("\n")
    stack_temp.append(line)
    i += 1

stack = []
for i in range(1, len(stack_temp[0]), 4):
    temp = []
    for j in range(len(stack_temp) - 2, -1, -1):
        if stack_temp[j][i] != " ":
            temp.append(stack_temp[j][i])
    stack.append(temp)

moves = []
for i in range(10, len(input)):
    numbers = input[i].strip("\n").split(" ")
    moves.append([int(numbers[1]), int(numbers[3]), int(numbers[5])])


for move in moves:
    for i in range(move[0]):
        temp = stack[move[1] - 1][-1]
        stack[move[1] - 1].pop(-1)
        stack[move[2] - 1].append(temp)

code = ""
for staple in stack:
    code += staple[-1]

print("First Puzzle:", code)


stack = []
for i in range(1, len(stack_temp[0]), 4):
    temp = []
    for j in range(len(stack_temp) - 2, -1, -1):
        if stack_temp[j][i] != " ":
            temp.append(stack_temp[j][i])
    stack.append(temp)

moves = []
for i in range(10, len(input)):
    numbers = input[i].strip("\n").split(" ")
    moves.append([int(numbers[1]), int(numbers[3]), int(numbers[5])])

for move in moves:
    if move[0] == 1:
        temp = stack[move[1] - 1][-1]
        stack[move[1] - 1].pop(-1)
        stack[move[2] - 1].append(temp)
    else:
        temp = ""
        for i in range(move[0]):
            temp += stack[move[1] - 1][-1]
            stack[move[1] - 1].pop(-1)
        temp2 = ""
        for i in range(len(temp) - 1, -1, -1):
            temp2 += temp[i]
        temp = temp2
        for letter in temp:
            stack[move[2] - 1].append(letter)

code = ""
for staple in stack:
    code += staple[-1]

print("Second Puzzle:", code)
