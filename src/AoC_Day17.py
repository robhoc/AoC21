from lib import *
from functools import reduce
import time


def calcNextPos(pos):

    currentX = pos[0]
    currentY = pos[1]
    currentVx = pos[2]
    currentVy = pos[3]

    nextX = currentX + currentVx
    nextY = currentY + currentVy
    nextVx = currentVx

    if currentVx > 0:
        nextVx = currentVx - 1
    elif currentVx < 0:
        nextVx = currentVx + 1

    return [nextX, nextY, nextVx, currentVy-1]

def getYForNumberOfSteps(initialVy, numSteps):
    currentY = 0
    currentVy = initialVy

    for i in range(numSteps):
        currentY = currentY + currentVy
        currentVy = currentVy - 1
    return currentY



class Shot:
    def __init__(self, target):
        self.Tx1 = target[0]
        self.Tx2 = target[1]
        self.Ty1 = target[2]
        self.Ty2 = target[3]

    def isInTargetYAfterSteps(self, intialVy, steps):
        y = getYForNumberOfSteps(intialVy, steps)
        return self.Ty2 <= y <= self.Ty1

    def getAllXForNumSteps(self, steps):
        result = []
        for x in range(self.Tx2 + 2):
            if self.isInTargetXAfterSteps(x, steps):
                result.append(x)
        return result

    def isInTargetXAfterSteps(self, Vx, steps):
        currentX = 0
        currentVx = Vx
        if currentVx == 0:
            return False
        for i in range(steps):
            currentX = currentX + currentVx
            currentVx = currentVx - 1
            if currentVx == 0:
                break
        if self.Tx1 <= currentX <= self.Tx2:
            return True


def part01(input01):

    # 5671 as my target Y is below 0, the probe will be hitting 0 after some step with exactly initial Velocity plus
    # 1 So maximum initial Vy is the lower end of the target area. That yields a highest point of Vy * (Vy + 1) / 2
    # as the sum of all the integers up to initial Vy
    Vy = input01[3]
    return Vy * (Vy+1) / 2

def part02(input02):
    print(input02)
    Tx1 = input02[0]
    Tx2 = input02[1]
    Ty1 = input02[2]
    Ty2 = input02[3]

    results = set()
    shot = Shot(input02)

    minY = 0

    #1 step
    for i in range(Tx1, Tx2 + 1):
        for j in range(Ty2, Ty1 + 1):
            if shot.isInTargetYAfterSteps(j, 1):
                results.add((i, j))
                if j < minY:
                    minY = j
    print('step 1 res',results, len(results))


    print('all 1', shot.getAllXForNumSteps(1))
    for steps in range(2, 2*abs(Ty2)+2):
        print('all',steps , shot.getAllXForNumSteps(steps))

    #n > 1 steps
    for steps in range(2, 2*abs(Ty2)+2):
        allY = {}
        print('res nach steps:', steps, results)

        for initialVy in range(Ty2-1, int((Ty2 * (Ty2+1) / 2)) + 5):
            if shot.isInTargetYAfterSteps(initialVy, steps):
                for x in shot.getAllXForNumSteps(steps):
                    results.add((x, initialVy))
                #if initialVy < nextMinY:
                #    nextMinY = initialVy
        #minY = nextMinY


    print(results)
    print(len(results))
    return len(results)


pathDay = "day17"
testResult01 = part01([20, 30, -5, -10])
if testResult01 == 45:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testResult02 = part02([20, 30, -5, -10])
if testResult02 == 112:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = [230, 283, -57, -107]

start_time = time.time()
print("Solution Part 01:", part01(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print("Solution Part 02:", part02(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

