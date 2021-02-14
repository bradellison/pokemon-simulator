from colorama import Fore, Back, Style, init

init()

overscore = chr(175)

screenTop = '/------------------------------------------------------\\'
screenBot = '\\------------------------------------------------------/'

tree = [
' ' + Fore.GREEN + '@@@@' + Style.RESET_ALL + ' ',
Fore.GREEN + '@@@@@@' + Style.RESET_ALL,
'  ||  '
]

water = [
Fore.BLUE + Style.BRIGHT + '~~~~~~' + Style.RESET_ALL,
Fore.BLUE + Style.BRIGHT + '~~~~~~' + Style.RESET_ALL,
Fore.BLUE + Style.BRIGHT + '~~~~~~' + Style.RESET_ALL
]

grass = [
Fore.GREEN + '^/^/^/' + Style.RESET_ALL,
Fore.GREEN + '/^/^/^' + Style.RESET_ALL,
Fore.GREEN + '^/^/^/' + Style.RESET_ALL
]

shortGrass = [
Fore.GREEN + ' `  ` ' + Style.RESET_ALL,
Fore.GREEN + '   ` `' + Style.RESET_ALL,
Fore.GREEN + '` `   ' + Style.RESET_ALL
]

#tree = [
#' @@@@ ',
#'@@@@@@',
#'  ||  '
#]

#water = [
#'~~~~~~',
#'~~~~~~',
#'~~~~~~'
#]

#grass = [
#'^/^/^/',
#'/^/^/^',
#'^/^/^/'
#]

#shortGrass = [
#' `  ` ',
#'   ` `',
#'` `   '
#]

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

you = [
'  o~  ',
' (//) ',
'  ||  '
]

rival = [
'  o~  ',
' <{}> ',
'  ||  '
]

oak = [
'  0~  ',
' ({}\ ',
'  ||  '
]

#you = [
#'o~',
#'(//)',
#'||'
#]

warp = [
'      ',
' WARP ',
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

houseMiddle = [
'------',
'-[  ]-',
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
'      '
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


spriteDict = {
'?': emptyStorySpot,
'@': tree,
'~': water,
'%': grass,
'=': ledge, 
' ': empty, 
'Y': you, 
'^': rival,
'0': oak,
'!': warp, 
'[': houseLeft, 
']': houseRight, 
'D': houseDoor, 
'K': houseMiddle, 
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
'c': bookcase}
