
## Exercise 4: Primitive Quiz - 30 Marks

choice = (input("Hi! Would you like to take a quiz about 10 capitals of each European countries? \n-Yes     -No\n: "))

if choice == "no":
    print("Oh, well that's a bummer.")
    print("Okay then. Have a nice day, I guess..")

while choice != "no" and choice != "yes":
    choice = (input("Hi! Would you like to take a quiz about 10 capitals of each European countries? \n-Yes     -No\n: "))

if choice == "yes":
    print("That's great! I hope you studied for this quiz.")
    print("Let's begin.")

    answ1 = (input("Question 1: What is the capital of France? \n: "))
    # Note: ".lower()" makes any string of the variable into lowercase. That way I don't have to have an issue when it comes to different capitalizations.
    while answ1.lower() != "paris":
        print("This is only the first round. Come on. I'll give you a chance.")
        answ1 = (input("Question 1: What is the capital of France? \n: "))
    print("Great job! I told you it was easy.")

    answ2 = (input("Question 2: What is the capital of the United Kingdom? \n: "))
    while answ2.lower() != "london":
        print("I hope you got your geography right. Here's another try.")
        answ2 = (input("Question 2: What is the capital of the United Kingdom? \n: "))
    print("You passed the second question! Great! \n Let's keep going, but this time it'll get harder.")

    answ3 = (input("Question 3: What is the capital of Italy? \n: "))
    while answ3.lower() != "rome":
        print("Come on! You must've heard or read this word before. Just think!")
        answ3 = (input("Question 3: What is the capital of Italy? \n: "))
    print("See? Question 3 is not that bad. \nAnyway, moving on.")

    answ4 = (input("Question 4: What is the capital of Russia \n: "))
    while answ4.lower() != "moscow":
        print("This is the same case as the Italy one. You just got to think harder")
        answ4 = (input("Question 4: What is the capital of Russia \n: "))
    print("Awesome! We're progressing through now.")

    answ5 = (input("Question 5: What is the capital of Monaco? \n: "))
    while answ5.lower() != "monaco":
        print("I'll give you a hint. (Though it gives away a lot) \n Capitals can have the same names as the country.")
        answ5 = (input("Question 5: What is the capital of Monaco? \n: "))
    print("5 Questions so far! You know your countries and capitals well.")

    #######
    #Transition
    #######

    print("Now we've done 5 questions so far. Every question seems to be easy.")
    choice2 = (input("Want to make it more fun and make it harder? \n-Yes   -No\n: "))
    attempts = []
    while choice2.lower() == "no":
        print("Aw come on! Don't be a wuss.")
        choice2 = (input("It's gonna be fun I promise. \n-Yes   -No\n: "))
        attempts.append(choice2)
        # Added an extra code for refusing the offer.
        if len(attempts) > 5:
            while True:
                print("Man, if you don't want to then, I guess you'll just have to suffer.")

    while choice2.lower() != "yes" and choice2.lower != "no":
        choice2 = (input("Want to make it more fun and make it harder? \n-Yes   -No\n: "))
        while choice2.lower() == "no":
            print("Aw come on! Don't be a wuss.")
            choice2 = (input("It's gonna be fun I promise. \n-Yes   -No\n: "))
            attempts.append(choice2)
            # Added an extra code for refusing the offer.
            if len(attempts) > 5:
                while True:
                    print("Man, if you don't want to then, I guess you'll just have to suffer.")

    print("Great! Let me explain the new conditions tho.")

    while choice2.lower() == "yes":
        # Time loop started.
        print("Everytime you fail, you will go back here.\nKind of like the Dormamu thing that Dr. Strange does.")
        print("Do your best to have a perfect score.")
        answ6 = (input("Question 6: What is the capital of Latvia? \n: "))
        if answ6.lower() == "riga":
            print("You survived the first round! Let's continue")

            answ7 = (input("Question 7: What is the capital of the Netherlands? \n: "))
            # Wrong answers will run the code continue skipping the if sequence and go back to the while loop.
            if answ7 != "amsterdam":
                print("Oh well. Rest in peac-")
                continue
            if answ7.lower() == "amsterdam":
                print("You got through! I underestimated you.")

                answ8 = (input("Question 8: What is the capital of Poland? \n: "))
                if answ8.lower() != "warsaw":
                    print("NOOOOOOOOOOOooOOOoooooo")
                    continue
                if answ8.lower() == "warsaw":
                    print("You're getting there! Very smart. \nLET'S SEE IF YOU CAN SURVIVE THESE!")

                    answ9 = (input("Question 9: What is the capital of Denmark? \n: "))
                    if answ9.lower() != "copenhagen":
                        print("HAHAHAHHAHAHA- BYE BYEEE-")
                        continue
                    if answ9.lower() == "copenhagen":
                        print("HOW ARE YOU THIS SMART..... \n I'LL MAKE THIS EXTRA HARDER!!!!")

                        answ10 = (input("Question 10: What is the capital of Andorra? \n: "))
                        print("YOU'D BE A FOOL TO FAIL ON THIS ONE!")
                        if answ10.lower() != "andorra la vella":
                            print("GOOD LUCK COMING BACK HER-")
                            continue
                        if answ10.lower() == "andorra la vella":
                            print("NO... HOW CAN THIS BE.\nYou're pretty good. I'll give you that.\nwell then, I guess this is goodbye.")

                            caught = []
                            print("But before you go. Here's one final question.")
                            answ11 = (input("Am I handsome? \n-??   -?? \n: "))
                        
                            
                            if answ11.lower() == "no":
                                    print("....")
                                    continue
                            
                            while answ11.lower() != "yes" and answ11.lower() != "no" :
                                answ11 = (input("Am I handsome? \n-??   -?? \n: "))
                            
                            # As for the answer yes, I changed the ending code to break to break the loop and end the cycle. 
                            if answ11.lower() == "yes":
                                print("AW. HOW CUTE.")
                                caught.append(answ11)
                                print(f"Now you caught in 4k. Check this out: \n############ \nAm I handsome? \n-??    -?? \n:{caught} \n################")
                                print("Look at that answer. Can't believe you like me like that fr.")
                                print("I'll treasure this answer forever from you muah.")
                                print("Anyways, thank you for playing with me. \nCome by anytime. It gets lonely here.\n I had a lot of fun.")
                                print("I guess I'll see you around.")
                                break
                            
print("Shutting down...")

