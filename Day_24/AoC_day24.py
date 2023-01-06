# Advent of Code
# Day 24
# https://adventofcode.com/2022/day/24


file = open("input.txt", "r")
input_ = file.readlines()

startpoint_x = 1
startpoint_y = 1
endpoint_x = len(input_[0]) - 3
endpoint_y = len(input_) - 2

arr = []
for line in input_:
    line = line.strip("\n")
    temp = []
    for chr in line:
        temp.append(chr)
    arr.append(temp)


def print_arr():
    for line in arr:
        for chr in line:
            print(chr, end="")
        print()


def calc_arr():
    global arr
    arr_temp = []
    for i in range(len(arr)):
        temp = []
        for j in range(len(arr[0])):
            temp.append(".")
        arr_temp.append(temp)
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i][j] == "^":
                if arr[i-1][j] == "#":
                    arr_temp[len(arr)-2][j] = "^"
                else:
                    arr_temp[i-1][j] = "^"
            if arr[i][j] == "v":
                if arr[i+1][j] == "#":
                    arr_temp[1][j] = "v"
                else:
                    arr_temp[i+1][j] = "v"
            if arr[i][j] == ">":
                if arr[i][j+1] == "#":
                    arr_temp[i][1] = ">"
                else:
                    arr_temp[i][j+1] = ">"
            if arr[i][j] == "<":
                if arr[i][j-1] == "#":
                    arr_temp[i][len(arr[0])-2] = "<"
                else:
                    arr_temp[i][j-1] = "<"
    
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            arr[i][j] = arr_temp[i][j]


while True:
    print_arr()
    key = input("> ")
    calc_arr()
    

print("First Puzzle:")


print("Second Puzzle:")
