# How to generate a password
# Start by importing random and string libraries.
from random import choice, shuffle # With choice the program will select the password generated with the characters, and shuffle is used for mixing them
import string

# A function to script how the system will create the password
def randomPassword():
    # Lower and upper letters and digits are listed with the string method
    lower = list(string.ascii_lowercase) # Lower/minus characters
    upper = list(string.ascii_uppercase) # Upper characters
    digits = list(string.digits) # Special characters and numbers
    
    # All of them will be added each other
    all = lower + upper + digits
    #Mix them with shuffle
    shuffle(all)
    # length to determine how many characters do you want to have the password
    length = int(input("How long do you wanna the password be?\n"))
    # An empty variable to fill later
    password = ""
    # Password variable will be added with choice method, that takes the all variable mixed
    for i in range(length):
        password += choice(all)
    
    print(password)

randomPassword()