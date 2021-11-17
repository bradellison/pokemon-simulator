from gameMaps import locationMapDict
from warpData import getLocationWarpZones
from enemyData import allTownEnemies

def getLocationEnemies(location):
    if location in allTownEnemies:
        return allTownEnemies[location]
    else:
        return []

