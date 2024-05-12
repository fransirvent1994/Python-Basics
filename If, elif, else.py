# Here we´re gonna see the differences and different uses between if, elif and else.
num1 = 2
num2 = 2
res = 2 + 2

# If:
# If is used to open a conditional.

if res == 4:
    print("The result is 4 and this is an example of if")

# We can use elif for different choices, for example, a list.
import random

words = ["baker", "street", "Sherlock"]

chosen_word = random.choice(words)

if chosen_word == "baker":
    print("The baker is an if bc it opens the conditional")
elif chosen_word == "street":
    print("This is an example of elif")
elif chosen_word == "Sherlock":
    print("This is another example of elif with Sherlock")

# Else is the last line to make an appointment like "this is it, no more options"

if res == 4:
    print("This example comes before else bc if is the first line, and this is the if part")
else:
    print("This example is an else, and it is the end of the road for it")
