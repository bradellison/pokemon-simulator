import time

from pcFunctions import usePC
from saveDataFunctions import saveGame, loadGame, saveOrLoad
from getVariableFunctions import getMaxPP
from choicesFunctions import getOption, getOptionOneOrTwo
from text import worldText, worldTextOptions




def pokemonCenter(data, whitedOut):
	if whitedOut == True:
		healAllPokemon(data)
	else:
		option = worldTextOptions(data, 'Hello, welcome to the Pokemon Centre, would you like me to heal your Pokemon?', options=["Yes","No"], response=True)
		if option == "Yes":
			worldText(data, "Okay, please let me take your pokemon for a few moments.")
			healAllPokemon(data)
			worldText(data, 'Your team is now at full health! We hope to see you again!')
		else:
			worldText(data, 'Alright, see you next time.')


def healAllPokemon(data):
	for pokemon in data.player.team:
		healPokemon(pokemon)
	

def healPokemon(pokemon, printHeal=False):
	pokemon.hp = pokemon.maxhp
	pokemon.nvStatus = 0
	pokemon.nvStatusCount = 0
	pokemon.movePPCurrent = getMaxPP(pokemon)
	if printHeal == True:
		print('Healed', pokemon.name + '!')
		time.sleep(1)