from choicesFunctions import getOption
from pokemonDictionaries import pokemonLevelUpMoves, pokemonEvolutionDetails
from getVariableFunctions import getExp, getBaseStats, getPokemonSprite, getPokemonType, getOneMaxPP, gethpStat, getStats
from screen import drawScreen
from text import text
from textTools import onlyTextBox, onlyTextBoxWithOptions


def getPokemonLevelUpMoves(pokemon):
	movesByLevel = pokemonLevelUpMoves[pokemon]
	return movesByLevel

def getPokemonEvolutionDetails(pokemon):
	evolutionDetails = pokemonEvolutionDetails[pokemon]
	return evolutionDetails

def getExpYield(data):
	inBattleCount = 0
	for j in data.player.team:
		if j.inCurrentBattle == 1:
			inBattleCount += 1
	for i in data.player.team:
		if i.level != 100:
			a = 1; e = 1; f = 1; p = 1; s = 1; t = 1; v = 1; x = 1; y = 1; z = inBattleCount
			if data.enemy.type != 'Wild':
				a = 1.5
			b = data.enemy.pokemon.BaseExpYield
			if i.item == 'Lucky Egg':
				e = 1.5
			if i.affection >= 2:
				f = 1.2
			l = data.enemy.pokemon.level
			if data.settings.settingsDict["Triple XP"]:
				x = 3
			if data.settings.settingsDict["10x XP"]:
				y = 100
			#p is for exp point power, not yet implemented
			if data.player.expShare == 1 and i.inCurrentBattle == 0:
				s = 2
			if data.player.expShare != 0 or i.inCurrentBattle != 0:
				#t is for traded pokemon, not implemented
				#v is for pokemon that could have evolved already, not implemented
				expYield = int((a * b * e * f * l * p * t * v * x * y) / (7 * s * z))
				i.exp += expYield
				text(data, i.name, 'gained', expYield, 'exp!')
				while i.exp > i.nextLevelExp and i.level < 100:
					levelUpPokemon(data, i)
					text(data, i.name, 'went up one level and is now level', str(i.level) + '!')
					i.lastLevelExp = getExp(i.species, i.level)
					i.nextLevelExp = getExp(i.species, i.level + 1)
					getMoveLearn(data, i)
					evolutionDetails = getPokemonEvolutionDetails(i.species)
					if evolutionDetails['Evolve'] == 'Yes':
						if evolutionDetails['Type'] == 'Level':
							if i.level >= evolutionDetails['Detail']:
								i.shouldEvolve = 1

def levelUpPokemon(data, pokemon):
	pokemon.level += 1
	oldMaxHealth = pokemon.maxhp
	pokemon.stats = getStats(pokemon)
	pokemon.maxhp = pokemon.stats[0]
	healthIncrease = pokemon.maxhp - oldMaxHealth
	pokemon.hp += healthIncrease


def evolvePokemon(data, pokemon):
	evolutionDetails = getPokemonEvolutionDetails(pokemon.species)
	evolveInto = evolutionDetails['Pokemon']
	oldPokemonName = pokemon.name
	if pokemon.name == pokemon.species:
		pokemon.name = evolveInto
	pokemon.species = evolveInto
	pokemon.sprite = getPokemonSprite(pokemon.species)
	text(data, oldPokemonName, 'evolved into', evolveInto + '!')
	pokemon.species = evolveInto
	pokemon.baseStats = getBaseStats(pokemon.species)
	pokemon.type = getPokemonType(pokemon)
	oldMaxHealth = pokemon.maxhp
	pokemon.maxhp = gethpStat(pokemon)
	
	increase = pokemon.maxhp - oldMaxHealth
	pokemon.hp += increase
	getMoveLearn(data, pokemon, justEvolved=True)

def getMoveLearn(data, i, justEvolved=False):
	tempDict = getPokemonLevelUpMoves(i.species)
	levels = [i.level]
	if justEvolved:
		levels.append(1)
	for level in levels:
		if level in tempDict:
			newMove = tempDict[level]
			# wants to learn a move
			if newMove not in i.moveSet:
				if len(i.moveSet) < 4:
					i.moveSet.append(newMove)
					newPP = getOneMaxPP(newMove)
					i.movePPMax.append(newPP)
					i.movePPCurrent.append(newPP)
					drawScreen(data)
					onlyTextBox(i.name + " learnt " + newMove + "!", pauseAfter=True)
				else:
					drawScreen(data)
					onlyTextBox(i.name + ' wants to learn ' + newMove + '! What move should be forgotten?', pauseAfter=True)
					getMoveLearnReplace(data, i, newMove, i.name)

def getMoveLearnReplace(data, pokemon, newMove, name):
	moveSet = pokemon.moveSet.copy()
	moveSet.append(newMove)
	moveToForget = "None"

	while moveToForget == "None":
		drawScreen(data)
		onlyTextBoxWithOptions("Which move to forget?   5 - Don't learn " + newMove, pokemon.moveSet)
		moveToForget = getOption(moveSet, backWithE=False)

	if moveToForget == newMove:
		drawScreen(data)
		onlyTextBox(name + " did not learn " + newMove + "!", pauseAfter=True)
	else:
		drawScreen(data)
		onlyTextBox(name + " forgot " + moveToForget + " and learnt " + newMove + "!", pauseAfter=True)
		index = pokemon.moveSet.index(moveToForget)
		pokemon.moveSet[index] = newMove
		newPP = getOneMaxPP(newMove)
		pokemon.movePPMax[index] = newPP
		pokemon.movePPCurrent[index] = newPP
			