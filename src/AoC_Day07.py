import sys
from lib import *
from functools import reduce


def move(x, toLevel):
    if x > toLevel:
        return x - toLevel
    return toLevel - x

def move(x, toLevel):
    if x > toLevel:
        return x - toLevel
    return toLevel - x


def move2(x, toLevel):
    if x > toLevel:
        return ((x - toLevel) * (x - toLevel + 1)) / 2
    return ((toLevel - x) * (toLevel - x + 1)) / 2


def getAllTo(level, allLevels):
    return reduce(lambda y, z: y + z, map(lambda x: move(x, level), allLevels))

def getAllTo2(level, allLevels):
    return reduce(lambda y, z: y + z, map(lambda x: move2(x, level), allLevels))

def part01(input01):
    numbersAsArray = list(map(int, getAllNumbersFromString(input01[0])))
    minimum = reduce(lambda x, y: min(x, y), numbersAsArray)
    maximum = reduce(lambda x, y: max(x, y), numbersAsArray)
    minFuel = maximum * len(numbersAsArray)
    goToLevel = 0
    for i in range(minimum, maximum+1):
        fuelConsumption = getAllTo(i, numbersAsArray)
        if fuelConsumption < minFuel:
            minFuel = fuelConsumption
            goToLevel = i
    return minFuel

def part02(input02):

    numbersAsArray = list(map(int, getAllNumbersFromString(input02[0])))
    minimum = reduce(lambda x, y: min(x, y), numbersAsArray)
    maximum = reduce(lambda x, y: max(x, y), numbersAsArray)
    minFuel = sys.maxsize

    for i in range(minimum, maximum+1):
        fuelConsumption = getAllTo2(i, numbersAsArray)
        if fuelConsumption < minFuel:
            minFuel = fuelConsumption
    return minFuel


testInput01 = readLinesFromFile("day07/input_test_01.txt")
testResult01 = part01(testInput01)
if testResult01 == 37:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("day07/input_test_01.txt")
testResult02 = part02(testInput01)
if testResult02 == 168:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("day07/input.txt")

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


