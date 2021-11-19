from time import sleep
from topLevelChoices import startGame, testFunction

loading = 'LOADING...'
for i in range(len(loading)):
    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.05)

startGame()
testFunction()

