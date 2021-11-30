from choicesFunctions import getOption
from spritesAll import screenBot, screenEmp, screenMid, screenTop
from textTools import getExtraSpace, onlyTextBox, printWithScreenSides, printWithScreenSidesAndSpacing

def optionsScreen(data):
    while True:
        print(screenTop)
        title = "OPTIONS"
        printWithScreenSidesAndSpacing(title + getExtraSpace(title, 52))
        optionsLines = []
        count = 1
        allSettings = data.settings.settings.copy()
        allSettings.append("Back")
        for setting in allSettings:
            if setting == "Back":
                toggleText = ""
            elif data.settings.settingsDict[setting] == True:
                toggleText = "Enabled"
            else:
                toggleText = "Disabled"
            settingText = str(count) + ' - ' + setting
            lineText = settingText + getExtraSpace(settingText, 20) + getExtraSpace(toggleText, 10) + toggleText
            printWithScreenSidesAndSpacing(lineText + getExtraSpace(lineText, 52))
            count += 1
        for _ in range(18 - count):
            print(screenEmp)
        print(screenMid)
        onlyTextBox("Which option would you like to toggle?")
        option = getOption(allSettings)
        if option == "Back":
            return
        else:
            toggleSetting(data, option)
        checkChecks(data)



def toggleSetting(data, option):
    if data.settings.settingsDict[option] == True:
        data.settings.settingsDict[option] = False
    else:
        data.settings.settingsDict[option] = True

def checkChecks(data):
    if data.settings.settingsDict["Skip Story"] == True:
        data.story.oakSpeechCompleted = True
        data.story.startPokemonChosen = True
        data.story.starterRivalFightCompleted = True