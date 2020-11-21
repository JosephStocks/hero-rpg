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
        print(f"\nThe {self.name} attacks the {defender.name} with {self.power} power")
        attacker = self
        defender.receive_damage(attacker, self.power)

    def receive_damage(self, attacker, attack_power):
        self.health -= attack_power
        print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
        if self.health <= 0:
            print(f"--> The {self.name} is dead.")

    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def attack(self, defender):
        # 20% chance to double attack power
        choice = random.choices(["regular", "double"], [80, 20])[0]
        if choice == "regular":
            super().attack(defender)
        else:
            print(f"\nThe {self.name} attacks the {defender.name} with {2 * self.power} power! Double the power!")
            attacker = self
            defender.receive_damage(attacker, 2 * self.power)


class Goblin(Character):
    pass

class Zombie(Character):
    @staticmethod
    def alive():
        return True

    def receive_damage(self, attacker, attack_power):
        self.health -= attack_power
        print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
        if self.health <= 0:
            print(f"--> The {self.name} is already undead! He can't die again!! Ha! Ha! Ha!!!")

class Medic(Character):
    def receive_damage(self, attacker, attack_power):
        # 20% chance to regain 2 health
        choice = random.choices(["regular", "recuperate"], [80, 20])[0]
        if choice == "regular":
            super().receive_damage(attacker, attack_power)
        else:
            self.health -= (attack_power - 2)
            print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
            
            if self.health <= 0:
                self.health = 2
            print(f"--> ...but the medic heals himself 2 points!! He now has {self.health} health!")

class Shadow(Character):
    def __init__(self, power):
        super().__init__(health=1, power=power)

    def receive_damage(self, attacker, attack_power):
        # 20% chance to take any damage
        choice = random.choices(["take_damage", "dodge"], [10, 90])[0]
        if choice == "take_damage":
            super().receive_damage(attacker, attack_power)
        else:
            print(f"--> The {self.name} dodged the attack! The {self.name} took no damage.")


def LOOK_AT_LATER():
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
    enemy = Shadow(power=2)

    while hero.alive() and enemy.alive():
        print('\n')
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