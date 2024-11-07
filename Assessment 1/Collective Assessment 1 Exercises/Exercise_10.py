# Exercise 10: Is it even? - 35 Marks

# Made it into a while loop to keep asking for input until "exit" is being inputted.
while True:
    def check(a):
        if int(a) % 2 == 0:
            print("The number is even!")
        else:
            print("The number is odd!")

    numb = (input("Enter a number: "))

    # Foolproofed it if:
    #       - The input is empty.
    #       - The input is a string 

    if numb == "":
        continue
    # The code breaks if exit is inputted.
    if numb.lower() == "exit":
        print("Closing program...")
        break
    if not numb.isdigit():
        continue
    # The code continues the loop after it performs.
    check(numb) 
    continue