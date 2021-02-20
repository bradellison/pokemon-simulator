class WarpZone(object):
	def __init__(self, sourceGrid, sourceLocation, targetGrid, targetLocation):
		self.warpSourceGrid = sourceGrid
		self.warpSourceLocation = sourceLocation
		self.warpTargetGrid = targetGrid
		self.warpTargetLocation = targetLocation

oakLabWarpOne = [9, 14, 'Oak Lab', 16, 16, 'Pallet Town']
oakLapWarpTwo = [10, 14, 'Oak Lab', 16, 16, 'Pallet Town']

palletTownWarpOne = [14, 3, 'Pallet Town', 11, 41, 'Route 1']
palletTownWarpTwo = [15, 3, 'Pallet Town', 12, 41, 'Route 1']
palletTownWarpThree = [16, 15, 'Pallet Town', 9, 13, 'Oak Lab']

routeOneWarpOne = [11, 42, 'Route 1', 14, 4, 'Pallet Town']
routeOneWarpTwo = [12, 42, 'Route 1', 15, 4, 'Pallet Town']
routeOneWarpThree = [11, 3, 'Route 1', 24, 36, 'Viridian City']
routeOneWarpFour = [12, 3, 'Route 1', 25, 36, 'Viridian City']

viridianCityWarpOne = [24, 37, 'Viridian City', 11, 4, 'Route 1']
viridianCityWarpTwo = [25, 37, 'Viridian City', 12, 4, 'Route 1']
viridianCityWarpThree = [21, 4, 'Viridian City', 11, 32, 'Route 2']
viridianCityWarpFour = [22, 4, 'Viridian City', 12, 32, 'Route 2']
viridianCityWarpFive = [27, 28, 'Viridian City', 9, 10, 'Viridian Center']

viridianCenterWarpOne = [10, 11, 'Viridian Center', 27, 29, 'Viridian City']
viridianCenterWarpTwo = [9, 11, 'Viridian Center', 27, 29, 'Viridian City']

routeTwoWarpOne = [11, 33, 'Route 2', 21, 5, 'Viridian City']
routeTwoWarpTwo = [12, 33, 'Route 2', 22, 5, 'Viridian City']
routeTwoWarpThree = [7, 3, 'Route 2', 9, 11, 'Viridian Forest Entrance']

viridianForestEntranceWarpOne = [9, 12, 'Viridian Forest Entrance', 7, 4, 'Route 2']
viridianForestEntranceWarpTwo = [10, 12, 'Viridian Forest Entrance', 7, 4, 'Route 2']
viridianForestEntranceWarpThree = [9, 4, 'Viridian Forest Entrance', 20, 51, 'Viridian Forest']
viridianForestEntranceWarpFour = [10, 4, 'Viridian Forest Entrance', 21, 51, 'Viridian Forest']

viridianForestWarpOne = [20, 52, 'Viridian Forest', 9, 5, 'Viridian Forest Entrance']
viridianForestWarpTwo = [21, 52, 'Viridian Forest', 10, 5, 'Viridian Forest Entrance']
viridianForestWarpThree = [5, 3, 'Viridian Forest', 9, 11, 'Viridian Forest Exit']
viridianForestWarpFour = [6, 3, 'Viridian Forest', 10, 11, 'Viridian Forest Exit']

viridianForestExitWarpOne = [9, 12, 'Viridian Forest Exit', 7, 4, 'Route 3']
viridianForestExitWarpTwo = [10, 12, 'Viridian Forest Exit', 7, 4, 'Route 3']
viridianForestExitWarpThree = [9, 4, 'Viridian Forest Exit', 20, 51, 'Viridian Forest']
viridianForestExitWarpFour = [10, 4, 'Viridian Forest Exit', 21, 51, 'Viridian Forest']


oakLabWarps = [oakLabWarpOne, oakLapWarpTwo]
palletTownWarps = [palletTownWarpOne, palletTownWarpTwo, palletTownWarpThree]
routeOneWarps = [routeOneWarpOne, routeOneWarpTwo, routeOneWarpThree, routeOneWarpFour]
viridianCityWarps = [viridianCityWarpOne, viridianCityWarpTwo, viridianCityWarpThree, viridianCityWarpFour, viridianCityWarpFive]
viridianCenterWarps = [viridianCenterWarpOne, viridianCenterWarpTwo]
routeTwoWarps = [routeTwoWarpOne, routeTwoWarpTwo, routeTwoWarpThree]
viridianForestEntranceWarps = [viridianForestEntranceWarpOne, viridianForestEntranceWarpTwo, viridianForestEntranceWarpThree, viridianForestEntranceWarpFour]
viridianForestWarps = [viridianForestWarpOne, viridianForestWarpTwo, viridianForestWarpThree, viridianForestWarpFour]
viridianForestExitWarps = [viridianForestExitWarpOne, viridianForestExitWarpTwo, viridianForestExitWarpThree, viridianForestExitWarpFour]

locationToWarpListDict = {
'Oak Lab': oakLabWarps, 
'Pallet Town': palletTownWarps, 
'Route 1': routeOneWarps, 
'Viridian City': viridianCityWarps, 
'Viridian Center': viridianCenterWarps, 
'Route 2': routeTwoWarps,
'Viridian Forest Entrance': viridianForestEntranceWarps,
'Viridian Forest': viridianForestWarps,
'Viridian Forest Exit': viridianForestExitWarps
}

def getWarpZones(location):
    warpZones = []
    warpInfo = locationToWarpListDict[location]
    for zone in warpInfo:
        warpZones.append(WarpZone([zone[0], zone[1]], zone[2], [zone[3], zone[4]], zone[5]))
    return warpZones