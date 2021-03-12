import time
import colorama
from gameMaps import routeOneMap, palletTownMap
from environmentSprites import screenTop, screenBot, spriteDict, you

x = 10
y = 7
playerLocation = [x,y]

def drawOverworld(x, y, location):
    print(screenTop)
    yAxis = 0
    for line in location:
        if yAxis > y-4 and yAxis < y+4:
            xAxis = 0
            for location in range(3):
                currentLineDraw = '|'
                for sprite in line:
                    if xAxis > x-5 and xAxis < x+5:
                        if [x, y] == [xAxis, yAxis]:
                            currentLineDraw += you[location]
                        else:
                            currentLineDraw += (spriteDict[sprite][location])
                    xAxis += 1
                currentLineDraw += '|'
                xAxis = 0
                print(currentLineDraw)
            location += 1
        yAxis += 1
    print(screenBot)

def directionChoice(data,x,y,location):
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
            elif commands(data, choiceInput):
                return
            if checkWall(newx, newy, location):
                data.xCo = newx
                data.yCo = newy
                return
            else:
                return
        except ValueError:
            print('Please choose an option!')

def commands(data, choiceInput):


def cheatCodes(data, choiceInput):
    if choiceInput == 'col':
        data.colorama = False


def checkWall(x,y,location):
    walls = ['@', '~', 'K', '[', ']', 'D', 'R']
    yAxis = 0
    for line in location:
        xAxis = 0
        for sprite in line:
            if [xAxis, yAxis] == [x,y]:
                if sprite in walls:
                    return True
                else:
                    return False
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

def checkAction(x, y, location):
    newSprite = checkNewSprite(x, y, location)
    if newSprite == '%':
        print('WILD BATTLE')
    if newSprite == '!':
        print('WARP')

def overworldMovement(data):
    drawOverworld(data.player.xCo, data.player.yCo, data.environment.map)
    checkAction(data.player.xCo, data.player.yCo, data.environment.map)
    directionChoice(data, x, y, palletTownMap)

