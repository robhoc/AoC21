from lib import *
from functools import reduce
import time


def part01(input01):
    algo = input01[0]
    image = input01[2:]

    image1 = doPart01(algo, image, str(0))
    image2 = doPart01(algo, image1, str(1))

    count = 0
    for i in image2:
        print(i)
        count = count +i.count('#')

    return count



def doPart01(algo, image, default):
    for line in image:
        print(line)
    print('\n')
    converted = []
    for i in range(-2, len(image)+3):
        converted.append('')
        for j in range(-2, len(image[0])+3):
            location = ''
            #print('current', i, j)
            for line in range(i-1, i+2):
                for column in range(j-1, j+2):
                    # print('zeile, spalte', line, column)
                    if line < 0 or column < 0 or line > len(image)-1 or column > len(image[0]) - 1:
                        location = location + default
                    else:
                        location = location + (str(1) if image[line][column] == '#' else str(0))
            converted[i+2] = converted[i+2] + algo[int(location, 2)]

    for c in converted:
        print(c)
    print('\n')
    return converted

def part02(input02):
    algo = input02[0]
    image = input02[2:]
    for i in range(25):
        image = doPart01(algo, image, str(0))
        image = doPart01(algo, image, str(1))

    count = 0
    for i in image:
        count = count + i.count('#')

    return count


pathDay = "day20"
testInput01 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult01 = part01(testInput01)
if testResult01 == 35:
    print("Test Part 01 successful")
else:
    print("Test Part 01 failed, returned", testResult01)

testInput02 = readLinesFromFile("%s/input_test_01.txt" % pathDay)
testResult02 = part02(testInput02)
if testResult02 == 3351:
    print("Test Part 02 successful")
else:
    print("Test Part 02 failed, returned", testResult02)


inputAsArray = readLinesFromFile("%s/input.txt" % pathDay)

start_time = time.time()
print("Solution Part 01:", part01(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print("Solution Part 02:", part02(inputAsArray))
print("--- %s seconds ---" % (time.time() - start_time))

