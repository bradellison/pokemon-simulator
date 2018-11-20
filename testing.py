myPokemon = 'Bulbasaur'
statChange = [0,1,0,-1,0,0,0]

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

getStatChangeWording(myPokemon,statChange)