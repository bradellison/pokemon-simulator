
def getOptionsXnumber(listOfOptions):
	if len(listOfOptions) == 2:
		return getOptionOneOrTwo(listOfOptions[0],listOfOptions[1])
	if len(listOfOptions) == 3:
		return getOptionOneOrTwoOrThree(listOfOptions[0],listOfOptions[1],listOfOptions[2])
	if len(listOfOptions) == 4:
		return getOptionOneOrTwoOrThreeOrFour(listOfOptions[0],listOfOptions[1],listOfOptions[2],listOfOptions[3])
	if len(listOfOptions) == 5:
		return getOptionOneOrTwoOrThreeOrFourOrFive(listOfOptions[0],listOfOptions[1],listOfOptions[2],listOfOptions[3],listOfOptions[4])


def getOptionOneOrTwo(option1, option2):
	print(' 1 -', option1, '\n 2 -', option2)
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

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

def getOptionOneOrTwoOrThreeOrFour(option1, option2, option3, option4):
	print(' 1 -', option1, '\n 2 -', option2, '\n 3 -', option3, '\n 4 -', option4)
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2 or choiceInput == 3 or choiceInput == 4:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def getOptionOneOrTwoOrThreeOrFourOrFive(option1, option2, option3, option4, option5):
	print(' 1 -', option1, '\n 2 -', option2, '\n 3 -', option3, '\n 4 -', option4, '\n 5 -', option5)
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2 or choiceInput == 3 or choiceInput == 4 or choiceInput == 5:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')

def getYesOrNo():
	print(' 1 - Yes\n 2 - No')
	while True:
		try:
			choiceInput = int(input('-- '))
			if choiceInput == 1 or choiceInput == 2:
				return choiceInput
			else:
				print('Please choose an option!')
		except ValueError:
			print('Please choose an option!')	