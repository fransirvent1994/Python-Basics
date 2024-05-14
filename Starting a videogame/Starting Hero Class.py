# Here´s a tutorial about how to start creating a videogame with POO

# Let´s creat the class Hero
class Hero: # Class name
    def __init__(self, name, lifes, attack, defense): # Parameters
        self.name = name # Declaring parameters as variables
        self.lifes = lifes
        self.attack = attack
        self.defense = defense
    
    # A function to print the name of the character
    def character_name(self): # The character name function
        print(f"The name is {self.name}") 

    # Function to create the lifes a character has
    def health(self):
        self.lifes = 3
        return f"The hero has {self.lifes} lives"
    
    # Function to create how much attack and defense point they has
    def power(self):
        self.attack = 1
        self.defense = 1
        return f"The hero has {self.attack} power of attack and {self.defense} defense points"

# Contain the class hero into a variable
player_name = Hero((input("What´s the name? ")), 3, 11, 9)

# To call the values into the player_name as an object
print(player_name.name)
print(player_name.attack)

# To call the functions values inserted
print(player_name.character_name())
print(player_name.power())
print(player_name.health())

# The same way we can manipulate this to make a second Hero, which will be our companion

class Companion(Hero):
    pass

print(Companion.health(self=Companion))