import math
import random
from random import randint 
from pokemonDictionaries import pokemonSprites

class BattleScreen(object):
    def __init__(self):
        self.healthBarPlayer = ''
        self.healthBarEnemy = ''
        self.extraSpaceHealthPlayer = ''
        self.nameBarPlayer = ''
        self.nameBarEnemy = ''
        self.playerStatus = '   '
        self.enemyStatus = '   '

def drawNameBarPlayer(name, level):
    nameLength = len(name)
    spaceRequiredName = 10 - nameLength
    extraSpaceName = ''
    for _ in range (spaceRequiredName):
        extraSpaceName += ' '
    levelLength = len(str(level))
    spaceRequiredLevel = 3 - levelLength
    extraSpaceLevel = ''
    for _  in range (spaceRequiredLevel):
        extraSpaceLevel += ' '
    return (name + ' - Lv' + str(level) + extraSpaceName + extraSpaceLevel)

def drawNameBarEnemy(name, level):
    nameLength = len(name)
    spaceRequiredName = 10 - nameLength
    extraSpaceName = ''
    for _ in range (spaceRequiredName):
        extraSpaceName += ' '
    levelLength = len(str(level))
    spaceRequiredLevel = 3 - levelLength
    extraSpaceLevel = ''
    for _  in range (spaceRequiredLevel):
        extraSpaceLevel += ' '
    return (extraSpaceName + extraSpaceLevel + name + ' - Lv' + str(level))

def drawHealthBar(health, maxHealth):
    healthPerSpace = (maxHealth / 20)
    spacesFilled = math.ceil(health / healthPerSpace)
    healthBar = ''
    spareSpaces = 20
    for _ in range (spacesFilled):
        healthBar += '='
        spareSpaces -= 1
    for _ in range (spareSpaces):
        healthBar += ' '
    healthInDigits = len(str(health)) + len(str(maxHealth))
    spaceNeeded = 10 - healthInDigits
    extraSpace = ''
    for _ in range (spaceNeeded):
        extraSpace += ' '
    return [healthBar, extraSpace]

def getStatusBar(pokemon):
    statusDict = {0:'   ',1:'BRN',2:'PAR',3:'SLP',4:'FRZ',5:'PSN',6:'PSN'}
    return statusDict[pokemon.nvStatus]

def getBattleScreenValues(data):
    playerOutcomes = (drawHealthBar(data.player.pokemon.hp, data.player.pokemon.maxhp))
    data.bscreen.healthBarPlayer = playerOutcomes[0]
    data.bscreen.extraSpaceHealthPlayer = playerOutcomes[1]
    data.bscreen.nameBarPlayer = drawNameBarPlayer(data.player.pokemon.name, data.player.pokemon.level)
    enemyOutcomes = (drawHealthBar(data.enemy.pokemon.hp, data.enemy.pokemon.maxhp))
    data.bscreen.healthBarEnemy = enemyOutcomes[0]
    data.bscreen.extraSpaceHealthEnemy = enemyOutcomes[1]
    data.bscreen.nameBarEnemy = drawNameBarEnemy(data.enemy.pokemon.name, data.enemy.pokemon.level)
    data.bscreen.playerStatus = getStatusBar(data.player.pokemon)
    data.bscreen.enemyStatus = getStatusBar(data.enemy.pokemon)

def reverseLine(line):
    return (line[::-1])

def fullBattleScreen(data):
    print('/------------------------------------------------------\\')
    print('|> ' + data.bscreen.nameBarEnemy  + ' <|    ' + pokemonSprites[data.enemy.pokemon.species][0] + '|')
    print('|(' + data.bscreen.healthBarEnemy + ')|    ' + pokemonSprites[data.enemy.pokemon.species][1] + '|')
    print('| ' + data.bscreen.enemyStatus + ' /----------------/    ' + pokemonSprites[data.enemy.pokemon.species][2] + '|')
    print('|----/                      ' + pokemonSprites[data.enemy.pokemon.species][3] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][0]) + pokemonSprites[data.enemy.pokemon.species][4] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][1]) + pokemonSprites[data.enemy.pokemon.species][5] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][2]) + pokemonSprites[data.enemy.pokemon.species][6] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][3]) + pokemonSprites[data.enemy.pokemon.species][7] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][4]) + pokemonSprites[data.enemy.pokemon.species][8] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][5]) + pokemonSprites[data.enemy.pokemon.species][9] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][6]) + pokemonSprites[data.enemy.pokemon.species][10] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][7]) + pokemonSprites[data.enemy.pokemon.species][11] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][8]) + pokemonSprites[data.enemy.pokemon.species][12] + '|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][9]) + '    /----------------------|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][10]) + '    |> ' + data.bscreen.nameBarPlayer + ' <|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][11]) + '    |(' + data.bscreen.healthBarPlayer + ')|')
    print('|' + reverseLine(pokemonSprites[data.player.pokemon.species][12]) + '    | ' + data.bscreen.playerStatus + '    ' + data.bscreen.extraSpaceHealthPlayer + str(data.player.pokemon.hp) + '/' + str(data.player.pokemon.maxhp) + 'HP |')
    print('|------------------------------------------------------|')

def liteBattleScreen(data):
    print('/------------------------------------------------------\\')
    print('|                               |> ' + data.bscreen.nameBarEnemy  + ' <|')
    print('|----------------------\\        |(' + data.bscreen.healthBarEnemy + ')|')
    print('|> ' + data.bscreen.nameBarPlayer + ' <|        \\----------------\\ ' + data.bscreen.enemyStatus + ' |')
    print('|(' + data.bscreen.healthBarPlayer + ')|                          \\----|')
    print('| ' + data.bscreen.playerStatus + '    ' + data.bscreen.extraSpaceHealthPlayer + str(data.player.pokemon.hp) + '/' + str(data.player.pokemon.maxhp) + 'HP |                               |')
    print('|------------------------------------------------------|')

def drawScreen(data):
    getBattleScreenValues(data)
    fullBattleScreen(data)

def battleChoiceScreen(lastChoice):
    one = ' '; two = ' '; thr = ' '; fou = ' '
    if lastChoice == 1:
        one = '>'
    elif lastChoice == 2:
        two = '>'
    elif lastChoice == 3:
        thr = '>'
    elif lastChoice == 4:
        fou = '>'
    print('| What would you like to do?                           |')
    print('|    ' + one + ' 1 - Fight                ' + two + ' 2 - Pokemon          |')
    print('|    ' + thr + ' 3 - Bag                  ' + fou + ' 4 - Run              |')
    print('\\------------------------------------------------------/')

def getExtraSpaceAttackChoice(a,b,c,d,e,f,g):
    length = len(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))
    space = ''
    #spareSpaces = 50 - length
    spareSpaces = 25 - length
    for _ in range(spareSpaces):
        space += ' '
    return space

#def attackChoiceScreen(data):
#    drawScreen(data)
#    moveSet = data.player.pokemon.moveSet
#    for i in range(len(moveSet)):
#        cc = '|'
#        if i + 1 == data.player.pokemon.lastAttackChoice:
#            cc = '>'
#        extraSpace = getExtraSpaceAttackChoice('| ', i + 1, '-', moveSet[i], '-', str(data.player.pokemon.movePPCurrent[i]) + '/' + str(data.player.pokemon.movePPMax[i]), 'PP')
#        print('|', i + 1, cc, moveSet[i], '-', str(data.player.pokemon.movePPCurrent[i]) + '/' + str(data.player.pokemon.movePPMax[i]), 'PP' + extraSpace + '|')
#    print('|', len(moveSet) + 1, '| Back                                             |')
#    print('\\------------------------------------------------------/')

def attackChoiceScreen(data):
    drawScreen(data)
    moveSet = data.player.pokemon.moveSet
    line = ""
    for i in range(4):
        if i + 1 == data.player.pokemon.lastAttackChoice:
            lastMoveIdentifier = '>'
        else:
            lastMoveIdentifier = '-'
        if i < len(moveSet):
            extraSpace = getExtraSpaceAttackChoice('| ', i + 1, '-', moveSet[i], '-', str(data.player.pokemon.movePPCurrent[i]) + '/' + str(data.player.pokemon.movePPMax[i]), 'PP')
            line += "| " + str(i+1) + " " + lastMoveIdentifier + " " + moveSet[i] + extraSpace + str(data.player.pokemon.movePPCurrent[i]) + '/' + str(data.player.pokemon.movePPMax[i]) + 'PP '
        else:
            line += "| " + str(i+1) + " -                      "
        if i in [1,3]:
            line += " |"
            print(line)
            line = ""
    if line != "":
        print(line)
    print('| 5 | Back                                             |')
    print('\\------------------------------------------------------/')
