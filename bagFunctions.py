import time
import math
from random import randint

from choicesFunctions import getYesOrNo
from text import text



####### BAG FUNCTIONS ########

ballCatchModifiers = {'PokeBall':1,'Great Ball':2,'Ultra Ball':3,'Master Ball':'Master'}
statusCatchModifiers = {0:1,1:1.5,2:1.5,3:2,4:2,5:1.5,6:1.5}

medicineHealAmount = {'Potion':20,'Super Potion':50,'Hyper Potion':100,'Max Potion':10000,'Full Restore':10000}

def getBallModifier(ball):
	return ballCatchModifiers[ball]

def getStatusCatchModifiers(data):
	return statusCatchModifiers[data.enemy.pokemon.nvStatus]

def getMedicineHeal(medicine):
	return medicineHealAmount[medicine]


def openBag(data):
	text(data, 'You opened your bag! What pocket would you like to go into?')
	x = 0
	while x == 0:
		choice = getPocketChoice()
		if choice == 'Balls':
			x = getBallPocket(data)
		elif choice == 'Medicine':
			x = getMedicinePocket(data)
		else:
			x = 1
			return 1
	return x

def getCatch(data, ball):
	ballModifier = ball.modifier
	if ballModifier == 'Master':
		text(data, 'You caught the opposing', data.enemy.pokemon.name + '!')
		getCaughtPokemon(data)
		return 'Catch'
	statusModifier = getStatusCatchModifiers(data)
	catchValue = int(((( 3 * data.enemy.pokemon.maxhp - 2 * data.enemy.pokemon.hp) * data.enemy.pokemon.catchRate * ballModifier) / ( 3 * data.enemy.pokemon.maxhp) ) * statusModifier)
	catch = 1048560 / math.sqrt(math.sqrt(16711680 / catchValue))
	count = 0
	for _ in range(3):
		random = randint(1,65535)
		count = count + 1
		text(data, 'Shook', count, 'times!')
		if catch > random:		
			if count == 3:
				text(data, 'You caught the opposing', data.enemy.pokemon.name + '!')
				getCaughtPokemon(data)
				return 'Catch'
		else:
			if count == 1:
				text(data, 'Not even close!')
			if count == 2:
				text(data, 'Oh, nearly had it!')
			if count == 3:
				text(data, 'So so close!')
			return 'No catch'

def getCaughtPokemon(data):
	if len(data.player.defaultTeam) < 6:
		getNamePokemon(data.enemy.pokemon)
		data.player.defaultTeam.append(data.enemy.pokemon)
		text(data, 'You added the', data.enemy.pokemon.name, 'to your team!')
	else:
		getNamePokemon(data.enemy.pokemon)
		data.pc.boxes[0].inventory.append(data.enemy.pokemon)
		text(data, 'You sent the', data.enemy.pokemon.name, 'to the PC!')

def getNamePokemon(pokemon):
	print('\nWould you like to name the', pokemon.name + '?')
	choice = getYesOrNo()
	if choice == 1:
		print('\nWhat would you like to name it?')
		while True:
			choiceInput = input('-- ')
			if len(choiceInput) <= 10:
				pokemon.name = choiceInput
				return
			else:
				print('That name is too long! 10 characters max!')

def getBallPocket(data):
	ball = getBallChoice(data)
	if ball == 0:
		return 0
	ball.quantity -= 1
	if ball.quantity == 0:
		data.bag.balls.remove(ball)
	text(data, 'You throw the', ball.name, 'at the opposing', data.enemy.pokemon.name + '!')
	if data.enemy.type != 'Wild':
		text(data, 'The', data.enemy.type, data.enemy.name, 'swatted the ball away! You can\'t use that here!')
		return 'No Catch'
	else:
		catch = getCatch(data, ball)
		if catch == 1:
			return 1
		else:
			return catch

def getMedicinePocket(data):
	medicine = getMedicineChoice(data)
	if medicine == 0:
		return 0
	choice = getPokemonHealChoice(data, medicine)
	if choice == 0:
		return 0
	medicine.quantity -= 1
	if medicine.quantity == 0:
		data.bag.medicine.remove(medicine)

#def getHealFunction(medicine):
#	if medicine in 

def getPokemonHealChoice(data, medicine):
	count = 1
	print('Which Pokemon would you like to use this on?')
	for i in data.player.team:
		print('', count, '-', i.name, '- Level', str(i.level), '-', str(i.hp) + '/' + str(i.maxhp) + 'HP')
		count += 1
	print('', count, '- Back')
	while True:
		try:
			x = 0
			choiceInput = input('-- ')
			if int(choiceInput) == int(count):
				return 0
			for j in range(len(data.player.team)):
				if choiceInput == data.player.team[j].name or int(choiceInput) == int(j+1):
					if data.player.team[j].hp == 0:
						print(data.player.team[j].name, 'has fainted! This would have no effect! Choose another!')
						x = 1
					elif data.player.team[j].hp == data.player.team[j].maxhp:
						print(data.player.team[j].name, 'is at full health! This would have no effect! Choose another!')
						x = 1
					else:
						heal = medicine.heal
						if data.player.team[j].maxhp - data.player.team[j].hp < heal:
							heal = data.player.team[j].maxhp - data.player.team[j].hp
						data.player.team[j].hp += heal
						text(data, data.player.team[j].name, 'has been healed by', heal, 'HP! It has', str(data.player.pokemon.hp) + '/' + str(data.player.pokemon.maxhp), 'remaining!')
						return 1
			if x == 0:
				print("Please choose a Pokemon from the list above!")
		except ValueError:
			print("Please choose a Pokemon from the list above!")	


def getMedicineChoice(data):
	options = len(data.bag.medicine)
	if options == 0:
		print('You have no medicine remaining!')
		return 0
	for i in range(options):
		print('', i+1, '-', data.bag.medicine[i].name, '-', data.bag.medicine[i].quantity, 'remaining.')
		i += 1
	i += 1
	print('', i, '- Back')
	while True:
		try:
			choiceInput = input('-- ')
			if int(choiceInput) < i and int(choiceInput) > 0:
				medicine = data.bag.medicine[int(choiceInput) - 1]
				return medicine
			elif int(choiceInput) == i:
				return 0
			print("Please choose an item from the list above!")
		except ValueError:
			print("Please choose an item from the list above!")	

def getBallChoice(data):
	options = len(data.bag.balls)
	if options == 0:
		print('You have no balls remaining!')
		return 0
	for i in range(options):
		print('', i+1, '-', data.bag.balls[i].name, '-', data.bag.balls[i].quantity, 'remaining.')
		i += 1
	i += 1
	print('', i, '- Back')
	while True:
		try:
			choiceInput = input('-- ')
			if int(choiceInput) < i and int(choiceInput) > 0:
				ball = data.bag.balls[int(choiceInput) - 1]
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