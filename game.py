# Author: Karch Forward
# Date 9/17/2023

# Python class that defines the game mechanics and associated functions 
# in order for a player to receieve a quote
# Also will check if end game is ever met (And congragulate them on winning if True)

import random
import quote_dictionary as quotes
import sys
import shop
from shop import Thrawn
import time

# Gets how many ships parts the player currently has
def how_many_ship_parts():
    return (Thrawn.get_ship_parts())

# Gets a random quote from the dictionary
def get_random_quote():
    # Checks to ensure quote_ditionary is not 0, if so reshuffle
    if quotes.get_length() > 0:
        random_quote = random.choice(list(quotes.list_dictionary()))
        return random_quote
    else:
        print("\nAll quotes used!")
        quotes.quote_dictionary = quotes.used_dictionary.copy()
        print("Reshuffling", end='')
        i = 0
        for _ in range(2):
            print(".", end='')
            time.sleep(.75)
            i += 1
        print('.')
        random_quote = random.choice(list(quotes.list_dictionary()))
        return random_quote
    

# Gets the answer(s) to the quote from the dictionary
def get_corresponding_value(quote):
    random_value = quotes.list_dictionary()[quote]
    return random_value

# Gives question to user (determine if they are right or wrong)
def give_question():
    Thrawn.add_questions_asked()

    for _ in range(5):
        quote = get_random_quote()
        print("\nQuote: " + quote)
        user_input = input("Who said this quote? ")

        answer = get_corresponding_value(quote)

        if user_input in answer:
            print("\nCorrect!")
            time.sleep(1)
            Thrawn.add_credits(1 + Thrawn.get_multipler())
            Thrawn.correct_counter += 1
            # Moves given quote to used dictionary
            quotes.move_quote_to_used(quote)
            
        else:
            print("\nWrong! You lost 5 points!\n")
            Thrawn.wrong_counter += 1
            time.sleep(1)
            if Thrawn.getcredits() < 5:
                Thrawn.reset_credits()
            else:
                Thrawn.sub_credits(5)
    menu()

# Print out collectible inventory
def list_collectibles():

    if len(Thrawn.get_items()) != 0:
        print("List of collectibles:")

        i = 0
        for i in range(len(Thrawn.get_items())):
            if Thrawn.get_index_items(i) != Thrawn.get_index_items(-1):
                print(Thrawn.get_index_items(i), end=', ')
            else:
                print(Thrawn.get_index_items(-1), end='\n')
    else:
        print("You do not have any collectibles!")
    time.sleep(2)

# Prints out ship parts inventory
def list_ship_parts():
    length = len(Thrawn.get_ship_parts())

    if length != 0:
        print("\nYou have " + str(length) + "/10 ship parts. Current inventory: ")

        i = 0
        for i in range(len(Thrawn.get_ship_parts())):
            if Thrawn.get_index_ship_parts(i) != Thrawn.get_index_ship_parts(-1):
                print(Thrawn.get_index_ship_parts(i), end=', ')
            else:
                print(Thrawn.get_index_ship_parts(-1))
    else:
        print("You do not have any ship parts!")
    time.sleep(2)

# Ends the program           
def end_program():
    quotes.reset()
    sys.exit("\nThanks for playing! May the Force be with you!")

# Switch cases based on player input
def switches(value):
    while True:
        if value == "1":
            give_question()
        elif value == "2":
            shop.shop_menu()
        elif value == "3":
            list_collectibles()
            menu()
        elif value == "4":
            list_ship_parts()
            menu()
        elif value == "5":
            end_program()
        else:
            user_input = input("Not a valid selection! Try again: ")
            switches(user_input)

# Invokes a method to give the player a question            
def start_game():
        shop.populate_collectibles()    
        title()
        menu()

    
# Main title text to display for a beginning of a game    
def title():
    print("------------------------------------")
    print("Welcome to the Star Wars quote quiz!")
    print("------------------------------------")
    time.sleep(1)

def game_ending():
    print("\nCongratulations! You have sucessfully aquired all\n"
          "10 of the required starship parts. Now you are able\n"
          "to travel the entire galaxy!")
    
    print("Game Statistics: \n"
          "Remaining credits -> " + str(Thrawn.getcredits()) + '\n'
          "Questions Asked -> " + str(Thrawn.questions_asked) + '\n'
          "Amount Correct -> " + str(Thrawn.correct_counter) + '\n'
          "Amount Wrong -> " + str(Thrawn.wrong_counter))
    end_program()


# Prints the menu options and waits for input
def menu():
    print("\nGame Menu:")
    print("[1] Give five questions\n"
          "[2] Show me the shop\n"
          "[3] List current collectibles\n"
          "[4] List current ship parts\n"
          "[5] Quit the game\n")
    selection = input("Please make a selection: ")
    switches(selection)


    

  



    




