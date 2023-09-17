# Python class to define a player and their associated attribute
# Contains various getters/setters to manipulate atrribute values

class Player:
    def __init__(self):
        self.credits = 0
        self.ship = []
        self.items = []
        self.multiplier = 0
        self.wrong_counter = 0
        self.correct_counter = 0
        self.questions_asked = 0

    def got_wrong(self):
        self.wrong_counter += 1

    def got_correct(self):
        self.correct_counter += 1

    def add_credits(self, value):
        self.credits += value

    def add_questions_asked(self):
        self.questions_asked += 5

    def sub_credits(self, value):
        self.credits -= value

    def getcredits(self):
       return self.credits
    
    def reset_credits(self):
        self.credits = 0
    
    def state_credits(self):
        return "You currently have " + str(self.getcredits()) + " points!"
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_index_items(self, index):
        return self.items[index]

    def get_items(self):
        return self.items
    
    def add_ship_part(self, part):
        self.ship.append(part)

    def get_ship_parts(self):
        return self.ship
    
    def get_index_ship_parts(self, index):
        return self.ship[index]
    
    def get_multipler(self):
        return self.multiplier
    
    def add_multiplier(self):
        self.multiplier = self.multiplier + 1
    
    
    
    


