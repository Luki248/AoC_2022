# Advent of Code
# Day 8
# https://adventofcode.com/2022/day/8


file = open("input.txt", "r")
input = file.readlines()

trees = []
for line in input:
    temp = list(map(int, list(line.strip("\n"))))
    trees.append(temp)


def is_visible(m, n):
    visible_t = True
    for i in range(m - 1, -1, -1):
        if trees[m][n] <= trees[i][n]:
            visible_t = False
            break

    visible_r = True
    for i in range(n + 1, len(trees[0]), 1):
        if trees[m][n] <= trees[m][i]:
            visible_r = False
            break

    visible_d = True
    for i in range(m + 1, len(trees), 1):
        if trees[m][n] <= trees[i][n]:
            visible_d = False
            break

    visible_l = True
    for i in range(n - 1, -1, -1):
        if trees[m][n] <= trees[m][i]:
            visible_l = False
            break

    return visible_t or visible_r or visible_d or visible_l

count_visible = 2 * len(trees[0]) + (2 * len(trees)) - 4
for i in range(1, len(trees[0]) - 1):
    for j in range(1, len(trees) - 1):
        if is_visible(i, j):
            count_visible += 1
print("First Puzzle:", count_visible)


scenic_score_max = 0
for i in range(1, len(trees[0]) - 1):
    for j in range(1, len(trees) - 1):
        
        if scenic_score_max < scenic_score:
            scenic_score_max += 1
print("Second Puzzle:", scenic_score_max)
