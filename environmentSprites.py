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
' ({}\\ ',
'  ||  '
]

nurseJoy = [
'  o~  ',
' (::) ',
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

colSpriteDict = {
    
}

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
'd': doormat,
'p': plantPot,
'P': plantTop,
'-': houseMiddle, 
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
'+': nurseJoy,
'U': healMachineTopLeft,
'I': healMachineTopRight,
'J': healMachineBottomLeft,
'K': healMachineBottomRight
}
