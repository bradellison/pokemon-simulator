
from choicesFunctions import getOption
from options import optionsScreen
from drawOverworld import drawOverworld
from saveDataFunctions import saveGame
from screenPokemonSelection import openPokemonSelectionScreen
from bagFunctions import openBag
from text import worldText


def chooseFromMenu(data):
    while True:
        choices = "Pokedex", "Pokemon", "Bag", "Player", "Save", "Options", "Exit"
        choice = getOption(["Pokedex", "Pokemon", "Bag", "Player", "Save", "Options", "Exit"])
        if choice == "Pokedex":
            print("Pokedex")
            worldText(data, "Sorry, this is not yet available!", menu=True, response=True)
        elif choice == "Pokemon":
            if data.story.startPokemonChosen or data.settings.settingsDict["WallClip"]:
                openPokemonSelectionScreen(data)
                drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map, text=False, menu=True)
            else:
                worldText(data, "You do not have any Pokemon yet!", menu=True, response=True)
        elif choice == "Bag":
            openBag(data)
            drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map, text=False, menu=True)
        elif choice == "Player":
            print("Player")
            worldText(data, "Sorry, this is not yet available!", menu=True, response=True)
        elif choice == "Save":
            saveGame(data)
            worldText(data, "Your game has been saved successfully!", menu=True, response=True)
        elif choice == "Options":
            optionsScreen(data)
            drawOverworld(data, data.player.xCo, data.player.yCo, data.environment.location.map, text=False, menu=True)
        elif choice == "Exit" or choice == "Back":
            print("Exit")
            return "Exit"

