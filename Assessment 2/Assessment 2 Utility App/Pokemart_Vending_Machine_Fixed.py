
# Importing os allows me to clear console.
import os
# Importing time allows me to time-related functions.
import time

currency = 79250

# Pokestock
Potion = [15, 300, 'Potion']
PokeBall = [25, 200, 'Pokeball']
GreatBall = [30, 600, 'Great Ball']
Superpotion = [30, 600, 'Super Potion']
Lure = [25, 600, "Lure"]
Escaperope = [25, 750, "Escape Rope"]

# Masterstock
MaxPotion = [35,750,'Max Potion']
MasterBall = [25, 100000, 'Masterball']
Mysteriouspokeball = [25, 1000, 'Mysterious Pokeball']
Expcandy = [25, 1500, 'EXP Candy']

# Finalstock
Goldmedal = [1,0,'Gold Medal']

# Stores
pokestore = {"1":Potion, "2":PokeBall, "3":GreatBall, '4':Superpotion, '5':Lure, '6':Escaperope}
masterstore = {"1":MaxPotion, "2":MasterBall, "3":Mysteriouspokeball, "4":Expcandy}
finalstore = {"1":Goldmedal}

# Variables for confirm()
cartbool = True
cart = {}
choice = ""
amount = ""
count = 0

# Variables for selection()
outofstockattempts = 0
removelist = ''

# Locks for repeated iteration.
pokestoreupgradelock = False
masterstoreupgradelock = False
finallock = False
upgradelock = True
# A counter for check() function
emptystores = 0
emptystockcount = 0
exitcode = False
cartchoice = ''

#########################

# Animation Functions

def newprint(prompt,duration):

    # This counts the amount of letters or characters in the given prompt.
    charactercount = len(prompt)

    # The variable contains the amount of time each character within the limited duration.
    # This makes it so that the animation finishes at the exact amount of duration. 
    timeslice = duration / charactercount

    for character in range(charactercount):
        # This allows me to slice one letter or character from the given prompt based on index given by charactercount range. 
        # Print function automatically ends with a new line. With the "end" perameter, I can overwrite the end to an empty string so that
        # The code doesn't print a new line in a for loop. This matters when Im using this code for text
        print(prompt[character],end='')

        # This function forces the console to wait for a specific amount of time in seconds before the loop continues.
        # This is where the timeslice comes in use.
        time.sleep(timeslice)

def clearconsolelines():

    # This code clears everything on console.
    os.system('cls')
   
# System Functions

def check():
    # variables are made global so I dont have to include them in the parentheses.
    global pokestore
    global masterstore
    global finalstore
    global finallock
    global upgradelock
    global emptystores
    global emptystockcount
    global pokestoreupgradelock
    global masterstoreupgradelock
    global cartbool
    global cart 
    global choice
    global amount 
    global count 

    # The code checks if the store's stocks are all empty.
    # If it's empty, the code tags the store empty with a variable that declares it. Another variable then would count how many stores are empty.

    for value in pokestore.values():
        if value[0] == "Out of Stock":
            emptystockcount = emptystockcount + 1

    # If the stocks that are empty equal to the amount of stocks available in the store, 
    # it counts 1 store empty and the upgrade lock is now false. ( When the upgrade lock is false, 
    # you then now have the option to upgrade the store.)
    
    if emptystockcount == len(pokestore):
        emptystores = emptystores + 1
        upgradelock = False

    # The stockcount is then reset for the next store to check.

    emptystockcount = 0

    # The same system is applied, but we now check the next store which is the masterstore.

    for value in masterstore.values():
        if value[0] == "Out of Stock":
            emptystockcount = emptystockcount + 1

    # When the masterstore is identified 'empty', the counter counts 2 ( different to the first store being empty)
    # so that we are able to have a different results in choiceinput() function. 

    if emptystockcount == len(masterstore):
        emptystores = 0
        emptystores = emptystores + 2

    # The counter then resets.
    emptystockcount = 0

    # The same empty stock counting is applied.

    for value in finalstore.values():
        if value[0] == "Out of Stock":
            emptystockcount = emptystockcount + 1

    # If finalstore stock is now empty, the variable for the Vending Machine's ending is then assigned.

    if emptystockcount == len(finalstore):
        finallock = True

    # These variables, and a dictionary resets the value so that 
    # when the functions call on the code it's fresh.
    cartbool = True
    cart = {}
    choice = ""
    amount = ""
    count = 0 

def display():
    # variables are made global so I dont have to include them in the parentheses.
    global pokestore

    newprint(f"""
##############################
Welcome to the Pokemart Vending Machine!
Your Currency: ${currency}
# Items Available:                    
                  \n\r""",0.1)

    # For every key:vaue in the dictionary it prints out the index(key),
    # and takes values(from the list inside the key's value) to fill in
    # information such as: amount, price, and name.

    newprint('[Index]: Item (Amount) - Price\n########################\n',0.10)
    for key,value in pokestore.items():
        newprint(f"[{key}]: {value[2]} ({value[0]}) - ${value[1]}\n",0.10)

    newprint(f"""\n
- Back:  
##############################
    \r\n""",0.1)

def simpledisplay():
   # variables are made global so I dont have to include them in the parentheses.
    global pokestore

    newprint(f"""
##############################
Your Currency: ${currency}
# Items Available:                    
                  \n\r""",0.01)

    # For every key:vaue in the dictionary it prints out the index(key),
    # and takes values(from the list inside the key's value) to fill in
    # information such as: amount, price, and name.

    for key,value in pokestore.items():
        newprint(f"[{key}]: {value[2]} ({value[0]}) - ${value[1]}\n",0.01)

    newprint(f"""\n
##############################
    \r""",0.01) 

def choiceinput():
    global choice
    global pokestore
    global masterstore
    global finalstore
    global currency
    global emptystores
    global pokestoreupgradelock
    global masterstoreupgradelock

    # This is where the variables that were modified in check() affect this function.

    # When finallock is enabled. You are given a new and only one option for the input.
    
    if finallock is True:
        choice = input("What would you like to do?\n-end\n:")

        # If the input is not the same as the only option, the question simply loops.

        while choice.lower() != "end":
            clearconsolelines()
            display()
            choice = input("What would you like to do?\n-end\n: ")

            # If it equals to 'end', the loop is lifted and the code flows and reaches its end.
            # The vending machine then ends with all its stocks are empty.

        if choice.lower() == "end":
            clearconsolelines()
            newprint("Thank you for using the Vending Machine....\n", 1)
            newprint("Closing Program...", 3)
            exit()

    # When upgradelock is false, we now unlock the option to upgrade.

    if upgradelock is False:
        
        # If there are empty stores, the code is stuck in the following code to prevent
        # the user to buy from an empty store. However, if masterupgradelock is True
        # (the indicator that finalstore is unlocked), this code won't play.

        # This was done as I wasn't able to find a way to optimize the code in check(), 
        # but at least it prevents the user from being unable to buy from finalstore.

        if emptystores > 0 and masterstoreupgradelock is False:
            choice = input("What would you like to do?\n-exit\t-upgrade\n: ")

            # If the user disobeys and chooses to buy, this code plays to prevent the user to get through.
            # You are informed why and display is replayed then you are given a chance to input again.

            while choice.lower() == "buy":
                clearconsolelines()
                newprint('All stocks are empty, there is nothing you can buy. Please try again.\n',0.5)

                display()
                choice = input("What would you like to do?\n-exit\t-upgrade\n: ")

        else:
            choice = input("What would you like to do?\n-buy\t-exit\t-upgrade\n: ")
        
        # If you choose to upgrade, the following if statement plays.

        if choice.lower() == "upgrade":

            # If you choose to upgrade but the masterstore upgrade lock is enabled, 
            # you are then prevented and informed that you cannot upgrade again when you already have.
            # You are then put in a loop until you choose something else.
            # The rest of the functions mentioned are for display.
            
            while choice.lower() == "upgrade" and masterstoreupgradelock is True:
                clearconsolelines()
                print("The store is already upgraded. Please try again.")
                
                display()
                choice = input("What would you like to do?\n-buy\t-exit\t-upgrade\n: ")

            # If there is no master store upgrade lock, two conditions have to be met
            # to be able to upgrade. 1 is that your choice is to upgrade, and 2 is that there are
            # the specific emptystores to meet the conditions. 

            if choice.lower() == "upgrade" and emptystores == 2:

                # This is where the locks are enabled after the upgrade is done to prevent
                # repetitive upgrades. Pokestore upgrade lock is made false so that you won't go
                # through another prevention after this code.


                pokestore = finalstore
                masterstoreupgradelock = True
                pokestoreupgradelock = False

            # Similar system, but different lock for the other store. This is for the pokestore lock when
            # you have already upgraded the store. 

            while choice.lower() == "upgrade" and pokestoreupgradelock is True:
                clearconsolelines()
                print(f"The store is already upgraded. Please try again.")

                display()
                choice = input("What would you like to do?\n-buy\t-exit\t-upgrade\n: ")

            if choice.lower() == "upgrade" and emptystores == 1:
                pokestore = masterstore
                pokestoreupgradelock = True
    
    # If upgradelock is on and finallock is on, you are brought in the else statement
    # and only have two options: 'buy' or 'exit.'

    else:
        choice = input("What would you like to do?\n-buy\t-exit\n: ")


   # Within the choiceinput() function, the emptystores variable is reset to 0 to have a controlled rate for upgrading stores.
    emptystores = 0
        
    # These if statements contain strings which contains coupons that adds more money to your currency.
    if choice.lower() == "metaverseagediscount":
        currency += 100000
        clearconsolelines()
        print("Coupon redeemed...\n")

    if choice.lower() == "theanonymousmaugift":
        currency += 2588750
        clearconsolelines()
        print("Coupon redeemed...\n")

    # If the input says 'exit', the code is terminated and the system ends using the exit() code.

    if choice.lower() == "exit":
        clearconsolelines()
        newprint("Thank you for using the program...",1)
        exit()

    # If input says neither, the console is cleared to not fill up the console with multiple displays.
    # The code will loop in the system therefore there are multiple displays but this code prevents it.
    if choice.lower() != "exit" and choice.lower() != "buy":
        clearconsolelines()

def selection():
    # variables are made global so I dont have to include them in the parentheses.
    global pokestore
    global cart
    global choice
    global amount
    global outofstockattempts
    global removelist

    while True:
        choice = input("Enter an index to select your item: ")
        
        # The following if statements fool proof the code so it prevents unwanted
        # input to slip through.

        if not choice.isdigit():
            print("Invalid input. Please try again.")
            continue

        if choice not in pokestore.keys():
            print("The item you are looking for is not in stock. Please try again.")
            continue

        # This if statement catches the code if choice is in the cart
        # That way it asks the user again if they want to modify the order.
        if choice in cart.keys():
            receiptcheck = input("Would you want to modify the previous item you bought?\n-yes\t-no\n: ")

            # This loop prevents the code to go through until the input is either 'yes' or 'no.'
            # I wouldn't use 'or' because if one were true(let's say 'no', but 'yes' is false)
            # The input 'yes' will not allow the code to pass because of 'or' used in the while loop wall.
            while receiptcheck.lower() != "yes" and receiptcheck.lower() != "no":
                receiptcheck = input("Would you want to modify the previous item you bought?\n-yes\t-no\n: ")

            # If the user does not want to modify the item, selection resets.
            if receiptcheck.lower() == "no":
                print("Please select a different item.")
                continue
        
        # If the list called has 'Out of Stock' in the first index, the code is prevented
        # to pass and is informed why before it resets the loop with 'continue.'

        # The code is placed in a try and except statement to avoid the error of comparing an integer and a string.

        try:
            if 'Out of Stock' == pokestore[choice][0]:
                print("This item is out of stock. Please try another item.")
                continue
        except:
            continue

        # This input confirms the number you entered just in case the user didn't
        # read the display. If the choice is in the cart, this code won't play.
        if not choice in cart.keys():
            check = input(f"Would you like to buy {pokestore[choice][2]}?\n-yes\t-no\n: ")
        
            if check.lower() != "yes" and check.lower != "no":
                print("Invalid input. Try again.")
                continue
 
            if check.lower() == 'no':
                print("Pick another item.")
                continue

        # This input asks for amount of the item selected. This variable matters for the next coming functions.
            
        amount = input(f"How much {pokestore[choice][2]} would you like?\n: ")

        if not amount.isdigit():
            print("The amount is not a valid number. Try again.")
            continue
        
        # If the user placed 0 in the amount, you are given an option to remove the item from the cart list, or
        # if it was a misclick you can refuse. 

        if int(amount) == 0:
            clearconsolelines()

            removelist = input(f"Would you like to remove {pokestore[choice][2]} from the list?\n-yes\t-no\n: ")

            # If the input is neither 'yes' or 'no', the code simply will loop until your answer is one of the options.

            while removelist.lower() != 'yes' and removelist.lower() != 'no':
                removelist = input(f"Would you like to remove {pokestore[choice][2]} from the list?\n-yes\t-no\n: ")
            
            # If the answer is no, the code will show its display and simply continue the function.

            if removelist.lower() == 'no' and len(cart) > 0:
                clearconsolelines()
                simpledisplay()
                continue

            # If the answer yes but the cart hasn't been even filled yet, you will get ridiculed for your decision.

            if removelist.lower() == 'yes' and len(cart) == 0:
                clearconsolelines()

                # The variable is then reset.
                removelist = ''

                newprint("\nThe cart list is empty and you're already removing something from it?\nJust pick an item.\n",3)
                simpledisplay()
                continue


        # If the user is reusing the code and has made the stock less than the amount required
        # The code is then rejected and resets the entire function.

        if int(amount) > pokestore[choice][0]:
            print("You're buying too much than what's available in the stock. Please try again.")
            continue

        else:
            

            # If the user wants to remove the item from the cart list, the removelist would be assigned with the 'yes' string
            # value. With this, I can create a wall where if removelist has 'yes' in their values this code won't play.
            # This is for the sake of not adding more numbers to the cart.

            if removelist.lower() != 'yes':
                # If the item selected is being modified, the value in the list is changed instead of adding a new dictionary.
                if choice in cart.keys():
                    cart[choice][3] = int(amount)

                # The amount and the item you selected(the entire list not the name.) is then
                # stored in a list which serves as a shopping cart.

                cart[choice] = pokestore[choice]
                pokestore[choice].append(int(amount))
                break        

            # Break function is then executed to close the function.
            break
        
def confirm():
    # Variables are made global so I dont have to include them in the parentheses.
    global cart
    global pokestore
    global totallist
    global cartbool
    global currency
    global exitcode
    global removelist

    # Variables only for this function.
    totallist = []


    clearconsolelines()

    # From selection() function, if the user did confirm to delete the item from the cart list,
    # This if-statement then obeys the order and runs the specific code to delete it from the list.

    
    if removelist.lower() == "yes":
        newprint(f'Removing {pokestore[choice][2]}... \n', 0.1)
        del cart[choice]
    
    # Variables are reset to not keep old answers
    cartchoice = ''
    removelist = ''
    
    # If the cart is empty, you are given a choice to continue, or go back to menu.

    if len(cart) == 0:
        cartchoice = input('The cart list is now empty.\nWould you like to exit?\n-yes\t-no\n: ')

        # If the cartchoice is neither 'yes' or 'no', the code simply loops until the input is one of the options.

        while cartchoice.lower() != 'yes' and cartchoice.lower() != 'no':
            cartchoice = input('The cart list is now empty.\nWould you like to exit?\n-yes\t-no\n: ')
        
        # If you don't want to exit, the function returns and goes back to the beginning of the loop.
        if cartchoice.lower() == 'no':
            clearconsolelines()
            return
        
        # If you want to exit, exitcode becomes "True" (This will be useful in the System), 
        # and cartbool (The variable responsible for the selection() and confirm() loop)4
        # will become False and the function is then returned. 
        # This should bring the user back to the beginning of the system.

        if cartchoice.lower() == 'yes':
            clearconsolelines()
            exitcode = True
            cartbool = False
            return
    
    # The variables are reset if its the second iteration and cartchoice couldn't change.
    exitcode = False
    cartbool = True
        
    newprint(f"""
###############################
Your purchase list is:
    \r\n""",0.3)
    
    newprint('Item - Amount - Price\n########################\n',0.10)
    for value in cart.values():
        newprint(f"{value[2]} - ({value[3]}) - ${value[1]*value[3]}\r\n",0.10)
        totallist.append(value[3]*value[1])

    newprint(f""" 
-----------------------
Current Balance: {currency}
###############################
    \r""",0.1)
    
    receiptcheck = input("Would you like to add on to your cart?\n-yes\t-no\n: ")

    # If the input does not match 'no', the user is just stuck in a loop till 
    # the input matches the following 'if' statements. This prevents the code to
    # pass without typing the negative option that is 'no'.

    while receiptcheck.lower() != "no" and receiptcheck.lower() != "yes":
        receiptcheck = input("Would you like to add on to your cart?\n-yes\t-no\n: ")

    # If the user wishes to add more to the cart, the code first clears the console lines
    # to make it seem like it started fresh but the info is stored in variables outside the system.
    # Then the code passes through and since the while loop condition is still true, it continues to selection.
    
    if receiptcheck.lower() == "yes":
        clearconsolelines()
    
    # If the user does not wish to add more to the cart, 
    # it sets the variable that puts simpledisplay, selection, and confirm to
    # False which breaks the loop and heads straight to payment.

    if receiptcheck.lower() == "no":
        cartbool = False
    
    return

def payment():
    # variables are made global so I dont have to include them in the parentheses.
    global totallist
    global cart
    global pokestore
    global choice
    global amount
    global currency

    while True:
        # This code is used to count the attempts.
        global count

        # If the code exceeds 6 amount of tries, the code breaks the loop and the function ends with no changes.

        if count > 6:
            print("It seems you are unable to pay for your purchases. Resetting system...\n")
            break
        
        # Pay asks for the user to input the amount of cash the user selectively pays.

        print(f"\nIt will be ${sum(totallist)} dollars.")
        pay = input("Enter the amount to pay: ")

        # This if statement blocks strings and etc.
        if not pay.isdigit():
            print("Invalid input. Try again.")
            continue

        # This if statement resets the code if the amount you pay is more than your currency.
        # It avoids the user from being in debt.
        if int(pay) > currency:
            print("You're paying more than you can. Don't even try to be in debt.\nResetting system...")
            count += 1
            continue
        
        # This if statement resets the code if the amount you pay is less than what is required.
        # It avoids the user for paying less than required.
        if int(pay) < sum(totallist):
            print("Your payment does not satisfy the required currency. Try again.")
            count += 1
            continue     

        # If the code is not caught by the if statements, 
        # the input has no issue and will carry on the full process of payment.

        currency -= sum(totallist)

        # For every key and value in cart:
        # First, it deducts the amount bought (this info is taken from cart)
        # from stock in the original dictionary(pokestore)
        
        for key, value in cart.items():
            pokestore[key][0] -= cart[key][3]

            # Second, it checks if the value that contains amount is 0
            # If the amount is 0, it changes the list data into 'Out of Stock"

            if value[0] == 0:
                value[0] = "Out of Stock"
                value[1] = ""

        # These lines of code prints out the change, and the line of confirmation before the function breaks.
        clearconsolelines()
        print(f"Returning change: ${int(pay) - sum(totallist) }..")
        print("Purchased succesfully!")
        
        break  
            
############################

# System:

while True:

    # This function checks if the items in the store are out of stock.
    # If the store is out of stock, the stocks are replaced with a different level of stocks
    # which are more expensive and exclusive.
    check()

    display()

    choiceinput()

    # If the input says 'buy', the system begins.
    if choice.lower() == "buy":
        # This clears consolelines as I will reintroduce display than having two displays.
        # This allows me to replay display when confirm function clears the console.
        clearconsolelines()

        # Selection and confirm is in a while loop so that if the user wants to add more to the cart
        # Instead of confirm calling the selection function, it exits and the loop brings the user back to selection.
        # Data from previous iteration won't be erased as it is stored in an outside variable, and dictionary.

        while cartbool == True:
            simpledisplay()
            selection()
            confirm()
        
        if exitcode == False:
            payment()

##########################




    

    


    