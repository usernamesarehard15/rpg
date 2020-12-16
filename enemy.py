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

    def kill(self, player):
        print(self.deathMessage)
        self.alive = False
        player.inCombat = False

    def heal(self, amount, player):
        self.health += amount
        if (self.health > self.maxHealth):
            self.health = self.maxHealth
        elif (self.health <= 0):
            self.kill(player)


class ghost(enemy):
    def __init__(self):
        enemy.__init__(self, 'ghost', 'You encounter a ghost',
                       'The ghost disapears into a puff of smoke', 15, 3)

    def special(self):
        print('The ghost rests and heals a bit')
        self.heal(3)
