from lib import *
from functools import reduce


def part01(input01):
    outputs = []
    for line in input01:
        outputLine = line.split('|')[1].strip()
        for val in outputLine.split(' '):
            outputs.append(val)

    return len(list(filter(lambda x: len(x) in [2, 3, 4, 7], outputs)))

class Board:
    def __init__(self):
        self.ONE = []
        self.SEVEN = []
        self.FOUR = []
        self.NINE = []

    def initUniqueNumbers(self,  sequences):
        self.ONE = list(list(filter(lambda x: len(x) == 2, sequences))[0])
        self.SEVEN = list(list(filter(lambda x: len(x) == 3, sequences))[0])
        self.FOUR = list(list(filter(lambda x: len(x) == 4, sequences))[0])

        #side effect -> set nine
        self.findNumbers(list(filter(lambda x: len(x) == 6, sequences)))

    def findNumbers(self, outputs):
        return reduce(lambda x, y: x+y, list(map(lambda x: self.getNumber(list(x)), outputs)))

    def getNumber(self, sequence):
        length = len(sequence)
        if length == 2:
            return '1'
        elif length == 3:
            return '7'
        elif length == 4:
            return '4'
        elif length == 7:
            return '8'
        elif length == 5:
            # 2, 3, 5
            # 3 hat 2 buchstaben gleich mit 1, 3 mit 4 und 3 mit 7
            # 2 und 5 haben 1 mit 1, 3 mit 4 und 2 mit 7
                # 5 und 9 haben 5 gleiche, 2 und 9 nur 4
            if lenIntersect(self.ONE, sequence, 2):
                return '3'
            elif lenIntersect(self.NINE, sequence, 5):
                return '5'
            else:
                return '2'
        elif length == 6:
            # 0, 6, 9
            # 0 hat 2 Buchstaben gleich mit 1, 3 mit 4 und 3 mit 7
            # 6 hat 1 Buchstaben gleich mit 1, 3 mit 4 und 2 mit 7
            # 9 hat 2 Buchstaben gleich mit 1, 4 mit 4 und 3 mit 7
            if lenIntersect(sequence, self.ONE, 2) and lenIntersect(sequence, self.FOUR, 3):
                return '0'
            elif lenIntersect(sequence, self.ONE, 1):
                return '6'
            else:
                self.NINE = sequence
                return '9'
        else:
            print("error")
            return 'error'

def lenIntersect(first, second, length):
    return len(list(set(first) & set(second))) == length

def part02(input02):

    sumOutputs = 0
    for line in input02:
        outputs = line.split('|')[1].strip().split(' ')
        signals = sorted(line.split('|')[0].strip().split(' '), key=lambda x: len(x))

        board = Board()
        board.initUniqueNumbers(list(filter(lambda x: len(x) in [2, 3, 4, 6], signals)))

        numbers = board.findNumbers(outputs)
        sumOutputs = sumOutputs + int(numbers)

    return sumOutputs


pathDay = "day08"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 26:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult02 = part02(testInput01)
if testResult02 == 61229:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


