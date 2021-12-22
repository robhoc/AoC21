from lib import *
from functools import reduce
import time

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
            self.costs = []
            for i in range(self.LINES):
                self.costs.append(self.COLUMNS * [False])

        def inBoundsLine(self, iLine):
            return 0 <= iLine < self.LINES

        def inBoundsColumn(self, iColumn):
            return 0 <= iColumn < self.COLUMNS


def part01(input01):
    print(input01)
    scoreP1 = 0
    scoreP2 = 0

    #fields sind von 1-10, ich will 0-9
    fieldP1 = input01[0] - 1
    fieldP2 = input01[1] - 1

    numDiceRolls = 0
    lastRoll = 0

    while scoreP1 < 1000 and scoreP2 < 1000:

        #Player 1
        numDiceRolls = numDiceRolls + 3
        roll = lastRoll + 1 + lastRoll + 2 + lastRoll + 3
        lastRoll = lastRoll + 3

        fieldP1 = (fieldP1 + roll) % 10

        # +1 wegen 0-9 statt 1-10
        scoreP1 = scoreP1 + fieldP1 + 1

        if scoreP1 >= 1000:
            break

        #Player 2
        numDiceRolls = numDiceRolls + 3
        roll = lastRoll + 1 + lastRoll + 2 + lastRoll + 3
        lastRoll = lastRoll + 3

        fieldP2 = (fieldP2 + roll) % 10

        #+1 wegen 0-9 statt 1-10
        scoreP2 = scoreP2 + fieldP2 + 1

    if scoreP1 >= 1000:
        return scoreP2 * numDiceRolls
    else:
        return scoreP1 * numDiceRolls


class GameRound:
    def __init__(self, startP1, startP2):
        self.parent = None
        self.currentPlayer = 1

        self.rolledInTurn = 0
        self.rolledTotal = 0

        self.fieldP1 = startP1
        self.fieldP2 = startP2

        self.scoreP1 = 0
        self.scoreP2 = 0

    def setParent(self, game):
        self.currentPlayer = game.currentPlayer
        self.rolledInTurn = game.rolledInTurn
        self.fieldP1 = game.fieldP1
        self.fieldP2 = game.fieldP2
        self.scoreP1 = game.scoreP1
        self.scoreP2 = game.scoreP2

    def play(self):

        p1wins = 0
        p2wins = 0
        if self.scoreP1 >= 21:
            return 1, 0
        if self.scoreP2 >= 21:
            return 0, 1

        game1 = GameRound(self.fieldP1, self.fieldP2)
        game1.setParent(self)
        game1.endRollAndCalcScores(1)
        (p1, p2) = game1.play()
        p1wins = p1 + p1wins
        p2wins = p2 + p2wins

        game2 = GameRound(self.fieldP1, self.fieldP2)
        game2.setParent(self)
        game2.endRollAndCalcScores(2)
        (p1, p2) = game2.play()
        p1wins = p1 + p1wins
        p2wins = p2 + p2wins

        game3 = GameRound(self.fieldP1, self.fieldP2)
        game3.setParent(self)
        game3.endRollAndCalcScores(3)
        (p1, p2) = game3.play()
        p1wins = p1 + p1wins
        p2wins = p2 + p2wins

        return p1wins, p2wins

    def endRollAndCalcScores(self, roll):

        if self.currentPlayer == 1:
            self.fieldP1 = (self.fieldP1 + roll) % 10
        else:
            self.fieldP2 = (self.fieldP2 + roll) % 10

        self.rolledInTurn = self.rolledInTurn + 1

        if self.rolledInTurn == 3:
            self.rolledInTurn = 0
            if self.currentPlayer == 1:
                self.scoreP1 = self.scoreP1 + self.fieldP1 + 1
            else:
                self.scoreP2 = self.scoreP2 + self.fieldP2 + 1
            self.currentPlayer = (self.currentPlayer + 1) % 2


class Game2:
    def __init__(self):
        self.memo = {}
        self.first =True

    def play(self, fieldP1, fieldP2, numRolls, scoreP1, scoreP2, current, roll):

        if str(fieldP1)+'#'+str(fieldP2)+'#'+str(numRolls)+'#'+str(scoreP1)+'#'+str(scoreP2)+'#'+str(current)+'#'+str(roll) in self.memo:
            return self.memo[str(fieldP1)+'#'+str(fieldP2)+'#'+str(numRolls)+'#'+str(scoreP1)+'#'+str(scoreP2)+'#'+str(current)+'#'+str(roll)]

        #print(scoreP1, scoreP2)

        nextFieldP1 = fieldP1
        nextFieldP2 = fieldP2
        nextScoreP1 = scoreP1
        nextScoreP2 = scoreP2
        nextCurrent = current

        p1wins = 0
        p2wins = 0

        if current == 1:
            nextFieldP1 = (fieldP1 + roll) % 10
        else:
            nextFieldP2 = (fieldP2 + roll) % 10

        nextNumRolls = numRolls + 1

        if nextNumRolls == 3:
            nextNumRolls = 0
            if current == 1:
                nextScoreP1 = scoreP1 + nextFieldP1 + 1
            else:
                nextScoreP2 = scoreP2 + nextFieldP2 + 1
            nextCurrent = 1 if current == 2 else 2

        if nextScoreP1 >= 21:
            return 1, 0
        if nextScoreP2 >= 21:
            return 0, 1

        p1, p2 = self.play(nextFieldP1, nextFieldP2, nextNumRolls, nextScoreP1, nextScoreP2, nextCurrent, 1)
        p1wins = p1wins + p1
        p2wins = p2wins + p2

        p1, p2 = self.play(nextFieldP1, nextFieldP2, nextNumRolls, nextScoreP1, nextScoreP2, nextCurrent, 2)
        p1wins = p1wins + p1
        p2wins = p2wins + p2

        p1, p2 = self.play(nextFieldP1, nextFieldP2, nextNumRolls, nextScoreP1, nextScoreP2, nextCurrent, 3)
        p1wins = p1wins + p1
        p2wins = p2wins + p2

        self.memo[str(fieldP1)+'#'+str(fieldP2)+'#'+str(numRolls)+'#'+str(scoreP1)+'#'+str(scoreP2)+'#'+str(current)+'#'+str(roll)] = (p1wins, p2wins)
        return p1wins, p2wins


def part02(input02):

    #game = GameRound(input02[0], input02[1])

    game = Game2()

    res1 = 0
    res2 = 0

    r1, r2 = game.play(input02[0]-1, input02[1]-1, 0, 0, 0, 1, 1)
    res1 = res1 + r1
    res2 = res2 + r2

    r1, r2 = game.play(input02[0]-1, input02[1]-1, 0, 0, 0, 1, 2)
    res1 = res1 + r1
    res2 = res2 + r2

    r1, r2 = game.play(input02[0]-1, input02[1]-1, 0, 0, 0, 1, 3)
    res1 = res1 + r1
    res2 = res2 + r2

    return max(res1, res2)


pathDay = "day21"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01([4, 8])
if testResult01 == 739785:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_02.txt" % pathDay)
testResult02 = part02([4, 8])
if testResult02 == 444356092776315:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

start_time = time.time()
#print("Solution Part 01:", part01([9, 4]))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print("Solution Part 02:", part02([9, 4]))
print("--- %s seconds ---" % (time.time() - start_time))

