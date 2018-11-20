from random import randint
from operator import add
import operator
import time
import random

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
volatileStatusNumberToType = {0:'Confused',1:'Leech Seed'}

bulbasaurType = {'Type One':'Grass','Type Two':'Poison'}
ivysaurType = {'Type One':'Grass','Type Two':'Poison'}
venusaurType = {'Type One':'Grass','Type Two':'Poison'}
charmanderType = {'Type One':'Fire','Type Two':'Null'}
charmeleonType = {'Type One':'Fire','Type Two':'Null'}
charizardType = {'Type One':'Fire','Type Two':'Flying'}
squirtleType = {'Type One':'Water','Type Two':'Null'}
wartortleType = {'Type One':'Water','Type Two':'Null'}
blastoiseType = {'Type One':'Water','Type Two':'Null'}
geodudeType = {'Type One':'Rock', 'Type Two':'Ground'}
onixType = {'Type One':'Rock', 'Type Two':'Ground'}

bulbasaurExpGroup = {'Exp Group':'Fast','Exp Yield':64}
ivysaurExpGroup = {'Exp Group':'Fast','Exp Yield':142}
venusaurExpGroup = {'Exp Group':'Fast','Exp Yield':236}
charmanderExpGroup = {'Exp Group':'Fast','Exp Yield':62}
charmeleonExpGroup = {'Exp Group':'Fast','Exp Yield':142}
charizardExpGroup = {'Exp Group':'Fast','Exp Yield':240}
squirtleExpGroup = {'Exp Group':'Fast','Exp Yield':63}
wartortleExpGroup = {'Exp Group':'Fast','Exp Yield':142}
blastoiseExpGroup = {'Exp Group':'Fast','Exp Yield':239}
geodudeExpGroup = {'Exp Group':'Fast','Exp Yield':90}
onixExpGroup = {'Exp Group':'Fast','Exp Yield':77}

bulbasaurEvolution = {'Evolve':'Yes','Level':16,'Pokemon':'Ivysaur'}
ivysaurEvolution = {'Evolve':'Yes','Level':36,'Pokemon':'Venusaur'}
venusaurEvolution = {'Evolve':'No'}
charmanderEvolution = {'Evolve':'Yes','Level':16,'Pokemon':'Charmeleon'}
charmeleonEvolution = {'Evolve':'Yes','Level':36,'Pokemon':'Charizard'}
charizardEvolution = {'Evolve':'No'}
squirtleEvolution = {'Evolve':'Yes','Level':16,'Pokemon':'Wartortle'}
wartortleEvolution = {'Evolve':'Yes','Level':36,'Pokemon':'Blastoise'}
blastoiseEvolution = {'Evolve':'No'}
geodudeEvolution = {'Evolve':'No'}
onixEvolution = {'Evolve':'No'}

bulbasaurMovesByLevel = {1:'Tackle',3:'Growl',7:'Leech Seed',9:'Vine Whip',1300:'Poison Powder',1400:'Sleep Powder',1500:'Take Down',1900:'Razor Leaf'}
ivysaurMovesByLevel = {1:'Tackle',3:'Growl',700:'Leech Seed',9:'Vine Whip',1300:'Poison Powder',1400:'Sleep Powder',1500:'Take Down',2000:'Razor Leaf'}
venusaurMovesByLevel = {1:'Tackle',3:'Growl',700:'Leech Seed',9:'Vine Whip',1300:'Poison Powder',1400:'Sleep Powder',1500:'Take Down',2000:'Razor Leaf'}
charmanderMovesByLevel = {1:'Scratch',2:'Growl',7:'Ember',10:'Smokescreen',16:'Dragon Rage',19:'Scary Face',25:'Fire Fang'}
charmeleonMovesByLevel = {1:'Scratch',2:'Growl',7:'Ember',10:'Smokescreen',17:'Dragon Rage',21:'Scary Face',28:'Fire Fang'}
charizardMovesByLevel = {1:'Scratch',2:'Growl',7:'Ember',10:'Smokescreen',17:'Dragon Rage',21:'Scary Face',28:'Fire Fang'}
squirtleMovesByLevel = {1:'Tackle',4:'Tail Whip',7:'Water Gun',10:'Withdraw',13:'Bubble',16:'Bite'}
wartortleMovesByLevel = {1:'Tackle',4:'Tail Whip',7:'Water Gun',10:'Withdraw',13:'Bubble',16:'Bite'}
blastoiseMovesByLevel = {1:'Tackle',4:'Tail Whip',7:'Water Gun',10:'Withdraw',13:'Bubble',16:'Bite'}
geodudeMovesByLevel = {1:'Tackle',2:'Defense Curl',4:'Rock Polish',12:'Magnitude',16:'Rock Throw'}
onixMovesByLevel = {1:'Tackle',2:'Defense Curl',400:'Mud Sport',6:'Rock Polish',1000:'Rollout',12:'Magnitude',16:'Rock Throw'}

geodudeMoves = {'Move One':'Tackle', 'Move Two':'Harden', 'Move Three':'Rock Polish', 'Move Four':'Magnitude'}
onixMoves = {'Move One':'Tackle', 'Move Two':'Harden', 'Move Three':'Rock Tomb', 'Move Four':'Rock Throw'}
#{'Move One':'', 'Move Two':'', 'Move Three':'', 'Move Four':''}

pokemonStats = {'Bulbasaur':bulbasaurBaseStats,'Ivysaur':ivysaurBaseStats,'Venusaur':venusaurBaseStats,'Charmander':charmanderBaseStats,'Charmeleon':charmeleonBaseStats,'Charizard':charizardBaseStats,'Squirtle':squirtleBaseStats,'Wartortle':wartortleBaseStats,'Blastoise':blastoiseBaseStats,'Geodude':geodudeBaseStats,'Onix':onixBaseStats}
pokemonTypes = {'Bulbasaur':bulbasaurType,'Ivysaur':ivysaurType,'Venusaur':venusaurType,'Charmander':charmanderType,'Charmeleon':charmeleonType,'Charizard':charizardType,'Squirtle':squirtleType,'Wartortle':wartortleType,'Blastoise':blastoiseType,'Geodude':geodudeType,'Onix':onixType}
pokemonMovesByLevel = {'Bulbasaur':bulbasaurMovesByLevel,'Ivysaur':ivysaurMovesByLevel,'Venusaur':venusaurMovesByLevel,'Charmander':charmanderMovesByLevel,'Charmeleon':charmeleonMovesByLevel,'Charizard':charizardMovesByLevel,'Squirtle':squirtleMovesByLevel,'Wartortle':wartortleMovesByLevel,'Blastoise':blastoiseMovesByLevel,'Geodude':geodudeMovesByLevel,'Onix':onixMovesByLevel}

pokemonExpGroup = {'Bulbasaur':bulbasaurExpGroup,'Ivysaur':ivysaurExpGroup,'Venusaur':venusaurExpGroup,'Charmander':charmanderExpGroup,'Charmeleon':charmeleonExpGroup,'Charizard':charizardExpGroup,'Squirtle':squirtleExpGroup,'Wartortle':wartortleExpGroup,'Blastoise':blastoiseExpGroup,'Geodude':geodudeExpGroup,'Onix':onixExpGroup}
pokemonEvolutionDetails = {'Bulbasaur':bulbasaurEvolution,'Ivysaur':ivysaurEvolution,'Venusaur':venusaurEvolution,'Charmander':charmanderEvolution,'Charmeleon':charmeleonEvolution,'Charizard':charizardEvolution,'Squirtle':squirtleEvolution,'Wartortle':wartortleEvolution,'Blastoise':blastoiseEvolution,'Geodude':geodudeEvolution,'Onix':onixEvolution}
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
leechSeedInfo = {'Base Damage':0, 'Move Type':'Grass', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}

growlExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
tailWhipExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
emberExtraInfo = {'Stat Change':'None', 'Non-Volatile Status Change':'Yes', 'Volatile Status Change':'No'}
defenseCurlExtraInfo = {'Stat Change':'Self', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
hardenExtraInfo = {'Stat Change':'Self', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
rockPolishExtraInfo = {'Stat Change':'Self', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
rockTombExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
leechSeedExtraInfo = {'Stat Change':'None', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'Yes'}

growlStatChangeInfo = {'HP':0,'Atk':-1,'Def':0,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
defenseCurlStatChangeInfo = {'HP':0,'Atk':0,'Def':1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
tailWhipStatChangeInfo = {'HP':0,'Atk':0,'Def':-1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
hardenStatChangeInfo = {'HP':0,'Atk':0,'Def':1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
rockPolishStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':2,'Accuracy':0,'Chance':100}
rockTombStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':-1,'Accuracy':0,'Chance':100}

emberNonVolatileStatusChangeInfo = {'Type':1,'Chance':10}

leechSeedVolatileStatusChangeInfo = {'Type':1,'Chance':100}

normalEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':1, 'Ghost':0, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
fightingEffect = {'Normal':2, 'Fighting':1, 'Flying':0.5, 'Poison':0.5, 'Ground':1, 'Rock':2, 'Bug':0.5, 'Ghost':0, 'Steel':2, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':0.5, 'Ice':2, 'Dragon':1, 'Dark':2, 'Fairy':0.5, 'Null':1}
flyingEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':2, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':2, 'Electric':0.5, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
poisonEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':0.5, 'Ground':0.5, 'Rock':0.5, 'Bug':1, 'Ghost':0.5, 'Steel':0, 'Fire':1, 'Water':1, 'Grass':2, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':2, 'Null':1}
groundEffect = {'Normal':1, 'Fighting':1, 'Flying':0, 'Poison':2, 'Ground':1, 'Rock':2, 'Bug':0.5, 'Ghost':1, 'Steel':2, 'Fire':2, 'Water':1, 'Grass':0.5, 'Electric':2, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
rockEffect = {'Normal':1, 'Fighting':0.5, 'Flying':2, 'Poison':1, 'Ground':0.5, 'Rock':1, 'Bug':2, 'Ghost':1, 'Steel':0.5, 'Fire':2, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':2, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
bugEffect = {'Normal':1, 'Fighting':0.5, 'Flying':0.5, 'Poison':0.5, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':0.5, 'Steel':0.5, 'Fire':0.5, 'Water':1, 'Grass':2, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':2, 'Fairy':0.5, 'Null':1}
ghostEffect = {'Normal':0, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':2, 'Steel':1, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':0.5, 'Fairy':1, 'Null':1}
steelEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':2, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':0.5, 'Grass':1, 'Electric':0.5, 'Psychic':1, 'Ice':2, 'Dragon':1, 'Dark':1, 'Fairy':2, 'Null':1}
fireEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':2, 'Ghost':1, 'Steel':2, 'Fire':0.5, 'Water':0.5, 'Grass':2, 'Electric':1, 'Psychic':1, 'Ice':2, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
waterEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':2, 'Rock':2, 'Bug':1, 'Ghost':1, 'Steel':1, 'Fire':2, 'Water':0.5, 'Grass':0.5, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
grassEffect = {'Normal':1, 'Fighting':1, 'Flying':0.5, 'Poison':0.5, 'Ground':2, 'Rock':2, 'Bug':0.5, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':2, 'Grass':0.5, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
electricEffect = {'Normal':1, 'Fighting':1, 'Flying':2, 'Poison':1, 'Ground':0, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':1, 'Fire':1, 'Water':2, 'Grass':0.5, 'Electric':0.5, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
psychicEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':2, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':0.5, 'Ice':1, 'Dragon':1, 'Dark':0, 'Fairy':1, 'Null':1}
iceEffect = {'Normal':1, 'Fighting':1, 'Flying':2, 'Poison':1, 'Ground':2, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':0.5, 'Grass':2, 'Electric':1, 'Psychic':1, 'Ice':0.5, 'Dragon':2, 'Dark':1, 'Fairy':1, 'Null':1}
dragonEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':2, 'Dark':1, 'Fairy':0, 'Null':1}
darkEffect = {'Normal':1, 'Fighting':0.5, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':2, 'Steel':1, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':0.5, 'Fairy':0.5, 'Null':1}
fairyEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':0.5, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':2, 'Dark':2, 'Fairy':1, 'Null':1}
allType = {'Normal':normalEffect, 'Fighting':fightingEffect, 'Flying':flyingEffect, 'Poison':poisonEffect, 'Ground':groundEffect, 'Rock':rockEffect, 'Bug':bugEffect, 'Ghost':ghostEffect, 'Steel':steelEffect, 'Fire':fireEffect, 'Water':waterEffect, 'Grass':grassEffect, 'Electric':electricEffect, 'Psychic':psychicEffect, 'Ice':iceEffect, 'Dragon':dragonEffect, 'Dark':darkEffect, 'Fairy':fairyEffect}

moveInfo = {'Tackle':tackleInfo,'Ember':emberInfo,'Bubble':bubbleInfo,'Vine Whip':vineWhipInfo,'Growl':growlInfo,'Defense Curl':defenseCurlInfo,'Scratch':scratchInfo,'Tail Whip':tailWhipInfo,'Flamethrower':flamethrowerInfo,'Hydro Pump':hydroPumpInfo,'Petal Blizzard':petalBlizzardInfo,'Harden':hardenInfo,'Rock Tomb':rockTombInfo,'Rock Throw':rockThrowInfo,'Rock Polish':rockPolishInfo,'Magnitude':magnitudeInfo,'Leech Seed':leechSeedInfo}
moveExtraInfo = {'Ember':emberExtraInfo,'Growl':growlExtraInfo,'Defense Curl':defenseCurlExtraInfo,'Tail Whip':tailWhipExtraInfo,'Harden':hardenExtraInfo,'Rock Polish':rockPolishExtraInfo,'Rock Tomb':rockTombExtraInfo,'Leech Seed':leechSeedExtraInfo}
moveStatChangeInfo = {'Growl':growlStatChangeInfo,'Defense Curl':defenseCurlStatChangeInfo,'Tail Whip':tailWhipStatChangeInfo,'Harden':hardenStatChangeInfo,'Rock Polish':rockPolishStatChangeInfo,'Rock Tomb':rockTombStatChangeInfo}
moveNonVolatileStatusChangeInfo = {'Ember':emberNonVolatileStatusChangeInfo}
moveVolatileStatusChangeInfo = {'Leech Seed':leechSeedVolatileStatusChangeInfo}

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

def getPokemonMovesByLevel(pokemon):
	movesByLevel = pokemonMovesByLevel[pokemon]
	return movesByLevel

def getRandomIV():
	IV = []
	for _ in range(6):
		x = randint(1,31)
		IV.append(x)
	return IV

def getMoveSet(pokemon,level):
	allMoves = []
	pokemonMovesByLevel = getPokemonMovesByLevel(pokemon)
	for i in range(1,level+1):
		if i in pokemonMovesByLevel:
			allMoves.append(pokemonMovesByLevel[i])
	if len(allMoves) <= 4:
		return allMoves
	moveSet = random.sample(allMoves,4)
	return moveSet

def getRandomMoveFromSet(pokemon,level):
	moveSet = getMoveSet(pokemon,level)
	movesetSize = len(moveSet)
	moveNumber = randint(1,movesetSize) - 1
	moveList = moveSet[moveNumber]
	move = moveList(0)
	return move

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

def gethpStat(pokemon,level,iv):
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
	statusType = getNonVolatileStatusType(status)
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

def getStatChangeWording(myPokemon,statChange):
	for i in range(7):
		if i == 0:
			stat = 'HP'
		if i == 1:
			stat = 'attack'
		if i == 2:
			stat = 'defense'
		if i == 3:
			stat = 'special attack'
		if i == 4:
			stat = 'special defense'
		if i == 5:
			stat = 'speed'
		if i == 6:
			stat = 'accuracy'
		changeForStat = statChange[i]
		if changeForStat == 1:
			print(myPokemon + '\'s', stat, 'raised!')
		if changeForStat == 2:
			print(myPokemon + '\'s', stat, 'raised greatly!')
		if changeForStat >= 3:
			print(myPokemon + '\'s', stat, 'raised hugely!')
		if changeForStat == -1:
			print(myPokemon + '\'s', stat, 'fell!')
		if changeForStat == -2:
			print(myPokemon + '\'s', stat, 'fell greatly!')
		if changeForStat <= -3:
			print(myPokemon + '\'s', stat, 'fell hugely!')

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

def getNonVolatileStatusChange(move):
	statusChange = moveExtraInfo[move]
	return statusChange['Non-Volatile Status Change']

def getNonVolatileStatusChangeType(move):
	statusChangeType = moveNonVolatileStatusChangeInfo[move]
	return statusChangeType['Type']

def getNonVolatileStatusChangeChance(move):
	statusChangeChance = moveNonVolatileStatusChangeInfo[move]
	return statusChangeChance['Chance']

def getVolatileStatusChange(move):
	statusChange = moveExtraInfo[move]
	return statusChange['Volatile Status Change']

def getVolatileStatusChangeType(move):
	statusChangeType = moveVolatileStatusChangeInfo[move]
	return statusChangeType['Type']

def getVolatileStatusChangeChance(move):
	statusChangeChance = moveVolatileStatusChangeInfo[move]
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

def getExpGroup(pokemon):
	expInfo = pokemonExpGroup[pokemon]
	expGroup = expInfo['Exp Group']
	return expGroup

def getExpYield(pokemon,level):
	expInfo = pokemonExpGroup[pokemon]
	expYieldBase = expInfo['Exp Yield']
	expYield = expYieldBase * level
	return expYield

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
	if expGroup == 'MediumFast':
		exp = n**3
	if expGroup == 'MediumSlow':
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

def getPokemonEvolve(pokemon,level):
	pokemonEvolutionInfo = pokemonEvolutionDetails[pokemon]
	pokemonEvolve = pokemonEvolutionInfo['Evolve']
	if pokemonEvolve == 'No':
		return pokemonEvolve
	pokemonEvolveLevel = pokemonEvolutionInfo['Level']
	if pokemonEvolveLevel <= level:
		pokemonEvolution = pokemonEvolutionInfo['Pokemon']
		return pokemonEvolution
	if pokemonEvolveLevel > level:
		return 'No'

def getMoveDamage(move,atkPokemon,atkLevel,atkIV,atkStatStage,atkStatus,defPokemon,defLevel,defIV,defStatStage):
	moveBaseDamage = getMoveBaseDamage(move)
	effectiveness = getEffectiveness(move,defPokemon)
	stabBonus = getStabBonus(move,atkPokemon)
	moveVariety = getMoveVariety(move)
	statusType = getNonVolatileStatusType(atkStatus)
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

def getNonVolatileStatusType(i):
	StatusType = nonVolatileStatusNumberToType[i]
	return StatusType

def getPostMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP,myMaxHP):
	myPokemonNVStatusType = getNonVolatileStatusType(myPokemonNVStatus)
	if myPokemonNVStatusType != 'Nothing':
		if myPokemonNVStatusType == 'Burned':
			burnDamage = int(myMaxHP / 16)
			myPokemonHP = (myPokemonHP - burnDamage)
			print(myPokemon, 'took', burnDamage, 'HP damage due to it\'s burn! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
			return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP]
		elif myPokemonNonVolatileStatusType == 'Poisoned':
			poisonDamage = int(myMaxHP / 8)
			myPokemonHP = (myPokemonHP - poisonDamage)
			print(myPokemon, 'took', poisonDamage, 'HP damage due to being poisoned! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
			return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP]
		elif myPokemonNonVolatileStatusType == 'Toxic':
			myPokemonStatusCount = myPokemonStatusCount + 1
			toxicDamage = int(myMaxHP * myPokemonStatusCount / 16)
			myPokemonHP = myPokemonHP - toxicDamage
			print(myPokemon, 'took', toxicDamage, 'HP damage due to being badly poisoned! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
			return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP]
	return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP]

def getPreMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount):
	myPokemonNVStatusType = getNonVolatileStatusType(myPokemonNVStatus)
	if myPokemonNVStatusType != 'Nothing':
		if myPokemonNVStatusType == 'Paralyzed':
			print(myPokemon, 'is paralyzed and may not be able to move!')
			i = randint(1,4)
			if i == 1:
				print(myPokemon, 'couldn\'t move!')
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,1]	
		elif myPokemonNonVolatileStatusType == 'Sleep':
			print(myPokemon, 'is sleeping!')
			myPokemonNVStatusCount = myPokemonNVStatusCount - 1
			if myPokemonNVStatusCount > 0:
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,1]	
			myPokemonNVStatusType = 0
			print(myPokemon, 'woke up!')
			return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,0]
		elif myPokemonNonVolatileStatusType == 'Frozen':
			i = randint(1,5)
			if i == 1:
				myPokemonStatus = 0
				print(myPokemon, 'thawed out!')
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,0]
			else:
				print(myPokemon, 'is frozen and couldn\'t move!')
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,1]	
	return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,0]	

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

def startMyTurn(move,myInformation,enemyInformation,environmentInformation):

	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	enemyTeam = enemyInformation[0];enemyBag = enemyInformation[1];enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0];enemyPokemonName = enemyPokemonInfo[1];enemyPokemonLevel = enemyPokemonInfo[2];enemyPokemonIV = enemyPokemonInfo[3];enemyPokemonEV = enemyPokemonInfo[4];enemyPokemonHP = enemyPokemonInfo[5];enemyPokemonExperience = enemyPokemonInfo[6];enemyPokemonForm = enemyPokemonInfo[7];enemyPokemonGender = enemyPokemonInfo[8];enemyPokemonAbility = enemyPokemonInfo[9];enemyPokemonTypeOne = enemyPokemonInfo[10];enemyPokemonTypeTwo = enemyPokemonInfo[11];enemyPokemonItem = enemyPokemonInfo[12];enemyPokemonMoveSet = enemyPokemonInfo[13];enemyPokemonMovePP = enemyPokemonInfo[14];enemyPokemonNVStatus = enemyPokemonInfo[15];enemyPokemonNVStatusCount = enemyPokemonInfo[16];enemyPokemonVStatus = enemyPokemonInfo[17];enemyPokemonVStatusCount = enemyPokemonInfo[18];enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0]; enemyWording = enemyPlayer[1]
	enemyMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV); myMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV)					
	preMoveNVStatusCheck = getPreMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount)
	myPokemonInfo[15]=preMoveNVStatusCheck[1];myPokemonInfo[16]=preMoveNVStatusCheck[2];interrupt=preMoveNVStatusCheck[3]
	if interrupt == 0:
		#preMoveVStatusCheck = getPreMoveVStatusCheck(myPokemon,myPokemonVStatus,myPokemonVStatusCount)
		#myPokemonInfo[17]=preMoveVStatusCheck[1],myPokemonInfo[16]=preMoveVStatusCheck[2],interrupt=preMoveVStatusCheck[3]
		if interrupt == 0:
			hitOrMiss = getHitOrMiss(move)
			if hitOrMiss == 'Miss':
				print(myPokemon, 'used', move, 'but it missed!')
				interrupt = 1
			if interrupt == 0:
				moveVariety = getMoveVariety(move)
				if moveVariety == 'Support':
					moveExtraForm = getMoveExtraForm(move)
					if moveExtraForm == 'Enemy':
						statChange = getStatChange(move)
						enemyPokemonStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
						enemyPokemonInfo[19]=enemyPokemonCurrentStatStage
						print(myPokemon, 'used', move, 'against the', enemyWording, enemyPokemon + '!')
						statChangeWording = getStatChangeWording(enemyPokemon,statChange)
					elif moveExtraForm == 'Self':
						statChange = getStatChange(move)
						myPokemonCurrentStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
						myPokemonInfo[19]=myPokemonCurrentStatStage
						print('Your', myPokemon, 'used', move + '!')
						statChangeWording = getStatChangeWording(myPokemon,statChange)
					
					elif moveExtraForm == 'None':
						nonVolatileStatus = getNonVolatileStatusChange(move)
						if nonVolatileStatus == 'Yes':
							nonVolatileStatusType = getNonVolatileStatusType(move)
							nonVolatileStatusChangeChance = getNonVolatileStatusChangeChance(move)
				if moveVariety == 'Physical' or moveVariety == 'Special':
					moveDamage = getMoveDamage(move,myPokemon,myPokemonLevel,myPokemonIV,myPokemonCurrentStatStage,myPokemonNVStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonCurrentStatStage)
					effectiveness = getEffectiveness(move,enemyPokemon); effectivenessWording = getEffectivesnessWording(effectiveness)

					enemyPokemonHP = enemyPokemonHP - moveDamage 
					
					if enemyPokemonHP < 0:
						enemyPokemonHP = 0

					enemyPokemonInfo[5] = enemyPokemonHP	

					print(myPokemon, 'used', move, 'against the', enemyWording, enemyPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', enemyPokemon, 'has', enemyPokemonHP, '/', enemyMaxHP, 'HP remaining!')
					moveExtra = getMoveExtra(move)
					if moveExtra == 'Yes':		
						moveExtraForm = getMoveExtraForm(move)
						if moveExtraForm == 'Enemy':
							statChange = getStatChange(move)
							enemyPokemonCurrentStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
							enemyPokemonInfo[19]=enemyPokemonCurrentStatStage
							statChangeWording = getStatChangeWording(enemyPokemon,statChange)

						elif moveExtraForm == 'Self':
							statChange = getStatChange(move)
							myPokemonCurrentStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
							myPokemonInfo[19]=myPokemonCurrentStatStage
							statChangeWording = getStatChangeWording(enemyPokemon,statChange)

						statusChange = getNonVolatileStatusChange(move)
						if statusChange == 'Yes':
							if enemyPokemonStatus == 0:
								statusChangeType = getNonVolatileStatusChangeType(move)
								statusChangeChance = getNonVolatileStatusChangeChance(move)
								x = randint(1,100)
								if x <= statusChangeChance:
									enemyPokemonStatus = statusChangeType
									statusType = getNonVolatileStatusType(enemyPokemonStatus)
									print(enemyPokemon, 'was', statusType + '!')
								if statusChangeType == 3:
									x = randint(1,3)	
									enemyPokemonStatusCount = x
	postMoveNVStatusCheck = getPostMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP,myMaxHP)
	myPokemonInfo[15]=preMoveNVStatusCheck[1];myPokemonInfo[16]=preMoveNVStatusCheck[2];myPokemonHP=preMoveNVStatusCheck[3]
	myTeam[0]=myPokemonInfo; myInformation[0]=myTeam
	enemyTeam[0]=enemyPokemonInfo; enemyInformation[0]=enemyTeam
	return [myInformation,enemyInformation,environmentInformation]


def startEnemyTurn(move,myInformation,enemyInformation,environmentInformation):
	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	enemyTeam = enemyInformation[0];enemyBag = enemyInformation[1];enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0];enemyPokemonName = enemyPokemonInfo[1];enemyPokemonLevel = enemyPokemonInfo[2];enemyPokemonIV = enemyPokemonInfo[3];enemyPokemonEV = enemyPokemonInfo[4];enemyPokemonHP = enemyPokemonInfo[5];enemyPokemonExperience = enemyPokemonInfo[6];enemyPokemonForm = enemyPokemonInfo[7];enemyPokemonGender = enemyPokemonInfo[8];enemyPokemonAbility = enemyPokemonInfo[9];enemyPokemonTypeOne = enemyPokemonInfo[10];enemyPokemonTypeTwo = enemyPokemonInfo[11];enemyPokemonItem = enemyPokemonInfo[12];enemyPokemonMoveSet = enemyPokemonInfo[13];enemyPokemonMovePP = enemyPokemonInfo[14];enemyPokemonNVStatus = enemyPokemonInfo[15];enemyPokemonNVStatusCount = enemyPokemonInfo[16];enemyPokemonVStatus = enemyPokemonInfo[17];enemyPokemonVStatusCount = enemyPokemonInfo[18];enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0]; enemyWording = enemyPlayer[1]
	enemyMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV); myMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV)					
	#Check for Non-Volatile Status
	preMoveNVStatusCheck = getPreMoveNVStatusCheck(enemyPokemon,enemyPokemonNVStatus,enemyPokemonNVStatusCount)
	enemyPokemonInfo[15]=preMoveNVStatusCheck[1];enemyPokemonInfo[16]=preMoveNVStatusCheck[2];interrupt=preMoveNVStatusCheck[3]
	if interrupt == 0:
		#preMoveVStatusCheck = getPreMoveVStatusCheck(myPokemon,myPokemonVStatus,myPokemonVStatusCount)
		#myPokemonInfo[17]=preMoveVStatusCheck[1],myPokemonInfo[16]=preMoveVStatusCheck[2],interrupt=preMoveVStatusCheck[3]
		if interrupt == 0:
			hitOrMiss = getHitOrMiss(move)
			if hitOrMiss == 'Miss':
				print('The', enemyWording, enemyPokemon, 'used', move, 'but it missed!')
				interrupt = 0
			if interrupt == 0:
				moveVariety = getMoveVariety(move)
				if moveVariety == 'Support':
					moveExtraForm = getMoveExtraForm(move)
					if moveExtraForm == 'Enemy':
						statChange = getStatChange(move)
						myPokemonCurrentStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
						myPokemonInfo[19]=myPokemonCurrentStatStage
						print(enemyPokemon, 'used', move, 'against the', myPokemon + '!')
						StatChangeWording = getStatChangeWording(myPokemon,statChange)					
					elif moveExtraForm == 'Self':
						statChange = getStatChange(move)
						enemyPokemonCurrentStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
						enemyPokemonInfo[19]=enemyPokemonCurrentStatStage
						print('The', enemyWording, enemyPokemon, 'used', move + '!')
						StatChangeWording = getStatChangeWording(enemyPokemon,statChange)
					elif moveExtraForm == 'None':
						nonVolatileStatus = getNonVolatileStatusChange(move)
						if nonVolatileStatus == 'Yes':
							nonVolatileStatusType = getNonVolatileStatusType(move)
							nonVolatileStatusChangeChance = getNonVolatileStatusChangeChance(move)
				if moveVariety == 'Physical' or moveVariety == 'Special':
					moveDamage = getMoveDamage(move,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonCurrentStatStage,enemyPokemonNVStatus,myPokemon,myPokemonLevel,myPokemonIV,myPokemonCurrentStatStage)
					effectiveness = getEffectiveness(move,myPokemon); effectivenessWording = getEffectivesnessWording(effectiveness)
					myPokemonHP = myPokemonHP - moveDamage
					if myPokemonHP < 0:
						myPokemonHP = 0
					myPokemonInfo[5] = myPokemonHP
					print('The', enemyWording, enemyPokemon, 'used', move, 'against', myPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', myPokemon, 'has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
					moveExtra = getMoveExtra(move)
					if moveExtra == 'Yes':		
						moveExtraForm = getMoveExtraForm(move)
						if moveExtraForm == 'Enemy':
							statChange = getStatChange(move)
							myPokemonCurrentStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
							StatChangeWording = getStatChangeWording(myPokemon,statChange)
						elif moveExtraForm == 'Self':
							statChange = getStatChange(move)
							enemyPokemonCurrentStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
							StatChangeWording = getStatChangeWording(enemyPokemon,statChange)
						statusChange = getNonVolatileStatusChange(move)
						if statusChange == 'Yes':
							if myPokemonStatus == 0:
								statusChangeType = getNonVolatileStatusChangeType(move)
								statusChangeChance = getNonVolatileStatusChangeChance(move)
								x = randint(1,100)
								if x <= statusChangeChance:
									myPokemonStatus = statusChangeType
									statusType = getNonVolatileStatusType(myPokemonStatus)
									print(myPokemon, 'was', statusType + '!')
									myPokemonInfo[15]=statusChangeType; myPokemonInfo[16]=0
								if statusChangeType == 3:
									x = randint(1,3)	
									myPokemonInfo[16]=x
	postMoveNVStatusCheck = getPostMoveNVStatusCheck(enemyPokemon,enemyPokemonNVStatus,enemyPokemonNVStatusCount,enemyPokemonHP,enemyMaxHP)
	enemyPokemonInfo[15]=preMoveNVStatusCheck[1];enemyPokemonInfo[16]=preMoveNVStatusCheck[2];enemyPokemonHP=preMoveNVStatusCheck[3]
	myTeam[0]=myPokemonInfo; myInformation[0]=myTeam
	enemyTeam[0]=enemyPokemonInfo; enemyInformation[0]=enemyTeam
	return [myInformation,enemyInformation,environmentInformation]

def getMoveInput(pokemonMoveSet):
	movesetSize = len(pokemonMoveSet)
	while True:
		try:
			moveInput = input('-- ')
			if moveInput in pokemonMoveSet:
				return moveInput
				break			
			moveInput
			if int(moveInput) <= movesetSize and int(moveInput) > 0:
				return pokemonMoveSet[int(moveInput)-1]
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

def getRandomSwitchPokemon(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0];myPokemonOneName = myPokemonOneInfo[1];myPokemonOneLevel = myPokemonOneInfo[2];myPokemonOneIV = myPokemonOneInfo[3];myPokemonOneEV = myPokemonOneInfo[4];myPokemonOneHP = myPokemonOneInfo[5];myPokemonOneExperience = myPokemonOneInfo[6];myPokemonOneForm = myPokemonOneInfo[7];myPokemonOneGender = myPokemonOneInfo[8];myPokemonOneAbility = myPokemonOneInfo[9];myPokemonOneTypeOne = myPokemonOneInfo[10];myPokemonOneTypeTwo = myPokemonOneInfo[11];myPokemonOneItem = myPokemonOneInfo[12];myPokemonOneMoveSet = myPokemonOneInfo[13];myPokemonOneMovePP = myPokemonOneInfo[14];myPokemonOneNVStatus = myPokemonOneInfo[15];myPokemonOneNVStatusCount = myPokemonOneInfo[16];myPokemonOneVStatus = myPokemonOneInfo[17];myPokemonOneVStatusCount = myPokemonOneInfo[18];myPokemonOneCurrentStatStage = myPokemonOneInfo[19];myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0];myPokemonTwoName = myPokemonTwoInfo[1];myPokemonTwoLevel = myPokemonTwoInfo[2];myPokemonTwoIV = myPokemonTwoInfo[3];myPokemonTwoEV = myPokemonTwoInfo[4];myPokemonTwoHP = myPokemonTwoInfo[5];myPokemonTwoExperience = myPokemonTwoInfo[6];myPokemonTwoForm = myPokemonTwoInfo[7];myPokemonTwoGender = myPokemonTwoInfo[8];myPokemonTwoAbility = myPokemonTwoInfo[9];myPokemonTwoTypeOne = myPokemonTwoInfo[10];myPokemonTwoTypeTwo = myPokemonTwoInfo[11];myPokemonTwoItem = myPokemonTwoInfo[12];myPokemonTwoMoveSet = myPokemonTwoInfo[13];myPokemonTwoMovePP = myPokemonTwoInfo[14];myPokemonTwoNVStatus = myPokemonTwoInfo[15];myPokemonTwoNVStatusCount = myPokemonTwoInfo[16];myPokemonTwoVStatus = myPokemonTwoInfo[17];myPokemonTwoVStatusCount = myPokemonTwoInfo[18];myPokemonTwoCurrentStatStage = myPokemonTwoInfo[19];myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV)
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0];myPokemonThreeName = myPokemonThreeInfo[1];myPokemonThreeLevel = myPokemonThreeInfo[2];myPokemonThreeIV = myPokemonThreeInfo[3];myPokemonThreeEV = myPokemonThreeInfo[4];myPokemonThreeHP = myPokemonThreeInfo[5];myPokemonThreeExperience = myPokemonThreeInfo[6];myPokemonThreeForm = myPokemonThreeInfo[7];myPokemonThreeGender = myPokemonThreeInfo[8];myPokemonThreeAbility = myPokemonThreeInfo[9];myPokemonThreeTypeOne = myPokemonThreeInfo[10];myPokemonThreeTypeTwo = myPokemonThreeInfo[11];myPokemonThreeItem = myPokemonThreeInfo[12];myPokemonThreeMoveSet = myPokemonThreeInfo[13];myPokemonThreeMovePP = myPokemonThreeInfo[14];myPokemonThreeNVStatus = myPokemonThreeInfo[15];myPokemonThreeNVStatusCount = myPokemonThreeInfo[16];myPokemonThreeVStatus = myPokemonThreeInfo[17];myPokemonThreeVStatusCount = myPokemonThreeInfo[18];myPokemonThreeCurrentStatStage = myPokemonThreeInfo[19];myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV)
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0];myPokemonFourName = myPokemonFourInfo[1];myPokemonFourLevel = myPokemonFourInfo[2];myPokemonFourIV = myPokemonFourInfo[3];myPokemonFourEV = myPokemonFourInfo[4];myPokemonFourHP = myPokemonFourInfo[5];myPokemonFourExperience = myPokemonFourInfo[6];myPokemonFourForm = myPokemonFourInfo[7];myPokemonFourGender = myPokemonFourInfo[8];myPokemonFourAbility = myPokemonFourInfo[9];myPokemonFourTypeOne = myPokemonFourInfo[10];myPokemonFourTypeTwo = myPokemonFourInfo[11];myPokemonFourItem = myPokemonFourInfo[12];myPokemonFourMoveSet = myPokemonFourInfo[13];myPokemonFourMovePP = myPokemonFourInfo[14];myPokemonFourNVStatus = myPokemonFourInfo[15];myPokemonFourNVStatusCount = myPokemonFourInfo[16];myPokemonFourVStatus = myPokemonFourInfo[17];myPokemonFourVStatusCount = myPokemonFourInfo[18];myPokemonFourCurrentStatStage = myPokemonFourInfo[19];myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV)
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0];myPokemonFiveName = myPokemonFiveInfo[1];myPokemonFiveLevel = myPokemonFiveInfo[2];myPokemonFiveIV = myPokemonFiveInfo[3];myPokemonFiveEV = myPokemonFiveInfo[4];myPokemonFiveHP = myPokemonFiveInfo[5];myPokemonFiveExperience = myPokemonFiveInfo[6];myPokemonFiveForm = myPokemonFiveInfo[7];myPokemonFiveGender = myPokemonFiveInfo[8];myPokemonFiveAbility = myPokemonFiveInfo[9];myPokemonFiveTypeOne = myPokemonFiveInfo[10];myPokemonFiveTypeTwo = myPokemonFiveInfo[11];myPokemonFiveItem = myPokemonFiveInfo[12];myPokemonFiveMoveSet = myPokemonFiveInfo[13];myPokemonFiveMovePP = myPokemonFiveInfo[14];myPokemonFiveNVStatus = myPokemonFiveInfo[15];myPokemonFiveNVStatusCount = myPokemonFiveInfo[16];myPokemonFiveVStatus = myPokemonFiveInfo[17];myPokemonFiveVStatusCount = myPokemonFiveInfo[18];myPokemonFiveCurrentStatStage = myPokemonFiveInfo[19];myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV)
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0];myPokemonSixName = myPokemonSixInfo[1];myPokemonSixLevel = myPokemonSixInfo[2];myPokemonSixIV = myPokemonSixInfo[3];myPokemonSixEV = myPokemonSixInfo[4];myPokemonSixHP = myPokemonSixInfo[5];myPokemonSixExperience = myPokemonSixInfo[6];myPokemonSixForm = myPokemonSixInfo[7];myPokemonSixGender = myPokemonSixInfo[8];myPokemonSixAbility = myPokemonSixInfo[9];myPokemonSixTypeOne = myPokemonSixInfo[10];myPokemonSixTypeTwo = myPokemonSixInfo[11];myPokemonSixItem = myPokemonSixInfo[12];myPokemonSixMoveSet = myPokemonSixInfo[13];myPokemonSixMovePP = myPokemonSixInfo[14];myPokemonSixNVStatus = myPokemonSixInfo[15];myPokemonSixNVStatusCount = myPokemonSixInfo[16];myPokemonSixVStatus = myPokemonSixInfo[17];myPokemonSixVStatusCount = myPokemonSixInfo[18];myPokemonSixCurrentStatStage = myPokemonSixInfo[19];myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV)
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

def getTeamTotalHP(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0];myPokemonOneName = myPokemonOneInfo[1];myPokemonOneLevel = myPokemonOneInfo[2];myPokemonOneIV = myPokemonOneInfo[3];myPokemonOneEV = myPokemonOneInfo[4];myPokemonOneHP = myPokemonOneInfo[5];myPokemonOneExperience = myPokemonOneInfo[6];myPokemonOneForm = myPokemonOneInfo[7];myPokemonOneGender = myPokemonOneInfo[8];myPokemonOneAbility = myPokemonOneInfo[9];myPokemonOneTypeOne = myPokemonOneInfo[10];myPokemonOneTypeTwo = myPokemonOneInfo[11];myPokemonOneItem = myPokemonOneInfo[12];myPokemonOneMoveSet = myPokemonOneInfo[13];myPokemonOneMovePP = myPokemonOneInfo[14];myPokemonOneNVStatus = myPokemonOneInfo[15];myPokemonOneNVStatusCount = myPokemonOneInfo[16];myPokemonOneVStatus = myPokemonOneInfo[17];myPokemonOneVStatusCount = myPokemonOneInfo[18];myPokemonOneCurrentStatStage = myPokemonOneInfo[19];myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
		myTeamTotalHP = myPokemonOneHP
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0];myPokemonTwoName = myPokemonTwoInfo[1];myPokemonTwoLevel = myPokemonTwoInfo[2];myPokemonTwoIV = myPokemonTwoInfo[3];myPokemonTwoEV = myPokemonTwoInfo[4];myPokemonTwoHP = myPokemonTwoInfo[5];myPokemonTwoExperience = myPokemonTwoInfo[6];myPokemonTwoForm = myPokemonTwoInfo[7];myPokemonTwoGender = myPokemonTwoInfo[8];myPokemonTwoAbility = myPokemonTwoInfo[9];myPokemonTwoTypeOne = myPokemonTwoInfo[10];myPokemonTwoTypeTwo = myPokemonTwoInfo[11];myPokemonTwoItem = myPokemonTwoInfo[12];myPokemonTwoMoveSet = myPokemonTwoInfo[13];myPokemonTwoMovePP = myPokemonTwoInfo[14];myPokemonTwoNVStatus = myPokemonTwoInfo[15];myPokemonTwoNVStatusCount = myPokemonTwoInfo[16];myPokemonTwoVStatus = myPokemonTwoInfo[17];myPokemonTwoVStatusCount = myPokemonTwoInfo[18];myPokemonTwoCurrentStatStage = myPokemonTwoInfo[19];myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0];myPokemonThreeName = myPokemonThreeInfo[1];myPokemonThreeLevel = myPokemonThreeInfo[2];myPokemonThreeIV = myPokemonThreeInfo[3];myPokemonThreeEV = myPokemonThreeInfo[4];myPokemonThreeHP = myPokemonThreeInfo[5];myPokemonThreeExperience = myPokemonThreeInfo[6];myPokemonThreeForm = myPokemonThreeInfo[7];myPokemonThreeGender = myPokemonThreeInfo[8];myPokemonThreeAbility = myPokemonThreeInfo[9];myPokemonThreeTypeOne = myPokemonThreeInfo[10];myPokemonThreeTypeTwo = myPokemonThreeInfo[11];myPokemonThreeItem = myPokemonThreeInfo[12];myPokemonThreeMoveSet = myPokemonThreeInfo[13];myPokemonThreeMovePP = myPokemonThreeInfo[14];myPokemonThreeNVStatus = myPokemonThreeInfo[15];myPokemonThreeNVStatusCount = myPokemonThreeInfo[16];myPokemonThreeVStatus = myPokemonThreeInfo[17];myPokemonThreeVStatusCount = myPokemonThreeInfo[18];myPokemonThreeCurrentStatStage = myPokemonThreeInfo[19];myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0];myPokemonFourName = myPokemonFourInfo[1];myPokemonFourLevel = myPokemonFourInfo[2];myPokemonFourIV = myPokemonFourInfo[3];myPokemonFourEV = myPokemonFourInfo[4];myPokemonFourHP = myPokemonFourInfo[5];myPokemonFourExperience = myPokemonFourInfo[6];myPokemonFourForm = myPokemonFourInfo[7];myPokemonFourGender = myPokemonFourInfo[8];myPokemonFourAbility = myPokemonFourInfo[9];myPokemonFourTypeOne = myPokemonFourInfo[10];myPokemonFourTypeTwo = myPokemonFourInfo[11];myPokemonFourItem = myPokemonFourInfo[12];myPokemonFourMoveSet = myPokemonFourInfo[13];myPokemonFourMovePP = myPokemonFourInfo[14];myPokemonFourNVStatus = myPokemonFourInfo[15];myPokemonFourNVStatusCount = myPokemonFourInfo[16];myPokemonFourVStatus = myPokemonFourInfo[17];myPokemonFourVStatusCount = myPokemonFourInfo[18];myPokemonFourCurrentStatStage = myPokemonFourInfo[19];myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0];myPokemonFiveName = myPokemonFiveInfo[1];myPokemonFiveLevel = myPokemonFiveInfo[2];myPokemonFiveIV = myPokemonFiveInfo[3];myPokemonFiveEV = myPokemonFiveInfo[4];myPokemonFiveHP = myPokemonFiveInfo[5];myPokemonFiveExperience = myPokemonFiveInfo[6];myPokemonFiveForm = myPokemonFiveInfo[7];myPokemonFiveGender = myPokemonFiveInfo[8];myPokemonFiveAbility = myPokemonFiveInfo[9];myPokemonFiveTypeOne = myPokemonFiveInfo[10];myPokemonFiveTypeTwo = myPokemonFiveInfo[11];myPokemonFiveItem = myPokemonFiveInfo[12];myPokemonFiveMoveSet = myPokemonFiveInfo[13];myPokemonFiveMovePP = myPokemonFiveInfo[14];myPokemonFiveNVStatus = myPokemonFiveInfo[15];myPokemonFiveNVStatusCount = myPokemonFiveInfo[16];myPokemonFiveVStatus = myPokemonFiveInfo[17];myPokemonFiveVStatusCount = myPokemonFiveInfo[18];myPokemonFiveCurrentStatStage = myPokemonFiveInfo[19];myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP + myPokemonFiveHP
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0];myPokemonSixName = myPokemonSixInfo[1];myPokemonSixLevel = myPokemonSixInfo[2];myPokemonSixIV = myPokemonSixInfo[3];myPokemonSixEV = myPokemonSixInfo[4];myPokemonSixHP = myPokemonSixInfo[5];myPokemonSixExperience = myPokemonSixInfo[6];myPokemonSixForm = myPokemonSixInfo[7];myPokemonSixGender = myPokemonSixInfo[8];myPokemonSixAbility = myPokemonSixInfo[9];myPokemonSixTypeOne = myPokemonSixInfo[10];myPokemonSixTypeTwo = myPokemonSixInfo[11];myPokemonSixItem = myPokemonSixInfo[12];myPokemonSixMoveSet = myPokemonSixInfo[13];myPokemonSixMovePP = myPokemonSixInfo[14];myPokemonSixNVStatus = myPokemonSixInfo[15];myPokemonSixNVStatusCount = myPokemonSixInfo[16];myPokemonSixVStatus = myPokemonSixInfo[17];myPokemonSixVStatusCount = myPokemonSixInfo[18];myPokemonSixCurrentStatStage = myPokemonSixInfo[19];myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP + myPokemonFiveHP + myPokemonSixHP
	return myTeamTotalHP

def getSwitchPokemon(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0];myPokemonOneName = myPokemonOneInfo[1];myPokemonOneLevel = myPokemonOneInfo[2];myPokemonOneIV = myPokemonOneInfo[3];myPokemonOneEV = myPokemonOneInfo[4];myPokemonOneHP = myPokemonOneInfo[5];myPokemonOneExperience = myPokemonOneInfo[6];myPokemonOneForm = myPokemonOneInfo[7];myPokemonOneGender = myPokemonOneInfo[8];myPokemonOneAbility = myPokemonOneInfo[9];myPokemonOneTypeOne = myPokemonOneInfo[10];myPokemonOneTypeTwo = myPokemonOneInfo[11];myPokemonOneItem = myPokemonOneInfo[12];myPokemonOneMoveSet = myPokemonOneInfo[13];myPokemonOneMovePP = myPokemonOneInfo[14];myPokemonOneNVStatus = myPokemonOneInfo[15];myPokemonOneNVStatusCount = myPokemonOneInfo[16];myPokemonOneVStatus = myPokemonOneInfo[17];myPokemonOneVStatusCount = myPokemonOneInfo[18];myPokemonOneCurrentStatStage = myPokemonOneInfo[19];myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0];myPokemonTwoName = myPokemonTwoInfo[1];myPokemonTwoLevel = myPokemonTwoInfo[2];myPokemonTwoIV = myPokemonTwoInfo[3];myPokemonTwoEV = myPokemonTwoInfo[4];myPokemonTwoHP = myPokemonTwoInfo[5];myPokemonTwoExperience = myPokemonTwoInfo[6];myPokemonTwoForm = myPokemonTwoInfo[7];myPokemonTwoGender = myPokemonTwoInfo[8];myPokemonTwoAbility = myPokemonTwoInfo[9];myPokemonTwoTypeOne = myPokemonTwoInfo[10];myPokemonTwoTypeTwo = myPokemonTwoInfo[11];myPokemonTwoItem = myPokemonTwoInfo[12];myPokemonTwoMoveSet = myPokemonTwoInfo[13];myPokemonTwoMovePP = myPokemonTwoInfo[14];myPokemonTwoNVStatus = myPokemonTwoInfo[15];myPokemonTwoNVStatusCount = myPokemonTwoInfo[16];myPokemonTwoVStatus = myPokemonTwoInfo[17];myPokemonTwoVStatusCount = myPokemonTwoInfo[18];myPokemonTwoCurrentStatStage = myPokemonTwoInfo[19];myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV)
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0];myPokemonThreeName = myPokemonThreeInfo[1];myPokemonThreeLevel = myPokemonThreeInfo[2];myPokemonThreeIV = myPokemonThreeInfo[3];myPokemonThreeEV = myPokemonThreeInfo[4];myPokemonThreeHP = myPokemonThreeInfo[5];myPokemonThreeExperience = myPokemonThreeInfo[6];myPokemonThreeForm = myPokemonThreeInfo[7];myPokemonThreeGender = myPokemonThreeInfo[8];myPokemonThreeAbility = myPokemonThreeInfo[9];myPokemonThreeTypeOne = myPokemonThreeInfo[10];myPokemonThreeTypeTwo = myPokemonThreeInfo[11];myPokemonThreeItem = myPokemonThreeInfo[12];myPokemonThreeMoveSet = myPokemonThreeInfo[13];myPokemonThreeMovePP = myPokemonThreeInfo[14];myPokemonThreeNVStatus = myPokemonThreeInfo[15];myPokemonThreeNVStatusCount = myPokemonThreeInfo[16];myPokemonThreeVStatus = myPokemonThreeInfo[17];myPokemonThreeVStatusCount = myPokemonThreeInfo[18];myPokemonThreeCurrentStatStage = myPokemonThreeInfo[19];myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV)
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0];myPokemonFourName = myPokemonFourInfo[1];myPokemonFourLevel = myPokemonFourInfo[2];myPokemonFourIV = myPokemonFourInfo[3];myPokemonFourEV = myPokemonFourInfo[4];myPokemonFourHP = myPokemonFourInfo[5];myPokemonFourExperience = myPokemonFourInfo[6];myPokemonFourForm = myPokemonFourInfo[7];myPokemonFourGender = myPokemonFourInfo[8];myPokemonFourAbility = myPokemonFourInfo[9];myPokemonFourTypeOne = myPokemonFourInfo[10];myPokemonFourTypeTwo = myPokemonFourInfo[11];myPokemonFourItem = myPokemonFourInfo[12];myPokemonFourMoveSet = myPokemonFourInfo[13];myPokemonFourMovePP = myPokemonFourInfo[14];myPokemonFourNVStatus = myPokemonFourInfo[15];myPokemonFourNVStatusCount = myPokemonFourInfo[16];myPokemonFourVStatus = myPokemonFourInfo[17];myPokemonFourVStatusCount = myPokemonFourInfo[18];myPokemonFourCurrentStatStage = myPokemonFourInfo[19];myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV)
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0];myPokemonFiveName = myPokemonFiveInfo[1];myPokemonFiveLevel = myPokemonFiveInfo[2];myPokemonFiveIV = myPokemonFiveInfo[3];myPokemonFiveEV = myPokemonFiveInfo[4];myPokemonFiveHP = myPokemonFiveInfo[5];myPokemonFiveExperience = myPokemonFiveInfo[6];myPokemonFiveForm = myPokemonFiveInfo[7];myPokemonFiveGender = myPokemonFiveInfo[8];myPokemonFiveAbility = myPokemonFiveInfo[9];myPokemonFiveTypeOne = myPokemonFiveInfo[10];myPokemonFiveTypeTwo = myPokemonFiveInfo[11];myPokemonFiveItem = myPokemonFiveInfo[12];myPokemonFiveMoveSet = myPokemonFiveInfo[13];myPokemonFiveMovePP = myPokemonFiveInfo[14];myPokemonFiveNVStatus = myPokemonFiveInfo[15];myPokemonFiveNVStatusCount = myPokemonFiveInfo[16];myPokemonFiveVStatus = myPokemonFiveInfo[17];myPokemonFiveVStatusCount = myPokemonFiveInfo[18];myPokemonFiveCurrentStatStage = myPokemonFiveInfo[19];myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV)
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0];myPokemonSixName = myPokemonSixInfo[1];myPokemonSixLevel = myPokemonSixInfo[2];myPokemonSixIV = myPokemonSixInfo[3];myPokemonSixEV = myPokemonSixInfo[4];myPokemonSixHP = myPokemonSixInfo[5];myPokemonSixExperience = myPokemonSixInfo[6];myPokemonSixForm = myPokemonSixInfo[7];myPokemonSixGender = myPokemonSixInfo[8];myPokemonSixAbility = myPokemonSixInfo[9];myPokemonSixTypeOne = myPokemonSixInfo[10];myPokemonSixTypeTwo = myPokemonSixInfo[11];myPokemonSixItem = myPokemonSixInfo[12];myPokemonSixMoveSet = myPokemonSixInfo[13];myPokemonSixMovePP = myPokemonSixInfo[14];myPokemonSixNVStatus = myPokemonSixInfo[15];myPokemonSixNVStatusCount = myPokemonSixInfo[16];myPokemonSixVStatus = myPokemonSixInfo[17];myPokemonSixVStatusCount = myPokemonSixInfo[18];myPokemonSixCurrentStatStage = myPokemonSixInfo[19];myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV)
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

def startRound(myInformation,enemyInformation,environmentInformation):
	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	enemyTeam = enemyInformation[0];enemyBag = enemyInformation[1];enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0];enemyPokemonName = enemyPokemonInfo[1];enemyPokemonLevel = enemyPokemonInfo[2];enemyPokemonIV = enemyPokemonInfo[3];enemyPokemonEV = enemyPokemonInfo[4];enemyPokemonHP = enemyPokemonInfo[5];enemyPokemonExperience = enemyPokemonInfo[6];enemyPokemonForm = enemyPokemonInfo[7];enemyPokemonGender = enemyPokemonInfo[8];enemyPokemonAbility = enemyPokemonInfo[9];enemyPokemonTypeOne = enemyPokemonInfo[10];enemyPokemonTypeTwo = enemyPokemonInfo[11];enemyPokemonItem = enemyPokemonInfo[12];enemyPokemonMoveSet = enemyPokemonInfo[13];enemyPokemonMovePP = enemyPokemonInfo[14];enemyPokemonNVStatus = enemyPokemonInfo[15];enemyPokemonNVStatusCount = enemyPokemonInfo[16];enemyPokemonVStatus = enemyPokemonInfo[17];enemyPokemonVStatusCount = enemyPokemonInfo[18];enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0]; enemyPlayerWording = enemyPlayer[1]
	enemyMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV); myMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV)					

	print('What will you do?')
	print('Fight - Bag - Pokemon - Run')
	choiceInput = getChoiceInput()
	if choiceInput == 'Fight':
		run = [0]
		print('\nWhat will', myPokemon, 'do?')
		print(myPokemonMoveSet + ['Back'])
		myMove = getMoveInput(myPokemonMoveSet + ['Back'])
		if myMove == 'Back':
			turnOutcomeInfo = startRound(myInformation,enemyInformation,environmentInformation)

			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			return turnOutcomeInfo
		print('')
		enemyMoveList = random.sample(enemyPokemonMoveSet,1); enemyMove = enemyMoveList[0]
		turnOrder = getTurnOrder(myPokemon,myPokemonLevel,myPokemonIV,myPokemonCurrentStatStage,myPokemonNVStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonCurrentStatStage,enemyPokemonNVStatus)
		if turnOrder == 'myPokemonFirst':
			turnOutcomeInfo = startMyTurn(myMove,myInformation,enemyInformation,environmentInformation)
			
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			if enemyPokemonHP == 0 or myPokemonHP == 0:
				roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
				return roundOutcomeInfo
			turnOutcomeInfo = startEnemyTurn(enemyMove,myInformation,enemyInformation,environmentInformation)

			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]

			roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation,run]
			return roundOutcomeInfo
		if turnOrder == 'enemyPokemonFirst':
			turnOutcomeInfo = startEnemyTurn(enemyMove,myInformation,enemyInformation,environmentInformation)
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			if myPokemonHP == 0 or enemyPokemonHP == 0:
				roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
				return roundOutcomeInfo
			turnOutcomeInfo = startMyTurn(myMove,myInformation,enemyInformation,environmentInformation)
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
			return roundOutcomeInfo
	if choiceInput == 'Run':
		run = [1]
		roundOutcomeInfo = [myTeam,enemyTeam,run]
		return roundOutcomeInfo
	if choiceInput == 'Bag':
		print('Nothing in your bag!')
		run = [0]
		enemyMoveList = random.sample(enemyPokemonMoveSet,1); enemyMove = enemyMoveList[0]
		turnOutcomeInfo = startEnemyTurn(enemyMove,myInformation,enemyInformation,environmentInformation)
		myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]
		enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
		roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
		return roundOutcomeInfo
	if choiceInput == 'Pokemon':
		run = [0]
		oldPokemon = myPokemon
		changePokemon = getSwitchPokemon(myTeam)
		myTeam = changePokemon[0]; change = changePokemon[1]
		if change == 0:
			roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
			return roundOutcomeInfo
		myPokemonInfo = myTeam[0]; myPokemon = myPokemonInfo[0]
		print ('You switched from', oldPokemon, 'into', myPokemon + '!')
		enemyMoveList = random.sample(enemyPokemonMoveSet,1); enemyMove = enemyMoveList[0]
		turnOutcomeInfo = startEnemyTurn(enemyMove,myInformation,enemyInformation,environmentInformation)
		myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]; myPokemon = myPokemonInfo[0]
		enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
		roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
		return roundOutcomeInfo

def startBattle(myInformation,enemyInformation,environmentInformation):
	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	enemyTeam = enemyInformation[0];enemyBag = enemyInformation[1];enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0];enemyPokemonName = enemyPokemonInfo[1];enemyPokemonLevel = enemyPokemonInfo[2];enemyPokemonIV = enemyPokemonInfo[3];enemyPokemonEV = enemyPokemonInfo[4];enemyPokemonHP = enemyPokemonInfo[5];enemyPokemonExperience = enemyPokemonInfo[6];enemyPokemonForm = enemyPokemonInfo[7];enemyPokemonGender = enemyPokemonInfo[8];enemyPokemonAbility = enemyPokemonInfo[9];enemyPokemonTypeOne = enemyPokemonInfo[10];enemyPokemonTypeTwo = enemyPokemonInfo[11];enemyPokemonItem = enemyPokemonInfo[12];enemyPokemonMoveSet = enemyPokemonInfo[13];enemyPokemonMovePP = enemyPokemonInfo[14];enemyPokemonNVStatus = enemyPokemonInfo[15];enemyPokemonNVStatusCount = enemyPokemonInfo[16];enemyPokemonVStatus = enemyPokemonInfo[17];enemyPokemonVStatusCount = enemyPokemonInfo[18];enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0]; enemyPlayerWording = enemyPlayer[1]
	enemyMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV); myMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV)					
	print('A wild lvl', enemyPokemonLevel, enemyPokemon, 'appeared! Go', myPokemon, '!')	
	myTeamTotalHP = getTeamTotalHP(myTeam)
	enemyTeamTotalHP = getTeamTotalHP(enemyTeam)
	while myTeamTotalHP > 0 and enemyPokemonHP > 0:
		while myPokemonHP > 0 and enemyPokemonHP > 0:
			turnOutcomeInfo = startRound(myInformation,enemyInformation,environmentInformation)
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			runLast=turnOutcomeInfo[2]; runLast=runLast[0]
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
			expOutcome = getExpOutcome(myPokemon,myPokemonLevel,myPokemonExperience,myPokemonMoveSet,enemyPokemon,enemyPokemonLevel)			
			myPokemonInfo[2] = expOutcome[0]; myPokemonInfo[6] = expOutcome[1]; myPokemonInfo[13] = expOutcome[2]; myPokemonInfo[0] = expOutcome[3]
			changePokemon = getRandomSwitchPokemon(enemyTeam)
			enemyTeam = changePokemon[0]; change = changePokemon[1]
			enemyPokemonInfo = enemyTeam[0]; enemyPokemon = enemyPokemonInfo[0]
			enemyPokemonHP = enemyPokemonInfo[5]
			print (enemyPlayerName, 'sent out', enemyPokemon + '!')
	myTeamTotalHP = getTeamTotalHP(myTeam)
	if myTeamTotalHP == 0:
		print('You whited out!')
	if enemyPokemonHP == 0:
		print('The wild', enemyPokemon, 'fainted! You win!')
		expOutcome = getExpOutcome(myPokemon,myPokemonLevel,myPokemonExperience,myPokemonMoveSet,enemyPokemon,enemyPokemonLevel)
		myPokemonInfo[2] = expOutcome[0]; myPokemonInfo[6] = expOutcome[1]; myPokemonInfo[13] = expOutcome[2]; myPokemonInfo[0] = expOutcome[3]

def getExpOutcome(myPokemon,myPokemonLevel,myPokemonExp,myPokemonMoveSet,enemyPokemon,enemyPokemonLevel):
	expYield = getExpYield(enemyPokemon,enemyPokemonLevel)
	print(myPokemon, 'gained', expYield, 'exp!')
	myPokemonExp = myPokemonExp + expYield
	myPokemonNextLevel = getExp(myPokemon,myPokemonLevel+1)
	while myPokemonExp > myPokemonNextLevel:
		if myPokemonLevel == 100:
			return [myPokemon,myPokemonLevel,myPokemonExp,myPokemonMoveSet]
		pokemonMovesByLevel = getPokemonMovesByLevel(myPokemon)
		myPokemonLevel = myPokemonLevel+1
		print(myPokemon, 'went up one level and is now level', str(myPokemonLevel) + '!')
		if myPokemonLevel in pokemonMovesByLevel:
			newMove = pokemonMovesByLevel[myPokemonLevel]
			if len(myPokemonMoveSet) < 4:
				print(myPokemon, 'learnt', newMove + '!')
			if len(myPokemonMoveSet) > 3:
				print(myPokemon, 'wants to learn', newMove + '! Which move should be forgotton?')
				print(myPokemonMoveSet + ['Keep Current Moves'])
				moveInput = getMoveInput(myPokemonMoveSet + ['Keep Current Moves'])
				if moveInput != 'Keep Current Moves':
					print(myPokemon, 'forgot', moveInput, 'and learnt', newMove + '!')
					for n, i in enumerate(myPokemonMoveSet):
						if i == moveInput:
							myPokemonMoveSet[n] = newMove
				if moveInput == 'Keep Current Moves':
					print(myPokemon, 'did not learn', newMove + '.')
		myPokemonNextLevel = getExp(myPokemon,myPokemonLevel+1)
		pokemonEvolving = getPokemonEvolve(myPokemon,myPokemonLevel)
		if pokemonEvolving != 'No':
			oldPokemon = myPokemon; myPokemon = pokemonEvolving
			print(oldPokemon, 'just evolved into a', myPokemon + '!')
	return [myPokemonLevel,myPokemonExp,myPokemonMoveSet,myPokemon]

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
	print('> To begin the game as normal, type 1\n> For a preset battle, type 2\n> Gym Leader Challenge, type 3')
	x = input()
	if x == '1':
		startGame()
	if x == '2':
		myPokemonOne = 'Squirtle'; myPokemonOneLevel = 100; myPokemonOneIV = getRandomIV(); myPokemonOneStatus = 0; myPokemonOneStatStage = [0,0,0,0,0,0,0]; myPokemonOneStatusCount = 0; myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage); myPokemonOneExp = getExp(myPokemonOne,myPokemonOneLevel)
		myPokemonTwo = 'Charmander'; myPokemonTwoLevel = 50; myPokemonTwoIV = getRandomIV(); myPokemonTwoStatus = 0; myPokemonTwoStatStage = [0,0,0,0,0,0,0]; myPokemonTwoStatusCount = 0; myPokemonTwoHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage); myPokemonTwoExp = getExp(myPokemonTwo,myPokemonTwoLevel)
		myPokemonThree = 'Bulbasaur'; myPokemonThreeLevel = 19; myPokemonThreeIV = getRandomIV(); myPokemonThreeStatus = 0; myPokemonThreeStatStage = [0,0,0,0,0,0,0]; myPokemonThreeStatusCount = 0; myPokemonThreeHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage); myPokemonThreeExp = getExp(myPokemonThree,myPokemonThreeLevel)
		enemyPokemonOne = 'Venusaur'; enemyPokemonOneLevel = 100; enemyPokemonOneIV = getRandomIV(); enemyPokemonOneStatus = 0; enemyPokemonOneStatStage = [0,0,0,0,0,0,0]; enemyPokemonOneStatusCount = 0; enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneStatStage)
		enemyPokemonTwo = 'Ivysaur'; enemyPokemonTwoLevel = 50; enemyPokemonTwoIV = getRandomIV(); enemyPokemonTwoStatus = 0; enemyPokemonTwoStatStage = [0,0,0,0,0,0,0]; enemyPokemonTwoStatusCount = 0; enemyPokemonTwoHP = gethpStat(enemyPokemonTwo,enemyPokemonTwoLevel,enemyPokemonTwoIV,enemyPokemonTwoStatStage)
		myPokemonOneList = [myPokemonOne,myPokemonOneLevel,myPokemonOneHP,myPokemonOneIV,myPokemonOneStatus,myPokemonOneStatusCount,myPokemonOneStatStage,myPokemonOneExp]
		myPokemonTwoList = [myPokemonTwo,myPokemonTwoLevel,myPokemonTwoHP,myPokemonTwoIV,myPokemonTwoStatus,myPokemonTwoStatusCount,myPokemonTwoStatStage,myPokemonTwoExp]
		myPokemonThreeList = [myPokemonThree,myPokemonThreeLevel,myPokemonThreeHP,myPokemonThreeIV,myPokemonThreeStatus,myPokemonThreeStatusCount,myPokemonThreeStatStage,myPokemonThreeExp]
		enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneHP,enemyPokemonOneIV,enemyPokemonOneStatus,enemyPokemonOneStatusCount,enemyPokemonOneStatStage]
		enemyPokemonTwoList = [enemyPokemonTwo,enemyPokemonTwoLevel,enemyPokemonTwoHP,enemyPokemonTwoIV,enemyPokemonTwoStatus,enemyPokemonTwoStatusCount,enemyPokemonTwoStatStage]
		myTeam = [myPokemonOneList,myPokemonTwoList,myPokemonThreeList]
		enemyTeam = [enemyPokemonOneList,enemyPokemonTwoList]
		myTrainerInfo = [1]
		enemyTrainerInfo = ['Trainer','Jimbo','opposing']
		startBattle(myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
	if x == '3':
		myPokemonOne = 'Bulbasaur'
		myPokemonOneName = 'Bulba'
		myPokemonOneLevel = 15
		myPokemonOneIV = [31,31,31,31,31,31]
		myPokemonOneEV = 'xxx'
		myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
		myPokemonOneExperience = getExp(myPokemonOne,myPokemonOneLevel)
		myPokemonOneForm = 'NA'
		myPokemonOneGender = 'Male'
		myPokemonOneAbility = 'Chloraphyll'
		myPokemonOneTypeOne = 'Grass'
		myPokemonOneTypeTwo = 'Poison'
		myPokemonOneItem = 'None'
		myPokemonOneMoveSet = ['Tackle', 'Vine Whip', 'Defense Curl','Flamethrower']
		myPokemonOneMovePP = [10, 10, 10]
		myPokemonOneNVStatus = 0
		myPokemonOneNVStatusCount = 0
		myPokemonOneVStatus = 0
		myPokemonOneVStatusCount = 0
		myPokemonOneCurrentStatStage = [0,0,0,0,0,0,0]
		
		myPokemonOneList = [myPokemonOne,myPokemonOneName,myPokemonOneLevel,myPokemonOneIV,myPokemonOneEV,myPokemonOneHP,myPokemonOneExperience,myPokemonOneForm,myPokemonOneGender,myPokemonOneAbility,myPokemonOneTypeOne,myPokemonOneTypeTwo,myPokemonOneItem,myPokemonOneMoveSet,myPokemonOneMovePP,myPokemonOneNVStatus,myPokemonOneNVStatusCount,myPokemonOneVStatus,myPokemonOneVStatusCount,myPokemonOneCurrentStatStage]
		myPokemonTwoList = [myPokemonOne,myPokemonOneName,myPokemonOneLevel,myPokemonOneIV,myPokemonOneEV,myPokemonOneHP,myPokemonOneExperience,myPokemonOneForm,myPokemonOneGender,myPokemonOneAbility,myPokemonOneTypeOne,myPokemonOneTypeTwo,myPokemonOneItem,myPokemonOneMoveSet,myPokemonOneMovePP,myPokemonOneNVStatus,myPokemonOneNVStatusCount,myPokemonOneVStatus,myPokemonOneVStatusCount,myPokemonOneCurrentStatStage]
		#myPokemonTwo = 'Bulbasaur'; myPokemonTwoLevel = 13; myPokemonTwoIV = getRandomIV(); myPokemonTwoStatus = 0; myPokemonTwoStatStage = [0,0,0,0,0,0,0]; myPokemonTwoStatusCount = 0; myPokemonTwoHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage); myPokemonTwoExp = getExp(myPokemonTwo,myPokemonTwoLevel); myPokemonTwoMoveSet = ['Tackle','Growl','Vine Whip']
		#myPokemonThree = 'Squirtle'; myPokemonThreeLevel = 13; myPokemonThreeIV = getRandomIV(); myPokemonThreeStatus = 0; myPokemonThreeStatStage = [0,0,0,0,0,0,0]; myPokemonThreeStatusCount = 0; myPokemonThreeHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage); myPokemonThreeExp = getExp(myPokemonThree,myPokemonThreeLevel); myPokemonThreeMoveSet = ['Tackle','Growl','Bubble']

		enemyPokemonOne = 'Ivysaur'
		enemyPokemonOneName = 'Bulba'
		enemyPokemonOneLevel = 16
		enemyPokemonOneIV = [31,31,31,31,31,31]
		enemyPokemonOneEV = 'xxx'
		enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV)
		enemyPokemonOneExperience = 800
		enemyPokemonOneForm = 'NA'
		enemyPokemonOneGender = 'Male'
		enemyPokemonOneAbility = 'Chloraphyll'
		enemyPokemonOneTypeOne = 'Grass'
		enemyPokemonOneTypeTwo = 'Poison'
		enemyPokemonOneItem = 'None'
		enemyPokemonOneMoveSet = ['Tackle', 'Vine Whip', 'Defense Curl']
		enemyPokemonOneMovePP = [10, 10, 10]
		enemyPokemonOneNVStatus = 0
		enemyPokemonOneNVStatusCount = 0
		enemyPokemonOneVStatus = 0
		enemyPokemonOneVStatusCount = 0
		enemyPokemonOneCurrentStatStage = [0,0,0,0,0,0,0]

		enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneName,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneEV,enemyPokemonOneHP,enemyPokemonOneExperience,enemyPokemonOneForm,enemyPokemonOneGender,enemyPokemonOneAbility,enemyPokemonOneTypeOne,enemyPokemonOneTypeTwo,enemyPokemonOneItem,enemyPokemonOneMoveSet,enemyPokemonOneMovePP,enemyPokemonOneNVStatus,enemyPokemonOneNVStatusCount,enemyPokemonOneVStatus,enemyPokemonOneVStatusCount,enemyPokemonOneCurrentStatStage]
		enemyPokemonTwoList = [enemyPokemonOne,enemyPokemonOneName,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneEV,enemyPokemonOneHP,enemyPokemonOneExperience,enemyPokemonOneForm,enemyPokemonOneGender,enemyPokemonOneAbility,enemyPokemonOneTypeOne,enemyPokemonOneTypeTwo,enemyPokemonOneItem,enemyPokemonOneMoveSet,enemyPokemonOneMovePP,enemyPokemonOneNVStatus,enemyPokemonOneNVStatusCount,enemyPokemonOneVStatus,enemyPokemonOneVStatusCount,enemyPokemonOneCurrentStatStage]



		myTeam = [myPokemonOneList,myPokemonTwoList]
		myBag = [0,0]; enemyBag = [0,0];
		myPlayer = [0,0]; enemyPlayer = [0,'opposing']
		environmentInformation = [0,0]
		enemyTeam = [enemyPokemonOneList,enemyPokemonTwoList]
		myTrainerInfo = [1]
		enemyTrainerInfo = ['Trainer','Brock','gym leader\'s']


		myInformation=[myTeam,myBag,myPlayer]; enemyInformation=[enemyTeam,enemyBag,enemyPlayer]
		startBattle(myInformation,enemyInformation,environmentInformation)

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
