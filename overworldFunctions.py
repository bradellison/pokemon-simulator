from random import randint

from battleFunctions import startBattle
from choicesFunctions import getOptionOneOrTwoOrThree
from choicesFunctions import getOptionOneOrTwo, getOptionOneOrTwoOrThree, getOptionOneOrTwoOrThreeOrFour, getOptionOneOrTwoOrThreeOrFourOrFive, getOptionsXnumber
from gameMaps import locationMapDict
from pokemonCentreFunctions import pokemonCenter
from battleFunctions import createEnemy
from classes import Pokemon, Location
from pokemonLocationsDictionaries import locationToDict

def chooseDirection(data):
    mapCode = locationToMapCodeDict[data.environment.location.name]
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
    print('You are currently in', data.environment.location.name + '. Which way would you like to go?')
    northD = 'North: ' + north
    eastD  = 'East: ' + east
    southD = 'South: ' + south
    westD  = 'West: ' + west
    current = 'Current: ' + data.environment.location.name
    allDirections = [northD, eastD, southD, westD]
    allLocations = [north, east, south, west]
    count = 0
    availableDirectionsD = [current]
    availableDirections = [data.environment.location.name]
    for direction in allDirections:
        if 'Nothing' not in direction:
            availableDirectionsD.append(direction)
            availableDirections.append(allLocations[count])
        count += 1
    choice = getOptionsXnumber(availableDirectionsD)
    return availableDirections[choice - 1]

def addLocationInformation(data, newLocation):
#    data.environment.location.name = newLocation
#    data.environment.location.grass = locationInformationDict[newLocation]['Grass']
#    data.environment.location.water = locationInformationDict[newLocation]['Water']
#    data.environment.location.centre = locationInformationDict[newLocation]['Centre']
#    data.environment.location.map = locationMapDict[newLocation]
#    data.environment.location.warpZones = 
    data.environment.location = Location(newLocation)

def directionChoice(data):
    newLocation = chooseDirection(data)
    addLocationInformation(data, newLocation)
    print('You are now in', data.environment.location.name + '!')

def getWildPokemon(location):
    number = randint(1,100)
    locationDict = locationToDict[location]
    while True:
        if number in locationDict:
            pokemon = locationDict[number]
            return pokemon     
        else:
            number += 1

def whitedOut(data):
    print('You whited out! You rushed to get your Pokemon healed at', data.player.lastCentre + '!')
    addLocationInformation(data, data.player.lastCentre)
    pokemonCenter(data, True)

def wildBattle(data):
    wildPokemon = getWildPokemon(data.environment.location.name)
    pokemon = wildPokemon[0]
    level = wildPokemon[1]
    wildTeam = [Pokemon(pokemon, level, 'Random')]
    createEnemy(data,'Wild', 'Wild', wildTeam, 0, 'Damn!')
    if startBattle(data) != 'Win':
        whitedOut(data)
