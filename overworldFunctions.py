
from battleFunctions import startBattle
from choicesFunctions import getOptionOneOrTwoOrThree
from pokemonLocationsDictionaries import getWildPokemon
from choicesFunctions import getOptionOneOrTwo, getOptionOneOrTwoOrThree, getOptionOneOrTwoOrThreeOrFour, getOptionOneOrTwoOrThreeOrFourOrFive, getOptionsXnumber
from gameMaps import overworldMap, mapCodeToLocationDict, locationToMapCodeDict

def showLinkingLocations(data):
    mapCode = locationToMapCodeDict[data.environment.location]
    count = 0
    for row in overworldMap:
        if mapCode in row:
            x = row.index(mapCode)
            y = count
        count += 1
    west = mapCodeToLocationDict[overworldMap[y][x-1]]
    east = mapCodeToLocationDict[overworldMap[y][x+1]]
    north = mapCodeToLocationDict[overworldMap[y-1][x]]
    south = mapCodeToLocationDict[overworldMap[y+1][x]]
    print('You are currently in', data.environment.location + '. Which way would you like to go?')
    northD = 'North: ' + north
    eastD  = 'East: ' + east
    southD = 'South: ' + south
    westD  = 'West: ' + west
    current = 'Current: ' + data.environment.location
    allDirections = [northD, eastD, southD, westD]
    allLocations = [north, east, south, west]
    count = 0
    availableDirectionsD = [current]
    availableDirections = [data.environment.location]
    for direction in allDirections:
        if 'Nothing' not in direction:
            availableDirectionsD.append(direction)
            availableDirections.append(allLocations[count])
        count += 1
    choice = getOptionsXnumber(availableDirectionsD)
    return availableDirections[choice - 1]

def directionChoice(data):
    data.environment.location = showLinkingLocations(data)


