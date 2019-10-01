def checkTintedLens(effectiveness):
	if effectiveness < 1:
		return 1
	else:
		return effectiveness

def getAccuracyAbilityMult(atkPokemon, defPokemon, move):
	mult = 1
	mult *= checkCompoundEyes(atkPokemon)
	mult *= checkTangledFeet(defPokemon)
	mult *= checkSandVeil(defPokemon)
	return mult

def checkCompoundEyes(pokemon):
	if pokemon.ability == 'Compound Eyes':
		return 1.3
	else:
		return 1

def checkTangledFeet(pokemon):
	if pokemon.ability == 'Tangled Feet' and pokemon.confused == 1:
		return 0.8
	else:
		return 1

def checkSandVeil(pokemon):
	if pokemon.ability == 'Sand Veil' and environment.weather == 'Sandstorm':
		return 0.8
	else:
		return 1

def getAbilityMultDamage(atkPerson,atkPokemon,defPerson,defPokemon,move):
	mult = 1
	mult *= checkPinch(atkPokemon,move)
	mult *= checkRivalry(atkPokemon, defPokemon)
	mult *= checkAbsorbedAbility(atkPokemon)
	return mult

def checkAbsorbedAbility(atkPokemon):
	abilityList = ['Flash Fire']
	abilityTypeDict = {'Flash Fire':'Fire'}
	if atkPokemon.ability in abilityList:
		if atkPokemon.move.type == abilityTypeDict[atkPokemon.ability]:
			return atkPokemon.flashFireMult
	return 1

def checkPinch(pokemon,move):
	pinchList = ['Blaze','Overgrow','Torrent','Swarm']
	pinchDict = {'Blaze':'Fire','Overgrow':'Grass','Torrent':'Water','Swarm':'Bug'}
	if pokemon.ability in pinchList:
		if pokemon.hp < pokemon.maxhp / 3:
			if move.type == pinchDict[pokemon.ability]:
				return 1.3
	return 1

def checkRivalry(atkPokemon, defPokemon):
	if atkPokemon.ability == 'Rivalry' and atkPokemon.gender == defPokemon.gender:
		return 1.2
	else:
		return 1

def checkCompetitive(pokemon, statEffect):
	if pokemon.ability == 'Competitive':
		negative = False
		for i in statEffect:
			if i < 0:
				negative = True
		if negative == True:
			competitiveEffect = [0,0,0,0,2,0,0,0,0]
			pokemon.statStage = list(map(add, pokemon.statStage, competitiveEffect))
			if pokemon == player.pokemon:
				moveStatWordingOnPlayer(competitiveEffect)
			else:
				moveStatWordingOnEnemy(competitiveEffect)

def checkKeenEye(pokemon):
	if pokemon.ability == 'Keen Eye':
		print('check')
		if pokemon == player.pokemon:
			print(player.pokemon.name + '\'s keen eye prevented it\'s accuracy from falling!')
		else:
			print('The opposing', enemy.pokemon.name + '\'s keen eye prevented it\'s accuracy from falling!')
		return 1
	else:
		return 0


def checkFlashFireOrSimilar(atkPokemon, defPokemon):
	abilityList = ['Flash Fire']
	abilityTypeDict = {'Flash Fire':'Fire'}
	if defPokemon.ability in abilityList:
		if abilityTypeDict[defPokemon.ability] == atkPokemon.move.type:
			if defPokemon == player.pokemon:
				print(player.pokemon.name, 'absorbed the attack with it\'s', player.pokemon.ability + '!')
			else:
				print('The opposing', enemy.pokemon.name, 'absorbed the attack with it\'s', enemy.pokemon.ability + '!')
			defPokemon.flashFireMult += 0.1
			return 1
	return 0

def checkContactAbilities(atkPokemon, defPokemon):
	checkStatic(atkPokemon, defPokemon)
	checkPoisonPoint(atkPokemon, defPokemon)
	checkEffectSpore(atkPokemon, defPokemon)

def checkEffectSpore(atkPokemon, defPokemon):
	if defPokemon.ability == 'Effect Spore' and atkPokemon.move.variety == 'Physical' and randint(1,5) == 1 and atkPokemon.nvStatus == 0:
		possibleStatusList = [2,3,5]
		atkPokemon.nvStatus = random.choice(possibleStatusList)
		statusToWordDictEffectSpore = {2:'became paralyzed',3:'was put to sleep',5:'became poisoned'}
		wording = statusToWordDictEffectSpore[atkPokemon.nvStatus]
		if atkPokemon == player.pokemon:
			print(player.pokemon.name, wording, 'by coming into contact with the opposing', enemy.pokemon.name + '!')
		else:
			print('The opposing', enemy.pokemon.name, wording, 'by coming into contact with', player.pokemon.name + '!')

def checkStatic(atkPokemon, defPokemon):
	if defPokemon.ability == 'Static' and atkPokemon.move.variety == 'Physical' and randint(1,5) == 1 and atkPokemon.nvStatus == 0:
		atkPokemon.nvStatus = 2
		if atkPokemon == player.pokemon:
			print(player.pokemon.name, 'became paralyzed by coming into contact with the opposing', enemy.pokemon.name + '!')
		else:
			print('The opposing', enemy.pokemon.name, 'became paralyzed by coming into contact with', player.pokemon.name + '!')

def checkPoisonPoint(atkPokemon, defPokemon):
	if defPokemon.ability == 'Poison Point' and atkPokemon.move.variety == 'Physical' and randint(1,5) == 1 and atkPokemon.nvStatus == 0:
		atkPokemon.nvStatus = 5
		if atkPokemon == player.pokemon:
			print(player.pokemon.name, 'became poisoned by coming into contact with the opposing', enemy.pokemon.name + '!')
		else:
			print('The opposing', enemy.pokemon.name, 'became poisoned by coming into contact with', player.pokemon.name + '!')

def checkStartBattleIntimidate():
	if player.pokemon.ability == 'Intimidate':
		enemy.pokemon.statStage = list(map(add, enemy.pokemon.statStage, [0,-1,0,0,0,0,0,0,0]))
		print(player.pokemon.name, 'intimidated the opposing', enemy.pokemon.name + '!')
	if enemy.pokemon.ability == 'Intimidate':
		player.pokemon.statStage = list(map(add, player.pokemon.statStage, [0,-1,0,0,0,0,0,0,0]))
		print('The opposing', enemy.pokemon.name, 'intimidated', player.pokemon.name + '!')

def checkIntimidateOnSwitch(atkPlayer, defPlayer):
	if atkPlayer.pokemon.ability == 'Intimidate':
		if defPlayer.mist == 0 and defPlayer.pokemon.substitute == 0:
			defPlayer.pokemon.statStage = list(map(add, defPlayer.pokemon.statStage, [0,-1,0,0,0,0,0,0,0]))
			if atkPlayer.pokemon == player.pokemon:
				print(player.pokemon.name, 'intimidated the opposing', enemy.pokemon.name + '!')
			else:
				print('The opposing', enemy.pokemon.name, 'intimidated', player.pokemon.name + '!')