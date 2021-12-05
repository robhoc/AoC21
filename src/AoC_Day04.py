from lib import *


class BingoBoard:
    def __init__(self):
        self.board = []
        self.tipps = []

    def appendLine(self,line):
        line = line.strip().replace('  ', ' ')
        boardLine = list(map(int, line.split(' ')))
        self.board.append(boardLine)
        self.tipps.append(len(boardLine)*[False])

    def playNumber(self, number):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == number:
                    self.tipps[i][j] = True

    def hasWon(self):
        # lines
        for tippLine in self.tipps:
            if len(list(filter(lambda x: x is False, tippLine))) == 0:
                return True

        # columns
        length = len(self.tipps[0])
        for column in range(length):
            won = True
            for line in self.tipps:
                if not line[column]:
                    won = False
                    break
            if won:
                return True
        return False

    def getWinningValue(self):
        #sum of all unmarked
        summe = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if not self.tipps[i][j]:
                    summe = summe + self.board[i][j]
        return summe


def part01(input01):

    guesses = list(map(int,input01[0].split(',')))
    boards = []
    currentBoard = ''

    #init boards
    for i, line in enumerate(input01):
        if i == 0:
            continue
        elif line == '':
            if currentBoard != '':
                boards.append(currentBoard)
            currentBoard = BingoBoard()
        else:
            currentBoard.appendLine(line)

    #ooops
    boards.append(currentBoard)

    #determine winning board
    for guess in guesses:
        for board in boards:
            board.playNumber(guess)
            if board.hasWon():
                return guess * board.getWinningValue()
    return "error"

def part02(input01):

    guesses = list(map(int,input01[0].split(',')))
    boards = []
    currentBoard = ''

    #init boards
    for i, line in enumerate(input01):
        if i == 0:
            continue
        elif line == '':
            if currentBoard != '':
                boards.append(currentBoard)
            currentBoard = BingoBoard()
        else:
            currentBoard.appendLine(line)

    #ooops
    boards.append(currentBoard)

    #determine winning board
    for guess in guesses:
        print('guessing', guess)
        for board in boards:
            board.playNumber(guess)
        for board in boards:
            if board.hasWon():
                if len(boards) == 1:
                    return guess * board.getWinningValue()
                else:
                    boards.remove(board)
    return "error"



testInput01 = readLinesFromFile("day04/input_test_01.txt")
testResult01 = part01(testInput01)
if testResult01 == 4512:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("day04/input_test_01.txt")
testResult02 = part02(testInput01)
if testResult02 == 1924:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("day04/input.txt")

print("Solution Part 01:", part01(inputAsArray))

print("Solution Part 02:", part02(inputAsArray))


