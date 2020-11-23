from inventory import inventory

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

	def action(self, command):
		args = command.lower().split(' ')
		action = args.pop(0)

		if action in ('use', 'u'):
			try:
				item = self.inv.get(args[0])
			except:
				return 'Item not found'
			if item:
				if item.type == 'weapon':
					#do something
					print()
				elif item.type == 'armour':
					#do something
					print()
				elif item.type == 'consumable':
					player.heal(self, item.health)
					self.inv.remove(item.name)
			else:
				return 'Item not found'
		elif action in ('i', 'inv', 'inventory'):
			self.inv.printInv()
		else:
			return 'Action does not exist'

	def kill(): #TODO DONT LEAVE IT LIKE THIS DUMBASS
		ded = True

	def printMap(map, floor):
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

