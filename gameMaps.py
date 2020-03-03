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

palletTownDict = {'Grass': False, 'Water': False, 'Centre': True}
routeOneDict = {'Grass': True, 'Water': False, 'Centre': False}
viridianCityDict = {'Grass': False, 'Water': False, 'Centre': True}
routeTwoDict = {'Grass': True, 'Water': False, 'Centre': False}
routeTwentyTwoDict = {'Grass': True, 'Water': False, 'Centre': False}
viridianForestDict = {'Grass': True, 'Water': False, 'Centre': False}
pewterCityDict = {'Grass': False, 'Water': False, 'Centre': True}




locationToMapCodeDict = {'Pallet Town': 'plt', 'Route 1': 'rt1', 'Route 2': 'rt2', 'Viridian City': 'vrc', 'Viridian Forest': 'vrf', 'Route 22': 'r22', 'Pewter City': 'ptc'}
mapCodeToLocationDict = {'xxx': 'Nothing', 'plt': 'Pallet Town', 'rt1': 'Route 1', 'rt2': 'Route 2', 'vrc': 'Viridian City', 'vrf': 'Viridian Forest', 'r22': 'Route 22', 'ptc': 'Pewter City'}
locationInformationDict = {'Pallet Town': palletTownDict, 'Route 1': routeOneDict, 'Route 2': routeTwoDict, 'Viridian City': viridianCityDict, 'Viridian Forest': viridianForestDict, 'Route 22': routeTwentyTwoDict, 'Pewter City': pewterCityDict}



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
'@@@@@                  @@@@@',
'@@@@@   {__}    {__}   @@@@@',
'@@@@@ gg[KK]  gg[KK]   @@@@@',
'@@@@@ gS[DK]  gS[DK]   @@@@@',
'@@@@@                  @@@@@',
'@@@@@                  @@@@@',
'@@@@@   gggg  {____}   @@@@@',
'@@@@@   bbbS  [KKKK]   @@@@@',
'@@@@@         [KDKK]   @@@@@',
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
'BBBBBBBBBL  bbbbbb@@            [KKKK]  @@@@@',
'BBBBBBBBBL b@@@@@@@@b   b       [KKKK]  @@@@@',
'BBBBBBBBBL b@@@@@@@@b   b      S[KDKK]  @@@@@',
'BBBBBBBBBL b@@@@@@@@b   {__}============@@@@@',
'BBBBBBBBBL b@@@@@@@@b   [DK]            @@@@@',
'BBBBBBBBBL b@@@@@@@@b                   @@@@@',
'BBBBBBBBBL b@@@@@@@@b                   @@@@@',
'LLLLLLLLLL b@@@@@@@@b   bbbbbbbbbbbbbbbb@@@@@',
'    L      b@@@@@@@@b   {__}            @@@@@',
'    !      b@@@@@@@@b   [DK]            @@@@@',
'    !       @@@@@@@@            {__}    @@@@@',
'    L                S  bbbb    [KK]    @@@@@',
'LLLLLLLL                        [KK]    @@@@@',
'BBBBBBBL                        [DK]    @@@@@',
'BBBBBBBL                                @@@@@',
'BBBBBBBL@@@@                            @@@@@',
'BBBBBBBL                  {__}          @@@@@',
'BBBBBBBL    @@            [KK]          @@@@@',
'BBBBBBBL    ~~~~~~        [KK]          @@@@@',
'BBBBBBBL    ~~~~~~        [DK]          @@@@@',
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
'@@@@  [KK]    @@@@  ',
'@@@@bb[DK]bbbb@@@@@=',
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


locationMapDict = {'Pallet Town': palletTownMap, 'Route 1': routeOneMap, 'Viridian City': viridianCityMap, 'Route 2': routeTwoMap}

#locationMapDict = {'Pallet Town': palletTownMap, 'Route 1': routeOneMap, 'Route 2': routeTwoMap, 'Viridian City': viridianCityMap, 'Viridian Forest': viridianForestMap, 'Route 22': routeTwentyTwoMap, 'Pewter City': pewterCityMap}
