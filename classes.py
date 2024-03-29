from random import randint
from getVariableFunctions import getNature, getRandomIV, getRandomPersonalityValue, getBaseStats, getStats, getGender, getAbility, getPokemonType, getExpGroup, getExpYieldBase, getExp, getPokemonCatchRate, getMoveSet, getMaxPP, getPokemonSprite
from moveDictionaries import moveInfo
from bagFunctions import getMedicineHeal, getBallModifier
from gameMaps import locationMapDict
from screen import BattleScreen
from spritesBattle import ballRight, ballLeft, ballStraight
from locationData import getLocationWarpZones, getLocationEnemies, allSignDict

class Data(object):
	def __init__(self):
		self.player = Player()
		self.settings = Settings()
		self.enemy = Enemy('Trainer', 'Default', [], 0, 'Default Text', [0,0], 0, "Up")
		self.rival = Enemy('Rival', 'Default', [], 420, 'Smell ya later!', [0,0], 0, "Up")
		self.environment = Environment('Pallet Town','None')
		self.story = Story()
		self.pc = PC()
		self.bag = Bag()
		self.bscreen = BattleScreen()
		self.expMult = 1

class Settings(object):
	def __init__(self):
		self.settings = ["Colorama", "WallClip", "Wild Battles", "Show Co-Ords", "Triple XP", "10x XP", "Skip Story"]
		self.settingsDict = {"Colorama":False, "WallClip": False, "Wild Battles": True, "Show Co-Ords": False, "Triple XP": False, "10x XP": False, "Skip Story": False}


class Player(object):
	def __init__(self):
		self.name = 'Brad'
		self.direction = "Down"
		self.rival = ''
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
		self.lastCentre = 'Pallet Town'
		self.lastDirection = None
		self.lastBattleChoice = 1
		self.lastAttackChoice = 1
		#self.xCo = 10
		#self.yCo = 10
		self.xCo = 9 #Outside Oak's door default
		self.yCo = 11 #Outside Oak's door default

class Story(object):
	def __init__(self):
		self.oakSpeechCompleted = False
		self.startPokemonChosen = False
		self.starterRivalFightCompleted = False

class PC(object):
	def __init__(self):
		self.boxes = [Box()]

class Box(object):
	def __init__(self):
		self.inventory = []

class Bag(object):
	def __init__(self):
		self.currentOpenIdentifier = "a"
		self.items = []
		self.medicine = []
		self.keyItems = []
		self.balls = []
		self.openBagDict = {"a": self.items, "b": self.medicine, "c": self.keyItems, "d": self.balls}
		self.openBag = self.items

class Item(object):
	def __init__(self, type, name, quantity):
		self.type = type
		self.name = name
		self.quantity = quantity
		self.modifier = self.getModifier()

	def getModifier(self):
		if self.type == "Healing":
			return getMedicineHeal(self.name)
		elif self.type == "Ball":
			return getBallModifier(self.name)


class Enemy(object):
	def __init__(self, type, name, team, prizeMoney, text, coords, viewDistance, viewDirection):
		self.type = type
		self.name = name
		self.team = team
		self.coords = coords
		self.aggroCoords = self.generateAggroCoords(coords, viewDistance, viewDirection)
		self.battleComplete = False
		self.battleReady = False
		self.battleReadySignalCoords = [self.coords[0], self.coords[1] - 1]
		self.viewDirection = viewDirection
		self.livingPokemon = 0
		self.prizeMoney = prizeMoney
		self.text = text
		self.lightScreen = 0
		self.lightScreenCount = 0
		self.reflect = 0
		self.reflectCount = 0
		self.mist = 0
		self.mistCount = 0

	def generateAggroCoords(self, coords, viewDistance, viewDirection):
		directionDict = {"Up": [0, -1], "Down": [0, 1], "Left": [-1, 0], "Right": [1, 0]}
		aggroCoords = [coords]
		baseCoord = coords.copy()
		for _ in range(viewDistance):
			baseCoord = [baseCoord[0] + directionDict[viewDirection][0], baseCoord[1] + directionDict[viewDirection][1]]
			aggroCoords.append(baseCoord)
		return aggroCoords
class Pokemon(object):
	def __init__(self, species, level, moveSet):
		self.species = species
		self.name = species
		self.level = level
		self.nature = getNature(species)
		self.sprite = getPokemonSprite(species)
		self.lastAttackChoice = 1
		self.iv = getRandomIV()
		self.ev = [0,0,0,0,0,0]
		self.personalityValue = getRandomPersonalityValue()
		self.baseStats = getBaseStats(species)
		self.stats = getStats(self)
		self.statStage = [0,0,0,0,0,0,0,0,0]
		self.maxhp = self.stats[0]
		self.hp = self.stats[0]
		self.gender = getGender(species)
		self.ability = getAbility(species)
		self.type = getPokemonType(self)
		self.item = Item("None", "None", 1)
		if moveSet == 'Random':
			self.moveSet = getMoveSet(self)
		else:
			self.moveSet = moveSet
#		self.moveSet = moveSet
		self.movePPMax = getMaxPP(self)
		self.movePPCurrent = getMaxPP(self)
		self.nvStatus = 0
		self.nvStatusCount = 0 
		self.expGroup = getExpGroup(species)
		self.BaseExpYield = getExpYieldBase(species)
		self.lastLevelExp = getExp(species, level)
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
		self.flashFireMult = 1
		self.inPokeball = False
		self.inPokeballCount = 0
		self.pokeballCountSpriteDict = {1: ballLeft, 2: ballRight, 3: ballLeft, 4: ballStraight}

class Environment(object):
	def __init__(self, location, weather):
		self.location = Location(location)
		self.locations = [self.location]
		self.weather = weather
		self.weathercount = 0
		self.payDayExtra = 0
		self.battleStart = False
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

class Location(object):
	def __init__(self, name):
		self.name = name
		self.map = locationMapDict[name]
		self.warpZones = getLocationWarpZones(name)
		self.enemies = self.buildEnemyData(getLocationEnemies(name))
		self.signs = self.buildSignData(name)
		
	def buildEnemyData(self, rawEnemies):
		enemies = []
		for rawEnemy in rawEnemies:
			team = []
			for pokemon in rawEnemy[2]:
				team.append(Pokemon(pokemon[0], pokemon[1], pokemon[2]))
			enemy = Enemy(rawEnemy[0], rawEnemy[1], team, rawEnemy[3], rawEnemy[4], rawEnemy[5], rawEnemy[6], rawEnemy[7])
			enemies.append(enemy)
		return enemies

	def buildSignData(self, name):
		signs = []
		if name in allSignDict:
			for sign in allSignDict[name]:
				signs.append(Sign(sign[0], sign[1], sign[2]))
		return signs


class Sign(object):
	def __init__(self, location, text, coords):
		self.location = location
		self.text = text
		self.coords = coords