import random

class enemy():
    """ base enemy class to be inherted

    Arugments
    name -- enemy name
    desc -- enemy description shown on encounter
    death -- message played on enemy death
    health -- the max health of the enemy
    damage -- the damage dealt on attack
    specialChance -- number between 0 and 1 to determan chance to use special
    """
    def __init__(self, name, desc, death, damage, health, specialChance):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.maxHealth = health
        self.health = health
        self.alive = True
        self.deathMessage = death
        self.specialChance = specialChance

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

    def attack(self, player):
        # rng to decide between normal and special attack
        if (random.random() < self.specialChance):
            self.special(player)
        else:
            print(f'{self.name.title()} dealt {self.damage} damage')
            player.heal(-self.damage)

class ghost(enemy):
    def __init__(self):
        enemy.__init__(self, 'ghost', 'You encounter a ghost',
                       'The ghost disapears into a puff of smoke', 6 , 15, 0.25)

    def special(self, player):
        print('The ghost rests and heals a bit')
        self.heal(3, player)

class livingTree(enemy):
    def __init__(self):
        enemy.__init__(self, 'living tree', 'A tree starts to move?',
                       'The tree stiffens in place and stops moving', 10 , 30, 0.33)

    def special(self, player):
        print('The trees branches grow thicker')
        self.damage *= 1.5 

class templeGuardian(enemy):
    def __init__(self):
        enemy.__init__(self, 'temple guardian', 
                        'A man of bricks holding a spear approaches you',
                       'The bricks collapse into a pile', 15 , 45, 0.2)
        self.charged = False

    def attack(self, player):
        # check if charge attack before doing normal attack function 
        if (self.charged):
            print('The guardian\'s staff\'s light becomes blinding')
            print(f'{self.name.title()} dealt {self.damage*2} damage')
            print('The light disapears')
            player.heal(-2.0*self.damage)
            return
        else:
            enemy.attack(self, player)

    def special(self, player):
        print('The staff starts glowing...')
        self.charged = True