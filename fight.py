import abc

class Weapon(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def use():
        raise NotImplementedError('users must define use() to use this base class')

class Sword(Weapon):
    def use():
        print('Check out my sword, you are a dead man!')

class Gun(Weapon):
    def use():
        print('Check out my gun, you are a dead man!')

class BowAndArrow(Weapon):
    def use():
        print('Check out my bow and arrow, you are a dead man!')

class Fist(Weapon):
    def use():
        print('Check out my fist, you are a dead man!')
