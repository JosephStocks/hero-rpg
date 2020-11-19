#!/usr/bin/env python3

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero: # Idea: could create a person class that hero and goblin inherit from OR
            # OR I could create a Hero class then a villain class that the Goblin inherits from
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"You do {self.power} damage to the {enemy.__class__.__name__.lower()}.")
        if enemy.health <= 0:
            print(f"The {enemy.__class__.name} is dead.")

    def alive(self):
        return self.health > 0

    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The goblin does {self.power} damage to you.")
        if enemy.health <= 0:
            print(f"You are dead.")

    def alive(self):
        return self.health > 0
    
    def print_status(self):
        print(f"The {self.__class__.__name__.lower()} has {self.health} health and {self.power} power.")

def main():
    hero = Hero(health=10, power=5, name='you')
    goblin = Goblin(health=6, power=2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()
