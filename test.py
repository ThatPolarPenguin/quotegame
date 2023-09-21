# Temporary file to test functions before implementing into main game

import random
import time


if __name__ == "__main__":


    used_dictionary = { }

    quote_dictionary = {
                        # Episode I
                        "I will not condone a course of action that will lead us to war.": ["Padme Amidala", "Queen Amidala", "Padme"],
                        "You're under arrest Chancellor.": ["Mace Windu", "Master Windu"]}

    while True:
        if len(quote_dictionary) > 0:
            random_quote = random.choice(list(quote_dictionary))
            print(random_quote)
            used_dictionary.update({random_quote:quote_dictionary.get(random_quote)})
            quote_dictionary.pop(random_quote)

        else:
            print("\nAll quotes used!")
            quote_dictionary = used_dictionary.copy()
            print("Reshuffling", end='')
            i = 0
            for _ in range(2):
                print(".", end='')
                time.sleep(.75)
                i += 1
            print('.')

            random_quote = random.choice(list(quote_dictionary))
            print(random_quote)



 

            