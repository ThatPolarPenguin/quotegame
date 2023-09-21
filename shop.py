# Author: Karch Forward
# Date 9/17/2023

# Python class which defines the shop UI and functions 
# such as purchasing collectibles, purchasing ship parts
# Other helper functions are contained within assist in making functions more readable (hopefully)

from player import Player
import game
import time
import random

Thrawn = Player()

collectibles_list = []

collectibles_list_database = [['Holocron', 15], ['Lightsaber', 15], ['Comlink', 15], ['Astromech Droid', 50], 
                     ['Phase I Clone Helmet', 20], ['DC-17 Pistol', 30], ['Beskar Ingot', 50], 
                     ['Thermal Detonator', 25], ['Kalikori', 15], ['Rancor Tooth', 20], ['Holopad', 30],
                     ['E-11 Blaster Rifile', 20], ['B1 Battle Droid Head', 30], ['Virosword', 30],
                     ['Electrostaff', 50]]

ship_parts_list = [['Hyperdrive', 100], ['Engines', 50], ['Weapon Systems', 40], ['Hull', 60], 
                   ['Deflector Shields', 80], ['Cockpit', 80], ['Coaxium', 100], ['Life Support Systems', 90],
                   ['Cargo Hold', 30], ['Navicomputer', 100]]


def populate_collectibles():

    while len(collectibles_list) < 5:
        selection = random.choice(collectibles_list_database)
        # Check if doesn't exist in array and add it
        if selection not in collectibles_list:
            collectibles_list.append(selection)


def shop_menu():
    print("\nWelcome to the shop!\n"
           "[1] View Your Credits\n"
           "[2] Buy Ship Parts\n"
           "[3] Buy Collectibles\n"
           "[4] Return To Game Menu\n")
    selection = input("Make a selection: ")
    switches_shop(selection)

def display_credits():
    print("\nYou have " + str(Thrawn.getcredits()) + " credits.")
    time.sleep(1)
    shop_menu()

def isValid_input_collectible(string):
    string = str(string)
    if string.isdigit() and int(string) >= 1 and int(string) <= len(collectibles_list):
        return True
    else:
        return False
    
def isValid_input_ship_part(string):
    string = str(string)
    if string.isdigit() and int(string) >= 1 and int(string) <= len(ship_parts_list):
        return True
    else:
        return False
    
def isEmpty(list):
    if len(list) == 0:
        return True
    return False

# Display list of collectibles available for purchase
def purchase_collectible():
    while not isEmpty(collectibles_list):

        print("\nHere is a list of collectibles available for purchase: ")
        # Loop to list items in collectible 
        index = 0
        i = 1
        for _ in range(len(collectibles_list)):
            part_name = collectibles_list[int(index)][0] 
            price = collectibles_list[int(index)][1]

            print(f"[{i}]", part_name, "->", price, "credits")
            i += 1
            index += 1

        # Ask user if they would want to buy a ship part and check for valid input
        S = input("\nWould you like to purchase a collectible? (yes/no): ")
        while True:
            if isYes_No(S) is True:
                if S == 'yes':
                    S = input("\nSelect a collectible to purchase: ")

                    while True:
                        if isValid_input_collectible(S):
                            S = int(S) - 1
                            string = collectibles_list[int(S)][0]
                            price = collectibles_list[int(S)][1]

                            #Check if you have enough credits
                            if int(price) > Thrawn.getcredits():
                                print("\nNot Enough credits! Returning to shop menu", end='')
                                time.sleep(1)
                                print('.', end='')
                                time.sleep(.5)
                                print('.', end='')
                                time.sleep(.5)
                                print('.', end='\n')
                                shop_menu()

                            # If you have enough, sub credits -> add ship part to inventory
                            else:
                                Thrawn.sub_credits(price)
                                Thrawn.add_item(string)
                                Thrawn.add_multiplier()
                                collectibles_list.remove(collectibles_list[S])
                                print("\nThank you for your purchase!")
                                time.sleep(1)
                                purchase_collectible()

                        # If you don't have a valid selection
                        else:
                            S = input("Invalid selection, try again: ")

                # If you do not want to purchase a collectible, go to shop menu            
                elif S == 'no':
                    print('\nReturning to shop menu', end='')
                    time.sleep(.5)
                    print('.', end='')
                    time.sleep(.5)
                    print('.', end='')
                    time.sleep(.5)
                    print('.', end='\n')
                    shop_menu()

            # If you say something other than yes or no, state Invalid Input -> return to shop menu     
            else:
                S = input("Invalid Input Would you like to purchase something? (yes/no): ")
    if isEmpty(collectibles_list):
        print("\nNo more collectibles to purchase!\n"
              "Returning to shop menu", end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(.5)
        print('.', end='\n')
        shop_menu()

def isYes_No(string):
    if string == 'yes' or string == 'no':
        return True
    return False

def purchase_ship_part():

    while not isEmpty(ship_parts_list):
        print("\nHere is a list of ship parts available for purchase: ")
        # Loop to list items in collectible 

        index = 0
        i = 1
        for _ in range(len(ship_parts_list)):
            part_name = ship_parts_list[int(index)][0] 
            price = ship_parts_list[int(index)][1]

            print(f"[{i}]", part_name, "->", price, "credits")
            i += 1
            index += 1

        # Ask user if they would want to buy a ship part and check for valid input
        S = input("\nWould you like to purchase a ship part? (yes/no): ")

        
        while True:
            if isYes_No(S) is True:
                if S == 'yes':
                    S = input("\nSelect a ship part to purchase: ")

                    while True:

                        if isValid_input_ship_part(S):
                            S = int(S) - 1
                            string = ship_parts_list[int(S)][0]
                            price = ship_parts_list[int(S)][1]

                            #Check if you have enough credits
                            if int(price) > Thrawn.getcredits():
                                print("\nNot Enough credits! Returning to shop menu", end='')
                                time.sleep(1)
                                print('.', end='')
                                time.sleep(.5)
                                print('.', end='')
                                time.sleep(.5)
                                print('.', end='\n')
                                shop_menu()

                            # If you have enough, sub credits -> add ship part to inventory
                            else:
                                Thrawn.sub_credits(price)
                                Thrawn.add_ship_part(string)
                                ship_parts_list.remove(ship_parts_list[S])
                                print("\nThank you for your purchase!")
                                time.sleep(.75)
                                purchase_ship_part()

                        # If you don't have a valid selection
                        else:
                            S = input("Invalid selection, try again: ")

                # If you do not want to purchase a collectible, go to shop menu            
                elif S == 'no':
                    print('\nReturning to shop menu', end='')
                    time.sleep(.5)
                    print('.', end='')
                    time.sleep(.5)
                    print('.', end='')
                    time.sleep(.5)
                    print('.', end='\n')
                    shop_menu()

            # If you say something other than yes or no, state Invalid Input -> return to shop menu     
            else:
                S = input("Invalid Input! Would you like to purchase something? (yes/no): ")
                
    if isEmpty(ship_parts_list) is True:
        game.game_ending()
        
    
def switches_shop(value):
    while True:
        if value == "1":
            return display_credits()
        elif value == "2":
            return purchase_ship_part()
        elif value == "3":
            return purchase_collectible()
        elif value == "4":
            game.menu()
        else:
            selection = input("Not a valid option, try again: ")
            switches_shop(selection)
            

           
    

    

    

    

   
    

