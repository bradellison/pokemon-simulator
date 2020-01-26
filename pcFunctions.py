
from choicesFunctions import getYesOrNo, getOptionOneOrTwo
from pokemonDictionaries import nonVolatileStatusNumberToType


def getPCChoice():
	print(' 1 - Withdraw\n 2 - Deposit\n 3 - Move\n 4 - Quit')
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2 or choiceInput == 3 or choiceInput == 4:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def usePC(data):
	leave = False
	while leave == False:
		print('\nWhat would you like to do?')
		choice = getPCChoice()
		if choice == 1:
			withdrawPokemonChoice(data)
		elif choice == 2:
			depositPokemonChoice(data)
		elif choice == 3:
			print('This functionality is currently unavailable!')
#			movePokemonChoice()
		elif choice == 4:
			leave = True
			print()
			return

def withdrawPokemonChoice(data):
	y = 0
	if len(data.pc.boxes) == 0:
		print('You have no Pokemon in the box.')
		return 0
	while y == 0:
		count = 1
		print('\nWhich Pokemon would you like to withdraw?')
		for j in range(len(data.pc.boxes[0].inventory)):
			i = data.pc.boxes[0].inventory[j]
			if i == 'Empty':
				print('', count, '- Empty')
			else:
				print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
			count += 1
		print('', count, '- Back')
		while True:
			try:
				x = 0
				choiceInput = input('-- ')
				if int(choiceInput) == int(count):
					return True
				for j in range(len(data.pc.boxes[0].inventory)):
					if int(choiceInput) == int(j+1):
						choice = data.pc.boxes[0].inventory[int(choiceInput) - 1]
						print('What would you like to do with this pokemon?')
						option = getOptionOneOrTwo('Withdraw', 'View more information')
						if option == 1:
							if len(data.player.team) < 6:
								data.player.team.append(choice)
								data.pc.boxes[0].inventory.remove(choice)
								print('You added', choice.name, 'to your party!')
							else:
								print('You have no room in your party for that right now!')
						else:
							getPokemonInfoViewPC(data, choice, 'withdraw')
						x = 1
						return 0
				if x == 0:
					print("Please choose a Pokemon from the list above!")
			except ValueError:
				print("Please choose a Pokemon from the list above!")	

def depositPokemonChoice(data):
	y = 0
	while y == 0:
		count = 1
		print('\nWhich Pokemon would you like to deposit?')
		for i in data.player.team:
			print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
			count += 1
		print('', count, '- Back')
		while True:
			try:
				x = 0
				choiceInput = input('-- ')
				if int(choiceInput) == int(count):
					return 0
				for j in range(len(data.player.team)):
					if choiceInput == data.player.team[j].name or int(choiceInput) == int(j+1):
						choice = data.player.team[int(choiceInput) - 1]
						print('What would you like to do with this pokemon?')
						option = getOptionOneOrTwo('Deposit', 'View more information')
						if option == 1:
							if len(data.player.team) > 1:
								data.player.team.remove(choice)
								data.pc.boxes[0].inventory.append(choice)
								print('You deposited', choice.name, 'into your PC!')
							else:
								print('You cannot deposit your only Pokemon!')
						else:
							getPokemonInfoViewPC(data, choice, 'deposit')
						x = 1
						return 0
				if x == 0:
					print("Please choose a Pokemon from the list above!")
			except ValueError:
				print("Please choose a Pokemon from the list above!")	

def getPokemonInfoViewChoiceTeam(data):
	y = 0
	while y == 0:
		count = 1
		print('Which Pokemon would you like to view?')
		for i in data.player.team:
			print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
			count += 1
		print('', count, '- Back')
		while True:
			try:
				x = 0
				choiceInput = input('-- ')
				if int(choiceInput) == int(count):
					return 0
				for j in range(len(data.player.team)):
					if choiceInput == data.player.team[j].name or int(choiceInput) == int(j+1):
						choice = data.player.team[int(choiceInput) - 1]
						getPokemonInfoViewTeam(data, choice)
						x = 1
						return 0
				if x == 0:
					print("Please choose a Pokemon from the list above!")
			except ValueError:
				print("Please choose a Pokemon from the list above!")	

def getPokemonInfoViewTeam(data, pokemon):
	print('')
	print(pokemon.name, '- Level', pokemon.level, pokemon.species)
	if len(pokemon.type) == 1:
		print(pokemon.type[0], 'Type')
	else:
		print(pokemon.type[0], '/', pokemon.type[1], 'Type')
	print('\nHealth')
	print(' ', str(pokemon.hp) + '/' + str(pokemon.maxhp) + 'HP')
	if pokemon.hp == 0:
		print(' ', 'Fainted')
	elif pokemon.nvStatus != 0:
		print(' ',nonVolatileStatusNumberToType[pokemon.nvStatus])
	else:
		print(' ', 'Healthy')
	print('\nMoves')
	count = 0
	for move in pokemon.moveSet:
		print(' ', move, '-', str(pokemon.movePPCurrent[count]) + '/' + str(pokemon.movePPMax[count]) + 'PP')
		count += 1
	print('\nWould you like to see more info about this Pokemon?')
	choice = getYesOrNo()
	if choice == 1:
		print('\n Stat - Current / Base')
		statList = ['HP   ', 'Atk  ', 'Def  ', 'SpAtk', 'SpDef','Spd  ']
		for i in range(6):
			print(' ', statList[i], '-', pokemon.stats[i], '-', pokemon.baseStats[1])
		print('\nNature')
		print(' ', pokemon.nature)
		print('\nAbility')
		print(' ', pokemon.ability)
		print('\nBack to first page?')
		choice = getYesOrNo()
		if choice == 1:
			getPokemonInfoViewTeam(data, pokemon)
		else:
			return
	else:
		return

def getPokemonInfoViewPC(data, pokemon, page):
	print('')
	print(pokemon.name, '- Level', pokemon.level, pokemon.species)
	if len(pokemon.type) == 1:
		print(pokemon.type[0], 'Type')
	else:
		print(pokemon.type[0], '/', pokemon.type[1], 'Type')
	print('\nHealth')
	print(' ', str(pokemon.hp) + '/' + str(pokemon.maxhp) + 'HP')
	if pokemon.hp == 0:
		print(' ', 'Fainted')
	elif pokemon.nvStatus != 0:
		print(' ',nonVolatileStatusNumberToType[pokemon.nvStatus])
	else:
		print(' ', 'Healthy')
	print('\nMoves')
	count = 0
	for move in pokemon.moveSet:
		print(' ', move, '-', str(pokemon.movePPCurrent[count]) + '/' + str(pokemon.movePPMax[count]) + 'PP')
		count += 1
	print('\nWould you like to see more info about this Pokemon?')
	choice = getYesOrNo()
	if choice == 1:
		print('\nStats')
		statList = ['HP   ', 'Atk  ', 'Def  ', 'SpAtk', 'SpDef','Spd  ']
		for i in range(6):
			print(' ', statList[i], '-', pokemon.stats[i])
		print('\nNature')
		print(' ', pokemon.nature)
		print('\nAbility')
		print(' ', pokemon.ability)
		print('\nBack to first page?')
		choice = getYesOrNo()
		if choice == 1:
			if page == 'withdraw':
				getPokemonInfoViewPC(data, pokemon, 'withdraw')
			else:
				getPokemonInfoViewPC(data, pokemon, 'deposit')
		else:
			if page == 'withdraw':
				withdrawPokemonChoice(data)
			else:
				depositPokemonChoice(data)
	else:
		if page == 'withdraw':
			withdrawPokemonChoice(data)
		else:
			depositPokemonChoice(data)
