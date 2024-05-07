# Functions are a way to write clean code. It make coding easier and cleaner, besides of shorter.

# From scratch, a Hello world function.

def hello_world(): # Init function
    return "hello world!" # Return inside the function

hello_world() # Calling the function

# This is the basic structure of a function, but there are more ways to do it.

def message():
    text = input("Insert a message: ")
    print(f"The message was {text}")

message()

# It can be used for maths too.

def sum_1(n1, n2):
    return n1 + n2
    
result = sum_1(2, 3)
print("Sum is:", result)

# It also can be used to make easier and shorter the code when, without functions, would take tons of codes.
# For example, we have the Hello World above in the first example, but that´s not its final use.
# We can recall the function again just by:

hello_world() # this calls again the function
print(hello_world() * 6) # this calls the function and also prints it 6 times.
print(" ".join([hello_world() for _ in range(6)])) # This one prints the samen but with spaces between them

# As valuable info, it also can be used for games, for example:
# Imagine we want to make a robot with attacks, and these attacks come from its arms, from a direction to another.

def left_arm():
    return "It kicked your right side"

print(left_arm())