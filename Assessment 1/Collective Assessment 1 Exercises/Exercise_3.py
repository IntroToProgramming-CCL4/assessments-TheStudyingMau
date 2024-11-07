## Exercise 3: Biography - 25 Marks

# In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

####################################

person = {}
print(person)
print("The dictionary is empty.")

# Code is looped if the input is not yes or no. If the code is no, the loop breaks ending the entire program.
answer = (input("Would you like to input your information in the dictionary? \n: "))
while answer != "yes":
    if answer == "no":
        break
    answer = (input("Would you like to input your information in the dictionary? \n:"))

# To avoid code reaching here, I have to apply a condition as a wall.
if answer == "yes":
    name = (input("Enter the name: "))

    # Foolproof is added if nothing is entered.
    while name == "":
        print("Please enter the name in the blank.")
        name = (input("Enter the name: "))

    hometown = (input("Enter the hometown: "))
    while hometown == "":
        print("Please enter the hometown in the blank.")
        hometown = (input("Enter the hometown: "))

    age = (input("Enter the age: "))
    
    # Made a collective foolproof. If the code is either a blank, a string, or a negative number, it will loop.
    # Using the "isdigit()" for me was initially to block string inputs, but knowing that it can reject blank and negative numbers made my code a bit simpler.

    while not age.isdigit():
        print("Error. Please put the correct input.")
        age = (input("Enter the age: "))

    print("Making all changes.... \n Changes are made successfully. \n")

    # Input is being applied to the person dictionary.
    person['Name'] = (name)
    person['Hometown'] = (hometown)
    person['Age'] = (age)
    
    # Used for loop to have each key and value placed on different lines
    for key, value in person.items():
        print(key + ":", value)

    choice = (input("\nWould you like to make changes to the dictionary? \n:"))
    # From this point, I'll make a loop to be able to constantly change the info inside the dictionary until they call the exit code.
    while choice != "no":
        newkey = (input("Enter to add or modify a key: "))
        newvalue = (input("Enter the value to add or modify: "))

        # Made the same foolproof if they ever modify the age.

        if newkey == "Age":
            while not newvalue.isdigit():
                print("Error. Please put the correct input.")
                newvalue = (input("Enter the value to add or modify: "))

        print("Making all changes.... \n Changes are made successfully. \n")
        person[newkey] = newvalue

        for key, value in person.items():
            print(key + ":", value)

        choice = (input("\nWould you like to make changes to the dictionary? \n:"))

# In my while condition, if the answer is no. Since this is the end of the for condition, it exits outside the condition which prints this and ends the code.
print("Thank you for using the Python dictionary")
        
