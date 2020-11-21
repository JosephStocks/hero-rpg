import random
# random.seed(42)

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = self.__class__.__name__.lower()

    def alive(self):
        return self.health > 0

    def attack(self, defender):
        print(f"The {self.name} attacks the {defender.name} with {self.power} power")
        attacker = self
        defender.receive_damage(attacker, self.power)

    def receive_damage(self, attacker, attack_power):
        self.health -= attack_power
        print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
        if self.health <= 0:
            print(f"The {self.name} is dead.")

    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def attack(self, defender):
        # 20% chance to double attack power
        choice = random.choices(["regular", "double"], [80, 20])[0]
        if choice == "regular":
            super().attack(defender)
        else:
            print(f"The {self.name} attacks the {defender.name} with {2 * self.power} power! Double the power!")
            attacker = self
            defender.receive_damage(attacker, 2 * self.power)


class Goblin(Character):
    pass

class Zombie(Character):
    pass


def LOOK_AT_LATER():
    
    class Medic(Character):
        pass

    class Shadow(Character):
        pass

    class Wizard(Character):
        pass

    class NewBadGuy2(Character):
        pass



    # ############################
    # class Store:
    #     pass




    # class Item:
    #     pass

    # class Armor(Item):
    #     pass

    # class Evade(Item):
    #     pass

    # class Swap(Item):
    #     pass

def main():
    hero = Hero(health=100, power=5)
    enemy = Goblin(health=70, power=2)

    while hero.alive() and enemy.alive():
        print()
        hero.print_status()
        enemy.print_status()

        print("\nWhat do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.health > 0:
            enemy.attack(hero)

main()