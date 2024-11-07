## Exercise 6: Brute Force Attack - 30 Marks

password = (input("What's the password? \n:"))

# Stored the passwords in a list in order to be able to count the attempts.

attempts = []
while password != "12345":
    attempts.append(password)
    number = 5 - len(attempts)
    # Note 1: If the attempts are exhausted, this code plays and the loop is broken.
    if number == 0:
        print("You have exceeded the amount of attempts given. Calling the authoroties for attempting on breaking in the national bank.")
        break
    print(f"Incorrect. You have {number} attempts left. Please try again.")
    print("Please try again.")
    password = (input("What's the password? \n:"))

# If the code is correct. This code plays confirming the user's entry of the password is correct.
if password == "12345":
    print("Welcome back. Sigma rizzler ohayo fanum tax mayor. You may access the national funds of this country.")

