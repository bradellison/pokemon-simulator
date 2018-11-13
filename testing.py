def getExp(expGroup,level):
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

print(getExp('Fluctuating',50))
print(getExp('Fluctuating',60))
print(getExp('Fluctuating',70))
print(getExp('Fluctuating',80))
print(getExp('Fluctuating',90))
print(getExp('Fluctuating',100))


print(2**2)



myInformation,enemyInformation,environmentInformation

myInformation
>myTeam,myBag,myPlayer

enemyInformation
>enemyTeam,enemyBag,enemyPlayer

myTeam
>myPokemonOne-Six

myPokemonOne-Six
>myPokemon,myPokemonName,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonEV,myPokemonExperience,myPokemonForm,myPokemonGender,myPokemonAbility,myPokemonTypeOne,myPokemonTypeTwo,myPokemonItem,myPokemonMoveSet,myPokemonMovePP,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonVStatus,myPokemonVStatusCount,myPokemonCurrentStatStage
0 > myPokemon
1 > myPokemonName
2 > myPokemonLevel
3 > myPokemonHP
4 > myPokemonIV
5 > myPokemonEV
6 > myPokemonExperience
7 > myPokemonForm
8 > myPokemonGender
9 > myPokemonAbility
10 > myPokemonTypeOne
11 > myPokemonTypeTwo
12 > myPokemonItem
13 > myPokemonMoveSet
14 > myPokemonMovePP
15 > myPokemonNVStatus
16 > myPokemonNVStatusCount
17 > myPokemonVStatus
18 > myPokemonVStatusCount
19 > myPokemonCurrentStatStage



myPokemon = myPokemonInfo[0],myPokemonName = myPokemonInfo[1],myPokemonLevel = myPokemonInfo[2],myPokemonHP = myPokemonInfo[3],myPokemonIV = myPokemonInfo[4],myPokemonEV = myPokemonInfo[5],myPokemonExperience = myPokemonInfo[6],myPokemonForm = myPokemonInfo[7],myPokemonGender = myPokemonInfo[8],myPokemonAbility = myPokemonInfo[9],myPokemonTypeOne = myPokemonInfo[10],myPokemonTypeTwo = myPokemonInfo[11],myPokemonItem = myPokemonInfo[12],myPokemonMoveSet = myPokemonInfo[13],myPokemonMovePP = myPokemonInfo[14],myPokemonNVStatus = myPokemonInfo[15],myPokemonNVStatusCount = myPokemonInfo[16],myPokemonVStatus = myPokemonInfo[17],myPokemonVStatusCount = myPokemonInfo[18],myPokemonCurrentStatStage = myPokemonInfo[19]


def startMyTurn(myInformation,enemyInformation,environmentInformation)

	myTeam = myInformation[0],myBag = myInformation[1],myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0],myPokemonName = myPokemonInfo[1],myPokemonLevel = myPokemonInfo[2],myPokemonHP = myPokemonInfo[3],myPokemonIV = myPokemonInfo[4],myPokemonEV = myPokemonInfo[5],myPokemonExperience = myPokemonInfo[6],myPokemonForm = myPokemonInfo[7],myPokemonGender = myPokemonInfo[8],myPokemonAbility = myPokemonInfo[9],myPokemonTypeOne = myPokemonInfo[10],myPokemonTypeTwo = myPokemonInfo[11],myPokemonItem = myPokemonInfo[12],myPokemonMoveSet = myPokemonInfo[13],myPokemonMovePP = myPokemonInfo[14],myPokemonNVStatus = myPokemonInfo[15],myPokemonNVStatusCount = myPokemonInfo[16],myPokemonVStatus = myPokemonInfo[17],myPokemonVStatusCount = myPokemonInfo[18],myPokemonCurrentStatStage = myPokemonInfo[19]
	
	enemyTeam = enemyInformation[0],enemyBag = enemyInformation[1],enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0],enemyPokemonName = enemyPokemonInfo[1],enemyPokemonLevel = enemyPokemonInfo[2],enemyPokemonHP = enemyPokemonInfo[3],enemyPokemonIV = enemyPokemonInfo[4],enemyPokemonEV = enemyPokemonInfo[5],enemyPokemonExperience = enemyPokemonInfo[6],enemyPokemonForm = enemyPokemonInfo[7],enemyPokemonGender = enemyPokemonInfo[8],enemyPokemonAbility = enemyPokemonInfo[9],enemyPokemonTypeOne = enemyPokemonInfo[10],enemyPokemonTypeTwo = enemyPokemonInfo[11],enemyPokemonItem = enemyPokemonInfo[12],enemyPokemonMoveSet = enemyPokemonInfo[13],enemyPokemonMovePP = enemyPokemonInfo[14],enemyPokemonNVStatus = enemyPokemonInfo[15],enemyPokemonNVStatusCount = enemyPokemonInfo[16],enemyPokemonVStatus = enemyPokemonInfo[17],enemyPokemonVStatusCount = enemyPokemonInfo[18],enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0], enemyPlayerWording = enemyPlayer[1]

	preMoveNVStatusCheck = getPreMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount)
	myPokemonInfo[15]=preMoveNVStatusCheck[1],myPokemonInfo[16]=preMoveNVStatusCheck[2],interrupt=preMoveNVStatusCheck[3]
	if interrupt == 0:
		preMoveVStatusCheck = getPreMoveVStatusCheck(myPokemon,myPokemonVStatus,myPokemonVStatusCount)
		myPokemonInfo[17]=preMoveVStatusCheck[1],myPokemonInfo[16]=preMoveVStatusCheck[2],interrupt=preMoveVStatusCheck[3]
		if interrupt == 0:
			hitOrMiss = getHitOrMiss(move)
			if hitOrMiss == 'Miss':
				print(myPokemon, 'used', move, 'but it missed!')
				interrupt = 0
			if interrupt == 0:
				moveVariety = getMoveVariety(move)
				if moveVariety == 'Support'; interrupt = 0
					moveExtraForm = getMoveExtraForm(move)
					if moveExtraForm == 'Enemy'
						statChange = getStatChange(move)
						enemyPokemonStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
						print(myPokemon, 'used', move, 'against the', enemyWording, enemyPokemon, 'and it\'s stats changed by', statChange, '. They are now', enemyPokemonStatStage, '.')
					elif moveExtraForm == 'Self':
						statChange = getStatChange(move)
						myPokemonStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
						print('Your', myPokemon, 'used', move, 'and it\'s stats changed by', statChange, '. They are now', myPokemonStatStage, '.')
					elif moveExtraForm == 'None':
						nonVolatileStatus = getNonVolatileStatusChange(move)
						if nonVolatileStatus == 'Yes':
							nonVolatileStatusType = getNonVolatileStatusType(move)
							nonVolatileStatusChangeChance = getNonVolatileStatusChangeChance(move)
				if moveVariety == 'Physical' or 'Special':
					moveDamage = getMoveDamage(move,myPokemon,myPokemonLevel,myPokemonIV,myPokemonCurrentStatStage,myPokemonNVStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonCurrentStatStage)
					if enemyPokemonHP < 0:
						enemyPokemonHP = 0
					enemyMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV,'Enemy Pokemon'); myMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV,'My Pokemon')					
					print(myPokemon, 'used', move, 'against the', enemyWording, enemyPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', enemyPokemon, 'has', enemyPokemonHP, '/', enemyMaxHP, 'HP remaining!')
					




	preMoveVStatusCheck = getPreMoveVStatusCheck(myPokemonVStatus,myPokemonNVStatusCount)
	preMoveItemCheck = getPreMoveItemCheck(myPokemonItem)


	myPokemonInfo = myTeam[0]; enemyPokemonInfo = enemyTeam[0]
	myPokemon = myPokemonInfo[0]; myPokemonLevel = myPokemonInfo[1]; myPokemonHP = myPokemonInfo[2]; myPokemonIV = myPokemonInfo[3]; myPokemonStatus = myPokemonInfo[4]; myPokemonStatusCount = myPokemonInfo[5]; myPokemonStatStage = myPokemonInfo[6]; myPokemonExp = myPokemonInfo[7]; myPokemonMoveSet = myPokemonInfo[8]
	enemyPokemon = enemyPokemonInfo[0]; enemyPokemonLevel = enemyPokemonInfo[1]; enemyPokemonHP = enemyPokemonInfo[2]; enemyPokemonIV = enemyPokemonInfo[3]; enemyPokemonStatus = enemyPokemonInfo[4]; enemyPokemonStatusCount = enemyPokemonInfo[5]; enemyPokemonStatStage = enemyPokemonInfo[6]; enemyPokemonMoveSet = enemyPokemonInfo[7]
	enemyBattleType = enemyTrainerInfo[0]; enemyTrainerName = enemyTrainerInfo[1]; enemyWording = enemyTrainerInfo[2]
	moveDamage = getMoveDamage(move,myPokemon,myPokemonLevel,myPokemonIV,myPokemonStatStage,myPokemonStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonStatStage)
	myPokemonNonVolatileStatusType = getNonVolatileStatusType(myPokemonStatus)
	enemyPokemonNonVolatileStatusType = getNonVolatileStatusType(enemyPokemonStatus)
	enemyMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV,'Enemy Pokemon')
	myMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV,'My Pokemon')
	hitOrMiss = getHitOrMiss(move)
	moveVariety = getMoveVariety(move)
	effectiveness = getEffectiveness(move,enemyPokemon)
	effectivenessWording = getEffectivesnessWording(effectiveness)

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
				myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage,myPokemonExp,myPokemonMoveSet]
				enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage,enemyPokemonMoveSet]
				myTeam[0] = myPokemonInfo
				enemyTeam[0] = enemyPokemonInfo
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,1]		
	
	if hitOrMiss == 'Miss':
		print(myPokemon, 'used', move, 'but it missed!')
		myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage,myPokemonExp,myPokemonMoveSet]
		enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage,enemyPokemonMoveSet]
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
		if moveExtraForm == 'None':
			nonVolatileStatus = getNonVolatileStatusChange(move)
			if nonVolatileStatus == 'Yes':
				nonVolatileStatusType = getNonVolatileStatusType(move)
				nonVolatileStatusChangeChance = getNonVolatileStatusChangeChance(move)




		myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage,myPokemonExp,myPokemonMoveSet]
		enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage,enemyPokemonMoveSet]
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
	myPokemonNonVolatileStatusType = getNonVolatileStatusType(myPokemonStatus)
	if myPokemonNonVolatileStatusType != 'Nothing':
		if myPokemonNonVolatileStatusType == 'Burned':
			burnDamage = int(myMaxHP / 16)
			myPokemonHP = (myPokemonHP - burnDamage)
			print(myPokemon, 'took', burnDamage, 'HP damage due to it\'s burn! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
		if myPokemonNonVolatileStatusType == 'Poisoned':
			poisonDamage = int(myMaxHP / 8)
			myPokemonHP = (myPokemonHP - poisonDamage)
			print(myPokemon, 'took', poisonDamage, 'HP damage due to being poisoned! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
		if myPokemonNonVolatileStatusType == 'Toxic':
			myPokemonStatusCount = myPokemonStatusCount + 1
			toxicDamage = int(myMaxHP * myPokemonStatusCount / 16)
			myPokemonHP = myPokemonHP - toxicDamage
			print(myPokemon, 'took', toxicDamage, 'HP damage due to being badly poisoned! It has', myPokemonHP, '/', myMaxHP, 'HP remaining!')
	myPokemonInfo = [myPokemon,myPokemonLevel,myPokemonHP,myPokemonIV,myPokemonStatus,myPokemonStatusCount,myPokemonStatStage,myPokemonExp,myPokemonMoveSet]
	enemyPokemonInfo = [enemyPokemon,enemyPokemonLevel,enemyPokemonHP,enemyPokemonIV,enemyPokemonStatus,enemyPokemonStatusCount,enemyPokemonStatStage,enemyPokemonMoveSet]
	myTeam[0] = myPokemonInfo
	enemyTeam[0] = enemyPokemonInfo
	return [myTeam,enemyTeam]