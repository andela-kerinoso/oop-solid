import abc

class Weapon(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def use(self):
        raise NotImplementedError('users must define use() to use this base class')

class Sword(Weapon):
    def use(self):
        return 'Check out my sword, you are a dead man!'

class Gun(Weapon):
    def use(self):
        return 'Check out my gun, you are a dead man!'

class BowAndArrow(Weapon):
    def use(self):
        return 'Check out my bow and arrow, you are a dead man!'

class Fist(Weapon):
    def use(self):
        return 'Check out my fist, you are a dead man!'
