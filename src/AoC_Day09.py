from lib import *
from functools import reduce

def part01(input01):

    board = Board(list(map(list, input01)))
    
    return board.calcMinima()

def part02(input02):

    board = Board(list(map(list, input02)))

    board.calcMinima()

    return board.calcBasins()

class Board:
    def __init__(self,boardLines):
        self.minima = []
        self.boardLines = boardLines
        self.LINES = len(boardLines)
        self.COLUMNS = len(boardLines[0])
        self.visited = []

    def calcMinima(self):
        riskSum = 0
        for i in range(self.LINES):
            for j in range(self.COLUMNS):
                riskSum = riskSum + self.calcRiskFor(self.boardLines[i][j], i, j)
        return riskSum

    def inBoundsLine(self, iLine):
        return 0 <= iLine < self.LINES

    def inBoundsColumn(self, iColumn):
        return 0 <= iColumn < self.COLUMNS

    def calcRiskFor(self, value, i, j):
        isRisky = True
        for (line, column) in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if not self.check(value, line, column):
                isRisky = False

        if isRisky:
            self.minima.append((i,j))
            return int(value) + 1
        return int(value) + 1 if isRisky else 0

    def check(self, value, i, j):
        if self.inBoundsLine(i) and self.inBoundsColumn(j):
            return int(self.boardLines[i][j]) > int(value)
        else:
            return True

    def calcBasins(self):
        total = []
        for minimum in self.minima:
            self.visited = []
            for i in range(self.LINES):
                self.visited.append(self.COLUMNS*[False])

            total.append(self.visitNeighbours(minimum[0], minimum[1]))

        total = sorted(total,reverse=True)
        return total[0] * total[1] * total[2]

    def visitNeighbours(self, line, column):
        self.visited[line][column] = True
        neighbours = 1
        for (nLine, nColumn) in [(line-1, column), (line+1, column), (line, column-1), (line, column+1)]:
            if self.inBoundsLine(nLine) and self.inBoundsColumn(nColumn) and not self.visited[nLine][nColumn] and not self.boardLines[nLine][nColumn] == '9':
                neighbours = neighbours + self.visitNeighbours(nLine, nColumn)
        return neighbours


pathDay = "day09"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 15:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_02.txt" % pathDay)
testResult02 = part02(testInput01)
if testResult02 == 1134:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


