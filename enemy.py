class enemy():
    def __init__(self, name, desc, damage, health):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.maxHealth = health
        self.health = health
        self.alive = True
        self.deathMessage = ""

    def kill(self):
        print(self.deathMessage)
        self.alive = False
