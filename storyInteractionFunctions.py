from text import text, worldText, worldTextOptions
from choicesFunctions import getOptionOneOrTwoOrThree, getYesOrNo
from classes import Pokemon, Item
from battleFunctions import startBattle
from bagFunctions import getNamePokemon
from pokemonCentreFunctions import healPokemon


def talkGary(data):
    if data.story.oakSpeechCompleted == False:
        pass

def starterBall(data, starter):
    if data.story.oakSpeechCompleted == False:
        worldText(data, 'There are three pokeballs on the table.')
    elif data.story.startPokemonChosen == True:
        worldText(data, 'This is where I got my first Pokemon!')
    else:
        chooseStarter(data, starter)

def chooseStarter(data, starter):
    if starter == 'Bulbasaur':
        outcome = worldTextOptions(data, 'Would you like Bulbasaur, the grass-type Pokemon?', options=["Yes", "No"], response=True)
    elif starter == 'Charmander':
        outcome = worldTextOptions(data, 'Would you like Charmander, the fire-type Pokemon?', options=["Yes", "No"], response=True)
    elif starter == 'Squirtle':
        outcome = worldTextOptions(data, 'Would you like Squirtle, the water-type Pokemon?', options=["Yes", "No"], response=True)
    if outcome == "Yes":
        getStarter(data, starter)
        worldText(data, '> Congratulations, you got a', data.player.team[0].name + '! <')
        getNamePokemon(data, data.player.team[0], battle=False)
        worldText(data, data.rival.name + ': Alright then, I\'ll take the', data.rival.team[0].name + '!')
    
def getStarter(data, starter):
    starters = ['Bulbasaur', 'Charmander', 'Squirtle']
    number = starters.index(starter)
    data.player.defaultTeam = [(Pokemon(starters[number], 5, 'Random'))]
    data.player.team = data.player.defaultTeam
    number += 1
    if number == 3:
        number = 0
    data.rival.team = [(Pokemon(starters[number], 5, 'Random'))]
    data.story.startPokemonChosen = True

def talkOak(data):
    if data.story.oakSpeechCompleted == False:
        oakOpeningMonologue(data)
    elif data.story.startPokemonChosen == False:
        worldText(data, 'Oak: Go ahead and choose one from the table there.')

def talkStarterRivalFight(data):
    worldText(data, data.rival.name + ': Where are you running off to?! Now that we\'ve both got Pokemon', data.player.name + ', let\'s fight and see who\'s best!')
    data.enemy = data.rival
    outcome = startBattle(data)
    if outcome == 'Win':
        text(data, data.rival.name + ': Yeah, okay, beginner\'s luck.')
        worldText(data, data.rival.name + ': Next time I won\'t go so easy on you. Anyway, smell ya later!')
    else:
        text(data, data.rival.name + ': Just as I expected, easy.')
        worldText(data, data.rival.name + ': Better luck next time. Anyway, smell ya later!')
    data.story.starterRivalFightCompleted = True
    worldText(data, 'Oak: In any case', data.player.name + ", great effort! Let me heal your " + data.player.pokemon.name + " up.")
    healPokemon(data.player.pokemon)
    worldText(data, "Here, take 5 PokeBalls and go and start your Pokemon adventure!")
    worldText(data, '> Congratulations, you received 5 PokeBalls!')
    #data.bag.balls.append(Ball('PokeBall', 5))  


#    pokemonChoice = getOptionOneOrTwoOrThree('Bulbasaur - the grass-type Pokemon.','Charmander - the fire-type Pokemon.','Squirtle - the water-type Pokemon.')
#    getStarter(data, pokemonChoice)
#    worldText(data, '> Congratulations, you got a', data.player.team[0].name + '! <')
#    worldText(data, data.rival.name + ': Alright then, I\'ll take the', data.rival.team[0].name + '!')
#    worldText(data, data.rival.name + ': Now that we\'ve both got Pokemon', data.player.name + ', let\'s fight and see who\'s best!')
#    data.enemy = data.rival
#    outcome = startBattle(data)
#    if outcome == 'Win':
#        worldText(data, data.rival.name + ': Yeah, okay, beginner\'s luck. Next time I won\'t go so easy on you. Anyway, smell ya later!')
#    if outcome == 'Lose':
#        worldText(data, data.rival.name + ': Just as I expected, easy. Better luck next time. Anyway, smell ya later!')
#    worldText(data, 'Oak: In any case', data.player.name + ', great effort! Here, take 5 PokeBalls and go and start your Pokemon adventure!')
#    worldText(data, '> Congratulations, you received 5 PokeBalls!')
#    data.bag.balls.append(Ball('PokeBall', 5))

def oakOpeningMonologue(data):
    worldText(data, 'Oak: Hello and welcome to the wonderful world of Pokemon!')
    worldText(data, 'Oak: My name is Professor Oak! What\'s your name?', response=True)
    data.player.name = chooseCharacterName(data)
    worldText(data, 'Oak: Ah yes, lovely to meet you. My grandson lives closeby too, any idea what his name is?', response=True)
    data.rival.name = chooseCharacterName(data)
    worldText(data, data.rival.name + ': Grandpa! Did you forget my name again?!')
    worldText(data, 'Oak: Ahem, no, of course not! I was just joking around. Now let\'s get down to business.')
    worldText(data, 'Oak: Now', data.player.name + ',', data.rival.name + ', I\'d like to give you each a Pokemon, and see how you get on in the world!')
    worldText(data, data.rival.name + ': Yeah! Thanks Grandpa!')
    worldText(data, 'Oak: Hold on', data.rival.name + ', we should let', data.player.name, 'choose first. Go ahead and choose one from the table there.')
    data.story.oakSpeechCompleted = True

def chooseCharacterName(data):
    while True:
        try:
            choiceInput = input('-- ')
            if choiceInput != '':
                return choiceInput
            worldText(data, 'Oak: Sorry, I missed that. Say again?', response=True)
        except ValueError:
            worldText(data, 'Oak: Sorry, I missed that. Say again?', response=True)

