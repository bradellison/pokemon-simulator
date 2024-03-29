class WarpZone(object):
	def __init__(self, sourceGrid, sourceLocation, targetGrid, targetLocation):
		self.warpSourceGrid = sourceGrid
		self.warpSourceLocation = sourceLocation
		self.warpTargetGrid = targetGrid
		self.warpTargetLocation = targetLocation

oakLabWarpOne = [9, 15, 'Oak Lab', 16, 16, 'Pallet Town']
oakLapWarpTwo = [10, 15, 'Oak Lab', 16, 16, 'Pallet Town']

palletTownWarpOne = [14, 3, 'Pallet Town', 11, 41, 'Route 1']
palletTownWarpTwo = [15, 3, 'Pallet Town', 12, 41, 'Route 1']
palletTownWarpThree = [16, 15, 'Pallet Town', 9, 14, 'Oak Lab']

routeOneWarpOne = [11, 42, 'Route 1', 14, 4, 'Pallet Town']
routeOneWarpTwo = [12, 42, 'Route 1', 15, 4, 'Pallet Town']
routeOneWarpThree = [11, 3, 'Route 1', 24, 36, 'Viridian City']
routeOneWarpFour = [12, 3, 'Route 1', 25, 36, 'Viridian City']

viridianCityWarpOne = [24, 37, 'Viridian City', 11, 4, 'Route 1']
viridianCityWarpTwo = [25, 37, 'Viridian City', 12, 4, 'Route 1']
viridianCityWarpThree = [21, 4, 'Viridian City', 11, 72, 'Route 2']
viridianCityWarpFour = [22, 4, 'Viridian City', 12, 72, 'Route 2']
viridianCityWarpFive = [27, 28, 'Viridian City', 9, 10, 'Viridian Center']

viridianCenterWarpOne = [10, 11, 'Viridian Center', 27, 29, 'Viridian City']
viridianCenterWarpTwo = [9, 11, 'Viridian Center', 27, 29, 'Viridian City']

routeTwoWarpOne = [11, 73, 'Route 2', 21, 5, 'Viridian City']
routeTwoWarpTwo = [12, 73, 'Route 2', 22, 5, 'Viridian City']
routeTwoWarpThree = [7, 43, 'Route 2', 9, 11, 'Viridian Forest Entrance']
routeTwoWarpFour = [7, 14, 'Route 2', 9, 5, 'Viridian Forest Exit']
routeTwoWarpFive = [12, 3, 'Route 2', 19, 33, 'Pewter City']
routeTwoWarpSix = [13, 3, 'Route 2', 20, 33, 'Pewter City']

viridianForestEntranceWarpOne = [9, 12, 'Viridian Forest Entrance', 7, 44, 'Route 2']
viridianForestEntranceWarpTwo = [10, 12, 'Viridian Forest Entrance', 7, 44, 'Route 2']
viridianForestEntranceWarpThree = [9, 4, 'Viridian Forest Entrance', 20, 51, 'Viridian Forest']
viridianForestEntranceWarpFour = [10, 4, 'Viridian Forest Entrance', 21, 51, 'Viridian Forest']

viridianForestWarpOne = [20, 52, 'Viridian Forest', 9, 5, 'Viridian Forest Entrance']
viridianForestWarpTwo = [21, 52, 'Viridian Forest', 10, 5, 'Viridian Forest Entrance']
viridianForestWarpThree = [5, 3, 'Viridian Forest', 9, 11, 'Viridian Forest Exit']
viridianForestWarpFour = [6, 3, 'Viridian Forest', 10, 11, 'Viridian Forest Exit']

viridianForestExitWarpOne = [9, 4, 'Viridian Forest Exit', 7, 13, 'Route 2']
viridianForestExitWarpTwo = [10, 4, 'Viridian Forest Exit', 7, 13, 'Route 2']
viridianForestExitWarpThree = [9, 12, 'Viridian Forest Exit', 5, 4, 'Viridian Forest']
viridianForestExitWarpFour = [10, 12, 'Viridian Forest Exit', 6, 4, 'Viridian Forest']

pewterCityWarpOne = [19, 34, 'Pewter City', 12, 4, 'Route 2']
pewterCityWarpTwo = [20, 34, 'Pewter City', 13, 4, 'Route 2']
pewterCityWarpThree = [14, 24, 'Pewter City', 9, 10, 'Pewter Center']
pewterCityWarpFour = [17, 16, 'Pewter City', 10, 17, 'Pewter Gym']

pewterCenterWarpOne = [10, 11, 'Pewter Center', 14, 25, 'Pewter City']
pewterCenterWarpTwo = [9, 11, 'Pewter Center', 14, 25, 'Pewter City']

pewterGymWarpOne = [10, 18, 'Pewter Gym', 17, 17, 'Pewter City']

oakLabWarps = [oakLabWarpOne, oakLapWarpTwo]
palletTownWarps = [palletTownWarpOne, palletTownWarpTwo, palletTownWarpThree]
routeOneWarps = [routeOneWarpOne, routeOneWarpTwo, routeOneWarpThree, routeOneWarpFour]
viridianCityWarps = [viridianCityWarpOne, viridianCityWarpTwo, viridianCityWarpThree, viridianCityWarpFour, viridianCityWarpFive]
viridianCenterWarps = [viridianCenterWarpOne, viridianCenterWarpTwo]
routeTwoWarps = [routeTwoWarpOne, routeTwoWarpTwo, routeTwoWarpThree, routeTwoWarpFour, routeTwoWarpFive, routeTwoWarpSix]
viridianForestEntranceWarps = [viridianForestEntranceWarpOne, viridianForestEntranceWarpTwo, viridianForestEntranceWarpThree, viridianForestEntranceWarpFour]
viridianForestWarps = [viridianForestWarpOne, viridianForestWarpTwo, viridianForestWarpThree, viridianForestWarpFour]
viridianForestExitWarps = [viridianForestExitWarpOne, viridianForestExitWarpTwo, viridianForestExitWarpThree, viridianForestExitWarpFour]
pewterCityWarps = [pewterCityWarpOne, pewterCityWarpTwo, pewterCityWarpThree, pewterCityWarpFour]
pewterCenterWarps = [pewterCenterWarpOne, pewterCenterWarpTwo]
pewterGymWarps = [pewterGymWarpOne]
routeThreeWarps = []

locationToWarpListDict = {
'Oak Lab': oakLabWarps, 
'Pallet Town': palletTownWarps, 
'Route 1': routeOneWarps, 
'Viridian City': viridianCityWarps, 
'Viridian Center': viridianCenterWarps, 
'Route 2': routeTwoWarps,
'Viridian Forest Entrance': viridianForestEntranceWarps,
'Viridian Forest': viridianForestWarps,
'Viridian Forest Exit': viridianForestExitWarps,
'Pewter City': pewterCityWarps,
'Pewter Center': pewterCenterWarps,
'Pewter Gym': pewterGymWarps,
'Route 3': routeThreeWarps
}

def getLocationWarpZones(location):
    warpZones = []
    warpInfo = locationToWarpListDict[location]
    for zone in warpInfo:
        warpZones.append(WarpZone([zone[0], zone[1]], zone[2], [zone[3], zone[4]], zone[5]))
    return warpZones