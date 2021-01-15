from characters import Hero, Goblin, Zombie, Medic, Shadow, Wizard, Thief
from items import SuperTonic, Armor, Evade
from time import sleep

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

        if enemy.alive():
            enemy.attack(hero)

def difficultyChoice():
    print("Choose your difficulty level?")
    for i, difficulty in enumerate(["easy", "normal", "impossible"]):
        print(f"{i + 1}. {difficulty.capitalize()}")
    print("\n\tOR\n")
    print('Enter q to quit the game')
    print("> ", end=' ')
    return int(input())

def startingScreen():
    print("\n" * 20, end="")
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
    print("\n" * 5, end="")
    input()

def printGameOver():
    print("\n" * 10, end="")
    print(r"""
      _____          __  __ ______    ______      ________ _____  _ 
     / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \| |
    | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | |
    | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /| |
    | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \|_|
     \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_(_)
                                                                    
                                                                    
    """)
    print("\n" * 10, end="")
    input()
    print("\n" * 10, end="")

class Store:
    def __init__(self):
        self.items = []

    def add_items(self, *items):
        for item in items:
            self.items.append(item)
    
    def store(self, hero):
        while True:
            print(f"You have {hero.coins} coins.\n")
            print("Would you like to buy something?")
            for i, item_class in enumerate(self.items):
                item = item_class()
                left = f"{i + 1}. {item.name.capitalize()}"
                right = f"${item.cost}"
                print(f"{left.ljust(20, '.')}{right.rjust(20, '.')}")
            print(f"{i + 2}. Exit the store")
            print("> ", end=' ')
            try:
                choice = int(input())
            except ValueError:
                print("Invalid Input\n")
                pass

            if choice >= i + 2:
                print("Exiting the store..")
                sleep(0.6)
                break
            
            item = self.items[choice - 1]

            if hero.coins >= item.cost:
                self.purchase_item(item, hero)
            else:
                print("You do not have enough money for that item.\n")
        
    def purchase_item(self, item, hero):
        hero.inventory.append(item)
        self.items.remove(item)
        hero.coins -= item.cost
        item.applyItem(hero)
        print(f"You purchased one {item().name}\n")
        input()

def main():
    hero = Hero(health=100, power=5, coins=10)
    while True:
        startingScreen()
        try:
            difficulty = difficultyChoice()
        except ValueError:
            break
        while hero.alive():
            print("\nWhat do you want to do?")
            print(f"1. Fight an enemy in the arena")
            print( "2. Go to the store")
            print( "3. Show all hero stats")
            print( "4. Exit to main screen")
            print( "> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                fighter = fightChoice([Goblin, Zombie, Medic, Shadow, Wizard, Thief])
                if difficulty == 1:
                    fighter = fighter.easy()
                elif difficulty == 2:
                    fighter = fighter.normal()
                else:
                    fighter = fighter.impossible()
                fightEngine(hero, fighter)
            elif raw_input == "2":
                store = Store()
                store.add_items(SuperTonic, Armor, Evade)
                store.store(hero)
            elif raw_input == "3":
                hero.display_all_stats()
            elif raw_input == "4":
                print("Exiting to main screen..")
                break
            else:
                print(f"Invalid input {raw_input}")
        if raw_input != "4":
            printGameOver()
            hero = Hero(health=100, power=5, coins=10)


main()