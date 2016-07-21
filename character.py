from .fight import Fist

class Character:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.weapon = Fist()

    def set_weapon(self, weapon):
        self.weapon = weapon

    def fight(self):
        self.weapon.use()

    def die(self):
        print('You killed me, I thought we were just playing!')
