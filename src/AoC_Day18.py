from math import ceil, floor

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


class SnailNumber():
    def __init__(self, number):
        self.number = number

        self.explodable = False
        self.indexExplosion = 0
        self.indexExplosionEnd = 0
        self.explodingPair = []

        self.splitable = False
        self.indexSplit = 0

    def parse(self):
        #print('parsing', self.number)
        self.explodable = False
        self.splitable = False
        self.indexExplosion = 0
        self.indexLeftNumberExplosion = 0

        countOpen = 0
        peeked = 0

        for i, c in enumerate(self.number):
            # bereits vorweg geschaut, überspringen
            if peeked > 0:
                peeked = peeked - 1
                continue
            elif c == '[':
                countOpen = countOpen + 1
                if countOpen > 4:
                    self.explodable = True
                    self.findIndexOfExplosion(i, countOpen)
                    return
            elif c == ']':
                countOpen = countOpen - 1
            elif c.isdigit():
                peeked = 0
                while self.number[1 + i + peeked].isdigit():
                    peeked = peeked + 1
                if peeked > 0:
                    self.splitable = True
                    self.indexSplit = i

    def reduce(self):

        while True:
            self.parse()
            if self.explodable:
                self.explode()
                continue
            if self.splitable:
                self.split()
                continue
            break

    def explode(self):
        #print('explode number old', self.number, 'at', self.indexExplosion, 'to', self.indexExplosionEnd)

        leftPart = ''
        rightPart = ''

        leftRegEx = re.search("\d+\D*$", self.number[:self.indexExplosion])
        #print(leftRegEx)
        if leftRegEx == None:
            leftPart = self.number[:self.indexExplosion]
        else:
            # left part of number
            stringLeft = self.number[:leftRegEx.start()]
            # int left of explosion

            numberToReplace = getAllNumbersFromString(leftRegEx.group())[0]
            numberLeft = numberToReplace + self.explodingPair[0]
            # part between left number and explosion

            leftInbetween = leftRegEx.group().replace(str(numberToReplace),'')
            leftPart = stringLeft + str(numberLeft) + leftInbetween
            #print('string left', stringLeft)
            #print('number left:', numberLeft)
            #print('left inbetween', leftInbetween)

        rightRegEx = re.search("\d+", self.number[self.indexExplosionEnd:])

        if rightRegEx == None:
            rightPart = self.number[self.indexExplosionEnd:]
        else:
            # right part of number
            stringRight = self.number[self.indexExplosionEnd + rightRegEx.end():]
            # int to the right of explosion
            numberRight = int(rightRegEx.group()) + self.explodingPair[1]
            # part between right number and explosion
            rightInbetween = self.number[self.indexExplosionEnd:(self.indexExplosionEnd + rightRegEx.start())]
            rightPart = rightInbetween + str(numberRight) + stringRight
            #print('right  inbetween', rightInbetween)
            #print('number right:', numberRight)
            #print('string right', stringRight)

        res = leftPart + '0' + rightPart
        #print('explode number new',res)
        self.number = res

    def split(self):

        #print('split number ', self.number, 'at', self.indexSplit)
        match = re.search("\d\d+", self.number)

        number = int(match.group())
        leftString = self.number[:match.start()]
        rightString = self.number[match.end():]

        res = leftString + '[' + str(floor(number/2)) + ',' + str(ceil(number/2)) + ']' + rightString
        #print('split done', res)
        self.number = res
        #print('new',res)
        return res

    def add(self, otherNumber):
        print('adding', self.number, otherNumber)
        self.number = '[' + self.number + ',' + otherNumber + ']'
        #print('new:', self.number)

    def findIndexOfExplosion(self, currentPosition, level):

        match = re.search("\[\d+,\d+]", self.number[currentPosition:])

        self.indexExplosion = currentPosition + match.start()
        self.indexExplosionEnd = currentPosition + match.end()
        self.explodingPair = getAllNumbersFromString(match.group())

        #print('index Explosion', self.indexExplosion)
        #print('index Explosion End', self.indexExplosionEnd)
        #print('pair exl', self.explodingPair)

    def calcMagnitude(self, number):
        currentNumber = number
        match = re.search("\[\d+,\d+]", currentNumber)

        while not match is None:
            print(currentNumber)
            numbers = getAllNumbersFromString(match.group())
            replacement = numbers[0] * 3 + numbers[1] * 2
            currentNumber = re.sub("\[\d+,\d+]", str(replacement), currentNumber, count=1)
            match = re.search("\[\d+,\d+]", currentNumber)
        return int(currentNumber)

def part01(input01):

    print(input01)
    current = SnailNumber(input01[0])

    for i in range(1, len(input01)):
        current.add(input01[i])
        current.reduce()
    return current.calcMagnitude(current.number)

def part02(input02):
    currentMax = 0
    for i in range(len(input02)):
        for j in range(len(input02)):
            if i == j:
                continue
            sumNum = part01([input02[i], input02[j]])
            if sumNum > currentMax:
                currentMax = sumNum
    return currentMax


pathDay = "day18"

testInput01 = readLinesFromFile("%s/input_test_01_1.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 3488:
    print("Test Part 01_1 successful")
else:
    print("Test Part 01_1 failed, returned", testResult01)

testInput01 = readLinesFromFile("%s/input_test_01_2.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 4140:
    print("Test Part 01_2 successful")
else:
    print("Test Part 01_2 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_02.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 3993:
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

