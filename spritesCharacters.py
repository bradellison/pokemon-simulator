
overscore = chr(175)

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

enemyBattleStartSign = [
'.----.',
'| !! |',
overscore + overscore + "\/" + overscore + overscore
]

characterSpriteDict = {
    'Y': you, 
    '^': rival,
    '0': oak,
    '+': nurseJoy,
    '*': enemyChars,
    '!': enemyBattleStartSign
}