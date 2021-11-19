from screen import drawScreen
from spritesAll import screenTop, screenBot, screenEmp, allSpriteDict
from textTools import splitIntoLines, getExtraSpace, turnIntoOneString
from drawOverworld import drawOverworld

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

def worldText(data, *therest, menu=False):
    drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map, text=True, menu=menu)
    newString = turnIntoOneString(therest)
    lines = splitIntoLines(newString, 52)
    for line in lines:
        extraSpace = getExtraSpace(line, 52)
        print('┃ ' + line + extraSpace + ' ┃')
    for _ in range(3 - len(lines)):
        print(screenEmp)
    print(screenBot)
    input()

