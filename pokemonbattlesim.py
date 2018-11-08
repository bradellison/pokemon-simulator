from random import randint
from operator import add
import operator
import time

bulbasaurBaseStats = [45,49,49,65,65,45]
ivysaurBaseStats = [60,62,63,80,80,60]
venusaurBaseStats = [80,82,83,100,100,80]
charmanderBaseStats = [39,52,43,60,50,65]
charmeleonBaseStats = [58,64,58,80,65,80]
charizardBaseStats = [78,84,78,109,85,100]
squirtleBaseStats = [44,48,65,50,64,43]
wartortleBaseStats = [59,63,80,65,80,58]
blastoiseBaseStats = [79,83,100,85,105,78]

pokemonBaseStatListToDict = {'HP':0,'Atk':1,'Def':2,'SpAtk':3,'SpDef':4,'Spd':5,'Accuracy':6}
pokemonBaseStatDictToList = {0:'HP',1:'Atk',2:'Def',3:'SpAtk',4:'SpDef',5:'Spd',6:'Accuracy'}

effectivenessScale = {0.25:'it was not very effective and',0.5:'it was not very effective and',1:'',2:'it was super-effective and',4:'it was super-effective and'}

myPokemonCurrentStatStage = [0,0,0,0,0,0,0]
enemyPokemonCurrentStatStage = [0,0,0,0,0,0,0]

pokemonCurrentStatStages = {'My Pokemon':myPokemonCurrentStatStage, 'Enemy Pokemon':enemyPokemonCurrentStatStage}

pokemonStatStageToMult = {-6:0.25,-5:0.28,-4:0.33,-3:0.40,-2:0.50,-1:0.66,0:1,1:1.5,2:2,3:2.5,4:3,5:3.5,6:4}

nonVolatileStatusNumberToType = {0:'Nothing',1:'Burned',2:'Paralyzed',3:'Sleep',4:'Frozen',5:'Poisoned',6:'Toxic'}

bulbasaurType = {'Type One':'Grass','Type Two':'Poison'}
ivysaurType = {'Type One':'Grass','Type Two':'Poison'}
venusaurType = {'Type One':'Grass','Type Two':'Poison'}
charmanderType = {'Type One':'Fire','Type Two':'Null'}
charmeleonType = {'Type One':'Fire','Type Two':'Null'}
charizardType = {'Type One':'Fire','Type Two':'Flying'}
squirtleType = {'Type One':'Water','Type Two':'Null'}
wartortleType = {'Type One':'Water','Type Two':'Null'}
blastoiseType = {'Type One':'Water','Type Two':'Null'}

bulbasaurMoves = {'Move One':'Tackle', 'Move Two':'Growl'}
ivysaurMoves = {'Move One':'Tackle', 'Move Two':'Growl', 'Move Three':'Vine Whip'}
venusaurMoves = {'Move One':'Tackle', 'Move Two':'Growl', 'Move Three':'Vine Whip', 'Move Four':'Petal Blizzard'}
charmanderMoves = {'Move One':'Scratch', 'Move Two':'Growl'}
charmeleonMoves = {'Move One':'Scratch', 'Move Two':'Growl', 'Move Three':'Ember'}
charizardMoves = {'Move One':'Scratch', 'Move Two':'Growl', 'Move Three':'Ember', 'Move Four':'Flamethrower'}
squirtleMoves = {'Move One':'Tackle', 'Move Two':'Tail Whip'}
wartortleMoves = {'Move One':'Tackle', 'Move Two':'Tail Whip', 'Move Three':'Bubble'}
blastoiseMoves = {'Move One':'Tackle', 'Move Two':'Tail Whip', 'Move Three':'Bubble', 'Move Four':'Hydro Pump'}

pokemonStats = {'Bulbasaur':bulbasaurBaseStats,'Ivysaur':ivysaurBaseStats,'Venusaur':venusaurBaseStats,'Charmander':charmanderBaseStats,'Charmeleon':charmeleonBaseStats,'Charizard':charizardBaseStats,'Squirtle':squirtleBaseStats,'Wartortle':wartortleBaseStats,'Blastoise':blastoiseBaseStats}
pokemonTypes = {'Bulbasaur':bulbasaurType,'Ivysaur':ivysaurType,'Venusaur':venusaurType,'Charmander':charmanderType,'Charmeleon':charmeleonType,'Charizard':charizardType,'Squirtle':squirtleType,'Wartortle':wartortleType,'Blastoise':blastoiseType}
pokemonMoves = {'Bulbasaur':bulbasaurMoves,'Ivysaur':ivysaurMoves,'Venusaur':venusaurMoves,'Charmander':charmanderMoves,'Charmeleon':charmeleonMoves,'Charizard':charizardMoves,'Squirtle':squirtleMoves,'Wartortle':wartortleMoves,'Blastoise':blastoiseMoves}
pokemonWild = ['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise']

tackleInfo = {'Base Damage':40, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
scratchInfo = {'Base Damage':40, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
emberInfo = {'Base Damage':45, 'Move Type':'Fire', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'Yes', 'Priority':0}
bubbleInfo = {'Base Damage':35, 'Move Type':'Water', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'No', 'Priority':0}
vineWhipInfo = {'Base Damage':40, 'Move Type':'Grass', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
growlInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':90, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
defenseCurlInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
tailWhipInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
flamethrowerInfo = {'Base Damage':90, 'Move Type':'Fire', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'No', 'Priority':0}
hydroPumpInfo = {'Base Damage':110, 'Move Type':'Water', 'Move Accuracy':80, 'Move Variety':'Special', 'Added Effect':'No', 'Priority':0}
petalBlizzardInfo = {'Base Damage':90, 'Move Type':'Grass', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}

growlExtraInfo = {'Stat Change':'Enemy', 'Status Change':'No'}
tailWhipExtraInfo = {'Stat Change':'Enemy', 'Status Change':'No'}
emberExtraInfo = {'Stat Change':'No', 'Status Change':'Yes'}
defenseCurlExtraInfo = {'Stat Change':'Self', 'Status Change':'No'}

growlStatChangeInfo = {'HP':0,'Atk':-1,'Def':0,'SpAtk':0,'SpDef':0,'Spd':0, 'Accuracy':0}
defenseCurlStatChangeInfo = {'HP':0,'Atk':0,'Def':1,'SpAtk':0,'SpDef':0,'Spd':0, 'Accuracy':0}
tailWhipStatChangeInfo = {'HP':0,'Atk':0,'Def':-1,'SpAtk':0,'SpDef':0,'Spd':0, 'Accuracy':0}

emberStatusChangeInfo = {'Type':3,'Chance':100}

normalEffect = {'Normal':1, 'Water':1, 'Grass':1, 'Fire':1, 'Poison':1, 'Flying':1, 'Null':1}
grassEffect = {'Normal':1, 'Water':2, 'Grass':1, 'Fire':0.5, 'Poison':1, 'Flying':1, 'Null':1}
fireEffect = {'Normal':1, 'Water':0.5, 'Grass':2, 'Fire':1, 'Poison':1, 'Flying':1, 'Null':1}
waterEffect = {'Normal':1, 'Water':1, 'Grass':0.5, 'Fire':2, 'Poison':1, 'Flying':1, 'Null':1}

allType = {'Normal':normalEffect, 'Grass':grassEffect, 'Fire':fireEffect, 'Water':waterEffect}

moveInfo = {'Tackle':tackleInfo,'Ember':emberInfo,'Bubble':bubbleInfo,'Vine Whip':vineWhipInfo,'Growl':growlInfo,'Defense Curl':defenseCurlInfo,'Scratch':scratchInfo,'Tail Whip':tailWhipInfo,'Flamethrower':flamethrowerInfo,'Hydro Pump':hydroPumpInfo,'Petal Blizzard':petalBlizzardInfo}
moveExtraInfo = {'Ember':emberExtraInfo,'Growl':growlExtraInfo,'Defense Curl':defenseCurlExtraInfo,'Tail Whip':tailWhipExtraInfo}
moveStatChangeInfo = {'Growl':growlStatChangeInfo,'Defense Curl':defenseCurlStatChangeInfo,'Tail Whip':tailWhipStatChangeInfo}
moveStatusChangeInfo = {'Ember':emberStatusChangeInfo}


def getRandomPokemon():
	pokemonSetSize = len(pokemonWild)
	pokemonNumber = randint(1,pokemonSetSize) - 1
	return pokemonWild[pokemonNumber]

def getRandomLevel():
	pokemonLevel = randint(1,100)
	return pokemonLevel

def getMoveOption(pokemon,moveNumber):
	pokemonMoveset = pokemonMoves[pokemon]
	if moveNumber == 0:
		return pokemonMoveset['Move One']
	if moveNumber == 1:
		return pokemonMoveset['Move Two']
	if moveNumber == 2:
		return pokemonMoveset['Move Three']
	if moveNumber == 3:
		return pokemonMoveset['Move Four']

def getRandomIV():
	IV = []
	for _ in range(6):
		x = randint(1,31)
		IV.append(x)
	return IV

def getMoveSet(pokemon):
	moveSet = []
	pokemonMovesetSize = len(pokemonMoves[pokemon])
	for i in range(pokemonMovesetSize):
		moveI = getMoveOption(pokemon,i)
		moveSet.append(moveI)
	return moveSet

def getRandomMoveFromSet(pokemon):
	moveSet = getMoveSet(pokemon)
	movesetSize = len(moveSet)
	moveNumber = randint(1,movesetSize) - 1
	return moveSet[moveNumber]

def getPokemonHPMult(pokemon):
	pokemonCurrentStatStage = statStage
	pokemonHPStage = pokemonCurrentStatStage[0]
	if pokemonHPStage > 6:
		pokemonHPStage = 6
	if pokemonHPStage < -6:
		pokemonHPStage = -6
	pokemonHPMult = pokemonStatStageToMult[pokemonHPStage]
	return pokemonHPMult

def getPokemonAtkMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonAtkStage = pokemonCurrentStatStage[1]
	if pokemonAtkStage > 6:
		pokemonAtkStage = 6
	if pokemonAtkStage < -6:
		pokemonAtkStage = -6
	pokemonAtkMult = pokemonStatStageToMult[pokemonAtkStage]
	return pokemonAtkMult

def getPokemonDefMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonDefStage = pokemonCurrentStatStage[2]
	if pokemonDefStage > 6:
		pokemonDefStage = 6
	if pokemonDefStage < -6:
		pokemonDefStage = -6
	pokemonDefMult = pokemonStatStageToMult[pokemonDefStage]
	return pokemonDefMult

def getPokemonSpAtkMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonSpAtkStage = pokemonCurrentStatStage[3]
	if pokemonSpAtkStage > 6:
		pokemonSpAtkStage = 6
	if pokemonSpAtkStage < -6:
		pokemonSpAtkStage = -6
	pokemonSpAtkMult = pokemonStatStageToMult[pokemonSpAtkStage]
	return pokemonSpAtkMult

def getPokemonSpDefMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonSpDefStage = pokemonCurrentStatStage[4]
	if pokemonSpDefStage > 6:
		pokemonSpDefStage = 6
	if pokemonSpDefStage < -6:
		pokemonSpDefStage = -6
	pokemonSpDefMult = pokemonStatStageToMult[pokemonSpDefStage]
	return pokemonSpDefMult

def getPokemonSpdMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonSpdStage = pokemonCurrentStatStage[5]
	if pokemonSpdStage > 6:
		pokemonSpdStage = 6
	if pokemonSpdStage < -6:
		pokemonSpdStage = -6
	pokemonSpdMult = pokemonStatStageToMult[pokemonSpdStage]
	return pokemonSpdMult

def gethpStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[0]
	return int(((2 * myPokemonStats[0] + iv) * level / 100 ) + level + 10)

def getAtkStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[1]
	pokemonAtkMult = getPokemonAtkMult(statStage)
	return pokemonAtkMult * (((2 * myPokemonStats[1] + iv) * level / 100 ) + 5)

def getDefStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[2]
	pokemonDefMult = getPokemonDefMult(statStage)
	return pokemonDefMult * (((2 * myPokemonStats[2] + iv) * level / 100 ) + 5)

def getSpAtkStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[3]
	pokemonSpAtkMult = getPokemonSpAtkMult(statStage)
	return pokemonSpAtkMult * (((2 * myPokemonStats[3] + iv) * level / 100 ) + 5)

def getSpDefStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[4]
	pokemonSpDefMult = getPokemonSpDefMult(statStage)
	return pokemonSpDefMult * (((2 * myPokemonStats[4] + iv) * level / 100 ) + 5)

def getSpdStat(pokemon,level,iv,statStage,status):
	myPokemonStats = pokemonStats[pokemon]
	statusType = getStatusType(status)
	if statusType == 'Paralyzed':
		statusMult = 0.5
	else:
		statusMult = 1
	iv = iv[5]
	pokemonSpdMult = getPokemonSpdMult(statStage)
	return pokemonSpdMult * statusMult * (((2 * myPokemonStats[5] + iv) * level / 100 ) + 5)

def getPokemonStatStage(pokemon):
	pokemonToApplyStatChange = pokemonCurrentStatStages[pokemon]
	return pokemonToApplyStatChange

def getPokemonTypeOne(pokemon):
	pokemonType = pokemonTypes[pokemon]
	return pokemonType['Type One']

def getPokemonTypeTwo(pokemon):
	pokemonType = pokemonTypes[pokemon]
	return pokemonType['Type Two']

def getMoveBaseDamage(move):
	moveBaseDam = moveInfo[move]
	return moveBaseDam['Base Damage']

def getMoveType(move):
	moveType = moveInfo[move]
	return moveType['Move Type']

def getMoveVariety(move):
	moveVariety = moveInfo[move]
	return moveVariety['Move Variety']

def getMoveExtra(move):
	moveExtra = moveInfo[move]
	return moveExtra['Added Effect'] 

def getMoveExtraForm(move):
	moveExtraForm = moveExtraInfo[move]
	return moveExtraForm['Stat Change']

def getStatusChange(move):
	statusChange = moveExtraInfo[move]
	return statusChange['Status Change']

def getStatusChangeType(move):
	statusChangeType = moveStatusChangeInfo[move]
	return statusChangeType['Type']

def getStatusChangeChance(move):
	statusChangeChance = moveStatusChangeInfo[move]
	return statusChangeChance['Chance']

def getMoveStatChangeInfo(move,stat):
	moveStatChange = moveStatChangeInfo[move]
	return moveStatChange[stat]

def getMoveAccuracy(move):
	moveAccuracy = moveInfo[move]
	return moveAccuracy['Move Accuracy']

def getMovePriority(move):
	movePriority = moveInfo[move]
	return movePriority['Priority']

def getEffectiveness(move,pokemon):
	moveType = getMoveType(move)
	pokemonTypeOne = getPokemonTypeOne(pokemon)
	pokemonTypeTwo = getPokemonTypeTwo(pokemon)
	moveType2 = allType[moveType]
	return moveType2[pokemonTypeOne] * moveType2[pokemonTypeTwo]

def getEffectivesnessWording(i):
	effectivenessWording = effectivenessScale[i]
	return effectivenessWording

def getStabBonus(move,pokemon):
	moveType = getMoveType(move)
	pokemonTypeOne = getPokemonTypeOne(pokemon)
	pokemonTypeTwo = getPokemonTypeTwo(pokemon)
	if moveType == pokemonTypeOne:
		return 1.5
	if moveType == pokemonTypeTwo:
		return 1.5
	else:
		return 1 

def getHitOrMiss(move):
	accuracy = getMoveAccuracy(move)
	randomOf100 = randint(1,100)
	if randomOf100 <= accuracy:
		return 'Hit'
	else:
		return 'Miss'

def getMoveDamage(move,atkPokemon,atkLevel,atkIV,atkStatStage,atkStatus,defPokemon,defLevel,defIV,defStatStage):
	moveBaseDamage = getMoveBaseDamage(move)
	effectiveness = getEffectiveness(move,defPokemon)
	stabBonus = getStabBonus(move,atkPokemon)
	moveVariety = getMoveVariety(move)
	statusType = getStatusType(atkStatus)
	if moveVariety == 'Physical':
		atkStat = getAtkStat(atkPokemon,atkLevel,atkIV,atkStatStage)
		defStat = getDefStat(defPokemon,defLevel,defIV,defStatStage)
		if statusType == 'Burned':
			statusMult = 0.5
		else:
			statusMult = 1
		moveDamage = int((((((2 * atkLevel / 5) + 2) * atkStat * moveBaseDamage / defStat) / 50 ) + 2) * stabBonus * effectiveness * statusMult * float(randint(0,15)+85)/100)
		return moveDamage	
	if moveVariety == 'Special':
		atkStat = getSpAtkStat(atkPokemon,atkLevel,atkIV,atkStatStage)
		defStat = getSpDefStat(defPokemon,defLevel,defIV,defStatStage)
		moveDamage = int((((((2 * atkLevel / 5) + 2) * atkStat * moveBaseDamage / defStat) / 50 ) + 2) * stabBonus * effectiveness * float(randint(0,15)+85)/100)
		return moveDamage
	if moveVariety == 'Support':
		moveExtraForm = getMoveExtraForm(move)
		if moveExtraForm == 'Self':
			return 0
		if moveExtraForm == 'Enemy':
			return 0

def getPokemonBaseStatDictToList(i):
	dictToList = pokemonBaseStatDictToList[i]
	return dictToList

def getStatChange(move):
	statChange=[]
	for i in range(0,7):
		stat = getPokemonBaseStatDictToList(i)
		moveStatChange = getMoveStatChangeInfo(move,stat)
		statChange.append(moveStatChange)
	return statChange
#
# def getStatChangeWording(i):
#	todo

def getStatusType(i):
	StatusType = nonVolatileStatusNumberToType[i]
	return StatusType

def getTurnOrder(myPokemon,myLevel,myIV,myStatStage,myStatus,enemyPokemon,enemyLevel,enemyIV,enemyStatStage,enemyStatus):
	mySpd = getSpdStat(myPokemon,myLevel,myIV,myStatStage,myStatus)
	enemySpd = getSpdStat(enemyPokemon,enemyLevel,enemyIV,enemyStatStage,enemyStatus)
	if mySpd > enemySpd:
		return 'myPokemonFirst'
	if mySpd < enemySpd:
		return 'enemyPokemonFirst'
	if mySpd == enemySpd:
		x = randint(0,1)
		if x == 0:
			return 'myPokemonFirst'
		if x == 1:
			return 'enemyPokemonFirst'

def getPokemonMove(move,myPokemon,myLevel,enemyPokemon,enemyLevel):
	moveDamage = getMoveDamage(move,myPokemon,myLevel,enemyPokemon,enemyLevel)
	effectiveness = getEffectiveness(move,enemyPokemon)
	addedEffect = getMoveExtra(move)

def startMyTurn(move,myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount):
	moveDamage = getMoveDamage(move,myPokemon,myLevel,myIV,myStatStage,myStatus,enemyPokemon,enemyLevel,enemyIV,enemyStatStage)
	myStatusType = getStatusType(myStatus)
	enemyStatusType = getStatusType(enemyStatus)
	enemyMaxHP = gethpStat(enemyPokemon,enemyLevel,enemyIV,'Enemy Pokemon')
	myMaxHP = gethpStat(myPokemon,myLevel,myIV,'My Pokemon')
	hitOrMiss = getHitOrMiss(move)
	moveVariety = getMoveVariety(move)
	effectiveness = getEffectiveness(move,enemyPokemon)
	effectivenessWording = getEffectivesnessWording(effectiveness)
	if myStatus != 'Nothing':
		if myStatusType == 'Paralyzed':
			print(myPokemon, 'is paralyzed and may not be able to move!')
			i = randint(1,4)
			if i == 1:
				print(myPokemon, 'couldn\'t move!')
				hpList = [myHP,enemyHP]
				statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]	
				outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
				return outcomeInfo
		if myStatusType == 'Sleep':
			print(myPokemon, 'is sleeping!')
			myStatusCount = myStatusCount - 1
			if myStatusCount > 0:
				hpList = [myHP,enemyHP]
				statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]	
				outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
				return outcomeInfo
			myStatus = 0
			myStatusType = getStatusType(myStatus)
			print(myPokemon, 'woke up!')
		if myStatusType == 'Frozen':
			i = randint(1,5)
			if i == 1:
				myStatus = 0
				myStatusType = getStatusType(myStatus)
			else:
				print(myPokemon, 'is frozen and couldn\'t move!')
				hpList = [myHP,enemyHP]
				statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]	
				outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
				return outcomeInfo			
	if hitOrMiss == 'Miss':
		print(myPokemon, 'used', move, 'but it missed!')
		hpList = [myHP,enemyHP]
		statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]	
		outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
		return outcomeInfo
	if moveVariety == 'Support':
		moveExtraForm = getMoveExtraForm(move)
		if moveExtraForm == 'Enemy':
			statChange = getStatChange(move)
			enemyStatStage = list(map(add, enemyStatStage, statChange))
			print(myPokemon, 'used', move, 'against the wild', enemyPokemon, 'and it\'s stats changed by', statChange, '. They are now', enemyStatStage, '.')
		if moveExtraForm == 'Self':
			statChange = getStatChange(move)
			myStatStage = list(map(add, myStatStage, statChange))
			print('Your', myPokemon, 'used', move, 'and it\'s stats changed by', statChange, '. They are now', myStatStage, '.')
		hpList = [myHP,enemyHP]
		statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]
		outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
		return outcomeInfo
	enemyHP = enemyHP - moveDamage
	if enemyHP < 0:
		enemyHP = 0
	print(myPokemon, 'used', move, 'against the wild', enemyPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', enemyPokemon, 'has', enemyHP, '/', enemyMaxHP, 'HP remaining!')
	moveExtra = getMoveExtra(move)
	if moveExtra == 'Yes':
		statusChange = getStatusChange(move)
		if statusChange == 'Yes':
			if enemyStatus == 0:
				statusChangeType = getStatusChangeType(move)
				statusChangeChance = getStatusChangeChance(move)
				x = randint(1,100)
				if x <= statusChangeChance:
					enemyStatus = statusChangeType
					statusType = getStatusType(enemyStatus)
					print(enemyPokemon, 'was', statusType + '!')
				if statusChangeType == 3:
					x = randint(1,3)	
					enemyStatusCount = x
	myStatusType = getStatusType(myStatus)
	if myStatusType != 'Nothing':
		if myStatusType == 'Burned':
			burnDamage = int(myMaxHP / 16)
			myHP = (myHP - burnDamage)
			print(myPokemon, 'took', burnDamage, 'HP damage due to it\'s burn! It has', myHP, '/', myMaxHP, 'HP remaining!')
		if myStatusType == 'Poisoned':
			poisonDamage = int(myMaxHP / 8)
			myHP = (myHP - poisonDamage)
			print(myPokemon, 'took', poisonDamage, 'HP damage due to being poisoned! It has', myHP, '/', myMaxHP, 'HP remaining!')
		if myStatusType == 'Toxic':
			myStatusCount = myStatusCount + 1
			toxicDamage = int(myMaxHP * myStatusCount / 16)
			myHP = myHP - toxicDamage
			print(myPokemon, 'took', toxicDamage, 'HP damage due to being badly poisoned! It has', myHP, '/', myMaxHP, 'HP remaining!')
	hpList = [myHP,enemyHP]
	statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]
	outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
	return outcomeInfo

def startEnemyTurn(move,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount,myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount):
	moveDamage = getMoveDamage(move,enemyPokemon,enemyLevel,enemyIV,enemyStatStage,enemyStatus,myPokemon,myLevel,myIV,myStatStage)
	myStatusType = getStatusType(myStatus)
	enemyStatusType = getStatusType(enemyStatus)
	myMaxHP = gethpStat(myPokemon,myLevel,myIV,'My Pokemon')
	enemyMaxHP = gethpStat(enemyPokemon,enemyLevel,enemyIV,'Enemy Pokemon')
	hitOrMiss = getHitOrMiss(move)
	moveVariety = getMoveVariety(move)
	moveExtra = getMoveExtra(move)
	effectiveness = getEffectiveness(move,myPokemon)
	effectivenessWording = getEffectivesnessWording(effectiveness)
	if enemyStatusType != 'Nothing':
		if enemyStatusType == 'Paralyzed':
			print('The wild', enemyPokemon, 'is paralyzed and may not be able to move!')
			i = randint(1,4)
			if i == 1:
				print(enemyPokemon, 'couldn\'t move!')
				hpList = [myHP,enemyHP]
				statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]	
				outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
				return outcomeInfo
		if enemyStatusType == 'Sleep':
			print('The wild', enemyPokemon, 'is sleeping!')
			enemyStatusCount = enemyStatusCount - 1
			if enemyStatusCount > 0:
				hpList = [myHP,enemyHP]
				statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]	
				outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
				return outcomeInfo
			enemyStatus = 0
			enemyStatusType = getStatusType(enemyStatus)
			print('The wild', enemyPokemon, 'woke up!')
		if enemyStatusType == 'Frozen':
			i = randint(1,5)
			if i == 1:
				enemyStatus = 0
				enemyStatusType = getStatusType(enemyStatus)
			else:
				print('The wild', enemyPokemon, 'is frozen and couldn\'t move!')
				hpList = [myHP,enemyHP]
				statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]	
				outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
				return outcomeInfo	
	if hitOrMiss == 'Miss':
		print(enemyPokemon, 'used', move, 'but it missed!')
		hpList = [myHP,enemyHP]
		statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]
		outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
		return outcomeInfo
	if moveVariety == 'Support':
		moveExtraForm = getMoveExtraForm(move)
		if moveExtraForm == 'Self':
			statChange = getStatChange(move)
			enemyStatStage = list(map(add, enemyStatStage, statChange))
			print('The wild', enemyPokemon, 'used', move, 'and it\'s stats changed by', statChange, '. They are now', enemyStatStage, '.')
		if moveExtraForm == 'Enemy':
			statChange = getStatChange(move)
			myStatStage = list(map(add, myStatStage, statChange))
			print('The wild', enemyPokemon, 'used', move, 'against your', myPokemon, 'and it\'s stats changed by', statChange, '. They are now', myStatStage, '.')
		hpList = [myHP,enemyHP]
		statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]
		outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
		return outcomeInfo
	myHP = myHP - moveDamage
	if myHP < 0:
		myHP = 0
	print('The wild', enemyPokemon, 'used', move, 'against', myPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', myPokemon, 'has', myHP, '/', myMaxHP, 'HP remaining!')
	enemyStatusType = getStatusType(enemyStatus)
	if enemyStatusType != 'Nothing':
		if enemyStatusType == 'Burned':
			burnDamage = int(enemyMaxHP / 16)
			enemyHP = (enemyHP - burnDamage)
			print('The wild', enemyPokemon, 'took', burnDamage, 'HP damage due to it\'s burn! It has', enemyHP, '/', enemyMaxHP, 'HP remaining!')
		if enemyStatusType == 'Poisoned':
			poisonDamage = int(enemyMaxHP / 8)
			enemyHP = (enemyHP - poisonDamage)
			print('The wild', enemyPokemon, 'took', poisonDamage, 'HP damage due to being poisoned! It has', enemyHP, '/', enemyMaxHP, 'HP remaining!')
		if enemyStatusType == 'Toxic':
			enemyStatusCount = enemyStatusCount + 1
			toxicDamage = int(enemyMaxHP * meneyStatusCount / 16)
			enemyHP = enemyHP - toxicDamage
			print('The wild', enemyPokemon, 'took', toxicDamage, 'HP damage due to being badly poisoned! It has', enemyHP, '/', enemyMaxHP, 'HP remaining!')
	hpList = [myHP,enemyHP]
	statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]
	outcomeInfo = hpList + myStatStage + enemyStatStage + statusList
	return outcomeInfo

def getMoveInput(myPokemon):
	movesetSize = len(getMoveSet(myPokemon))
	while True:
		try:
			moveInput = input('-- ')
			if moveInput in getMoveSet(myPokemon):
				return moveInput
				break			
			moveInput
			if int(moveInput) <= movesetSize and int(moveInput) > 0:
				moveset = getMoveSet(myPokemon)
				return moveset[int(moveInput)-1]
				break	
			print("Please choose a move from the list below!")
		except ValueError:
			print("Please choose a move from the list.")

def getChoiceInput():
	while True:
		try:
			choiceInput = input('-- ')
			if choiceInput == 'Fight':
				return choiceInput
			if choiceInput == 'Bag':
				return choiceInput
			if choiceInput == 'Pokemon':
				return choiceInput
			if choiceInput == 'Run':
				return choiceInput						
			if int(choiceInput) == 1:
				choiceInput = 'Fight'
				return choiceInput
			if int(choiceInput) == 2:
				choiceInput = 'Bag'
				return choiceInput
			if int(choiceInput) == 3:
				choiceInput = 'Pokemon'
				return choiceInput
			if int(choiceInput) == 4:
				choiceInput = 'Run'
				return choiceInput
			print("Please choose a move from the list below!")
		except ValueError:
			print("Please choose a move from the list.")

def startRound(myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount):
	print('What will you do?')
	print('Fight - Bag - Pokemon - Run')
	choiceInput = getChoiceInput()
	if choiceInput == 'Fight':
		run = [0]
		print('\nWhat will', myPokemon, 'do?')
		print(getMoveSet(myPokemon))
		myMove = getMoveInput(myPokemon)
		print('')
		enemyMove = getRandomMoveFromSet(enemyPokemon)
		turnOrder = getTurnOrder(myPokemon,myLevel,myIV,myStatStage,myStatus,enemyPokemon,enemyLevel,enemyIV,enemyStatStage,enemyStatus)
		if turnOrder == 'myPokemonFirst':
			turnOutcomeInfo = startMyTurn(myMove,myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount)
			myHP = turnOutcomeInfo[0]
			enemyHP = turnOutcomeInfo[1]
			if enemyHP == 0 or myHP == 0:
				roundOutcomeInfo = turnOutcomeInfo + run
				return roundOutcomeInfo
			turnOutcomeInfo = startEnemyTurn(enemyMove,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount,myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount)
			roundOutcomeInfo = turnOutcomeInfo + run
			return roundOutcomeInfo
		if turnOrder == 'enemyPokemonFirst':
			turnOutcomeInfo = startEnemyTurn(enemyMove,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount,myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount)
			myHP = turnOutcomeInfo[0]
			enemyHP = turnOutcomeInfo[1]
			if myHP == 0 or enemyHP == 0:
				roundOutcomeInfo = turnOutcomeInfo + run
				return roundOutcomeInfo
			turnOutcomeInfo = startMyTurn(myMove,myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount)
			roundOutcomeInfo = turnOutcomeInfo + run
			return roundOutcomeInfo
	if choiceInput == 'Run':
		run = [1]
		hpList = [myHP,enemyHP]
		statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]
		roundOutcomeInfo = hpList + myStatStage + enemyStatStage + statusList + run
		return roundOutcomeInfo
	if choiceInput == 'Bag':
		print('Nothing in your bag!')
		run = [0]
		enemyMove = getRandomMoveFromSet(enemyPokemon)
		turnOutcomeInfo = startEnemyTurn(enemyMove,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount,myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount)
		hpList = [myHP,enemyHP]
		statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]
		roundOutcomeInfo = hpList + myStatStage + enemyStatStage + statusList + run
		return roundOutcomeInfo
	if choiceInput == 'Pokemon':
		print('No other Pokemon!')
		run = [0]
		enemyMove = getRandomMoveFromSet(enemyPokemon)
		turnOutcomeInfo = startEnemyTurn(enemyMove,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount,myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount)
		hpList = [myHP,enemyHP]
		statusList = [myStatus,myStatusCount,enemyStatus,enemyStatusCount]
		roundOutcomeInfo = hpList + myStatStage + enemyStatStage + statusList + run
		return roundOutcomeInfo

def startBattle(myPokemon,myLevel,myIV,myStatus,enemyPokemon,enemyLevel):
	print('A wild Level', enemyLevel, enemyPokemon, 'appeared! Go', myPokemon, '!')
	enemyIV = getRandomIV()
	enemyStatus = 0
	myStatusCount = 0
	enemyStatusCount = 0
	myHP = gethpStat(myPokemon,myLevel,myIV,'My Pokemon')
	enemyHP = gethpStat(enemyPokemon,enemyLevel,enemyIV,'Enemy Pokemon')
	myStatStage = getPokemonStatStage('My Pokemon')
	enemyStatStage = getPokemonStatStage('Enemy Pokemon')
	while myHP > 0 and enemyHP > 0:
		roundOutcomeInfo = startRound(myPokemon,myLevel,myHP,myIV,myStatStage,myStatus,myStatusCount,enemyPokemon,enemyLevel,enemyHP,enemyIV,enemyStatStage,enemyStatus,enemyStatusCount)
		myHP = roundOutcomeInfo[0]
		enemyHP = roundOutcomeInfo[1]
		myStatStage = list(operator.itemgetter(2,3,4,5,6,7,8)(roundOutcomeInfo))
		enemyStatStage = list(operator.itemgetter(9,10,11,12,13,14,15)(roundOutcomeInfo))
		myStatus = roundOutcomeInfo[16]
		myStatusCount = roundOutcomeInfo[17]
		enemyStatus = roundOutcomeInfo[18]
		enemyStatusCount=roundOutcomeInfo[19]
		runLast=roundOutcomeInfo[20]
		if int(runLast) > 0:
			print('You got away safely!')
			return 1
	if myHP == 0:
		print(myPokemon, 'fainted! You lose!')
	if myHP > 0:
		print('The wild', enemyPokemon, 'fainted! You win!')

def startGame():
	print('Professor Oak: \n- Hello! Welcome to the wonderful world of Pokemon. My name is Professor Oak, it\'s great to meet you. What was your name again?')
	name = input(': ')
	print('Professor Oak: \n- Ah yes,', name + '. How could I forget?')
	input()
	print('- Woah now! You don\'t want to go into that long grass without a Pokemon! Come with me!')
	input()
	print('Gary: \n- Wahwahwah, I want one first!')
	input()
	print('Professor Oak: \n- Be patient, Gary!', name, 'is our guest. Go ahead and choose one of the balls in from of you. Will you choose:')
	print('Bulbasaur - the grass Pokemon. \nCharmander - the fire Pokemon. \nSquirtle - the water Pokemon.')
	myPokemon = input('Choose: ')
	if myPokemon == 'Bulbasaur':
		enemyPokemon = 'Charmander'	
	if myPokemon == 'Charmander':
		enemyPokemon = 'Squirtle'
	if myPokemon == 'Squirtle':
		enemyPokemon = 'Bulbasaur'
	myIV = getRandomIV()
	myStatus = 0
	myLevel = 5
	enemyLevel = 5
	print('Gary: \n Fine, I choose', enemyPokemon + '! Let\'s fight!')
	input()
	startBattle(myPokemon,myLevel,myIV,myStatus,enemyPokemon,enemyLevel)

def chooseGameplay():
	print('> To begin the game as normal, type 1\n> For a random battle (both yours and the enemy Pokemon and levels random), type 2\n> To fight a level 100 Venusaur with a Level 100 Charizard, type 3\n> To fight a level 100 random pokemon with a random level 100 pokemon, type 4')
	x = input()
	if x == '1':
		startGame()
	if x == '2':
		myPokemon = getRandomPokemon()
		myLevel = getRandomLevel()
		enemyPokemon = getRandomPokemon()
		enemyLevel = getRandomLevel()
		myIV = getRandomIV()
		myStatus = 0
		print('Your', myPokemon, 'is level', myLevel)
		startBattle(myPokemon,myLevel,myIV,myStatus,enemyPokemon,enemyLevel)
	if x == '3':
		myPokemon = 'Charizard'
		myLevel = 100
		enemyPokemon = 'Venusaur'
		enemyLevel = 100
		myIV = getRandomIV()
		myStatus = 0
		print('Your', myPokemon, 'is level', myLevel)
		startBattle(myPokemon,myLevel,myIV,myStatus,enemyPokemon,enemyLevel)
	if x == '4':
		myPokemon = getRandomPokemon()
		myLevel = 100
		enemyPokemon = getRandomPokemon()
		enemyLevel = 100
		myIV = getRandomIV()
		myStatus = 0
		print('Your', myPokemon, 'is level', myLevel)
		startBattle(myPokemon,myLevel,myIV,myStatus,enemyPokemon,enemyLevel)

chooseGameplay()

myPokemon='Charizard'
enemyPokemon='Venusaur'
myLevel=100
enemyLevel=100
myIV = [31, 31, 31, 31, 31, 31]
#enemyPokemon = getRandomPokemon()
#enemyLevel = getRandomLevel()




#startBattle(myPokemon,myLevel,myIV,enemyPokemon,enemyLevel)
