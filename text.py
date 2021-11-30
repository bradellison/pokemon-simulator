from screen import drawScreen
import math
from spritesAll import screenTop, screenBot, screenEmp, allSpriteDict
from textTools import splitIntoLines, getExtraSpace, turnIntoOneString, onlyTextBoxWithOptions
from drawOverworld import drawOverworld
from choicesFunctions import getOption

def text(data, *therest):
    drawScreen(data)
    newString = turnIntoOneString(therest)
    lines = splitIntoLines(newString, 52)
    for line in lines:
        extraSpace = getExtraSpace(line, 52)
        print('┃ ' + line + extraSpace + ' ┃')
    for _ in range(3 - len(lines)):
        print(screenEmp)
    print(screenBot)
    input()

def worldText(data, *therest, menu=False, response=False):
    drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map, text=True, menu=menu)
    newString = turnIntoOneString(therest)
    lines = splitIntoLines(newString, 52)
    for line in lines:
        extraSpace = getExtraSpace(line, 52)
        print('┃ ' + line + extraSpace + ' ┃')
    for _ in range(3 - len(lines)):
        print(screenEmp)
    print(screenBot)
    if response == False:
        input()

def worldTextOptions(data, *therest, options, menu=False, response=False):
    drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map, text=True, menu=menu)
    string = turnIntoOneString(therest)
    onlyTextBoxWithOptions(string, options)
    option = getOption(options)
    if response == False:
        input()
    return option
