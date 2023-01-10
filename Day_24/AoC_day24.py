# Advent of Code
# Day 24
# https://adventofcode.com/2022/day/24


file = open("input.txt", "r")
input_ = file.readlines()


class Item:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol


class Board:
    def __init__(self, w, h):
        self.board = []
        self.w = w
        self.h = h

    def add_item(self, x, y, symbol):
        item = Item(x, y, symbol)
        self.board.append(item)

    def print(self):
        arr = []
        for _ in range(self.h):
            temp = []
            for _ in range(self.w):
                temp.append(".")
            arr.append(temp)

        for item in self.board:
            arr[item.y][item.x] = item.symbol

        print("#" * (self.w + 2))
        for line in arr:
            print("#", end="")
            for chr in line:
                print(chr, end="")
            print("#")
        print("#" * (self.w + 2))

    def calc_move(self):
        for item in self.board:
            if item.symbol == "^":
                if item.y >= 0:
                    item.y = self.h - 1
                else:
                    item.y -= 1
            if item.symbol == "v":
                if item.y >= self.h-1:
                    item.y = 0
                else:
                    item.y += 1
            if item.symbol == ">":
                if item.x >= self.w-1:
                    item.x = 0
                else:
                    item.x += 1
            if item.symbol == "<":
                if item.x <= 0:
                    item.x = self.w - 1
                else:
                    item.x -= 1


width = 100
height = 35
board = Board(width, height)
i = 0
j = 0
for line in input_:
    line = line.strip("\n#.")
    if line != "":
        for chr in line:
            if chr != ".":
                board.add_item(i, j, chr)
            i += 1
        i = 0
        j += 1


while True:
    board.print()
    key = input("> ")
    board.calc_move()


print("First Puzzle:")


print("Second Puzzle:")
