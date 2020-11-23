class Item:
    cost = 10
    def __init__(self):
        self.name = self.__class__.__name__.lower()

class SuperTonic(Item):
    def applyItem(character):
        character.health += 10

class Armor(Item):
    def applyItem(character):
        if hasattr(character, 'armor'):
            character.armor += 2
        else:
            character.armor = 2
        
class Evade(Item):
    def applyItem(character):
        if hasattr(character, 'evade'):
            character.evade += 2
        else:
            character.evade = 2

# class Swap(Item):
#     pass