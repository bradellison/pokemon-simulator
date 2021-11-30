from random import randint

from battleFunctions import startBattle
from choicesFunctions import getOptionOneOrTwoOrThree
from choicesFunctions import getOptionOneOrTwo, getOptionOneOrTwoOrThree, getOptionOneOrTwoOrThreeOrFour, getOptionOneOrTwoOrThreeOrFourOrFive, getOptionsXnumber
from gameMaps import locationMapDict
from pokemonCentreFunctions import pokemonCenter
from battleFunctions import createEnemy
from classes import Pokemon, Location
from pokemonLocationsDictionaries import locationToDict

def addLocationInformation(data, newLocation):
    for location in  data.environment.locations:
        if location.name == newLocation:
            data.environment.location = location
            return
    newLocationObject = Location(newLocation)
    data.environment.location = newLocationObject
    data.environment.locations.append(newLocationObject)

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
    if data.player.lastCentre != "Pallet Town":
        data.player.xCo = 9; data.player.yCo = 7
    else:
        data.player.xCo = 9; data.player.yCo = 11
    pokemonCenter(data, True)

def wildBattle(data):
    wildPokemon = getWildPokemon(data.environment.location.name)
    pokemon = wildPokemon[0]
    level = wildPokemon[1]
    wildTeam = [Pokemon(pokemon, level, 'Random')]
    createEnemy(data,'Wild', 'Wild', wildTeam, 0, 'Damn!')
    if startBattle(data) != 'Win':
        whitedOut(data)

def trainerBattle(data, enemy):
    data.enemy = enemy
    if startBattle(data) != 'Win':
        whitedOut(data)   
