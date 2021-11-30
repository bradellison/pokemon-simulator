from spritesAll import screenTop, screenMid, screenBot, screenEmp
from textTools import getExtraSpace, printWithScreenSides, onlyTextBoxWithOptions, drawBar
from choicesFunctions import getOption
from text import text
import math

topLine = "╭──────────────────────────╮                          "
rightTop = "├─────────────────────────╮"
leftMid = "├┴───────┴─────────────────"
rightMid = "├┴───────┴────────────────┤"
leftBot = "╰┴───────┴─────────────────"
bottomLine = "                           ╰┴───────┴────────────────╯"


        

def compilePokemonData(pokemon, placeInParty):
    if placeInParty % 2 == 0:
        rightSpaceReq = 13
        beforeNum = "┤"
        endLine = "│"
    else:
        rightSpaceReq = 14
        beforeNum = "│"
        endLine = ""
    #26 characters total
    extraSpaceAfterName = getExtraSpace(pokemon.name, 11)
    pokemonLevel = "Lvl " + str(pokemon.level)
    extraSpaceAfterLevel = getExtraSpace(pokemonLevel, rightSpaceReq)
    pokemonStatus = getPokemonStatusText(pokemon)
    extraSpaceAfterStatus = getExtraSpace(pokemonStatus, 11)
    pokemonCurrentExp = shortenExp(pokemon.exp)
    pokemonNextLevelExp = shortenExp(pokemon.nextLevelExp)
    pokemonExpString = "XP: " + pokemonCurrentExp + "/" + pokemonNextLevelExp
    extraSpaceAfterExp = getExtraSpace(pokemonExpString, rightSpaceReq)
    pokemonHPString = "HP: " + str(pokemon.hp) + "/" + str(pokemon.maxhp)
    topOfBall = "│╭───────╮   "
    extraSpaceAfterHP = getExtraSpace(pokemonHPString, rightSpaceReq)
    middleOfBall = beforeNum + "│(-(" + str(placeInParty) + ")-)│   "
    pokemonHealthBarInside = drawBar(pokemon.hp, pokemon.maxhp, 11)
    pokemonHealthBar = "(" + pokemonHealthBarInside + ")"
    extraSpaceAfterHealthBar = getExtraSpace(pokemonHealthBar, rightSpaceReq)
    
    line1 = "│ " + pokemon.name + extraSpaceAfterName + pokemonLevel + extraSpaceAfterLevel + endLine
    line2 = "│ " + pokemonStatus + extraSpaceAfterStatus + pokemonExpString + extraSpaceAfterExp + endLine
    line3 = topOfBall + pokemonHPString + extraSpaceAfterHP + endLine 
    line4 = middleOfBall + pokemonHealthBar + extraSpaceAfterHealthBar + endLine

    return[line1, line2, line3, line4]

def drawEmptyPokemonScreen(placeInParty):
    if placeInParty % 2 == 0:
        lineEmpt = "│                         │"
        lineTopBall = "│╭───────╮                │"
        lineMidBall = "┤│(-(" + str(placeInParty) + ")-)│                │"
    else:
        lineEmpt = "│                          "
        lineTopBall = "│╭───────╮                 "
        lineMidBall = "││(-(" + str(placeInParty) + ")-)│                 "


    return [lineEmpt, lineEmpt, lineTopBall, lineMidBall]

def shortenExp(exp):
    if len(str(exp)) > 4:
        if len(str(exp)) > 6:
            return str(round((exp / 1000000), 1)) + "m"
        return str(math.floor(exp / 1000)) + "k"    
    else:
        return str(exp)



def openPokemonSelectionScreen(data, pokemonChosen=None, battle=False, selectionText="Which Pokemon would you like to select?", useOrGiveItem=False):
    if battle == True:
        team = data.player.team
    else:
        team = data.player.defaultTeam
    while True:
        pokemonData = []
        for placeInParty in range(1,7):
            if placeInParty <= len(team):
                pokemonData.append(compilePokemonData(team[placeInParty - 1], placeInParty))
            else:
                pokemonData.append(drawEmptyPokemonScreen(placeInParty))
        drawMainSelectionScreen(pokemonData)
        if pokemonChosen == None:
            pokemonChosen = choosePokemon(data, team, selectionText)
            if pokemonChosen == "Back":
                return "Back"
            if useOrGiveItem == True:
                return pokemonChosen
        else:
            onlyTextBoxWithOptions("What would you like to do with " + pokemonChosen.name + "?", ["More Info", "Switch", "Use Item", "Back"])
            option = getOption(["More Info", "Switch", "Use Item", "Back"])
            if option == "More Info":
                moreInfoScreen(data, team, pokemonChosen)
                pokemonChosen = None
            elif option == "Switch":
                if battle == True:
                    switchOutcome = getSwitchBattle(data, pokemonChosen)
                    if switchOutcome == True:
                        return True
                    else:
                        selectionText = switchOutcome
                        pokemonChosen = None
                else:
                    drawMainSelectionScreen(pokemonData)
                    switchSelectionText = "Which Pokemon should you switch " + pokemonChosen.name + " with?"
                    secondPokemon = choosePokemon(data, team, switchSelectionText)
                    if secondPokemon != pokemonChosen and secondPokemon != "Back":

                        index1 = team.index(pokemonChosen)
                        index2 = team.index(secondPokemon)
                        team[index1] = secondPokemon
                        team[index2] = pokemonChosen
                    pokemonChosen = None
            elif option == "Use Item":
                print("Item time")
            elif option == "Back":
                pokemonChosen = None

def getSwitchBattle(data, pokemonChosen):
    while True:
            try:
                x = 0
                trapped = data.player.pokemon.bind + data.player.pokemon.clamp + data.player.pokemon.fireSpin + data.player.pokemon.wrap
                if pokemonChosen == data.player.pokemon:
                    if data.player.pokemon.hp == 0:
                        return data.player.pokemon.name + ' has fainted! Please choose another Pokemon!'
                    else:
                        return 'That Pokemon is already out! Please choose another Pokemon!'
                elif pokemonChosen == "Back":
                    if data.player.pokemon.hp == 0:
                        return data.player.pokemon.name + ' has fainted! Please choose another Pokemon!'
                    else:
                        text(data, 'Keep going,', data.player.pokemon.name + '!')
                        return False

                        # No switch
                elif data.player.pokemon.hp != 0 and trapped != 0:
                    return data.player.pokemon.name, ' is unable to escape due to being trapped!'
                    return False
                else:
                    if pokemonChosen.hp == 0:
                        return pokemonChosen.name + ' has fainted! Please choose another Pokemon!'

                        return False
                    else:
                        j = data.player.team.index(pokemonChosen)
                        data.player.team[j], data.player.team[0] = data.player.team[0], data.player.team[j]
                        data.player.pokemon = data.player.team[0]
                        return True
                if x == 0:
                    return "Please choose a Pokemon from the list above!"
            except ValueError:
                return "Please choose a Pokemon from the list above!"

def choosePokemon(data, team, selectionText):
    onlyTextBoxWithOptions(selectionText, [], backWithE=True)
    option = getOption(team)
    return option


def getPokemonStatusText(pokemon):
    statusDict = {0:'ABLE',1:'BRN',2:'PAR',3:'SLP',4:'FRZ',5:'PSN',6:'PSN'}
    if pokemon.hp > 0:
        pokemonStatus = statusDict[pokemon.nvStatus]
    else:
        pokemonStatus = "FNT"
    return pokemonStatus

def moreInfoScreen(data, team, pokemon):
    print(screenTop)
    lineText = " " + pokemon.name
    printWithScreenSides(lineText + getExtraSpace(lineText, 26) + "│" + pokemon.sprite[0])
    lineText = (" Level " + str(pokemon.level) + " " + pokemon.species) 
    printWithScreenSides(lineText + getExtraSpace(lineText, 26) + "│" + pokemon.sprite[1])
    lineText = "─[HEALTH]─────────────────│"
    printWithScreenSides(lineText + pokemon.sprite[2])
    lineText = " " + str(pokemon.hp) + "/" + str(pokemon.maxhp) + " - " + getPokemonStatusText(pokemon)
    printWithScreenSides(lineText + getExtraSpace(lineText, 26) + "│" + pokemon.sprite[3])
    lineText = "  (" + drawBar(pokemon.hp, pokemon.maxhp, 20) + ")  "
    printWithScreenSides(lineText + "│" + pokemon.sprite[4])
    lineText = "─[EXP]────────────────────│"
    printWithScreenSides(lineText + pokemon.sprite[5]) 
    lineText = " " + str(pokemon.exp) + " - " + getExpToNextLevel(pokemon)
    printWithScreenSides(lineText + getExtraSpace(lineText, 26) + "│" + pokemon.sprite[6])
    lineText = "  [" + drawBar(pokemon.exp - pokemon.lastLevelExp, pokemon.nextLevelExp - pokemon.lastLevelExp, 20, "-", finalBarDifferent=True) + "]  "
    printWithScreenSides(lineText + "│" + pokemon.sprite[7])
    lineText = "─[STATS]──────────────────│"
    printWithScreenSides(lineText + pokemon.sprite[8])
    statText = []
    emptyText = []
    stats = ["  HP", " Atk", " Def", " SpA", " SpD", " Spd"]
    for i in range(6):
        line = stats[i] + ": " + str(pokemon.stats[i])
        statText.append(line)
        emptyText.append(getExtraSpace(line, 13))
    printWithScreenSides(statText[0] + emptyText[0] + statText[3] + emptyText[3] + "│" + pokemon.sprite[9])
    printWithScreenSides(statText[1] + emptyText[1] + statText[4] + emptyText[4] + "│" + pokemon.sprite[10])
    printWithScreenSides(statText[2] + emptyText[2] + statText[5] + emptyText[5] + "│" + pokemon.sprite[11])
    lineText = "─[MOVES]──────────────────│"
    printWithScreenSides(lineText + pokemon.sprite[12])
    moveText = []
    for i in range(4):
        if len(pokemon.moveSet) > i:
            movePPText = str(pokemon.movePPCurrent[i]) + "/" + str(pokemon.movePPMax[i]) + "PP"
            moveText.append(" " + pokemon.moveSet[i] + getExtraSpace(pokemon.moveSet[i],15) + getExtraSpace(movePPText, 9) + movePPText)
        else:
            moveText.append("                         ")
    printWithScreenSides(moveText[0] +  " ╰──[OTHER]──────────────────")
    lineText = "Nature: " + pokemon.nature
    printWithScreenSides(moveText[1] + "  │ " + lineText + getExtraSpace(lineText, 25))
    lineText = "Ability: " + pokemon.ability
    printWithScreenSides(moveText[2] + "  │ " + lineText + getExtraSpace(lineText, 25))
    lineText = "Item: " + pokemon.item.name
    printWithScreenSides(moveText[3] + "  │ " + lineText + getExtraSpace(lineText, 25))
    print(screenMid)
    options = ["View previous Pokemon", "View next Pokemon", "Use Item", "Back"]
    onlyTextBoxWithOptions("What would you like to do with " + pokemon.name + "?", options)
    option = getOption(options)
    if option == "View previous Pokemon":
        moreInfoScreen(data, team, returnNextOrPreviousInParty(data, team, pokemon, next=False))
        return
    elif option == "View next Pokemon":
        moreInfoScreen(data, team, returnNextOrPreviousInParty(data, team, pokemon, next=True))
        return    
    elif option == "Use Item":
        print("Item time")
    elif option == "Back":
        return
    input("-- ")

def returnNextOrPreviousInParty(data, team, pokemon, next):
    if next == True:
        direction = 1
    else:
        direction = -1
    placeInParty = team.index(pokemon)
    toCheckPlaceInParty = placeInParty + direction
    if toCheckPlaceInParty < 0 : 
        toCheckPlaceInParty = len(team) - 1
    elif toCheckPlaceInParty >= len(team):
        toCheckPlaceInParty = 0
    return team[toCheckPlaceInParty]

def getExpToNextLevel(pokemon):
    if pokemon.level == 100:
        return "No next level"
    else:
        toNextLevel = pokemon.nextLevelExp - pokemon.exp
        return str(toNextLevel) + " to next"


def drawMainSelectionScreen(pokemonData):
    print(screenTop)
    printWithScreenSides(topLine)
    printWithScreenSides(pokemonData[0][0] + rightTop)
    printWithScreenSides(pokemonData[0][1] + pokemonData[1][0])
    printWithScreenSides(pokemonData[0][2] + pokemonData[1][1])
    printWithScreenSides(pokemonData[0][3] + pokemonData[1][2])
    printWithScreenSides(leftMid + pokemonData[1][3])
    printWithScreenSides(pokemonData[2][0] + rightMid)
    printWithScreenSides(pokemonData[2][1] + pokemonData[3][0])
    printWithScreenSides(pokemonData[2][2] + pokemonData[3][1])
    printWithScreenSides(pokemonData[2][3] + pokemonData[3][2])
    printWithScreenSides(leftMid + pokemonData[3][3])
    printWithScreenSides(pokemonData[4][0] + rightMid)
    printWithScreenSides(pokemonData[4][1] + pokemonData[5][0])
    printWithScreenSides(pokemonData[4][2] + pokemonData[5][1])
    printWithScreenSides(pokemonData[4][3] + pokemonData[5][2])
    printWithScreenSides(leftBot + pokemonData[5][3])
    printWithScreenSides(bottomLine)
    print(screenMid)













#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Charmander               │                           ┃
#┃ Level 100 Charmander     │                           ┃
#┃─[HEALTH]─────────────────│                           ┃
#┃ 261/261HP - ABLE         │        ▒▒▓▓▒              ┃
#┃ (======================) │       ▓▒▒▓▓▓      ░       ┃
#┃─[EXP]────────────────────│       ▒▓▓▓▓▓    ░▓▓▒      ┃
#┃ 1000000 - 30000 to next  │      ▒▒▓▒▒▓▓▓▓▒ ▒▓▓▓      ┃
#┃ [--------------->      ] │        ▒░▒▓▓▓    ▒▒       ┃
#┃─[STATS]──────────────────│       ▒▒░▒▓▓▓▓▒▒▓▒        ┃
#┃  HP: 261     SpA: 120-   │       ▓▓▓▓█▓▓▓▓▒          ┃
#┃ Atk: 141+    SpD: 55     │       ▒▒▒  ▒▓▓            ┃
#┃ Def: 250     Spd: 123    │                           ┃
#┃─[MOVES]──────────────────│                           ┃
#┃ Sleep Powder   15/15PP   ╰──[OTHER]──────────────────┃
#┃ Constrict      35/35PP    │ Nature: Adamant          ┃
#┃ PoisonPowder   35/35PP    │ Ability: Blaze           ┃
#┃ Slam           20/20PP    │ Item: None               ┃
#┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
#┃ Which would you like to do with Charmander?          ┃
#┃ 1 - View previous Pokemon  2 - View next Pokemon     ┃
#┃ 3 - Use Item               4 - Back                  ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛




example = [
"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓",
"┃╭──────────────────────────╮                          ┃",
"┃│ Bulbasaur1 Lvl 100       ├─────────────────────────╮┃",
"┃│ ABLE       XP: 15/62     │ Tauros1234 Lvl 100      │┃",
"┃│╭───────╮   HP: 131/135   │ ABLE       XP: 2910/3910│┃",
"┃││(-(1)-)│   (===========) │╭───────╮   HP: 131/135  │┃",
"┃├┴───────┴─────────────────┤│(-(2)-)│   (===========)│┃",
"┃│ Alakazam   Lvl 100       ├┴───────┴────────────────┤┃",
"┃│ ABLE       XP: 2910/3134 │ Mew        Lvl 100      │┃",
"┃│╭───────╮   HP: 131/135   │ ABLE       XP: 2910/3134│┃",
"┃││(-(3)-)│   (===========) │╭───────╮   HP: 131/135  │┃",
"┃├┴───────┴─────────────────┤│(-(4)-)│   (===========)│┃",
"┃│ Dragonite  Lvl 100       ├┴───────┴────────────────┤┃",
"┃│ ABLE       XP: 2910/3134 │ Gyarados   Lvl 100      │┃",
"┃│╭───────╮   HP: 131/135   │ ABLE       XP: 27k/30k  │┃",
"┃││(-(5)-)│   (===========) │╭───────╮   HP: 131/135  │┃",
"┃╰┴───────┴─────────────────┤│(-(6)-)│   (===========)│┃",
"┃                           ╰┴───────┴────────────────╯┃",
"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫",
"┃                                                      ┃",
"┃                                                      ┃",
"┃                                                      ┃",
"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"]


#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃╭──────────────────────────╮                          ┃
#┃│ Charmander Lvl 100       ├─────────────────────────╮┃
#┃│ ABLE       XP: 15/62     │ Tauros1234 Lvl 100      │┃
#┃│╭───────╮   HP: 131/135   │ ABLE       XP: 2910/3910│┃
#┃││(-(1)-)│   (===========) │╭───────╮   HP: 131/135  │┃
#┃├┴───────┴─────────────────┤│(-(2)-)│   (===========)│┃
#┃│ Alakazam   Lvl 100       ├┴───────┴────────────────┤┃
#┃│ ABLE       XP: 2910/3134 │ Mew        Lvl 100      │┃
#┃│╭───────╮   HP: 131/135   │ ABLE       XP: 2910/3134│┃
#┃││(-(3)-)│   (===========) │╭───────╮   HP: 131/135  │┃
#┃├┴───────┴─────────────────┤│(-(4)-)│   (===========)│┃
#┃│ Dragonite  Lvl 100       ├┴───────┴────────────────┤┃
#┃│ ABLE       XP: 2910/3134 │ Gyarados   Lvl 100      │┃
#┃│╭───────╮   HP: 131/135   │ ABLE       XP: 27k/30k  │┃
#┃││(-(5)-)│   (===========) │╭───────╮   HP: 131/135  │┃
#┃╰┴───────┴─────────────────┤│(-(6)-)│   (===========)│┃
#┃                           ╰┴───────┴────────────────╯┃
#┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
#┃ Which would you like to do with Charmander?          ┃
#┃ 1 - More Info                 2 - Switch                ┃
#┃ 3 - Use Item               4 - Back                  ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#-- 1
#
#
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Charmander               │                           ┃
#┃ Level 100 Charmander     │                           ┃
#┃─[HEALTH]─────────────────│                           ┃
#┃ 261/261HP    - ABLE      │        ▒▒▓▓▒              ┃
#┃ (======================) │       ▓▒▒▓▓▓      ░       ┃
#┃─[Exp]────────────────────│       ▒▓▓▓▓▓    ░▓▓▒      ┃
#┃ 1000000 - 30000 to next  │      ▒▒▓▒▒▓▓▓▓▒ ▒▓▓▓      ┃
#┃ [--------------->      ] │        ▒░▒▓▓▓    ▒▒       ┃
#┃─[CURRENT]────────────────│       ▒▒░▒▓▓▓▓▒▒▓▒        ┃
#┃ HP  261 SpA 55           │       ▓▓▓▓█▓▓▓▓▒          ┃
#┃ Atk 141 SpD 55           │       ▒▒▒  ▒▓▓            ┃
#┃ Def 250/123 Spd 55       │                           ┃
#┃─[MOVES]──────────────────│                           ┃
#┃ Sleep Powder   15/15PP   ╰──[OTHER]──────────────────┃
#┃ Constrict      35/35PP    │   Nature: Adamant        ┃
#┃ PoisonPowder   35/35PP    │   Ability: Blaze         ┃
#┃ Slam           20/20PP    │   Item: None             ┃
#┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
#┃ Which would you like to do with Charmander?          ┃
#┃ 1 - More Info              2 - Switch                ┃
#┃ 3 - Use Item               4 - Back                  ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛