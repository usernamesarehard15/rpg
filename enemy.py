class enemy():
    """ base enemy class to be inherted

    Arugments
    name -- enemy name
    desc -- enemy description shown on encounter
    death -- message played on enemy death
    health -- the max health of the enemy
    damage -- the damage dealt on attack
    """
    def __init__(self, name, desc, death, damage, health):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.maxHealth = health
        self.health = health
        self.alive = True
        self.deathMessage = death

    def kill(self):
        print(self.deathMessage)
        self.alive = False

