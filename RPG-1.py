


# class Hero:

#     def __init__(self, health, power):
#         self.health = health
#         self.power = power
    
#     def attack(self, goblin):
#         goblin.health -= self.power
    
#     def alive(self):
#         if self.health > 0:
#             return True
#         else:
#             return False
    
#     def print_status(self):
#         print("You have %d health and %d power." % (self.health, self.power))
    

    
# class Goblin:

#     def __init__(self, health, power):
#         self.health = health
#         self.power = power

#     def attack(self, hero):
#         hero.health -= self.power

#     def alive(self):
#         if self.health > 0:
#             return True
#         else:
#             return False
#     def print_status(self):
#         print("The goblin has %d health and %d power." % (self.health, self.power))

class Character:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, opponent):
        opponent.health -= self.power
        if self.name != "goblin":
            print("You do %d damage to the %s." % (self.power, opponent.name))
        else:
            print("The goblin does %d damage to the %s." % (self.power, opponent.name))




    def alive(self):
        if self.health < 0:
            print("The %s is dead." % self.name)
            return False
        else:
            return True
    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))



goblin = Character("goblin", 6, 2)
hero = Character("hero", 10, 5)

def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while goblin.alive() and hero.alive():
        # print("You have %d health and %d power." % (hero_health, hero_power))
        # print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            # goblin.alive()
            # print("You do %d damage to the goblin." % hero.power)
            # if goblin.alive() == False:
            #     print("The goblin is dead.")
            
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
        else:
            break
            
            # print("The goblin does %d damage to you." % goblin_power)
        #   if hero.alive() == False:
        #         print("You are dead.")

main()
  


