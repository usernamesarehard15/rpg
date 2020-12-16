from inventory import inventory
import map as Map
import math
import color as col


class action:
    def __init__(self, name, aliases):
        self.name = name
        self.aliases = aliases


class actInventory(action):
    def __init__(self):
        aliases = ('show inventory', 'show inv', 'inventory', 'inv', 'i')
        action.__init__(self, 'Show inventory', aliases)

    def run(self, player, args):
        # print health
        for i in range(0, math.floor(player.health / 10)):
            print(col.colorStr('❤ ', (5, 0, 0)), end='')
        for i in range(0, math.floor((player.maxHealth - player.health) / 10)):
            print(col.colorStr('❤ ', (1, 1, 1)), end='')
        print(f'{player.health}/{player.maxHealth}')
        # print inv
        player.inv.printInv()


class actMap(action):
    def __init__(self):
        aliases = ('show map', 'show m', 'map', 'ma')
        action.__init__(self, 'Show map', aliases)

    def run(self, player, args):
        # Set Map Boarder Colour
        if (player.floor == 0):
            mapCol = (0, 1, 0)
        elif (player.floor == 1):
            mapCol = (5, 5, 5)
        else:
            mapCol = (5, 5, 5)

        # Print First Line
        print(col.colorStr('╔═══', mapCol), end='')
        for i in range(1, player.map.size):
            print(col.colorStr('╦═══', mapCol), end='')
        print(col.colorStr('╗', mapCol))
        # Print Middle Tiles
        for y in range(0, player.map.size):
            for x in range(0, player.map.size):
                tile = player.map.getTile(player.floor, x, y)
                # set mapCharacter
                char = tile.mapChar
                # Hide character if unexplored room
                if (tile.hidden):
                    char = ' '
                # Check if player is in tile
                if (x == player.x and y == player.y):
                    char = col.colorStr('P', (0, 5, 0))
                print(col.colorStr('║', mapCol), f'{char} ', end='')
            print(col.colorStr('║', mapCol))
            if (y == player.map.size - 1):
                continue
            print(col.colorStr('╠═══', mapCol), end='')
            for i in range(1, player.map.size):
                print(col.colorStr('╬═══', mapCol), end='')
            print(col.colorStr('╣', mapCol))
        # Print Last Row
        print(col.colorStr('╚═══', mapCol), end='')
        for i in range(1, player.map.size):
            print(col.colorStr('╩═══', mapCol), end='')
        print(col.colorStr('╝', mapCol))
        # Print Key
        print(
            'KEY',
            'E - Enemy',
            'T - Treasure',
            'X - Trap',
            'P - Player',
            '* - Empty',
            sep='\n')


class actMove(action):
    def __init__(self):
        aliases = ('move', 'mov', 'mo', 'm')
        action.__init__(self, 'Move', aliases)

    def run(self, player, args):
        # Check if first argument exists and is a valid argument
        # Argument is valid if the first character of it is in directions
        directions = ('u', 'd', 'l', 'r')
        if (len(args) < 1 or not args[0][0] in directions):
            print('Invalid arguments! Example usage: move up')
            return
        # Move player based on direction input
        if (args[0][0] == directions[0]):
            player.move(player.floor, player.x, player.y-1)
        elif (args[0][0] == directions[1]):
            player.move(player.floor, player.x, player.y+1)
        elif (args[0][0] == directions[2]):
            player.move(player.floor, player.x-1, player.y)
        elif (args[0][0] == directions[3]):
            player.move(player.floor, player.x+1, player.y)


class player:
    def __init__(self, maxHealth, floor, x, y, *items):
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.floor = floor
        self.x = x
        self.y = y
        self.inv = inventory([item for item in items])
        self.alive = True
        self.actions = [actInventory(), actMap(), actMove()]
        self.map = Map.map(self)

    def heal(self, amount):
        self.health += amount
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        elif self.health <= 0:
            player.kill()

    def action(self, playerInput):
        # Parse action input into action (string) and arguments (list)
        args = playerInput.lower().strip().split(' ')
        command = args.pop(0)
        # handling edge cases for multi word commands
        if (command in ('show')):
            command += ' ' + args.pop(0)

        # Find and run action, note if successful
        successful = False
        for action in self.actions:
            for alias in action.aliases:
                if (alias == command):
                    action.run(self, args)
                    successful = True
        if (not successful):
            print('Invalid Action!')
        print()

    def move(self, floor, x, y):
        # move player if not out of bounds
        if (0 <= y < self.map.size and
                0 <= x < self.map.size and
                0 <= floor < len(self.map.map)):
            self.x = x
            self.y = y
            self.floor = floor

            # initilize room
            self.map.getTile(self.floor, self.x, self.y).enter(self)

    def combat(self): # TODO finish
        print('')

    def kill(self): # TODO finish
        print('uh oh not finished stuff woops')

    def printActions(self):
        print('Action List:')
        for act in self.actions:
            print('-', act.name)
