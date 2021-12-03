from lib import *

def part01(input01):
    depth = 0
    coord = 0
    for instruction in input01:
        if doesStringStartWithString(instruction, "forward"):
            coord = coord + getNumbersFromString(instruction)
        elif doesStringStartWithString(instruction, "up"):
            depth = depth - getNumbersFromString(instruction)
        elif doesStringStartWithString(instruction, "down"):
            depth = depth + getNumbersFromString(instruction)
    return depth * coord


def part02(input02):
    depth = 0
    coord = 0
    aim = 0
    for instruction in input02:
        X = getNumbersFromString(instruction)
        if doesStringStartWithString(instruction, "forward"):
            string = X
            coord = coord + string
            depth = depth + (X * aim)
        elif doesStringStartWithString(instruction, "up"):
            aim = aim - X
        elif doesStringStartWithString(instruction, "down"):
            aim = aim + X
    return depth * coord



testInput01 = readLinesFromFile("day02/input_test_01.txt")
testResult01 = part01(testInput01)
if testResult01 == 150:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("day02/input_test_02.txt")
testResult02 = part02(testInput02)
if testResult02 == 900:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("day02/input.txt")

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


