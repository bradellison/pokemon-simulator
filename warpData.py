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

routeOneWarpOne = [11, 41, 'Route 1', 14, 3, 'Pallet Town']
routeOneWarpTwo = [12, 41, 'Route 1', 15, 3, 'Pallet Town']
routeOneWarpThree = [11, 4, 'Route 1', 24, 37, 'Viridian City']
routeOneWarpFour = [12, 4, 'Route 1', 25, 37, 'Viridian City']

viridianCityWarpOne = [25, 37, 'Viridian City', 12, 4, 'Route 1']
viridianCityWarpTwo = [24, 37, 'Viridian City', 11, 4, 'Route 1']
viridianCityWarpThree = [21, 4, 'Viridian City', 11, 30, 'Route 2']
viridianCityWarpFour = [22, 4, 'Viridian City', 12, 30, 'Route 2']
viridianCityWarpFive = [27, 28, 'Viridian City', 9, 10, 'Viridian Center']

viridianCenterWarpOne = [10, 11, 'Viridian Center', 27, 29, 'Viridian City']
viridianCenterWarpTwo = [9, 11, 'Viridian Center', 27, 29, 'Viridian City']

routeTwoWarpOne = [11, 30, 'Route 2', 21, 4, 'Viridian City']
routeTwoWarpTwo = [12, 30, 'Route 2', 22, 4, 'Viridian City']

oakLabWarps = [oakLabWarpOne, oakLapWarpTwo]
palletTownWarps = [palletTownWarpOne, palletTownWarpTwo, palletTownWarpThree]
routeOneWarps = [routeOneWarpOne, routeOneWarpTwo, routeOneWarpThree, routeOneWarpFour]
viridianCityWarps = [viridianCityWarpOne, viridianCityWarpTwo, viridianCityWarpThree, viridianCityWarpFour, viridianCityWarpFive]
viridianCenterWarps = [viridianCenterWarpOne, viridianCenterWarpTwo]
routeTwoWarps = [routeTwoWarpOne, routeTwoWarpTwo]

locationToWarpListDict = {'Oak Lab': oakLabWarps, 'Pallet Town': palletTownWarps, 'Route 1': routeOneWarps, 'Viridian City': viridianCityWarps, 'Viridian Center': viridianCenterWarps, 'Route 2': routeTwoWarps}

def getWarpZones(location):
    warpZones = []
    warpInfo = locationToWarpListDict[location]
    for zone in warpInfo:
        warpZones.append(WarpZone([zone[0], zone[1]], zone[2], [zone[3], zone[4]], zone[5]))
    return warpZones