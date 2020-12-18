class item:
    def __init__(self, name, desc, itemType):
        self.name = name
        self.desc = desc
        self.type = itemType


class weapon(item):
    def __init__(self, name, desc, damage):
        item.__init__(self, name, desc, 'weapon')
        self.damage = damage


class consumable(item):
    def __init__(self, name, desc, health):
        item.__init__(self, name, desc, 'consumable')
        self.health = health


class apple(consumable):
    def __init__(self):
        consumable.__init__(self, 'apple', 'Eating this might heal you a bit', 10)


class bandages(consumable):
    def __init__(self):
        consumable.__init__(self, 'bandages', 'Heals some pretty big wounds', 50)

class healthPotion(consumable):
    def __init__(self):
        consumable.__init__(self, 'health potion', 'Fully heals you', 9999)


class stick(weapon):
    def __init__(self):
        weapon.__init__(self, 'stick',
                        "A pointy stick, not the best for fighting", 4)

class oneHit(weapon):
    def __init__(self):
        weapon.__init__(self, 'one hit',
                        "you're not supposed to have this?", 9999)