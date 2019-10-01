def getCatch(ball):
	ballModifier = ball.modifier
	if ballModifier == 'Master':
		print('You caught the opposing', enemy.pokemon.name + '!')
		getCaughtPokemon()
		return 'Catch'
	statusModifier = getStatusCatchModifiers()
	catchValue = int(((( 3 * enemy.pokemon.maxhp - 2 * enemy.pokemon.hp) * enemy.pokemon.catchRate * ballModifier) / ( 3 * enemy.pokemon.maxhp) ) * statusModifier)
	catch = 1048560 / math.sqrt(math.sqrt(16711680 / catchValue))
	count = 0
	for i in range(3):
		random = randint(1,65535)
		count = count + 1
		print('Shook', count, 'times!')
		time.sleep(1)
		if catch > random:		
			if count == 3:
				print('You caught the opposing', enemy.pokemon.name + '!')
				getCaughtPokemon()
				return 'Catch'
		else:
			if count == 1:
				print('Not even close!')
			if count == 2:
				print('Oh, nearly had it!')
			if count == 3:
				print('So so close!')
			print('')
			return 'No catch'