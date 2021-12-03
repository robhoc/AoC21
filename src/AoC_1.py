import collections

from lib import *

def part01(input_01):
    first = True
    last = 0
    count = 0
    for line in input_01:
        num = forceAsInt(line)
        if first:
            first = False
        else:
            if num > last:
                count = count + 1
        last = num
    return count

def part02(input02):
    first = True
    second = True
    third = True
    last = 0
    count = 0
    window = collections.deque(3 * [0], 3)
    sumWindow = 0

    for line in input02:
        num = forceAsInt(line)
        window.appendleft(num)
        sumWindow = 0
        for entry in window:
            sumWindow = sumWindow + entry

        if first:
            first = False
        elif second:
            second = False
        elif third:
            third = False
        else:
            if sumWindow > last:
                count = count + 1

        last = sumWindow
    return count

testInput01 = readLinesFromFile("day01/input_test_01.txt")
testResult = part01(testInput01)
if testResult == 7:
    print("Test Part 01 succeeded")
else:
    print("Test Part 01 failed, returned", testResult)

testInput02 = readLinesFromFile("day01/input_test_02.txt")
testResult02 = part02(testInput01)
if testResult02 == 5:
    print("Test Part 02 succeeded")
else:
    print("Test Part 02 failed, returned", testResult02)


inputDay01 = readLinesFromFile("day01/input.txt")

print("Solution Part 01:", part01(inputDay01))

print("Solution Part 02:", part02(inputDay01))


