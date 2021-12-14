from lib import *
from functools import reduce

def part01(input01):
    instructionsArray = [i.split(' -> ') for i in input01[2:]]
    instructionsDict = {}
    for x, y in instructionsArray:
        instructionsDict[x] = y

    template = input01[0]

    for i in range(10):
        next = template[0]
        for j in range(len(template)):
            if template[j:j + 2] in instructionsDict:
                next = next + instructionsDict[template[j:j + 2]] + template[j + 1]
        template = next

    histogram = {}
    for c in template:
        if c in histogram:
            histogram[c] = histogram[c] + 1
        else:
            histogram[c] = 1

    min = histogram['B']
    max = histogram['B']

    for c in histogram.keys():
        num = histogram[c]
        if num > max:
            max = num
        elif num < min:
            min = num
    return max - min



class Board:
    def __init__(self, instructions):
        self.histogram = {}
        self.instructions = instructions
        self.memo = {}

    def addCharToHistogram(self, c):
        if c in self.histogram:
            self.histogram[c] = self.histogram[c] + 1
        else:
            self.histogram[c] = 1

    def addAllCharsButFirstToHistogram(self, string):
        for i in range(len(string)):
            if i:
                self.addCharToHistogram(string[i])

    def createHistoFromStringButFirstChar(self, string):
        histogram = {}
        for i in range(len(string)):
            if i:
                c = string[i]
                if c in histogram:
                    histogram[c] = histogram[c] + 1
                else:
                    histogram[c] = 1
        return histogram

    def getHistoResult(self):
        min = self.histogram['B']
        max = self.histogram['B']

        for c in self.histogram.keys():
            num = self.histogram[c]
            if num > max:
                max = num
            elif num < min:
                min = num
        return max - min

    def getResultForHisto(self, histo):
        min = histo['B']
        max = histo['B']

        for c in histo.keys():
            num = histo[c]
            if num > max:
                max = num
            elif num < min:
                min = num
        return max - min

    def solve(self, string, stepsRemaining):
        if stepsRemaining:
            for j in range(len(string)-1):
                c = self.instructions["".join(string[j:j + 2])]
                self.solve(string[j] + c + string[j+1], stepsRemaining - 1)
        else:
            self.addAllCharsButFirstToHistogram(string)

    def solveAndReturn(self, string, stepsRemaining):

        if str(stepsRemaining)+string in self.memo:
            return self.memo[str(stepsRemaining)+string]

        histo = {}

        if stepsRemaining:
            for j in range(len(string)-1):
                c = self.instructions["".join(string[j:j + 2])]
                histo = self.combineHistos(histo, self.solveAndReturn(string[j] + c + string[j+1], stepsRemaining - 1))
        else:
            return self.createHistoFromStringButFirstChar(string)

        self.memo[str(stepsRemaining) + string] = histo
        return histo

    def combineHistos(self, histo1, histo2):
        res = histo1

        for c in histo2.keys():
            if c in histo1:
                res[c] = histo1[c] + histo2[c]
            else:
                res[c] = histo2[c]
        return res


def part02(input01):

    instructionsArray = [i.split(' -> ') for i in input01[2:]]
    instructionsDict = {}
    for x, y in instructionsArray:
        instructionsDict[x] = y

    board = Board(instructionsDict)

    histo = board.solveAndReturn(input01[0], 40)

    print(histo)

    return board.getResultForHisto(histo)

pathDay = "day14"

testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 1588:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 2188189693529:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


