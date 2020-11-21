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
        self.name = self.__class__.__name__.lower()

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power
        if self.isYou:
            print(f"You do {self.power} damage to the {enemy.name}.")
            if enemy.health <= 0:
                print(f"The {enemy.name} is dead.")
        else:
            print(f"The {self.name} does {self.power} damage to you.")
            if enemy.health <= 0:
                print(f"You are dead.")

    def print_status(self):
        if self.isYou:
            print(f"You ({self.name}) have {self.health} health and {self.power} power.")
        else:
            print(f"The {self.name} has {self.health} health and {self.power} power.")


class Hero(Character): 
    pass

class Goblin(Character):
    pass

class Zombie(Character):
    pass

def main():
    player = Goblin(isYou=True, health=10, power=5)
    enemy = Zombie(isYou=False, health=7, power=2)

    while player.alive() and enemy.alive():
        player.print_status()
        enemy.print_status()

        print("\nWhat do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            player.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.health > 0:
            enemy.attack(player)

main()
