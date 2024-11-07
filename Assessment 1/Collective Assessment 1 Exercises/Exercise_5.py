## Exercise 5: Days of the Month - 30 Marks

# Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.


print("This program will identify how many days in the said month in your input.\nThe system only accepts numerical terms of the months and not the names of the months.")
while True:
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    print("Type 'exit' to close the program.")
    call = (input("Please input your month:  "))
    
    # If the input was other than the number of the months, I made a system to handle those problems.
    
    if call.lower() == "exit":
        print("Closing the program..")
        # The entire while loop breaks ending the entire code.
        break

    if call == "":
        print("Input empty. Please enter the month you'd like to pick.")
        continue

    if not call.isdigit():
        print("The system only accepts numerical terms of the months and not the names of the months.")
        continue
    
    # I made the call variable (which has the input) into an integer to be equal to the required condition to open this code:
    if int(call) == 1:
        # I used the ".get" code to get only the values of the said key in the parentheses. I learned this from my brother and discovered it in pythoncheatcodes.org.
        print(f"January has {months.get(1)} days.")
        # The code continue brings the code back to the first code of the while loop so I can have infinite amount of times to input a month until I type 'exit.'
        continue
    if int(call) == 2:
        tell = (input("Is the year a leap year? \n:"))
        if tell == "yes":
            months[2] = 29
            print(f"February has {months.get(2)} days.")
            continue
        if tell == "no":
            print(f"February has {months.get(2)} days.")
            continue
        else:
            print("Please input the proper option. \nResetting program..")
            continue
    if int(call) == 3:
        print(f"March has {months.get(3)} days.")
        continue
    if int(call) == 4:
        print(f"April has {months.get(4)} days.")
        continue
    if int(call) == 5:
        print(f"May has {months.get(5)} days.")
        continue
    if int(call) == 6:
        print(f"June has {months.get(6)} days.")
        continue
    if int(call) == 7:
        print(f"July has {months.get(7)} days.")
        continue
    if int(call) == 8:
        print(f"August has {months.get(8)} days.")
        continue
    if int(call) == 9:
        print(f"September has {months.get(9)} days.")
        continue
    if int(call) == 10:
        print(f"October has {months.get(10)} days.")
        continue
    if int(call) == 11:
        print(f"November has {months.get(11)} days.")
        continue
    if int(call) == 12:
        print(f"December has {months.get(12)} days.")
        continue
    else: 
        print("The number you placed is unrealisitic. Please input a proper number of the month.")
        continue