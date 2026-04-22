#Prepping the code to be read "&" manipulated:

with open ("Hotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")

#Add Vendor "&" Generate Vendor ID function
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

addVendor()
