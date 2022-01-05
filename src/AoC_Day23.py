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
            self.boardLines.append(list(map(int, list(line))))
            #self.boardLines.append(list(line))
            #self.boardLines.append(line)

        def resetVisited(self):
            self.costs = []
            for i in range(self.LINES):
                self.costs.append(self.COLUMNS * [False])

        def inBoundsLine(self, iLine):
            return 0 <= iLine < self.LINES

        def inBoundsColumn(self, iColumn):
            return 0 <= iColumn < self.COLUMNS


def part01(input01):
    return "todo"

def part02(input02):
    print("Todo")
    return "todo"


pathDay = "day23"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == "bullshit":
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

