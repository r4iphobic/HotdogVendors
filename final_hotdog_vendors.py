"""Final Version of Hotdog Vendors Program"""

#Prepping the code to be read "&" manipulated:
try:
    with open ("Testhotdogs.txt", "r+", encoding="utf-8") as data:
        #opens file to read and write (also automatically closes)
        currenthv =[]
        currenthv = data.read().split("\n")       #splits the text file into a list by each new line

    for i in range(0,(len(currenthv) -1) ):
        #splits the text file into smaller lists by each ','
        currenthv[i] = currenthv[i].split(",")

except FileNotFoundError:
    print("File with vendor data has not been found.\n" \
    "Please download 'Hotdogs.txt' or rename your file with the vendor data 'Hotdogs.txt'")

#Password Validation function
def password_validation():
    """Password Validator Function (returns username)"""

    users = {
        "WDC_ceo" : "password1",
        "WDC_IT" : "password2",
        "WDC_employee1" : "password3",
        "WDC_employee2" : "password4"
    }

    def password_input():
        password = input("Enter password: ")
        if password == users[username]:
            print(f"Welcome {username}. \n")
        else:
            while True:
                try:
                    print("Invalid password. \n" \
                    "Input... \n" \
                    "0 to try again\n" \
                    "1 to enter a different username")
                    choice = int(input(""))
                    if choice == 0:
                        password_input()
                        break
                    elif choice == 1:
                        password_validation()
                        break
                    else:
                        print("Please input 0 or 1. \n")
                except ValueError:
                    print("Please input 0 or 1. \n")

    while True:
        username = input("Enter username: ")
        if username in users:
            break
        else:
            print("Invalid username. \n")

    password_input()

    return username

#Employee Menu function
def employeeMenu():
    """Employee Menu
    Allows users to...
    * View vendors
    * Add new vendors
    * Search for vendors"""

    while True:
        try:
            choice = int(input("What would you like to do?: \n" \
            "1. View Vendors\n" \
            "2. Add Vendor\n" \
            "3. Search for a Vendor\n"
            "Input: "))
        except ValueError:
            print("Please enter an integer between 1 & 3 (inclusive).\n")


        if (choice == 1):
            displayVendors(currenthv)
            break
        elif (choice == 2):
            addVendor()
            break
        elif (choice == 3):
            searchVendor()
            break
        else:
            print("Please enter an integer between 1 & 3 (inclusive).\n")
    
    while True:
        repeat = input("Would you like to do anything else? Yes/No ")
    
        if (repeat == "Yes"):
            employeeMenu()
            break
        elif(repeat == "No"):
            break
        else:
            print("Please input 'Yes' or 'No'.\n")

#UNLINTED Display Vendors function

def displayVendors(array):
    """displays multiple vendors (and asks to sort them)"""

    #formats the titles (clarifying what each value in the file is)
    title = "{:<20} {:^25} {:>20}       {:>20} {:>20} {:^15} {:^15}"

    #formats the values within the file
    values = "{:<20} {:^25}{:>20}       {:^20} {:^20} {:^15} {:^15}"

    print(title.format("Vendor ID", "Vendor Name", "Year and Week", "# of Vegan Hotdogs", "# of Meat Hotdogs", "Onions (kg)", "Ketchup (litres)"), f"\n{"-"*139}")

    for i in array:
        if (type(i) == str):
            i = i.split(",")

        print(values.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    
    while True:
        sort = input("Sort vendors? Yes/No ")

        if (sort == "Yes"):
            displayVendors(sortVendors(currenthv))
            break
        elif (sort == "No"):
            break
        else:
            print("Please input 'Yes' or 'No' (character sensitive)\n")
