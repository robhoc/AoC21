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


class Parser:
    def __init__(self, binaryString, indent):
        self.indent = indent
        self.binaryString = binaryString
        self.currentPosition = 0
        self.type = -1
        self.version = 0
        self.lengthTypeId = ''
        self.subPacketLengths = 0
        self.literal = 0
        print(self.indent + 'new parser for', binaryString)

    def parse(self):

        # 010 000 0 000000101101011 0000110011100010010000

        self.parseHeader()

        if self.type == 4:
            print(self.indent + 'literal')
            self.parseLiteral()
            print(self.indent, self.literal)
            self.printCurrentPosition()
            return self.literal
        else:
            print(self.indent + 'operator id', self.type)
            self.parseLengthTypeId()
            self.parseLengthInformation()

            if self.lengthTypeId == '0':
                print(self.indent + 'fixed length subs')
                self.printCurrentPosition()
                subLengthsParsed = 0
                packageResults = []
                while subLengthsParsed+7 < self.subPacketLengths:
                    print(self.indent + 'parsed', subLengthsParsed, 'bits of', self.subPacketLengths)
                    self.printCurrentPosition()
                    parser = Parser(self.binaryString[self.currentPosition: self.currentPosition + self.subPacketLengths], self.indent + '   ')
                    packageResults.append(parser.parse())

                    subParserLength = parser.currentPosition
                    subLengthsParsed = subLengthsParsed + subParserLength
                    self.getNextBits(subParserLength)

                return self.calcResultForSubPackages(packageResults)
            else:
                print(self.indent, self.subPacketLengths, 'subs')
                self.printCurrentPosition()
                packageResults = []
                for i in range(self.subPacketLengths):
                    print(self.indent + 'parsing', i, 'of', self.subPacketLengths)
                    self.printCurrentPosition()
                    parser = Parser(self.binaryString[self.currentPosition:], self.indent + '   ')
                    packageResults.append(parser.parse())

                    # lesekopf weiter
                    self.getNextBits(parser.currentPosition)

                print(self.indent + 'multi package parser returning', packageResults)

                return self.calcResultForSubPackages(packageResults)

        return "error"


    def parseHeader(self):
        header = self.getNextBits(3)
        self.version = int(header, 2)
        print(self.indent + "version", self.version)

        typeId = self.getNextBits(3)
        self.type = int(typeId, 2)
        print(self.indent + 'type', self.type)

    def parseLengthTypeId(self):
        self.lengthTypeId = self.getNextBits(1)
        print(self.indent + 'Length type', '15 bits fixed' if self.lengthTypeId == '0' else '11 bits multi')

    def parseLengthInformation(self):

        if self.lengthTypeId == '1':
            lengthInformation = self.getNextBits(11)
        else:
            lengthInformation = self.getNextBits(15)

        self.subPacketLengths = int(lengthInformation, 2)

    def getNextBits(self, numBits):
        res = self.binaryString[self.currentPosition:self.currentPosition + numBits]
        self.currentPosition = self.currentPosition + numBits
        return res

    def parseLiteral(self):
        res = ''
        while not self.getNextBits(1)[0] == '0':
            res = res + ''.join(self.getNextBits(4))
        res = res + ''.join(self.getNextBits(4))
        res = int(res, 2)
        self.literal = res

    def printCurrentPosition(self):
        print(self.indent + 'current position', self.currentPosition, 'of', len(self.binaryString))

    def calcResultForSubPackages(self, packageResults):
        if self.type == 0:
            sum = 0
            for r in packageResults:
                sum = sum + r
            print(self.indent, 'sum', sum)
            return sum
        elif self.type == 1:
            product = 1
            for r in packageResults:
                product = product * r
            print(self.indent,'prod', product)
            return product
        elif self.type == 2:
            min = packageResults[0]
            for r in packageResults:
                if r < min:
                    min = r
            print(self.indent,'min', min)
            return min
        elif self.type == 3:
            max = packageResults[0]
            for r in packageResults:
                if r > max:
                    max = r
            print(self.indent,'max', max)
            return max
        elif self.type == 5:
            print(self.indent,'gt')
            if packageResults[0] > packageResults[1]:
                return 1
            return 0
        elif self.type == 6:
            print(self.indent,'lt')
            if packageResults[0] < packageResults[1]:
                return 1
            return 0
        elif self.type == 7:
            print(self.indent,'eq')
            if packageResults[0] == packageResults[1]:
                return 1
            return 0

class Parser01:
    def __init__(self, binaryString, indent):
        self.indent = indent
        self.binaryString = binaryString
        self.currentPosition = 0
        self.type = ''
        self.version = 0
        self.lengthTypeId = ''
        self.subPacketLengths = 0
        print(self.indent + 'new parser for', binaryString)

    def parse(self):

        # 1_1
        #100 010 1 00000000001
        #    001 010 1 00000000001
        #        101 010 0 000000000001011
        #            110 100 01111 000

        # 1_2
        # 011 000 1 00000000010
        #   #2 sub
        #   000 000 0 000000000010110
        #       fixed length sub(s)
        #       000 100 01010
        #       101 100 0 1011
        #   001 000 1 00000000010
                #2 sub
        #           000 100 01100
        #           011 100 01101 00

        self.parseHeader()

        if self.type == 4:
            print(self.indent + 'literal')
            self.parseLiteral()
            self.printCurrentPosition()
            return self.version
        else:
            print(self.indent + 'operator')
            self.parseLengthTypeId()
            self.parseLengthInformation()

            if self.lengthTypeId == '0':
                print(self.indent + 'fixed length subs')
                self.printCurrentPosition()
                subLengthsParsed = 0
                version = 0
                while subLengthsParsed+7 < self.subPacketLengths:
                    print(self.indent + 'parsed', subLengthsParsed, 'bits of', self.subPacketLengths)
                    self.printCurrentPosition()
                    parser = Parser01(self.binaryString[self.currentPosition: self.currentPosition + self.subPacketLengths], self.indent + '   ')
                    version = version + parser.parse()

                    # lesekopf weiter
                    subParserLength = parser.currentPosition
                    subLengthsParsed = subLengthsParsed + subParserLength
                    self.getNextBits(subParserLength)

                return version + self.version
            else:
                print(self.indent, self.subPacketLengths, 'subs')
                self.printCurrentPosition()
                version = 0
                for i in range(self.subPacketLengths):
                    print(self.indent + 'parsing', i, 'of', self.subPacketLengths)
                    self.printCurrentPosition()
                    parser = Parser01(self.binaryString[self.currentPosition:], self.indent + '   ')
                    version = version + parser.parse()

                    # lesekopf weiter
                    self.getNextBits(parser.currentPosition)

                print(self.indent + 'multi package parser returning', version + self.version)

                return version + self.version

        return "error"

    def parseHeader(self):
        header = self.getNextBits(3)
        self.version = int(header, 2)
        print(self.indent + "version", self.version)

        typeId = self.getNextBits(3)
        self.type = int(typeId, 2)
        print(self.indent + 'type', self.type)

    def parseLengthTypeId(self):
        self.lengthTypeId = self.getNextBits(1)
        print(self.indent + 'Length type', '15 bits fixed' if self.lengthTypeId == '0' else '11 bits multi')

    def parseLengthInformation(self):

        if self.lengthTypeId == '1':
            lengthInformation = self.getNextBits(11)
        else:
            lengthInformation = self.getNextBits(15)

        self.subPacketLengths = int(lengthInformation, 2)

    def getNextBits(self, numBits):
        res = self.binaryString[self.currentPosition:self.currentPosition + numBits]
        self.currentPosition = self.currentPosition + numBits
        return res

    def parseLiteral(self):
        res = ''
        while not self.getNextBits(1)[0] == '0':
            res = res + ''.join(self.getNextBits(4))
        res = res + ''.join(self.getNextBits(4))
        res = int(res, 2)
        return res

    def printCurrentPosition(self):
        print(self.indent + 'current position', self.currentPosition, 'of', len(self.binaryString))


def part01(input01):
    binaryString = str(bin(int(input01[0], 16)))[2:]
    while not len(binaryString) % 4 == 0:
        binaryString = '0' + binaryString

    parser = Parser01(binaryString, '')
    return parser.parse()


def part02(input02):
    print(input02[0])
    binaryString = str(bin(int(input02[0], 16)))[2:]
    print(binaryString)
    while not len(binaryString) % 8 == 0:
        binaryString = '0' + binaryString

    parser = Parser(binaryString, '')
    return parser.parse()


pathDay = "day16"
testInput01 = readLinesFromFile("%s/input_test_01_1.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 16:
    print("##### Test Part 01_1 successful")
else:
    print("##### Test Part 01_1 failed, returned", testResult01)

testInput01 = readLinesFromFile("%s/input_test_01_2.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 12:
    print("##### Test Part 01_2 successful")
else:
    print("##### Test Part 01_2 failed, returned", testResult01)

testInput01 = readLinesFromFile("%s/input_test_01_3.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 23:
    print("##### Test Part 01_3 successful")
else:
    print("##### Test Part 01_3 failed, returned", testResult01)

testInput01 = readLinesFromFile("%s/input_test_01_4.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 31:
    print("Test Part 01_4 successful")
else:
    print("Test Part 01_4 failed, returned", testResult01)


testInput02 = readLinesFromFile("%s/input_test_02_1.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 3:
    print("Test Part 02_1 successful")
    print("Test Part 02_1 successful")
    print("Test Part 02_1 successful")
else:
    print("Test Part 02_1 failed, returned", testResult02)


testInput02 = readLinesFromFile("%s/input_test_02_2.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 54:
    print("Test Part 02_2 successful")
    print("Test Part 02_2 successful")
    print("Test Part 02_2 successful")
else:
    print("Test Part 02_2 failed, returned", testResult02)


testInput02 = readLinesFromFile("%s/input_test_02_3.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 7:
    print("Test Part 02_3 successful")
    print("Test Part 02_3 successful")
    print("Test Part 02_3 successful")
else:
    print("Test Part 02_3 failed, returned", testResult02)


testInput02 = readLinesFromFile("%s/input_test_02_4.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 9:
    print("Test Part 02_4 successful")
    print("Test Part 02_4 successful")
    print("Test Part 02_4 successful")
else:
    print("Test Part 02_4 failed, returned", testResult02)


testInput02 = readLinesFromFile("%s/input_test_02_5.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 1:
    print("Test Part 02_5 successful")
    print("Test Part 02_5 successful")
    print("Test Part 02_5 successful")
else:
    print("Test Part 02_5 failed, returned", testResult02)


testInput02 = readLinesFromFile("%s/input_test_02_6.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 0:
    print("Test Part 02_6 successful")
    print("Test Part 02_6 successful")
    print("Test Part 02_6 successful")
else:
    print("Test Part 02_6 failed, returned", testResult02)


testInput02 = readLinesFromFile("%s/input_test_02_7.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 0:
    print("Test Part 02_7 successful")
    print("Test Part 02_7 successful")
    print("Test Part 02_7 successful")
else:
    print("Test Part 02_7 failed, returned", testResult02)


testInput02 = readLinesFromFile("%s/input_test_02_8.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 1:
    print("Test Part 02_8 successful")
    print("Test Part 02_8 successful")
    print("Test Part 02_8 successful")
else:
    print("Test Part 02_8 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

start_time = time.time()
print("Solution Part 01:", part01(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print("Solution Part 02:", part02(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

