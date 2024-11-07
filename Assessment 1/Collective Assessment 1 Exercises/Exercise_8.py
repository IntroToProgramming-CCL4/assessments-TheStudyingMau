# Exercise 8: Simple Search - 30 Marks

print("Welcome to the search system.\nI see you have lost someone and would like to find out if they're here. \nFear not, the system will find it for you. ")
while True:
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    search = (input("Search: "))

    # Used ".title()" as it only capitalizes the first letter which makes the input and the list compatible when compared.
    
    search = search.title()

    # Using "in" and "not in" operators is more functional than the "for" loop because the "for" loop goes
    # through the list one at a time. This will cause an error if I asked if "jake" is there when I just finished asking about "Sam"
    # because the code cannot find jake after sam unless the list resets. Therefore using the "in" and "not in" operators were more effective.
    
    if search.lower() == "exit":
        print("Shutting down..")
        break
    if search in names:
            print(f"{search} is found.")
            continue
    if search not in names:
            print("The following input is not found in the list. Please try again.")
            continue
    