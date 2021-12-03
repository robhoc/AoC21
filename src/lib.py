import re


def readLines(textData):
    lines = []
    for line in textData.splitlines():
        lines.append(line)
    return lines

def readLinesFromFileAsChars(filename):
    file = open(filename)
    lines = file.read()
    file.close()
    return list(map(split, readLines(lines)))

def split(word):
    return [char for char in word]

def readLinesFromFile(filename):
    file = open(filename)
    lines = file.read()
    file.close()
    return readLines(lines)

def forceAsInt(string):
    return int(string)

def getNumbersFromString(string):
    return int(re.findall("-?\d+", string)[0])

def doesStringStartWithString(fullString,searchTerm):
    pattern = '\A'+searchTerm
    match = re.match(pattern, fullString)
    if match:
        return True
    return False
