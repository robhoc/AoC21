from lib import *



class Board:
    def __init__(self):
        self.board = []

    def init(self,pointPairs):
        maxX = 0
        maxY = 0
        for pointPair in pointPairs:
            if pointPair[0] > maxX:
                maxX = pointPair[0]
            if pointPair[2] > maxX:
                maxX = pointPair[2]
            if pointPair[1] > maxY:
                maxY = pointPair[1]
            if pointPair[3] > maxY:
                maxY = pointPair[3]

        for i in range(1+maxX):
            self.board.append((1+maxY) * [0])

        for pointPair in pointPairs:
            self.addLine(pointPair)

    def addLine(self, line):
        if line[0] == line[2]:
            self.addVerticalLine(line)
        elif line[1] == line[3]:
            self.addHorizontalLine(line)
        #this destroys solution of pt. 1
        else:
            self.addDiagonalLine(line)

    def addVerticalLine(self, line):
        smallerY = min(line[1], line[3])
        largerY = max(line[1], line[3])
        for y in range(smallerY, largerY+1):
            self.board[line[0]][y] = self.board[line[0]][y] + 1

    def addHorizontalLine(self, line):
        smallerX = min(line[0], line[2])
        largerX = max(line[0], line[2])

        for x in range(smallerX, largerX+1):
            self.board[x][line[1]] = self.board[x][line[1]] + 1

    def addDiagonalLine(self, line):
        stepX = 1 if line[0] < line[2] else -1
        stepY = 1 if line[1] < line[3] else -1

        xCoords = list(range(line[0], line[2]+stepX, stepX))
        yCoords = list(range(line[1], line[3]+stepY, stepY))

        i = 0
        while i < len(xCoords):
            self.board[xCoords[i]][yCoords[i]] = self.board[xCoords[i]][yCoords[i]] + 1
            i = i+1


    def getNumberOfDangerousPoints(self):

        number = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] > 1:
                    number = number + 1
        return number




def part01(input01):
    pointPairs = list(map(getAllNumbersFromString, input01))
    board = Board()
    board.init(pointPairs)

    return board.getNumberOfDangerousPoints()

def part02(input02):
    pointPairs = list(map(getAllNumbersFromString, input02))
    board = Board()
    board.init(pointPairs)

    return board.getNumberOfDangerousPoints()


testInput01 = readLinesFromFile("day05/input_test_01.txt")
testResult01 = part01(testInput01)
if testResult01 == 5:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("day05/input_test_02.txt")
testResult02 = part02(testInput01)
if testResult02 == 12:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("day05/input.txt")

#print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


