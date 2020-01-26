from random import randint
import random
from operator import add 

from classes import Move
from abilityFunctions import checkShedSkin, getAccuracyAbilityMult, getAbilityMultDamage, checkTintedLens, checkCompetitive, checkStartBattleIntimidate, checkKeenEye, checkShieldDust, checkIntimidateOnSwitch, checkFlashFireOrSimilar, checkContactAbilities
from getVariableFunctions import getBattleAccStat, getBattleAtkStat, getBattleDefStat, getBattleSpAtkStat, getBattleSpDefStat, getBattleSpdStat, getBattleEvasStat, getBattleCritStage, getPokemonType
from pokemonDictionaries import pokemonCritStageToMult, effectivenessScale, statDict
from moveDictionaries import allMoveList
from choicesFunctions import getYesOrNo
from bagFunctions import openBag
from typeInfo import allType
from levelUpFunctions import getExpYield, evolvePokemon
from pcFunctions import getPokemonInfoViewChoiceTeam
from screen import drawScreen

def getStabBonus(id,move):
	pokemonType = id.type; moveType = move.type
	if moveType in pokemonType:
		return 1.5
	else:
		return 1

def getTypeEffectiveness(defPokemon,atkPokemon):
	pokemonType = defPokemon.type; moveType = atkPokemon.move.type
	effectiveDict = allType[moveType]
	effectiveness = 1
	for i in pokemonType:
		effectiveness *= effectiveDict[i]
		effectiveness = checkTintedLens(effectiveness, atkPokemon)
	return effectiveness

def getHitOrMiss(data, atkPokemon,defPokemon,move):
	if defPokemon.immune == 1:
		return 'Miss'
	pokemonAccuracy = getBattleAccStat(atkPokemon)
	pokemonEvasiveness = getBattleEvasStat(defPokemon)
	moveAccuracy = move.accuracy
	abilityMult = getAccuracyAbilityMult(data, atkPokemon,defPokemon,move)
	chance = int(pokemonAccuracy * moveAccuracy * abilityMult / pokemonEvasiveness)
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

def getMoveDamage(data,atkPerson,atkPokemon,defPerson,defPokemon,move):
	stabBonus = getStabBonus(atkPokemon,move)
	effectiveness = getTypeEffectiveness(defPokemon,atkPokemon)
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
	abilityMult = getAbilityMultDamage(data,atkPerson,atkPokemon,defPerson,defPokemon,move)
	damage = int((((((2 * atkPokemon.level / 5) + 2) * aStat * move.damage / dStat) / 50) + 2) * stabBonus * effectiveness * critical * abilityMult / wall * float(randint(85,100)/100))
	if defPokemon.hp - damage < 0:
		damage = defPokemon.hp
	return damage

def getTurnOrder(data, myPokemon,enemyPokemon,myMove,enemyMove):
	if myMove.priority == enemyMove.priority:
		mySpd = getBattleSpdStat(data, myPokemon)
		enemySpd = getBattleSpdStat(data, enemyPokemon)
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

def battleStartPhrasing(data):
	if data.enemy.type == 'Wild':
		print('A wild', data.enemy.pokemon.name, 'appeared! Go,', data.player.pokemon.name + '!')
	else:
		print(data.enemy.type, data.enemy.name, 'sent out a', data.enemy.pokemon.name + '.', 'Go,', data.player.pokemon.name + '!')

def battleEnd(data):
	if data.enemy.type == 'Wild':
		print('You defeated the wild', data.enemy.pokemon.name)
	if data.enemy.type == 'Trainer' or data.enemy.type == 'Gym Leader':
		print('You defeated', data.enemy.type, data.enemy.name + '.', 'You received', data.enemy.prizeMoney, 'for winning!')

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

def moveChoiceInput(data):
	totalPP = getTotalPP(data.player.pokemon)
	if totalPP == 0:
		return 'Struggle'
	moveSet = data.player.pokemon.moveSet
	for i in range(len(moveSet)):
		print('', i + 1, '-', moveSet[i], '-', str(data.player.pokemon.movePPCurrent[i]) + '/' + str(data.player.pokemon.movePPMax[i]), 'PP')
	print('', len(moveSet) + 1, '- Back')
	while True:
		try:
			choiceInput = input('-- ')
			if int(choiceInput) == 1 and len(moveSet) >= 1:
				if data.player.pokemon.movePPCurrent[0] > 0:
					if data.player.pokemon.moveSet[0] != data.player.pokemon.disabledMove:
						data.player.pokemon.movePPCurrent[0] -= 1
						return moveSet[0]
					print('That move is disabled! Please choose another!')
				else:
					print('No PP remaining! Please choose another move!')
			elif int(choiceInput) == 2 and len(moveSet) >= 2:
				if data.player.pokemon.movePPCurrent[1] > 0:
					if data.player.pokemon.moveSet[1] != data.player.pokemon.disabledMove:
						data.player.pokemon.movePPCurrent[1] -= 1
						return moveSet[1]
					print('That move is disabled! Please choose another!')
				else:
					print('No PP remaining! Please choose another move!')
			elif int(choiceInput) == 3 and len(moveSet) >= 3:
				if data.player.pokemon.movePPCurrent[2] > 0:
					if data.player.pokemon.moveSet[2] != data.player.pokemon.disabledMove:
						data.player.pokemon.movePPCurrent[2] -= 1
						return moveSet[2]
					print('That move is disabled! Please choose another!')
				else:
					print('No PP remaining! Please choose another move!')
			elif int(choiceInput) == 4 and len(moveSet) >= 4:
				if data.player.pokemon.movePPCurrent[3] > 0:
					if data.player.pokemon.moveSet[3] != data.player.pokemon.disabledMove:
						data.player.pokemon.movePPCurrent[3] -= 1
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

def postTurnNVStatusCheckPlayer(data, player):
	if checkShedSkin(data, player.pokemon) == False:
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

def postTurnNVStatusCheckEnemy(data, enemy):
	if checkShedSkin(data, enemy.pokemon) == False:
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


def getEffectivenessWording(i):
	effectivenessWording = effectivenessScale[i]
	return effectivenessWording

def getMultiAttackCount(move):
	return randint(move.multiAttackMin,move.multiAttackMax)

def checkHealthSteal(atkPokemon, atkMove, damage):
	healAmount = 0
	if atkMove.healthSteal == 1 and atkPokemon.hp < atkPokemon.maxhp:
		healAmount = int(damage / 2)
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

def moveDealDamagePlayer(data):
	if data.player.pokemon.move.multiAttack == 1:
		numberOfHits = getMultiAttackCount(data.player.pokemon.move)
	else:
		numberOfHits = 1
	actualHits = 0
	totalDamage = 0
	while numberOfHits > 0 and data.enemy.pokemon.hp > 0:
		damage = getMoveDamage(data, data.player, data.player.pokemon, data.enemy, data.enemy.pokemon, data.player.pokemon.move)
		substitute = checkHitSubstitute(data.player.pokemon, data.enemy.pokemon, damage)
		if substitute == 1:
			damage = 0
		data.enemy.pokemon.hp -= damage	
		effectivenessWording = getEffectivenessWording(data.player.pokemon.move.currentEffectiveness)
		print('It did', damage, 'damage' + effectivenessWording, 'The opposing', data.enemy.pokemon.name, 'has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!')		
		if data.player.pokemon.criticalMove == 1:
			print('It was a critical hit!')
			data.player.pokemon.criticalMove = 0
		actualHits += 1
		numberOfHits -= 1
		totalDamage += damage
		healedAmount = checkHealthSteal(data.player.pokemon, data.player.pokemon.move, damage)
		checkAddBideDamage(data.enemy.pokemon, damage)
		checkRageBonus(data, data.enemy.pokemon)
		if healedAmount > 0:
			print(data.player.pokemon.name, 'gained', healedAmount, 'HP!')
	data.player.pokemon.previousDamage = totalDamage
	if data.player.pokemon.move.multiAttack == 1:
		print('It hit the enemy', actualHits, 'times!')

def moveDealDamageEnemy(data):
	if data.enemy.pokemon.move.multiAttack == 1:
		numberOfHits = getMultiAttackCount(data.enemy.pokemon.move)
	else:
		numberOfHits = 1
	actualHits = 0
	totalDamage = 0
	while numberOfHits > 0 and data.player.pokemon.hp > 0:
		damage = getMoveDamage(data, data.enemy, data.enemy.pokemon, data.player, data.player.pokemon, data.enemy.pokemon.move)
		substitute = checkHitSubstitute(data.enemy.pokemon, data.player.pokemon, damage)
		if substitute == 1:
			damage = 0
		data.player.pokemon.hp -= damage
		effectivenessWording = getEffectivenessWording(data.enemy.pokemon.move.currentEffectiveness)
		print('It did', damage, 'damage' + effectivenessWording, data.player.pokemon.name, 'has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!')
		if data.enemy.pokemon.criticalMove == 1:
			print('It was a critical hit!')
			data.enemy.pokemon.criticalMove = 0
		actualHits += 1
		numberOfHits -= 1
		totalDamage += damage
		healedAmount = checkHealthSteal(data.enemy.pokemon, data.enemy.pokemon.move, damage)
		checkAddBideDamage(data.player.pokemon, damage)
		checkRageBonus(data, data.player.pokemon)
		if healedAmount > 0:
			print('The opposing', data.player.pokemon.name, 'gained', healedAmount, 'HP!')
	data.enemy.pokemon.previousDamage = totalDamage
	if data.enemy.pokemon.move.multiAttack == 1:
		print('It hit', data.player.pokemon.name, actualHits, 'times!')

def moveDamageConfusion(data, atkPokemon):
	move = Move('Hit Self')
	damage = getMoveDamage(data, 0,atkPokemon,0,atkPokemon,move)
	if damage > atkPokemon.hp:
		damage = atkPokemon.hp
	return damage

def moveStatChangePlayer(data):
	chance = randint(1,100)
	if chance <= data.player.pokemon.move.statEffectChance:
		if data.player.pokemon.move.target == 'Self':
			data.player.pokemon.statStage = list(map(add, data.player.pokemon.statStage, data.player.pokemon.move.statEffect))
			moveStatWordingOnPlayer(data, data.player.pokemon.move.statEffect)
			checkCompetitive(data, data.player.pokemon, data.player.pokemon.move.statEffect)
			statStageMax(data, data.player.pokemon)
		if data.player.pokemon.move.target == 'Enemy':
			if data.enemy.mist == 0 and data.enemy.pokemon.substitute == 0:
				if data.player.pokemon.move.statEffect[6] < 0 and checkKeenEye(data, data.enemy.pokemon) == 1:
					return
				data.enemy.pokemon.statStage = list(map(add, data.enemy.pokemon.statStage, data.player.pokemon.move.statEffect))
				moveStatWordingOnEnemy(data, data.player.pokemon.move.statEffect)
				checkCompetitive(data, data.enemy.pokemon, data.player.pokemon.move.statEffect)
				statStageMax(data, data.enemy.pokemon)
			else:
				print('But it failed!')

def moveStatChangeEnemy(data):
	chance = randint(1,100)
	if chance <= data.enemy.pokemon.move.statEffectChance:
		if data.enemy.pokemon.move.target == 'Self':
			data.enemy.pokemon.statStage = list(map(add, data.enemy.pokemon.statStage, data.enemy.pokemon.move.statEffect))
			moveStatWordingOnEnemy(data, data.enemy.pokemon.move.statEffect)
			checkCompetitive(data, data.enemy.pokemon, data.enemy.pokemon.move.statEffect)
			statStageMax(data, data.enemy.pokemon)
		if data.enemy.pokemon.move.target == 'Enemy':
			if data.player.mist == 0 and data.player.pokemon.substitute == 0:
				if data.enemy.pokemon.move.statEffect[6] < 0 and checkKeenEye(data, data.player.pokemon) == 1:
					return
				data.player.pokemon.statStage = list(map(add, data.player.pokemon.statStage, data.enemy.pokemon.move.statEffect))
				moveStatWordingOnPlayer(data, data.enemy.pokemon.move.statEffect)
				checkCompetitive(data, data.player.pokemon, data.enemy.pokemon.move.statEffect)
				statStageMax(data, data.player.pokemon)
			else:
				print('But it failed!')

def statStageMax(data, pokemon):
	statStage = pokemon.statStage
	if pokemon == data.player.pokemon:
		count = 0
		for i in statStage:
			if i > 6:
				data.player.pokemon.statStage[count] = 6
			elif i < -6:
				data.player.pokemon.statStage[count] = -6
			count += 1
		if data.player.pokemon.statStage[8] > 3:
			data.player.pokemon.statStage[8] = 3
	else:
		count = 0
		for i in statStage:
			if i > 6:
				data.enemy.pokemon.statStage[count] = 6
			elif i < -6:
				data.enemy.pokemon.statStage[count] = -6
			count += 1
		if data.enemy.pokemon.statStage[8] > 3:
			data.enemy.pokemon.statStage[8] = 3

def moveStatWordingOnPlayer(data, statList):
	count = 0
	for i in statList:
		if i != 0:
			stat = statDict[count]
			changeForStat = statList[count]
			if changeForStat == 1:
				print(data.player.pokemon.name + '\'s', stat, 'raised!')
			if changeForStat == 2:
				print(data.player.pokemon.name + '\'s', stat, 'raised sharply!')
			if changeForStat >= 3:
				print(data.player.pokemon.name + '\'s', stat, 'raised hugely!')
			if changeForStat == -1:
				print(data.player.pokemon.name + '\'s', stat, 'fell!')
			if changeForStat == -2:
				print(data.player.pokemon.name + '\'s', stat, 'fell sharply!')
			if changeForStat <= -3:
				print(data.player.pokemon.name + '\'s', stat, 'fell hugely!')
		count += 1

def moveStatWordingOnEnemy(data, statList):
	count = 0
	for i in statList:
		if i != 0:
			stat = statDict[count]
			changeForStat = statList[count]
			if changeForStat == 1:
				print('The opposing', data.enemy.pokemon.name + '\'s', stat, 'raised!')
			if changeForStat == 2:
				print('The opposing', data.enemy.pokemon.name + '\'s', stat, 'raised sharply!')
			if changeForStat >= 3:
				print('The opposing', data.enemy.pokemon.name + '\'s', stat, 'raised hugely!')
			if changeForStat == -1:
				print('The opposing', data.enemy.pokemon.name + '\'s', stat, 'fell!')
			if changeForStat == -2:
				print('The opposing', data.enemy.pokemon.name + '\'s', stat, 'fell sharply!')
			if changeForStat <= -3:
				print('The opposing', data.enemy.pokemon.name + '\'s', stat, 'fell hugely!')
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

def moveNVEffectPlayer(data):
	if data.player.pokemon.move.nvEffect != 0 and randint(1,100) <= data.player.pokemon.move.nvEffectChance:
		if data.enemy.pokemon.nvStatus == 0 and data.enemy.pokemon.substitute == 0:
			if checkShieldDust(data.enemy.pokemon, data.player.pokemon) == False:
				data.enemy.pokemon.nvStatus = data.player.pokemon.move.nvEffect
				if data.enemy.pokemon.nvStatus == 3:
					data.enemy.pokemon.nvStatusCount = randint(2,4)
				wording = moveNVEffectWording(data.enemy.pokemon.nvStatus)
				print('The opposing', data.enemy.pokemon.name, 'was', wording)
		else:
			print('But it failed!')

def moveNVEffectEnemy(data):
	if data.enemy.pokemon.move.nvEffect != 0 and randint(1,100) <= data.enemy.pokemon.move.nvEffectChance:
		if data.player.pokemon.nvStatus == 0 and data.player.pokemon.substitute == 0:
			if checkShieldDust(data.player.pokemon, data.enemy.pokemon) == False:
				data.player.pokemon.nvStatus = data.enemy.pokemon.move.nvEffect
				if data.player.pokemon.nvStatus == 3:
					data.player.pokemon.nvStatusCount = randint(2,4)
				wording = moveNVEffectWording(data.player.pokemon.nvStatus)
				print(data.player.pokemon.name, 'was', wording)
		else:
			print('But it failed!')

def getEnemyMove(data):
	totalPP = getTotalPP(data.enemy.pokemon)
	if totalPP == 0:
		return 'Struggle'
	check = 0
	totalChoices = len(data.enemy.pokemon.moveSet)
	while check == 0:
		choice = randint(1,totalChoices)
		if data.enemy.pokemon.disabled == 1 and data.enemy.pokemon.moveSet[choice - 1] == data.enemy.pokemon.disabledMove:
			check = 0
		elif data.enemy.pokemon.movePPCurrent[choice - 1] > 0:
			data.enemy.pokemon.movePPCurrent[choice - 1] -= 1
			check = 1
			return data.enemy.pokemon.moveSet[choice - 1]

def getEnemySwitchPokemon(data):
	oldPokemon = data.enemy.pokemon
	while True:
		choice = random.choice(data.enemy.team)
		if choice != oldPokemon and choice.hp != 0:
			resetOnSwitch(oldPokemon)
			data.enemy.pokemon = choice
			break

def getEnemySwitchPokemonForce(data):
	oldPokemon = data.enemy.pokemon
	while True:
		choice = random.choice(data.enemy.team)
		if choice != oldPokemon and choice.hp != 0:
			resetOnSwitch(oldPokemon)
			data.enemy.pokemon = choice
			print('The opposing', oldPokemon.name, 'was forced out!', 'The', data.enemy.type, data.enemy.name, 'switched into', choice.name + '!')
			checkIntimidateOnSwitch(data, data.enemy, data.player)
			break

def getPlayerSwitchPokemonForce(data):
	oldPokemon = data.player.pokemon
	while True:
		choice = random.choice(data.player.team)
		if choice != oldPokemon and choice.hp != 0:
			resetOnSwitch(oldPokemon)
			data.player.pokemon = choice
			print(oldPokemon.name, 'was forced out and replaced with', choice.name + '!')
			checkIntimidateOnSwitch(data, data.player, data.enemy)
			break

def getSwitchPokemon(data):
	count = 1
	print('Which Pokemon would you like to switch to?')
	for i in data.player.team:
		print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
		count += 1
	print('', count, '- View more information')
	count += 1
	print('', count, '- Back')
	while True:
		try:
			x = 0
			choiceInput = input('-- ')
			trapped = data.player.pokemon.bind + data.player.pokemon.clamp + data.player.pokemon.fireSpin + data.player.pokemon.wrap
			if int(choiceInput) == 1:
				if data.player.pokemon.hp == 0:
					print(data.player.pokemon.name, 'has fainted! Please choose another Pokemon!')
					x = 1
				else:
					print('That Pokemon is already out! Please choose another Pokemon!')
					x = 1
			elif int(choiceInput) == int(count):
				if data.player.pokemon.hp == 0:
					print(data.player.pokemon.name, 'has fainted! Please choose another Pokemon!')
					x = 1
				else:
					print('Keep going,', data.player.pokemon.name + '!')
					return 0

					# No switch
			elif int(choiceInput) == int(count) - 1:
				getPokemonInfoViewChoiceTeam(data)
				print('')
				print('Which Pokemon would you like to switch to?')
				count = 1
				for i in data.player.team:
					print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
					count += 1
				print('', count, '- View more information')
				count += 1
				print('', count, '- Back')
				x = 1
			elif data.player.pokemon.hp != 0 and trapped != 0:
				print(data.player.pokemon.name, 'is unable to escape due to being trapped!')
			else:
				for j in range(len(data.player.team)):
					if choiceInput == data.player.team[j].name or int(choiceInput) == int(j+1):
						if data.player.team[j].hp == 0:
							print(data.player.team[j].name, 'has fainted! Please choose another Pokemon!')
							x = 1
						else:
							oldPokemon = data.player.pokemon
							data.player.team[j], data.player.team[0] = data.player.team[0], data.player.team[j]
							data.player.pokemon = data.player.team[0]
							resetOnSwitch(oldPokemon)
							print('You switched from', oldPokemon.name, 'into', data.player.pokemon.name + '!')
							checkIntimidateOnSwitch(data, data.player, data.enemy)
							print()
							data.player.pokemon.inCurrentBattle = 1
							return 1
			if x == 0:
				print("Please choose a Pokemon from the list above!")
		except ValueError:
			print("Please choose a Pokemon from the list above!")	


def checkSplash(move):
	if move == 'Splash':
		print('But nothing happened!')

def checkTrapStart(data, atkPokemon, defPokemon):
	move = atkPokemon.move.move
	traplist = ['Bind','Clamp','Fire Spin','Wrap','Leech Seed']
	if move in traplist:
		if move == traplist[0]:
			if defPokemon.bind == 0 and defPokemon.substitute == 0:
				defPokemon.bind = 1
				defPokemon.bindCount = randint(4,5)
				if atkPokemon == data.player.pokemon:
					print('The opposing', data.enemy.pokemon.name, 'is caught in a bind!')
				else:
					print(data.player.pokemon.name, 'is caught in a bind!')
				print()
			else:
				print('But it failed!\n')
		elif move == traplist[1]:
			if defPokemon.clamp == 0 and defPokemon.substitute == 0:
				defPokemon.clamp = 1
				defPokemon.clampCount = randint(4,5)
				if atkPokemon == data.player.pokemon:
					print('The opposing', data.enemy.pokemon.name, 'is clamped down!')
				else:
					print(data.player.pokemon.name, 'is clamped down!')
				print()
			else:
				print('But it failed!\n')
		elif move == traplist[2]:
			if defPokemon.fireSpin == 0 and defPokemon.substitute == 0:
				defPokemon.fireSpin = 1
				defPokemon.fireSpinCount = randint(4,5)
				if atkPokemon == data.player.pokemon:
					print('The opposing', data.enemy.pokemon.name, 'is caught in a firey vortex!')
				else:
					print(data.player.pokemon.name, 'is caught in a firey vortex!')
				print()
			else:
				print('But it failed!\n')
		elif move == traplist[3]:
			if defPokemon.wrap == 0 and defPokemon.substitute == 0:
				defPokemon.wrap = 1
				defPokemon.wrapCount = randint(4,5)
				if atkPokemon == data.player.pokemon:
					print('The opposing', data.enemy.pokemon.name, 'is wrapped up!')
				else:
					print(data.player.pokemon.name, 'is caught in a bind!')
				print()
			else:
				print('But it failed!\n')
		elif move == traplist[4]:
			if defPokemon.leechSeed == 0 and defPokemon.substitute == 0:
				defPokemon.leechSeed = 1
				if atkPokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'planted it\'s seed on the opposing', data.enemy.pokemon.name + '!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'planted it\'s seed on', data.player.pokemon.name + '!')
			else:
				print('But it failed!\n')

def checkTrapEffect(data, pokemon):
	if pokemon.bind == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'took', damage, 'HP damage due to it\'s bind! It has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', data.enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s bind! It has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!' )			
		if pokemon.hp > 0:
			pokemon.bindCount -= 1
			if pokemon.bindCount == 0:
				pokemon.bind = 0
				if pokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'escaped from it\'s bind!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'escaped from it\'s bind!' )
	if pokemon.clamp == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'took', damage, 'HP damage due to it\'s clamp! It has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', data.enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s clamp! It has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!' )			
		if pokemon.hp > 0:
			pokemon.clampCount -= 1
			if pokemon.clampCount == 0:
				pokemon.clamp = 0
				if pokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'escaped from it\'s clamp!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'escaped from it\'s clamp!' )
	if pokemon.fireSpin == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'took', damage, 'HP damage due to the firey vortex! It has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', data.enemy.pokemon.name, 'took', damage, 'HP damage due to the firey vortex! It has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!' )			
		if pokemon.hp > 0:
			pokemon.fireSpinCount -= 1
			if pokemon.fireSpinCount == 0:
				pokemon.fireSpin = 0
				if pokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'escaped from the firey vortex!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'escaped from the firey vortex!' )
	if pokemon.wrap == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'took', damage, 'HP damage due to it\'s wrap! It has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', data.enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s wrap! It has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!' )			
		if pokemon.hp > 0:
			pokemon.wrapCount -= 1
			if pokemon.wrapCount == 0:
				pokemon.wrap = 0
				if pokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'escaped from it\'s wrap!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'escaped from it\'s wrap!' )
	if pokemon.leechSeed == 1:
		damage = int(pokemon.maxhp / 16)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'took', damage, 'HP damage due to it\'s leeching! It has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!' )
		else:
			print('The opposing', data.enemy.pokemon.name, 'took', damage, 'HP damage due to it\'s leeching! It has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!' )			

	
def checkMetronome(data, pokemon):
	if pokemon.move.move == 'Metronome':
		randomMove = (random.choice(allMoveList))
		data.player.pokemon.move = Move(randomMove)
		if pokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'used', randomMove + '!')
		else:
			print('The opposing', data.enemy.pokemon.name, 'used', randomMove + '!')

def checkConversion(data, pokemon):
	if pokemon.move.move == 'Conversion':
		if pokemon == data.player.pokemon:
			data.player.pokemon.type = data.enemy.pokemon.type
			print(data.player.pokemon.name, 'copied the type of the opposing', data.enemy.pokemon.name + '!')
		else:
			data.enemy.pokemon.type = data.player.pokemon.type
			print('The opposing', data.enemy.pokemon.name, 'copied the type of', data.player.pokemon.name + '!')

def checkCounter(data, atkPokemon, defPokemon):
	if atkPokemon.move.move == 'Counter':
		if defPokemon.move.variety == 'Physical' and defPokemon.previousDamage > 0:
			damage = defPokemon.previousDamage * 2
			if defPokemon.hp < damage:
				damage = defPokemon.hp
			defPokemon.hp -= damage
			if atkPokemon == data.player.pokemon:
				print('It did', damage, 'damage! The opposing', data.enemy.pokemon.name, 'has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!')
			else:
				print('It did', damage, 'damage!', data.player.pokemon.name, 'has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!')
			checkRageBonus(data, defPokemon)
		else:
			print('But it failed!')		

def checkRecoil(data, atkPokemon):
	recoilList = ['Struggle','Double-Edge','Submission','Take Down']
	if atkPokemon.move.move in recoilList:
		recoilOneOver = 4
		if atkPokemon.move.move == 'Struggle':
			recoilOneOver = 2
		damage = int(atkPokemon.previousDamage / recoilOneOver)
		if damage > atkPokemon.hp:
			damage = atkPokemon.hp
		atkPokemon.hp -= damage
		if atkPokemon == data.player.pokemon:
			print('It took', damage, 'HP recoil damage!', data.player.pokemon.name, 'has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!')
		else:
			print('It took', damage, 'HP recoil damage! The opposing', data.enemy.pokemon.name, 'has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!' )

def checkSetDamage(data, atkPokemon, defPokemon):
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
			damage = atkPokemon.level
		elif move == 'Sonic Boom':
			damage = 20
		elif move == 'Super Fang':
			damage = int(defPokemon.hp / 2)
		if defPokemon.hp < damage:
			damage = defPokemon.hp
		defPokemon.hp -= damage
		if atkPokemon == data.player.pokemon:
			print('It did', damage, 'damage! The opposing', data.enemy.pokemon.name, 'has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!')
		else:
			print('It did', damage, 'damage!', data.player.pokemon.name, 'has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!')
		checkRageBonus(data, defPokemon)

def checkRest(data, pokemon):
	if pokemon.move.move == 'Rest':
		pokemon.nvStatus = 3
		pokemon.nvStatusCount = 3
		healAmount = pokemon.maxhp - pokemon.hp
		pokemon.hp = pokemon.maxhp
		if pokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'went to sleep to regain health, gaining', healAmount, 'HP. It has', (data.player.pokemon.hp), '/', (data.player.pokemon.maxhp), 'HP remaining!')
		else:
			print('The opposing', data.enemy.pokemon.name, 'went to sleep to regain health, gaining', healAmount, 'HP. It has', (data.enemy.pokemon.hp), '/', (data.enemy.pokemon.maxhp), 'HP remaining!')

def checkRegainHealth(data, pokemon):
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
		if pokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'regained', healAmount, 'HP. It has', (data.player.pokemon.hp), '/', (data.player.pokemon.maxhp), 'HP remaining!')
		else:
			print('The opposing', data.enemy.pokemon.name, 'regained', healAmount, 'HP. It has', (data.enemy.pokemon.hp), '/', (data.enemy.pokemon.maxhp), 'HP remaining!')

def gainHealth(data, pokemon, typeOfHeal, value):
	if typeOfHeal == 'constant':
		healAmount = value
	elif typeOfHeal == 'percentage':
		healAmount = (pokemon.maxhp / 100) * value
	if healAmount > pokemon.maxhp - pokemon.hp:
		healAmount = pokemon.maxhp - pokemon.hp
	pokemon.hp += healAmount
	if pokemon == data.player.pokemon:
		print(data.player.pokemon.name, 'regained', healAmount, 'HP. It has', (data.player.pokemon.hp), '/', (data.player.pokemon.maxhp), 'HP remaining!')
	else:
		print('The opposing', data.enemy.pokemon.name, 'regained', healAmount, 'HP. It has', (data.enemy.pokemon.hp), '/', (data.enemy.pokemon.maxhp), 'HP remaining!')

def checkHaze(atkPokemon, defPokemon):
	if atkPokemon.move.move  == 'Haze':
		print('All stat changes have been reset!')
		atkPokemon.statStage = [0,0,0,0,0,0,0,0,0]
		defPokemon.statStage = [0,0,0,0,0,0,0,0,0]

def checkForceSwitch(data, atkPokemon):
	forceSwitchMoves = ['Roar','Whirlwind']
	if atkPokemon.move.move in forceSwitchMoves:
		if atkPokemon == data.player.pokemon:
			if data.enemy.type != 'Wild':
				if data.enemy.livingPokemon > 1:
					getEnemySwitchPokemonForce(data)
				else:
					print('But it failed!')
			else:
				print(data.player.pokemon.name, 'blew the opposing', data.enemy.pokemon.name, 'away! The battle is over!')
				data.environment.battleEnd = 1
		else:
			if data.enemy.type != 'Wild':
				if data.player.livingPokemon > 1:
					getPlayerSwitchPokemonForce(data)
				else:
					print('But it failed!')
			else:
				print('The opposing', data.enemy.pokemon.name, 'blew', data.enemy.pokemon.name, 'away! The battle is over!')
				data.environment.battleEnd = 1

def checkCopyMove(data, atkPokemon,defPokemon):
	copyMoveList = ['Mimic','Mirror Move']
	if atkPokemon.move.move in copyMoveList:
		if defPokemon.previousMove != 0:
			atkPokemon.move = defPokemon.previousMove
			if atkPokemon == data.player.pokemon:
				print(data.player.pokemon.name, 'copied', atkPokemon.move.move + '!')
			else:
				print('The opposing', data.enemy.pokemon.name, 'copied', atkPokemon.move.move + '!')	
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

def checkDefensiveWall(data, person):
	wallList = ['Light Screen','Reflect','Mist']
	move = person.pokemon.move.move
	if move in wallList:
		if move == 'Light Screen':
			if person.lightScreen == 0:
				person.lightScreen = 1
				person.lightScreenCount = 6
				if person == data.player:
					print('Light Screen raised your team\'s Sp. Def!')
				else:
					print('Light Screen raised the opposing team\'s Sp. Def!')
			else:
				print('But it failed!')
		if move == 'Reflect':
			if person.reflect == 0:
				person.reflect = 1
				person.reflectCount = 6
				if person == data.player:
					print('Reflect raised your team\'s Def!')
				else:
					print('Reflect raised the opposing team\'s Def!')
			else:
				print('But it failed!')
		if move == 'Mist':
			if person.mist == 0:
				person.mist = 1
				person.mistCount = 6
				if person == data.player:
					print('Your team has been protected from stat changes!')
				else:
					print('Your opponent\'s team has been protected from stat changes')
			else:
				print('But it failed!')


def checkAttackSecondTurnMoves(data, pokemon):
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
				statStageMax(data, pokemon)		
			elif pokemon.move.move == 'Sky Attack':
				wording = 'began charging up!'
			if pokemon == data.player.pokemon:
				print(data.player.pokemon.name, wording)
			else:
				print('The opposing', data.enemy.pokemon.name, wording)	
			return 1		
		else:
			pokemon.lockedInMoveNumber -= 1
			if pokemon.lockedInMoveNumber == 0:
				pokemon.immune = 0
				return 0
	else:
		return 0

def checkAttackFirstTurnMoves(data, pokemon):
	firstTurnMoves = ['Hyper Beam', 'Solar Beam']
	if pokemon.move.move in firstTurnMoves:
		if pokemon.lockedInMoveNumber == 0:
			pokemon.lockedInMoveNumber = 1
			return 0	
		else:
			pokemon.lockedInMoveNumber -= 1
			if pokemon.lockedInMoveNumber == 0:
				if pokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'has to recharge!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'has to recharge')
				return 1
	else:
		return 0

def checkBide(data, pokemon, defPokemon):
	if pokemon.move.move == 'Bide':
		if pokemon.lockedInMoveNumber == 0:
			pokemon.bide = 1
			pokemon.lockedInMoveNumber = 2
			if pokemon == data.player.pokemon:
				print(data.player.pokemon.name, 'began storing energy!')
			else:
				print('The opposing', data.enemy.pokemon.name, 'began storing energy!')	
			return 0	
		else:
			pokemon.lockedInMoveNumber -= 1
			if pokemon.lockedInMoveNumber == 0:
				damage = 2 * pokemon.bideDamage
				if defPokemon.hp < damage:
					damage = defPokemon.hp
				defPokemon.hp -= damage
				if pokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'released it\'s energy! It did', damage, 'against the opposing', data.enemy.pokemon.name + '! It has', str(data.enemy.pokemon.hp) + '/' + str(data.enemy.pokemon.maxhp), 'remaining!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'released it\'s energy! It did', damage, 'against', data.player.pokemon.name + '! It has', str(data.player.pokemon.hp) + '/' + str(data.player.pokemon.maxhp), 'remaining!')				
				checkRageBonus(data, defPokemon)
				pokemon.bideDamage = 0
				pokemon.bide = 0
			else:
				if pokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'is still storing energy!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'is still storing energy!')					
	else:
		return 0

def checkThrashOrPetal(data, pokemon):
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
				if pokemon == data.player.pokemon:
					print(data.player.pokemon.name, 'has become confused!')
				else:
					print('The opposing', data.enemy.pokemon.name, 'has become confused!')					
				return 0
			else:
				return 0		
	else:
		return 0

def checkPayDay(data, pokemon):
	if pokemon.move.move == 'Pay Day':
		multiplier = randint(2,5)
		data.environment.payDayExtra += multiplier * pokemon.level

def checkAddBideDamage(pokemon, damage):
	if pokemon.bide == 1:
		pokemon.bideDamage += damage

def checkRage(data, pokemon):
	if pokemon.move.move == 'Rage':
		pokemon.rage = 1
	else:
		if pokemon.rageCount != 0:
			pokemon.statStage = list(map(add, pokemon.statStage, [0,-pokemon.rageCount,0,0,0,0,0,0,0]))
			statStageMax(data, pokemon)
			pokemon.rageCount = 0
		pokemon.rage = 0

def checkRageBonus(data, pokemon):
	if pokemon.rage == 1:
		pokemon.statStage = list(map(add, pokemon.statStage, [0,1,0,0,0,0,0,0,0]))
		statStageMax(data, pokemon)
		pokemon.rageCount += 1

def checkTeleport(data, player, enemy):
	if data.player.pokemon.move.move == 'Teleport':
		if data.enemy.type == 'Wild':
			return 1
	if data.enemy.pokemon.move.move == 'Teleport':
		return 1

def checkStartSubstitute(data, pokemon):
	if pokemon.move.move == 'Substitute':
		if pokemon.substitute == 1:
			print('But it failed!')
		elif pokemon.hp > int(pokemon.maxhp / 4) + 1:
			pokemon.substitute = 1
			pokemon.substituteHealth = int(pokemon.maxhp / 4)
			pokemon.hp -= pokemon.substituteHealth
			print(pokemon.substitute, 'yy')
			if pokemon == data.player.pokemon:
				print(data.player.pokemon.name, 'has placed a substitute and lost', pokemon.substituteHealth, 'HP! It has', data.player.pokemon.hp, '/', data.player.pokemon.maxhp, 'HP remaining!')
			else:
				print('The opposing', data.enemy.pokemon.name, 'has placed a substitute and lost', pokemon.substituteHealth, 'HP! It has', data.enemy.pokemon.hp, '/', data.enemy.pokemon.maxhp, 'HP remaining!')	
		else:
			print('But it failed!')

def checkDisable(data, atkPokemon, defPokemon):
	if atkPokemon.move.move == 'Disable':
		if defPokemon.previousMove != 0 and defPokemon.disabled != 1:
			defPokemon.disabled = 1
			defPokemon.disabledCount = randint(3,6)
			defPokemon.disabledMove = defPokemon.previousMove.move
			if atkPokemon == data.player.pokemon:
				print('The opposing', data.enemy.pokemon.name, 'can no longer use', data.enemy.pokemon.disabledMove + '!')
			else:
				print(data.player.pokemon.name, 'can no longer use', data.player.pokemon.disabledMove + '!')	
		else:
			print('But it failed!')

def checkTransform(data, atkPokemon, defPokemon):
	if atkPokemon.move.move == 'Transform':
		atkPokemon.moveSet = defPokemon.moveSet
		atkPokemon.movePPCurrent = defPokemon.movePPMax
		if atkPokemon == data.enemy.pokemon:
			print('The opposing', data.enemy.pokemon.name, 'transformed into', data.player.pokemon.name + '!')
		else:
			print(data.player.pokemon.name, 'transformed into', data.enemy.pokemon.name + '!')	

def startPlayerTurn(data):
	interrupt = 0
	interrupt = checkAttackFirstTurnMoves(data, data.player.pokemon)
	if data.player.pokemon.flinch == 1:
		interrupt += 1
		print(data.player.pokemon.name, 'flinched!')
	if data.player.pokemon.nvStatus != 0:
		interrupt += preTurnNVStatusCheck(data.player)
	if interrupt == 0:
		if interrupt == 0:
			if data.player.pokemon.confused == 1:
				print(data.player.pokemon.name, 'is confused!')
				hitOrConfused = getHitOrConfused(data.player.pokemon)
				if hitOrConfused > 0:
					if hitOrConfused == 1:
						damage = moveDamageConfusion(data, data.player.pokemon)
						data.player.pokemon.hp -= damage
						print(data.player.pokemon.name, 'hit itself in confusion and did', damage, 'HP damage. It has', str(data.player.pokemon.hp) + '/' + str(data.player.pokemon.maxhp), 'remaining!')
						interrupt = 1
					else:
						print(data.player.pokemon.name, 'snapped out of confusion!')
			if interrupt == 0:
				interrupt = checkAttackSecondTurnMoves(data, data.player.pokemon)
				if interrupt == 0:				
					hitOrMiss = getHitOrMiss(data, data.player.pokemon,data.enemy.pokemon,data.player.pokemon.move)
					if hitOrMiss == 'Miss':
						print(data.player.pokemon.name, 'tried to use', data.player.pokemon.move.move + ', but it missed!')
						checkMissDamage(data, data.player.pokemon)
						interrupt = 1
					if interrupt == 0:
						print(data.player.pokemon.name, 'used', data.player.pokemon.move.move, 'against the opposing', data.enemy.pokemon.name + '.')
						interrupt = checkFainted(data.enemy.pokemon)
						interrupt += checkDreamEater(data.player.pokemon, data.enemy.pokemon)
						if interrupt == 0:
							checkCopyMove(data, data.player.pokemon, data.enemy.pokemon)
							checkMetronome(data, data.player.pokemon)
							checkConversion(data, data.player.pokemon)
							checkCounter(data, data.player.pokemon, data.enemy.pokemon)
							checkFlinch(data.player.pokemon.move, data.enemy.pokemon)
							checkSplash(data.player.pokemon.move.move)
							checkSetDamage(data, data.player.pokemon, data.enemy.pokemon)
							checkRest(data, data.player.pokemon)
							checkRegainHealth(data, data.player.pokemon)
							checkHaze(data.player.pokemon, data.enemy.pokemon)
							checkForceSwitch(data, data.player.pokemon)
							checkDefensiveWall(data, data.player)
							checkBide(data, data.player.pokemon, data.enemy.pokemon)
							checkRage(data, data.player.pokemon)
							checkPayDay(data, data.player.pokemon)
							checkStartSubstitute(data, data.player.pokemon)
							checkDisable(data, data.player.pokemon, data.enemy.pokemon)
							checkTransform(data, data.player.pokemon, data.enemy.pokemon)
							if checkFlashFireOrSimilar(data, data.player.pokemon, data.enemy.pokemon) == 0:
								if data.player.pokemon.move.damage != 0:
									moveDealDamagePlayer(data)
									checkRecoil(data, data.player.pokemon)
									checkContactAbilities(data, data.player.pokemon, data.enemy.pokemon)
							checkThrashOrPetal(data, data.player.pokemon)
							if data.enemy.pokemon.hp == 0:
								print('The opposing', data.enemy.pokemon.name, 'fainted!')
							checkTrapStart(data, data.player.pokemon, data.enemy.pokemon)
							checkKamikaze(data, data.player.pokemon.move, data.player.pokemon)
							if data.enemy.pokemon.hp != 0:
								if data.player.pokemon.move.statEffect != 0:
									moveStatChangePlayer(data)
								if data.player.pokemon.move.nvEffect != 0:
									moveNVEffectPlayer(data)
								if data.player.pokemon.move.vEffect != 0:
									confuse = checkConfusion(data.player.pokemon.move, data.enemy.pokemon)
									if confuse == 1:
										print('The opposing', data.enemy.pokemon.name, 'is confused!')
	data.player.pokemon.previousMove = data.player.pokemon.move
#	if player.pokemon.lockedInMoveNumber > 0:
#		player.pokemon.lockedInMoveNumber -= 1
	print()	

def startEnemyTurn(data):
	interrupt = 0
	interrupt = checkAttackFirstTurnMoves(data, data.enemy.pokemon)
	if data.enemy.pokemon.flinch == 1:
		interrupt += 1
		print('The opposing', data.enemy.pokemon.name, 'flinched!')	
	if data.enemy.pokemon.nvStatus != 0:
		interrupt += preTurnNVStatusCheck(data.enemy)
	if interrupt == 0:
		if interrupt == 0:
			if data.enemy.pokemon.confused == 1:
				print(data.enemy.pokemon.name, 'is confused!')				
				hitOrConfused = getHitOrConfused(data.enemy.pokemon)		
				if hitOrConfused > 0:
					if hitOrConfused == 1:
						damage = moveDamageConfusion(data, data.enemy.pokemon)
						data.enemy.pokemon.hp -= damage
						print('The opposing', data.enemy.pokemon.name, 'hit itself in confusion and did', damage, 'HP damage. It has', str(data.enemy.pokemon.hp) + '/' + str(data.enemy.pokemon.maxhp), 'remaining!')
						interrupt = 1
					else:
						print('The opposing', data.enemy.pokemon.name, 'snapped out of confusion!')
			if interrupt == 0:
				interrupt = checkAttackSecondTurnMoves(data, data.enemy.pokemon)
				if interrupt == 0:
					hitOrMiss = getHitOrMiss(data, data.enemy.pokemon,data.player.pokemon,data.enemy.pokemon.move)
					if hitOrMiss == 'Miss':
						print('The opposing', data.enemy.pokemon.name, 'tried to use', data.enemy.pokemon.move.move + ', but it missed!')
						checkMissDamage(data, data.enemy.pokemon)
						interrupt = 1
					if interrupt == 0:
						print('The opposing', data.enemy.pokemon.name, 'used', data.enemy.pokemon.move.move, 'against', data.player.pokemon.name + '.')
						interrupt = checkFainted(data.player.pokemon)
						interrupt += checkDreamEater(data.enemy.pokemon, data.player.pokemon)
						if interrupt == 0:
							checkCopyMove(data, data.enemy.pokemon, data.player.pokemon)
							checkMetronome(data, data.enemy.pokemon)
							checkConversion(data, data.enemy.pokemon)
							checkCounter(data, data.enemy.pokemon, data.player.pokemon)
							checkSplash(data.enemy.pokemon.move.move)
							checkFlinch(data.enemy.pokemon.move, data.player.pokemon)
							checkSetDamage(data, data.enemy.pokemon, data.player.pokemon)
							checkRest(data, data.enemy.pokemon)
							checkRegainHealth(data, data.enemy.pokemon)
							checkHaze(data.enemy.pokemon, data.player.pokemon)
							checkForceSwitch(data, data.enemy.pokemon)
							checkDefensiveWall(data, data.enemy)
							checkBide(data, data.enemy.pokemon, data.player.pokemon)
							checkRage(data, data.enemy.pokemon)
							checkPayDay(data, data.enemy.pokemon)
							checkStartSubstitute(data, data.enemy.pokemon)
							checkDisable(data, data.enemy.pokemon, data.player.pokemon)
							checkTransform(data, data.enemy.pokemon, data.player.pokemon)
							if checkFlashFireOrSimilar(data, data.enemy.pokemon, data.player.pokemon) == 0:
								if data.enemy.pokemon.move.damage != 0:
									moveDealDamageEnemy(data)
									checkRecoil(data, data.enemy.pokemon)
									checkContactAbilities(data, data.enemy.pokemon, data.player.pokemon)
							checkThrashOrPetal(data, data.enemy.pokemon)
							if data.player.pokemon.hp == 0:
								print(data.player.pokemon.name, 'fainted!')					
							checkTrapStart(data, data.enemy.pokemon, data.player.pokemon)
							checkKamikaze(data, data.enemy.pokemon.move, data.enemy.pokemon)
							if data.player.pokemon.hp != 0:
								if data.enemy.pokemon.move.statEffect != 0:
									moveStatChangeEnemy(data)
								if data.enemy.pokemon.move.nvEffect != 0:
									moveNVEffectEnemy(data)
								if data.enemy.pokemon.move.vEffect != 0:
									confuse = checkConfusion(data.enemy.pokemon.move, data.player.pokemon)
									if confuse == 1:
										print(data.player.pokemon.name, 'is confused!')
	data.enemy.pokemon.previousMove = data.enemy.pokemon.move
#	if enemy.pokemon.lockedInMoveNumber > 0:
#		enemy.pokemon.lockedInMoveNumber -= 1
	print()

def checkMissDamage(data,pokemon):
	if pokemon.move.move == 'High Jump Kick' or pokemon.move.move == 'Jump Kick':
		damage = int(pokemon.maxhp / 2)
		if damage > pokemon.hp:
			damage = pokemon.hp
		pokemon.hp -= damage
		if pokemon.hp == 0:
			if pokemon == data.player.pokemon:
				print(data.player.pokemon.name, 'kept going and took', damage, 'HP damage and fainted!')
			else:
				print('The opposing', data.enemy.pokemon.name, 'kept going and took', damage, 'HP damage and fainted!')
		else:
			if pokemon == data.player.pokemon:
				print(data.player.pokemon.name, 'kept going and took', damage, 'HP damage! It has', str(data.player.pokemon.hp) + '/' + str(data.player.pokemon.maxhp), 'remaining!')
			else:
				print('The opposing', data.enemy.pokemon.name, 'kept going and took', damage, 'HP damage! It has', str(data.enemy.pokemon.hp) + '/' + str(data.enemy.pokemon.maxhp), 'remaining!')

def teamTotalHP(person):
	totalHP = 0
	for i in person.team:
		totalHP += i.hp
	return totalHP

def getRun(data):
	if data.enemy.type == 'Wild':
		chance = randint(1,2)
		if chance == 1 or data.player.pokemon.ability == 'Run Away':
			print('You got away!')
			return 1
		else:
			print('You couldn\'t get away!')
			return 0

def checkWallCounts(data):
	if data.player.lightScreen == 1:
		data.player.lightScreenCount -= 1
		if data.player.lightScreenCount == 0:
			data.player.lightScreen = 0
			print('Your team\'s light screen wore off!')
	if data.player.reflect == 1:
		data.player.reflectCount -= 1
		if data.player.reflectCount == 0:
			data.player.reflect = 0
			print('Your team\'s reflect wore off!')
	if data.player.mist == 1:
		data.player.mistCount -= 1
		if data.player.mistCount == 0:
			data.player.mist = 0
			print('Your team\'s mist wore off!')
	if data.enemy.lightScreen == 1:
		data.enemy.lightScreenCount -= 1
		if data.enemy.lightScreenCount == 0:
			data.enemy.lightScreen = 0
			print('The opposing team\'s light screen wore off!')
	if data.enemy.reflect == 1:
		data.enemy.reflectCount -= 1
		if data.enemy.reflectCount == 0:
			data.enemy.reflect = 0
			print('The opposing team\'s reflect wore off!')
	if data.enemy.mist == 1:
		data.enemy.mistCount -= 1
		if data.enemy.mistCount == 0:
			data.enemy.mist = 0
			print('The opposing team\'s mist wore off!')

def checkDisableCounts(data):
	if data.player.pokemon.disabledCount == 1:
		data.player.pokemon.disabledCount -= 1
		if data.player.pokemon.disabledCount == 0:
			data.player.pokemon.disabled = 0
			print(data.player.pokemon.name, 'is now able to use', data.player.pokemon.disabledMove, 'again!')
			data.player.pokemon.disabledMove = 0
	if data.enemy.pokemon.disabled == 1:
		data.enemy.pokemon.disabledCount -= 1
		if data.enemy.pokemon.disabledCount == 0:
			data.enemy.pokemon.disabled = 0
			print(data.enemy.pokemon.name, 'is now able to use', data.enemy.pokemon.disabledMove, 'again!')
			data.enemy.pokemon.disabledMove = 0

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
	pokemon.flashFireMult = 1

def endRound(data):
	for pokemon in data.player.team:
		pokemon.flinch = 0
	for pokemon in data.enemy.team:
		pokemon.flinch = 0
	checkWallCounts(data)
	checkDisableCounts(data)

def endBattlePokemonInfo(data):
	for pokemon in data.player.team:
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
		pokemon.flashFireMult = 1
	for pokemon in data.enemy.team:
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
		pokemon.flashFireMult = 1

def checkFlinch(atkMove, defPokemon):
	if atkMove.flinch == 1 and defPokemon.ability != 'Inner Focus':
		if randint(1,100) <= atkMove.flinchChance:
			defPokemon.flinch = 1

def checkKamikaze(data, atkMove, atkPokemon):
	if atkMove.move == 'Self-Destruct' or atkMove.move == 'Explosion':
		damage = atkPokemon.hp
		atkPokemon.hp -= atkPokemon.hp
		if atkPokemon == data.player.pokemon:
			print(data.player.pokemon.name, 'took', damage, 'HP damage and fainted!')
		else:
			print('The opposing', data.enemy.pokemon.name, 'took', damage, 'HP damage and fainted!')

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

def getCurrentFight(data):
		while data.player.pokemon.hp > 0 and data.enemy.pokemon.hp > 0 and data.environment.battleEnd == 0:
			drawScreen(data)
			data.player.pokemon.inCurrentBattle = 1
			interrupt = 0
			if data.player.pokemon.lockedInMoveNumber == 0:
				battleChoice = battleChoiceInput()
			if battleChoice == 'Fight':
				data.player.pokemon.inCurrentBattle = 1
				if data.player.pokemon.lockedInMoveNumber == 0:
					moveChoice = moveChoiceInput(data)
				if moveChoice == 'Back':
					interrupt = 1
				else:
					if data.enemy.pokemon.lockedInMoveNumber == 0:
						enemyChoice = getEnemyMove(data)
						data.enemy.pokemon.move = Move(enemyChoice)
					data.player.pokemon.move = Move(moveChoice)
					turnOrder = getTurnOrder(data, 
					data.player.pokemon,data.enemy.pokemon,data.player.pokemon.move,data.enemy.pokemon.move)
					if turnOrder == 'myPokemonFirst':
						startPlayerTurn(data)
						if data.enemy.pokemon.hp != 0 and data.environment.battleEnd == 0:
							startEnemyTurn(data)
					if turnOrder == 'enemyPokemonFirst':
						startEnemyTurn(data)
						if data.player.pokemon.hp != 0 and data.environment.battleEnd == 0:
							startPlayerTurn(data)
			elif battleChoice == 'Pokemon':
				switch = getSwitchPokemon(data)
				if switch == 1:
					if data.enemy.pokemon.lockedInMoveNumber == 0:
						enemyChoice = getEnemyMove(data)
						data.enemy.pokemon.move = Move(enemyChoice)					
					startEnemyTurn(data)
				else:
					interrupt = 1
			elif battleChoice == 'Bag':
				choice = openBag(data)
				if choice == 1:
					interrupt = 1
				elif choice == 'Catch':
					return 'End'
				else:
					if data.enemy.pokemon.lockedInMoveNumber == 0:
						enemyChoice = getEnemyMove(data)
						data.enemy.pokemon.move = Move(enemyChoice)					
					startEnemyTurn(data)
			elif battleChoice == 'Run':
				if data.enemy.type == 'Wild':
					run = getRun(data)
					print()
					if run == 0:
						if data.enemy.pokemon.lockedInMoveNumber == 0:
							enemyChoice = getEnemyMove(data)
							data.enemy.pokemon.move = Move(enemyChoice)
						startEnemyTurn(data)
					else:
						return 'End'
				else:
					print('You can\'t run away from this battle!')
					interrupt = 1
			teleport = checkTeleport(data, data.player, data.enemy)
			if teleport == 1:
				print('The battle ended!')
				return 'End'
			if interrupt == 0:
				if data.player.pokemon.hp != 0:
					postTurnNVStatusCheckPlayer(data, data.player)
				if data.player.pokemon.hp != 0:
					checkTrapEffect(data, data.player.pokemon)
				if data.player.pokemon.hp == 0:
					if teamTotalHP(data.player) > 0:
						data.player.livingPokemon -= 1
						data.player.pokemon.inCurrentBattle = 0
						switch = getSwitchPokemon(data)
						while switch == 0:
							switch = getSwitchPokemon(data)		
				if data.enemy.pokemon.hp != 0:
					postTurnNVStatusCheckEnemy(data, data.enemy)
				if data.player.pokemon.hp != 0:
					checkTrapEffect(data, data.enemy.pokemon)
				if data.enemy.pokemon.hp == 0:
					getExpYield(data)
					if teamTotalHP(data.enemy) > 0:
						data.enemy.livingPokemon -= 1
						getResetInBattle(data)
						getEnemySwitchPokemon(data)
						print('The', data.enemy.type, data.enemy.name, 'is about to send out a', data.enemy.pokemon.name + '.', 'Would you like to switch?')
						choice = getYesOrNo()
						if choice == 1:
							getSwitchPokemon(data)
							checkStartBattleIntimidate(data)
						else:
							checkIntimidateOnSwitch(data, data.enemy,data.player)
			endRound(data)

def getResetInBattle(data):
	for i in data.player.team:
		i.inCurrentBattle = 0

def startBattle(data):
	data.player.team = data.player.defaultTeam
	data.player.pokemon = data.player.team[0]
	data.enemy.pokemon = data.enemy.team[0]
	battleStartPhrasing(data)
	getPreBattleEffects(data)
	while teamTotalHP(data.player) > 0 and teamTotalHP(data.enemy) > 0 and data.environment.battleEnd == 0:
		game = getCurrentFight(data)
		if game == 'End':
			return 'Win'
	if teamTotalHP(data.player) == 0:
		print('You lost!')
		return 'Lose'
	elif teamTotalHP(data.enemy) == 0:
		winBattle(data)
		return 'Win'
	elif data.environment.battleEnd == 1:
		data.environment.battleEnd = 0
		return 'Win'

def getPreBattleEffects(data):
	checkStartBattleIntimidate(data)

def winBattle(data):
	if data.enemy.type != 'Wild':
		print(data.enemy.text)
		cash = randint(200,500)
		cash += data.environment.payDayExtra
		data.player.money += cash
		print('You earned $' + str(cash), 'for winning!\n')
	for i in data.player.team:
		if i.shouldEvolve == 1:
			print('Something is happening to', i.name + '! Let it continue?')
			if getYesOrNo() == 1:
				evolvePokemon(i)
	endBattlePokemonInfo(data)


def createEnemy(data, typex, name, team, prizeMoney, text):
	data.enemy.type = typex
	data.enemy.name = name
	data.enemy.team = team
	data.enemy.livingPokemon = len(team)
	data.enemy.prizeMoney = prizeMoney
	data.enemy.text = text
	data.enemy.pokemon = data.enemy.team[0]