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
    print(f"ID Generated: {ID}")

#---Add Vendor

while True:                                                         #enter vendor name
    v_name = input("")
    if ((len(v_name) <= 25) and (len(v_name) >= 2)):
        print(f"Name valid: {v_name}")
        break
    else:
        print("Vendor Name must be between 2 to 25 characters.")

v_name = v_name.title()

generateVendorID(v_name)

while True:                                                         #enter vendor's date
    v_year = int(input("Enter year: "))
    if ((v_year < 10000) and (v_year >= 1000)):
        v_week = int(input("Enter week: "))
        if((v_week >= 1) and (v_week <= 52)):
            v_date = str(v_year) + str(v_week).zfill(2)
            print(f"Date valid: {v_date}")
            break
        else:
            print("Week must be between 1 and 52")
    else:
        print("Year must be in YYYY format (e.g. 2026)")

