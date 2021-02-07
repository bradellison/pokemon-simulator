import time
import colorama
from random import randint
from gameMaps import routeOneMap, palletTownMap
from environmentSprites import screenTop, screenBot, spriteDict, you
from overworldFunctions import addLocationInformation, wildBattle
from pokemonCentreFunctions import pokemonCenter

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
                            #youTile = overlayCharacterSprite(you[location], spriteDict[sprite][location], location)
                            #screenDraw += youTile
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

def overlayCharacterSprite(you, sprite, location):
    if location == 1:
        youTile = sprite[:1] + you + sprite[-1:]
    else:
        youTile = sprite[:2] + you + sprite[-2:]
    return youTile


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
            if checkWall(newx, newy, location):
                return
            else:
                data.player.xCo = newx
                data.player.yCo = newy
                return
        except ValueError:
            print('Please choose an option!')

def checkWall(x,y,location):
    walls = ['@', '~', 'K', '[', ']', 'D', '{', '}', '_', 'b']
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

def checkAction(data, x, y, location):
    newSprite = checkNewSprite(x, y, location)
    if newSprite == '%':
        wildBattleChance(data)
    if newSprite == '!':
        warpZone(data)
        return True
    if newSprite == 'S':
        pokemonCenter(data, False)
        addLocationInformation(data, data.environment.location.name)
        return True

def wildBattleChance(data):
    if randint(1,20) == 1:
        wildBattle(data)

def warpZone(data):
    for zone in data.environment.location.warpZones:
        if [data.player.xCo, data.player.yCo] == zone.warpSourceGrid:
            [data.player.xCo, data.player.yCo] = zone.warpTargetGrid
            addLocationInformation(data, zone.warpTargetLocation)



def overworldMovement(data):
    drawOverworld(data.player.xCo, data.player.yCo, data.environment.location.map)
    if checkAction(data, data.player.xCo, data.player.yCo, data.environment.location.map):
        drawOverworld(data.player.xCo, data.player.yCo, data.environment.location.map)
    print('X:', data.player.xCo, '- Y:', data.player.yCo, ' Region:', data.environment.location.name)
    directionChoice(data, data.player.xCo, data.player.yCo, data.environment.location.map)


