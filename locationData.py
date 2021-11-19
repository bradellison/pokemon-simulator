from gameMaps import locationMapDict
from warpData import getLocationWarpZones
from enemyData import allTownEnemies
from signData import allSignDict

def getLocationEnemies(location):
    if location in allTownEnemies:
        return allTownEnemies[location]
    else:
        return []

