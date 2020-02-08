




print('/------------------------------------------------------\\')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('\\-----------------------------------------------------/')

treeTop = ' @@@@ '
treeMid = '@@@@@@'
treeBot = '  ||  '

waterTop = '~~~~~~'
waterMid = '~~~~~~'
waterBot = '~~~~~~'



print('/------------------------------------------------------\\')
print('|' + treeTop + treeTop + treeTop + '                            |')
print('|' + treeMid + treeMid + treeMid + '                      |')
print('|' + treeTop + treeTop + treeTop + '                            |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('|                                                      |')
print('\\-----------------------------------------------------/')



map = [
'TTTTTTTTT',
'TTTTWTTTT',
'TTWWWWTTT',
'TTTWWWWTT',
'TTTTWWTTT',
'TTTTTTTTT',
'TTTTTTTTT'
]

tree = [treeTop, treeMid, treeBot] 
water = [waterTop, waterMid, waterBot]

spriteDict = {'T': tree, 'W': water}


for line in map:
    yAxis = 0
    for location in range(3):
        currentLineDraw = '' 
        for sprite in line:
            currentLineDraw += (spriteDict[sprite][location])
        print(currentLineDraw)
    location += 1
