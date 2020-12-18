class item:
    """ base item class to inherit

    Arugments
    name -- name of item
    desc -- description of item
    type -- item type
    """
    def __init__(self, name, desc, itemType):
        self.name = name
        self.desc = desc
        self.type = itemType


class weapon(item):
    """ weapon class

    Arugments
    name -- name of item
    desc -- description of item
    damage -- how much damage the item deals
    """
    def __init__(self, name, desc, damage):
        item.__init__(self, name, desc, 'weapon')
        self.damage = damage


class consumable(item):
    """ consumable class

    Arugments
    name -- name of item
    desc -- description of item
    health -- how much damage the item heals
    """
    def __init__(self, name, desc, health):
        item.__init__(self, name, desc, 'consumable')
        self.health = health


class apple(consumable):
    def __init__(self):
        consumable.__init__(self, 'apple',
                            'Eating this might heal you a bit', 10)


class bandages(consumable):
    def __init__(self):
        consumable.__init__(self, 'bandages',
                            'Heals some pretty big wounds', 50)


class healthPotion(consumable):
    def __init__(self):
        consumable.__init__(self, 'health potion', 'Fully heals you', 100)


class stick(weapon):
    def __init__(self):
        weapon.__init__(self, 'stick',
                        "A pointy stick, not the best for fighting", 4)


class axe(weapon):
    def __init__(self):
        weapon.__init__(self, 'axe',
                        "An iron axe, pretty good for combat", 8)


class sword(weapon):
    def __init__(self):
        weapon.__init__(self, 'sword',
                        ('Really good at killing things, '
                         'what else is there to say?'), 12)


class oneHit(weapon):
    def __init__(self):
        weapon.__init__(self, 'one hit',
                        "How did you get this?", 9999)
