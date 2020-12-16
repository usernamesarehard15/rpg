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
        # Make new lists of the names of the items to sort
        # put weapons in weaponNames and consumables in consumablesNames
        weaponNames = []
        consumablesNames = []
        for item in self.items:
            if (item.type == 'weapon'):
                weaponNames.append(item.name)
            else:
                consumablesNames.append(item.name)
        weaponNames.sort()
        consumablesNames.sort()
        # replace inventory with sorted items from both lists
        sortedItems = []
        for name in weaponNames:
            sortedItems.append(self.get(name))
        for name in consumablesNames:
            sortedItems.append(self.get(name))

        self.items = sortedItems
