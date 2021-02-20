import time
import colorama
from gameMaps import routeOneMap, palletTownMap
from environmentSprites import screenTop, screenBot, spriteDict, you

x = 10
y = 7
playerLocation = [x,y]

def drawOverworld(x, y, location):
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
                            screenDraw += you[location]
                        else:
                            screenDraw += (spriteDict[sprite][location])
                    xAxis += 1
                screenDraw += '|\n'
                xAxis = 0
            location += 1
        yAxis += 1
    screenDraw += screenBot
    print(screenDraw)

def directionChoice(x,y,location):
    newx = x
    newy = y
    while True:
        try:
            choiceInput = (input('-- '))
            if choiceInput == 'w':
                newy -= 1
            elif choiceInput == 'a':
                newx -= 1
            elif choiceInput == 's':
                newy += 1
            elif choiceInput == 'd':
                newx += 1
            if checkWall(newx, newy, location):
                return [newx, newy]
            else:
                return [x, y]
        except ValueError:
            print('Please choose an option!')

def checkWall(x,y,location):
    walls = ['@', '~', 'K', '[', ']', 'D', 'R', 'b', 'S']
    yAxis = 0
    for line in location:
        xAxis = 0
        for sprite in line:
            if [xAxis, yAxis] == [x,y]:
                if sprite in walls:
                    return False
                else:
                    return True
            xAxis += 1
        yAxis += 1

def checkNewSprite(x,y,location):
    yAxis = 0
    for line in location:
        xAxis = 0
        for sprite in line:
            if [xAxis, yAxis] == [x,y]:
                return sprite
            xAxis += 1
        yAxis += 1   

