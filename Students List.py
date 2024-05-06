# This code is a lesson about how to make a students list names with the basic of Python commands.
# Variable declared of students. It is an empty list to fill with data.
students = []

# I decided to use a function to make it easier. This function will contain the commands to choose an option.
def get_option():
    while True:
        option = input("""Choose an option:
    1: Add a name 
    2: See the students list names
    3: Search for a student name
    4: Erase student name
    5: Exit\n """)
        
        if option in ["1", "2", "3", "4", "5"]:
            return option
        else:
            print("Invalid input. Please choose a valid option.")

# We use a loop while to keep the list activated while being used.
while True:
    # List of options
    print("1: Add a name")
    print("2: See the students list names")
    print("3: Search for a student name")
    print("4: Erase a student name")
    print("5: Exit")

    # Choice is the name of the variable that contains the function.
    choice = get_option()

    if choice == "1":
        # Add a student name to the list
        student_name = input("Add a student name: ")
        students.append(student_name)
        print("Student name added!")

    elif choice == "2":
        # Display the list of student names
        print("List of student names:")
        for student in students:
            print(student)

    elif choice == "3":
        # Search for a student name
        search_name = input("Enter the student name to search: ")
        if search_name in students:
            print(f"{search_name} is in the list.")
        else:
            print(f"{search_name} is not in the list.")

    elif choice == "4":
        # We declared a variable to delete a name that contains an input that will be filled with a name from the list in order to be erased.
        deleted_name = input("Insert the student name you want to erase: ")
        # If-else used to detect if the student name exists or not.
        if deleted_name in students:
            students.remove(student_name)
            print("Student erased!")
        else:
            print("An error occurred. Try again.")

    elif choice == "5":
        # Exit the program
        print("Exiting...")
        break
