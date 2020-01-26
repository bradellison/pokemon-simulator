from pokemonDictionaries import pokemonLevelUpMoves, pokemonEvolutionDetails
from getVariableFunctions import getExp, getBaseStats, getPokemonType, getOneMaxPP

def getPokemonLevelUpMoves(pokemon):
	movesByLevel = pokemonLevelUpMoves[pokemon]
	return movesByLevel

def getPokemonEvolutionDetails(pokemon):
	evolutionDetails = pokemonEvolutionDetails[pokemon]
	return evolutionDetails

def getExpYield(data):
	for i in data.player.team:
		if i.level != 100:
			a = 1; e = 1; f = 1; p = 1; s = 1; t = 1; v = 1
			if data.enemy.type != 'Wild':
				a = 1.5
			b = data.enemy.pokemon.BaseExpYield
			if i.item == 'Lucky Egg':
				e = 1.5
			if i.affection >= 2:
				f = 1.2
			l = data.enemy.pokemon.level
			#p is for exp point power, not yet implemented
			if data.player.expShare == 1 and i.inCurrentBattle == 0:
				s = 2
			if data.player.expShare == 0 and i.inCurrentBattle == 0:
				return
			#t is for traded pokemon, not implemented
			#v is for pokemon that could have evolved already, not implemented
			expYield = int((a * b * e * f * l * p * t * v) / (7 * s))
			i.exp += expYield
			print(i.name, 'gained', expYield, 'exp!')
			while i.exp > i.nextLevelExp and i.level < 100:
				i.level += 1
				print(i.name, 'went up one level and is now level', str(i.level) + '!')
				i.nextLevelExp = getExp(i.species, i.level + 1)
				getMoveLearn(i)
				evolutionDetails = getPokemonEvolutionDetails(i.species)
				if evolutionDetails['Evolve'] == 'Yes':
					if evolutionDetails['Type'] == 'Level':
						if i.level >= evolutionDetails['Detail']:
							i.shouldEvolve = 1
			print('')

def evolvePokemon(pokemon):
	evolutionDetails = getPokemonEvolutionDetails(pokemon.species)
	evolveInto = evolutionDetails['Pokemon']
	print(pokemon.name, 'evolved into', evolveInto + '!')
	if pokemon.name == pokemon.species:
		pokemon.name = evolveInto
	pokemon.species = evolveInto
	print(pokemon.species)
	pokemon.baseStats = getBaseStats(pokemon.species)
	pokemon.type = getPokemonType(pokemon)
	getMoveLearn(pokemon)

def getMoveLearn(i):
	tempDict = getPokemonLevelUpMoves(i.species)
	if i.level in tempDict:
		newMove = tempDict[i.level]
		# wants to learn a move
		if newMove not in i.moveSet:
			print('')
			if len(i.moveSet) < 4:
				i.moveSet.append(newMove)
				newPP = getOneMaxPP(newMove)
				i.movePPMax.append(newPP)
				i.movePPCurrent.append(newPP)
				print(i.name, 'learnt', newMove + '!')
			else:
				print(i.name, 'wants to learn a new move! What move should be forgotten?')
				getMoveLearnReplace(i, newMove, i.name)

def getMoveLearnReplace(pokemon, newMove, name):
	moveSet = pokemon.moveSet
	print('Current Moves:')
	for i in range(1,5):
		print('', i, '-', moveSet[i-1])
	print('New Move:')
	print('', i+1, '-', newMove)
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput < 5 and choiceInput > 0:
				print(name, 'forgot', moveSet[choiceInput - 1], 'and learnt', newMove + '!')
				moveSet[choiceInput - 1] = newMove
				newPP = getOneMaxPP(newMove)
				pokemon.movePPMax[choiceInput - 1] = newPP
				pokemon.movePPCurrent[choiceInput - 1] = newPP
				return
			elif choiceInput == 5:
				print(name, 'did not learn', newMove + '!')
				return
			else:
				print("Please choose a move from the list above!")
		except ValueError:
			print("Please choose a move from the list above!")		