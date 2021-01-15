import random
# random.seed(42)
import math

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
    def __init__(self, health, power, coins):
        super().__init__(health, power)
        self.coins = coins
        self.inventory = []

    def attack(self, defender):
        # 20% chance to double attack power
        choice = random.choices(["regular", "double"], [80, 20])[0]
        if choice == "regular":
            super().attack(defender)
        else:
            print(f"\nThe {self.name} attacks the {defender.name} with {2 * self.power} power! Double the power!")
            attacker = self
            defender.receive_damage(attacker, 2 * self.power)

    def receive_damage(self, attacker, attack_power):
        if hasattr(self, 'armor'):
            attack_power = max(attack_power - self.armor, 0)
            print(f"Armor reduces the attack by {self.armor}")
        if hasattr(self, 'evade'):
            evade_chance = min(7 * math.sqrt(self.evade), 30)
            choice = random.choices(["take_damage", "evade"], [100 - evade_chance, evade_chance])[0]
            if choice == "take_damage":
                super().receive_damage(attacker, attack_power)
            else:
                print(f"--> The {self.name} dodged the attack! The {self.name} took no damage.")
        else:
            self.health -= attack_power
            print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
            if self.health <= 0:
                print(f"--> The {self.name} is dead.")

    def take_bounty(self, bounty):
        self.coins += bounty
        print(f"\nThe hero takes the bounty of {bounty} coins. He now has {self.coins} coins.", end="")
        input()

    def display_all_stats(self):
        print("\nHero's Stats\n--------------------")

        print(f"Health: {self.health}")
        print(f"Power: {self.power}")
        if hasattr(self, 'armor'):
            print(f"Armor: {self.armor}")
        print(f"Coins: ${self.coins}")
        if hasattr(self, 'evade'):
            dodge_chance = min(7 * math.sqrt(self.evade), 30)
            print(f"Evade: {self.evade}  [Hero has a {dodge_chance:.1f}% chance to dodge attacks]")
        input()


class BadGuy(Character):
    bounty = 5
    @classmethod
    def easy(cls):
        return cls(health=10, power=2)

    @classmethod
    def normal(cls):
        return cls(health=50, power=5)

    @classmethod
    def impossible(cls):
        return cls(health=500, power=20)

    def receive_damage(self, attacker, attack_power):
        self.health -= attack_power
        print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
        if not self.alive():
            print(f"--> The {self.name} is dead.")
            attacker.take_bounty(self.bounty)


class Goblin(BadGuy):
    pass
