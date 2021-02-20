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
'     b    b  b    b     ',
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
'@@@@@@@@@@@%%@@@@@@@@@@@',
'@@@@@@@@@@@%%@@@@@@@@@@@',
'@@@@@@@@@@@%%@@@@@@@@@@@',
'@@@@@@@@@@@%%@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@@'
]


palletTownMap = [
'@@@@@@@@@    @%%@    @@@@@@@',
'@@@@@@@@@    @%%@    @@@@@@@',
'@@@@@@@@@    @%%@    @@@@@@@',
'@@@@@@@@@@@@@@%%@@@@@@@@@@@@',
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
'BBBBBBBBBL@@@@@@@@@@b  @@@@@@@@@@@@@@@@@@@@@@',
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
'                  b    b  b    b        @@@@@',
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
'@@@@@@@@@@b  @@@@@@@',
'@@@@@@@@@@b  @@@@@@@',
'@@@@@@@@@@b  @@@@@@@',
'@@@@@@@@@@b  S@@@@  ',
'@@@@@@@@@@b   @@@@  ',
'@@@@@@@@@@b         '
]

viridianForestEntrance = [
'                    ',
'                    ',
'                    ',
'                    ',
'     mwwwDDwwwM     ',
'     mPP    PPM     ',
'     mpp    ppM     ',
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

viridianForestMap = [
'                                          ',
'                                          ',
'                                          ',
'    wDDw                                  ',
'    T  TuiTTTTTTTTuiTTTTTTTTTTTTTTTTTT    ',
'    T STjk        jk                 T    ',
'    T  Tui        ui                 T    ',
'    T  Tjk        jk    TTTTTTTTTT   T    ',
'    T  Tui   TT   ui   TuiuiuiuiuiT  T    ',
'    T  Tjk   TT   jk   TjkjkjkjkjkT  T    ',
'    T%%Tui%%%TT%%%ui%%%TuiuiuiuiuiT  T    ',
'    T%%Tjk%%%TT%%%jk%%%TjkjkjkjkjkT  T    ',
'    T%%Tui%%%TT%%%ui%%%%%%%%         T    ',
'    T%%Tjk%%%TT%%%jk%%%%%%%%         T    ',
'    T%%Tui%%%TT%%%ui%%%TuiuiT  Tui%%%T    ',
'    T%%Tjk%%%TT%%%jk%%%TjkjkT  Tjk%%%T    ',
'    T%%Tui%%%TT%%%ui%%%TuiuiT  Tui%%%T    ',
'    T%%Tjk%%%TT%%%jk%%%TjkjkT  Tjk%%%T    ',
'    T%%Tui%%%TT%%%ui%%%TuiuiT  Tui%%%T    ',
'    T%%Tjk%%%TT%%%jk%%%TjkjkT  Tjk%%%T    ',
'    T%%Tui%%%TT%%%  %%%TuiuiT  Tui%%%T    ',
'    T%%Tjk%%%TT%%%  %%%TjkjkT STjk%%%T    ',
'    T%%Tui%%%TT        TuiuiT        T    ',
'    T%%Tjk%%%TT        TjkjkT        T    ',
'    T%%Tui%%%TuiuiuiuiuiuiuiT%%%uiT  T    ',
'    T%%Tjk%%%TjkjkjkjkjkjkjkT%%%jkT  T    ',
'    T%%%  %%%TuiuiuiuiuiuiuiT%%%uiT  T    ',
'    T%%%  %%%TjkjkjkjkjkjkjkT%%%jkT  T    ',
'    T   S        TuiuiuiuiuiT%%%uiT  T    ',
'    T            TjkjkjkjkjkT%%%jkT  T    ',
'    uiuiuiuiuiT  TuiuiuiuiuiT%%%uiT  T    ',
'    jkjkjkjkjkT  TjkjkjkjkjkT%%%jkT  T    ',
'    uiuiuiuiuiT  TuiuiuiuiuiT%%%uiT  T    ',
'    jkjkjkjkjkT  TjkjkjkjkjkT%%%jkT  T    ',
'    T%%%%%%%%TuiuiuiuiuiuiuiT%%%uiT  T    ',
'    T%%%%%%%%TjkjkjkjkjkjkjkT%%%jkT  T    ',
'    uiuiui  %%%%%%%%S %TuiuiT%       T    ',
'    jkjkjk  %%%%%%%%  %TjkjkT%       T    ',
'    uiuiui  %TuiuiT%  %TuiuiT%  uiuiui    ',
'    jkjkjk  %TjkjkT%  %TjkjkT%  jkjkjk    ',
'    uiuiui  %TuiuiT%  %TuiuiT%  uiuiui    ',
'    jkjkjk  %TjkjkT%  %TjkjkT%  jkjkjk    ',
'    uiuiui  %TuiuiT%  %TuiuiT%  uiuiui    ',
'    jkjkjk  %TjkjkT%  %TjkjkT%  jkjkjk    ',
'    T%%%%%  %%%%%%%%  %%%%%%%%  %%%%%T    ',
'    T%%%%%  %%%%%%%%ui%%%%%%%%  %%%%%T    ',
'    T%%%%%          jk          %%%%%T    ',
'    T%%%%%                      %%%%%T    ',
'    uiuiuiuiuiuiuiT    Tuiuiuiuiuiuiui    ',
'    jkjkjkjkjkjkjkT    Tjkjkjkjkjkjkjk    ',
'    uiuiuiuiuiuiuiT    Tuiuiuiuiuiuiui    ',
'    jkjkjkjkjkjkjkTTddTTjkjkjkjkjkjkjk    ',
'                                          ',
'                                          ',
'                                          ',
'                                          '
]

viridianForestExit = [
'                    ',
'                    ',
'                    ',
'                    ',
'     mwwwDDwwwM     ',
'     mPP    PPM     ',
'     mpp    ppM     ',
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


locationMapDict = {'Oak Lab': oakLabMap, 'Pallet Town': palletTownMap, 'Route 1': routeOneMap, 'Viridian City': viridianCityMap, 'Viridian Center': viridianCentreMap, 'Route 2': routeTwoMap, 'Viridian Forest': viridianForestMap, 'Viridian Forest Entrance': viridianForestEntrance, 'Viridian Forest Exit': viridianForestExit}

#locationMapDict = {'Pallet Town': palletTownMap, 'Route 1': routeOneMap, 'Route 2': routeTwoMap, 'Viridian City': viridianCityMap, 'Viridian Forest': viridianForestMap, 'Route 22': routeTwentyTwoMap, 'Pewter City': pewterCityMap}
