#!/usr/bin/env python3

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero: # Idea: could create a person class that hero and goblin inherit from OR
            # OR I could create a Hero class then a villain class that the Goblin inherits from
    def __init__(self, health, power):
        self.health = health
        self.power = power


class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

def main():
    hero = Hero(health=10, power=5)
    goblin = Goblin(health=6, power=2)


    while goblin.health > 0 and hero.health > 0:
        print(f"You have {hero.health} health and {hero.power} power.")
        print(f"The goblin has {goblin.health} health and {goblin.power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print(f"You do {hero.power} damage to the goblin.")
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")

main()
