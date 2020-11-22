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
    def __init__(self, health, power, coins):
        super().__init__(health, power)
        self.coins = coins

    def attack(self, defender):
        # 20% chance to double attack power
        choice = random.choices(["regular", "double"], [80, 20])[0]
        if choice == "regular":
            super().attack(defender)
        else:
            print(f"\nThe {self.name} attacks the {defender.name} with {2 * self.power} power! Double the power!")
            attacker = self
            defender.receive_damage(attacker, 2 * self.power)

    def take_bounty(self, bounty):
        self.coins += bounty
        print(f"\nThe hero takes the bounty of {bounty} coins. He now has {self.coins} coins.")

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

def LOOK_AT_LATER():


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

def fightChoice(fighter_classes):
    print("\nWho do you want to fight?!")
    choice_dict = {}
    for i, fighter_class in enumerate(dict.fromkeys(fighter_classes)):
        choice_dict[i + 1] = fighter_class
        print(f"{i + 1}. {fighter_class.__name__}")
    print("> ", end=' ')

    return choice_dict[int(input())]

def fightEngine(hero, enemy):
    while hero.alive() and enemy.alive():
        print('\n')
        hero.print_status()
        enemy.print_status()

        print("\nWhat do you want to do?")
        print(f"1. Fight {enemy.name}")
        print("2. Do nothing")
        print("3. Flee")
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

def difficultyChoice():
    print("Choose your difficulty level?")
    for i, difficulty in enumerate(["easy", "normal", "impossible"]):
        print(f"{i + 1}. {difficulty.capitalize()}")
    print("> ", end=' ')
    return int(input())

def startingScreen():
    print(r"""
   _____ _                 _        _____       _   _                 
  / ____(_)               | |      |  __ \     | | | |                
 | (___  _ _ __ ___  _ __ | | ___  | |__) |   _| |_| |__   ___  _ __  
  \___ \| | '_ ` _ \| '_ \| |/ _ \ |  ___/ | | | __| '_ \ / _ \| '_ \ 
  ____) | | | | | | | |_) | |  __/ | |   | |_| | |_| | | | (_) | | | |
 |_____/|_|_| |_| |_| .__/|_|\___| |_|    \__, |\__|_| |_|\___/|_| |_|
                    | |                    __/ |                      
                    |_|                   |___/                       
          _____  _____   _____      _____                      
         |  __ \|  __ \ / ____|    / ____|                     
         | |__) | |__) | |  __    | |  __  __ _ _ __ ___   ___ 
         |  _  /|  ___/| | |_ |   | | |_ |/ _` | '_ ` _ \ / _ \
         | | \ \| |    | |__| |   | |__| | (_| | | | | | |  __/
         |_|  \_\_|     \_____|    \_____|\__,_|_| |_| |_|\___|
                                                               
                              _,.
                            ,` -.)
                           ( _/-\\-._
                          /,|`--._,-^|            ,
                          \_| |`-._/||          ,'|
                            |  `-, / |         /  /
                            |     || |        /  /
                             `r-._||/   __   /  /
                         __,-<_     )`-/  `./  /
                        '  \   `---'   \   /  /
                            |           |./  /
                            /           //  /
                        \_/' \         |/  /
                         |    |   _,^-'/  /
                         |    , ``  (\/  /_
                          \,.->._    \X-=/^
                          (  /   `-._//^`
                           `Y-.____(__}
                            |     {__)
                                  ()
    """)
    input()

def main():
    startingScreen()
    hero = Hero(health=100, power=5, coins=10)
    difficulty = difficultyChoice()
    while hero.alive():
        print("\nWhat do you want to do?")
        print(f"1. Fight an enemy in the arena")
        print("2. Go to the store")
        print("3. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            fighter = fightChoice([Goblin, Zombie, Medic, Shadow, Wizard])
            if difficulty == 1:
                fighter = fighter.easy()
            elif difficulty == 2:
                fighter = fighter.normal()
            else:
                fighter = fighter.impossible()
            fightEngine(hero, fighter)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

main()