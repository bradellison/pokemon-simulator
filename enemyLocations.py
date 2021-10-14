
from classes import Enemy, Pokemon

oakTeam = elite4BlueTeam = [Pokemon('Pidgeot',61,['Wing Attack','Mirror Move','Sky Attack','Whirlwind']),Pokemon('Alakazam',59,['Psybeam','Psychic','Reflect','Recover']),Pokemon('Rhydon',61,['Leer','Tail Whip','Fury Attack','Horn Drill']),Pokemon('Exeggutor',63,['Hypnosis','Barrage','Stomp']),Pokemon('Arcanine',61,['Roar','Leer','Ember','Take Down']),Pokemon('Blastoise',65,['Hydro Pump','Blizzard','Bite','Withdraw'])]
enemyOak = Enemy("Badman", "Oak", oakTeam, 10000, "ppp", [12,19])
palletTownEnemies = [enemyOak]




allTownEnemies = {"Pallet Town": palletTownEnemies}