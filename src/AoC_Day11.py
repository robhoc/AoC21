from lib import *
from functools import reduce


class Board:
    def __init__(self, boardLines):
        self.boardLines = []
        self.LINES = len(boardLines)
        self.COLUMNS = len(boardLines[0])
        self.flashed = []
        for line in boardLines:
            self.boardLines.append(list(map(int,list(line))))

    def doStep(self):
        numFlashes = 0

        # increase energy for 1 each
        for i, line in enumerate(self.boardLines):
            for j, column in enumerate(line):
                self.boardLines[i][j] = column + 1

        # do flash, while any octo has energy > 9 and not flashed
        self.resetFlashed()

        someOctoNeedsAGoodFlashing = True
        while someOctoNeedsAGoodFlashing:
            someOctoNeedsAGoodFlashing = False
            for i, line in enumerate(self.boardLines):
                for j, _ in enumerate(line):
                    if self.needsFlashing(i, j):
                        someOctoNeedsAGoodFlashing = True
                        numFlashes = numFlashes + self.doFlash(i, j)
        # reset energy to 0 for every octo flashed
        for i, line in enumerate(self.boardLines):
            for j, column in enumerate(line):
                if self.flashed[i][j]:
                    self.boardLines[i][j] = 0
        return numFlashes

    def resetFlashed(self):
        self.flashed = []
        for i in range(self.LINES):
            self.flashed.append(self.COLUMNS * [False])

    def inBoundsLine(self, iLine):
        return 0 <= iLine < self.LINES

    def inBoundsColumn(self, iColumn):
        return 0 <= iColumn < self.COLUMNS

    def doFlash(self, i, j):
        self.flashed[i][j] = True
        for line in range(i-1, i+2):
            for column in range(j-1, j+2):
                if self.inBoundsLine(line) and self.inBoundsColumn(column):
                    # obdA: ignoriere, dass hier der initiierende Octo auch erhöht wird
                    self.boardLines[line][column] = self.boardLines[line][column] + 1
        return 1

    def needsFlashing(self, i, j):
        needs = self.boardLines[i][j] > 9 and not self.flashed[i][j]
        #print('needs flashing',i, j, self.boardLines[i][j], self.flashed[i][j], needs)
        return needs


def part01(input01):
    board = Board(input01)
    number = 0

    for i in range(100):
        number = number + board.doStep()
    return number

def part02(input02):
    board = Board(input02)
    number = 0

    for i in range(10000):
        number = board.doStep()
        if number == 100:
            return i+1

    return 'foo'





pathDay = "day11"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 1656:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult02 = part02(testInput01)
if testResult02 == 195:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


