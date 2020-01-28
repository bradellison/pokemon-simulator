import math
import random
from random import randint 

class BattleScreen(object):
    def __init__(self):
        self.healthBarPlayer = ''
        self.healthBarEnemy = ''
        self.extraSpaceHealthPlayer = ''
        self.nameBarPlayer = ''
        self.nameBarEnemy = ''

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
    return (name + ' - L' + str(level) + extraSpaceName + extraSpaceLevel)

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
    return (extraSpaceName + extraSpaceLevel + name + ' - L' + str(level))

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

def getBattleScreenValues(data):
    playerOutcomes = (drawHealthBar(data.player.pokemon.hp, data.player.pokemon.maxhp))
    data.bscreen.healthBarPlayer = playerOutcomes[0]
    data.bscreen.extraSpaceHealthPlayer = playerOutcomes[1]
    data.bscreen.nameBarPlayer = drawNameBarPlayer(data.player.pokemon.name, data.player.pokemon.level)
    enemyOutcomes = (drawHealthBar(data.enemy.pokemon.hp, data.enemy.pokemon.maxhp))
    data.bscreen.healthBarEnemy = enemyOutcomes[0]
    data.bscreen.extraSpaceHealthEnemy = enemyOutcomes[1]
    data.bscreen.nameBarEnemy = drawNameBarEnemy(data.enemy.pokemon.name, data.enemy.pokemon.level)

#def fullBattleScreen(bscreen, playerMaxHealth, playerCurrentHealth):
#    print('/---------------------------------------------------------------------------\\')
#    print('|                                                    |    ' + bscreen.nameBarEnemy  + ' |')
#    print('|                                                    |(' + bscreen.healthBarEnemy + ')|')
#    print('|                                                    \\----------------------|')
#    print('|                                                                           |')
#    print('|                                                                           |')
#    print('|                                                                           |')
#    print('|                                                                           |')
#    print('|                                                                           |')
#    print('|----------------------\\                                                    |')
#    print('| ' + bscreen.nameBarPlayer + '    |                                                    |')
#    print('|(' + bscreen.healthBarPlayer + ')|                                                    |')
#    print('|        ' + bscreen.extraSpaceHealthPlayer + str(playerCurrentHealth) + '/' + str(playerMaxHealth) + 'HP |                                                    |')
#    print('\\---------------------------------------------------------------------------/')
#    print('|                                                                           |')
#    print('|                                                                           |')
#    print('|                                                                           |')
#    print('|                                                                           |')
#    print('|                                                                           |')
#    print('\\---------------------------------------------------------------------------/')

def liteBattleScreen(data):
    print('/------------------------------------------------------\\')
    print('|                               |>  ' + data.bscreen.nameBarEnemy  + ' <|')
    print('|----------------------\\        |(' + data.bscreen.healthBarEnemy + ')|')
    print('|> ' + data.bscreen.nameBarPlayer + '  <|        \\----------------------|')
    print('|(' + data.bscreen.healthBarPlayer + ')|                               |')
    print('|        ' + data.bscreen.extraSpaceHealthPlayer + str(data.player.pokemon.hp) + '/' + str(data.player.pokemon.maxhp) + 'HP |                               |')
    print('|------------------------------------------------------|')

def drawScreen(data):
    getBattleScreenValues(data)
    liteBattleScreen(data)

def battleChoiceScreen():
    print('| What would you like to do?                           |')
    print('|      1 - Fight                  2 - Pokemon          |')
    print('|      3 - Bag                    4 - Run              |')
    print('\\------------------------------------------------------/')

def getExtraSpaceAttackChoice(a,b,c,d,e,f,g):
    length = len(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))
    space = ''
    spareSpaces = 50 - length
    for _ in range(spareSpaces):
        space += ' '
    return space

def attackChoiceScreen(data):
    drawScreen(data)
    moveSet = data.player.pokemon.moveSet
    for i in range(len(moveSet)):
        extraSpace = getExtraSpaceAttackChoice('| ', i + 1, '-', moveSet[i], '-', str(data.player.pokemon.movePPCurrent[i]) + '/' + str(data.player.pokemon.movePPMax[i]), 'PP')
        print('|', i + 1, '|', moveSet[i], '-', str(data.player.pokemon.movePPCurrent[i]) + '/' + str(data.player.pokemon.movePPMax[i]), 'PP' + extraSpace + '|')
    print('|', len(moveSet) + 1, '| Back                                             |')
    print('\\------------------------------------------------------/')
