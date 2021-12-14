from lib import *
from functools import reduce

class Board:
    def __init__(self, boardLines):
        self.boardLines = []
        self.LINES = len(boardLines)
        self.COLUMNS = len(boardLines[0])
        self.visited = []
        for line in boardLines:
            self.boardLines.append(list(map(int, list(line))))
            #self.boardLines.append(list(line))
            #self.boardLines.append(line)

        def resetVisited(self):
            self.visited = []
            for i in range(self.LINES):
                self.visited.append(self.COLUMNS * [False])


class Graph:
    def __init__(self):
        self.connections = {}
        self.visitedLower = []

    def add(self, edge):
        first = edge[0]
        second = edge[1]

        if first in self.connections:
            self.connections[first].append(second)
        else:
            self.connections[first] = [second]

        if second in self.connections:
            self.connections[second].append(first)
        else:
            self.connections[second] = [first]

    def solve(self):
        self.visitedLower = ['start']
        return self.findNumberOfPaths('start')

    def findNumberOfPaths(self, currentNode):
        if currentNode == 'end':
            return 1

        count = 0
        for node in self.connections[currentNode]:
            if node in self.visitedLower:
                continue
            if not node.isupper():
                self.visitedLower.append(node)
            count = count + self.findNumberOfPaths(node)
            if not node.isupper():
                self.visitedLower.remove(node)
        return count

def part01(input01):
    graph = Graph()

    connections = list(map(lambda x: x.split('-'), input01))
    for edge in connections:
        graph.add(edge)

    return graph.solve()

def part02(input02):
    graph = Graph()

    connections = list(map(lambda x: x.split('-'), input02))
    for edge in connections:
        graph.add(edge)

    return graph.solve()


pathDay = "day12"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 10:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

#testInput01 = readLinesFromFile("%s/input_test_02.txt" % pathDay)
#testResult01 = part01(testInput01)
#if testResult01 == 226:
#    print("Test Part 01.2 successful")
#else:
#    print("Test Part 01.2 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 36:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

print("Solution Part 01:", part01(inputAsArray))

#print("Solution Part 02:", part02(inputAsArray))


