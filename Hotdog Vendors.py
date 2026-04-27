#Hotdog Vendors

#Prepping the code to be read "&" manipulated:

with open ("Testhotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")


#UNLINTED, UNVALIDATED Password Validation function
def passwordValidation():

    #potential users are...
    #* the CEO (middle access: able to view all users and all vendor data | can't view passwords nor change login data)
    #* IT Dept. (middle access: able to view users & passwords and change passwords | can't view vendor data)
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


#UNLINTED, UNVALIDATED Employee Menu function
def employeeMenu():
    choice = int(input("What would you like to do?: \n" \
    "1. View Vendors\n" \
    "2. Add Vendor\n" \
    "3. Search for a Vendor\n"
    "Input: "))

    if (choice == 1):
        displayVendors(currenthv)
    elif (choice == 2):
        addVendor()
    elif (choice == 3):
        searchVendor()
    else:
        print("Please enter an integer between 1 & 3 (inclusive).\n")
    
    repeat = input("Would you like to do anything else? Yes/No ")
    
    if (repeat == "Yes"):
        employeeMenu()
    elif(repeat == "No"):
        exit
    else:
        print("Please input 'Yes' or 'No'.\n")



#UNLINTED, UNVALIDATED Display Vendors function

def displayVendors(array):
    title = "{:<20} {:^25} {:>20}       {:>20} {:>20} {:^15} {:^15}"        #formats the titles (clarifying what each value in the file is)
    values = "{:<20} {:^25}{:>20}       {:^20} {:^20} {:^15} {:^15}"        #formats the values within the file

    print(title.format("Vendor ID", "Vendor Name", "Year and Week", "# of Vegan Hotdogs", "# of Meat Hotdogs", "Onions (kg)", "Ketchup (litres)"), f"\n{"-"*139}")

    for i in array:
        if (type(i) == str):
            i = i.split(",")

        print(values.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    
    sort = input("Sort vendors? Yes/No ")

    if (sort == "Yes"):
        displayVendors(sortVendors(currenthv))
    else:
        return



#UNLINTED, UNVALIDATED Add Vendor "&" Generate Vendor ID function
#v_ means vendor

#---Generate Vendor ID
import random
def generateVendorID(name):
    ID = ""
    for i in range(0,len(name) - 1):
        if ((name[i]).isupper()):
            ID += name[i]
    
    if (len(ID) > 2):
        ID = ID[:2]
    elif (len(ID) == 1):
        ID = ID + "V"       #V for vendor
    
    differentiator = str(random.randrange(1,1000)).zfill(3)

    ID = ID + "_" + differentiator
    print(f"ID Generated: {ID}\n")
    return (ID)

#---Add Vendor
import math
def addVendor():
    while True:                                                         #enter vendor name
        v_name = input("Enter name: ")
        if ((len(v_name) <= 25) and (len(v_name) >= 2)):
            print(f"Name valid: {v_name}")
            break
        else:
            print("Vendor Name must be between 2 to 25 characters.")

    v_name = v_name.title()

    v_ID = generateVendorID(v_name)                                            #generates vendor ID based off name

    while True:                                                         #enter vendor's date
        v_year = int(input("Enter year: "))
        if ((v_year < 10000) and (v_year >= 1000)):
            v_week = int(input("Enter week: "))
            if((v_week >= 1) and (v_week <= 52)):
                v_date = str(v_year) + str(v_week).zfill(2)
                print(f"Date valid: {v_date}\n")
                break
            else:
                print("Week must be between 1 and 52")
        else:
            print("Year must be in YYYY format (e.g. 2026)")



    while True:                                                                     #enter number of vegan hotdogs supplied to vendor
        v_vhotdogs = float(input("Enter the # of Vegan Hotdogs supplied: "))
        if ((v_vhotdogs%10) == 0):
            print(f"# of Vegan Hotdogs valid: {v_vhotdogs}\n")
            break
        else:
            print("# of Vegan Hotdogs must be divisble by 10.")

    while True:                                                                     #enter number of meat hotdogs supplied to vendor
        v_mhotdogs = float(input("Enter the # of Meat Hotdogs supplied: "))
        if ((v_mhotdogs%10) == 0):
            print(f"# of Meat Hotdogs valid: {v_mhotdogs}\n")
            break
        else:
            print("# of Meat Hotdogs must be divisble by 10.")



    while True:                                                                                         #enter vendor's weight of onions ordered
        v_onions = float(input("Enter the weight of onions ordered (in kg): "))
        if (((v_onions - math.trunc(v_onions)) == 0.5) or ((v_onions - math.trunc(v_onions)) == 0)):
            print(f"Onions (kg) valid: {v_onions}\n")
            break
        else:
            print("The weight of onions must be in half kilogram increments (e.g. '0.5' or '0.0')")

    while True:                                                                                         #enter vendor's volume of ketchup ordered
        v_ketchup = int(input("Enter the volume of ketchup ordered (litres): "))
        if ((v_ketchup >= 1) and (v_ketchup <= 4)):
            print(f"Ketchup (litres) valid: {v_ketchup}\n")
            break
        else:
            print("Volume of ketchup ordered must be an integer (not a decimal number) between 1 and 4.")

    newVendor = [v_ID, v_name, v_date, str(v_vhotdogs), str(v_mhotdogs), str(v_onions), str(v_ketchup)]

    print(f"Final Current Vendor information: {newVendor}.\n")

    while True:
        shouldEdit = input("Would you like to edit any of your vendor information? (Yes/No): ")
        shouldEdit = shouldEdit.title()
        if ((shouldEdit != "Yes") and (shouldEdit != "No")):
            print("Answer must be Yes or No.\n")
        else:
            break
    
    if (shouldEdit == "Yes"):
        #would have "editVendorFunction(newVendor)" - the line below is a placeholder
        print("Editing. . .")
    else:
        currenthv.append(newVendor)


#UNLINTED, UNVALIDATED Search Vendor function

def searchVendor():
    targetname = input("Input vendor's name: ")
    targetdate = input(f"Input the date you wish to view for {targetname}: ")
    target = [targetname, targetdate]
    print(target)

    def quickSortByDate(array):
        if (len(array) <= 1):
            return(array)
        else:
            pivot = array.pop()

        greater = []
        less = []

        for i in array:
            if (i[2] > pivot[2]):
                greater.append(i)
            else:
                less.append(i)
        
        combined = quickSortByDate(less) + [pivot] + quickSortByDate(greater)

        return(combined)
    
    def binarySearch(array, target):
        if (len(array)> 2):
            midpoint = array[round((len(array) - 1)//2)]

            midpoint_nd = [midpoint[1], midpoint[2]]        #nd means name date (so: midpoint_namedate)
            print(midpoint, "\n", midpoint_nd)

            if (midpoint_nd == target):
                print(f"we found it: {midpoint}")
                return(midpoint)
            else:
                if (midpoint[1] != target[0]):
                    if (midpoint[1] < target[0]):
                        print("looking at upper half...")
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(0)
                        findings = binarySearch(newarray,target)
                        return(findings)

                    else:
                        print("looking at lower half...")
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
            	            newarray.pop(len(newarray) - 1)
                        findings = binarySearch(newarray,target)
                        return(findings)

                elif (midpoint[1] == target[0]):
                    if (midpoint[2] < target[1]):
                        print("looking at upper half...")
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(0)
                        findings = binarySearch(newarray,target)
                        return(findings)

                    else:
                        print("looking at lower half...")
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
            	            newarray.pop(len(newarray) - 1)
                        findings = binarySearch(newarray,target)
                        return(findings)
        else:
            midpoint = array[0]
            midpoint_nd = [midpoint[1], midpoint[2]]        #nd means name date (so: midpoint_namedate)

            if (midpoint_nd == target):
                print(f"we found it: {midpoint}")
                return(midpoint)

            elif (midpoint_nd != target):
                return(midpoint)

    array = quickSortByDate(currenthv)
    print(array)

    findings = binarySearch(array, target)
    print(findings)
    findings_nd = [findings[1], findings[2]]

    if (findings_nd != target):
        print("target not found. sorry!")

#UNLINTED, UNVALIDATED Quick Sort function
def sortVendors(array):
    while True:
        index = int(input("Would you like to sort by...\n" \
            "1. Name\n" \
            "2. Date\n"))

        if ((index != 1) and (index != 2)):
            print("Please enter the integer 1 or 2.\n")
        else:
            break

    def quickSort(array):
        if (len(array) <= 1):
            return(array)
        else:
            pivot = array.pop()

        greater = []
        less = []

        for i in array:
            if (i[index] > pivot[index]):
                greater.append(i)
            else:
                less.append(i)
        
        combined = quickSort(less) + [pivot] + quickSort(greater)

        return(combined)
    
    return(quickSort(array))


user = passwordValidation()

if ((user == "WDC_employee1") or (user == "WDC_employee2")):
    employeeMenu()