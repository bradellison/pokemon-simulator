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
['xxx','xxx','ptc','xxx','xxx'],
['xxx','xxx','vrf','xxx','xxx'],
['xxx','xxx','rt2','xxx','xxx'],
['xxx','r22','vrc','xxx','xxx'],
['xxx','xxx','rt1','xxx','xxx'],
['xxx','xxx','plt','xxx','xxx'],
['xxx','xxx','xxx','xxx','xxx'] 
]

oakLabDict = {'Grass': False, 'Water': False, 'Centre': False}
palletTownDict = {'Grass': False, 'Water': False, 'Centre': True}
routeOneDict = {'Grass': True, 'Water': False, 'Centre': False}
viridianCityDict = {'Grass': False, 'Water': False, 'Centre': True}
viridianCenterDict = {'Grass': False, 'Water': False, 'Centre': True}
routeTwoDict = {'Grass': True, 'Water': False, 'Centre': False}
routeTwentyTwoDict = {'Grass': True, 'Water': False, 'Centre': False}
viridianForestDict = {'Grass': True, 'Water': False, 'Centre': False}
pewterCityDict = {'Grass': False, 'Water': False, 'Centre': True}




locationToMapCodeDict = {'Pallet Town': 'plt', 'Route 1': 'rt1', 'Route 2': 'rt2', 'Viridian City': 'vrc', 'Viridian Forest': 'vrf', 'Route 22': 'r22', 'Pewter City': 'ptc'}
mapCodeToLocationDict = {'xxx': 'Nothing', 'plt': 'Pallet Town', 'rt1': 'Route 1', 'rt2': 'Route 2', 'vrc': 'Viridian City', 'vrf': 'Viridian Forest', 'r22': 'Route 22', 'ptc': 'Pewter City'}
locationInformationDict = {'Oak Lab': oakLabDict, 'Pallet Town': palletTownDict, 'Route 1': routeOneDict, 'Route 2': routeTwoDict, 'Viridian City': viridianCityDict, 'Viridian Center': viridianCenterDict, 'Viridian Forest': viridianForestDict, 'Route 22': routeTwentyTwoDict, 'Pewter City': pewterCityDict}


viridianCentreMap = [
'                    ',
'                    ',
'                    ',
'                    ',
'     mMUIwwwwmM     ',
'     mMJK+   mM     ',
'     mrttRrttyM     ',
'     m        M     ',
'     m        M     ',
'     mPP    PPM     ',
'     mpp    ppM     ',
'     mWWWddWWWM     ',
'                    ',
'                    ',
'                    ',
'                    '
]

oakLabMap = [
'                    ',
'                    ',
'                    ',
'                    ',
'    mwwwwwwwwwwM    ',
'    mryry  ccccM    ',
'    m     0    M    ',
'    mUI  ^ OqQ M    ',
'    mJK        M    ',
'    m          M    ',
'    mcccc??ccccM    ',
'    m          M    ',
'    m          M    ',
'    m          M    ',
'    mWWWWddWWWWM    ',
'                    ',
'                    ',
'                    ',
'                    '
]





routeOneMap = [
'     b    b  b    b     ',
'     b    b  b    b     ',
'     b    b  b    b     ',
'     b    b  b    b     ',
'     b    b!!b    b     ',
'     b    b  b    b     ',
'@@@@@@@@@@@  @@@@@@@@@@@',
'@@@@@              @@@@@',
'@@@@@              @@@@@',
'@@@@@     @        @@@@@',
'@@@@@=====@====    @@@@@',
'@@@@@     @%%%%%%%%@@@@@',
'@@@@@     @%%%%%%%%@@@@@',
'@@@@@     @%%%%%%%%@@@@@',
'@@@@@=====@%%%%%%%%@@@@@',
'@@@@@              @@@@@',
'@@@@@              @@@@@',
'@@@@@          %%%%@@@@@',
'@@@@@@@====@@@@%%%%@@@@@',
'@@@@@          %%%%@@@@@',
'@@@@@          %%%%@@@@@',
'@@@@@              @@@@@',
'@@@@@              @@@@@',
'@@@@@              @@@@@',
'@@@@@= === ========@@@@@',
'@@@@@              @@@@@',
'@@@@@              @@@@@',
'@@@@@        %%%%  @@@@@',
'@@@@@@@@@@@@@%%%%==@@@@@',
'@@@@@        %%%%  @@@@@',
'@@@@@        %%%%  @@@@@',
'@@@@@              @@@@@',
'@@@@@==   =========@@@@@',
'@@@@@  %%%%    %%%%@@@@@',
'@@@@@  %%%%    %%%%@@@@@',
'@@@@@%%%%    %%%%  @@@@@',
'@@@@@%%%%    %%%%  @@@@@',
'@@@@@@@@@@@%%@@@@@@@@@@@',
'@@@@@     @%%@     @@@@@',
'@@@@@     @%%@     @@@@@',
'@@@@@     @%%@     @@@@@',
'@@@@@@@@@@@!!@@@@@@@@@@@',
'@@@@@@@@@@@%%@@@@@@@@@@@',
'@@@@@@@@@@@%%@@@@@@@@@@@',
'@@@@@@@@@@@%%@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@@'
]


palletTownMap = [
'@@@@@@@@@    @%%@    @@@@@@@',
'@@@@@@@@@    @%%@    @@@@@@@',
'@@@@@@@@@    @%%@    @@@@@@@',
'@@@@@@@@@@@@@@!!@@@@@@@@@@@@',
'@@@@@@@@@@@@@@%%@@@@@@@@@@@@',
'@@@@@@@@@@@@@@%%@@@@@@@@@@@@',
'@@@@@@@@@@@@@@%%@@@@@@@@@@@@',
'@@@@@         ??       @@@@@',
'@@@@@   {__}    {__}   @@@@@',
'@@@@@ gg[--]  gg[--]   @@@@@',
'@@@@@ gS[D-]  gS[D-]   @@@@@',
'@@@@@                  @@@@@',
'@@@@@                  @@@@@',
'@@@@@   gggg  {____}   @@@@@',
'@@@@@   bbbS  [----]   @@@@@',
'@@@@@         [-D--]   @@@@@',
'@@@@@         gggggggg @@@@@',
'@@@@@   ~~~~  bbbSbbgg @@@@@',
'@@@@@   ~~~~           @@@@@',
'@@@@@   ~~~~           @@@@@',
'@@@@@   ~~~~           @@@@@',
'@@@@@@@@~~~~@@@@@@@@@@@@@@@@',
'@@@@@@@@~~~~@@@@@@@@@@@@@@@@',
'@@@@@@@@~~~~@@@@@@@@@@@@@@@@',
'@@@@@@@@~~~~@@@@@@@@@@@@@@@@',
]

viridianCityMap = [
'@@@@@@@@@@@@@@@@@@@@b  @@@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@b  @@@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@b  @@@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@b  @@@@@@@@@@@@@@@@@@@@@@',
'BBBBBBBBBL@@@@@@@@@@b!!@@@@@@@@@@@@@@@@@@@@@@',
'BBBBBBBBBL@@@@@@@@@@b  @@@@@@@@@@@@@@@@@@@@@@',
'BBBBBBBBBL@@@@@@@@@@b  S@@@@            @@@@@',
'BBBBBBBBBL@@@@@@@@@@b   @@@@            @@@@@',
'BBBBBBBBBL                      {____}  @@@@@',
'BBBBBBBBBL  bbbbbb@@            [----]  @@@@@',
'BBBBBBBBBL b@@@@@@@@b   b       [----]  @@@@@',
'BBBBBBBBBL b@@@@@@@@b   b      S[-D--]  @@@@@',
'BBBBBBBBBL b@@@@@@@@b   {__}============@@@@@',
'BBBBBBBBBL b@@@@@@@@b   [D-]            @@@@@',
'BBBBBBBBBL b@@@@@@@@b                   @@@@@',
'BBBBBBBBBL b@@@@@@@@b                   @@@@@',
'LLLLLLLLLL b@@@@@@@@b   bbbbbbbbbbbbbbbb@@@@@',
'    L      b@@@@@@@@b   {__}            @@@@@',
'    !      b@@@@@@@@b   [D-]            @@@@@',
'    !       @@@@@@@@            {__}    @@@@@',
'    L                S  bbbb    [--]    @@@@@',
'LLLLLLLL                        [--]    @@@@@',
'BBBBBBBL                        [D-]    @@@@@',
'BBBBBBBL                                @@@@@',
'BBBBBBBL@@@@                            @@@@@',
'BBBBBBBL                  {__}          @@@@@',
'BBBBBBBL    @@            [--]          @@@@@',
'BBBBBBBL    ~~~~~~        [--]          @@@@@',
'BBBBBBBL    ~~~~~~        [D-]          @@@@@',
'BBBBBBBL    ~~~~~~                      @@@@@',
'LLLLLLLL====~~~~~~= === ================@@@@@',
'       b                                @@@@@',
'       b                 S              @@@@@',
'       b                                @@@@@',
'       bbbbbbbbbbbbbbbbb  bbbbbbbbbbbbbb@@@@@',
'                  b    b  b    b        @@@@@',
'                  b    b  b    b        @@@@@',
'                  b    b!!b    b        @@@@@',
'                  b    b  b    b        @@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@              @@@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@              @@@@@@@@@@@@@'
]


routeTwoMap = [
'@@@@  @ @     @@@@  ',
'@@@@  {__}    @@@@  ',
'@@@@  [--]    @@@@  ',
'@@@@bb[D-]bbbb@@@@@=',
'@@@@           @    ',
'@@@@           @    ',
'@@@@           @    ',
'@@@@========   @    ',
'@@@@    %%%%%% @    ',
'@@@@    %%%%%% @====',
'@@@@    %%%%%% @    ',
'@@@@    %%%%%% @    ',
'@@@@            @   ',
'@@@@      @@@@@@@@  ',
'@@@@     @@@@@@@@   ',
'@@@@     @@@@@@@@   ',
'@@@@      @@@@@@@   ',
'@@@@            @   ',
'@@@@            @   ',
'@@@@            @   ',
'@@@@@@          @   ',
'@@@@@@===== ====@@= ',
'@@@@@@          @   ',
'@@@@@@          @   ',
'@@@@@@          @   ',
'@@@@@@    S     @   ',
'@@@@@@          @   ',
'@@@@@@          @   ',
'@@@@@@          @   ',
'@@@@@@        @@@@@@',
'@@@@@@@@@@b  @@@@@@@',
'@@@@@@@@@@b!!@@@@@@@',
'@@@@@@@@@@b  @@@@@@@',
'@@@@@@@@@@b  @@@@@@@',
'@@@@@@@@@@b  @@@@@@@'
]

viridianForestMap = [


]




locationMapDict = {'Oak Lab': oakLabMap, 'Pallet Town': palletTownMap, 'Route 1': routeOneMap, 'Viridian City': viridianCityMap, 'Viridian Center': viridianCentreMap, 'Route 2': routeTwoMap, 'ViridianForest': viridianForestMap}

#locationMapDict = {'Pallet Town': palletTownMap, 'Route 1': routeOneMap, 'Route 2': routeTwoMap, 'Viridian City': viridianCityMap, 'Viridian Forest': viridianForestMap, 'Route 22': routeTwentyTwoMap, 'Pewter City': pewterCityMap}
