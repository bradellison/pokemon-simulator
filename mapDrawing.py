import time
import colorama
from random import randint
from gameMaps import routeOneMap, palletTownMap
from environmentSprites import screenTop, screenBot, spriteDict, you
from overworldFunctions import addLocationInformation, wildBattle
from pokemonCentreFunctions import pokemonCenter
from text import worldText
from storyInteractionFunctions import talkGary, talkOak, starterBall, talkStarterRivalFight

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
            if choiceInput == '':
                choiceInput = data.player.lastDirection
            if choiceInput in ['w', 'a', 's', 'd']:
                data.player.lastDirection = choiceInput
                if choiceInput == 'w':
                    newy -= 1
                elif choiceInput == 'a':
                    newx -= 1
                elif choiceInput == 's':
                    newy += 1
                elif choiceInput == 'd':
                    newx += 1
                if checkWall(newx, newy, location, choiceInput) or checkInteraction(data, newx, newy, location):
                    return
                else:
                    data.player.xCo = newx
                    data.player.yCo = newy
                    return
        except ValueError:
            print('Please choose an option!')

def checkWall(x,y,location,direction):
    walls = ['@', '~', 'K', '[', ']', '{', '}', '_', 'b', 'w', 'W', 'm', 'M', 'c', '=', 'r', 't', 'y', 'u', 'i', 'j', 'k', 'U', 'I', 'J', 'K', 'T']
    yAxis = 0
    for line in location:
        xAxis = 0
        for sprite in line:
            if [xAxis, yAxis] == [x,y]:
                if sprite in walls:
                    if sprite == '=' and direction == 's':
                        return False
                    return True
                else:
                    return False
            xAxis += 1
        yAxis += 1

def checkInteraction(data,x,y,location):
    interactions = ['^', '0', 'q', 'O', 'Q', 'o', '?', 'R']
    yAxis = 0
    for line in location:
        xAxis = 0
        for sprite in line:
            if [xAxis, yAxis] == [x,y]:
                if sprite in interactions:
                    if sprite != '?':
                        runInteraction(data, sprite, x, y, location)
                        return True
                    else:
                        return checkStoryInteraction(data,x,y)
                else:
                    return False
            xAxis += 1
        yAxis += 1

def checkStoryInteraction(data,x,y):
    print(data.environment.location)
    if data.environment.location.name == 'Pallet Town':
        if data.story.startPokemonChosen == False:
            worldText(data, 'You shouldn\'t go into tall grass without a Pokemon!')
            return True
        else:
            return False
    elif data.environment.location.name == 'Oak Lab':
        if data.story.startPokemonChosen == True and data.story.starterRivalFightCompleted == False:
            talkStarterRivalFight(data)
            return False
        else:
            return False
    else:
        return False

def runInteraction(data, sprite, x, y, location):
    if sprite == '^':
        talkGary(data)
    elif sprite == '0':
        talkOak(data)
    elif sprite == 'O':
        starterBall(data, 'Bulbasaur')
    elif sprite == 'q':
        starterBall(data, 'Charmander')
    elif sprite == 'Q':
        starterBall(data, 'Squirtle')
    elif sprite == 'R':
        pokemonCenter(data, False)

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
        if wildBattleChance(data):
            return True
    warpSprites = ['!', 'D', 'd']
    if newSprite in warpSprites:
        warpZone(data)
        return True      
    if newSprite == 'S':
        pokemonCenter(data, False)
        addLocationInformation(data, data.environment.location.name)
        return True

def wildBattleChance(data):
    if randint(1,20) == 1:
        wildBattle(data)
        return True

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


