# Variables are the way to introduce values into words that work as containers of info or data.
# It´s the basic of any program language

# A variable must follow some rules:
# To be minus
# Not to be numbers, or start with it.
# Neither start with "_"or special characters
# Cannot be a reserved word of Python (such as "def")

message = "Hello world" # Variable message contains the value "Hello world"
print(message) # Command print will show the value of message.

# Numbers
# Variables with number values works the same way, but it´s very important to keep the code clean and clear.
# It means that, when we create a variable name, we should make it clear to what it is referenced for.

# For example, a bad practice could be using a variable which be "hello = 2"

num1 = 1 # The variable num1, referenced to number 1, contains the value 1.
# This value is an integer, which means that is an entire number, not a string, real or float, its an int.
# Strings number cannot be operated, they join theirselfs

string_num = "1" # This is not a number, is a string.

# We can replace the value of a variable just by rewriting them with a new value.
num1 = 3 # Above, num1 was 1, but now is 3
num2 = 2
result = num1 + num2 # Result variable contains the sum of num1 and num2
print(result)

