from lib import *


def part01(input01):
    countOn = len(input01[0]) * [0]
    countOff = len(input01[0]) * [0]

    for readings in input01:
        for i, reading in enumerate(readings):
            if int(reading):
                countOn[i] = countOn[i] + 1
            else:
                countOff[i] = countOff[i] + 1

    gamma = ''
    epsilon = ''

    for i, on in enumerate(countOn):
        if on > countOff[i]:
            gamma = gamma + '1'
        else:
            gamma = gamma + '0'

    for i, on in enumerate(countOn):
        if on < countOff[i]:
            epsilon = epsilon + '1'
        else:
            epsilon = epsilon + '0'

    return int(gamma, 2) * int(epsilon, 2)


def part02(input02):
    gamma = calcNumberOfBits(input02)

    ## here starts 2

    oxy = list(filter(lambda x: int(x[0]) == gamma[0], input02))
    co2 = list(filter(lambda x: int(x[0]) != gamma[0], input02))
    i = 1
    while len(oxy) > 1:
        gamma = calcNumberOfBits(oxy)
        oxy = list(filter(lambda x: int(x[i]) == gamma[i], oxy))
        i = i+1
    i = 1
    while len(co2) > 1:
        gamma = calcNumberOfBits(co2)
        co2 = list(filter(lambda x: int(x[i]) != gamma[i], co2))
        i = i+1
    return int("".join(map(str, oxy[0])), 2) * int("".join(map(str, co2[0])), 2)


def calcNumberOfBits(input):
    countOn = len(input[0]) * [0]
    countOff = len(input[0]) * [0]

    for readings in input:
        for i, reading in enumerate(readings):
            if int(reading):
                countOn[i] = countOn[i] + 1
            else:
                countOff[i] = countOff[i] + 1

    gamma = len(input[0]) * [0]

    for i, on in enumerate(countOn):
        if on >= countOff[i]:
            gamma[i] = 1
        else:
            gamma[i] = 0

    return gamma


testInput01 = readLinesFromFileAsChars("day03/input_test_01.txt")
testResult01 = part01(testInput01)
if testResult01 == 198:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFileAsChars("day03/input_test_01.txt")
testResult02 = part02(testInput02)
if testResult02 == 230:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)

inputAsArray = readLinesFromFileAsChars("day03/input.txt")

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


