from screen import drawScreen
from spritesAll import screenTop, screenBot, allSpriteDict
from time import sleep

def splitIntoLines(string):
    output = []
    length = 52
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

def getExtraSpace(line):
    spaces = 52 - len(line)
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

def text(data, *therest):
    drawScreen(data)
    newString = turnIntoOneString(therest)
    lines = splitIntoLines(newString)
    for line in lines:
        extraSpace = getExtraSpace(line)
        print('| ' + line + extraSpace + ' |')
    print ('\\------------------------------------------------------/')
    input()

def worldText(data, *therest):
    drawOverworldText(data.player.xCo, data.player.yCo, data.environment.location.map)
    newString = turnIntoOneString(therest)
    lines = splitIntoLines(newString)
    for line in lines:
        extraSpace = getExtraSpace(line)
        print('| ' + line + extraSpace + ' |')
    print ('\\------------------------------------------------------/')
    input()

loading = 'LOADING...'
for i in range(len(loading)):
    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.05)

def drawOverworldText(x, y, location):
    screenDraw = screenTop + '\n'
    yAxis = 0
    for line in location:
        if yAxis > y-4 and yAxis < y+4:
            xAxis = 0
            for location in range(3):
                screenDraw += '|'
                for sprite in line:
                    if xAxis > x-5 and xAxis < x+5:
                        if [x, y] == [xAxis, yAxis]:
                            #youTile = overlayCharacterSprite(you[location], spriteDict[sprite][location], location)
                            #screenDraw += youTile
                            screenDraw += allSpriteDict["Y"][location]
                        else:
                            screenDraw += (allSpriteDict[sprite][location])
                    xAxis += 1
                screenDraw += '|\n'
                xAxis = 0
            location += 1
        yAxis += 1
        if yAxis == 18:
            screenDraw += '|------------------------------------------------------|'
            print(screenDraw)
