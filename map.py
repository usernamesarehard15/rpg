class mapTile:
	"""base mapTile class to build with position, type and description"""
	def __init__(self, x, y, floor, tileType, desc):
		self.x = x
		self.y = y
		self.floor = floor
		self.type = tileType
		self.desc = desc

class enemyTile(mapTile):
	"""mapTile with an enemy"""
	def __init__(self, x, y, floor, desc):
		mapTile.__init__(self, x, y, floor, 'enemy')

class treasureTile(mapTile):
	"""mapTile with treasure"""
	def __init__(self, x, y, floor, desc):
		mapTile.__init__(self, x, y, floor, 'treasure')

class trapTile(mapTile):
	"""mapTile with treasure"""
	def __init__(self, x, y, floor, name, desc):
		mapTile.__init__(self, x, y, floor, 'treasure')
