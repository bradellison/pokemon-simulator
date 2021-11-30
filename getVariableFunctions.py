import random
from random import randint

from pokemonDictionaries import pokemonStats, natureDictionary, pokemonStatStageToMult, pokemonTypes, pokemonCatchRates, pokemonExpGroup, pokemonYields, pokemonGenderRatio, allNaturesList, pokemonAbilities, pokemonPossibleMovesByLevel, pokemonSprites
from moveDictionaries import moveInfo

def getRandomIV():
	IV = []
	for _ in range(6):
		x = randint(1,31)
		IV.append(x)
	return IV

def getBaseStats(species):
	stats = pokemonStats[species]
	return stats

def gethpStat(id):
	level = id.level; iv = id.iv; baseStats = id.baseStats
	return int(((2 * baseStats[0] + iv[0])* level / 100 ) + level + 10)

def getAtkStat(id):
	level = id.level; iv = id.iv; baseStats = id.baseStats
	natureBonus = getNatureChange(id, 1)
	return int((((2 * baseStats[1] + iv[1]) * level / 100) + 5) * natureBonus)

def getDefStat(id):
	level = id.level; iv = id.iv; baseStats = id.baseStats
	natureBonus = getNatureChange(id, 2)
	return int((((2 * baseStats[2] + iv[2]) * level / 100) + 5) * natureBonus)

def getSpAtkStat(id):
	level = id.level; iv = id.iv; baseStats = id.baseStats
	natureBonus = getNatureChange(id, 3)
	return int((((2 * baseStats[3] + iv[3]) * level / 100) + 5) * natureBonus)

def getSpDefStat(id):
	level = id.level; iv = id.iv; baseStats = id.baseStats
	natureBonus = getNatureChange(id, 4)
	return int((((2 * baseStats[4] + iv[4]) * level / 100) + 5) * natureBonus)

def getSpdStat(id):
	level = id.level; iv = id.iv; baseStats = id.baseStats
	natureBonus = getNatureChange(id, 5)
	return int((((2 * baseStats[5] + iv[5]) * level / 100) + 5) * natureBonus)

def getNatureChange(id, stat):
	natureChangeList = natureDictionary[id.nature]
	if stat == natureChangeList[0]:
		return 1.1
	elif stat == natureChangeList[1]:
		return 0.9
	else:
		return 1

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

def getBattleSpdStat(data, id):
	stat = id.stats[5]; statStage = id.statStage[5]
	mult = pokemonStatStageToMult[statStage]
	mult *= getSpdAbilityMult(data, id)
	return int(mult * stat)

def getSpdAbilityMult(data, id):
	if id.ability == 'Chlorophyll' and data.environment.weather == 'Sunshine':
		return 2
	return 1

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

def getBattleStats(data, id):
	return [getBattlehpStat(id),getBattleAtkStat(id),getBattleDefStat(id),getBattleSpAtkStat(id),getBattleSpDefStat(id),getBattleSpdStat(data, id),getBattleAccStat(id),getBattleEvasStat(id)]

def getPokemonType(id):
	fromDict = pokemonTypes[id.species]
	pokemonType = [fromDict['Type One']]
	if fromDict['Type Two'] != 'Null':
		pokemonType.append(fromDict['Type Two'])
	return pokemonType

def getRandomPersonalityValue():
	personalityValueString = ''
	for _ in range(32):
		digit = str(randint(0,1))
		personalityValueString += digit
	return int(personalityValueString)

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
	if n > 100:
		n = 100
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
	genderRatio = pokemonGenderRatio[pokemon]
	if genderRatio[0] == 0:
		if genderRatio[1] == 0:
			return 'Genderless'
		else:
			return 'Female'
	elif genderRatio[1] == 0:
		return 'Male'
	else:
		totalParts = genderRatio[0] + genderRatio[1]
		random = randint(1,totalParts)
		if random <= genderRatio[0]:
			return 'Male'
		else:
			return 'Female'

def getNature(pokemon):
	return random.sample(allNaturesList,1)[0]

def getAbility(pokemon):
	abilityList = pokemonAbilities[pokemon]
	if abilityList[1] == 'None':
		return abilityList[0]
	else:
		random = randint(0,1)
		return abilityList[random]

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

def getPokemonSprite(id):
	return pokemonSprites[id]