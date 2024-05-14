# OOP are a way to structure data and info with commands inside of a class, which semantically looks like  a variable, but it´s not.

class Person: # Define a class
    def __init__(self, name, age, occupation): # Define the parameters
        self.name = name
        self.age = age
        self.occupation = occupation
    
    def introduce(self): # A function to introduce the person.
        return f"Hello! I'm {self.name}, I'm {self.age} years old, and I work as a {self.occupation}."

    def celebrate_birthday(self): # Function to print a birthday message +1 years
        self.age += 1
        return f"Happy birthday! I'm now {self.age} years old."

# Create objects of the Person class
person1 = Person("Bart", 30, "Engineer")
person2 = Person("Lisa", 25, "Doctor")

# Access attributes and methods of the objects
print(person1.name)
print(person2.occupation)

print(person1.introduce())
print(person1.celebrate_birthday())
print(person2.introduce())
print(person2.celebrate_birthday())