from lib import *
from functools import reduce
import time

class Boat:
    def __init__(self):
        self.cubesOn = [[[False for i in range(-50, 51)] for j in range(-50, 51)] for k in range(-50, 51)]

    def doStep(self, s):
        xFrom = max(-50, s[0])
        xTo = min(50, s[1]) + 1

        yFrom = max(-50, s[2])
        yTo = min(50, s[3]) + 1

        zFrom = max(-50, s[4])
        zTo = min(50, s[5]) + 1

        on = True if s[6] else False

        for x in range(xFrom, xTo):
            for y in range(yFrom, yTo):
                for z in range(zFrom, zTo):
                    self.cubesOn[x][y][z] = on

    def numOn(self):
        numOn = 0
        for x in self.cubesOn:
            for y in x:
                numOn = numOn + y.count(True)
        return numOn

class Cubeoid:
    def __init__(self, minX, maxX, minY, maxY, minZ, maxZ, on):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ
        self.on = True if on == 1 else False

class BootStep:
    def __init__(self, cubeoids):
        self.cubies = cubeoids

    def calcOverlap(self, other):

        res = []

        for cuby in self.cubies:
            for otherCuby in other.cubies:
                cuby.calcIntersection(otherCuby, cuby.on, otherCuby.on)

        return BootStep(res)

    def doStep(self, s):
        #todo: calc number of on cubes instead
        xFrom = max(self.minX, s[0])
        xTo = min(self.maxX, s[1]) + 1

        yFrom = max(self.minY, s[2])
        yTo = min(self.maxY, s[3]) + 1

        zFrom = max(self.minZ, s[4])
        zTo = min(self.maxZ, s[5]) + 1

        on = True if s[6] else False

        for x in range(xFrom, xTo):
            for y in range(yFrom, yTo):
                for z in range(zFrom, zTo):
                    self.cubesOn[x][y][z] = on



def part01(input01):

    bootSequence = [getAllNumbersFromString(i) for i in input01]
    boat = Boat()

    for i,s in enumerate(bootSequence):
        if "on" in input01[i]:
            s.append(1)
        else:
            s.append(0)
        boat.doStep(s)

    return boat.numOn()

def part02(input02):
    bootSequence = [getAllNumbersFromString(i) for i in input02]

    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    minZ = 0
    maxZ = 0

    bootSteps = []

    for i, s in enumerate(bootSequence):
        minX = min(s[0], minX)
        maxX = max(s[1], maxX)

        minY = min(s[2], minY)
        maxY = max(s[3], maxY)

        minZ = min(s[4], minZ)
        maxZ = max(s[5], maxZ)

        if "on" in input02[i]:
            s.append(1)
        else:
            s.append(0)

        bootSteps.append(BootStep([Cubeoid(minX, maxX, minY, maxY, minZ, maxZ, s[6])]))

    print(reduce(lambda x, y: x.calcOverlap, bootSteps))


    return 1


class Cubeoid:
    def __init__(self, minX,maxX, minY, maxY, minZ, maxZ):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ

    def overlaps(self, other):

        if self.minX <= other.minX <= self.maxX:
            return True
        if self.minY <= other.minY <= self.maxY:
            return True
        if self.minZ <= other.minZ <= self.maxZ:
            return True
        if self.minX <= other.maxX <= self.maxX:
            return True
        if self.minY <= other.maxY <= self.maxY:
            return True
        if self.minZ <= other.maxZ <= self.maxZ:
            return True




pathDay = "day22"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 39:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput01 = readLinesFromFile("%s/input_test_01_2.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 590784:
    print("Test Part 01_1 successful")
else:
    print("Test Part 01_1 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_02.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == "bullshit":
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

start_time = time.time()
print("Solution Part 01:", part01(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
#print("Solution Part 02:", part02(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

