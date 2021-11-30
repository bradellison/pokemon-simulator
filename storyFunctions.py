from classes import Pokemon, Item

from battleFunctions import startBattle
from choicesFunctions import getOptionOneOrTwoOrThree, getYesOrNo
from overworldFunctions import getWildPokemon, wildBattle
from pokemonCentreFunctions import pokemonCenter
from mapDrawing import overworldMovement
from text import worldText
import time

def mainGame(data):
    while True:
        overworldMovement(data)        

