class item:
    def __init__(self, name, desc, itemType):
        self.name = name
        self.desc = desc
        self.type = itemType


class weapon(item):
    def __init__(self, name, desc, damage):
        item.__init__(self, name, desc, 'weapon')
        self.damage = damage


class armour(item):
    def __init__(self, name, desc, defence):
        item.__init__(self, name, desc, 'armour')
        self.defence = defence


class consumable(item):
    def __init__(self, name, desc, health):
        item.__init__(self, name, desc, 'consumable')
        self.health = health


class apple(consumable):
    def __init__(self):
        consumable.__init__(self, 'apple', 'Regular Red Apple', 5)


class bandages(consumable):
    def __init__(self):
        consumable.__init__(self, 'bandages', 'Bright Brown Banages', 25)
        