import time
import math
from random import randint

from choicesFunctions import getOption, getYesOrNo
from text import text, worldTextOptions, worldText
from textTools import onlyTextBox, onlyTextBoxWithOptions, printWithScreenSides, printWithScreenSidesAndSpacing, getExtraSpace
from screenPokemonSelection import openPokemonSelectionScreen
from screen import drawScreen
from spritesAll import screenEmp, screenBot, screenMid, screenTop



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

def drawBagTabs(data):
	if data.bag.currentOpenIdentifier == "a":
		topTab = "┃ │           ╭╮     b     ╭╮     c     ╭╮     d     │ ┃"
		midTab = "┃ │     a     ││  HEALING  ││ KEY ITEMS ││   BALLS   │ ┃"
		lowTab = "┃ │   ITEMS   │╰───────────╯╰───────────╯╰───────────╯ ┃"
		botTab = "┃ ╰───────────╯                                        ┃"
	elif data.bag.currentOpenIdentifier == "b":
		topTab = "┃ │     a     ╭╮           ╭╮     c     ╭╮     d     │ ┃"
		midTab = "┃ │   ITEMS   ││     b     ││ KEY ITEMS ││   BALLS   │ ┃"
		lowTab = "┃ ╰───────────╯│  HEALING  │╰───────────╯╰───────────╯ ┃"
		botTab = "┃              ╰───────────╯                           ┃"
	elif data.bag.currentOpenIdentifier == "c":
		topTab = "┃ │     a     ╭╮     b     ╭╮           ╭╮     d     │ ┃"
		midTab = "┃ │   ITEMS   ││  HEALING  ││     c     ││   BALLS   │ ┃"
		lowTab = "┃ ╰───────────╯╰───────────╯│ KEY ITEMS │╰───────────╯ ┃"
		botTab = "┃                           ╰───────────╯              ┃"
	elif data.bag.currentOpenIdentifier == "d":
		topTab = "┃ │     a     ╭╮     b     ╭╮     c     ╭╮           │ ┃"
		midTab = "┃ │   ITEMS   ││  HEALING  ││ KEY ITEMS ││     d     │ ┃"
		lowTab = "┃ ╰───────────╯╰───────────╯╰───────────╯│   BALLS   │ ┃"
		botTab = "┃                                        ╰───────────╯ ┃"
	print(topTab)
	print(midTab)
	print(lowTab)
	print(botTab)


def openBag(data, selectionText="Which item would you like to use?", battle=False, itemChosen=None, showOptions=True):
	itemDropped = False
	while True:
		print(screenTop)
		drawBagTabs(data)
		count = 1
		for item in data.bag.openBag:
			itemText = str(count) + ' - ' + item.name + getExtraSpace(item.name, 20) + "x" + str(item.quantity)
			printWithScreenSidesAndSpacing(itemText + getExtraSpace(itemText, 52))
			count += 1
		for _ in range(14 - count):
			print(screenEmp)
		print(screenMid)
		if itemChosen == None:
			onlyTextBoxWithOptions(selectionText, [], backWithE=True)
			tabOptions = ["a","b","c","d","e"]
			allOptions = data.bag.openBag + tabOptions
			option = getOption(allOptions)
			if option == "Back":
				return "None"
			if option in tabOptions:
				switchTab(data, option)
			elif option in data.bag.openBag:
				print("You chose " + option.name)
				itemChosen = option
		else:
			itemOptions = ["Use Item", "Give Item", "Drop Item", "Back"]
			if showOptions == False:
				onlyTextBox(selectionText, pauseAfter=True)
				if itemChosen not in data.bag.openBag:
					itemChosen = None
				showOptions = True
				selectionText = "Which item would you like to use? e to exit."
			else:
				onlyTextBoxWithOptions("What would you like to do with the " + itemChosen.name + "?", itemOptions)
				option = getOption(itemOptions)

				if option == "Use Item":
					if item.type == "Ball" and battle == False:
						openBag(data, "You can't use that right now!", battle=battle, itemChosen=itemChosen, showOptions=False)
						return
					if item.type == "Healing" and data.story.startPokemonChosen == False:
						openBag(data, "You don't have any Pokemon yet!", battle=battle, itemChosen=itemChosen, showOptions=False)
						return
					used = useItem(data, itemChosen, battle)
					if used == False:
						itemChosen = None
					else:
						if battle == True:
							return used

				elif option == "Give Item":
					if data.story.startPokemonChosen == False:
						openBag(data, "You don't have any Pokemon yet!", battle=battle, itemChosen=itemChosen, showOptions=False)
						return					
					if battle == True:
						outcome = openBag(data, "You can't give that during a battle!", battle=battle, itemChosen=itemChosen, showOptions=False)
						return outcome
					giveItem(data, itemChosen)
					return 

				elif option == "Drop Item":
					if battle == True:
						outcome = openBag(data, "You can't drop that during a battle!", battle=battle, itemChosen=itemChosen, showOptions=False)
						return outcome
					dropItem(data, itemChosen)
					outcome = openBag(data, "You dropped 1 " + itemChosen.name + "!", battle=battle, itemChosen=itemChosen, showOptions=False)
					return outcome
				else:
					itemChosen = None


def useItem(data, item, battle):
	if item.type == "Healing":
		selectionText = "Which Pokemon would you like to use " + item.name + " on?"
		while True:
			pokemon = openPokemonSelectionScreen(data, battle=battle, selectionText=selectionText, useOrGiveItem=True)
			if pokemon == "Back":
				return False
			else:
				healed = healPokemon(data, pokemon, item, battle)
				if healed == True:
					removeItemFromBag(data, item, 1)
					return
				else:
					selectionText = "This would have no effect on " + pokemon.name + "! Choose another Pokemon!"
	if item.type == "Ball":
		removeItemFromBag(data, item, 1)
		text(data, 'You throw the', item.name, 'at the opposing', data.enemy.pokemon.name + '!')
		if data.enemy.type != 'Wild':
			text(data, 'The', data.enemy.type, data.enemy.name, 'swatted the ball away! You can\'t use that here!')
			return 'No Catch'
		else:
			catch = getCatch(data, item)
			if catch == 1:
				return 1
			else:
				return catch			
			pass

def giveItem(data, item):
	selectionText = "Which Pokemon would you like to give " + item.name + " to?"
	while True:
		pokemon = openPokemonSelectionScreen(data, selectionText=selectionText, useOrGiveItem=True)
		if pokemon == "Back":
			return False
		else:
			pokemon.item = item
			removeItemFromBag(data, item, 1)
			outcome = openBag(data, "You gave the " + item.name + " to " + pokemon.name + "!", battle=False, itemChosen=item, showOptions=False)
			return True



def dropItem(data, item):
	removeItemFromBag(data, item, 1) 

def removeItemFromBag(data, item, quantity):
	item.quantity -= quantity
	if item.quantity == 0:
		data.bag.openBag.remove(item)
	
def switchTab(data, tab):
	data.bag.currentOpenIdentifier = tab
	data.bag.openBag = data.bag.openBagDict[tab]

def healPokemon(data, pokemon, item, battle):
	if pokemon.hp == 0:
		return False
	elif pokemon.hp == pokemon.maxhp:
		return False
	else:
		heal = item.modifier
		if pokemon.maxhp - pokemon.hp < heal:
			heal = pokemon.maxhp - pokemon.hp
		pokemon.hp += heal

		if battle == True:
			text(data, pokemon.name, 'has been healed by', heal, 'HP! It has', str(data.player.pokemon.hp) + '/' + str(data.player.pokemon.maxhp), 'remaining!')
		if item.name == "Full Restore" or item.name == "Full Heal":
			if pokemon.nvStatus != 0:
				pokemon.nvStatus = 0
				if battle == True:
					text(data, pokemon.name + ' no longer has a status condition!')
		return True

def getCatch(data, ball):
	ballModifier = ball.modifier
	if ballModifier == 'Master':
		text(data, 'You caught the opposing', data.enemy.pokemon.name + '!')
		getCaughtPokemon(data)
		return 'Catch'
	statusModifier = getStatusCatchModifiers(data)
	catchValue = int(((( 3 * data.enemy.pokemon.maxhp - 2 * data.enemy.pokemon.hp) * data.enemy.pokemon.catchRate * ballModifier) / ( 3 * data.enemy.pokemon.maxhp) ) * statusModifier)
	catch = 1048560 / math.sqrt(math.sqrt(16711680 / catchValue))
	for _ in range(3):
		random = randint(1,65535)
		data.enemy.pokemon.inPokeballCount += 1
		text(data, 'Shook', data.enemy.pokemon.inPokeballCount, 'times!')
		if catch > random:		
			if data.enemy.pokemon.inPokeballCount == 3:
				data.enemy.pokemon.inPokeballCount += 1
				text(data, 'You caught the opposing', data.enemy.pokemon.name + '!')
				getCaughtPokemon(data)
				return 'Catch'
		else:
			if data.enemy.pokemon.inPokeballCount == 1:
				data.enemy.pokemon.inPokeballCount = 0
				text(data, 'Not even close!')
			elif data.enemy.pokemon.inPokeballCount == 2:
				data.enemy.pokemon.inPokeballCount = 0
				text(data, 'Oh, nearly had it!')
			elif data.enemy.pokemon.inPokeballCount == 3:
				data.enemy.pokemon.inPokeballCount = 0
				text(data, 'So so close!')
			return 'No catch'

def getCaughtPokemon(data):
	if len(data.player.defaultTeam) < 6:
		getNamePokemon(data, data.enemy.pokemon)
		data.player.defaultTeam.append(data.enemy.pokemon)
		data.player.team = data.player.defaultTeam.copy()
		text(data, 'You added', data.enemy.pokemon.name, 'to your team!')
	else:
		getNamePokemon(data, data.enemy.pokemon)
		data.pc.boxes[0].inventory.append(data.enemy.pokemon)
		text(data, 'You sent', data.enemy.pokemon.name, 'to the PC!')

def getNamePokemon(data, pokemon, battle=True):
	if battle == False:
		choice = worldTextOptions(data, 'Would you like to name the ' + pokemon.name + '?', options=["Yes", "No"], response=True)
	else:
		drawScreen(data)
		onlyTextBoxWithOptions('Would you like to name the ' + pokemon.name + '?', options=["Yes", "No"])
		choice = getOption(["Yes", "No"])
	if choice == "Yes":
		if battle == False:
			worldText(data, "What would you like to name it?", response=True)
		else:
			drawScreen(data)
			onlyTextBox("What would you like to name it?")
		while True:
			choiceInput = input('-- ')
			if len(choiceInput) <= 10:
				if choiceInput == "":
					pokemon.name = pokemon.species
					return
				pokemon.name = choiceInput
				return
			else:
				print('That name is too long! 10 characters max!')








#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ │	 a	 ╭╮		   ╭╮	 c	 ╭╮	 d	 │ ┃
#┃ │   ITEMS   ││	 b	 ││ KEY ITEMS ││   BALLS   │ ┃
#┃ ╰───────────╯│  HEALING  │╰───────────╯╰───────────╯ ┃
#┃			  ╰───────────╯						   ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┃						   │						  ┃
#┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
#┃ Which item would you like to choose?				 ┃
#┃													  ┃
#┃													  ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛