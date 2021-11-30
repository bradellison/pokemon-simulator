from os import statvfs_result
import math
from spritesAll import screenBot, screenEmp


def splitIntoLines(string, length):
    output = []
    lastSpace = length + 1
    firstCount = 0
    while firstCount == 0:
        lastSpace = length
        if len(string) > length:
            secondCount = 0
            while secondCount == 0:
                endCharacter = string[lastSpace]
                if endCharacter == ' ':
                    output.append(string[:lastSpace])
                    string = string[lastSpace + 1:]
                    secondCount += 1
                else:
                    lastSpace -= 1
        else:
            output.append(string)
            return output

def getExtraSpace(line, totalSpaceAvialable):
    spaces = totalSpaceAvialable - len(line)
    extraSpace = ''
    for _ in range(spaces):
        extraSpace += ' '
    return extraSpace

def turnIntoOneString(therest):
    results = [] 
    for t in therest: 
        t = str(t)
        for x in t: 
            results.append(x)
        results.append(' ') 
    totalString = ''
    count = 0
    for string in results:
        if count == 0:
            totalString += str(string)
            count += 1
        else:
            totalString += str(string)
    return (totalString[:-1])

def printWithScreenSides(toPrint):
    print("┃" + toPrint + "┃")

def printWithScreenSidesAndSpacing(toPrint):
    print("┃ " + toPrint + " ┃")

def onlyTextBox(string, pauseAfter=False):
    length = 0
    newString = turnIntoOneString(string)
    lines = splitIntoLines(string, 52)
    for line in lines:
        extraSpace = getExtraSpace(line, 52)
        print('┃ ' + line + extraSpace + ' ┃')
        length += 1
    count = 1
    line = ""
    for _ in range(3 - length):
        print(screenEmp)
    print(screenBot)
    if pauseAfter:
        input()

def onlyTextBoxWithOptions(string, options, backWithE=False):
    length = 0
    newString = turnIntoOneString(string)
    lines = splitIntoLines(string, 52)
    for line in lines:
        extraSpace = getExtraSpace(line, 52)
        print('┃ ' + line + extraSpace + ' ┃')
        length += 1
    count = 1
    line = ""
    for option in options:
        line += str(count) + " - " + option
        if count % 2 == 0:
            line += getExtraSpace(line,52)
            printWithScreenSidesAndSpacing(line)
            length += 1
            line = ""
        else:
            line += getExtraSpace(line, 27)
        count += 1
    if line != "" and options != []:
        line += getExtraSpace(line,52)
        printWithScreenSidesAndSpacing(line)
    if backWithE:
        line = "e - Back"
        line += getExtraSpace(line, 52)
        printWithScreenSidesAndSpacing(line)
        length += 1
    for _ in range(3 - length):
        print(screenEmp)
    print(screenBot)
        

def drawBar(currentValue, maxValue, barCount, barString="=", finalBarDifferent=False, finalBarString=">"):
    if currentValue == 0 and maxValue == 0:
        currentValue = 1
        maxValue = 1
    valuePerSpace = (maxValue / barCount)
    spacesFilled = math.ceil(currentValue / valuePerSpace)
    if spacesFilled > barCount:
        spacesFilled = barCount
    bar = ''
    spareSpaces = barCount
    for i in range (spacesFilled):
        if i == spacesFilled - 1 and finalBarDifferent == True:
            bar += finalBarString
        else:
            bar += barString
        spareSpaces -= 1
    for _ in range (spareSpaces):
        bar += ' '
    return bar

