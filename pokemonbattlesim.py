from random import randint
from operator import add

venusaurBaseStats = [80,82,83,100,100,80]
charizardBaseStats = [78,84,78,109,85,100]
blastoiseBaseStats = [79,83,100,85,105,78]

pokemonBaseStatListToDict = {'HP':0,'Atk':1,'Def':2,'SpAtk':3,'SpDef':4,'Spd':5}
pokemonBaseStatDictToList = {0:'HP',1:'Atk',2:'Def',3:'SpAtk',4:'SpDef',5:'Spd'}

pokemonOneCurrentStatStage = [0,2,0,0,0,0]
pokemonTwoCurrentStatStage = [0,5,0,0,0,0]

pokemonCurrentStatStages = {'My Pokemon':pokemonOneCurrentStatStage, 'Enemy Pokemon':pokemonTwoCurrentStatStage}

pokemonStatStageToMult = {-6:0.25,-5:0.28,-4:0.33,-4:0.40,-2:0.50,-1:0.66,0:1,1:1.5,2:2,3:2.5,4:3,5:3.5,6:4}

venusaurType = {'Type One':'Grass','Type Two':'Poison'}
charizardType = {'Type One':'Fire','Type Two':'Flying'}
blastoiseType = {'Type One':'Water','Type Two':'Null'}

venusaurMoves = {'Move One':'Tackle', 'Move Two':'Vine Whip', 'Move Three':'Growl'}
charizardMoves = {'Move One':'Tackle', 'Move Two':'Ember', 'Move Three':'Growl'}
blastoiseMoves = {'Move One':'Tackle', 'Move Two':'Bubble', 'Move Three':'Defense Curl'}

pokemonStats = {'Venusaur':venusaurBaseStats, 'Charizard':charizardBaseStats, 'Blastoise':blastoiseBaseStats}
pokemonTypes = {'Venusaur':venusaurType, 'Charizard':charizardType, 'Blastoise':blastoiseType}
pokemonMoves = {'Venusaur':venusaurMoves, 'Charizard':charizardMoves, 'Blastoise':blastoiseMoves}
pokemonWild = ['Venusaur','Charizard','Blastoise']

tackleInfo = {'Base Damage':50, 'Move Type':'Normal', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'No'}
emberInfo = {'Base Damage':45, 'Move Type':'Fire', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'Yes'}
bubbleInfo = {'Base Damage':35, 'Move Type':'Water', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'No'}
vineWhipInfo = {'Base Damage':40, 'Move Type':'Grass', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'No'}
growlInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':90, 'Move Variety':'Support', 'Added Effect':'Yes'}
defenseCurlInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'Yes'}

growlExtraInfo = {'Stat Change':'Enemy', 'Condition Change':'No'}
emberExtraInfo = {'Stat Change':'No', 'Condition Change':'Yes'}
defenseCurlExtraInfo = {'Stat Change':'Self', 'Condition Change':'No'}

growlStatChangeInfo = {'HP':0,'Atk':-1,'Def':0,'SpAtk':0,'SpDef':0,'Spd':0}
defenseCurlStatChangeInfo = {'HP':0,'Atk':0,'Def':1,'SpAtk':0,'SpDef':0,'Spd':0}
normalEffect = {'Normal':1, 'Water':1, 'Grass':1, 'Fire':1, 'Poison':1, 'Flying':1, 'Null':1}
grassEffect = {'Normal':1, 'Water':2, 'Grass':1, 'Fire':0.5, 'Poison':1, 'Flying':1, 'Null':1}
fireEffect = {'Normal':1, 'Water':0.5, 'Grass':2, 'Fire':1, 'Poison':1, 'Flying':1, 'Null':1}
waterEffect = {'Normal':1, 'Water':1, 'Grass':0.5, 'Fire':2, 'Poison':1, 'Flying':1, 'Null':1}

allType = {'Normal':normalEffect, 'Grass':grassEffect, 'Fire':fireEffect, 'Water':waterEffect}

moveInfo = {'Tackle':tackleInfo,'Ember':emberInfo,'Bubble':bubbleInfo,'Vine Whip':vineWhipInfo,'Growl':growlInfo,'Defense Curl':defenseCurlInfo}
moveExtraInfo = {'Ember':emberExtraInfo,'Growl':growlExtraInfo,'Defense Curl':defenseCurlExtraInfo}
moveStatChangeInfo = {'Growl':growlStatChangeInfo,'Defense Curl':defenseCurlStatChangeInfo}

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

def getPokemonHPMult():
	pokemonHPStage = pokemonOneCurrentStatStage[0]
	if pokemonHPStage > 6:
		pokemonHPStage = 6
	if pokemonHPStage < -6:
		pokemonHPStage = -6
	pokemonHPMult = pokemonStatStageToMult[pokemonHPStage]
	return pokemonHPMult
def getPokemonAtkMult():
	pokemonAtkStage = pokemonOneCurrentStatStage[1]
	if pokemonAtkStage > 6:
		pokemonAtkStage = 6
	if pokemonAtkStage < -6:
		pokemonAtkStage = -6
	pokemonAtkMult = pokemonStatStageToMult[pokemonAtkStage]
	return pokemonAtkMult
def getPokemonDefMult():
	pokemonDefStage = pokemonOneCurrentStatStage[2]
	if pokemonDefStage > 6:
		pokemonDefStage = 6
	if pokemonDefStage < -6:
		pokemonDefStage = -6
	pokemonDefMult = pokemonStatStageToMult[pokemonDefStage]
	return pokemonDefMult
def getPokemonSpAtkMult():
	pokemonSpAtkStage = pokemonOneCurrentStatStage[3]
	if pokemonSpAtkStage > 6:
		pokemonSpAtkStage = 6
	if pokemonSpAtkStage < -6:
		pokemonSpAtkStage = -6
	pokemonSpAtkMult = pokemonStatStageToMult[pokemonSpAtkStage]
	return pokemonSpAtkMult
def getPokemonSpDefMult():
	pokemonSpDefStage = pokemonOneCurrentStatStage[4]
	if pokemonSpDefStage > 6:
		pokemonSpDefStage = 6
	if pokemonSpDefStage < -6:
		pokemonSpDefStage = -6
	pokemonSpDefMult = pokemonStatStageToMult[pokemonSpDefStage]
	return pokemonSpDefMult
def getPokemonSpdMult():
	pokemonSpdStage = pokemonOneCurrentStatStage[5]
	if pokemonSpdStage > 6:
		pokemonSpdStage = 6
	if pokemonSpdStage < -6:
		pokemonSpdStage = -6
	pokemonSpdMult = pokemonStatStageToMult[pokemonSpdStage]
	return pokemonSpdMult

def gethpStat(pokemon,level):
	myPokemonStats = pokemonStats[pokemon]
	return ((2 * myPokemonStats[0]) * level / 100 ) + level + 10
def getAtkStat(pokemon,level):
	myPokemonStats = pokemonStats[pokemon]
	pokemonAtkMult = getPokemonAtkMult()
	return pokemonAtkMult * (((2 * myPokemonStats[1]) * level / 100 ) + 5)
def getDefStat(pokemon,level):
	myPokemonStats = pokemonStats[pokemon]
	pokemonDefMult = getPokemonDefMult()
	return pokemonDefMult * (((2 * myPokemonStats[2]) * level / 100 ) + 5)
def getSpAtkStat(pokemon,level):
	myPokemonStats = pokemonStats[pokemon]
	pokemonSpAtkMult = getPokemonSpAtkMult()
	return pokemonSpAtkMult * (((2 * myPokemonStats[3]) * level / 100 ) + 5)
def getSpDefStat(pokemon,level):
	myPokemonStats = pokemonStats[pokemon]
	pokemonSpDefMult = getPokemonSpDefMult()
	return pokemonSpDefMult * (((2 * myPokemonStats[4]) * level / 100 ) + 5)
def getSpdStat(pokemon,level):
	myPokemonStats = pokemonStats[pokemon]
	pokemonSpdMult = getPokemonSpdMult()
	return pokemonSpdMult * (((2 * myPokemonStats[5]) * level / 100 ) + 5)

def getPokemonToApplyStatChange(pokemon):
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
def getMoveStatChangeInfo(move,stat):
	moveStatChange = moveStatChangeInfo[move]
	return moveStatChange[stat]

def getMoveAccuracy(move):
	moveAccuracy = moveInfo[move]
	return moveAccuracy['Move Accuracy']
def getEffectiveness(move,pokemon):
	moveType = getMoveType(move)
	pokemonTypeOne = getPokemonTypeOne(pokemon)
	pokemonTypeTwo = getPokemonTypeTwo(pokemon)
	moveType2 = allType[moveType]
	return moveType2[pokemonTypeOne] * moveType2[pokemonTypeTwo]
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
	if randomOf100 < accuracy:
		return 'Hit'
	else:
		return 'Miss'
def getMoveDamage(move,atkPokemon,atkLevel,defPokemon,defLevel):
	moveBaseDamage = getMoveBaseDamage(move)
	effectiveness = getEffectiveness(move,defPokemon)
	stabBonus = getStabBonus(move,atkPokemon)
	moveVariety = getMoveVariety(move)
	if moveVariety == 'Physical':
		atkStat = getAtkStat(atkPokemon,atkLevel)
		defStat = getDefStat(defPokemon,defLevel)
		moveDamage = int(((((2 * myLevel / 5 + 2) * atkStat * moveBaseDamage / defStat) / 50 ) + 2) * stabBonus * effectiveness * float(randint(0,15)+85)/100)
		return moveDamage	
	if moveVariety == 'Special':
		atkStat = getSpAtkStat(atkPokemon,atkLevel)
		defStat = getSpDefStat(defPokemon,defLevel)
		moveDamage = int(((((2 * myLevel / 5 + 2) * atkStat * moveBaseDamage / defStat) / 50 ) + 2) * stabBonus * effectiveness * float(randint(0,15)+85)/100)
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



#def getStatBuff(pokemon,stat):
def getStatChange(move):
	print move
	statChange=[]
	for i in range(0,6):
		stat = getPokemonBaseStatDictToList(i)
		moveStatChange = getMoveStatChangeInfo(move,stat)
		statChange.append(moveStatChange)
	return statChange




getStatChange('Defense Curl')


def getTurnOrder(myPokemon,myLevel,enemyPokemon,enemyLevel):
	mySpd = getSpdStat(myPokemon,myLevel)
	enemySpd = getSpdStat(enemyPokemon,enemyLevel)
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
def startTurn(atkMove,atkPokemon,atkLevel,defPokemon,defLevel,defHP):
	moveDamage = getMoveDamage(atkMove,atkPokemon,atkLevel,defPokemon,defLevel)
	defMaxHP = gethpStat(defPokemon,defLevel)
	hitOrMiss = getHitOrMiss(atkMove)
	moveVariety = getMoveVariety(atkMove)
	if hitOrMiss == 'Miss':
		print atkPokemon, 'used', atkMove, 'but it missed!'
		return defHP
	if moveVariety == 'Support':
		moveExtraForm = getMoveExtraForm(atkMove)
		if moveExtraForm == 'Self':
			if atkPokemon == myPokemon:
				pokemonToApplyStatChange = getPokemonToApplyStatChange('My Pokemon')
			if atkPokemon == enemyPokemon:
				pokemonToApplyStatChange = getPokemonToApplyStatChange('Enemy Pokemon')
		if moveExtraForm == 'Enemy':
			if atkPokemon == myPokemon:
				pokemonToApplyStatChange = getPokemonToApplyStatChange('Enemy Pokemon')
			if atkPokemon == enemyPokemon:
				pokemonToApplyStatChange = getPokemonToApplyStatChange('My Pokemon')
		statChange = getStatChange(atkMove)
		pokemonToApplyStatChange = list(map(add, pokemonToApplyStatChange, statChange))
		print pokemonToApplyStatChange
		print atkPokemon, 'used', atkMove, 'against', defPokemon, '- it changed the stat stage of', defPokemon, 'by', statChange, '.', defPokemon, 'has', defHP, '/', defMaxHP, 'HP remaining!'
		HPList = [defHP]
		print HPList
		outcomeInfo = pokemonToApplyStatChange + HPList
		print outcomeInfo
		return outcomeInfo

	defHP = defHP - moveDamage
	if defHP < 0:
		defHP = 0
	print atkPokemon, 'used', atkMove, 'against', defPokemon, '- it dealt', moveDamage, 'HP damage!', defPokemon, 'has', defHP, '/', defMaxHP, 'HP remaining!'
	return defHP
def getMoveInput(myPokemon):
	movesetSize = len(getMoveSet(myPokemon))
	while True:
		try:
			moveInput = raw_input('-- ')
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
def startRound(myPokemon,myLevel,myHP,enemyPokemon,enemyLevel,enemyHP):
	print '\nWhat will', myPokemon, 'do?'
	print getMoveSet(myPokemon)
	myMove = getMoveInput(myPokemon)
	print ''
	enemyMove = getRandomMoveFromSet(enemyPokemon)
	turnOrder = getTurnOrder(myPokemon,myLevel,enemyPokemon,enemyLevel)
	if turnOrder == 'myPokemonFirst':
		enemyHP = startTurn(myMove,myPokemon,myLevel,enemyPokemon,enemyLevel,enemyHP)
		if enemyHP == 0:
			return [myHP,enemyHP]
		myHP = startTurn(enemyMove,enemyPokemon,enemyLevel,myPokemon,myLevel,myHP)
	if turnOrder == 'enemyPokemonFirst':
		myHP = startTurn(enemyMove,enemyPokemon,enemyLevel,myPokemon,myLevel,myHP)
		if myHP == 0:
			return [myHP,enemyHP]
		enemyHP = startTurn(myMove,myPokemon,myLevel,enemyPokemon,enemyLevel,enemyHP)
	print [myHP,enemyHP]
	return [myHP,enemyHP]
def startBattle(myPokemon,myLevel,enemyPokemon,enemyLevel):
	print 'A wild Level', enemyLevel, enemyPokemon, 'appeared! Go', myPokemon, '!'
	myHP = gethpStat(myPokemon,myLevel)
	enemyHP = gethpStat(enemyPokemon,enemyLevel)
	while myHP > 0 and enemyHP > 0:
		newHP = startRound(myPokemon,myLevel,myHP,enemyPokemon,enemyLevel,enemyHP)
		myHP = newHP[0]
		enemyHP = newHP[1]
	if myHP == 0:
		print myPokemon, 'fainted! You lose!'
	if myHP > 0:
		print 'The wild', enemyPokemon, 'fainted! You win!'


myPokemon='Charizard'
#enemyPokemon='Venusaur'
myLevel=100
#enemyLevel=100
enemyPokemon = getRandomPokemon()
enemyLevel = getRandomLevel()

startBattle(myPokemon,myLevel,enemyPokemon,enemyLevel)
