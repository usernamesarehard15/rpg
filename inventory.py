# import item

class inventory:
	def __init__(self, items):
		self.items = items
	
	def get(self, name):
		for item in self.items:
			if item.name == name:
				return item

	def remove(self, name):
		for idx, item in enumerate(self.items):
			if item.name == name:
				del self.items[idx]
				return True
		return False

	def give(self, item):
		self.items.append(item)
	
	def printInv(self):
		text = 'Inventory:'
		if len(self.items) == 0: 
			print('Inventory Empty')
		else:
			for item in self.items:
				text += f'\n-{item.name.title()}'
		print(text)