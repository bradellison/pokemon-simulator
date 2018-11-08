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

geodudeBaseStats = [40,80,100,30,30,20]
onixBaseStats = [35,45,160,30,45,70]

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

bulbasaurExpGroup = {'Fast'}
ivysaurExpGroup = {'Fast'}
venusaurExpGroup = {'Fast'}
charmanderExpGroup = {'Fast'}
charmeleonExpGroup = {'Fast'}
charizardExpGroup = {'Fast'}
squirtleExpGroup = {'Fast'}
wartortleExpGroup = {'Fast'}
blastoiseExpGroup = {'Fast'}
geodudeExpGroup = {'Fast'}
onixExpGroup = {'Fast'}

geodudeType = {'Type One':'Rock', 'Type Two':'Ground'}
onixType = {'Type One':'Rock', 'Type Two':'Ground'}

bulbasaurMoves = {'Move One':'Tackle', 'Move Two':'Growl', 'Move Three':'Vine Whip'}
ivysaurMoves = {'Move One':'Tackle', 'Move Two':'Growl', 'Move Three':'Vine Whip'}
venusaurMoves = {'Move One':'Tackle', 'Move Two':'Growl', 'Move Three':'Vine Whip', 'Move Four':'Petal Blizzard'}
charmanderMoves = {'Move One':'Scratch', 'Move Two':'Growl', 'Move Three':'Ember'}
charmeleonMoves = {'Move One':'Scratch', 'Move Two':'Growl', 'Move Three':'Ember'}
charizardMoves = {'Move One':'Scratch', 'Move Two':'Growl', 'Move Three':'Ember', 'Move Four':'Flamethrower'}
squirtleMoves = {'Move One':'Tackle', 'Move Two':'Tail Whip', 'Move Three':'Bubble'}
wartortleMoves = {'Move One':'Tackle', 'Move Two':'Tail Whip', 'Move Three':'Bubble'}
blastoiseMoves = {'Move One':'Tackle', 'Move Two':'Tail Whip', 'Move Three':'Bubble', 'Move Four':'Hydro Pump'}

geodudeMoves = {'Move One':'Tackle', 'Move Two':'Harden', 'Move Three':'Rock Polish', 'Move Four':'Magnitude'}
onixMoves = {'Move One':'Tackle', 'Move Two':'Harden', 'Move Three':'Rock Tomb', 'Move Four':'Rock Throw'}
#{'Move One':'', 'Move Two':'', 'Move Three':'', 'Move Four':''}

pokemonStats = {'Bulbasaur':bulbasaurBaseStats,'Ivysaur':ivysaurBaseStats,'Venusaur':venusaurBaseStats,'Charmander':charmanderBaseStats,'Charmeleon':charmeleonBaseStats,'Charizard':charizardBaseStats,'Squirtle':squirtleBaseStats,'Wartortle':wartortleBaseStats,'Blastoise':blastoiseBaseStats,'Geodude':geodudeBaseStats,'Onix':onixBaseStats}
pokemonTypes = {'Bulbasaur':bulbasaurType,'Ivysaur':ivysaurType,'Venusaur':venusaurType,'Charmander':charmanderType,'Charmeleon':charmeleonType,'Charizard':charizardType,'Squirtle':squirtleType,'Wartortle':wartortleType,'Blastoise':blastoiseType,'Geodude':geodudeType,'Onix':onixType}
pokemonMoves = {'Bulbasaur':bulbasaurMoves,'Ivysaur':ivysaurMoves,'Venusaur':venusaurMoves,'Charmander':charmanderMoves,'Charmeleon':charmeleonMoves,'Charizard':charizardMoves,'Squirtle':squirtleMoves,'Wartortle':wartortleMoves,'Blastoise':blastoiseMoves,'Geodude':geodudeMoves,'Onix':onixMoves}
pokemonExpGroup = {'Bulbasaur':bulbasaurExpGroup,'Ivysaur':ivysaurExpGroup,'Venusaur':venusaurExpGroup,'Charmander':charmanderExpGroup,'Charmeleon':charmeleonExpGroup,'Charizard':charizardExpGroup,'Squirtle':squirtleExpGroup,'Wartortle':wartortleExpGroup,'Blastoise':blastoiseExpGroup,'Geodude':geodudeExpGroup,'Onix':onixExpGroup}
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
hardenInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
rockTombInfo = {'Base Damage':60, 'Move Type':'Rock', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'Yes', 'Priority':0}
rockThrowInfo = {'Base Damage':50, 'Move Type':'Rock', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
rockPolishInfo = {'Base Damage':0, 'Move Type':'Rock', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
magnitudeInfo = {'Base Damage':50, 'Move Type':'Ground', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}

growlExtraInfo = {'Stat Change':'Enemy', 'Status Change':'No'}
tailWhipExtraInfo = {'Stat Change':'Enemy', 'Status Change':'No'}
emberExtraInfo = {'Stat Change':'None', 'Status Change':'Yes'}
defenseCurlExtraInfo = {'Stat Change':'Self', 'Status Change':'No'}
hardenExtraInfo = {'Stat Change':'Self', 'Status Change':'No'}
rockPolishExtraInfo = {'Stat Change':'Self', 'Status Change':'No'}
rockTombExtraInfo = {'Stat Change':'Enemy', 'Status Change':'No'}

growlStatChangeInfo = {'HP':0,'Atk':-1,'Def':0,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
defenseCurlStatChangeInfo = {'HP':0,'Atk':0,'Def':1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
tailWhipStatChangeInfo = {'HP':0,'Atk':0,'Def':-1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
hardenStatChangeInfo = {'HP':0,'Atk':0,'Def':1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
rockPolishStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':2,'Accuracy':0,'Chance':100}
rockTombStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':-1,'Accuracy':0,'Chance':100}

emberStatusChangeInfo = {'Type':1,'Chance':10}

normalEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':1, 'Ghost':0, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
fightingEffect = {'Normal':2, 'Fighting':1, 'Flying':0.5, 'Poison':0.5, 'Ground':1, 'Rock':2, 'Bug':0.5, 'Ghost':0, 'Steel':2, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':0.5, 'Ice':2, 'Dragon':1, 'Dark':2, 'Fairy':0.5, 'Null':1}
flyingEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':2, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':2, 'Electric':0.5, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
poisonEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':0.5, 'Ground':0.5, 'Rock':0.5, 'Bug':1, 'Ghost':0.5, 'Steel':0, 'Fire':1, 'Water':1, 'Grass':2, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':2, 'Null':1}
groundEffect = {'Normal':1, 'Fighting':1, 'Flying':0, 'Poison':2, 'Ground':1, 'Rock':2, 'Bug':0.5, 'Ghost':1, 'Steel':2, 'Fire':2, 'Water':1, 'Grass':0.5, 'Electric':2, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
rockEffect = {'Normal':1, 'Fighting':0.5, 'Flying':2, 'Poison':1, 'Ground':0.5, 'Rock':1, 'Bug':2, 'Ghost':1, 'Steel':0.5, 'Fire':2, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':2, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
bugEffect = {'Normal':1, 'Fighting':0.5, 'Flying':0.5, 'Poison':0.5, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':0.5, 'Steel':0.5, 'Fire':0.5, 'Water':1, 'Grass':2, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':2, 'Fairy':0.5, 'Null':1}
ghostEffect = {'Normal':0, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':2, 'Steel':1, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':0.5, 'Fairy':1, 'Null':1}
steelEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':2, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':0.5, 'Grass':1, 'Electric':0.5, 'Psychic':1, 'Ice':2, 'Dragon':1, 'Dark':1, 'Fairy':2, 'Null':1}
fireEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':2, 'Ghost':1, 'Steel':2, 'Fire':0.5, 'Water':0.5, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':2, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
waterEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':2, 'Rock':2, 'Bug':1, 'Ghost':1, 'Steel':1, 'Fire':2, 'Water':0.5, 'Grass':0.5, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
grassEffect = {'Normal':1, 'Fighting':1, 'Flying':0.5, 'Poison':0.5, 'Ground':2, 'Rock':2, 'Bug':0.5, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':2, 'Grass':0.5, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
electricEffect = {'Normal':1, 'Fighting':1, 'Flying':2, 'Poison':1, 'Ground':0, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':1, 'Fire':1, 'Water':2, 'Grass':0.5, 'Electric':0.5, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
psychicEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':2, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':0.5, 'Ice':1, 'Dragon':1, 'Dark':0, 'Fairy':1, 'Null':1}
iceEffect = {'Normal':1, 'Fighting':1, 'Flying':2, 'Poison':1, 'Ground':2, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':0.5, 'Grass':2, 'Electric':1, 'Psychic':1, 'Ice':0.5, 'Dragon':2, 'Dark':1, 'Fairy':1, 'Null':1}
dragonEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':2, 'Dark':1, 'Fairy':0, 'Null':1}
darkEffect = {'Normal':1, 'Fighting':0.5, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':2, 'Steel':1, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':0.5, 'Fairy':0.5, 'Null':1}
fairyEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':0.5, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':2, 'Dark':2, 'Fairy':1, 'Null':1}


allType = {'Normal':normalEffect, 'Fighting':fightingEffect, 'Flying':flyingEffect, 'Poison':poisonEffect, 'Ground':groundEffect, 'Rock':rockEffect, 'Bug':bugEffect, 'Ghost':ghostEffect, 'Steel':steelEffect, 'Fire':fireEffect, 'Water':waterEffect, 'Grass':grassEffect, 'Electric':electricEffect, 'Psychic':psychicEffect, 'Ice':iceEffect, 'Dragon':dragonEffect, 'Dark':darkEffect, 'Fairy':fairyEffect}
moveInfo = {'Tackle':tackleInfo,'Ember':emberInfo,'Bubble':bubbleInfo,'Vine Whip':vineWhipInfo,'Growl':growlInfo,'Defense Curl':defenseCurlInfo,'Scratch':scratchInfo,'Tail Whip':tailWhipInfo,'Flamethrower':flamethrowerInfo,'Hydro Pump':hydroPumpInfo,'Petal Blizzard':petalBlizzardInfo,'Harden':hardenInfo,'Rock Tomb':rockTombInfo,'Rock Throw':rockThrowInfo,'Rock Polish':rockPolishInfo,'Magnitude':magnitudeInfo}
moveExtraInfo = {'Ember':emberExtraInfo,'Growl':growlExtraInfo,'Defense Curl':defenseCurlExtraInfo,'Tail Whip':tailWhipExtraInfo,'Harden':hardenExtraInfo,'Rock Polish':rockPolishExtraInfo,'Rock Tomb':rockTombExtraInfo}
moveStatChangeInfo = {'Growl':growlStatChangeInfo,'Defense Curl':defenseCurlStatChangeInfo,'Tail Whip':tailWhipStatChangeInfo,'Harden':hardenStatChangeInfo,'Rock Polish':rockPolishStatChangeInfo,'Rock Tomb':rockTombStatChangeInfo}
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

def getExpGroup(pokemon,level):
	expGroup = getPokemonExpGroup
	exp = getExp(expGroup,level)

#def getExp(expGroup,level):
#	n = level
#	if expGroup == 'Erratic':
#		if n <= 50:
#			exp = ((n^3)*100-n)/50
#		if 50 < n <= 68:
#			exp = ((n^3)*150-n)/50
#		if 68 < n <= 98:
#			exp = ((n^3)*((1911-10*n)/3)/500
#		if 98 < n <= 100:
#			exp = ((n^3)*160-n)/100
#	if expGroup == 'Fast':
#		exp = (4*n^3)/5
#	if expGroup == 'MediumFast':
#		exp = n^3
#	if expGroup == 'MediumSlow':
#		exp = (6/5)*n^3 - 15*n^2 + 100*n - 140
#	if expGroup == 'Slow':
#		exp = (5*n^3)/4
#	return exp






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

def getTurnOrder(myPokemon,myPokemonLevel,myPokemonIV,myPokemonStatStage,myPokemonStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonStatStage,enemyPokemonStatus):
	mySpd = getSpdStat(myPokemon,myPokemonLevel,myPokemonIV,myPokemonStatStage,myPokemonStatus)
	enemySpd = getSpdStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonStatStage,enemyPokemonStatus)
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

def getPokemonMove(move,myPokemon,myPokemonLevel,enemyPokemon,enemyPokemonLevel):
	moveDamage = getMoveDamage(move,myPokemon,myPokemonLevel,enemyPokemon,enemyPokemonLevel)
	effectiveness = getEffectiveness(move,enemyPokemon)
	addedEffect = getMoveExtra(move)

def startMyTurn(move,myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo):
	myPokemonInfo = myTeam[0]; enemyPokemonInfo = enemyTeam[0]
	myPokemon = myPokemonInfo[0]; myPokemonLevel = myPokemonInfo[1]; myPokemonHP = myPokemonInfo[2]; myPokemonIV = myPokemonInfo[3]; myPokemonStatus = myPokemonInfo[4]; myPokemonStatusCount = myPokemonInfo[5]; myPokemonStatStage = myPokemonInfo[6]
	enemyPokemon = enemyPokemonInfo[0]; enemyPokemonLevel = enemyPokemonInfo[1]; enemyPokemonHP = enemyPokemonInfo[2]; enemyPokemonIV = enemyPokemonInfo[3]; enemyPokemonStatus = enemyPokemonInfo[4]; enemyPokemonStatusCount = enemyPokemonInfo[5]; enemyPokemonStatStage = enemyPokemonInfo[6]
	enemyBattleType = enemyTrainerInfo[0]; enemyTrainerName = enemyTrainerInfo[1]; enemyWording = enemyTrainerInfo[2]
	moveDamage = getMoveDamage(move,myPokemon,myPokemonLevel,myPokemonIV,myPokemonStatStage,myPokemonStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonStatStage)
	myPokemonStatusType = getStatusType(myPokemonStatus)
	enemyPokemonStatusType = getStatusType(enemyPokemonStatus)
	enemyMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV,'Enemy Pokemon')
	myMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV,'My Pokemon')
	hitOrMiss = getHitOrMiss(move)
	moveVariety = getMoveVariety(move)
	effectiveness = getEffectiveness(move,enemyPokemon)
	effectivenessWording = getEffectivesnessWording(effectiveness)

	if myPokemonStatus != 'Nothing':
		if myPokemonStatusType == 'Paralyzed':
			print(myPokemon, 'is paralyzed and may not be able to move!')
			i = randint(1,4)
			if i == 1:
				print(myPokemon, 'couldn\'t move!')
				myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
				enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
				myTeam[0] = myPokemonInfo
				enemyTeam[0] = enemyPokemonInfo
				return [myTeam,enemyTeam]	
		if myPokemonStatusType == 'Sleep':
			print(myPokemon, 'is sleeping!')
			myPokemonStatusCount = myPokemonStatusCount - 1
			if myPokemonStatusCount > 0:
				myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
				enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
				myTeam[0] = myPokemonInfo
				enemyTeam[0] = enemyPokemonInfo
				return [myTeam,enemyTeam]	
			myPokemonStatus = 0
			myPokemonStatusType = getStatusType(myPokemonStatus)
			print(myPokemon, 'woke up!')
		if myPokemonStatusType == 'Frozen':
			i = randint(1,5)
			if i == 1:
				myPokemonStatus = 0
				myPokemonStatusType = getStatusType(myPokemonStatus)
			else:
				print(myPokemon, 'is frozen and couldn\'t move!')
				myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
				enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
				myTeam[0] = myPokemonInfo
				enemyTeam[0] = enemyPokemonInfo
				return [myTeam,enemyTeam]		
	if hitOrMiss == 'Miss':
		print(myPokemon, 'used', move, 'but it missed!')
		myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
		enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
		myTeam[0] = myPokemonInfo
		enemyTeam[0] = enemyPokemonInfo
		return [myTeam,enemyTeam]
	if moveVariety == 'Support':
		moveExtraForm = getMoveExtraForm(move)
		if moveExtraForm == 'Enemy':
			statChange = getStatChange(move)
			enemyPokemonStatStage = list(map(add, enemyPokemonStatStage, statChange))
			print(myPokemon, 'used', move, 'against the', enemyWording, enemyPokemon, 'and it\'s stats changed by', statChange, '. They are now', enemyPokemonStatStage, '.')
		if moveExtraForm == 'Self':
			statChange = getStatChange(move)
			myPokemonStatStage = list(map(add, myPokemonStatStage, statChange))
			print('Your', myPokemon, 'used', move, 'and it\'s stats changed by', statChange, '. They are now', myPokemonStatStage, '.')
		myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
		enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
		myTeam[0] = myPokemonInfo
		enemyTeam[0] = enemyPokemonInfo
		return [myTeam,enemyTeam]
	enemyPokemonHP = enemyPokemonHP - moveDamage
	if enemyPokemonHP < 0:
		enemyPokemonHP = 0
	print(myPokemon, 'used', move, 'against the', enemyWording, enemyPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', enemyPokemon, 'has', enemyPokemonHP, '/', enemyMaxHP, 'HP remaining!')
	moveExtra = getMoveExtra(move)
	if moveExtra == 'Yes':		
		moveExtraForm = getMoveExtraForm(move)
		if moveExtraForm == 'Enemy':
			statChange = getStatChange(move)
			enemyPokemonStatStage = list(map(add, enemyPokemonStatStage, statChange))
			print('The', enemyWording, enemyPokemon, '\'s stats changed by', statChange, '. They are now', enemyPokemonStatStage, '.')
		if moveExtraForm == 'Self':
			statChange = getStatChange(move)
			myPokemonStatStage = list(map(add, myPokemonStatStage, statChange))
			print(myPokemon, '\'s stats changed by', statChange, '. They are now', myPokemonStatStage, '.')
		statusChange = getStatusChange(move)
		if statusChange == 'Yes':
			if enemyPokemonStatus == 0:
				statusChangeType = getStatusChangeType(move)
				statusChangeChance = getStatusChangeChance(move)
				x = randint(1,100)
				if x <= statusChangeChance:
					enemyPokemonStatus = statusChangeType
					statusType = getStatusType(enemyPokemonStatus)
					print(enemyPokemon, 'was', statusType + '!')
				if statusChangeType == 3:
					x = randint(1,3)	
					enemyPokemonStatusCount = x
	myPokemonStatusType = getStatusType(myPokemonStatus)
	if myPokemonStatusType != 'Nothing':
		if myPokemonStatusType == 'Burned':
			burnDamage = int(myMaxHP / 16)
			myPokemonHP = (myPokemonHP - burnDamage)
			print(myPokemon, 'took', burnDamage, 'HP damage due to it\'s burn! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
		if myPokemonStatusType == 'Poisoned':
			poisonDamage = int(myMaxHP / 8)
			myPokemonHP = (myPokemonHP - poisonDamage)
			print(myPokemon, 'took', poisonDamage, 'HP damage due to being poisoned! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
		if myPokemonStatusType == 'Toxic':
			myPokemonStatusCount = myPokemonStatusCount + 1
			toxicDamage = int(myMaxHP * myPokemonStatusCount / 16)
			myPokemonHP = myPokemonHP - toxicDamage
			print(myPokemon, 'took', toxicDamage, 'HP damage due to being badly poisoned! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
	myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
	enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
	myTeam[0] = myPokemonInfo
	enemyTeam[0] = enemyPokemonInfo
	return [myTeam,enemyTeam]

def startEnemyTurn(move,myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo):
	myPokemonInfo = myTeam[0]; enemyPokemonInfo = enemyTeam[0]
	myPokemon = myPokemonInfo[0]; myPokemonLevel = myPokemonInfo[1]; myPokemonHP = myPokemonInfo[2]; myPokemonIV = myPokemonInfo[3]; myPokemonStatus = myPokemonInfo[4]; myPokemonStatusCount = myPokemonInfo[5]; myPokemonStatStage = myPokemonInfo[6]
	enemyPokemon = enemyPokemonInfo[0]; enemyPokemonLevel = enemyPokemonInfo[1]; enemyPokemonHP = enemyPokemonInfo[2]; enemyPokemonIV = enemyPokemonInfo[3]; enemyPokemonStatus = enemyPokemonInfo[4]; enemyPokemonStatusCount = enemyPokemonInfo[5]; enemyPokemonStatStage = enemyPokemonInfo[6]
	enemyBattleType = enemyTrainerInfo[0]; enemyTrainerName = enemyTrainerInfo[1]; enemyWording = enemyTrainerInfo[2]
	moveDamage = getMoveDamage(move,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonStatStage,enemyPokemonStatus,myPokemon,myPokemonLevel,myPokemonIV,myPokemonStatStage)
	myPokemonStatusType = getStatusType(myPokemonStatus)
	enemyPokemonStatusType = getStatusType(enemyPokemonStatus)
	myMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV,'My Pokemon')
	enemyMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV,'Enemy Pokemon')
	hitOrMiss = getHitOrMiss(move)
	moveVariety = getMoveVariety(move)
	moveExtra = getMoveExtra(move)
	effectiveness = getEffectiveness(move,myPokemon)
	effectivenessWording = getEffectivesnessWording(effectiveness)
	if enemyPokemonStatusType != 'Nothing':
		if enemyPokemonStatusType == 'Paralyzed':
			print('The', enemyWording, enemyPokemon, 'is paralyzed and may not be able to move!')
			i = randint(1,4)
			if i == 1:
				print(enemyPokemon, 'couldn\'t move!')
				myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
				enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
				myTeam[0] = myPokemonInfo
				enemyTeam[0] = enemyPokemonInfo
				return [myTeam,enemyTeam]
		if enemyPokemonStatusType == 'Sleep':
			print('The', enemyWording, enemyPokemon, 'is sleeping!')
			enemyPokemonStatusCount = enemyPokemonStatusCount - 1
			if enemyPokemonStatusCount > 0:
				myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
				enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
				myTeam[0] = myPokemonInfo
				enemyTeam[0] = enemyPokemonInfo
				return [myTeam,enemyTeam]
			enemyPokemonStatus = 0
			enemyPokemonStatusType = getStatusType(enemyPokemonStatus)
			print('The', enemyWording, enemyPokemon, 'woke up!')
		if enemyPokemonStatusType == 'Frozen':
			i = randint(1,5)
			if i == 1:
				enemyPokemonStatus = 0
				enemyPokemonStatusType = getStatusType(enemyPokemonStatus)
			else:
				print('The', enemyWording, enemyPokemon, 'is frozen and couldn\'t move!')
				myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
				enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
				myTeam[0] = myPokemonInfo
				enemyTeam[0] = enemyPokemonInfo
				return [myTeam,enemyTeam]	
	if hitOrMiss == 'Miss':
		print(enemyPokemon, 'used', move, 'but it missed!')
		myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
		enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
		myTeam[0] = myPokemonInfo
		enemyTeam[0] = enemyPokemonInfo
		return [myTeam,enemyTeam]
	if moveVariety == 'Support':
		moveExtraForm = getMoveExtraForm(move)
		if moveExtraForm == 'Self':
			statChange = getStatChange(move)
			enemyPokemonStatStage = list(map(add, enemyPokemonStatStage, statChange))
			print('The', enemyWording, enemyPokemon, 'used', move, 'and it\'s stats changed by', statChange, '. They are now', enemyPokemonStatStage, '.')
		if moveExtraForm == 'Enemy':
			statChange = getStatChange(move)
			myPokemonStatStage = list(map(add, myPokemonStatStage, statChange))
			print('The', enemyWording, enemyPokemon, 'used', move, 'against your', myPokemon, 'and it\'s stats changed by', statChange, '. They are now', myPokemonStatStage, '.')
		myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
		enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
		myTeam[0] = myPokemonInfo
		enemyTeam[0] = enemyPokemonInfo
		return [myTeam,enemyTeam]
	myPokemonHP = myPokemonHP - moveDamage
	if myPokemonHP < 0:
		myPokemonHP = 0
	print('The', enemyWording, enemyPokemon, 'used', move, 'against', myPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', myPokemon, 'has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
	moveExtra = getMoveExtra(move)
	if moveExtra == 'Yes':	
		moveExtraForm = getMoveExtraForm(move)
		if moveExtraForm == 'Self':
			statChange = getStatChange(move)
			enemyPokemonStatStage = list(map(add, enemyPokemonStatStage, statChange))
			print('The', enemyWording, enemyPokemon, '\'s stats changed by', statChange, '. They are now', enemyPokemonStatStage, '.')
		if moveExtraForm == 'Enemy':
			statChange = getStatChange(move)
			myPokemonStatStage = list(map(add, myPokemonStatStage, statChange))
			print(myPokemon, '\'s stats changed by', statChange, '. They are now', myPokemonStatStage, '.')
		statusChange = getStatusChange(move)
		if statusChange == 'Yes':
			if myPokemonStatus == 0:
				statusChangeType = getStatusChangeType(move)
				statusChangeChance = getStatusChangeChance(move)
				x = randint(1,100)
				if x <= statusChangeChance:
					myPokemonStatus = statusChangeType
					statusType = getStatusType(myPokemonStatus)
					print(myPokemon, 'was', statusType + '!')
				if statusChangeType == 3:
					x = randint(1,3)	
					myPokemonStatusCount = x
	enemyPokemonStatusType = getStatusType(enemyPokemonStatus)
	if enemyPokemonStatusType != 'Nothing':
		if enemyPokemonStatusType == 'Burned':
			burnDamage = int(enemyMaxHP / 16)
			enemyPokemonHP = (enemyPokemonHP - burnDamage)
			print('The', enemyWording, enemyPokemon, 'took', burnDamage, 'HP damage due to it\'s burn! It has', enemyPokemonHP, '/', enemyMaxHP, 'HP remaining!')
		if enemyPokemonStatusType == 'Poisoned':
			poisonDamage = int(enemyMaxHP / 8)
			enemyPokemonHP = (enemyPokemonHP - poisonDamage)
			print('The', enemyWording, enemyPokemon, 'took', poisonDamage, 'HP damage due to being poisoned! It has', enemyPokemonHP, '/', enemyMaxHP, 'HP remaining!')
		if enemyPokemonStatusType == 'Toxic':
			enemyPokemonStatusCount = enemyPokemonStatusCount + 1
			toxicDamage = int(enemyMaxHP * meneyStatusCount / 16)
			enemyPokemonHP = enemyPokemonHP - toxicDamage
			print('The', enemyWording, enemyPokemon, 'took', toxicDamage, 'HP damage due to being badly poisoned! It has', enemyPokemonHP, '/', enemyMaxHP, 'HP remaining!')
	myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]
	enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage]
	myTeam[0] = myPokemonInfo
	enemyTeam[0] = enemyPokemonInfo
	return [myTeam,enemyTeam]

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

def getStarterInput():
	while True:
		try:
			choiceInput = input('-- ')
			if choiceInput == 'Bulbasaur':
				return choiceInput
			if choiceInput == 'Charmander':
				return choiceInput
			if choiceInput == 'Squirtle':
				return choiceInput					
			if int(choiceInput) == 1:
				choiceInput = 'Bulbasaur'
				return choiceInput
			if int(choiceInput) == 2:
				choiceInput = 'Charmander'
				return choiceInput
			if int(choiceInput) == 3:
				choiceInput = 'Squirtle'
				return choiceInput
			print("Please choose a Pokemon from the list above!")
		except ValueError:
			print("Please choose a move from the list.")

def getSwitchPokemon(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0]; myPokemonOneLevel = myPokemonOneInfo[1]; myPokemonOneHP = myPokemonOneInfo[2]; myPokemonOneIV = myPokemonOneInfo[3]; myPokemonOneStatus = myPokemonOneInfo[4]; myPokemonOneStatusCount = myPokemonOneInfo[5]; myPokemonOneStatStage = myPokemonOneInfo[6]; myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage)
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0]; myPokemonTwoLevel = myPokemonTwoInfo[1]; myPokemonTwoHP = myPokemonTwoInfo[2]; myPokemonTwoIV = myPokemonTwoInfo[3]; myPokemonTwoStatus = myPokemonTwoInfo[4]; myPokemonTwoStatusCount = myPokemonTwoInfo[5]; myPokemonTwoStatStage = myPokemonTwoInfo[6]; myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage)
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0]; myPokemonThreeLevel = myPokemonThreeInfo[1]; myPokemonThreeHP = myPokemonThreeInfo[2]; myPokemonThreeIV = myPokemonThreeInfo[3]; myPokemonThreeStatus = myPokemonThreeInfo[4]; myPokemonThreeStatusCount = myPokemonThreeInfo[5]; myPokemonThreeStatStage = myPokemonThreeInfo[6]; myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage)
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0]; myPokemonFourLevel = myPokemonFourInfo[1]; myPokemonFourHP = myPokemonFourInfo[2]; myPokemonFourIV = myPokemonFourInfo[3]; myPokemonFourStatus = myPokemonFourInfo[4]; myPokemonFourStatusCount = myPokemonFourInfo[5]; myPokemonFourStatStage = myPokemonFourInfo[6]; myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV,myPokemonFourStatStage)
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0]; myPokemonFiveLevel = myPokemonFiveInfo[1]; myPokemonFiveHP = myPokemonFiveInfo[2]; myPokemonFiveIV = myPokemonFiveInfo[3]; myPokemonFiveStatus = myPokemonFiveInfo[4]; myPokemonFiveStatusCount = myPokemonFiveInfo[5]; myPokemonFiveStatStage = myPokemonFiveInfo[6]; myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV,myPokemonFiveStatStage)
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0]; myPokemonSixLevel = myPokemonSixInfo[1]; myPokemonSixHP = myPokemonSixInfo[2]; myPokemonSixIV = myPokemonSixInfo[3]; myPokemonSixStatus = myPokemonSixInfo[4]; myPokemonSixStatusCount = myPokemonSixInfo[5]; myPokemonSixStatStage = myPokemonSixInfo[6]; myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV,myPokemonSixStatStage)
	print('Who would you like to choose?')
	if numberOfPokemon > 0:
		print('1 -', myPokemonOne, '- Lvl', myPokemonOneLevel, '-', myPokemonOneHP, '/', myPokemonOneMaxHP, 'HP.')
	if numberOfPokemon > 1:
		print('2 -', myPokemonTwo, '- Lvl', myPokemonTwoLevel, '-', myPokemonTwoHP, '/', myPokemonTwoMaxHP, 'HP.')
	if numberOfPokemon > 2:
		print('3 -', myPokemonThree, '- Lvl', myPokemonThreeLevel, '-', myPokemonThreeHP, '/', myPokemonThreeMaxHP, 'HP.')			
	if numberOfPokemon > 3:
		print('4 -', myPokemonFour, '- Lvl', myPokemonFourLevel, '-', myPokemonFourHP, '/', myPokemonFourMaxHP, 'HP.')	
	if numberOfPokemon > 4:
		print('5 -', myPokemonFive, '- Lvl', myPokemonFiveLevel, '-', myPokemonFiveHP, '/', myPokemonFiveMaxHP, 'HP.')	
	if numberOfPokemon > 5:
		print('Pokemon 6 -', myPokemonSix, '- Lvl', myPokemonSixLevel, '-', myPokemonSixHP, '/', myPokemonSixMaxHP, 'HP.')
	while True:
		try:
			choice = input('-- ')
			if int(choice) > 0 and int(choice) <= numberOfPokemon:
				choice = int(choice) - 1
				if choice == 0:
					change = 0
				else:
					change = 1
					pokemonToChangeToInfo = myTeam[choice]
					pokemon = pokemonToChangeToInfo[0]
					pokemonHP = pokemonToChangeToInfo[2]
					if pokemonHP > 0:
						myTeam[choice], myTeam[0] = myTeam[0], myTeam[choice]
						return [myTeam, change]
					if pokemonHP == 0:
						print(pokemon, 'has fainted! Choose another!')
			print('Please choose one of the above!')
		except ValueError:
			print("Please choose one of the above!")

def getRandomSwitchPokemon(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0]; myPokemonOneLevel = myPokemonOneInfo[1]; myPokemonOneHP = myPokemonOneInfo[2]; myPokemonOneIV = myPokemonOneInfo[3]; myPokemonOneStatus = myPokemonOneInfo[4]; myPokemonOneStatusCount = myPokemonOneInfo[5]; myPokemonOneStatStage = myPokemonOneInfo[6]; myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage)
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0]; myPokemonTwoLevel = myPokemonTwoInfo[1]; myPokemonTwoHP = myPokemonTwoInfo[2]; myPokemonTwoIV = myPokemonTwoInfo[3]; myPokemonTwoStatus = myPokemonTwoInfo[4]; myPokemonTwoStatusCount = myPokemonTwoInfo[5]; myPokemonTwoStatStage = myPokemonTwoInfo[6]; myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage)
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0]; myPokemonThreeLevel = myPokemonThreeInfo[1]; myPokemonThreeHP = myPokemonThreeInfo[2]; myPokemonThreeIV = myPokemonThreeInfo[3]; myPokemonThreeStatus = myPokemonThreeInfo[4]; myPokemonThreeStatusCount = myPokemonThreeInfo[5]; myPokemonThreeStatStage = myPokemonThreeInfo[6]; myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage)
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0]; myPokemonFourLevel = myPokemonFourInfo[1]; myPokemonFourHP = myPokemonFourInfo[2]; myPokemonFourIV = myPokemonFourInfo[3]; myPokemonFourStatus = myPokemonFourInfo[4]; myPokemonFourStatusCount = myPokemonFourInfo[5]; myPokemonFourStatStage = myPokemonFourInfo[6]; myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV,myPokemonFourStatStage)
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0]; myPokemonFiveLevel = myPokemonFiveInfo[1]; myPokemonFiveHP = myPokemonFiveInfo[2]; myPokemonFiveIV = myPokemonFiveInfo[3]; myPokemonFiveStatus = myPokemonFiveInfo[4]; myPokemonFiveStatusCount = myPokemonFiveInfo[5]; myPokemonFiveStatStage = myPokemonFiveInfo[6]; myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV,myPokemonFiveStatStage)
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0]; myPokemonSixLevel = myPokemonSixInfo[1]; myPokemonSixHP = myPokemonSixInfo[2]; myPokemonSixIV = myPokemonSixInfo[3]; myPokemonSixStatus = myPokemonSixInfo[4]; myPokemonSixStatusCount = myPokemonSixInfo[5]; myPokemonSixStatStage = myPokemonSixInfo[6]; myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV,myPokemonSixStatStage)
	while True:
		try:
			choice = randint(1,numberOfPokemon)
			if int(choice) > 0 and int(choice) <= numberOfPokemon:
				choice = int(choice) - 1
				if choice == 0:
					change = 0
				else:
					change = 1
					pokemonToChangeTo = myTeam[choice]
					pokemonHP = pokemonToChangeTo[2]
					if pokemonHP > 0:
						myTeam[choice], myTeam[0] = myTeam[0], myTeam[choice]
						return [myTeam, change]
		except ValueError:
			change

#def startRound(myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatStage,myPokemonStatus,myPokemonStatusCount,enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatStage,enemyPokemonStatus,enemyPokemonStatusCount):
def startRound(myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo):
	myPokemonInfo = myTeam[0]; enemyPokemonInfo = enemyTeam[0]
	myPokemon = myPokemonInfo[0]; myPokemonLevel = myPokemonInfo[1]; myPokemonHP = myPokemonInfo[2]; myPokemonIV = myPokemonInfo[3]; myPokemonStatus = myPokemonInfo[4]; myPokemonStatusCount = myPokemonInfo[5]; myPokemonStatStage = myPokemonInfo[6]
	enemyPokemon = enemyPokemonInfo[0]; enemyPokemonLevel = enemyPokemonInfo[1]; enemyPokemonHP = enemyPokemonInfo[2]; enemyPokemonIV = enemyPokemonInfo[3]; enemyPokemonStatus = enemyPokemonInfo[4]; enemyPokemonStatusCount = enemyPokemonInfo[5]; enemyPokemonStatStage = enemyPokemonInfo[6]
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
		turnOrder = getTurnOrder(myPokemon,myPokemonLevel,myPokemonIV,myPokemonStatStage,myPokemonStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonStatStage,enemyPokemonStatus)
		if turnOrder == 'myPokemonFirst':
			turnOutcomeInfo = startMyTurn(myMove,myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
			myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]
			enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[2]; enemyPokemonHP = enemyPokemonInfo[2]
			if enemyPokemonHP == 0 or myPokemonHP == 0:
				roundOutcomeInfo = [myTeam,enemyTeam,run]
				return roundOutcomeInfo
			turnOutcomeInfo = startEnemyTurn(enemyMove,myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
			myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]
			enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
			roundOutcomeInfo = [myTeam,enemyTeam,run]
			return roundOutcomeInfo
		if turnOrder == 'enemyPokemonFirst':
			turnOutcomeInfo = startEnemyTurn(enemyMove,myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
			myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]
			enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[2]; enemyPokemonHP = enemyPokemonInfo[2]
			if myPokemonHP == 0 or enemyPokemonHP == 0:
				roundOutcomeInfo = [myTeam,enemyTeam,run]
				return roundOutcomeInfo
			turnOutcomeInfo = startMyTurn(myMove,myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
			myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]
			enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
			roundOutcomeInfo = [myTeam,enemyTeam,run]
			return roundOutcomeInfo
	if choiceInput == 'Run':
		run = [1]
		roundOutcomeInfo = [myTeam,enemyTeam,run]
		return roundOutcomeInfo
	if choiceInput == 'Bag':
		print('Nothing in your bag!')
		run = [0]
		enemyMove = getRandomMoveFromSet(enemyPokemon)
		turnOutcomeInfo = startEnemyTurn(enemyMove,myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
		myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]
		enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
		roundOutcomeInfo = [myTeam,enemyTeam,run]
		return roundOutcomeInfo
	if choiceInput == 'Pokemon':
		run = [0]
		oldPokemon = myPokemon
		changePokemon = getSwitchPokemon(myTeam)
		myTeam = changePokemon[0]; change = changePokemon[1]
		if change == 0:
			roundOutcomeInfo = [myTeam,enemyTeam,run]
			return roundOutcomeInfo
		myPokemonInfo = myTeam[0]; myPokemon = myPokemonInfo[0]
		print ('You switched from', oldPokemon, 'into', myPokemon + '!')
		enemyMove = getRandomMoveFromSet(enemyPokemon)
		turnOutcomeInfo = startEnemyTurn(enemyMove,myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
		myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]; myPokemon = myPokemonInfo[0]
		enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
		roundOutcomeInfo = [myTeam,enemyTeam,run]
		return roundOutcomeInfo

#def startBattle(myTeam,enemyTeam):
#	print('A wild Level', enemyPokemonLevel, enemyPokemon, 'appeared! Go', myPokemon, '!')
#	enemyPokemonIV = getRandomIV()
#	enemyPokemonStatus = 0
#	myPokemonStatusCount = 0
#	enemyPokemonStatusCount = 0
#	myPokemonHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV,'My Pokemon')
#	enemyPokemonHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV,'Enemy Pokemon')
#	myPokemonStatStage = getPokemonStatStage('My Pokemon')
#	enemyPokemonStatStage = getPokemonStatStage('Enemy Pokemon')
#	while myPokemonHP > 0 and enemyPokemonHP > 0:
#		roundOutcomeInfo = startRound(myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatStage,myPokemonStatus,myPokemonStatusCount,enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatStage,enemyPokemonStatus,enemyPokemonStatusCount)
#		myPokemonHP = roundOutcomeInfo[0]
#		enemyPokemonHP = roundOutcomeInfo[1]
#		myPokemonStatStage = list(operator.itemgetter(2,3,4,5,6,7,8)(roundOutcomeInfo))
#		enemyPokemonStatStage = list(operator.itemgetter(9,10,11,12,13,14,15)(roundOutcomeInfo))
#		myPokemonStatus = roundOutcomeInfo[16]
#		myPokemonStatusCount = roundOutcomeInfo[17]
#		enemyPokemonStatus = roundOutcomeInfo[18]
#		enemyPokemonStatusCount=roundOutcomeInfo[19]
#		runLast=roundOutcomeInfo[20]
#		if int(runLast) > 0:
#			print('You got away safely!')
#			return 1
#	if myPokemonHP == 0:
#		print(myPokemon, 'fainted! You lose!')
#	if myPokemonHP > 0:
#		print('The wild', enemyPokemon, 'fainted! You win!')

def getTeamTotalHP(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0]; myPokemonOneLevel = myPokemonOneInfo[1]; myPokemonOneHP = myPokemonOneInfo[2]; myPokemonOneIV = myPokemonOneInfo[3]; myPokemonOneStatus = myPokemonOneInfo[4]; myPokemonOneStatusCount = myPokemonOneInfo[5]; myPokemonOneStatStage = myPokemonOneInfo[6]; myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage)
		myTeamTotalHP = myPokemonOneHP
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0]; myPokemonTwoLevel = myPokemonTwoInfo[1]; myPokemonTwoHP = myPokemonTwoInfo[2]; myPokemonTwoIV = myPokemonTwoInfo[3]; myPokemonTwoStatus = myPokemonTwoInfo[4]; myPokemonTwoStatusCount = myPokemonTwoInfo[5]; myPokemonTwoStatStage = myPokemonTwoInfo[6]; myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0]; myPokemonThreeLevel = myPokemonThreeInfo[1]; myPokemonThreeHP = myPokemonThreeInfo[2]; myPokemonThreeIV = myPokemonThreeInfo[3]; myPokemonThreeStatus = myPokemonThreeInfo[4]; myPokemonThreeStatusCount = myPokemonThreeInfo[5]; myPokemonThreeStatStage = myPokemonThreeInfo[6]; myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0]; myPokemonFourLevel = myPokemonFourInfo[1]; myPokemonFourHP = myPokemonFourInfo[2]; myPokemonFourIV = myPokemonFourInfo[3]; myPokemonFourStatus = myPokemonFourInfo[4]; myPokemonFourStatusCount = myPokemonFourInfo[5]; myPokemonFourStatStage = myPokemonFourInfo[6]; myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV,myPokemonFourStatStage)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0]; myPokemonFiveLevel = myPokemonFiveInfo[1]; myPokemonFiveHP = myPokemonFiveInfo[2]; myPokemonFiveIV = myPokemonFiveInfo[3]; myPokemonFiveStatus = myPokemonFiveInfo[4]; myPokemonFiveStatusCount = myPokemonFiveInfo[5]; myPokemonFiveStatStage = myPokemonFiveInfo[6]; myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV,myPokemonFiveStatStage)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP + myPokemonFiveHP
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0]; myPokemonSixLevel = myPokemonSixInfo[1]; myPokemonSixHP = myPokemonSixInfo[2]; myPokemonSixIV = myPokemonSixInfo[3]; myPokemonSixStatus = myPokemonSixInfo[4]; myPokemonSixStatusCount = myPokemonSixInfo[5]; myPokemonSixStatStage = myPokemonSixInfo[6]; myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV,myPokemonSixStatStage)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP + myPokemonFiveHP + myPokemonSixHP
	return myTeamTotalHP

def startBattle(myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo):
	myPokemonInfo = myTeam[0]; enemyPokemonInfo = enemyTeam[0]
	myPokemon = myPokemonInfo[0]; myPokemonLevel = myPokemonInfo[1]; myPokemonHP = myPokemonInfo[2]; myPokemonIV = myPokemonInfo[3]; myPokemonStatus = myPokemonInfo[4]; myPokemonStatusCount = myPokemonInfo[5]; myPokemonStatStage = [6]
	enemyPokemon = enemyPokemonInfo[0]; enemyPokemonLevel = enemyPokemonInfo[1]; enemyPokemonHP = enemyPokemonInfo[2]; enemyPokemonIV = enemyPokemonInfo[3]; enemyPokemonStatus = enemyPokemonInfo[4]; enemyPokemonStatusCount = enemyPokemonInfo[5]; enemyPokemonStatStage = [6]
	enemyBattleType = enemyTrainerInfo[0]; enemyTrainerName = enemyTrainerInfo[1]
	if enemyBattleType == 'Trainer':
		print(enemyTrainerName, 'sent out a lvl', enemyPokemonLevel, enemyPokemon + '!', 'Go', myPokemon + '!')
	if enemyBattleType == 'Wild':
		print('A wild lvl', enemyPokemonLevel, enemyPokemon, 'appeared! Go', myPokemon, '!')
	myTeamTotalHP = getTeamTotalHP(myTeam)
	enemyTeamTotalHP = getTeamTotalHP(enemyTeam)
	while myTeamTotalHP > 0 and enemyPokemonHP > 0:
		while myPokemonHP > 0 and enemyPokemonHP > 0:
			roundOutcomeInfo = startRound(myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
			myTeam = roundOutcomeInfo[0]; enemyTeam = roundOutcomeInfo[1]
			myPokemonInfo = myTeam[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemon = myPokemonInfo[0]; myPokemonLevel = myPokemonInfo[1]; myPokemonHP = myPokemonInfo[2]; myPokemonIV = myPokemonInfo[3]; myPokemonStatus = myPokemonInfo[4]; myPokemonStatusCount = myPokemonInfo[5]; myPokemonStatStage = [6]
			enemyPokemon = enemyPokemonInfo[0]; enemyPokemonLevel = enemyPokemonInfo[1]; enemyPokemonHP = enemyPokemonInfo[2]; enemyPokemonIV = enemyPokemonInfo[3]; enemyPokemonStatus = enemyPokemonInfo[4]; enemyPokemonStatusCount = enemyPokemonInfo[5]; enemyPokemonStatStage = [6]
			runLast=roundOutcomeInfo[2]; runLast=runLast[0]
			if int(runLast) > 0:
				print('You got away safely!')
				return 1
		myTeamTotalHP = int(getTeamTotalHP(myTeam)); enemyTeamTotalHP = int(getTeamTotalHP(enemyTeam))
		if myTeamTotalHP == 0:
			break
		if enemyTeamTotalHP == 0:
			break
		if myPokemonHP == 0:	
			print (myPokemon, 'fainted! Who would you like to switch to?')
			myTeam = roundOutcomeInfo[0]; enemyTeam = roundOutcomeInfo[1]
			myPokemonInfo = myTeam[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemon = myPokemonInfo[0]; myPokemonLevel = myPokemonInfo[1]; myPokemonHP = myPokemonInfo[2]; myPokemonIV = myPokemonInfo[3]; myPokemonStatus = myPokemonInfo[4]; myPokemonStatusCount = myPokemonInfo[5]; myPokemonStatStage = [6]
			enemyPokemon = enemyPokemonInfo[0]; enemyPokemonLevel = enemyPokemonInfo[1]; enemyPokemonHP = enemyPokemonInfo[2]; enemyPokemonIV = enemyPokemonInfo[3]; enemyPokemonStatus = enemyPokemonInfo[4]; enemyPokemonStatusCount = enemyPokemonInfo[5]; enemyPokemonStatStage = [6]
			oldPokemon = myPokemon
			changePokemon = getSwitchPokemon(myTeam)
			myTeam = changePokemon[0]; change = changePokemon[1]
			if change == 0:
				roundOutcomeInfo = [myTeam,enemyTeam,run]
				return roundOutcomeInfo
			myPokemonInfo = myTeam[0]; myPokemon = myPokemonInfo[0]
			myPokemonHP = myPokemonInfo[2]
			print ('You switched from', oldPokemon, 'into', myPokemon + '!')
		if enemyPokemonHP == 0:
			print (enemyPokemon, 'fainted!')
			myTeam = roundOutcomeInfo[0]; enemyTeam = roundOutcomeInfo[1]
			myPokemonInfo = myTeam[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemon = myPokemonInfo[0]; myPokemonLevel = myPokemonInfo[1]; myPokemonHP = myPokemonInfo[2]; myPokemonIV = myPokemonInfo[3]; myPokemonStatus = myPokemonInfo[4]; myPokemonStatusCount = myPokemonInfo[5]; myPokemonStatStage = [6]
			enemyPokemon = enemyPokemonInfo[0]; enemyPokemonLevel = enemyPokemonInfo[1]; enemyPokemonHP = enemyPokemonInfo[2]; enemyPokemonIV = enemyPokemonInfo[3]; enemyPokemonStatus = enemyPokemonInfo[4]; enemyPokemonStatusCount = enemyPokemonInfo[5]; enemyPokemonStatStage = [6]
			oldEnemyPokemon = enemyPokemon
			changePokemon = getRandomSwitchPokemon(enemyTeam)
			enemyTeam = changePokemon[0]; change = changePokemon[1]
			enemyPokemonInfo = enemyTeam[0]; enemyPokemon = enemyPokemonInfo[0]
			enemyPokemonHP = enemyPokemonInfo[2]
			print (enemyTrainerName, 'switched from', oldEnemyPokemon, 'into', enemyPokemon + '!')
	myTeamTotalHP = getTeamTotalHP(myTeam)
	if myTeamTotalHP == 0:
		print('You whited out!')
	if enemyPokemonHP == 0:
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
	myPokemonOne = getStarterInput()
	if myPokemonOne == 'Bulbasaur':
		enemyPokemonOne = 'Charmander'
	if myPokemonOne == 'Charmander':
		enemyPokemonOne = 'Squirtle'
	if myPokemonOne == 'Squirtle':
		enemyPokemonOne = 'Bulbasaur'
	myPokemonOneLevel = 5; myPokemonOneIV = getRandomIV(); myPokemonOneStatus = 0; myPokemonOneStatStage = [0,0,0,0,0,0,0]; myPokemonOneStatusCount = 0; myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage)
	enemyPokemonOneLevel = 5; enemyPokemonOneIV = getRandomIV(); enemyPokemonOneStatus = 0; enemyPokemonOneStatStage = [0,0,0,0,0,0,0]; enemyPokemonOneStatusCount = 0; enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneStatStage)
	myPokemonOneList = [myPokemonOne,myPokemonOneLevel,myPokemonOneHP,myPokemonOneIV,myPokemonOneStatus,myPokemonOneStatusCount,myPokemonOneStatStage]
	enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneHP,enemyPokemonOneIV,enemyPokemonOneStatus,enemyPokemonOneStatusCount,enemyPokemonOneStatStage]
	myTeam = [myPokemonOneList]
	enemyTeam = [enemyPokemonOneList]
	print('Gary: \n Fine, I choose', enemyPokemonOne + '! Let\'s fight!')
	input()
	startBattle(myTeam,enemyTeam,1)

def chooseGameplay():
	print('> To begin the game as normal, type 1\n> For a preset battle, type 2\n > Gym Leader Challenge, type 3')
	x = input()
	if x == '1':
		startGame()
	if x == '2':
		myPokemonOne = 'Charizard'; myPokemonOneLevel = 100; myPokemonOneIV = getRandomIV(); myPokemonOneStatus = 0; myPokemonOneStatStage = [0,0,0,0,0,0,0]; myPokemonOneStatusCount = 0; myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage)
		myPokemonTwo = 'Charmander'; myPokemonTwoLevel = 50; myPokemonTwoIV = getRandomIV(); myPokemonTwoStatus = 0; myPokemonTwoStatStage = [0,0,0,0,0,0,0]; myPokemonTwoStatusCount = 0; myPokemonTwoHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage)
		myPokemonThree = 'Bulbasaur'; myPokemonThreeLevel = 19; myPokemonThreeIV = getRandomIV(); myPokemonThreeStatus = 0; myPokemonThreeStatStage = [0,0,0,0,0,0,0]; myPokemonThreeStatusCount = 0; myPokemonThreeHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage)
		enemyPokemonOne = 'Venusaur'; enemyPokemonOneLevel = 100; enemyPokemonOneIV = getRandomIV(); enemyPokemonOneStatus = 0; enemyPokemonOneStatStage = [0,0,0,0,0,0,0]; enemyPokemonOneStatusCount = 0; enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneStatStage)
		enemyPokemonTwo = 'Ivysaur'; enemyPokemonTwoLevel = 50; enemyPokemonTwoIV = getRandomIV(); enemyPokemonTwoStatus = 0; enemyPokemonTwoStatStage = [0,0,0,0,0,0,0]; enemyPokemonTwoStatusCount = 0; enemyPokemonTwoHP = gethpStat(enemyPokemonTwo,enemyPokemonTwoLevel,enemyPokemonTwoIV,enemyPokemonTwoStatStage)
		myPokemonOneList = [myPokemonOne,myPokemonOneLevel,myPokemonOneHP,myPokemonOneIV,myPokemonOneStatus,myPokemonOneStatusCount,myPokemonOneStatStage]
		myPokemonTwoList = [myPokemonTwo,myPokemonTwoLevel,myPokemonTwoHP,myPokemonTwoIV,myPokemonTwoStatus,myPokemonTwoStatusCount,myPokemonTwoStatStage]
		myPokemonThreeList = [myPokemonThree,myPokemonThreeLevel,myPokemonThreeHP,myPokemonThreeIV,myPokemonThreeStatus,myPokemonThreeStatusCount,myPokemonThreeStatStage]
		enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneHP,enemyPokemonOneIV,enemyPokemonOneStatus,enemyPokemonOneStatusCount,enemyPokemonOneStatStage]
		enemyPokemonTwoList = [enemyPokemonTwo,enemyPokemonTwoLevel,enemyPokemonTwoHP,enemyPokemonTwoIV,enemyPokemonTwoStatus,enemyPokemonTwoStatusCount,enemyPokemonTwoStatStage]
		myTeam = [myPokemonOneList,myPokemonTwoList,myPokemonThreeList]
		enemyTeam = [enemyPokemonOneList,enemyPokemonTwoList]
		myTrainerInfo = [1]
		enemyTrainerInfo = ['Trainer','Jimbo','opposing']
		startBattle(myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
	if x == '3':
		myPokemonOne = 'Onix'; myPokemonOneLevel = 13; myPokemonOneIV = getRandomIV(); myPokemonOneStatus = 0; myPokemonOneStatStage = [0,0,0,0,0,0,0]; myPokemonOneStatusCount = 0; myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage)
		myPokemonTwo = 'Bulbasaur'; myPokemonTwoLevel = 13; myPokemonTwoIV = getRandomIV(); myPokemonTwoStatus = 0; myPokemonTwoStatStage = [0,0,0,0,0,0,0]; myPokemonTwoStatusCount = 0; myPokemonTwoHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage)
		myPokemonThree = 'Squirtle'; myPokemonThreeLevel = 13; myPokemonThreeIV = getRandomIV(); myPokemonThreeStatus = 0; myPokemonThreeStatStage = [0,0,0,0,0,0,0]; myPokemonThreeStatusCount = 0; myPokemonThreeHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage)
		enemyPokemonOne = 'Geodude'; enemyPokemonOneLevel = 12; enemyPokemonOneIV = getRandomIV(); enemyPokemonOneStatus = 0; enemyPokemonOneStatStage = [0,0,0,0,0,0,0]; enemyPokemonOneStatusCount = 0; enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneStatStage)
		enemyPokemonTwo = 'Onix'; enemyPokemonTwoLevel = 14; enemyPokemonTwoIV = getRandomIV(); enemyPokemonTwoStatus = 0; enemyPokemonTwoStatStage = [0,0,0,0,0,0,0]; enemyPokemonTwoStatusCount = 0; enemyPokemonTwoHP = gethpStat(enemyPokemonTwo,enemyPokemonTwoLevel,enemyPokemonTwoIV,enemyPokemonTwoStatStage)
		myPokemonOneList = [myPokemonOne,myPokemonOneLevel,myPokemonOneHP,myPokemonOneIV,myPokemonOneStatus,myPokemonOneStatusCount,myPokemonOneStatStage]
		myPokemonTwoList = [myPokemonTwo,myPokemonTwoLevel,myPokemonTwoHP,myPokemonTwoIV,myPokemonTwoStatus,myPokemonTwoStatusCount,myPokemonTwoStatStage]
		myPokemonThreeList = [myPokemonThree,myPokemonThreeLevel,myPokemonThreeHP,myPokemonThreeIV,myPokemonThreeStatus,myPokemonThreeStatusCount,myPokemonThreeStatStage]
		enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneHP,enemyPokemonOneIV,enemyPokemonOneStatus,enemyPokemonOneStatusCount,enemyPokemonOneStatStage]
		enemyPokemonTwoList = [enemyPokemonTwo,enemyPokemonTwoLevel,enemyPokemonTwoHP,enemyPokemonTwoIV,enemyPokemonTwoStatus,enemyPokemonTwoStatusCount,enemyPokemonTwoStatStage]
		myTeam = [myPokemonOneList,myPokemonTwoList,myPokemonThreeList]
		enemyTeam = [enemyPokemonOneList,enemyPokemonTwoList]
		myTrainerInfo = [1]
		enemyTrainerInfo = ['Trainer','Brock','gym leader\'s']
		startBattle(myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)


chooseGameplay()

#team (pre battle) = [pokemonOneList,pokemonTwoList,pokemonThreeList,pokemonFourList]
#pokemonOneList (pre battle) = [pokemonOne,pokemonOneLevel,pokemonOneHP,pokemonOneIV,pokemonOneStatus]

		#myPokemonList = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage]

myPokemon='Charizard'
enemyPokemon='Venusaur'
myPokemonLevel=100
enemyPokemonLevel=100
myPokemonIV = [31, 31, 31, 31, 31, 31]
#enemyPokemon = getRandomPokemon()
#enemyPokemonLevel = getRandomLevel()




#startBattle(myPokemon,myPokemonLevel,myPokemonIV,enemyPokemon,enemyPokemonLevel)
