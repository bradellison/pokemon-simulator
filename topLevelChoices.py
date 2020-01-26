import random

from classes import Pokemon, Data, Player
from pokemonDictionaries import allPokemonList
from storyFunctions import mainGame
from choicesFunctions import getOptionOneOrTwoOrThree, getOptionOneOrTwo
from pcFunctions import getPokemonInfoViewPC
from battleFunctions import createEnemy, startBattle, teamTotalHP
from saveDataFunctions import loadGame
from pokemonCentreFunctions import healAllPokemon, pokemonCenter
from overworldFunctions import directionChoice

def battleTypeChoice():
	print('What would you like to do?')
	print(' 1 - Battle Trainer\n 2 - Battle Wild Pokemon\n 3 - Go To Pokemon Center\n 4 - Elite Four Attempt\n 5 - Battle Frontier\n 6 - Main Game')
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2 or choiceInput == 3 or choiceInput == 4 or choiceInput == 5 or choiceInput == 6:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def eliteFour(data):
#	elite4LorelaiTeam = [Pokemon('Dewgong',53,['Growl','Aurora Beam','Rest','Take Down']),Pokemon('Cloyster',53,['Supersonic','Clamp','Aurora Beam','Spike Cannon']),Pokemon('Slowbro',54,['Water Gun','Growl','Withdraw','Amnesia']),Pokemon('Jynx',56,['Double Slap','Ice Punch','Body Slam','Thrash']),Pokemon('Lapras',56,['Body Slam','Confuse Ray','Hydro Pump','Blizzard'])]
	elite4LorelaiTeam = [Pokemon('Dewgong',53,['Toxic']),Pokemon('Cloyster',53,['Supersonic','Clamp','Aurora Beam','Spike Cannon']),Pokemon('Slowbro',54,['Water Gun','Growl','Withdraw','Amnesia']),Pokemon('Jynx',56,['Double Slap','Ice Punch','Body Slam','Thrash']),Pokemon('Lapras',56,['Body Slam','Confuse Ray','Hydro Pump','Blizzard'])]
	healAllPokemon(data)
	elite4BrunoTeam = [Pokemon('Onix',53,['Rock Throw','Rage','Slam','Harden']),Pokemon('Hitmonchan',55,['Ice Punch','Fire Punch','Thunder Punch','Counter']),Pokemon('Hitmonlee',55,['Jump Kick','Focus Energy','High Jump Kick','Mega Kick']),Pokemon('Onix',56,['Rock Throw','Rage','Slam','Harden']),Pokemon('Machamp',58,['Leer','Focus Energy','Fissure','Submission'])]
	elite4AgathaTeam = [Pokemon('Gengar',56,['Confuse Ray','Night Shade','Hypnosis','Dream Eater']),Pokemon('Golbat',56,['Supersonic','Confuse Ray','Wing Attack','Haze']),Pokemon('Haunter',55,['Confuse Ray','Night Shade','Hypnosis','Dream Eater']),Pokemon('Arbok',58,['Bite','Glare','Screech','Acid']),Pokemon('Gengar',60,['Confuse Ray','Night Shade','Toxic','Dream Eater'])]
	elite4LanceTeam = [Pokemon('Gyarados',58,['Hydro Pump','Dragon Rage','Leer','Hyper Beam']),Pokemon('Dragonair',56,['Agility','Slam','Dragon Rage','Hyper Beam']),Pokemon('Dragonair',56,['Agility','Slam','Dragon Rage','Hyper Beam']),Pokemon('Aerodactyl',60,['Supersonic','Take Down','Bite','Hyper Beam']),Pokemon('Dragonite',62,['Agility','Slam','Barrier','Hyper Beam'])]
	elite4BlueTeam = [Pokemon('Pidgeot',61,['Wing Attack','Mirror Move','Sky Attack','Whirlwind']),Pokemon('Alakazam',59,['Psybeam','Psychic','Reflect','Recover']),Pokemon('Rhydon',61,['Leer','Tail Whip','Fury Attack','Horn Drill']),Pokemon('Exeggutor',63,['Hypnosis','Barrage','Stomp']),Pokemon('Arcanine',61,['Roar','Leer','Ember','Take Down']),Pokemon('Blastoise',65,['Hydro Pump','Blizzard','Bite','Withdraw'])]
	createEnemy(data,'Elite Four member', 'Lorelai', elite4LorelaiTeam, 1000, 'Ice cold!')
	startBattle(data)
	healAllPokemon(data)
	createEnemy(data,'Elite Four member', 'Bruno', elite4BrunoTeam, 1000, 'You fought hard!')
	startBattle(data)
	healAllPokemon(data)
	createEnemy(data,'Elite Four member', 'Agatha', elite4AgathaTeam, 1000, 'Spooky stuff!')
	startBattle(data)
	healAllPokemon(data)
	createEnemy(data,'Elite Four member', 'Lance', elite4LanceTeam, 1000, 'You beat me! But someone beat me first!')
	startBattle(data)
	healAllPokemon(data)
	createEnemy(data,'Elite Four champion', 'Blue', elite4BlueTeam, 1000, 'No! You\'re the new champion!')
	startBattle(data)


def battleTrainer(data):
	enemyTeam = [Pokemon(random.choice(allPokemonList),100, 'Random'), Pokemon(random.choice(allPokemonList),100, 'Random'), Pokemon(random.choice(allPokemonList),100, 'Random')]
	createEnemy(data,'Gym Leader', 'Brock', enemyTeam, 100, 'Damn! You beat me fair and square!')
	startBattle(data)

def wildBattleTopLevel(data):
	wildTeam = [Pokemon(random.choice(allPokemonList),50, 'Random')]
	createEnemy(data,'Wild', 'Wild', wildTeam, 0, 'Damn!')
	startBattle(data)

def battleFrontier(data):
	print('Welcome to the Battle Frontier! This will be a true test of your skills and we will see how far you can make it against some of the regions top trainers!')
	print('The first thing you need to do is choose your Pokemon! Let\'s see what\'s available today!')
	generateFrontierStartingPokemon(data)
	frontierPokemonChoice(data)

def frontierPokemonChoice(data):
	y = 0
	numberChosen = 0
	while y == 0:
		count = 1
		print('\nWhich Pokemon would you like to look at?')
		for j in range(len(data.pc.boxes[0].inventory)):
			i = data.pc.boxes[0].inventory[j]
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
				for j in range(len(data.pc.boxes[0].inventory)):
					if int(choiceInput) == int(j+1):
						choice = data.pc.boxes[0].inventory[int(choiceInput) - 1]
						print('What would you like to do with this pokemon?')
						option = getOptionOneOrTwo('Withdraw', 'View more information')
						if option == 1:
							if len(data.player.team) < 6:
								data.player.team.append(choice)
								data.pc.boxes[0].inventory.remove(choice)
								print('You added', choice.name, 'to your party!')
							else:
								print('You have no room in your party for that right now!')
						else:
							getPokemonInfoViewPC(data, choice, 'withdraw')
						x = 1
						numberChosen += 1
						if numberChosen == 3:
							return 0
				if x == 0:
					print("Please choose a Pokemon from the list above!")
			except ValueError:
				print("Please choose a Pokemon from the list above!")	

def generateFrontierStartingPokemon(data):
	data.pc.boxes[0].inventory = []
	data.pc.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),50, 'Random'))
	data.pc.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),50, 'Random'))
	data.pc.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),50, 'Random'))
	data.pc.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),50, 'Random'))
	data.pc.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),50, 'Random'))
	data.pc.boxes[0].inventory.append(Pokemon(random.choice(allPokemonList),50, 'Random'))	

def startGame():
	print('New game or continue?')
	newOrContinue = getOptionOneOrTwo('New Game', 'Continue') 
	if newOrContinue == 2:
		data = loadGame()
	else:
		data = Data()
		data.player = Player()
		data.player.defaultTeam.append(Pokemon(random.choice(allPokemonList), 100, 'Random'))
		data.player.defaultTeam.append(Pokemon(random.choice(allPokemonList), 100, 'Random'))
		data.player.defaultTeam.append(Pokemon(random.choice(allPokemonList), 100, 'Random'))
		data.player.team = data.player.defaultTeam
		data.player.pokemon = data.player.team[0]
	while teamTotalHP(data.player) > 0:
		choice = battleTypeChoice()
		if choice == 1:
			battleTrainer(data)
		elif choice == 2:
			wildBattleTopLevel(data)
		elif choice == 3:
			pokemonCenter(data)
		elif choice == 4:
			eliteFour(data)
		elif choice == 5:
			battleFrontier(data)
		elif choice == 6:
			mainGame(data, newOrContinue)

def testFunction():
	data = Data()
	directionChoice(data)
