
def mainGame(player):
    oakSpeech(player)

def oakSpeech(player):
    text('Oak','Hello and welcome to the wonderful world of Pokemon!')
    text('Oak','My name is Professor Oak! What\'s your name?')
    chooseName(player.name)
    text('Oak',('Ah yes, lovely to meet you. My grandson lives closeby too, any idea what his name is?'))
    chooseName(player.rival)
    text('Oak','Of course, now I remember! Now let\'s get down to business.')
    text('Oak','I\'d like you to take one of these Pokemon here and see how you get on in the world on Pokemon!')
    string = 'Now', player.name + ',', player.rival, 'I\'d like to give you each a Pokemon!'
    text('Oak',string)
    pokemonChoice = getOptionOneOrTwoOrThree('Bulbasaur - the grass-type Pokemon.','Charmander - the fire-type Pokemon.','Squirtle - the water-type Pokemon.')


def getOptionOneOrTwoOrThree(option1, option2, option3):
	print(' 1 -', option1, '\n 2 -', option2, '\n 3 -', option3)
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2 or choiceInput == 3:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def chooseName(person):
    while True:
        try:
            choiceInput = input('-- ')
            if choiceInput != '':
                person = choiceInput
                return
            text('Oak','Sorry, I missed that. Say again?')
        except ValueError:
            text('Oak','Sorry, I missed that. Say again?')



def text(name, text):
    print(name + ':', text)
    input()

