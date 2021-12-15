import sys
import time
from lib import *
from functools import reduce

class Board:
    def __init__(self, boardLines):
        self.unvisitedNodes = {}
        self.visitedNodes = {}
        self.nextUnvisitedNodes = {}
        self.boardArray = []
        self.costs = {}

        self.LINES = len(boardLines)
        self.COLUMNS = len(boardLines[0])
        for i, line in enumerate(boardLines):
            for j, column in enumerate(line):
                self.unvisitedNodes[(i, j)] = boardLines[i][j]
                self.costs[(i, j)] = sys.maxsize
        for line in boardLines:
            self.boardArray.append(list(map(int, list(line))))

    def inBoundsLine(self, iLine):
        return 0 <= iLine < self.LINES

    def inBoundsColumn(self, iColumn):
        return 0 <= iColumn < self.COLUMNS

    def result(self):
        return self.costs[(self.LINES-1, self.COLUMNS-1)]

    def solve(self):
        self.costs[(0, 0)] = 0
        self.nextUnvisitedNodes[(0, 1)] = self.boardArray[0][1]
        self.nextUnvisitedNodes[(1, 0)] = self.boardArray[1][0]

        while len(self.nextUnvisitedNodes.keys()) > 0:
            self.visitNext()
        return

    def visitNext(self):
        currentCosts = {k: v for k, v in sorted(self.nextUnvisitedNodes.items(), key=lambda item: int(item[1]))}

        #get first item
        currentNode = list(currentCosts)[0]
        distance = currentCosts[currentNode]
        del self.unvisitedNodes[currentNode]
        del self.nextUnvisitedNodes[currentNode]

        x = currentNode[0]
        y = currentNode[1]

        for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if self.inBoundsLine(i) and self.inBoundsColumn(j) and (i, j) in self.unvisitedNodes:
                if not (i, j) in self.nextUnvisitedNodes:
                    self.nextUnvisitedNodes[(i, j)] = sys.maxsize

                if distance + self.boardArray[i][j] < self.costs[(i, j)]:
                    self.costs[(i, j)] = distance + self.boardArray[i][j]
                    self.nextUnvisitedNodes[(i,j)] = self.costs[(i, j)]


    def visitNext2(self):

        #sort by distance to start and only respect unvisited nodes
        currentCosts = {k: v for k, v in sorted(self.costs.items(), key=lambda item: int(item[1])) if k in self.unvisitedNodes}

        #get first item
        currentNode = list(currentCosts)[0]
        distance = currentCosts[currentNode]
        del self.unvisitedNodes[currentNode]

        x = currentNode[0]
        y = currentNode[1]

        for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if self.inBoundsLine(i) and self.inBoundsColumn(j) and (i, j) in self.unvisitedNodes:
                if distance + self.boardArray[i][j] < self.costs[(i, j)]:
                    self.costs[(i, j)] = distance + self.boardArray[i][j]



def part01(input01):
    board = Board(input01)

    board.solve()

    return board.result()

def part02(input02):
    length = len(input02)
    input = []
    for i in range(length * 5):
        input.append([''] * length * 5)

    for multiLine in range(5):
        for multiCol in range(5):
            for i in range(length):
                for j in range(length):
                    nextValue = int(input02[i][j]) + multiLine + multiCol
                    nextValue = nextValue if nextValue < 10 else (nextValue + 1) % 10
                    input[i+(multiLine*length)][j+(multiCol*length)] = nextValue
    return part01(input)


pathDay = "day15"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 40:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_02.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 315:
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


