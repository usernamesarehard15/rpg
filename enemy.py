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
        # mark self as dead, exit combat, print death message
        print(self.deathMessage)
        self.alive = False
        player.inCombat = False

    def heal(self, amount, player):
        # Heal/damage enemy and then confine it to valid values
        self.health += amount
        self.health = max(0, min(self.health, self.maxHealth))
        # Kill enemy if health is less than 0
        if (self.health <= 0):
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
                       'The ghost disapears into a puff of smoke',
                       6, 15, 0.25)

    def special(self, player):
        print('The ghost rests and heals a bit')
        self.heal(5, player)


class livingTree(enemy):
    def __init__(self):
        enemy.__init__(self, 'living tree', 'A tree starts to move?',
                       'The tree stiffens in place and stops moving',
                       10, 30, 0.33)

    def special(self, player):
        print('The trees branches grow thicker')
        self.damage *= 1.5


class templeGuardian(enemy):
    def __init__(self):
        enemy.__init__(self, 'temple guardian',
                       'A man of bricks holding a spear approaches you',
                       'The bricks collapse into a pile', 15, 45, 0.2)
        self.charged = False

    def attack(self, player):
        # check if charge attack before doing normal attack function
        if (self.charged):
            print('The guardian\'s staff\'s light becomes blinding')
            print(f'{self.name.title()} dealt {self.damage*2} damage')
            print('The light disapears')
            player.heal(-2*self.damage)
            return
        else:
            enemy.attack(self, player)

    def special(self, player):
        print('The staff starts glowing...')
        self.charged = True


class templeGolem(enemy):
    def __init__(self):
        enemy.__init__(self, 'temple golem',
                       ('A massive golem stands infront of you'
                        '\nIt appears to be powered by '
                        'a glowing gem in its chest'),
                       'The golem collapses leaving the glowing gem',
                       15, 80, 0.1)

    def special(self, player):
        print('Flame flys out the golems mouth')
        print(f'{self.name.title()} dealt {self.damage*3} damage')
        player.heal(-3*self.damage)

    def kill(self, player):
        enemy.kill(self, player)
        player.win()
