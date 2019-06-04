import math

maxHealth = 100
health = 99


#if health == 100:
#    healthBarPlayer = '===================='

healthPerSpace = int(maxHealth / 20)
spacesFilled = math.ceil(health / healthPerSpace)


healthBarPlayer = ''
spareSpaces = 20
for i in range (spacesFilled):
    healthBarPlayer += '='
    spareSpaces -= 1
for i in range (spareSpaces):
    healthBarPlayer += ' '
healthInDigits = len(str(health)) + len(str(maxHealth))
spaceNeeded = 10 - healthInDigits

extraSpace = ''
for i in range (spaceNeeded):
    extraSpace += ' '

def display():

print('/---------------------------------------------------------------------------\\')
print('|                                                    |       Bulbasaur - L10|')
print('|                                                    |(====================)|')
print('|                                                    \\----------------------|')
print('|                                                                           |')
print('|                                                                           |')
print('|                                                                           |')
print('|                                                                           |')
print('|                                                                           |')
print('|----------------------\\                                                    |')
print('|Charmander - L10      |                                                    |')
print('|(' + healthBarPlayer + ')|                                                    |')
print('|        ' + extraSpace + str(health) + '/' + str(maxHealth) + 'HP |                                                    |')
print('\\---------------------------------------------------------------------------/')
print('|                                                                           |')
print('|                                                                           |')
print('|                                                                           |')
print('|                                                                           |')
print('|                                                                           |')
print('\\---------------------------------------------------------------------------/')

