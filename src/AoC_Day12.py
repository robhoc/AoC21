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
    def __init__(self, nodes):
        self.nodeList = nodes
        self.paths = []
        self.paths = { "end": 1 }

    def add(self, node):
        if node[0].isupper():
            print('Upper Case', node)
            #return

        start = node[0]
        end = node[1]

        if start in self.paths:
            self.paths[start] = self.paths[start] + self.paths[end]
        else:
            self.paths[start] = self.paths[end]

def part01(input01):
    graph = Graph(list(map(lambda x: x.split('-'), input01)))

    startAt = 'end'
    nextNodes = list(filter(lambda x: x[0] == startAt or x[1] == startAt, graph.nodeList))

    for node in nextNodes:
        graph.add(node)

    while True:
        #not a direct#ed graph.
        lastStarts = list(map(lambda x: x[0], nextNodes))
        if lastStarts == ['start']:
            break
        nextNodes = list(filter(lambda x: x[1] in lastStarts, graph.nodeList))
        for node in nextNodes:
            graph.add(node)
    return graph.paths['start']

def part02(input02):
    print("Todo")
    return "todo"


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

testInput02 = readLinesFromFile("%s/input_test_03.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == "bullshit":
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

#print("Solution Part 01:", part01(inputAsArray))

#print("Solution Part 02:", part02(inputAsArray))


