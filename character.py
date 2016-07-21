from weapon import Weapon, Fist

class Character:
    def __init__(self, name, gender='male'):
        self.name = name
        self.gender = gender
        self.weapon = Fist()

    def set_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            raise TypeError('Supply instance of {}'.format(Weapon))
        self.weapon = weapon

    def fight(self):
        return self.weapon.use()

    def die(self):
        return 'You killed me, I thought we were just playing!'
