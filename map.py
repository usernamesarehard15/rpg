import enemy

class mapTile:
    """base mapTile class to build with position, type and description"""
    def __init__(self, tileType, desc):
        self.type = tileType
        self.desc = desc
        self.hidden = True
    
    def enter(self):
        print(self.desc)

class emptyTile(mapTile):
    """mapTile with no special features"""
    def __init__(self, desc):
        mapTile.__init__(self, 'empty', desc)

class enemyTile(mapTile):
    """mapTile with an enemy"""
    def __init__(self, desc, enemy):
        mapTile.__init__(self, 'enemy', desc)
        mapTile.enemy = enemy

class treasureTile(mapTile):
    """mapTile with treasure"""
    def __init__(self, desc):
        mapTile.__init__(self, 'treasure', desc)

class trapTile(mapTile):
    """mapTile with treasure"""
    def __init__(self, desc):
        mapTile.__init__(self, 'trap', desc)

map = []
# map should be accessed as map[floor][y][x]
for floor in range(0,4):
    map.append([])
    for x in range(0,5):
        map[floor].append([emptyTile('Theres just more trees here') for i in range(0,5)])
        #map[floor].append([emptyTile('')])