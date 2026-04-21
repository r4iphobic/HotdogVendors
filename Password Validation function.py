#Password Validation function


def passwordValidation():
    #potential users are...
    #* the CEO (middle access: able to view all users and all vendor data | can't view passwords nor change login data)
    #* IT Dept. (middle access: able to view users & passwords, add users, change passwords | can't view vendor data)
    #* Employee (no access: can't view anything | can view vendor data)

    users = {
        "WDC_ceo" : "password1",
        "WDC_IT" : "password2",
        "WDC_employee1" : "password3",
        "WDC_employee2" : "password4"
    }

    def passwordInput():
            password = input("Enter password: ")
            if (password == users[username] ):
                print(f"Welcome {username}. \n")
            else:
                while True:
                    print("Invalid password. \n" \
                    "Input... \n" \
                    "0 to try again\n" \
                    "1 to enter a different username")
                    choice = int(input(""))
                    if (choice == 0):
                        passwordInput()
                        break
                    elif (choice == 1):
                        passwordValidation()
                        break
                    else:
                        print("Please input 0 or 1. \n")

    while True:
        username = input("Enter username: ")
        if (username in users):
            break
        else:
            print("Invalid username. \n")
    
    passwordInput()

    return(username)

passwordValidation()