class inventory:
    """ inventory class for player

    Arugments
    items -- array of items, blank for no items (default = [])
    """

    def __init__(self, items=[]):
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
        self.sort()

    def printInv(self):
        text = 'Inventory:'
        if len(self.items) == 0:
            print('Inventory Empty')
        else:
            for item in self.items:
                text += f'\n-{item.name.title()}'
        print(text)

    def sort(self):
        # Make a new list of the names of the items to sort
        itemNames = []
        for item in self.items:
            itemNames.append(item.name)
        itemNames.sort()
        # Convert item names back to itemNames
        sortedItems = []
        for name in itemNames:
            sortedItems.append(self.get(name))
        self.items = sortedItems
