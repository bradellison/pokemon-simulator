from classes import Pokemon
from classes import Ball

from battleFunctions import startBattle
from choicesFunctions import getOptionOneOrTwoOrThree
from overworldFunctions import directionChoice
import time

def mainGame(data, newOrContinue):
    while True:
        if newOrContinue == 1:
            oakSpeech(data)
        directionChoice(data)

def oakSpeech(data):
    print('Oak: Hello and welcome to the wonderful world of Pokemon!'); time.sleep(1)
    print('Oak: My name is Professor Oak! What\'s your name?')
    data.player.name = chooseCharacterName()
    print('Oak: Ah yes, lovely to meet you. My grandson lives closeby too, any idea what his name is?')
    data.rival.name = chooseCharacterName()
    print('Oak: Of course, now I remember! Now let\'s get down to business.'); time.sleep(1)
    print('Oak: I\'d like you to take one of these Pokemon here and see how you get on in the world on Pokemon!'); time.sleep(1)
    print('Oak: Now', data.player.name + ',', data.rival.name + ', I\'d like to give you each a Pokemon!'); time.sleep(1)
    print(data.rival.name + ': Yeah! Thanks Grandpa!'); time.sleep(1)
    print('Oak: Hold on', data.rival.name + ', let', data.player.name, 'choose first. Which one would you like?'); time.sleep(1)
    pokemonChoice = getOptionOneOrTwoOrThree('Bulbasaur - the grass-type Pokemon.','Charmander - the fire-type Pokemon.','Squirtle - the water-type Pokemon.')
    getStarter(data, pokemonChoice)
    print('> Congratulations, you got a', data.player.team[0].name + '! <'); time.sleep(1)
    print(data.rival.name + ': Alright then, I\'ll take the', data.rival.team[0].name + '!'); time.sleep(1)
    print(data.rival.name + ': Now that we\'ve both got Pokemon', data.player.name + ', let\'s fight and see who\'s best!'); time.sleep(1)
    data.enemy = data.rival
    outcome = startBattle(data)
    if outcome == 'Win':
        print(data.rival.name + ': Yeah, okay, beginner\'s luck. Next time I won\'t go so easy on you. Anyway, smell ya later!'); time.sleep(1)
    if outcome == 'Lose':
        print(data.rival.name + ': Just as I expected, easy. Better luck next time. Anyway, smell ya later!'); time.sleep(1)
    print('Oak: In any case', data.player.name + ', great effort! Here, take 5 PokeBalls and go and start your Pokemon adventure!')
    print('> Congratulations, you received 5 PokeBalls!')
    data.bag.balls.append(Ball('PokeBall', 5))

def getStarter(data, number):
    number -= 1
    starters = ['Bulbasaur', 'Charmander', 'Squirtle']
    data.player.defaultTeam = [(Pokemon(starters[number], 5, 'Random'))]
    data.player.team = data.player.defaultTeam
    number += 1
    if number == 3:
        number = 0
    data.rival.team = [(Pokemon(starters[number], 5, 'Random'))]

def chooseCharacterName():
    while True:
        try:
            choiceInput = input('-- ')
            if choiceInput != '':
                return choiceInput
            print('Oak: Sorry, I missed that. Say again?')
        except ValueError:
            print('Oak: Sorry, I missed that. Say again?')

