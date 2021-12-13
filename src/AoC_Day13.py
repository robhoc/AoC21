from lib import *
from functools import reduce

class Board:
    def __init__(self, boardLines):
        self.boardLines = []
        self.LINES = len(boardLines)
        self.COLUMNS = len(boardLines[0])
        self.visited = []

        maxX = 0
        maxY = 0
        coords = []
        for line in boardLines:
            (x, y) = getAllNumbersFromString(line)
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
            coords.append((x, y))
        self.boardLines = [((1+maxY) * [False]) for x in range(maxX + 1)]

        count = 0
        for (cX,cY) in coords:
            count = count + 1
            self.boardLines[cX][cY] = True

    def fold(self, foldAlongX, foldLine):
        #vertical
        if foldAlongX:
            newNormal = self.boardLines[:foldLine]
            for i, l in enumerate(self.boardLines):
                for j, isPointSet in enumerate(l):
                    if i > foldLine and isPointSet:
                        newNormal[foldLine-(i-foldLine)][j] = True
        #horizontal:
        else:
            newNormal = [i[:foldLine] for i in self.boardLines]
            for i, l in enumerate(self.boardLines):
                for j, isPointSet in enumerate(l):
                    if j > foldLine and isPointSet:
                        newNormal[i][foldLine-(j - foldLine)] = True

        self.boardLines = newNormal

def part01(input01):
    board = Board([i for i in input01 if ',' in i])
    foldingInstructions =[i for i in input01 if 'x' in i or 'y' in i]
    #for instruction in foldingInstructions:
    #   board.fold('x' in instruction, getNumbersFromString(instruction))
    board.fold('x' in foldingInstructions[0], getNumbersFromString(foldingInstructions[0]))

    count = 0
    for line in board.boardLines:
        for column in line:
            if column:
                count = count + 1

    return reduce(lambda x, y: x+y, list(map(lambda x: x.count(True), board.boardLines)))

def part02(input02):
    board = Board([i for i in input02 if ',' in i])
    foldingInstructions = [i for i in input02 if 'x' in i or 'y' in i]
    for instruction in foldingInstructions:
        board.fold('x' in instruction, getNumbersFromString(instruction))

    for line in board.boardLines:

        print(''.join(list(map(lambda x: '#' if x else '.', line))))


    return ''

pathDay = "day13"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 17:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


