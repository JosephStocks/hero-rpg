class Character:
    def __init__(self, isYou, health, power):
        self.health = health
        self.power = power
        self.name = self.__class__.__name__.lower()

    def alive(self):
        return self.health > 0

    def attack(self, defender):
        pass

    def receive_damage(self, attacker):
        pass

    def print_status(self):
        pass

class Hero(Character):
    pass

class BadGuy(Character):
    pass

class Goblin(BadGuy):
    pass

class Zombie(BadGuy):
    pass

class Medic(BadGuy):
    pass

class Shadow(BadGuy):
    pass

class Wizard(BadGuy):
    pass

class NewBadGuy2(BadGuy):
    pass



############################
class Store:
    pass

class Item:
    pass

class Armor(Item):
    pass

class Evade(Item):
    pass

class Swap(Item):
    pass

# 