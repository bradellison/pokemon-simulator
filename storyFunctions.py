from classes import Pokemon
from classes import Ball

from battleFunctions import startBattle
from choicesFunctions import getOptionOneOrTwoOrThree, getYesOrNo
from overworldFunctions import directionChoice, getWildPokemon, wildBattle
from pokemonCentreFunctions import pokemonCenter
from mapDrawing import overworldMovement
from text import worldText
import time

def mainGame(data, newOrContinue):
    while True:
        overworldMovement(data)        

