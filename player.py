from inventory import inventory

class player:
	def __init__(self, maxHealth, *items):
		self.maxHealth = maxHealth
		self.health = maxHealth
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

	def kill():
		ded = True

