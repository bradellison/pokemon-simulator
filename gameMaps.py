class MapData(object):
    def __init__(self,position):
        self.grass = []
        self.trees = []
        self.ledges = []
        self.warps = []
        self.players = []

class Tree(object):
    def __init__(self,position):
        self.position = position

class OpenSpace(object):
    def __init__(self,position):
        self.position = position

class Grass(object):
    def __init__(self,position):
        self.position = position

class Ledge(object):
    def __init__(self,position):
        self.position = position

class Warp(object):
    def __init__(self,position):
        self.position = position

overworldMap = [
['xxx','xxx','vrf','xxx','xxx'],
['xxx','xxx','rt2','xxx','xxx'],
['xxx','r22','vrc','xxx','xxx'],
['xxx','xxx','rt1','xxx','xxx'],
['xxx','xxx','plt','xxx','xxx'],
['xxx','xxx','xxx','xxx','xxx'] 
]

locationToMapCodeDict = {'Pallet Town': 'plt', 'Route 1': 'rt1', 'Route 2': 'rt2', 'Viridian City': 'vrc', 'Viridian Forest': 'vrf', 'Route 22': 'r22'}
mapCodeToLocationDict = {'xxx': 'Nothing', 'plt': 'Pallet Town', 'rt1': 'Route 1', 'rt2': 'Route 2', 'vrc': 'Viridian City', 'vrf': 'Viridian Forest', 'r22': 'Route 22'}


T = 'Tree'



water = '~'
tree = '^'
grass = '#'
ledge = '-'
path = ' '
player = 'O'
enemy = 'Q'

routeOne = [
'^^^^^^^^^^^^^^^^^^^^^^^^',
'^^^^^^^^^^^^^^^^^^^^^^^^',
'^^^^^^^^^^^^^^^^^^^^^^^^',
'^^^^^^^^^^^^^^^^^^^^^^^^',
'^^^^^     ^!!^         ^',
'^^^^^     ^  ^     ^^^^^',
'^^^^^^^^^^^  ^^^^^^^^^^^',
'^^^^^              ^^^^^',
'^^^^^              ^^^^^',
'^^^^^     ^        ^^^^^',
'^^^^^-----^----    ^^^^^',
'^^^^^     ^########^^^^^',
'^^^^^     ^########^^^^^',
'^^^^^     ^########^^^^^',
'^^^^^-----^########^^^^^',
'^^^^^              ^^^^^',
'^^^^^              ^^^^^',
'^^^^^          ####^^^^^',
'^^^^^^^----^^^^####^^^^^',
'^^^^^          ####^^^^^',
'^^^^^          ####^^^^^',
'^^^^^              ^^^^^',
'^^^^^              ^^^^^',
'^^^^^              ^^^^^',
'^^^^^- --- --------^^^^^',
'^^^^^              ^^^^^',
'^^^^^              ^^^^^',
'^^^^^        ####  ^^^^^',
'^^^^^^^^^^^^^####--^^^^^',
'^^^^^        ####  ^^^^^',
'^^^^^    O   ####  ^^^^^',
'^^^^^              ^^^^^',
'^^^^^--   ---------^^^^^',
'^^^^^  ####    ####^^^^^',
'^^^^^  ####    ####^^^^^',
'^^^^^####    ####  ^^^^^',
'^^^^^####    ####  ^^^^^',
'^^^^^^^^^^^##^^^^^^^^^^^',
'^^^^^     ^##^     ^^^^^',
'^^^^^     ^##^     ^^^00^^',
'^^^^^     ^##^     ^^^^^',
'^^^^^^^^^^^!!^^^^^^^^^^^',
'^^^^^^^^^^^^^^^^^^^^^^^^',
'^^^^^^^^^^^^^^^^^^^^^^^^',
'^^^^^^^^^^^^^^^^^^^^^^^^',
'^^^^^^^^^^^^^^^^^^^^^^^^'
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in routeOne:
	for col in row:
		if col == "^":
			Tree((x, y))
		if col == "C":
			OpenSpace((x, y))
		if col == "#":
			Grass((x, y))
		if col == "-":
			Ledge((x, y))
		if col == "!":
			Warp((x, y))
		if col == "O":
			Warp((x, y))
		x += 1
	y += 1
	x = 0












