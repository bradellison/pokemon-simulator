import operator
import time
import random
import math
#import pygame
import os
import pickle

from random import randint
from operator import add

from pokemonDictionaries import *
from moveDictionaries import *
from typeInfo import *

####### CLASSES ######

class Player(object):
	def __init__(self):
		self.name = 'Brad'
		self.type = 'Player'
		self.defaultTeam = []
		self.team = []
		self.livingPokemon = 0
		self.activePokemon = 0
		self.money = 5000
		self.id = randint(1,65535)
		self.badges = [0,0,0,0,0,0,0,0]
		self.expShare = 0
		self.lightScreen = 0
		self.lightScreenCount = 0
		self.reflect = 0
		self.reflectCount = 0
		self.mist = 0
		self.mistCount = 0

class PC(object):
	def __init__(self):
		self.boxes = []

class Box(object):
	def __init__(self):
		self.inventory = []

class Bag(object):
	def __init__(self):
		self.balls = []
		self.medicine = []

class Medicine(object):
	def __init__(self, name, quantity):
		self.name = name
		self.heal = getMedicineHeal(name)
		self.quantity = quantity

class Ball(object):
	def __init__(self, name, quantity):
		self.name = name
		self.modifier = getBallModifier(name)
		self.quantity = quantity

class Enemy(object):
	def __init__(self, type, name, team, prizeMoney, text):
		self.type = type
		self.name = name
		self.team = team
		self.livingPokemon = 0
		self.prizeMoney = prizeMoney
		self.text = text
		self.lightScreen = 0
		self.lightScreenCount = 0
		self.reflect = 0
		self.reflectCount = 0
		self.mist = 0
		self.mistCount = 0

class Pokemon(object):
	def __init__(self, species, level):
		self.species = species
		self.name = species
		self.level = level
		self.iv = getRandomIV()
		self.ev = [0,0,0,0,0,0]
		self.baseStats = getBaseStats(species)
		self.stats = getStats(self)
		self.statStage = [0,0,0,0,0,0,0,0,0]
		self.maxhp = self.stats[0]
		self.hp = self.stats[0]
		self.nature = 'None'
#		self.form = 
		self.gender = getGender(species)
		self.ability = 'None'
		self.type = getPokemonType(self)
		self.item = 'None'
		self.moveSet = getMoveSet(self)
		self.movePPMax = getMaxPP(self)
		self.movePPCurrent = getMaxPP(self)
		self.nvStatus = 0
		self.nvStatusCount = 0 
		self.expGroup = getExpGroup(species)
		self.BaseExpYield = getExpYieldBase(species)
		self.exp = getExp(species, level)
		self.nextLevelExp = getExp(species, level+1)
		self.move = Move('None')
		self.previousMove = 0
		self.inCurrentBattle = 0
		self.affection = 0
		self.shouldEvolve = 0
		self.catchRate = getPokemonCatchRate(species)
		self.criticalMove = 0
		self.lockedInMoveNumber = 0
		self.immune = 0
		self.flinch = 0
		self.confused = 0
		self.confusedCount = 0
		self.bind = 0
		self.bindCount = 0
		self.clamp = 0
		self.clampCount = 0
		self.fireSpin = 0
		self.fireSpinCount = 0
		self.wrap = 0
		self.wrapCount = 0
		self.leechSeed = 0
		self.previousDamage = 0
		self.bide = 0
		self.bideDamage = 0
		self.rage = 0
		self.rageCount = 0
		self.substitute = 0
		self.substituteHealth = 0
		self.disabled = 0
		self.disabledMove = 0
		self.disabledCount = 0
		self.transform = 0

class Environment(object):
	def __init__(self, location, weather):
		self.location = location
		self.weather = weather
		self.weathercount = 0
		self.payDayExtra = 0
		self.battleEnd = 0

class Move(object):
	def __init__(self, moveName):
		moveList = moveInfo[moveName]
		self.move = moveName
		self.type = moveList[1]
		self.variety = moveList[2]
		self.damage = moveList[3]
		self.accuracy = moveList[4]
		self.pp = moveList[5]
		self.description = moveList[6]
		self.target = moveList[7]
		self.priority = moveList[8]
		self.turnsToComplete = moveList[9]
		self.multiAttack = moveList[10]
		self.multiAttackMin = moveList[11]
		self.multiAttackMax = moveList[12]
		self.nvEffect = moveList[13]
		self.nvEffectChance = moveList[14]
		self.vEffect = moveList[15]
		self.vEffectChance = moveList[16]
		self.statEffect = moveList[17]
		self.statEffectChance = moveList[18]
		self.critBonus = moveList[19]
		self.attackOnTurnNumber = moveList[20]
		self.grantsImmunity = moveList[21]
		self.flinch = moveList[22]
		self.flinchChance = moveList[23]
		self.healthSteal = moveList[24]
		self.currentEffectiveness = 1

####### GET VARIABLE FUNCTIONS #######

def getRandomIV():
	IV = []
	for i in range(6):
		x = randint(1,31)
		IV.append(x)
	return IV

def getBaseStats(species):
	stats = pokemonStats[species]
	return stats

def gethpStat(id):
	species = id.species; level = id.level; iv = id.iv; baseStats = id.baseStats	
	return int(((2 * baseStats[0] + iv[0])* level / 100 ) + level + 10)

def getAtkStat(id):
	species = id.species; level = id.level; iv = id.iv; baseStats = id.baseStats
	return int(((2 * baseStats[1] + iv[1]) * level / 100) + 5)

def getDefStat(id):
	species = id.species; level = id.level; iv = id.iv; baseStats = id.baseStats
	return int(((2 * baseStats[2] + iv[2]) * level / 100) + 5)

def getSpAtkStat(id):
	species = id.species; level = id.level; iv = id.iv; baseStats = id.baseStats
	return int(((2 * baseStats[3] + iv[3]) * level / 100) + 5)

def getSpDefStat(id):
	species = id.species; level = id.level; iv = id.iv; baseStats = id.baseStats
	return int(((2 * baseStats[4] + iv[4]) * level / 100) + 5)

def getSpdStat(id):
	species = id.species; level = id.level; iv = id.iv; baseStats = id.baseStats
	return int(((2 * baseStats[5] + iv[5]) * level / 100) + 5)

def getStats(id):
	return [gethpStat(id),getAtkStat(id),getDefStat(id),getSpAtkStat(id),getSpDefStat(id),getSpdStat(id)]

def getBattlehpStat(id):
	return id.stats[0]

def getBattleAtkStat(id):
	stat = id.stats[1]; statStage = id.statStage[1]; nvStatus = id.nvStatus
	mult = pokemonStatStageToMult[statStage]
	if nvStatus == 1:
		mult /= 2
	return int(mult * stat)

def getBattleDefStat(id):
	stat = id.stats[2]; statStage = id.statStage[2]
	mult = pokemonStatStageToMult[statStage]
	return int(mult * stat)

def getBattleSpAtkStat(id):
	stat = id.stats[3]; statStage = id.statStage[3]
	mult = pokemonStatStageToMult[statStage]
	return int(mult * stat)

def getBattleSpDefStat(id):
	stat = id.stats[4]; statStage = id.statStage[4]
	mult = pokemonStatStageToMult[statStage]
	return int(mult * stat)

def getBattleSpdStat(id):
	stat = id.stats[5]; statStage = id.statStage[5]
	mult = pokemonStatStageToMult[statStage]
	return int(mult * stat)

def getBattleAccStat(id):
	stat = 1; statStage = id.statStage[6]
	mult = pokemonStatStageToMult[statStage]
	return (mult * stat)

def getBattleEvasStat(id):
	stat = 1; statStage = id.statStage[7]
	mult = pokemonStatStageToMult[statStage]
	return (mult * stat)

def getBattleCritStage(id):
	return id.statStage[8]

def getBattleStats(id):
	return [getBattlehpStat(id),getBattleAtkStat(id),getBattleDefStat(id),getBattleSpAtkStat(id),getBattleSpDefStat(id),getBattleSpdStat(id),getBattleAccStat(id),getBattleEvasStat(id)]

def getPokemonType(id):
	fromDict = pokemonTypes[id.species]
	pokemonType = [fromDict['Type One']]
	if fromDict['Type Two'] != 'Null':
		pokemonType.append(fromDict['Type Two'])
	return pokemonType

def getPokemonCatchRate(id):
	return pokemonCatchRates[id]

def getExpGroup(species):
	expGroup = pokemonExpGroup[species]
	return expGroup

def getExpYieldBase(species):
	yieldInfo = pokemonYields[species]
	expYieldBase = yieldInfo[0]
	return expYieldBase

def getExp(pokemon,level):
	expGroup = getExpGroup(pokemon)
	n = level
	if expGroup == 'Erratic':
		if n <= 50:
			exp = ((n**3)*(100-n))/50
		if 50 < n <= 68:
			exp = ((n**3)*(150-n))/100
		if 68 < n <= 98:
			exp = (((n**3)*((1911-10*n)/3))/500)
		if 98 < n <= 100:
			exp = ((n**3)*(160-n))/100
	if expGroup == 'Fast':
		exp = (4*n**3)/5
	if expGroup == 'Medium Fast':
		exp = n**3
	if expGroup == 'Medium Slow':
		exp = (6/5)*n**3 - 15*n**2 + 100*n - 140
	if expGroup == 'Slow':
		exp = (5*n**3)/4
	if expGroup == 'Fluctuating':
		if n <= 15:
			exp = n**3 * ((((n+1)/3)+24)/50)
		if 15 < n <= 36:
			exp = n**3 * ((n+14/50))
		if 36 < n <= 100:
			exp = n**3 * (((n/2)+32)/50)
	return int(exp)

def getGender(pokemon):
	num = randint(1,100)
	if num > 50:
		return 'Male'
	else:
		return 'Female'

def getMoveSet(id):
	allMoves = []
	possibleMovesByLevel = pokemonPossibleMovesByLevel[id.species]
	for i in range(1,id.level+1):
		if i in possibleMovesByLevel:
			allMoves.append(possibleMovesByLevel[i])
	if len(allMoves) <= 4:
		return allMoves
	moveSet = random.sample(allMoves,4)
	return moveSet

def getMaxPP(id):
	ppList = []
	moveSet = id.moveSet
	for i in moveSet:
		moveDetails = moveInfo[i]
		ppList.append(moveDetails[5])
	return ppList

def getOneMaxPP(move):
	moveDetails = moveInfo[move]
	return moveDetails[5]

#def getPokemonMovesByLevel(pokemon):
#	movesByLevel = pokemonPossibleMovesByLevel[pokemon]
#	return movesByLevel

def getPokemonLevelUpMoves(pokemon):
	movesByLevel = pokemonLevelUpMoves[pokemon]
	return movesByLevel

def getPokemonEvolutionDetails(pokemon):
	evolutionDetails = pokemonEvolutionDetails[pokemon]
	return evolutionDetails

####### BAG FUNCTIONS ########

ballCatchModifiers = {'PokeBall':1,'Great Ball':2,'Ultra Ball':3,'Master Ball':'Master'}
statusCatchModifiers = {0:1,1:1.5,2:1.5,3:2,4:2,5:1.5,6:1.5}

medicineHealAmount = {'Potion':20,'Super Potion':50,'Hyper Potion':100,'Max Potion':10000,'Full Restore':10000}

def getBallModifier(ball):
	return ballCatchModifiers[ball]

def getStatusCatchModifiers():
	return statusCatchModifiers[enemy.pokemon.nvStatus]

def getMedicineHeal(medicine):
	return medicineHealAmount[medicine]

####### BATTLE FUNCTIONS #######

def getStabBonus(id,move):
	pokemonType = id.type; moveType = move.type
	if moveType in pokemonType:
		return 1.5
	else:
		return 1

def getTypeEffectiveness(id,move):
	pokemonType = id.type; moveType = move.type
	effectiveDict = allType[moveType]
	effectiveness = 1
	for i in pokemonType:
		effectiveness *= effectiveDict[i]
	return effectiveness

def getHitOrMiss(atkPokemon,defPokemon,move):
	if defPokemon.immune == 1:
		return 'Miss'
	pokemonAccuracy = getBattleAccStat(atkPokemon)
	pokemonEvasiveness = getBattleEvasStat(defPokemon)
	moveAccuracy = move.accuracy
	chance = int(pokemonAccuracy * moveAccuracy / pokemonEvasiveness)
	randomOf100 = randint(1,100)
	if chance >= randomOf100:
		return 'Hit'
	else:
		return 'Miss'

def getHitOrConfused(atkPokemon):
	confused = 0
	if atkPokemon.confused == 1:
		atkPokemon.confusedCount -= 1
		if atkPokemon.confusedCount <= 0:
			confused = 2
			atkPokemon.confused = 0
			return confused
		chance = randint(1,2)
		if chance == 1:
			confused = 1
	return confused

def getCriticalHit(atkPokemon,move):
	moveCritBonus = move.critBonus
	pokemonCritBonus = getBattleCritStage(atkPokemon)
	totalCritBonus = moveCritBonus + pokemonCritBonus
	chance24 = pokemonCritStageToMult[totalCritBonus]
	if chance24 >= randint(1,24):
		return 2
	else:
		return 1

def getMoveDamage(atkPerson,atkPokemon,defPerson,defPokemon,move):
	stabBonus = getStabBonus(atkPokemon,move)
	effectiveness = getTypeEffectiveness(defPokemon,move)
	move.currentEffectiveness = effectiveness
	critical = getCriticalHit(atkPokemon,move)
	wall = 1
	if critical == 2:
		atkPokemon.criticalMove = 1
	if move.variety == 'Physical':
		aStat = getBattleAtkStat(atkPokemon)
		dStat = getBattleDefStat(defPokemon)
		if defPerson != 0:
			if defPerson.reflect == 1:
				wall = 2
	if move.variety == 'Special':
		aStat = getBattleSpAtkStat(atkPokemon)
		dStat = getBattleSpDefStat(defPokemon)
		if defPerson != 0:
			if defPerson.lightScreen == 1:
				wall = 2
	damage = int((((((2 * atkPokemon.level / 5) + 2) * aStat * move.damage / dStat) / 50) + 2) * stabBonus * effectiveness * critical / wall * float(randint(85,100)/100))
	if defPokemon.hp - damage < 0:
		damage = defPokemon.hp
	return damage

def getTurnOrder(myPokemon,enemyPokemon,myMove,enemyMove):
	if myMove.priority == enemyMove.priority:
		mySpd = getBattleSpdStat(myPokemon)
		enemySpd = getBattleSpdStat(enemyPokemon)
		if mySpd > enemySpd:
			return 'myPokemonFirst'
		elif enemySpd > mySpd:
			return 'enemyPokemonFirst'
		else:
			thisList = ['myPokemonFirst','enemyPokemonFirst']
			return random.choice(thisList)
	elif myMove.priority > enemyMove.priority:
		return 'myPokemonFirst'
	else:
		return 'enemyPokemonFirst'

def battleStartPhrasing():
	if enemy.type == 'Wild':
		print('A wild', enemy.pokemon.name, 'appeared! Go,', player.pokemon.name + '!')
	if enemy.type == 'Trainer' or enemy.type == 'Gym Leader':
		print('The', enemy.type, enemy.name, 'sent out a', enemy.pokemon.name + '.', 'Go,', player.pokemon.name + '!')

def battleEnd():
	if enemy.type == 'Wild':
		print('You defeated the wild', enemy.pokemon.name)
	if enemy.type == 'Trainer' or enemy.type == 'Gym Leader':
		print('You defeated', enemy.type, enemy.name + '.', 'You received', enemy.prizeMoney, 'for winning!')

def battleChoiceInput():
	print('What would you like to do? \n 1 - Fight \n 2 - Pokemon \n 3 - Bag \n 4 - Run')
	while True:
		try:
			choiceInput = input('-- ')
			if choiceInput == 'Fight' or int(choiceInput) == 1:
				return 'Fight'
			if choiceInput == 'Pokemon' or int(choiceInput) == 2:
				return 'Pokemon'
			if choiceInput == 'Bag' or int(choiceInput) == 3:
				return 'Bag'
			if choiceInput == 'Run' or int(choiceInput) == 4:
				return 'Run'
			print("Please choose an option from the list above!")
		except ValueError:
			print("Please choose an option from the list above!")

def getTotalPP(pokemon):
	totalPP = 0
	for i in range(len(pokemon.moveSet)):
		totalPP += pokemon.movePPCurrent[i]
	return totalPP

def moveChoiceInput():
	totalPP = getTotalPP(player.pokemon)
	if totalPP == 0:
		return 'Struggle'
	moveSet = player.pokemon.moveSet
	for i in range(len(moveSet)):
		print('', i + 1, '-', moveSet[i], '-', str(player.pokemon.movePPCurrent[i]) + '/' + str(player.pokemon.movePPMax[i]), 'PP')
	print('', len(moveSet) + 1, '- Back')
	while True:
		try:
			choiceInput = input('-- ')
			if int(choiceInput) == 1 and len(moveSet) >= 1:
				if player.pokemon.movePPCurrent[0] > 0:
					if player.pokemon.moveSet[0] != player.pokemon.disabledMove:
						player.pokemon.movePPCurrent[0] -= 1
						return moveSet[0]
					print('That move is disabled! Please choose another!')
				else:
					print('No PP remaining! Please choose another move!')
			elif int(choiceInput) == 2 and len(moveSet) >= 2:
				if player.pokemon.movePPCurrent[1] > 0:
					if player.pokemon.moveSet[1] != player.pokemon.disabledMove:
						player.pokemon.movePPCurrent[1] -= 1
						return moveSet[1]
					print('That move is disabled! Please choose another!')
				else:
					print('No PP remaining! Please choose another move!')
			elif int(choiceInput) == 3 and len(moveSet) >= 3:
				if player.pokemon.movePPCurrent[2] > 0:
					if player.pokemon.moveSet[2] != player.pokemon.disabledMove:
						player.pokemon.movePPCurrent[2] -= 1
						return moveSet[2]
					print('That move is disabled! Please choose another!')
				else:
					print('No PP remaining! Please choose another move!')
			elif int(choiceInput) == 4 and len(moveSet) >= 4:
				if player.pokemon.movePPCurrent[3] > 0:
					if player.pokemon.moveSet[3] != player.pokemon.disabledMove:
						player.pokemon.movePPCurrent[3] -= 1
						return moveSet[3]
					print('That move is disabled! Please choose another!')
				else:
					print('No PP remaining! Please choose another move!')
			elif choiceInput == 'Back' or int(choiceInput) == len(moveSet) + 1:
				return 'Back'
			print("Please choose a move from the list above!")
		except ValueError:
			print("Please choose a move from the list above!")	

def preTurnNVStatusCheck(person):
	if person.pokemon.nvStatus == 2:
		print(person.pokemon.name, 'is paralyzed and may not be able to move!')
		i = randint(1,4)
		if i == 1:
			print(person.pokemon.name, 'couldn\'t move!')
			return 1
		return 0
	elif person.pokemon.nvStatus == 3:
		print(person.pokemon.name, 'is sleeping!')
		person.pokemon.nvStatusCount -= 1
		if person.pokemon.nvStatusCount > 0:
			return 1
		person.pokemon.nvStatus = 0
		print(person.pokemon.name, 'woke up!')
		return 0
	elif person.pokemon.nvStatus == 4:
		i = randint(1,5)
		if i == 1:
			person.pokemon.nvStatus = 0
			print(person.pokemon.name, 'thawed out!')
			return 0
		else:
			print(person.pokemon.name, 'is frozen and couldn\'t move!')
			return 1
	else:
		return 0

def postTurnNVStatusCheckPlayer():
	if player.pokemon.nvStatus == 1:
		damage = int(player.pokemon.maxhp / 16)
		if damage > player.pokemon.hp:
			damage = player.pokemon.hp
		player.pokemon.hp -= damage
		print(player.pokemon.name, 'took', damage, 'HP damage due to it\'s burn! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!')
	elif player.pokemon.nvStatus == 5:
		damage = int(player.pokemon.maxhp / 8)
		if damage > player.pokemon.hp:
			damage = player.pokemon.hp
		player.pokemon.hp -= damage
		print(player.pokemon.name, 'took', damage, 'HP damage due to being poisoned! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!')
	elif player.pokemon.nvStatus == 6:
		player.pokemon.nvStatusCount += 1
		damage = int(player.pokemon.maxhp * player.pokemon.nvStatusCount / 16)
		if damage > player.pokemon.hp:
			damage = player.pokemon.hp
		player.pokemon.hp -= damage
		print(player.pokemon.name, 'took', damage, 'HP damage due to being poisoned! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!')

def postTurnNVStatusCheckEnemy():
	if enemy.pokemon.nvStatus == 1:
		damage = int(enemy.pokemon.maxhp / 16)
		if damage > enemy.pokemon.hp:
			damage = enemy.pokemon.hp
		enemy.pokemon.hp -= damage
		print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s burn! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!')
	elif enemy.pokemon.nvStatus == 5:
		damage = int(enemy.pokemon.maxhp / 8)
		if damage > enemy.pokemon.hp:
			damage = enemy.pokemon.hp
		enemy.pokemon.hp -= damage
		print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage due to being poisoned! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!')
	elif enemy.pokemon.nvStatus == 6:
		enemy.pokemon.nvStatusCount += 1
		damage = int(enemy.pokemon.maxhp * enemy.pokemon.nvStatusCount / 16)
		if damage > enemy.pokemon.hp:
			damage = enemy.pokemon.hp
		enemy.pokemon.hp -= damage
		print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage due to being poisoned! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!')

def getExpYield():
	for i in player.team:
		if i.level != 100:
			a = 1; e = 1; f = 1; p = 1; s = 1; t = 1; v = 1
			if enemy.type != 'Wild':
				a = 1.5
			b = enemy.pokemon.BaseExpYield
			if i.item == 'Lucky Egg':
				e = 1.5
			if i.affection >= 2:
				f = 1.2
			l = enemy.pokemon.level
			#p is for exp point power, not yet implemented
			if player.expShare == 1 and i.inCurrentBattle == 0:
				s = 2
			if player.expShare == 0 and i.inCurrentBattle == 0:
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

def getEffectivenessWording(i):
	effectivenessWording = effectivenessScale[i]
	return effectivenessWording

def getMultiAttackCount(move):
	return randint(move.multiAttackMin,move.multiAttackMax)

def checkHealthSteal(atkPokemon, atkMove, damage):
	healAmount = 0
	if atkMove.healthSteal == 1 and atkPokemon.hp < atkPokemon.maxhp:
		healAmount = damage / 2
		if healAmount > atkPokemon.maxhp - atkPokemon.hp:
			healAmount = atkPokemon.maxhp - atkPokemon.hp
		atkPokemon.hp += healAmount
	return healAmount

def checkHitSubstitute(atkPokemon,defPokemon,damage):
	if defPokemon.substitute == 1:
		print('The substitute protected', defPokemon.name, 'from the attack!')
		if defPokemon.substituteHealth < damage:
			damage = defPokemon.substituteHealth
		defPokemon.substituteHealth -= damage
		if defPokemon.substituteHealth == 0:
			print('The substitute was destroyed!')
			defPokemon.substitute = 0
		return 1
	else:
		return 0


def moveDealDamagePlayer():
	if player.pokemon.move.multiAttack == 1:
		numberOfHits = getMultiAttackCount(player.pokemon.move)
	else:
		numberOfHits = 1
	actualHits = 0
	totalDamage = 0
	while numberOfHits > 0 and enemy.pokemon.hp > 0:
		damage = getMoveDamage(player,player.pokemon,enemy,enemy.pokemon,player.pokemon.move)
		substitute = checkHitSubstitute(player.pokemon, enemy.pokemon, damage)
		if substitute == 1:
			damage = 0
		enemy.pokemon.hp -= damage	
		effectivenessWording = getEffectivenessWording(player.pokemon.move.currentEffectiveness)
		print('It did', damage, 'damage' + effectivenessWording, 'The opposing', enemy.pokemon.name, 'has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!')		
		if player.pokemon.criticalMove == 1:
			print('It was a critical hit!')
			player.pokemon.criticalMove = 0
		actualHits += 1
		numberOfHits -= 1
		totalDamage += damage
		healedAmount = checkHealthSteal(player.pokemon, player.pokemon.move, damage)
		checkAddBideDamage(enemy.pokemon, damage)
		checkRageBonus(enemy.pokemon)
		if healedAmount > 0:
			print(player.pokemon.name, 'gained', healedAmount, 'HP!')
	player.pokemon.previousDamage = totalDamage
	if player.pokemon.move.multiAttack == 1:
		print('It hit the enemy', actualHits, 'times!')

def moveDealDamageEnemy():
	if enemy.pokemon.move.multiAttack == 1:
		numberOfHits = getMultiAttackCount(enemy.pokemon.move)
	else:
		numberOfHits = 1
	actualHits = 0
	totalDamage = 0
	while numberOfHits > 0 and player.pokemon.hp > 0:
		damage = getMoveDamage(enemy,enemy.pokemon,player,player.pokemon,enemy.pokemon.move)
		substitute = checkHitSubstitute(enemy.pokemon, player.pokemon, damage)
		if substitute == 1:
			damage = 0
		player.pokemon.hp -= damage
		effectivenessWording = getEffectivenessWording(enemy.pokemon.move.currentEffectiveness)
		print('It did', damage, 'damage' + effectivenessWording, player.pokemon.name, 'has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!')
		if enemy.pokemon.criticalMove == 1:
			print('It was a critical hit!')
			enemy.pokemon.criticalMove = 0
		actualHits += 1
		numberOfHits -= 1
		totalDamage += damage
		healedAmount = checkHealthSteal(enemy.pokemon, enemy.pokemon.move, damage)
		checkAddBideDamage(player.pokemon, damage)
		checkRageBonus(player.pokemon)
		if healedAmount > 0:
			print('The opposing', player.pokemon.name, 'gained', healedAmount, 'HP!')
	enemy.pokemon.previousDamage = totalDamage
	if enemy.pokemon.move.multiAttack == 1:
		print('It hit', player.pokemon.name, actualHits, 'times!')

def moveDamageConfusion(atkPokemon):
	move = Move('Hit Self')
	damage = getMoveDamage(0,atkPokemon,0,atkPokemon,move)
	if damage > atkPokemon.hp:
		damage = atkPokemon.hp
	return damage

def moveStatChangePlayer():
	chance = randint(1,100)
	if chance <= player.pokemon.move.statEffectChance:
		if player.pokemon.move.target == 'Self':
			player.pokemon.statStage = list(map(add, player.pokemon.statStage, player.pokemon.move.statEffect))
			moveStatWordingOnPlayer(player.pokemon.move.statEffect)
			statStageMax(player.pokemon)
		if player.pokemon.move.target == 'Enemy':
			if enemy.mist == 0 and enemy.pokemon.substitute == 0:
				enemy.pokemon.statStage = list(map(add, enemy.pokemon.statStage, player.pokemon.move.statEffect))
				moveStatWordingOnEnemy(player.pokemon.move.statEffect)
				statStageMax(enemy.pokemon)
			else:
				print('But it failed!')

def moveStatChangeEnemy():
	chance = randint(1,100)
	if chance <= enemy.pokemon.move.statEffectChance:
		if enemy.pokemon.move.target == 'Self':
			enemy.pokemon.statStage = list(map(add, enemy.pokemon.statStage, enemy.pokemon.move.statEffect))
			moveStatWordingOnEnemy(enemy.pokemon.move.statEffect)
			statStageMax(enemy.pokemon)
		if enemy.pokemon.move.target == 'Enemy':
			if player.mist == 0 and player.pokemon.substitute == 0:
				player.pokemon.statStage = list(map(add, player.pokemon.statStage, enemy.pokemon.move.statEffect))
				moveStatWordingOnPlayer(enemy.pokemon.move.statEffect)
				statStageMax(player.pokemon)
			else:
				print('But it failed!')

def statStageMax(pokemon):
	statStage = pokemon.statStage
	if pokemon == player.pokemon:
		count = 0
		for i in statStage:
			if i > 6:
				player.pokemon.statStage[count] = 6
			elif i < -6:
				player.pokemon.statStage[count] = -6
			count += 1
		if player.pokemon.statStage[8] > 3:
			player.pokemon.statStage[8] = 3
	else:
		count = 0
		for i in statStage:
			if i > 6:
				enemy.pokemon.statStage[count] = 6
			elif i < -6:
				enemy.pokemon.statStage[count] = -6
			count += 1
		if enemy.pokemon.statStage[8] > 3:
			enemy.pokemon.statStage[8] = 3

def moveStatWordingOnPlayer(statList):
	count = 0
	for i in statList:
		if i != 0:
			stat = statDict[count]
			changeForStat = statList[count]
			if changeForStat == 1:
				print(player.pokemon.name + '\'s', stat, 'raised!')
			if changeForStat == 2:
				print(player.pokemon.name + '\'s', stat, 'raised greatly!')
			if changeForStat >= 3:
				print(player.pokemon.name + '\'s', stat, 'raised hugely!')
			if changeForStat == -1:
				print(player.pokemon.name + '\'s', stat, 'fell!')
			if changeForStat == -2:
				print(player.pokemon.name + '\'s', stat, 'fell greatly!')
			if changeForStat <= -3:
				print(player.pokemon.name + '\'s', stat, 'fell hugely!')
		count += 1

def moveStatWordingOnEnemy(statList):
	count = 0
	for i in statList:
		if i != 0:
			stat = statDict[count]
			changeForStat = statList[count]
			if changeForStat == 1:
				print('The opposing', enemy.pokemon.name + '\'s', stat, 'raised!')
			if changeForStat == 2:
				print('The opposing', enemy.pokemon.name + '\'s', stat, 'raised greatly!')
			if changeForStat >= 3:
				print('The opposing', enemy.pokemon.name + '\'s', stat, 'raised hugely!')
			if changeForStat == -1:
				print('The opposing', enemy.pokemon.name + '\'s', stat, 'fell!')
			if changeForStat == -2:
				print('The opposing', enemy.pokemon.name + '\'s', stat, 'fell greatly!')
			if changeForStat <= -3:
				print('The opposing', enemy.pokemon.name + '\'s', stat, 'fell hugely!')
		count += 1

def moveNVEffectWording(nvStatus):
	if nvStatus == 1:
		return 'burned!'
	elif nvStatus == 2:
		return 'paralyzed!'
	elif nvStatus == 3:
		return 'put to sleep!'
	elif nvStatus == 4:
		return 'frozen!'
	else:
		return 'poisoned!'

def moveNVEffectPlayer():
	if player.pokemon.move.nvEffect != 0 and randint(1,100) <= player.pokemon.move.nvEffectChance:
		if enemy.pokemon.nvStatus == 0 and enemy.pokemon.substitute == 0:
			enemy.pokemon.nvStatus = player.pokemon.move.nvEffect
			if enemy.pokemon.nvStatus == 3:
				enemy.pokemon.nvStatusCount = randint(2,4)
			wording = moveNVEffectWording(enemy.pokemon.nvStatus)
			print('The opposing', enemy.pokemon.name, 'was', wording)
		else:
			print('But it failed!')

def moveNVEffectEnemy():
	if enemy.pokemon.move.nvEffect != 0 and randint(1,100) <= enemy.pokemon.move.nvEffectChance:
		if player.pokemon.nvStatus == 0 and player.pokemon.substitute == 0:
			player.pokemon.nvStatus = enemy.pokemon.move.nvEffect
			if player.pokemon.nvStatus == 3:
				player.pokemon.nvStatusCount = randint(1,3)
			wording = moveNVEffectWording(player.pokemon.nvStatus)
			print(player.pokemon.name, 'was', wording)
		else:
			print('But it failed!')

def getEnemyMove():
	totalPP = getTotalPP(enemy.pokemon)
	if totalPP == 0:
		return 'Struggle'
	check = 0
	totalChoices = len(enemy.pokemon.moveSet)
	while check == 0:
		choice = randint(1,totalChoices)
		if enemy.pokemon.disabled == 1 and enemy.pokemon.moveSet[choice - 1] == enemy.pokemon.disabledMove:
			check = 0
		elif enemy.pokemon.movePPCurrent[choice - 1] > 0:
			enemy.pokemon.movePPCurrent[choice - 1] -= 1
			check = 1
			return enemy.pokemon.moveSet[choice - 1]

def getEnemySwitchPokemon():
	oldPokemon = enemy.pokemon
	while True:
		choice = random.choice(enemy.team)
		if choice != oldPokemon and choice.hp != 0:
			resetOnSwitch(oldPokemon)
			enemy.pokemon = choice
			break

def getEnemySwitchPokemonForce():
	oldPokemon = enemy.pokemon
	while True:
		choice = random.choice(enemy.team)
		if choice != oldPokemon and choice.hp != 0:
			resetOnSwitch(oldPokemon)
			enemy.pokemon = choice
			print('The opposing', oldPokemon.name, 'was forced out!', 'The', enemy.type, enemy.name, 'switched into', choice.name + '!')
			break

def getPlayerSwitchPokemonForce():
	oldPokemon = player.pokemon
	while True:
		choice = random.choice(player.team)
		if choice != oldPokemon and choice.hp != 0:
			resetOnSwitch(oldPokemon)
			player.pokemon = choice
			print(oldPokemon.name, 'was forced out and replaced with', choice.name + '!')
			break

def getSwitchPokemon():
	count = 1
	print('Which Pokemon would you like to switch to?')
	for i in player.team:
		print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
		count += 1
	print('', count, '- View more information')
	count += 1
	print('', count, '- Back')
	while True:
		try:
			x = 0
			choiceInput = input('-- ')
			trapped = player.pokemon.bind + player.pokemon.clamp + player.pokemon.fireSpin + player.pokemon.wrap
			if int(choiceInput) == 1:
				if player.pokemon.hp == 0:
					print(player.pokemon.name, 'has fainted! Please choose another Pokemon!')
					x = 1
				else:
					print('That Pokemon is already out! Please choose another Pokemon!')
					x = 1
			elif int(choiceInput) == int(count):
				if player.pokemon.hp == 0:
					print(player.pokemon.name, 'has fainted! Please choose another Pokemon!')
					x = 1
				else:
					print('Keep going,', player.pokemon.name + '!')
					return 0

					# No switch
			elif int(choiceInput) == int(count) - 1:
				getPokemonInfoViewChoiceTeam()
				print('')
				print('Which Pokemon would you like to switch to?')
				count = 1
				for i in player.team:
					print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
					count += 1
				print('', count, '- View more information')
				count += 1
				print('', count, '- Back')
				x = 1
			elif player.pokemon.hp != 0 and trapped != 0:
				print(player.pokemon.name, 'is unable to escape due to being trapped!')
			else:
				for j in range(len(player.team)):
					if choiceInput == player.team[j].name or int(choiceInput) == int(j+1):
						if player.team[j].hp == 0:
							print(player.team[j].name, 'has fainted! Please choose another Pokemon!')
							x = 1
						else:
							oldPokemon = player.pokemon
							player.team[j], player.team[0] = player.team[0], player.team[j]
							player.pokemon = player.team[0]
							resetOnSwitch(oldPokemon)
							print('You switched from', oldPokemon.name, 'into', player.pokemon.name + '!')
							print()
							player.pokemon.inCurrentBattle = 1
							return 1
			if x == 0:
				print("Please choose a Pokemon from the list above!")
		except ValueError:
			print("Please choose a Pokemon from the list above!")	


def checkSplash(move):
	if move == 'Splash':
		print('But nothing happened!')

def checkTrapStart(atkPokemon, defPokemon):
	move = atkPokemon.move.move
	traplist = ['Bind','Clamp','Fire Spin','Wrap','Leech Seed']
	if move in traplist:
		if move == traplist[0]:
			if defPokemon.bind == 0 and defPokemon.substitute == 0:
				defPokemon.bind = 1
				defPokemon.bindCount = randint(4,5)
				if atkPokemon == player.pokemon:
					print('The opposing', enemy.pokemon.name, 'is caught in a bind!')
				else:
					print(player.pokemon.name, 'is caught in a bind!')
				print()
			else:
				print('But it failed!\n')
		elif move == traplist[1]:
			if defPokemon.clamp == 0 and defPokemon.substitute == 0:
				defPokemon.clamp = 1
				defPokemon.clampCount = randint(4,5)
				if atkPokemon == player.pokemon:
					print('The opposing', enemy.pokemon.name, 'is clamped down!')
				else:
					print(player.pokemon.name, 'is clamped down!')
				print()
			else:
				print('But it failed!\n')
		elif move == traplist[2]:
			if defPokemon.fireSpin == 0 and defPokemon.substitute == 0:
				defPokemon.fireSpin = 1
				defPokemon.fireSpinCount = randint(4,5)
				if atkPokemon == player.pokemon:
					print('The opposing', enemy.pokemon.name, 'is caught in a firey vortex!')
				else:
					print(player.pokemon.name, 'is caught in a firey vortex!')
				print()
			else:
				print('But it failed!\n')
		elif move == traplist[3]:
			if defPokemon.wrap == 0 and defPokemon.substitute == 0:
				defPokemon.wrap = 1
				defPokemon.wrapCount = randint(4,5)
				if atkPokemon == player.pokemon:
					print('The opposing', enemy.pokemon.name, 'is wrapped up!')
				else:
					print(player.pokemon.name, 'is caught in a bind!')
				print()
			else:
				print('But it failed!\n')
		elif move == traplist[4]:
			if defPokemon.leechSeed == 0 and defPokemon.substitute == 0:
				defPokemon.leechSeed = 1
				if atkPokemon == player.pokemon:
					print(player.pokemon.name, 'planted it\'s seed on the opposing', enemy.pokemon.name + '!')
				else:
					print('The opposing', enemy.pokemon.name, 'planted it\'s seed on', player.pokemon.name + '!')
			else:
				print('But it failed!\n')

def checkTrapEffect(pokemon):
	if pokemon.bind == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == player.pokemon:
			print(player.pokemon.name, 'took', damage, 'HP damage due to it\'s bind! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s bind! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!' )			
		if pokemon.hp > 0:
			pokemon.bindCount -= 1
			if pokemon.bindCount == 0:
				pokemon.bind = 0
				if pokemon == player.pokemon:
					print(player.pokemon.name, 'escaped from it\'s bind!')
				else:
					print('The opposing', enemy.pokemon.name, 'escaped from it\'s bind!' )
	if pokemon.clamp == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == player.pokemon:
			print(player.pokemon.name, 'took', damage, 'HP damage due to it\'s clamp! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s clamp! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!' )			
		if pokemon.hp > 0:
			pokemon.clampCount -= 1
			if pokemon.clampCount == 0:
				pokemon.clamp = 0
				if pokemon == player.pokemon:
					print(player.pokemon.name, 'escaped from it\'s clamp!')
				else:
					print('The opposing', enemy.pokemon.name, 'escaped from it\'s clamp!' )
	if pokemon.fireSpin == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == player.pokemon:
			print(player.pokemon.name, 'took', damage, 'HP damage due to the firey vortex! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage due to the firey vortex! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!' )			
		if pokemon.hp > 0:
			pokemon.fireSpinCount -= 1
			if pokemon.fireSpinCount == 0:
				pokemon.fireSpin = 0
				if pokemon == player.pokemon:
					print(player.pokemon.name, 'escaped from the firey vortex!')
				else:
					print('The opposing', enemy.pokemon.name, 'escaped from the firey vortex!' )
	if pokemon.wrap == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == player.pokemon:
			print(player.pokemon.name, 'took', damage, 'HP damage due to it\'s wrap! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s wrap! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!' )			
		if pokemon.hp > 0:
			pokemon.wrapCount -= 1
			if pokemon.wrapCount == 0:
				pokemon.wrap = 0
				if pokemon == player.pokemon:
					print(player.pokemon.name, 'escaped from it\'s wrap!')
				else:
					print('The opposing', enemy.pokemon.name, 'escaped from it\'s wrap!' )
	if pokemon.leechSeed == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == player.pokemon:
			print(player.pokemon.name, 'took', damage, 'HP damage due to it\'s leeching! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s leeching! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!' )			

	
def checkMetronome(pokemon):
	if pokemon.move.move == 'Metronome':
		randomMove = (random.choice(allMoveList))
		player.pokemon.move = Move(randomMove)
		if pokemon == player.pokemon:
			print(player.pokemon.name, 'used', randomMove + '!')
		else:
			print('The opposing', enemy.pokemon.name, 'used', randomMove + '!')

def checkConversion(pokemon):
	if pokemon.move.move == 'Conversion':
		if pokemon == player.pokemon:
			player.pokemon.type = enemy.pokemon.type
			print(player.pokemon.name, 'copied the type of the opposing', enemy.pokemon.name + '!')
		else:
			enemy.pokemon.type = player.pokemon.type
			print('The opposing', enemy.pokemon.name, 'copied the type of', player.pokemon.name + '!')

def checkCounter(atkPokemon, defPokemon):
	if atkPokemon.move.move == 'Counter':
		if defPokemon.move.variety == 'Physical' and defPokemon.previousDamage > 0:
			damage = defPokemon.previousDamage * 2
			if defPokemon.hp < damage:
				damage = defPokemon.hp
			defPokemon.hp -= damage
			if atkPokemon == player.pokemon:
				print('It did', damage, 'damage! The opposing', enemy.pokemon.name, 'has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!')
			else:
				print('It did', damage, 'damage!', player.pokemon.name, 'has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!')
			checkRageBonus(defPokemon)
		else:
			print('But it failed!')		

def checkRecoil(atkPokemon):
	recoilList = ['Struggle','Double-Edge','Submission','Take Down']
	if atkPokemon.move.move in recoilList:
		recoilOneOver = 4
		if atkPokemon.move.move == 'Struggle':
			recoilOneOver = 2
		damage = int(atkPokemon.previousDamage / 4)
		if damage > atkPokemon.hp:
			damage = atkPokemon.hp
		atkPokemon.hp -= damage
		if atkPokemon == player.pokemon:
			print('It took', damage, 'HP recoil damage!', player.pokemon.name, 'has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!')
		else:
			print('It took', damage, 'HP recoil damage! The opposing', enemy.pokemon.name, 'has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!' )

def checkSetDamage(atkPokemon, defPokemon):
	setDamageList = ['Dragon Rage','Night Shade','Psywave','Seismic Toss','Sonic Boom','Super Fang']
	move = atkPokemon.move.move
	if move in setDamageList:
		if move == 'Dragon Rage':
			damage = 40
		elif move == 'Night Shade':
			damage = atkPokemon.level
		elif move == 'Psywave':
			r = randint(5,15) / 10
			damage = int(atkPokemon.level * r)
		elif move == 'Seismic Toss':
			damage = defPokemon.level
		elif move == 'Sonic Boom':
			damage = 20
		elif move == 'Super Fang':
			damage = int(defPokemon.hp / 2)
		if defPokemon.hp < damage:
			damage = defPokemon.hp
		defPokemon.hp -= damage
		if atkPokemon == player.pokemon:
			print('It did', damage, 'damage! The opposing', enemy.pokemon.name, 'has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!')
		else:
			print('It did', damage, 'damage!', player.pokemon.name, 'has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!')
		checkRageBonus(defPokemon)

def checkRest(pokemon):
	if pokemon.move.move == 'Rest':
		pokemon.nvStatus = 3
		pokemon.nvStatusCount = 3
		healAmount = pokemon.maxhp - pokemon.hp
		pokemon.hp = pokemon.maxhp
		if pokemon == player.pokemon:
			print(player.pokemon.name, 'went to sleep to regain health, gaining', healAmount, 'HP. It has', (player.pokemon.hp), '/', (player.pokemon.maxhp), 'HP remaining!')
		else:
			print('The opposing', enemy.pokemon.name, 'went to sleep to regain health, gaining', healAmount, 'HP. It has', (enemy.pokemon.hp), '/', (enemy.pokemon.maxhp), 'HP remaining!')

def checkRegainHealth(pokemon):
	regainHealthList = ['Recover','Soft-Boiled']
	move = pokemon.move.move
	if move in regainHealthList:
		if pokemon.hp == pokemon.maxhp:
			print('But it failed!')
			return
		healAmount = int(pokemon.maxhp / 2)
		if healAmount > pokemon.maxhp - pokemon.hp:
			healAmount = pokemon.maxhp - pokemon.hp
		pokemon.hp += healAmount
		if pokemon == player.pokemon:
			print(player.pokemon.name, 'regained', healAmount, 'HP. It has', (player.pokemon.hp), '/', (player.pokemon.maxhp), 'HP remaining!')
		else:
			print('The opposing', enemy.pokemon.name, 'regained', healAmount, 'HP. It has', (enemy.pokemon.hp), '/', (enemy.pokemon.maxhp), 'HP remaining!')

def checkHaze(atkPokemon, defPokemon):
	if atkPokemon.move.move  == 'Haze':
		print('All stat changes have been reset!')
		atkPokemon.statStage = [0,0,0,0,0,0,0,0,0]
		defPokemon.statStage = [0,0,0,0,0,0,0,0,0]

def checkForceSwitch(atkPokemon):
	forceSwitchMoves = ['Roar','Whirlwind']
	if atkPokemon.move.move in forceSwitchMoves:
		if atkPokemon == player.pokemon:
			if enemy.type != 'Wild':
				if enemy.livingPokemon > 1:
					getEnemySwitchPokemonForce()
				else:
					print('But it failed!')
			else:
				print(player.pokemon.name, 'blew the opposing', enemy.pokemon.name, 'away! The battle is over!')
				environment.battleEnd = 1
		else:
			if enemy.type != 'Wild':
				if player.livingPokemon > 1:
					getPlayerSwitchPokemonForce()
				else:
					print('But it failed!')
			else:
				print('The opposing', enemy.pokemon.name, 'blew', enemy.pokemon.name, 'away! The battle is over!')
				environment.battleEnd = 1

def checkCopyMove(atkPokemon,defPokemon):
	copyMoveList = ['Mimic','Mirror Move']
	if atkPokemon.move.move in copyMoveList:
		if defPokemon.previousMove != 0:
			atkPokemon.move = defPokemon.previousMove
			if atkPokemon == player.pokemon:
				print(player.pokemon.name, 'copied', atkPokemon.move.move + '!')
			else:
				print('The opposing', enemy.pokemon.name, 'copied', atkPokemon.move.move + '!')	
		else:
			print('But it failed!')	

def checkDreamEater(atkPokemon,defPokemon):
	if atkPokemon.move.move == 'Dream Eater':
		if defPokemon.nvStatus == 3:
			return 0
		else:
			print('But it failed!')
			return 1
	return 0

def checkDefensiveWall(person):
	wallList = ['Light Screen','Reflect','Mist']
	move = person.pokemon.move.move
	if move in wallList:
		if move == 'Light Screen':
			if person.lightScreen == 0:
				person.lightScreen = 1
				person.lightScreenCount = 6
				if person == player:
					print('Light Screen raised your team\'s Sp. Def!')
				else:
					print('Light Screen raised the opposing team\'s Sp. Def!')
			else:
				print('But it failed!')
		if move == 'Reflect':
			if person.reflect == 0:
				person.reflect = 1
				person.reflectCount = 6
				if person == player:
					print('Reflect raised your team\'s Def!')
				else:
					print('Reflect raised the opposing team\'s Def!')
			else:
				print('But it failed!')
		if move == 'Mist':
			if person.mist == 0:
				person.mist = 1
				person.mistCount = 6
				if person == player:
					print('Your team has been protected from stat changes!')
				else:
					print('Your opponent\'s team has been protected from stat changes')
			else:
				print('But it failed!')


def checkAttackSecondTurnMoves(pokemon):
	secondTurnMoves = ['Dig', 'Fly', 'Razor Wind', 'Skull Bash', 'Sky Attack']
	if pokemon.move.move in secondTurnMoves:
		if pokemon.lockedInMoveNumber == 0:
			pokemon.lockedInMoveNumber = 1
			if pokemon.move.move == 'Dig':
				wording = 'dug underground!'
				pokemon.immune = 1
			elif pokemon.move.move == 'Fly':
				wording = 'flew high up!'
				pokemon.immune = 1
			elif pokemon.move.move == 'Razor Wind':
				wording = 'began charging up!'
			elif pokemon.move.move == 'Skull Bash':
				wording = 'began charging up! It\'s defense rose!'
				pokemon.statStage = list(map(add, pokemon.statStage, [0,0,1,0,0,0,0,0,0]))
				statStageMax(pokemon)		
			elif pokemon.move.move == 'Sky Attack':
				wording = 'began charging up!'
			if pokemon == player.pokemon:
				print(player.pokemon.name, wording)
			else:
				print('The opposing', enemy.pokemon.name, wording)	
			return 1		
		else:
			pokemon.lockedInMoveNumber -= 1
			if pokemon.lockedInMoveNumber == 0:
				pokemon.immune = 0
				return 0
	else:
		return 0

def checkAttackFirstTurnMoves(pokemon):
	firstTurnMoves = ['Hyper Beam', 'Solar Beam']
	if pokemon.move.move in firstTurnMoves:
		if pokemon.lockedInMoveNumber == 0:
			pokemon.lockedInMoveNumber = 1
			return 0	
		else:
			pokemon.lockedInMoveNumber -= 1
			if pokemon.lockedInMoveNumber == 0:
				if pokemon == player.pokemon:
					print(player.pokemon.name, 'has to recharge!')
				else:
					print('The opposing', enemy.pokemon.name, 'has to recharge')
				return 1
	else:
		return 0

def checkBide(pokemon, defPokemon):
	if pokemon.move.move == 'Bide':
		if pokemon.lockedInMoveNumber == 0:
			pokemon.bide = 1
			pokemon.lockedInMoveNumber = 2
			if pokemon == player.pokemon:
				print(player.pokemon.name, 'began storing energy!')
			else:
				print('The opposing', enemy.pokemon.name, 'began storing energy!')	
			return 0	
		else:
			pokemon.lockedInMoveNumber -= 1
			if pokemon.lockedInMoveNumber == 0:
				damage = 2 * pokemon.bideDamage
				if defPokemon.hp < damage:
					damage = defPokemon.hp
				defPokemon.hp -= damage
				if pokemon == player.pokemon:
					print(player.pokemon.name, 'released it\'s energy! It did', damage, 'against the opposing', enemy.pokemon.name + '! It has', str(enemy.pokemon.hp) + '/' + str(enemy.pokemon.maxhp), 'remaining!')
				else:
					print('The opposing', enemy.pokemon.name, 'released it\'s energy! It did', damage, 'against', player.pokemon.name + '! It has', str(player.pokemon.hp) + '/' + str(player.pokemon.maxhp), 'remaining!')				
				checkRageBonus(defPokemon)
				pokemon.bideDamage = 0
				pokemon.bide = 0
			else:
				if pokemon == player.pokemon:
					print(player.pokemon.name, 'is still storing energy!')
				else:
					print('The opposing', enemy.pokemon.name, 'is still storing energy!')					
	else:
		return 0

def checkThrashOrPetal(pokemon):
	moveList = ['Thrash', 'Petal Dance']
	if pokemon.move.move in moveList:
		if pokemon.lockedInMoveNumber == 0:
			pokemon.lockedInMoveNumber = randint(1,2)
			return 0
		else:
			pokemon.lockedInMoveNumber -= 1
			if pokemon.lockedInMoveNumber == 0:
				pokemon.confused = 1
				pokemon.confusedCount = randint(3,5)
				if pokemon == player.pokemon:
					print(player.pokemon.name, 'has become confused!')
				else:
					print('The opposing', enemy.pokemon.name, 'has become confused!')					
				return 0
			else:
				return 0		
	else:
		return 0

def checkPayDay(pokemon):
	if pokemon.move.move == 'Pay Day':
		multiplier = randint(2,5)
		environment.payDayExtra += multiplier * pokemon.level

def checkAddBideDamage(pokemon, damage):
	if pokemon.bide == 1:
		pokemon.bideDamage += damage

def checkRage(pokemon):
	if pokemon.move.move == 'Rage':
		pokemon.rage = 1
	else:
		if pokemon.rageCount != 0:
			pokemon.statStage = list(map(add, pokemon.statStage, [0,-pokemon.rageCount,0,0,0,0,0,0,0]))
			statStageMax(pokemon)
			pokemon.rageCount = 0
		pokemon.rage = 0

def checkRageBonus(pokemon):
	if pokemon.rage == 1:
		pokemon.statStage = list(map(add, pokemon.statStage, [0,1,0,0,0,0,0,0,0]))
		statStageMax(pokemon)
		pokemon.rageCount += 1

def checkTeleport(player, enemy):
	if player.pokemon.move.move == 'Teleport':
		if enemy.type == 'Wild':
			return 1
	if enemy.pokemon.move.move == 'Teleport':
		return 1

def checkStartSubstitute(pokemon):
	if pokemon.move.move == 'Substitute':
		if pokemon.substitute == 1:
			print('But it failed!')
		elif pokemon.hp > int(pokemon.maxhp / 4) + 1:
			pokemon.substitute = 1
			pokemon.substituteHealth = int(pokemon.maxhp / 4)
			pokemon.hp -= pokemon.substituteHealth
			print(pokemon.substitute, 'yy')
			if pokemon == player.pokemon:
				print(player.pokemon.name, 'has placed a substitute and lost', pokemon.substituteHealth, 'HP! It has', player.pokemon.hp, '/', player.pokemon.maxhp, 'HP remaining!')
			else:
				print('The opposing', enemy.pokemon.name, 'has placed a substitute and lost', pokemon.substituteHealth, 'HP! It has', enemy.pokemon.hp, '/', enemy.pokemon.maxhp, 'HP remaining!')	
		else:
			print('But it failed!')

def checkDisable(atkPokemon, defPokemon):
	if atkPokemon.move.move == 'Disable':
		if defPokemon.previousMove != 0 and defPokemon.disabled != 1:
			defPokemon.disabled = 1
			defPokemon.disabledCount = randint(3,6)
			defPokemon.disabledMove = defPokemon.previousMove.move
			if atkPokemon == player.pokemon:
				print('The opposing', enemy.pokemon.name, 'can no longer use', enemy.pokemon.disabledMove + '!')
			else:
				print(player.pokemon.name, 'can no longer use', player.pokemon.disabledMove + '!')	

		else:
			print('But it failed!')

def checkTransform(atkPokemon, defPokemon):
	if atkPokemon.move.move == 'Transform':
		atkPokemon.moveSet = defPokemon.moveSet
		atkPokemon.movePPCurrent = defPokemon.movePPMax
		if atkPokemon == enemy.pokemon:
			print('The opposing', enemy.pokemon.name, 'transformed into', player.pokemon.name + '!')
		else:
			print(player.pokemon.name, 'transformed into', enemy.pokemon.name + '!')	

def startPlayerTurn():
	interrupt = 0
	interrupt = checkAttackFirstTurnMoves(player.pokemon)
	if player.pokemon.flinch == 1:
		interrupt += 1
		print(player.pokemon.name, 'flinched!')
	if player.pokemon.nvStatus != 0:
		interrupt += preTurnNVStatusCheck(player)
	if interrupt == 0:
		if interrupt == 0:
			if player.pokemon.confused == 1:
				print(player.pokemon.name, 'is confused!')
				hitOrConfused = getHitOrConfused(player.pokemon)
				if hitOrConfused > 0:
					if hitOrConfused == 1:
						damage = moveDamageConfusion(player.pokemon)
						player.pokemon.hp -= damage
						print(player.pokemon.name, 'hit itself in confusion and did', damage, 'HP damage. It has', str(player.pokemon.hp) + '/' + str(player.pokemon.maxhp), 'remaining!')
						interrupt = 1
					else:
						print(player.pokemon.name, 'snapped out of confusion!')
			if interrupt == 0:
				interrupt = checkAttackSecondTurnMoves(player.pokemon)
				if interrupt == 0:				
					hitOrMiss = getHitOrMiss(player.pokemon,enemy.pokemon,player.pokemon.move)
					if hitOrMiss == 'Miss':
						print(player.pokemon.name, 'tried to use', player.pokemon.move.move + ', but it missed!')
						checkMissDamage(player.pokemon)
						interrupt = 1
					if interrupt == 0:
						print(player.pokemon.name, 'used', player.pokemon.move.move, 'against the opposing', enemy.pokemon.name + '.')
						interrupt = checkFainted(enemy.pokemon)
						interrupt += checkDreamEater(player.pokemon, enemy.pokemon)
						if interrupt == 0:
							checkCopyMove(player.pokemon, enemy.pokemon)
							checkMetronome(player.pokemon)
							checkConversion(player.pokemon)
							checkCounter(player.pokemon, enemy.pokemon)
							checkFlinch(player.pokemon.move, enemy.pokemon)
							checkSplash(player.pokemon.move.move)
							checkSetDamage(player.pokemon, enemy.pokemon)
							checkRest(player.pokemon)
							checkRegainHealth(player.pokemon)
							checkHaze(player.pokemon, enemy.pokemon)
							checkForceSwitch(player.pokemon)
							checkDefensiveWall(player)
							checkBide(player.pokemon, enemy.pokemon)
							checkRage(player.pokemon)
							checkPayDay(player.pokemon)
							checkStartSubstitute(player.pokemon)
							checkDisable(player.pokemon, enemy.pokemon)
							checkTransform(player.pokemon, enemy.pokemon)
							if player.pokemon.move.damage != 0:
								moveDealDamagePlayer()
								checkRecoil(player.pokemon)
							checkThrashOrPetal(player.pokemon)
							if enemy.pokemon.hp == 0:
								print('The opposing', enemy.pokemon.name, 'fainted!')
							checkTrapStart(player.pokemon, enemy.pokemon)
							checkKamikaze(player.pokemon.move, player.pokemon)
							if enemy.pokemon.hp != 0:
								if player.pokemon.move.statEffect != 0:
									moveStatChangePlayer()
								if player.pokemon.move.nvEffect != 0:
									moveNVEffectPlayer()
								if player.pokemon.move.vEffect != 0:
									confuse = checkConfusion(player.pokemon.move, enemy.pokemon)
									if confuse == 1:
										print('The opposing', enemy.pokemon.name, 'is confused!')
	player.pokemon.previousMove = player.pokemon.move
#	if player.pokemon.lockedInMoveNumber > 0:
#		player.pokemon.lockedInMoveNumber -= 1
	print()	

def startEnemyTurn():
	interrupt = 0
	interrupt = checkAttackFirstTurnMoves(enemy.pokemon)
	if enemy.pokemon.flinch == 1:
		interrupt += 1
		print('The opposing', enemy.pokemon.name, 'flinched!')	
	if enemy.pokemon.nvStatus != 0:
		interrupt += preTurnNVStatusCheck(enemy)
	if interrupt == 0:
		if interrupt == 0:
			if enemy.pokemon.confused == 1:
				print(enemy.pokemon.name, 'is confused!')				
				hitOrConfused = getHitOrConfused(enemy.pokemon)		
				if hitOrConfused > 0:
					if hitOrConfused == 1:
						damage = moveDamageConfusion(enemy.pokemon)
						enemy.pokemon.hp -= damage
						print('The opposing', enemy.pokemon.name, 'hit itself in confusion and did', damage, 'HP damage. It has', str(enemy.pokemon.hp) + '/' + str(enemy.pokemon.maxhp), 'remaining!')
						interrupt = 1
					else:
						print('The opposing', enemy.pokemon.name, 'snapped out of confusion!')
			if interrupt == 0:
				interrupt = checkAttackSecondTurnMoves(enemy.pokemon)
				if interrupt == 0:
					hitOrMiss = getHitOrMiss(enemy.pokemon,player.pokemon,enemy.pokemon.move)
					if hitOrMiss == 'Miss':
						print('The opposing', enemy.pokemon.name, 'tried to use', enemy.pokemon.move.move + ', but it missed!')
						checkMissDamage(enemy.pokemon)
						interrupt = 1
					if interrupt == 0:
						print('The opposing', enemy.pokemon.name, 'used', enemy.pokemon.move.move, 'against', player.pokemon.name + '.')
						interrupt = checkFainted(player.pokemon)
						interrupt += checkDreamEater(enemy.pokemon, player.pokemon)
						if interrupt == 0:
							checkCopyMove(enemy.pokemon, player.pokemon)
							checkMetronome(enemy.pokemon)
							checkConversion(enemy.pokemon)
							checkCounter(enemy.pokemon, player.pokemon)
							checkSplash(enemy.pokemon.move.move)
							checkFlinch(enemy.pokemon.move, player.pokemon)
							checkSetDamage(enemy.pokemon, player.pokemon)
							checkRest(enemy.pokemon)
							checkRegainHealth(enemy.pokemon)
							checkHaze(enemy.pokemon, player.pokemon)
							checkForceSwitch(enemy.pokemon)
							checkDefensiveWall(enemy)
							checkBide(enemy.pokemon, player.pokemon)
							checkRage(enemy.pokemon)
							checkPayDay(enemy.pokemon)
							checkStartSubstitute(enemy.pokemon)
							checkDisable(enemy.pokemon, player.pokemon)
							checkTransform(enemy.pokemon, player.pokemon)

							if enemy.pokemon.move.damage != 0:
								moveDealDamageEnemy()
								checkRecoil(enemy.pokemon)
							checkThrashOrPetal(enemy.pokemon)
							if player.pokemon.hp == 0:
								print(player.pokemon.name, 'fainted!')					
							checkTrapStart(enemy.pokemon, player.pokemon)
							checkKamikaze(enemy.pokemon.move, enemy.pokemon)
							if player.pokemon.hp != 0:
								if enemy.pokemon.move.statEffect != 0:
									moveStatChangeEnemy()
								if enemy.pokemon.move.nvEffect != 0:
									moveNVEffectEnemy()
								if enemy.pokemon.move.vEffect != 0:
									confuse = checkConfusion(enemy.pokemon.move, player.pokemon)
									if confuse == 1:
										print(player.pokemon.name, 'is confused!')
	enemy.pokemon.previousMove = enemy.pokemon.move
#	if enemy.pokemon.lockedInMoveNumber > 0:
#		enemy.pokemon.lockedInMoveNumber -= 1
	print()

def checkMissDamage(pokemon):
	if pokemon.move.move == 'High Jump Kick' or pokemon.move.move == 'Jump Kick':
		damage = int(pokemon.maxhp / 2)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon.hp == 0:
			if pokemon == player.pokemon:
				print(player.pokemon.name, 'kept going and took', damage, 'HP damage and fainted!')
			else:
				print('The opposing', enemy.pokemon.name, 'kept going and took', damage, 'HP damage and fainted!')
		else:
			if pokemon == player.pokemon:
				print(player.pokemon.name, 'kept going and took', damage, 'HP damage! It has', str(player.pokemon.hp) + '/' + str(player.pokemon.maxhp), 'remaining!')
			else:
				print('The opposing', enemy.pokemon.name, 'kept going and took', damage, 'HP damage! It has', str(enemy.pokemon.hp) + '/' + str(enemy.pokemon.maxhp), 'remaining!')

def teamTotalHP(person):
	totalHP = 0
	for i in person.team:
		totalHP += i.hp
	return totalHP

def getRun():
	if enemy.type == 'Wild':
		chance = randint(1,2)
		if chance == 1:
			print('You got away!')
			return 1
		else:
			print('You couldn\'t get away!')
			return 0


def checkWallCounts():
	if player.lightScreen == 1:
		player.lightScreenCount -= 1
		if player.lightScreenCount == 0:
			player.lightScreen = 0
			print('Your team\'s light screen wore off!')
	if player.reflect == 1:
		player.reflectCount -= 1
		if player.reflectCount == 0:
			player.reflect = 0
			print('Your team\'s reflect wore off!')
	if player.mist == 1:
		player.mistCount -= 1
		if player.mistCount == 0:
			player.mist = 0
			print('Your team\'s mist wore off!')
	if enemy.lightScreen == 1:
		enemy.lightScreenCount -= 1
		if enemy.lightScreenCount == 0:
			enemy.lightScreen = 0
			print('The opposing team\'s light screen wore off!')
	if enemy.reflect == 1:
		enemy.reflectCount -= 1
		if enemy.reflectCount == 0:
			enemy.reflect = 0
			print('The opposing team\'s reflect wore off!')
	if enemy.mist == 1:
		enemy.mistCount -= 1
		if enemy.mistCount == 0:
			enemy.mist = 0
			print('The opposing team\'s mist wore off!')

def checkDisableCounts():
	if player.pokemon.disabledCount == 1:
		player.pokemon.disabledCount -= 1
		if player.pokemon.disabledCount == 0:
			player.pokemon.disabled = 0
			print(player.pokemon.name, 'is now able to use', player.pokemon.disabledMove, 'again!')
			player.pokemon.disabledMove = 0
	if enemy.pokemon.disabled == 1:
		enemy.pokemon.disabledCount -= 1
		if enemy.pokemon.disabledCount == 0:
			enemy.pokemon.disabled = 0
			print(enemy.pokemon.name, 'is now able to use', enemy.pokemon.disabledMove, 'again!')
			enemy.pokemon.disabledMove = 0

def resetOnSwitch(pokemon):
	pokemon.statStage = [0,0,0,0,0,0,0,0,0]
	pokemon.move = Move('None')
	pokemon.previousMove = 0
	pokemon.criticalMove = 0
	pokemon.lockedInMoveNumber = 0
	pokemon.immune = 0
	pokemon.flinch = 0
	pokemon.confused = 0
	pokemon.confusedCount = 0
	pokemon.type = getPokemonType(pokemon)
	pokemon.leechSeed = 0

def endRound():
	for pokemon in player.team:
		pokemon.flinch = 0
	for pokemon in enemy.team:
		pokemon.flinch = 0
	checkWallCounts()
	checkDisableCounts()

def endBattlePokemonInfo():
	for pokemon in player.team:
		pokemon.statStage = [0,0,0,0,0,0,0,0,0]
#		pokemon.ability =  
		pokemon.type = getPokemonType(pokemon)
		pokemon.move = Move('None')
		pokemon.previousMove = 0
		pokemon.inCurrentBattle = 0
		pokemon.shouldEvolve = 0
		pokemon.criticalMove = 0
		pokemon.lockedInMoveNumber = 0
		pokemon.immune = 0
		pokemon.flinch = 0
		pokemon.confused = 0
		pokemon.confusedCount = 0
		pokemon.bind = 0
		pokemon.bindCount = 0
		pokemon.clamp = 0
		pokemon.clampCount = 0
		pokemon.fireSpin = 0
		pokemon.fireSpinCount = 0
		pokemon.wrap = 0
		pokemon.wrapCount = 0
		pokemon.leechSeed = 0
	for pokemon in enemy.team:
		pokemon.statStage = [0,0,0,0,0,0,0,0,0]
#		pokemon.ability =  
		pokemon.type = getPokemonType(pokemon)
		pokemon.move = Move('None')
		pokemon.previousMove = 0
		pokemon.inCurrentBattle = 0
		pokemon.shouldEvolve = 0
		pokemon.criticalMove = 0
		pokemon.lockedInMoveNumber = 0
		pokemon.immune = 0
		pokemon.flinch = 0
		pokemon.confused = 0
		pokemon.confusedCount = 0
		pokemon.bind = 0
		pokemon.bindCount = 0
		pokemon.clamp = 0
		pokemon.clampCount = 0
		pokemon.fireSpin = 0
		pokemon.fireSpinCount = 0
		pokemon.wrap = 0
		pokemon.wrapCount = 0
		pokemon.leechSeed = 0

def checkFlinch(atkMove, defPokemon):
	if atkMove.flinch == 1:
		if randint(1,100) <= atkMove.flinchChance:
			defPokemon.flinch = 1

def checkKamikaze(atkMove, atkPokemon):
	if atkMove.move == 'Self-Destruct' or atkMove.move == 'Explosion':
		damage = atkPokemon.hp
		atkPokemon.hp -= atkPokemon.hp
		if atkPokemon == player.pokemon:
			print(player.pokemon.name, 'took', damage, 'HP damage and fainted!')
		else:
			print('The opposing', enemy.pokemon.name, 'took', damage, 'HP damage and fainted!')

def checkFainted(defPokemon):
	fainted = 0
	if defPokemon.hp == 0:
		print('But it failed!')
		fainted = 1
	return fainted

def checkConfusion(atkMove, defPokemon):
	confusion = 0
	if atkMove.vEffect == 1 and defPokemon.confused == 0 and defPokemon.substitute == 0:
		if randint(1,100) <= atkMove.vEffectChance:
			defPokemon.confused = 1
			defPokemon.confusedCount = randint(3,5)
			confusion = 1
	return confusion



def getCurrentFight():
		while player.pokemon.hp > 0 and enemy.pokemon.hp > 0 and environment.battleEnd == 0:
			player.pokemon.inCurrentBattle = 1
			interrupt = 0
			if player.pokemon.lockedInMoveNumber == 0:
				battleChoice = battleChoiceInput()
			if battleChoice == 'Fight':
				player.pokemon.inCurrentBattle = 1
				if player.pokemon.lockedInMoveNumber == 0:
					moveChoice = moveChoiceInput()
				if moveChoice == 'Back':
					interrupt = 1
				else:
					if enemy.pokemon.lockedInMoveNumber == 0:
						enemyChoice = getEnemyMove()
						enemy.pokemon.move = Move(enemyChoice)
					player.pokemon.move = Move(moveChoice); 
					turnOrder = getTurnOrder(player.pokemon,enemy.pokemon,player.pokemon.move,enemy.pokemon.move)
					if turnOrder == 'myPokemonFirst':
						startPlayerTurn()
						if enemy.pokemon.hp != 0 and environment.battleEnd == 0:
							startEnemyTurn()
					if turnOrder == 'enemyPokemonFirst':
						startEnemyTurn()
						if player.pokemon.hp != 0 and environment.battleEnd == 0:
							startPlayerTurn()
			elif battleChoice == 'Pokemon':
				switch = getSwitchPokemon()
				if switch == 1:
					startEnemyTurn()
				else:
					interrupt = 1
			elif battleChoice == 'Bag':
				choice = openBag()
				if choice == 1:
					interrupt = 1
				elif choice == 'Catch':
					return 'End'
				else:
					startEnemyTurn()
			elif battleChoice == 'Run':
				if enemy.type == 'Wild':
					run = getRun()
					print()
					if run == 0:
						startEnemyTurn()
					else:
						return 'End'
				else:
					print('You can\'t run away from this battle!')
					interrupt = 1
			teleport = checkTeleport(player, enemy)
			if teleport == 1:
				print('The battle ended!')
				return 'End'
			if interrupt == 0:
				if player.pokemon.hp != 0:
					postTurnNVStatusCheckPlayer()
				if player.pokemon.hp != 0:
					checkTrapEffect(player.pokemon)
				if player.pokemon.hp == 0:
					if teamTotalHP(player) > 0:
						player.livingPokemon -= 1
						player.pokemon.inCurrentBattle = 0
						switch = getSwitchPokemon()
						while switch == 0:
							switch = getSwitchPokemon()		
				if enemy.pokemon.hp != 0:
					postTurnNVStatusCheckEnemy()
				if enemy.pokemon.hp != 0:
					checkTrapEffect(enemy.pokemon)
				if enemy.pokemon.hp == 0:
					getExpYield()
					if teamTotalHP(enemy) > 0:
						enemy.livingPokemon -= 1
						getResetInBattle()
						getEnemySwitchPokemon()
						print('The', enemy.type, enemy.name, 'is about to send out a', enemy.pokemon.name + '.', 'Would you like to switch?')
						choice = getYesOrNo()
						if choice == 1:
							getSwitchPokemon()
			endRound()

def openBag():
	print('You opened your bag! What pocket would you like to go into?')
	x = 0
	while x == 0:
		choice = getPocketChoice()
		if choice == 'Balls':
			x = getBallPocket()
		elif choice == 'Medicine':
			x = getMedicinePocket()
		else:
			x = 1
			return 1
	return x

def getCatch(ball):
	ballModifier = ball.modifier
	if ballModifier == 'Master':
		print('You caught the opposing', enemy.pokemon.name + '!')
		getCaughtPokemon()
		return 'Catch'
	statusModifier = getStatusCatchModifiers()
	catchValue = int(((( 3 * enemy.pokemon.maxhp - 2 * enemy.pokemon.hp) * enemy.pokemon.catchRate * ballModifier) / ( 3 * enemy.pokemon.maxhp) ) * statusModifier)
	catch = 1048560 / math.sqrt(math.sqrt(16711680 / catchValue))
	count = 0
	for i in range(3):
		random = randint(1,65535)
		count = count + 1
		print('Shook', count, 'times!')
		time.sleep(1)
		if catch > random:		
			if count == 3:
				print('You caught the opposing', enemy.pokemon.name + '!')
				getCaughtPokemon()
				return 'Catch'
		else:
			if count == 1:
				print('Not even close!')
			if count == 2:
				print('Oh, nearly had it!')
			if count == 3:
				print('So so close!')
			print('')
			return 'No catch'

def getCaughtPokemon():
	if len(player.team) < 6:
		getNamePokemon(enemy.pokemon)
		player.team.append(enemy.pokemon)

		print('You added the', enemy.pokemon.name, 'to your team!\n')
	else:
		getNamePokemon(enemy.pokemon)
		PC.boxes[0].inventory.append(enemy.pokemon)

		print('You sent the', enemy.pokemon.name, 'to the PC!\n')

def getNamePokemon(pokemon):
	print('\nWould you like to name the', pokemon.name + '?')
	choice = getYesOrNo()
	if choice == 1:
		print('\nWhat would you like to name it?')
		choiceInput = input('-- ')
		pokemon.name = choiceInput

def getBallPocket():
	ball = getBallChoice()
	if ball == 0:
		return 0
	ball.quantity -= 1
	if ball.quantity == 0:
		bag.balls.remove(ball)
	print('You throw the', ball.name, 'at the opposing', enemy.pokemon.name + '!')
	if enemy.type != 'Wild':
		print('The', enemy.type, enemy.name, 'swatted the ball away! You can\'t use that here!')
		return 'No Catch'
	else:
		catch = getCatch(ball)
		if catch == 1:
			return 1
		else:
			return catch
	print()

def getMedicinePocket():
	medicine = getMedicineChoice()
	if medicine == 0:
		return 0
	choice = getPokemonHealChoice(medicine)
	if choice == 0:
		return 0
	medicine.quantity -= 1
	if medicine.quantity == 0:
		bag.medicine.remove(medicine)

#def getHealFunction(medicine):
#	if medicine in 

def getPokemonHealChoice(medicine):
	count = 1
	print('Which Pokemon would you like to use this on?')
	for i in player.team:
		print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
		count += 1
	print('', count, '- Back')
	while True:
		try:
			x = 0
			choiceInput = input('-- ')
			if int(choiceInput) == int(count):
				return 0
			for j in range(len(player.team)):
				if choiceInput == player.team[j].name or int(choiceInput) == int(j+1):
					if player.team[j].hp == 0:
						print(player.team[j].name, 'has fainted! This would have no effect! Choose another!')
						x = 1
					elif player.team[j].hp == player.team[j].maxhp:
						print(player.team[j].name, 'is at full health! This would have no effect! Choose another!')
						x = 1
					else:
						heal = medicine.heal
						if player.team[j].maxhp - player.team[j].hp < heal:
							heal = player.team[j].maxhp - player.team[j].hp
						player.team[j].hp += heal
						print(player.team[j].name, 'has been healed by', heal, 'HP! It has', str(player.pokemon.hp) + '/' + str(player.pokemon.maxhp), 'remaining!')
						return 1
			if x == 0:
				print("Please choose a Pokemon from the list above!")
		except ValueError:
			print("Please choose a Pokemon from the list above!")	


def getMedicineChoice():
	options = len(bag.medicine)
	if options == 0:
		print('You have no medicine remaining!')
		return 0
	for i in range(options):
		print('', i+1, '-', bag.medicine[i].name, '-', bag.medicine[i].quantity, 'remaining.')
		i += 1
	i += 1
	print('', i, '- Back')
	while True:
		try:
			choiceInput = input('-- ')
			if int(choiceInput) < i and int(choiceInput) > 0:
				medicine = bag.medicine[int(choiceInput) - 1]
				return medicine
			elif int(choiceInput) == i:
				return 0
			print("Please choose an item from the list above!")
		except ValueError:
			print("Please choose an item from the list above!")	

def getBallChoice():
	options = len(bag.balls)
	if options == 0:
		print('You have no balls remaining!')
		return 0
	for i in range(options):
		print('', i+1, '-', bag.balls[i].name, '-', bag.balls[i].quantity, 'remaining.')
		i += 1
	i += 1
	print('', i, '- Back')
	while True:
		try:
			choiceInput = input('-- ')
			if int(choiceInput) < i and int(choiceInput) > 0:
				ball = bag.balls[int(choiceInput) - 1]
				return ball
			elif int(choiceInput) == i:
				return 0
			print("Please choose a ball from the list above!")
		except ValueError:
			print("Please choose a ball from the list above!")

def getPocketChoice():
	print(' 1 - Balls')
	print(' 2 - Medicine')
	print(' 3 - Back')
	while True:
		try:
			choiceInput = input('-- ')
			if choiceInput == 'Balls' or int(choiceInput) == 1:
				return 'Balls'
			if choiceInput == 'Medicine' or int(choiceInput) == 2:
				return 'Medicine'
			if choiceInput == 'Back' or int(choiceInput) == 3:
				return 'Back'
			print("Please choose an option from the list above!")
		except ValueError:
			print("Please choose an option from the list.")

def getResetInBattle():
	for i in player.team:
		i.inCurrentBattle = 0

def getYesOrNo():
	print(' 1 - Yes\n 2 - No')
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')	

def battleTypeChoice():
	print('What would you like to do?')
	print(' 1 - Battle Trainer\n 2 - Battle Wild Pokemon\n 3 - Go To Pokemon Center')
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2 or choiceInput == 3:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def startBattle():
	player.team = player.defaultTeam
	player.pokemon = player.team[0]
	enemy.pokemon = enemy.team[0]
	battleStartPhrasing()
	while teamTotalHP(player) > 0 and teamTotalHP(enemy) > 0 and environment.battleEnd == 0:
		game = getCurrentFight()
		if game == 'End':
			return
	if teamTotalHP(player) == 0:
		print('You lost!')
	elif teamTotalHP(enemy) == 0:
		winBattle()
	elif environment.battleEnd == 1:
		environment.battleEnd = 0

def winBattle():
	if enemy.type != 'Wild':
		print(enemy.text)
		cash = randint(200,500)
		cash += environment.payDayExtra
		player.money += cash
		print('You earned $' + str(cash), 'for winning!\n')
	for i in player.team:
		if i.shouldEvolve == 1:
			print('Something is happening to', i.name + '! Let it continue?')
			if getYesOrNo() == 1:
				evolvePokemon(i)
	endBattlePokemonInfo()


def createEnemy(typex, name, team, prizeMoney, text):
	enemy.type = typex
	enemy.name = name
	enemy.team = team
	enemy.livingPokemon = len(team)
	enemy.prizeMoney = prizeMoney
	enemy.text = text
	enemy.pokemon = enemy.team[0]

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

def pokemonCenter():
	print('Hello, welcome to the Pokemon Center. What would you like to do here today?')
	leave = 0
	while leave == 0:
		choice = getPokemonCenterChoice()
		if choice == 1:
			healAllPokemon()
		elif choice == 2:
			usePC()
		elif choice == 3:
			print(player.money)
			print('The shop is currently closed, please come again later!\n')
		elif choice == 4:
			saveOrLoad()
		elif choice == 5:
			leave = 1
			print('Thank you for coming, we hope to see you again!\n')
			return
		print('Anything else we can do for you today?')

def saveOrLoad():
	option = getOptionOneOrTwo('Save', 'Load')
	if option == 1:
		saveGame()
	if option == 2:
		loadGame()


def healAllPokemon():
	print('Of course, please let me take your pokemon for a few moments!')
	for pokemon in player.team:
		pokemon.hp = pokemon.maxhp
		pokemon.nvStatus = 0
		pokemon.nvStatusCount = 0
		pokemon.movePPCurrent = pokemon.movePPMax
		print('Healed', pokemon.name + '!')
		time.sleep(1)
	print('Your team is now at full health!\n')

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

def usePC():
	leave = False
	while leave == False:
		print('\nWhat would you like to do?')
		choice = getPCChoice()
		if choice == 1:
			withdrawPokemonChoice()
		elif choice == 2:
			depositPokemonChoice()
		elif choice == 3:
			print('This functionality is currently unavailable!')
#			movePokemonChoice()
		elif choice == 4:
			leave = True
			print()
			return

def withdrawPokemonChoice():
	y = 0
	while y == 0:
		count = 1
		print('\nWhich Pokemon would you like to withdraw?')
		for j in range(len(PC.boxes[0].inventory)):
			i = PC.boxes[0].inventory[j]
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
				for j in range(len(PC.boxes[0].inventory)):
					if int(choiceInput) == int(j+1):
						choice = PC.boxes[0].inventory[int(choiceInput) - 1]
						option = getOptionOneOrTwo('Withdraw', 'View more information')
						if option == 1:
							if len(player.team) < 6:
								player.team.append(choice)
								PC.boxes[0].inventory.remove(choice)
								print('You added', choice.name, 'to your party!')
							else:
								print('You have no room in your party for that right now!')
						else:
							getPokemonInfoViewPC(choice, 'withdraw')
						x = 1
						return 0
				if x == 0:
					print("Please choose a Pokemon from the list above!")
			except ValueError:
				print("Please choose a Pokemon from the list above!")	

def depositPokemonChoice():
	y = 0
	while y == 0:
		count = 1
		print('\nWhich Pokemon would you like to deposit?')
		for i in player.team:
			print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
			count += 1
		print('', count, '- Back')
		while True:
			try:
				x = 0
				choiceInput = input('-- ')
				if int(choiceInput) == int(count):
					return 0
				for j in range(len(player.team)):
					if choiceInput == player.team[j].name or int(choiceInput) == int(j+1):
						choice = player.team[int(choiceInput) - 1]
						option = getOptionOneOrTwo('Deposit', 'View more information')
						if option == 1:
							if len(player.team) > 1:
								player.team.remove(choice)
								PC.boxes[0].inventory.append(choice)
								print('You deposited', choice.name, 'into your PC!')
							else:
								print('You cannot deposit your only Pokemon!')
						else:
							getPokemonInfoViewPC(choice, 'deposit')
						x = 1
						return 0
				if x == 0:
					print("Please choose a Pokemon from the list above!")
			except ValueError:
				print("Please choose a Pokemon from the list above!")	

def getOptionOneOrTwo(option1, option2):
	print('What would you like to do with this pokemon?')
	print(' 1 -', option1, '\n 2 -', option2)
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def getOptionOneOrTwoOrThree(option1, option2, option3):
	print('What would you like to do with this pokemon?')
	print(' 1 -', option1, '\n 2 -', option2, '\n 3 -', option3)
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2 or choiceInput == 3:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def getPokemonInfoViewChoiceTeam():
	y = 0
	while y == 0:
		count = 1
		print('Which Pokemon would you like to view?')
		for i in player.team:
			print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
			count += 1
		print('', count, '- Back')
		while True:
			try:
				x = 0
				choiceInput = input('-- ')
				if int(choiceInput) == int(count):
					return 0
				for j in range(len(player.team)):
					if choiceInput == player.team[j].name or int(choiceInput) == int(j+1):
						choice = player.team[int(choiceInput) - 1]
						getPokemonInfoViewTeam(choice)
						x = 1
						return 0
				if x == 0:
					print("Please choose a Pokemon from the list above!")
			except ValueError:
				print("Please choose a Pokemon from the list above!")	

def getPokemonInfoViewTeam(pokemon):
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
			getPokemonInfoViewTeam(pokemon)
		else:
			return
	else:
		return

def getPokemonInfoViewPC(pokemon, page):
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
				getPokemonInfoViewPC(pokemon, 'withdraw')
			else:
				getPokemonInfoViewPC(pokemon, 'deposit')
		else:
			if page == 'withdraw':
				withdrawPokemonChoice()
			else:
				depositPokemonChoice()
	else:
		if page == 'withdraw':
			withdrawPokemonChoice()
		else:
			depositPokemonChoice()

def saveGame():
#	print("Before serialization: ")
#	print(player.name)
#	print("----------")
	serialized = pickle.dumps(player)
	filename = 'serialized.native'

	with open(filename,'wb') as file_object:
		file_object.write(serialized)


def loadGame():
	filename = 'serialized.native'

	with open(filename,'wb') as file_object:
		raw_data = file_object.read()

	player = pickle.loads(raw_data)

def startGame():
	player = Player()
	player.defaultTeam.append(test)
	player.defaultTeam.append(test2)
	player.defaultTeam.append(test3)
	player.team = player.defaultTeam
	while teamTotalHP(player) > 0:
		choice = battleTypeChoice()
		print('')
		if choice == 1:
#			enemyTeam = [Pokemon(random.choice(allPokemonList),100), Pokemon(random.choice(allPokemonList),100), Pokemon(random.choice(allPokemonList),100)]
			enemyTeam = [Pokemon(random.choice(allPokemonList),70),Pokemon(random.choice(allPokemonList),70)]
#			enemyTeam = [Pokemon(random.choice(allPokemonList),70)]
			createEnemy('Gym Leader', 'Brock', enemyTeam, 100, 'Damn! You beat me fair and square!')
			startBattle()
		elif choice == 2:
			wildTeam = [Pokemon('Kakuna',30)]
			#wildTeam = [Pokemon(random.choice(allPokemonList),50)]
			createEnemy('Wild', 'Wild', wildTeam, 0, 'Damn!')
			startBattle()
		elif choice == 3:
			pokemonCenter()


savefile = "/Users/bradellison/Documents/GitHub/pokemon-simulator/savefile.txt"

test = Pokemon('Ditto', 100)
#test = Pokemon(random.choice(allPokemonList),100)
test3 = Pokemon('Alakazam', 100)
test4 = Pokemon('Rattata', 10)
#test4 = Pokemon(random.choice(allPokemonList),100)
test5 = Pokemon('Rattata', 10)
test6 = Pokemon('Persian', 100)
test7 = Pokemon('Charmander', 100)

test = Pokemon(random.choice(allPokemonList),100)
test2 = Pokemon(random.choice(allPokemonList),100)
test3 = Pokemon(random.choice(allPokemonList),100)
test4 = Pokemon(random.choice(allPokemonList),100)
test5 = Pokemon(random.choice(allPokemonList),100)
test6 = Pokemon(random.choice(allPokemonList),100)

test7 = Pokemon(random.choice(allPokemonList),100)

balls = Ball('PokeBall',2)
balls2 = Ball('Master Ball',50)
#balls2 = Ball('Ultra Ball')

medicinex = Medicine('Potion',2)
mediciney = Medicine('Super Potion',1)

environment = Environment('x','y')
PC = PC()
PC.boxes.append(Box())

bag = Bag()

PC.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),100))
PC.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),100))
PC.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),100))
PC.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),100))
PC.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),100))
PC.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),100))

bag.balls.append(balls)
bag.balls.append(balls2)

bag.medicine.append(medicinex)
bag.medicine.append(mediciney)

player = Player()
player.defaultTeam.append(test)
player.defaultTeam.append(test2)
player.defaultTeam.append(test3)
player.team = player.defaultTeam
player.livingPokemon = len(player.team)

#wildTeam = [test7]
#enemyTeam = [Pokemon(random.choice(allPokemonList),100), Pokemon(random.choice(allPokemonList),100), Pokemon(random.choice(allPokemonList),100)]
#
##enemy = Enemy('Gym Leader', 'Brock', enemyTeam, 100, 'Damn!')
#enemy = Enemy('Wild', 'Wild', wildTeam, 0, 'Damn!')
enemyTeam = [Pokemon(random.choice(allPokemonList),100), Pokemon(random.choice(allPokemonList),100), Pokemon(random.choice(allPokemonList),100)]

enemy = Enemy(0, 0, 0, 0, 0)
print()

x = startGame()


## SOLVED - 