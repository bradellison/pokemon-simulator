import random
from random import randint
from operator import add

from pokemonDictionaries import statDict

from text import text


def checkTintedLens(effectiveness, atkPokemon):
	if effectiveness < 1 and effectiveness > 0 and atkPokemon.ability == 'Tinted Lens':
		return effectiveness * 2
	else:
		return effectiveness

def checkShieldDust(atkPokemon, defPokemon):
	if atkPokemon.move.nvEffectChance < 100 and defPokemon.ability == 'Shield Dust':
		return True
	else:
		return False

def checkShedSkin(data, defPokemon):
	if defPokemon.ability == 'Shed Skin' and defPokemon.nvStatus != 0 and randint(1,3) == 3:
		defPokemon.nvStatus = 0
		defPokemon.nvStatusCount = 0
		if defPokemon == data.player.pokemon:
			text(data, data.player.pokemon.name, 'shed it\'s skin and lost it\'s condition!')
		else:
			text(data, 'The opposing', data.enemy.pokemon.name, 'shed it\'s skin and lost it\'s condition!')
		return True
	else:
		return False		

def getAccuracyAbilityMult(data, atkPokemon, defPokemon, move):
	mult = 1
	mult *= checkCompoundEyes(atkPokemon)
	mult *= checkTangledFeet(defPokemon)
	mult *= checkSandVeil(data, defPokemon)
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

def checkSandVeil(data, pokemon):
	if pokemon.ability == 'Sand Veil' and data.environment.weather == 'Sandstorm':
		return 0.8
	else:
		return 1

def checkDrySkinFire(atkPerson, defPerson):
	if defPerson.pokemon.ability == 'Dry Skin' and atkPerson.pokemon.move.type == 'Fire':
		return 1.25
	else:
		return 1

def getAbilityMultDamage(data,atkPerson,atkPokemon,defPerson,defPokemon,move):
	mult = 1
	if atkPerson != 0:
		mult *= checkPinch(atkPokemon,move)
		mult *= checkRivalry(data, atkPokemon, defPokemon)
		mult *= checkAbsorbedAbility(atkPokemon)
		mult *= checkDrySkinFire(atkPerson, defPerson)
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

def checkRivalry(data, atkPokemon, defPokemon):
	if atkPokemon.ability == 'Rivalry' and atkPokemon.gender == defPokemon.gender:
		return 1.2
	else:
		return 1

def checkCompetitive(data, pokemon, statList):
	if pokemon.ability == 'Competitive':
		negative = False
		for i in statList:
			if i < 0:
				negative = True
		if negative == True:
			competitiveEffect = [0,0,0,0,2,0,0,0,0]
			pokemon.statStage = list(map(add, pokemon.statStage, competitiveEffect))
			if pokemon == data.player.pokemon:
				moveStatWordingAbilityOnPlayer(data, competitiveEffect)
			else:
				moveStatWordingAbilityOnEnemy(data, competitiveEffect)

def checkKeenEye(data, pokemon):
	if pokemon.ability == 'Keen Eye':
		if pokemon == data.player.pokemon:
			text(data, data.player.pokemon.name + '\'s keen eye prevented it\'s accuracy from falling!')
		else:
			text(data, 'The opposing', data.enemy.pokemon.name + '\'s keen eye prevented it\'s accuracy from falling!')
		return 1
	else:
		return 0

def checkFlashFireOrSimilar(data, atkPokemon, defPokemon):
	abilityList = ['Flash Fire','Dry Skin']
	abilityTypeDict = {'Flash Fire':'Fire','Dry Skin':'Water'}
	if defPokemon.ability in abilityList:
		if abilityTypeDict[defPokemon.ability] == atkPokemon.move.type:
			if defPokemon == data.player.pokemon:
				text(data, data.player.pokemon.name, 'absorbed the attack with it\'s', data.player.pokemon.ability + '!')
			else:
				text(data, 'The opposing', data.enemy.pokemon.name, 'absorbed the attack with it\'s', data.enemy.pokemon.ability + '!')
			if defPokemon.ability == 'Flash Fire':
				defPokemon.flashFireMult += 0.1
			elif defPokemon.ability == 'Dry Skin':
				gainHealthAbility(data, defPokemon, 'percentage', 25)
			return 1
	return 0

def checkContactAbilities(data, atkPokemon, defPokemon):
	checkStatic(data, atkPokemon, defPokemon)
	checkPoisonPoint(data, atkPokemon, defPokemon)
	checkEffectSpore(data, atkPokemon, defPokemon)

def checkEffectSpore(data, atkPokemon, defPokemon):
	if defPokemon.ability == 'Effect Spore' and atkPokemon.move.variety == 'Physical' and randint(1,5) == 1 and atkPokemon.nvStatus == 0:
		possibleStatusList = [2,3,5]
		atkPokemon.nvStatus = random.choice(possibleStatusList)
		statusToWordDictEffectSpore = {2:'became paralyzed',3:'was put to sleep',5:'became poisoned'}
		wording = statusToWordDictEffectSpore[atkPokemon.nvStatus]
		if atkPokemon == data.player.pokemon:
			text(data, data.player.pokemon.name, wording, 'by coming into contact with the opposing', data.enemy.pokemon.name + '!')
		else:
			text(data, 'The opposing', data.enemy.pokemon.name, wording, 'by coming into contact with', data.player.pokemon.name + '!')

def checkStatic(data, atkPokemon, defPokemon):
	if defPokemon.ability == 'Static' and atkPokemon.move.variety == 'Physical' and randint(1,5) == 1 and atkPokemon.nvStatus == 0:
		atkPokemon.nvStatus = 2
		if atkPokemon == data.player.pokemon:
			text(data, data.player.pokemon.name, 'became paralyzed by coming into contact with the opposing', data.enemy.pokemon.name + '!')
		else:
			text(data, 'The opposing', data.enemy.pokemon.name, 'became paralyzed by coming into contact with', data.player.pokemon.name + '!')

def checkPoisonPoint(data, atkPokemon, defPokemon):
	if defPokemon.ability == 'Poison Point' and atkPokemon.move.variety == 'Physical' and randint(1,5) == 1 and atkPokemon.nvStatus == 0:
		atkPokemon.nvStatus = 5
		if atkPokemon == data.player.pokemon:
			text(data, data.player.pokemon.name, 'became poisoned by coming into contact with the opposing', data.enemy.pokemon.name + '!')
		else:
			text(data, 'The opposing', data.enemy.pokemon.name, 'became poisoned by coming into contact with', data.player.pokemon.name + '!')

def checkStartBattleIntimidate(data):
	statList = [0,-1,0,0,0,0,0,0,0]
	if data.player.pokemon.ability == 'Intimidate':
		data.enemy.pokemon.statStage = list(map(add, data.enemy.pokemon.statStage, [0,-1,0,0,0,0,0,0,0]))
		text(data, data.player.pokemon.name, 'intimidated the opposing', data.enemy.pokemon.name + '!')
		moveStatWordingAbilityOnEnemy(data, statList)
	if data.enemy.pokemon.ability == 'Intimidate':
		data.player.pokemon.statStage = list(map(add, data.player.pokemon.statStage, [0,-1,0,0,0,0,0,0,0]))
		text(data, 'The opposing', data.enemy.pokemon.name, 'intimidated', data.player.pokemon.name + '!')
		moveStatWordingAbilityOnPlayer(data, statList)

def checkIntimidateOnSwitch(data, atkPlayer, defPlayer):
	if atkPlayer.pokemon.ability == 'Intimidate':
		if defPlayer.mist == 0 and defPlayer.pokemon.substitute == 0:
			statList = [0,-1,0,0,0,0,0,0,0]
			defPlayer.pokemon.statStage = list(map(add, defPlayer.pokemon.statStage, statList))
			if atkPlayer.pokemon == data.player.pokemon:
				text(data, data.player.pokemon.name, 'intimidated the opposing', data.enemy.pokemon.name + '!')
				moveStatWordingAbilityOnEnemy(data, statList)
			else:
				text(data, 'The opposing', data.enemy.pokemon.name, 'intimidated', data.player.pokemon.name + '!')
				moveStatWordingAbilityOnPlayer(data, statList)

def moveStatWordingAbilityOnPlayer(data, statList):
	count = 0
	for i in statList:
		if i != 0:
			stat = statDict[count]
			changeForStat = statList[count]
			if changeForStat == 1:
				text(data, data.player.pokemon.name + '\'s', stat, 'raised!')
			if changeForStat == 2:
				text(data, data.player.pokemon.name + '\'s', stat, 'raised sharply!')
			if changeForStat >= 3:
				text(data, data.player.pokemon.name + '\'s', stat, 'raised hugely!')
			if changeForStat == -1:
				text(data, data.player.pokemon.name + '\'s', stat, 'fell!')
			if changeForStat == -2:
				text(data, data.player.pokemon.name + '\'s', stat, 'fell sharply!')
			if changeForStat <= -3:
				text(data, data.player.pokemon.name + '\'s', stat, 'fell hugely!')
		count += 1

def moveStatWordingAbilityOnEnemy(data, statList):
	count = 0
	for i in statList:
		if i != 0:
			stat = statDict[count]
			changeForStat = statList[count]
			if changeForStat == 1:
				text(data, 'The opposing', data.enemy.pokemon.name + '\'s', stat, 'raised!')
			if changeForStat == 2:
				text(data, 'The opposing', data.enemy.pokemon.name + '\'s', stat, 'raised sharply!')
			if changeForStat >= 3:
				text(data, 'The opposing', data.enemy.pokemon.name + '\'s', stat, 'raised hugely!')
			if changeForStat == -1:
				text(data, 'The opposing', data.enemy.pokemon.name + '\'s', stat, 'fell!')
			if changeForStat == -2:
				text(data, 'The opposing', data.enemy.pokemon.name + '\'s', stat, 'fell sharply!')
			if changeForStat <= -3:
				text(data, 'The opposing', data.enemy.pokemon.name + '\'s', stat, 'fell hugely!')
		count += 1

def gainHealthAbility(data, pokemon, typeOfHeal, value):
	if typeOfHeal == 'constant':
		healAmount = value
	elif typeOfHeal == 'percentage':
		healAmount = (pokemon.maxhp / 100) * value
	if healAmount > pokemon.maxhp - pokemon.hp:
		healAmount = pokemon.maxhp - pokemon.hp
	pokemon.hp += healAmount
	if pokemon == data.player.pokemon:
		text(data, data.player.pokemon.name, 'regained', healAmount, 'HP. It has', (data.player.pokemon.hp), '/', (data.player.pokemon.maxhp), 'HP remaining!')
	else:
		text(data, 'The opposing', data.enemy.pokemon.name, 'regained', healAmount, 'HP. It has', (data.enemy.pokemon.hp), '/', (data.enemy.pokemon.maxhp), 'HP remaining!')