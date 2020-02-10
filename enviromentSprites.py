from colorama import Fore, Back, Style, init

init()

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

you = [
'  o~  ',
' (//) ',
'  ||  '
]

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

spriteDict = {'@': tree, '~': water, '%': grass, '=': ledge, ' ': empty, 'Y': you, '!': warp, '[': houseLeft, ']': houseRight, 'D':houseDoor, 'K': houseMiddle, 'g': shortGrass, 'S': sign, 'b': bollard, '{': roofLeft, '_': roofMid, '}': roofRight}


print(tree[0])