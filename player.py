from inventory import inventory
import map

class action:
	def __init__(self, name, aliases):
		self.name = name
		self.aliases = aliases

class actInventory(action):
	def __init__(self):
		aliases = ('show inventory', 'show inv', 'inventory', 'inv', 'i')
		action.__init__(self, 'Show inventory', aliases)

	def run(self, player, args):
		player.inv.printInv()

class actMap(action):
    def __init__(self):
        aliases = ('show map', 'show m', 'map', 'ma')
        action.__init__(self, 'Show map', aliases)

    def run(self, player, args):
        player.printMap(map.map, player.floor)


class player:
	def __init__(self, maxHealth, floor, x, y, *items):
		self.maxHealth = maxHealth
		self.health = maxHealth
		self.floor = floor
		self.x = x
		self.y = y
		self.inv = inventory([item for item in items])

	def heal(self, amount):
		self.health += amount
		if self.health > self.maxHealth:
			 self.health = self.maxHealth
		elif self.health == 0:
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
		actions = [actInventory(),actMap()]
		for action in actions:
			for alias in action.aliases:
				if (alias == command):
					action.run(self, args)
					successful = True
		if (not successful):
			print('Invalid Action!')
		print()

	def kill(self): #TODO DONT LEAVE IT LIKE THIS DUMBASS
		ded = True

	def printMap(self, map, floor):
		mapWidth = len(map[floor][0])

		# Print First Line
		print('╔═══',end='')
		for i in range(1,mapWidth):
			print('╦═══',end='')
		print('╗')
		# Print Middle Tiles
		for idx, row in enumerate(map[floor]):
			for tile in row:
				# Get Tile Type
				if (tile.type == 'empty' or tile.hidden == True):
					char = ' '
				elif (tile.type == 'enemy'):
					char = 'E'
				elif (tile.type == 'treasure'):
					char = 'X'
				elif (tile.type == 'trap'):
					char = 'T'
				print(f'║ {char} ',end='')
			print('║')
			if (idx == mapWidth - 1): 
				continue
			print('╠═══',end='')
			for i in range(1,mapWidth):
				print('╬═══',end='')
			print('╣')
		# Print Last Row
		print('╚═══',end='')
		for i in range(1,mapWidth):
			print('╩═══',end='')
		print('╝')
		# Print Key
		print('KEY','E - Enemy', 'X - Treasure', 'T - Trap', sep='\n')

