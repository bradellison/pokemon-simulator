#PokemonInfo = [["Pok1Name", Poke1Lvl, ["Poke1Mov1", "Poke1Mov2"]], "Pok2Name", Poke2Lvl, ["Poke2Mov1", "Poke2Mov2"]]]
#enemyInfo = ["Class", "Name", team, prizeMoney, "EndBattleText", "coordinates", viewDistance, "viewDirection"]



## PALLET TOWN ##
oakTeam = [['Pidgeot',61,['Wing Attack']],['Pidgeot',61,['Wing Attack','Mirror Move','Sky Attack','Whirlwind']]]
#oakTeam = [['Pidgeot', 61, ['Wing Attack']]]
enemyOak = ["Badman", "Oak", oakTeam, 10000, "Student becomes the master, eh?", [12,19], 3, "Right"]

#palletTownEnemies = [enemyOak]
palletTownEnemies = []


## VIRIDIAN FOREST ##
bugCatcherRickTeam = [['Weedle', 7, 'Random'], ['Caterpie', 7, 'Random']]
bugCatcherRick = ["Bug Catcher", "Rick", bugCatcherRickTeam, 72, "You bug me!", [33,37], 3, "Down"]
bugCatcherDougTeam = [['Weedle', 7, 'Random'], ['Kakuna', 7, 'Random'], ['Weedle', 7, 'Random']]
bugCatcherDoug = ["Bug Catcher", "Doug", bugCatcherDougTeam, 84, "You bug me!", [35,23], 3, "Down"]
bugCatcherAnthonyTeam = [['Caterpie', 7, 'Random'], ['Caterpie', 8, 'Random']]
bugCatcherAnthony = ["Bug Catcher", "Anthony", bugCatcherAnthonyTeam, 84, "You bug me!", [31,5], 3, "Down"]
bugCatcherCharlieTeam = [['Metapod', 7, 'Random'], ['Caterpie', 7, 'Random'], ['Metapod', 7, 'Random']]
bugCatcherCharlie = ["Bug Catcher", "Charlie", bugCatcherCharlieTeam, 84, "You bug me!", [13,5], 3, "Down"]
bugCatcherSammyTeam = [['Weedle', 9, 'Random']]
bugCatcherSammy = ["Bug Catcher", "Sammy", bugCatcherSammyTeam, 84, "You bug me!", [6,23], 3, "Down"]
viridianForestEnemies = [bugCatcherRick, bugCatcherDoug, bugCatcherAnthony, bugCatcherCharlie, bugCatcherSammy]



## PEWTER GYM ##
camperLiamTeam = [["Geodude", 10, 'Random'], ['Sandshrew', 11, 'Random']]
camperLiam = ["Camper", "Liam", camperLiamTeam, 220, "You might be better than me, but you won't beat Brock!", [7,10], 3, "Right"]
gymLeaderBrockTeam = [["Geodude", 12, "Random"], ["Onix", 14, "Random"]]
gymLeaderBrock = ["Gym Leader", "Brock", gymLeaderBrockTeam, 1400, "Wow, what a fight! Here, take this Boulder Badge!", [10,7], 0, "Down"]
pewterGymEnemies = [camperLiam, gymLeaderBrock]

allTownEnemies = {"Pallet Town": palletTownEnemies, "Viridian Forest": viridianForestEnemies, "Pewter Gym": pewterGymEnemies}