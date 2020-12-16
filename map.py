import enemy
import item


class mapTile:
    """base mapTile class to build with position, type and description"""
    def __init__(self, tileType, desc, mapChar):
        self.type = tileType
        self.desc = desc
        self.hidden = True
        self.mapChar = mapChar

    def enter(self, player):
        self.hidden = False
        print(self.desc)


class emptyTile(mapTile):
    """mapTile with no special features"""
    def __init__(self, desc):
        mapTile.__init__(self, 'empty', desc, '*')

    def enter(self, player):
        mapTile.enter(self, player)


class enemyTile(mapTile):
    """mapTile with an enemy"""
    def __init__(self, desc, enemy):
        mapTile.__init__(self, 'enemy', desc, 'E')
        mapTile.enemy = enemy

    def enter(self, player):
        mapTile.enter(self, player)
        if (self.enemy.alive):
            player.inCombat = True
        print(self.enemy.desc)
        self.enemy.heal(-1000, player)


class treasureTile(mapTile):
    """mapTile with treasure"""
    def __init__(self, desc, item):
        mapTile.__init__(self, 'treasure', desc, 'T')
        self.item = item
        self.looted = False

    def enter(self, player):
        mapTile.enter(self, player)
        if (not self.looted):
            print(f'You got a {self.item.name}!')
            player.inv.give(self.item)
            self.looted = True


class trapTile(mapTile):
    """mapTile with a trap"""
    def __init__(self, desc, trapMsg, damage):
        mapTile.__init__(self, 'trap', desc, 'X')
        self.armed = True
        self.damage = damage
        self.trapMsg = trapMsg

    def enter(self, player):
        mapTile.enter(self, player)
        if (self.armed):
            print(self.trapMsg, f'and dealt {self.damage} damage!')
            player.heal(-self.damage)
            print(f'')
            self.armed = False


class stairTile(mapTile):
    """mapTile with an option to move between floors"""
    def __init__(self, exitFloor, exitX, exitY):
        mapTile.__init__(self, 'stair',
                         'Theres a stairway down to the inside of the temple ',
                         '\\')
        self.exitX = exitX
        self.exitY = exitY
        self.exitFloor = exitFloor

    def enter(self, player):
        mapTile.enter(self, player)
        print('Use move downstairs to enter')
        print('WARNING: once you enter there is no escape')


class winTile(mapTile):
    """mapTile that ends the game when found"""
    def __init__(self):
        mapTile.__init__(self, 'win', '', ' ')

    def enter(self, player):
        print('You enter a room full of gold!')
        print('In the middle there is a gem encrusted mask')
        print('You take it and traps spring up as you rush out')
        print('narrowly avoiding death you escape')
        print('YOU WIN!')
        player.playing = False


# map class
class map():
    """map class for handling map things"""
    def __init__(self, player):
        self.size = 5
        # Make map of empty
        self.map = [[], []]
        for x in range(0, self.size):
            self.map[0].append([emptyTile('Just more trees here')
                                for i in range(0, self.size)])
        for x in range(0, self.size):
            self.map[1].append([emptyTile('An empty temple room')
                                for i in range(0, self.size)])

        # Initialize first room
        self.getTile(0, 0, 0).enter(player)

        # Add Special Rooms
        self.replaceTile(treasureTile('Theres a tree with an apple on it',
                                      item.apple()), 0, 1, 0)
        self.replaceTile(trapTile('Just more regular trees?',
                                  'A volley of arrows shoot from the tree',
                                  10), 0, 1, 2)
        self.replaceTile(enemyTile('The trees are dying here', enemy.ghost()),
                         0, 1, 1)
        self.replaceTile(stairTile(1, 0, 0), 0, 4, 4)
        self.replaceTile(winTile(), 1, 4, 4)

    def getTile(self, floor, x, y):
        return self.map[floor][x][y]

    def replaceTile(self, newTile, floor, x, y):
        del self.map[floor][x][y]
        self.map[floor][x].insert(y, newTile)
