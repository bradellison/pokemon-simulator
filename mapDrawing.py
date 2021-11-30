import time
import colorama
from random import randint
from battleFunctions import startBattle
from spritesAll import screenTop, screenBot, allSpriteDict
from overworldFunctions import addLocationInformation, trainerBattle, wildBattle
from pokemonCentreFunctions import pokemonCenter
from text import worldText
from storyInteractionFunctions import talkGary, talkOak, starterBall, talkStarterRivalFight
from drawOverworld import drawOverworld
from menu import chooseFromMenu

def overlayCharacterSprite(you, sprite, location):
    if location == 1:
        youTile = sprite[:1] + you + sprite[-1:]
    else:
        youTile = sprite[:2] + you + sprite[-2:]
    return youTile

def actionChoice(data,x,y,location):
    newx = x
    newy = y
    choiceInput = (input('-- '))
    if choiceInput == '':
        choiceInput = data.player.lastDirection
    if choiceInput in ['w', 'a', 's', 'd', 'm', 'menu']:
        data.player.lastDirection = choiceInput
        if choiceInput == 'w':
            data.player.direction = "Up"
            newy -= 1
        elif choiceInput == 'a':
            data.player.direction = "Left"
            newx -= 1
        elif choiceInput == 's':
            data.player.direction = "Down"
            newy += 1
        elif choiceInput == 'd':
            data.player.direction = "Right"
            newx += 1
        elif choiceInput == "m" or choiceInput == "menu":
            return "Menu"
        if warpZone(data, newx, newy):
            return
        elif checkWall(data, newx, newy, location, choiceInput) or checkInteraction(data, newx, newy, location):
            return
        else:
            checkEnemyInteration(data, newx, newy)
            data.player.xCo = newx
            data.player.yCo = newy
            return


def checkWall(data,x,y,location,direction):
    if data.settings.settingsDict["WallClip"] == True:
        return False
    walls = ['@', '~', 'K', '[', ']', 'D', '{', '}', '_', 'b', 'w', 'W', 'm', 'M', 'c', '=', '-', 'r', 't', 'y', 'u', 'i', 'j', 'k', 'U', 'I', 'J', 'K', 'T', '(', ':', ')', '<', '$', 'h', 'B', 'L', 's']
    yAxis = 0
    for line in location:
        xAxis = 0
        for sprite in line:
            if [xAxis, yAxis] == [x,y]:
                if sprite in walls:
                    if sprite == '=' and direction != 'w':
                        return False
                    return True
                else:
                    return False
            xAxis += 1
        yAxis += 1

def checkInteraction(data,x,y,location):
    interactions = ['^', '0', '+', '*', 'q', 'O', 'Q', 'o', '?', 'R', 'S']
    yAxis = 0
    for line in location:
        xAxis = 0
        for sprite in line:
            if [xAxis, yAxis] == [x,y]:
                if sprite in interactions:
                    if sprite != '?':
                        runInteraction(data, sprite, xAxis, yAxis, location)
                        return True
                    else:
                        return checkStoryInteraction(data,x,y)
                else:
                    return False
            xAxis += 1
        yAxis += 1

def checkStoryInteraction(data,x,y):
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

def checkEnemyInteration(data, newX, newY):
    for enemy in data.environment.location.enemies:
        if [newX, newY] in enemy.aggroCoords:
            if enemy.battleComplete == False:
                enemy.battleReady = True
                data.environment.battleStart = True
                characterFound = True    
            return True

def runInteraction(data, sprite, newX, newY, location):
    if sprite == '^':
        talkGary(data)
    elif sprite == '0':
        talkOak(data)
    elif sprite == '*':
        checkEnemyInteration(data, newX, newY)
    elif sprite == 'O':
        starterBall(data, 'Bulbasaur')
    elif sprite == 'q':
        starterBall(data, 'Charmander')
    elif sprite == 'Q':
        starterBall(data, 'Squirtle')
    elif sprite == 'R':
        pokemonCenter(data, False)
    elif sprite == 'S':
        printSign(data, newX, newY)
        return True

def printSign(data, newX, newY):
    for sign in data.environment.location.signs:
        if sign.coords == [newX, newY]:
            worldText(data, sign.text)


def checkNewSprite(x,y,location):
    yAxis = 0
    for line in location:
        xAxis = 0
        for sprite in line:
            if [xAxis, yAxis] == [x,y]:
                return sprite
            xAxis += 1
        yAxis += 1   

def checkBattle(data, x, y, location):
    newSprite = checkNewSprite(x, y, location)
    if data.environment.battleStart == True:
        for enemy in data.environment.location.enemies:
            if enemy.battleReady == True:
                #print('X:', data.player.xCo, '- Y:', data.player.yCo, ' Region:', data.environment.location.name)
                input("--")
                trainerBattle(data, enemy)
                enemy.battleReady = False
                enemy.battleComplete = True
                data.environment.battleStart = False
                return True
    if not checkEnemyInteration(data, x, y):
        if newSprite == '%':
            if wildBattleChance(data):
                return True
    else:
        return False

def wildBattleChance(data):
    if randint(1,20) == 1:
        wildBattle(data)
        return True

def warpZone(data, newx, newy):
    for zone in data.environment.location.warpZones:
        if [newx, newy] == zone.warpSourceGrid:
            [data.player.xCo, data.player.yCo] = zone.warpTargetGrid
            addLocationInformation(data, zone.warpTargetLocation)
            return True



def overworldMovement(data):
    drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map)
    if checkBattle(data, data.player.xCo, data.player.yCo, data.environment.location.map):
        drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map)
    if data.settings.settingsDict["Show Co-Ords"]:
        print('X:', data.player.xCo, '- Y:', data.player.yCo, ' Region:', data.environment.location.name)
    action = actionChoice(data, data.player.xCo, data.player.yCo, data.environment.location.map)
    while action == "Menu":
        drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map, text=False, menu=True)
        action = chooseFromMenu(data)


