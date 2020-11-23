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
    @classmethod
    def easy(cls):
        return cls(health=10, power=2)

    @classmethod
    def normal(cls):
        return cls(health=50, power=5)

    @classmethod
    def impossible(cls):
        return cls(health=500, power=20)

    bounty = 5
    def receive_damage(self, attacker, attack_power):
        self.health -= attack_power
        print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
        if self.health <= 0:
            print(f"--> The {self.name} is dead.")
            attacker.take_bounty(self.bounty)

class Goblin(BadGuy):
    pass

class Zombie(BadGuy):
    bounty = 100

    @staticmethod
    def alive():
        return True

    def receive_damage(self, attacker, attack_power):
        self.health -= attack_power
        print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
        if self.health <= 0:
            print(f"--> The {self.name} is already undead! He can't die again!! Ha! Ha! Ha!!!")

class Medic(BadGuy):
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

class Shadow(BadGuy):
    # def __init__(self, power):
    #     super().__init__(health=1, power=power)
    @classmethod
    def easy(cls):
        return cls(health=1, power=2)

    @classmethod
    def normal(cls):
        return cls(health=10, power=5)

    @classmethod
    def impossible(cls):
        return cls(health=500, power=20)

    def receive_damage(self, attacker, attack_power):
        # 10% chance to take any damage
        choice = random.choices(["take_damage", "dodge"], [10, 90])[0]
        if choice == "take_damage":
            super().receive_damage(attacker, attack_power)
        else:
            print(f"--> The {self.name} dodged the attack! The {self.name} took no damage.")

class Wizard(BadGuy):
    bounty = 6
    spell_cooldown = 0

    def receive_damage(self, attacker, attack_power):
        if self.spell_cooldown == 0:
            choice = random.choices(["cast_spell", "regular"], [10, 90])[0]
            if choice == "regular":
                self.health -= attack_power
                print(f"--> The {attacker.name}'s attack deals {attack_power} damage to the {self.name}.")
                if self.health <= 0:
                    print(f"--> The {self.name} is dead.")
            else:
                print(f"The {self.name} casts a spell!! The hero's attack has been rendered harmless for 4 turns.")
                print(f"--> The {attacker.name}'s attack deals 0 damage to the {self.name}.")
                self.spell_cooldown = 3
        else: # self.spell_cooldown > 0:
            print(f"The {self.name}'s spell still has a hold of the hero. He has no powers for {self.spell_cooldown} turns.")
            print(f"--> The {attacker.name}'s attack deals 0 damage to the {self.name}.")
            self.spell_cooldown -= 1
    

def LOOK_AT_LATER():

    class NewBadGuy2(Character):
        pass



    # ############################
    # class Store:
    #     pass




