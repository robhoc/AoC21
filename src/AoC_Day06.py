from lib import *
from functools import reduce

class Game:
    def __init__(self, initial):
        self.fishes = 9*[0]
        for timer in initial:
            self.fishes[timer] = self.fishes[timer] + 1

    def evolve(self):
        nextTick = (9*[0])
        for i,fish in enumerate(self.fishes):
            if i == 0:
                nextTick[8] = self.fishes[0]
                nextTick[6] = self.fishes[0]
            else:
                nextTick[i-1] = nextTick[i-1] + self.fishes[i]

        self.fishes = nextTick

    def count(self):
        return reduce(lambda x, y: x+y, self.fishes)


def part01(input01):
    game = Game(getAllNumbersFromString(input01[0]))
    for i in range(1,81):
        game.evolve()
    return game.count()

def part02(input02):
    game = Game(getAllNumbersFromString(input02[0]))
    for i in range(1,257):
        game.evolve()
    return game.count()

testInput01 = readLinesFromFile("day06/input_test_01.txt")
testResult01 = part01(testInput01)
if testResult01 == 5934:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("day06/input_test_01.txt")
testResult02 = part02(testInput01)
if testResult02 == 26984457539:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("day06/input.txt")

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


