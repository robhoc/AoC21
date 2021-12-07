from lib import *
from functools import reduce

def part01(input01):
    print("Todo")
    return "todo"

def part02(input02):
    print("Todo")
    return "todo"


testInput01 = readLinesFromFile("dayX/input_test_01.txt")
testResult01 = part01(testInput01)
if testResult01 == "bullshit":
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("dayX/input_test_02.txt")
testResult02 = part02(testInput01)
if testResult02 == "bullshit":
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("dayX/input.txt")

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


