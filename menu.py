
from choicesFunctions import getOption
from saveDataFunctions import saveGame
from text import worldText


def chooseFromMenu(data):
    choices = "Pokedex", "Pokemon", "Bag", "Player", "Save", "Options", "Exit"
    choice = getOption(["Pokedex", "Pokemon", "Bag", "Player", "Save", "Options", "Exit"])
    if choice == "Pokedex":
        print("Pokedex")
        worldText(data, "Sorry, this is not yet available!", menu=True)
    elif choice == "Pokemon":
        print("Pokemon")
        worldText(data, "Sorry, this is not yet available!", menu=True)
    elif choice == "Bag":
        print("Bag")
        worldText(data, "Sorry, this is not yet available!", menu=True)
    elif choice == "Player":
        print("Player")
        worldText(data, "Sorry, this is not yet available!", menu=True)
    elif choice == "Save":
        saveGame(data)
        worldText(data, "Your game has been saved successfully!", menu=True)
    elif choice == "Options":
        print("Options")
        worldText(data, "Sorry, this is not yet available!", menu=True)
    elif choice == "Exit":
        print("Exit")
        return "Exit"
    return "Menu"

