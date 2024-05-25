# Here we´re gonna learn about how lists work.
# First things first:
"""Lists are mutable, it means they can be modified, and they are declared by []"""

# Let´s start declaring a variable which contains a list:

my_list = [1, 2, 3]
# Now we have a list declared with 3 numbers, so we´re gonna get access to them.

# First, let´s print the contain.
print(my_list) # This prints the original list values.

# Let´s see what happens when we want to get access to any of the elements of the list.
# First, let´s make a point:
    # When we talk about elements in Python, 
    # it doesn´t start counting on 1, but in 0, 
    # so first number won´t be in [1], it will be in [0]

#So, to access the element on the list, we will add the [num] we are looking for, like the element 2, so:
print(my_list[1]) # It will print second element on the list, number 2 in this case.

# If we want to add a new element,
my_list.append(4) # This way we add number 4 on the list at the tail
print(my_list) # Now the list will be printed with the new element
# To remove an element:

my_list.remove(4) # We have erased the number 4 from the elements on the list
print(my_list) # Now the list is printed without num 4

# We can add different elements on the list at the same time also by doing ([])
my_list.extend([4, 5, 6])
print(my_list)

# with sort the list will be ordered in ascending order, so, I will declare a new list.
my_new_list = [8,4,2,5,9]
my_new_list.sort()
print(my_new_list)

# With pop we can see if we have an element that matches with the value and be erased.
my_list.pop(2)
print(my_list)