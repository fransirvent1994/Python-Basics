# On this file I will show how to use some maths on python.
# Friendly reminder that maths are not essencially necessary to program, but can be useful.

# There are tons of libraries to use maths and different kind of maths, but this is a basic tutorial, so I´ll just show the math one and the predetermined by Python.

# Library import. We will use it later, but just to clarify: Python has its own way to calculate simple operations, so it´s not necessary to import anything to calculate simple operations.

import math

# Here is a very basic example of how can be declare a variable with a number contained and operate with them.
# This is just to be clear about how it works, but it´s not a good practice, due to this kind of program is very limited.
a = 1
b = 2
basic_sum = a + b
print(basic_sum)

# So, let´s do a better program with the same logic, the only thing that must pay attention is to convert the inputs into ints. Inputs are str, so nums cannot be operated if they are strings. I´ll show how to convert them.
# This code allows the user to insert the numbers they wants by creating variables that contains inputs.
input_a = int(input("Insert a number: "))
input_b = int(input("Insert a second number:")) 
inputs_sum = input_a + input_b
print(inputs_sum)

# These examples were to sum numbers, but let´s going with the subtract of operations.
# To subtract
input_subtract_a = int(input("Insert a number: "))
input_subtract_b = int(input("Insert a second num: "))
input_subtract = input_subtract_a - input_subtract_b
print(input_subtract)

# To multiply
input_mult_a = int(input("Insert a number: "))
input_mult_b = int(input("Insert a second num: "))
input_mult = input_mult_a * input_mult_b # To multiply we use *
print(input_mult)

# To divide
input_divide_a = int(input("Insert a number: "))
input_divide_b = int(input("Insert a second num: "))
input_divide = input_divide_a // input_divide_b # To divide we use // and the output will give an int result. To be given decimals, we use /
print(input_divide)

# This way we have the basics: add, substract, multiply and divide. Let´s continue using the math library.

# We use the library declaring the name of itself before the rest, followed by .<module>
# Example with pi number.

pi_number = math.pi # math.pi could be used in a print(math.pi) and the result would be outputed, but I think is better to contain in a variable.
print(f"Pi number is: {pi_number}") # By using print(f{variable}) we can get access to the data inserted in the variable.

e_value = math.e
print(f"e value is: {e_value}")

# To clarify this one, this is the square root number.
# It could have just been used with print(math.sqrt(9)), but with this extract the user can interact with data and insert the number to be calculated.
# Variable number contains the number to be inserted converted into int.
# sqrt_num variable contains the module sqrt with the value given in the input with the variable number.
number = int(input("Insert a number: "))
sqrt_num = int(math.sqrt(number))
print(sqrt_num)

# These are some examples of basic maths with the library math and some of its modules, but it has more modules.
# As I said, this is the basic of Python maths, there are more scientific libraries. They will be explained in another repository.