#Prepping the code to be read "&" manipulated:

with open ("Hotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")

#UNLINTED, UNVALIDATED Edit vendor

def editVendor(list):
    import math

    index = int(input("What would you like to edit?\n" \
    "1. Name\n" \
    "2. Date\n" \
    "3. # of Vegan Hotdogs\n" \
    "4. # of Meat Hotdogs\n" \
    "5. Weight of Onions (kg)\n" \
    "6. Volume of Ketchup (litres)\n"))


    if (index == 1):
        while True:
            newval = input("Enter name: ")
            if ((len(newval) <= 25) and (len(newval) >= 2)):
                print(f"Name valid: {newval}")
                break
            else:
                print("Vendor Name must be between 2 to 25 characters.")

        newval = newval.title()

    elif (index == 2):
        while True:                                                         #enter vendor's date
            v_year = int(input("Enter year: "))
            if ((v_year < 10000) and (v_year >= 1000)):
                v_week = int(input("Enter week: "))
                if((v_week >= 1) and (v_week <= 52)):
                    newval = str(v_year) + str(v_week).zfill(2)
                    print(f"Date valid: {newval}\n")
                    break
                else:
                    print("Week must be between 1 and 52")
            else:
                print("Year must be in YYYY format (e.g. 2026)")
        
    elif (index == 3):
        while True:                                                                     #enter number of vegan hotdogs supplied to vendor
            newval = float(input("Enter the # of Vegan Hotdogs supplied: "))
            if ((newval%10) == 0):
                print(f"# of Vegan Hotdogs valid: {newval}\n")
                break
            else:
                print("# of Vegan Hotdogs must be divisble by 10.")
    
    elif (index == 4):
        while True:                                                                     #enter number of meat hotdogs supplied to vendor
            newval = float(input("Enter the # of Meat Hotdogs supplied: "))
            if ((newval%10) == 0):
                print(f"# of Meat Hotdogs valid: {newval}\n")
                break
            else:
                print("# of Meat Hotdogs must be divisble by 10.")

    elif (index == 5):
        while True:                                                                                         #enter vendor's weight of onions ordered
            newval = float(input("Enter the weight of onions ordered (in kg): "))
            if (((newval - math.trunc(newval)) == 0.5) or ((newval - math.trunc(newval)) == 0)):
                print(f"Onions (kg) valid: {newval}\n")
                break
            else:
                print("The weight of onions must be in half kilogram increments (e.g. '0.5' or '0.0')")
    
    elif (index == 6):
        while True:                                                                                         #enter vendor's volume of ketchup ordered
            newval = int(input("Enter the volume of ketchup ordered (litres): "))
            if ((newval >= 1) and (newval <= 4)):
                print(f"Ketchup (litres) valid: {newval}\n")
                break
            else:
                print("Volume of ketchup ordered must be an integer (not a decimal number) between 1 and 4.")
    
    else:
        print("Selection must be an integer between 1 & 6 (inclusive)")
        editVendor(list)
    
    list.pop(index)
    list.insert(index, newval)

    print(f"Vendor post edit: {list} \n")

    repeat = input("Edit another value? Yes/No ")
    if (repeat == "Yes"):
        editVendor(list)
    elif (repeat == "No"):
        return(list)

editVendor(currenthv[1])