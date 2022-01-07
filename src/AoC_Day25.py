from lib import *
from functools import reduce
import time

class Board:
    def __init__(self, boardLines):
        self.boardLines = []
        self.LINES = len(boardLines)
        self.COLUMNS = len(boardLines[0])
        self.visited = []
        for line in boardLines:
            self.boardLines.append(list(line))
        print(self.boardLines)

    def resetVisited(self):
        self.costs = []
        for i in range(self.LINES):
            self.costs.append(self.COLUMNS * [False])

    def inBoundsLine(self, iLine):
        return 0 <= iLine < self.LINES

    def inBoundsColumn(self, iColumn):
        return 0 <= iColumn < self.COLUMNS

    def doSteps(self):
        count = 0
        res = True
        while res:
            moveRight = self.doMoveRight()
            moveDown = self.doMoveDown()
            res = moveRight or moveDown

            count = count+1
            print('move',count,'done')
        return count

    def doMoveRight(self):
        res = False
        next = [self.COLUMNS * ['.'] for line in self.boardLines]

        for i, line in enumerate(self.boardLines):
            for j, column in enumerate(line):
                if self.boardLines[i][j] == '.' and not next[i][j] == '>':
                    next[i][j] = '.'
                elif self.boardLines[i][j] == 'v':
                    next[i][j] = 'v'
                elif self.boardLines[i][j] == '>' and self.boardLines[i][(j+1) % self.COLUMNS] == '.':
                    res = True
                    next[i][(j+1) % self.COLUMNS] = '>'
                elif self.boardLines[i][j] == '>':
                    next[i][j] = '>'
        self.boardLines = next
        return res

    def doMoveDown(self):
        res = False
        next = [self.COLUMNS * ['.'] for line in self.boardLines]

        for i, line in enumerate(self.boardLines):
            for j, column in enumerate(line):
                if self.boardLines[i][j] == '.' and not next[i][j] == 'v':
                    next[i][j] = '.'
                elif self.boardLines[i][j] == '>':
                    next[i][j] = '>'
                elif self.boardLines[i][j] == 'v' and self.boardLines[(i + 1) % self.LINES][j] == '.':
                    res = True
                    next[(i + 1) % self.LINES][j] = 'v'
                elif self.boardLines[i][j] == 'v':
                    next[i][j] = 'v'

        self.boardLines = next
        return res


def part01(input01):
    print(input01)
    board = Board(input01)
    return board.doSteps()

def part02(input02):
    print("Todo")
    return "todo"


pathDay = "day25"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 58:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_02.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == "bullshit":
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

start_time = time.time()
print("Solution Part 01:", part01(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print("Solution Part 02:", part02(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

