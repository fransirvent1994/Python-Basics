# This is a program to create a list with different words that are accompanied with their explanations
# This can be useful to teach

import random

# First we create a variable called word that contains the words we want.
word_list = ["elephant", "fork", "island"]

# Then we have to make a variable that contains the chosen word

chosen_word = random.choice(word_list)

# We can make a conditional with if, elif and else to give the explanations for each word

if chosen_word == "elephant":
    print("It´s an animal with a very good memory")
elif chosen_word == "fork":
    print("Tool to eat, don´t try to conquer the Seven Seas with it")
elif chosen_word == "island":
    print == "The home of Robinson Crusoe"

print(chosen_word)