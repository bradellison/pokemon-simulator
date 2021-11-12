
from classes import Enemy, Pokemon

#oakTeam = [Pokemon('Pidgeot',61,['Wing Attack','Mirror Move','Sky Attack','Whirlwind']),Pokemon('Alakazam',59,['Psybeam','Psychic','Reflect','Recover']),Pokemon('Rhydon',61,['Leer','Tail Whip','Fury Attack','Horn Drill']),Pokemon('Exeggutor',63,['Hypnosis','Barrage','Stomp']),Pokemon('Arcanine',61,['Roar','Leer','Ember','Take Down']),Pokemon('Blastoise',65,['Hydro Pump','Blizzard','Bite','Withdraw'])]
oakTeam = [Pokemon('Pidgeot',61,['Wing Attack','Mirror Move','Sky Attack','Whirlwind'])]
enemyOak = Enemy("Badman", "Oak", oakTeam, 10000, "ppp", [12,19], 3, "Up")
palletTownEnemies = [enemyOak]



## VIRIDIAN FOREST ##
bugCatcherRickTeam = [Pokemon('Weedle', 7, 'Random'), Pokemon('Caterpie', 7, 'Random')]
bugCatcherRick = Enemy("Bug Catcher", "Rick", bugCatcherRickTeam, 72, "You bug me!", [33,37], 3, "Down")
bugCatcherDougTeam = [Pokemon('Weedle', 7, 'Random'), Pokemon('Kakuna', 7, 'Random'), Pokemon('Weedle', 7, 'Random')]
bugCatcherDoug = Enemy("Bug Catcher", "Doug", bugCatcherDougTeam, 84, "You bug me!", [35,23], 3, "Down")
bugCatcherAnthonyTeam = [Pokemon('Caterpie', 7, 'Random'), Pokemon('Caterpie', 8, 'Random')]
bugCatcherAnthony = Enemy("Bug Catcher", "Anthony", bugCatcherAnthonyTeam, 84, "You bug me!", [31,5], 3, "Down")
bugCatcherCharlieTeam = [Pokemon('Metapod', 7, 'Random'), Pokemon('Caterpie', 7, 'Random'), Pokemon('Metapod', 7, 'Random')]
bugCatcherCharlie = Enemy("Bug Catcher", "Charlie", bugCatcherCharlieTeam, 84, "You bug me!", [13,6], 3, "Down")
bugCatcherSammyTeam = [Pokemon('Weedle', 9, 'Random')]
bugCatcherSammy = Enemy("Bug Catcher", "Sammy", bugCatcherSammyTeam, 84, "You bug me!", [6,23], 3, "Down")
viridianForestEnemies = [bugCatcherRick, bugCatcherDoug, bugCatcherAnthony, bugCatcherCharlie, bugCatcherSammy]




allTownEnemies = {"Pallet Town": palletTownEnemies, "Viridian Forest": viridianForestEnemies}