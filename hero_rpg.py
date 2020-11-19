#!/usr/bin/env python3

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, isYou, health, power):
        self.isYou = isYou
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power
        if self.isYou:
            enemy_name = enemy.__class__.__name__.lower()
            print(f"You do {self.power} damage to the {enemy_name}.")
            if enemy.health <= 0:
                print(f"The {enemy_name} is dead.")
        else:
            character_name = self.__class__.__name__.lower()
            print(f"The {character_name} does {self.power} damage to you.")
            if enemy.health <= 0:
                print(f"You are dead.")

    def print_status(self):
        if self.isYou:
            print(f"You have {self.health} health and {self.power} power.")
        else:
            character_name = self.__class__.__name__.lower()
            print(f"The {character_name} has {self.health} health and {self.power} power.")


class Hero(Character): 
    pass


class Goblin(Character):
    pass


def main():
    hero = Hero(isYou=True, health=10, power=5)
    goblin = Goblin(isYou=False, health=6, power=2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()

        print("\nWhat do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            goblin.attack(hero)

main()
