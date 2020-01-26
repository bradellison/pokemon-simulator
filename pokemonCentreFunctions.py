import time

from pcFunctions import usePC
from saveDataFunctions import saveGame, loadGame, saveOrLoad
from choicesFunctions import getOptionOneOrTwo



def getPokemonCenterChoice():
	print(' 1 - Heal Team\n 2 - Use PC\n 3 - Shop\n 4 - Save or Load \n 5 - Leave')
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2 or choiceInput == 3 or choiceInput == 4 or choiceInput == 5:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def pokemonCenter(data):
	print('Hello, welcome to the Pokemon Center. What would you like to do here today?')
	leave = 0
	while leave == 0:
		choice = getPokemonCenterChoice()
		if choice == 1:
			healAllPokemon(data)
		elif choice == 2:
			usePC(data)
		elif choice == 3:
			print(data.player.money)
			print('The shop is currently closed, please come again later!\n')
		elif choice == 4:
			saveOrLoad(data)
		elif choice == 5:
			leave = 1
			print('Thank you for coming, we hope to see you again!\n')
			return
		print('Anything else we can do for you today?')



def healAllPokemon(data):
	print('Of course, please let me take your pokemon for a few moments!')
	for pokemon in data.player.team:
		pokemon.hp = pokemon.maxhp
		pokemon.nvStatus = 0
		pokemon.nvStatusCount = 0
		pokemon.movePPCurrent = pokemon.movePPMax
		print('Healed', pokemon.name + '!')
		time.sleep(1)
	print('Your team is now at full health!\n')