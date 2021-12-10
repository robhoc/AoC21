from math import ceil

from lib import *
from functools import reduce


def getClosing(c):
    if c == '(':
        return ')'
    if c == '[':
        return ']'
    if c == '{':
        return '}'
    if c == '<':
        return '>'


def getScore(c):
    if c == ')':
        return 3
    if c == ']':
        return 57
    if c == '}':
        return 1197
    if c == '>':
        return 25137


def getScore2(c):
    if c == ')':
        return 1
    if c == ']':
        return 2
    if c == '}':
        return 3
    if c == '>':
        return 4

def part01(input01):

    closing = [')', '>', ']', '}']

    stack = []
    corruptionScore = 0

    for line in input01:
        stack = []
        for c in list(line):
            if c in closing:
                if c != stack.pop():
                    #corrupted
                    corruptionScore = corruptionScore + getScore(c)
            else:
                stack.append(getClosing(c))
    return corruptionScore



def part02(input02):

    closing = [')', '>', ']', '}']

    scores = []

    for line in input02:
        stack = []
        for idx, c in enumerate(list(line)):
            if c in closing:
                if c != stack.pop():
                    #corrupted
                    break
            else:
                stack.append(getClosing(c))
            if idx == len(line) - 1:
                score = 0
                for i in range(len(stack)):
                    missingChar = stack.pop()
                    score = score * 5
                    score = score + getScore2(missingChar)
                scores.append(score)
    length = len(scores) - 1
    scores = sorted(scores)
    return scores[ceil(length/2)]


pathDay = "day10"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 26397:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult02 = part02(testInput01)
if testResult02 == 288957:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


