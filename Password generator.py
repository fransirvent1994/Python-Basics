# How to generate a password
# Start by importing random library, which will be used to generate the password.
from random import choice, shuffle
import string

def randomPassword():
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)

    all = lower + upper + digits

    shuffle(all)
    length = int(input("How long do you wanna the password be?\n"))

    password = ""

    for i in range(length):
        password += choice(all)
    
    print(password)

randomPassword()