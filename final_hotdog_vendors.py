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

password_validation()
