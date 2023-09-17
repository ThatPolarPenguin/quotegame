import random


if __name__ == "__main__":

    test = ['apple', 'banana', 'pear', 'orange', 'melon', 'berry', 'pie', 'chocolate', 'cheesecake']

    empty = []

    while len(empty) < 5:
        selection = random.choice(test)
        # Check if doesn't exist in array and add it
        if selection not in empty:
            empty.append(selection)
        

    print(empty)




