from spritesAll import screenTop, screenBot, screenMid, allSpriteDict, menuSprite

def drawOverworld(data, x, y, location, text=False, menu=False):
    screenDraw = screenTop + '\n'
    yAxis = 0
    layer = 0
    for line in location:
        if yAxis > y-4 and yAxis < y+4:
            xAxis = 0
            for location in range(3):
                if text == True and yAxis == y+2 and location == 2:
                    screenDraw += screenMid
                    print(screenDraw)
                    return
                screenDraw += '┃'
                menuDrawn = False
                for sprite in line:
                    if xAxis > x-5 and xAxis < x+5:
                        if menu == True and xAxis >= x+2 and yAxis <= y+1 and menuDrawn == False:
                            screenDraw += menuSprite[layer]
                            menuDrawn = True
                        elif menuDrawn == True:
                            pass
                        elif [x, y] == [xAxis, yAxis]:
                            screenDraw += allSpriteDict["Y"][data.player.direction][location]
                        elif sprite == "*":
                            for enemy in data.environment.location.enemies:
                                if [xAxis, yAxis] == enemy.coords:
                                    screenDraw += allSpriteDict["*"][enemy.viewDirection][location]
                        elif data.environment.battleStart == True:
                            for enemy in data.environment.location.enemies:
                                if enemy.battleReady == True:
                                    if [xAxis, yAxis] == enemy.battleReadySignalCoords:
                                        screenDraw += allSpriteDict["!"][location]
                                    else:
                                        screenDraw += (allSpriteDict[sprite][location])
                        else:
                            screenDraw += (allSpriteDict[sprite][location])
                    xAxis += 1
                screenDraw += '┃\n'
                layer += 1
                xAxis = 0
            location += 1
        yAxis += 1
    screenDraw += screenBot
    print(screenDraw)