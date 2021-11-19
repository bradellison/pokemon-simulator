from colorama import Fore, Back, Style, init

init()

overscore = chr(175)

screenTop = '/------------------------------------------------------\\'
screenBot = '\\------------------------------------------------------/'

treeCol = [
' ' + Fore.GREEN + '@@@@' + Style.RESET_ALL + ' ',
Fore.GREEN + '@@@@@@' + Style.RESET_ALL,
'  ||  '
]

waterCol = [
Fore.BLUE + Style.BRIGHT + '~~~~~~' + Style.RESET_ALL,
Fore.BLUE + Style.BRIGHT + '~~~~~~' + Style.RESET_ALL,
Fore.BLUE + Style.BRIGHT + '~~~~~~' + Style.RESET_ALL
]

grassCol = [
Fore.GREEN + '^/^/^/' + Style.RESET_ALL,
Fore.GREEN + '/^/^/^' + Style.RESET_ALL,
Fore.GREEN + '^/^/^/' + Style.RESET_ALL
]

shortGrassCol = [
Fore.GREEN + ' `  ` ' + Style.RESET_ALL,
Fore.GREEN + '   ` `' + Style.RESET_ALL,
Fore.GREEN + '` `   ' + Style.RESET_ALL
]

tree = [
' @@@@ ',
'@@@@@@',
'  ||  '
]

water = [
'~~~~~~',
'~~~~~~',
'~~~~~~'
]

grass = [
'^/^/^/',
'/^/^/^',
'^/^/^/'
]

shortGrass = [
' `  ` ',
'   ` `',
'` `   '
]

sign = [
',----,',
'[____|',   
'    ||'
]

ledge = [
'      ',
'      ',
'======'
]

empty = [
'      ',
'      ',
'      '
]

emptyStorySpot = [
'      ',
'      ',
'      '
]

houseLeft = [
'|-----',
'|-----',
'|-----'
]

houseRight = [
'-----|',
'-----|',
'-----|'
]

houseMiddleWindow = [
'------',
'-[  ]-',
'------'
]

houseMiddle = [
'------',
'------',
'------'
]

gymText = [
'------',
'-GYM--',
'------'
]

pokemonCentreText = [
'------',
'-POKÉ-',
'------'
]

martText = [
'------',
'-MART-',
'------'
]

houseDoor = [
'--__--',
'-|  |-',
'-|  |-'
]

roofLeft = [
'  ____',
' /__/_',
'/__/__'
]

roofMid = [
'______',
'______',
'______'
]

roofRight = [
'____  ',
'_\\__\\ ',
'__\\__\\',
]

bollard = [
'/\\/\\/\\',
'||||||',
'||||||'
]

boulder = [
'(_)(_)',
'(_)(_)',
'(_)(_)'
]

boulderSide = [
'(_)(_)',
'(_)(_)',
'(_)(_)'
]

insideWallTop = [
'------',
'______',
'======'
]

insideWallBottom = [
'______',
'      ',
'______'
]

insideVerticalWallRight = [
'|     ',
'|     ',
'|     '
]

insideVerticalWallLeft = [
'     |',
'     |',
'     |'
]

bookcase = [
'[____]',
'[____]',
'[====]'
]

doormat = [
'      ',
'======',
'======'
]

ballOnGround = [
'  __  ',
' (-o) ',
'  ' + overscore + overscore + '  '
]

ballOnTableLeft = [
'|' + overscore + '__' + overscore + overscore,
'|(-o) ',
'|_' + overscore + overscore + '__'
]

ballOnTableMiddle = [
overscore + overscore + '__' + overscore + overscore,
' (-o) ',
'__' + overscore + overscore + '__'
]

ballOnTableRight = [
overscore + overscore + '__' + overscore + '|',
' (-o)|',
'__' + overscore + overscore + '_|'
]

plantPot = [
'__||__',
'| || |',
' \\__/ '
]

plantTop = [
Fore.GREEN + '@@' + Style.RESET_ALL + '  ' + Fore.GREEN +  '@@' + Style.RESET_ALL,
' ' + Fore.GREEN + '@@@@' + Style.RESET_ALL + ' ',
Fore.GREEN + '@@' + Style.RESET_ALL + '||' + Fore.GREEN +  '@@' + Style.RESET_ALL,
]

tableLeft = [
'|' + overscore + overscore + overscore + overscore + overscore,
'|_____',
'||    '
]

tableMiddle = [
overscore + overscore + overscore + overscore + overscore + overscore,
'______',
'      '
]

TableRight = [
overscore + overscore + overscore + overscore + overscore + '|',
'_____|',
'    ||'
]

TableRightAction = [
overscore + overscore + overscore + overscore + overscore + '|',
'_____|',
'    ||'
]

treetrunk = [
'  __  ',
' |  | ',
'/____\\'
]

bigTreeBottomLeft = [
'@@@@@@',
' @@@@@',
'   /__'
]

bigTreeBottomRight = [
'@@@@@@',
'@@@@@ ',
'__\\   '
]

bigTreeTopLeft = [
'   @@@',
' @@@@@',
'@@@@@@',
]

bigTreeTopRight = [
'@@@   ',
'@@@@@ ',
'@@@@@@'
]

healMachineBottomLeft = [
' _|   ',
'/_|   ',
'/ |___'
]

healMachineBottomRight = [
'   |_ ',
'   |_\\',
'___| \\'
]

healMachineTopLeft = [
'   ___',
'   |  ',
'  /|__',
]

healMachineTopRight = [
'___   ',
'  |   ',
'__|\\  '
]




environmentSpriteDict = {
'?': emptyStorySpot,
'@': tree,
'~': water,
'%': grass,
'=': ledge, 
' ': empty, 
'[': houseLeft, 
']': houseRight, 
'D': houseDoor, 
'd': doormat,
'p': plantPot,
'P': plantTop,
'-': houseMiddleWindow,
'h': houseMiddle,
'G': gymText,
'$': martText,
'<': pokemonCentreText,
'g': shortGrass, 
'S': sign, 
'b': bollard, 
'{': roofLeft, 
'_': roofMid, 
'}': roofRight, 
'B': boulder, 
'L': boulderSide,
'w': insideWallTop,
'W': insideWallBottom,
'm': insideVerticalWallLeft,
'M': insideVerticalWallRight,
'o': ballOnGround,
'q': ballOnTableMiddle,
'O': ballOnTableLeft,
'Q': ballOnTableRight,
'c': bookcase,
'r': tableLeft,
't': tableMiddle,
'y': TableRight,
'R': TableRightAction,
'T': treetrunk,
'u': bigTreeTopLeft,
'i': bigTreeTopRight,
'j': bigTreeBottomLeft,
'k': bigTreeBottomRight,
'U': healMachineTopLeft,
'I': healMachineTopRight,
'J': healMachineBottomLeft,
'K': healMachineBottomRight
}
