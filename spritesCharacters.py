
overscore = chr(175)

you = [
'  o~  ',
' (//) ',
'  ||  '
]

youDown = [
"  ⪽⪾  ",
" (||) ",
"  ⌋⌊  "
]

youRight = [
"  ⪾⪾  ",
" (||\\ ",
"  ⌊⌊  "]

youLeft = [
"  ⪽⪽  ",
" /||) ",
"  ⌋⌋  "]

youUp = [
"  ⫏⫐  ",
" (||) ",
"  ⌋⌊  "
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

enemyCharDown = [
'  *~  ',
' (!V) ',
'  ||  '
]

enemyCharUp = [
'  *~  ',
' (!^) ',
'  ||  '
]

enemyCharDown = [
'  *~  ',
' (!v) ',
'  ||  '
]

enemyCharLeft = [
'  *~  ',
' (!<) ',
'  ||  '
]

enemyCharRight = [
'  *~  ',
' (!>) ',
'  ||  '
]

enemyChars = {"Down": enemyCharDown, "Up": enemyCharUp, "Left": enemyCharLeft, "Right": enemyCharRight}
youChars = {"Down": youDown, "Up": youUp, "Left": youLeft, "Right": youRight}

enemyBattleStartSign = [
'.----.',
'| !! |',
overscore + overscore + "\/" + overscore + overscore
]

characterSpriteDict = {
    'Y': youChars, 
    '^': rival,
    '0': oak,
    '+': nurseJoy,
    '*': enemyChars,
    '!': enemyBattleStartSign
}