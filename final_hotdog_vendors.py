"""Final Version of Hotdog Vendors Program"""
import math
import random
import time

#Prepping the code to be read "&" manipulated:
try:
    with open ("Hotdogs.txt", "r+", encoding="utf-8") as data:
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

#Employee Menu procedure
def employee_menu():
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
            "3. Search for a Vendor\n"\
            "4. Exit\n"
            "Input choice: "))
        except ValueError:
            print("Please enter an integer between 1 & 4 (inclusive).\n")

        else:
            if choice == 1:
                display_vendors(currenthv)
                while True:
                    sort = (input("Sort vendors? Yes/No ")).title()
                    if sort == "Yes":
                        display_vendors(sort_vendors(currenthv))
                        break
                    elif sort == "No":
                        break
                    else:
                        print("Please input 'Yes' or 'No' (character sensitive)\n")
                break

            elif choice == 2:
                add_vendor()
                break

            elif choice == 3:

                vendor = search_vendor()

                if vendor:
                    while True:
                        should_edit = (input("Would you like to edit any of the \
                        vendor information? (Yes/No): ")).title()
                        if ((should_edit != "Yes") and (should_edit != "No")):
                            print("Answer must be Yes or No.\n")
                        else:
                            break
                
                        if should_edit == "Yes":
                            edit_vendor(vendor)
                            break
            
            elif choice == 4:
                break

            else:
                print("Please enter an integer between 1 & 4 (inclusive).\n")

    while True:
        repeat = (input("Would you like to do anything else? Yes/No ")).title()

        if repeat == "Yes":
            employee_menu()
            break
        elif repeat == "No":
            break
        else:
            print("Please input 'Yes' or 'No'.\n")

#IT Menu procedure

def it_menu():
    """IT Menu
    Allows users to...
    * View efficiency of sorters and searchers"""

    while True:
        try:
            choice = int(input("What would you like to do?: \n" \
            "1. Calculate efficiency\n" \
            "2. Exit\n" \
            "Input: "))

        except ValueError:
            print("Please enter either 1 or 2 (integers).\n")
        
        else:
            if choice == 1:
                efficiency_calculator()
            elif choice == 2:
                break
            else:
                print("Please enter either 1 or 2 (integers).")

#Display Vendor(s) procedures

def display_vendors(array):
    """displays multiple vendors (and asks to sort them)"""

    #formats the titles (clarifying what each value in the file is)
    title = "{:<20} {:^25} {:>20}       {:>20} {:>20} {:^15} {:^15}"

    #formats the values within the file
    values = "{:<20} {:^25}{:>20}       {:^20} {:^20} {:^15} {:^15}"

    print(title.format("Vendor ID", "Vendor Name", "Year and Week",
    "# of Vegan Hotdogs", "# of Meat Hotdogs", "Onions (kg)", "Ketchup (litres)"), f"\n{"-"*139}")

    for sublist in array:
        if isinstance(sublist, str):
            sublist = sublist.split(",")

        print(values.format(sublist[0],sublist[1],sublist[2],sublist[3],
        sublist[4],sublist[5],sublist[6]))

def display_single_vendor(array):
    """displays one vendor (therefore doesn't ask to sort)"""

    #formats the titles (clarifying what each value in the file is)
    title = "{:<20} {:^25} {:>20}       {:>20} {:>20} {:^15} {:^15}"

    #formats the values within the file
    values = "{:<20} {:^25}{:>20}       {:^20} {:^20} {:^15} {:^15}"

    print(title.format("Vendor ID", "Vendor Name", "Year and Week",
    "# of Vegan Hotdogs", "# of Meat Hotdogs", "Onions (kg)", "Ketchup (litres)"), f"\n{"-"*149}")

    print(values.format(array[0],array[1],array[2],array[3],array[4],array[5],array[6]))

#Display Analysis procedure

def display_analysis():
    """Generates and displays analysis about vendors
    Includes...
    * Most productive vendor
    * No. of vegan hotdogs vs meat hotdogs supplied
    * Vendor using the most onions
    * Vendor using the most ketchup
    * Vendor using the most vegan hotdogs
    * Vendor using the most meat hotdogs"""

    #enter today's date
    while True:
        try:
            while True:
                #enter today's date
                year = int(input("Enter the current year: "))
                if ((year < 10000) and (year >= 1000)):
                    week = int(input("Enter the current week: "))

                    if((week >= 1) and (week <= 52)):
                        #todays date in YYYYMM format
                        date = str(year) + str(week).zfill(2)
                        print(f"Date valid: {date}\n")
                        break
                    else:
                        print("Week must be between 1 and 52")

                else:
                    print("Year must be in YYYY format (e.g. 2026)")
            break
        except ValueError:
            print("Please enter ineger values only (e.g. 2000 or 7)\n")

    analysis = ""
    array = []

    while True:
        try:
            vendor_choice = int(input("Analyse...\n" \
            "1. All Vendors\n" \
            "2. One Vendor\n" \
            "Input: "))
        except ValueError:
            print("Please enter either 1 or 2 (integers).\n")

        else:
            if vendor_choice == 1:
                array = currenthv
                break
            elif vendor_choice == 2:
                while True:
                    v_name = input("Input vendor name: ")

                    #look for inputted name
                    for h, sublist in enumerate(currenthv - 1):
                        if isinstance(sublist, str):
                            sublist = sublist.split(",")

                        if sublist[1] == v_name:
                            array.append(sublist)

                    if array:
                        break
                    else:
                        print("Vendor not found.\n")
                break
            else:
                print("Please enter either 1 or 2 (integers).\n")

    def superlative_finder(index):
        superlative = array[0]
        superlative_nd = []
        superlative = float(superlative[index])

        for sublist in array:
            if isinstance(sublist, str):
                sublist = sublist.split(",")

            currentval = float(sublist[index])

            if currentval > superlative:
                superlative_nd = f"{sublist[1]} during {sublist[2]}"
                superlative = currentval
            elif currentval == superlative:
                superlative_nd += f" and {sublist[1]} during {sublist[2]}"
                superlative = currentval

        return superlative_nd

    #Most Productive Vendor
    superlative = []
    superlative = array[0]
    superlative_nd = []

    superlative = float(superlative[3]) + float(superlative[4]) \
        + float(superlative[5]) + float(superlative[6])

    for sublist in array:
        if isinstance(sublist, str):
            sublist = sublist.split(",")

        currentval = float(sublist[3]) + float(sublist[4]) + float(sublist[5]) + float(sublist[6])

        if currentval > superlative:
            superlative_nd = f"{sublist[1]} during {sublist[2]}"
            superlative = currentval
        elif currentval == superlative:
            superlative_nd += f" and {sublist[1]} during {sublist[2]}"
            superlative = currentval

    analysis += f"The vendor(s) that was/were the most productive is/are {superlative_nd} \n \n"

    #Number of vegan hotdogs versus meat hotdogs supplied
    vegan_hotdog_count = 0
    meat_hotdog_count = 0

    for sublist in array:
        if isinstance(sublist, str):
            sublist = sublist.split(",")

        vegan_hotdog_count += float(sublist[3])
        meat_hotdog_count += float(sublist[4])

    if vegan_hotdog_count > meat_hotdog_count:
        hotdog_evaluation = f"Overall, there were {vegan_hotdog_count-meat_hotdog_count} \
        more vegan hotdogs supplied than meat hotdogs."

    elif vegan_hotdog_count == meat_hotdog_count:
        hotdog_evaluation = f"Overall, there has been an equal amount of vegan and meat \
        hotdogs supplied ({vegan_hotdog_count})"

    else:
        hotdog_evaluation = f"Overall, there were {meat_hotdog_count-vegan_hotdog_count} \
        more meat hotdogs supplied than vegan hotdogs."

    analysis += f"{hotdog_evaluation} \n \n"

    #Vendor using the most amount of ketchup

    ketchup = 0

    for sublist in array:
        if isinstance(sublist, str):
            sublist = sublist.split(",")

        ketchup += int(sublist[6])

    analysis += f"Total ketchup supplied as of {date} is {ketchup} litres. \n \n"

    #Vendor that has ordered the most amount of onions
    analysis += f"The vendor(s) that ordered the most onions was/were {superlative_finder(6)} \n \n"

    #Vendor that ordered the most vegan hotdogs
    analysis += f"The vendor(s) that ordered the most vegan hotdogs was/were \
    {superlative_finder(3)} \n \n"

    #Vendor that ordered that most meat hotdogs
    analysis += f"The vendor(s) that ordered the most meat hotdogs was/were \
    {superlative_finder(4)} \n \n"

    print(f"\nAnalysis... \n{("-"*11)} \n{analysis}")

    if vendor_choice == 1:
        with open (f"Analysis on {date}", "a+", encoding="utf-8") as file:
            file.write(analysis)
    elif vendor_choice == 2:
        with open (f"{v_name} Analysis on {date}", "a+", encoding="utf-8") as file:
            file.write(analysis)

#Add Vendor "&" Generate Vendor ID procedures

#---Generate Vendor ID
def generate_vendor_id(name):
    """Generates vendor ID for added vendor."""

    v_id = ""
    for letter in range(0,len(name) - 1):
        if (name[letter]).isupper():
            v_id += name[letter]

    if len(v_id) > 2:
        v_id = v_id[:2]
    elif len(v_id) == 1:
        v_id = v_id + "V"       #V for vendor

    differentiator = str(random.randrange(1,1000)).zfill(3)

    v_id = v_id + "_" + differentiator
    print(f"ID Generated: {v_id}\n")
    return v_id

#---Add Vendor
def add_vendor():
    """Allows user to add a vendor.
    Requires...
    * Vendor name
    * Vendor date (year and week)
    * # of vegan hotdogs
    * # of meat hotdogs
    * Weight of onions (kg)
    * Volume of ketchup (litres)"""

    while True:                                                         #enter vendor name
        v_name = input("Enter name: ")
        if ((len(v_name) <= 25) and (len(v_name) >= 2)):
            print(f"Name valid: {v_name}")
            break
        else:
            print("Vendor Name must be between 2 to 25 characters.")

    v_name = v_name.title()

    v_id = generate_vendor_id(v_name)           #generates vendor ID based off name

    while True:
        try:
            while True:
                #enter vendor's date
                v_year = int(input("Enter year: "))
                if ((v_year < 10000) and (v_year >= 1000)):
                    v_week = int(input("Enter week: "))
                    if((v_week >= 1) and (v_week <= 52)):
                        v_date = str(v_year) + str(v_week).zfill(2)
                        print(f"Date valid: {v_date}\n")
                        break
                    else:
                        print("Week must be between 1 and 52\n")
                else:
                    print("Year must be in YYYY format (e.g. 2026)\n")
            break
        except ValueError:
            print("Please enter integer values only (e.g. 2000 or 7)\n")



    while True:
        #enter number of vegan hotdogs supplied to vendor
        while True:
            try:
                v_vhotdogs = float(input("Enter the # of Vegan Hotdogs supplied: "))
            except ValueError:
                print("Please enter a number (float or integer).\n")
            else:
                break

        if (v_vhotdogs%10) == 0:
            print(f"# of Vegan Hotdogs valid: {v_vhotdogs}\n")
            break
        else:
            print("# of Vegan Hotdogs must be divisble by 10 (a.k.a. a whole number).\n")

    while True:
        #enter number of meat hotdogs supplied to vendor
        while True:
            try:
                v_mhotdogs = float(input("Enter the # of Meat Hotdogs supplied: "))
            except ValueError:
                print("Please enter a number (float or integer).\n")
            else:
                break

        if (v_mhotdogs%10) == 0:
            print(f"# of Meat Hotdogs valid: {v_mhotdogs}\n")
            break
        else:
            print("# of Meat Hotdogs must be divisble by 10.")



    while True:
        #enter vendor's weight of onions ordered
        while True:
            try:
                v_onions = float(input("Enter the weight of onions ordered (in kg): "))
            except ValueError:
                print("Please enter a number (float or integer).\n")
            else:
                break

        if (((v_onions - math.trunc(v_onions)) == 0.5) or ((v_onions - math.trunc(v_onions)) == 0)):
            print(f"Onions (kg) valid: {v_onions}\n")
            break
        else:
            print("The weight of onions must be in half kilogram increments (e.g. '0.5' or '0.0')")

    while True:
        #enter vendor's volume of ketchup ordered
        while True:
            try:
                v_ketchup = int(input("Enter the volume of ketchup ordered (litres): "))
            except ValueError:
                print("Please enter integer values only (e.g. 2000 or 7)\n")
            else:
                break

        if ((v_ketchup >= 1) and (v_ketchup <= 4)):
            print(f"Ketchup (litres) valid: {v_ketchup}\n")
            break
        else:
            print("Volume of ketchup ordered must be an integer (not a decimal number)\
            between 1 and 4.")

    new_vendor = [v_id, v_name, v_date, str(v_vhotdogs), str(v_mhotdogs), \
        str(v_onions), str(v_ketchup)]

    print(f"Final Current Vendor information: {new_vendor}.\n")

    while True:
        should_edit = (input("Would you like to edit any of the vendor information? \
        (Yes/No): ")).title()
        if ((should_edit != "Yes") and (should_edit != "No")):
            print("Answer must be Yes or No.\n")
        else:
            break

    if should_edit == "Yes":
        edit_vendor(new_vendor)
    else:
        currenthv.append(new_vendor)

#Edit vendor function

def edit_vendor(array):
    """Edits given array, a.k.a. vendor"""
    try:
        while True:
            index = int(input("What would you like to edit?\n" \
            "1. Name\n" \
            "2. Date\n" \
            "3. # of Vegan Hotdogs\n" \
            "4. # of Meat Hotdogs\n" \
            "5. Weight of Onions (kg)\n" \
            "6. Volume of Ketchup (litres)\n"))

            if index >= 1 or index <= 6:
                break
            else:
                print("Please input an integer between 1 & 6 (inclusive)")
    except ValueError:
        print("Please input an integer between 1 & 6 (inclusive)")


    if index == 1:
        while True:
            newval = input("Enter name: ")
            if ((len(newval) <= 25) and (len(newval) >= 2)):
                print(f"Name valid: {newval}")
                break
            else:
                print("Vendor Name must be between 2 to 25 characters.")

        newval = newval.title()

    elif index == 2:
        while True:
            try:
                while True:
                    #enter vendor's date
                    v_year = int(input("Enter year: "))
                    if ((v_year < 10000) and (v_year >= 1000)):
                        v_week = int(input("Enter week: "))
                        if((v_week >= 1) and (v_week <= 52)):
                            newval = str(v_year) + str(v_week).zfill(2)
                            print(f"Date valid: {newval}\n")
                            break
                        else:
                            print("Week must be between 1 and 52\n")
                    else:
                        print("Year must be in YYYY format (e.g. 2026)\n")
                break
            except ValueError:
                print("Please enter integer values only (e.g. 2000 or 7)\n")

    elif index == 3:
        while True:
            #enter number of vegan hotdogs supplied to vendor
            while True:
                try:
                    newval = float(input("Enter the # of Vegan Hotdogs supplied: "))
                except ValueError:
                    print("Please enter a number (float or integer).\n")
                else:
                    break

            if (newval%10) == 0:
                print(f"# of Vegan Hotdogs valid: {newval}\n")
                break
            else:
                print("# of Vegan Hotdogs must be divisble by 10 (a.k.a. a whole number).\n")

    elif index == 4:
        while True:
            #enter number of meat hotdogs supplied to vendor
            while True:
                try:
                    newval = float(input("Enter the # of Meat Hotdogs supplied: "))
                except ValueError:
                    print("Please enter a number (float or integer).\n")
                else:
                    break

            if (newval%10) == 0:
                print(f"# of Meat Hotdogs valid: {newval}\n")
                break
            else:
                print("# of Meat Hotdogs must be divisble by 10.")

    elif index == 5:
        while True:
            #enter vendor's weight of onions ordered
            while True:
                try:
                    newval = float(input("Enter the weight of onions ordered (in kg): "))
                except ValueError:
                    print("Please enter a number (float or integer).\n")
                else:
                    break

            if (((newval - math.trunc(newval)) == 0.5) or ((newval - math.trunc(newval)) == 0)):
                print(f"Onions (kg) valid: {newval}\n")
                break
            else:
                print("The weight of onions must be in half kilogram increments \
                (e.g. '0.5' or '0.0')")

    elif index == 6:
        while True:
            #enter vendor's volume of ketchup ordered
            while True:
                try:
                    v_ketchup = int(input("Enter the volume of ketchup ordered (litres): "))
                except ValueError:
                    print("Please enter integer values only (e.g. 2000 or 7)\n")
                else:
                    break

            if ((v_ketchup >= 1) and (v_ketchup <= 4)):
                print(f"Ketchup (litres) valid: {v_ketchup}\n")
                break
            else:
                print("Volume of ketchup ordered must be an integer (not a decimal number)\
                between 1 and 4.")

    else:
        print("Selection must be an integer between 1 & 6 (inclusive)")
        edit_vendor(array)

    array.pop(index)
    array.insert(index, newval)

    print(f"Vendor post edit: {array} \n")

    while True:
        repeat = (input("Edit another value? Yes/No ")).title()
        if repeat == "Yes":
            edit_vendor(array)
            break
        elif repeat == "No":
            return array
        else:
            print("Please enter 'Yes' or 'No'.\n")

#Search Vendor function

def search_vendor():
    """Searches for vendor that user inputs the name of"""

    targetname = input("Input vendor's name: ")

    while True:
        try:
            targetdate = int(input(f"Input the date you wish to view for {targetname}: "))
        except ValueError:
            print("Please enter integers. (YYYYWW format, e.g. 202618)")
        else:
            break

    target = [targetname, str(targetdate)]

    def quick_sort_by_name(array):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()

        greater = []
        less = []

        for i in array:
            if i[1] > pivot[1]:
                greater.append(i)
            else:
                less.append(i)

        combined = quick_sort_by_name(less) + [pivot] + quick_sort_by_name(greater)

        return combined

    def binary_search(array, target):
        if len(array) > 2:
            midpoint = array[round((len(array) - 1)//2)]

            midpoint_nd = [midpoint[1], midpoint[2]]
            #nd means name date (so: midpoint_namedate)

            if midpoint_nd == target:                     #if found
                return midpoint
            else:
                if midpoint[1] != target[0]:
                    if midpoint[1] < target[0]:
                        #looks @ upper half if the names of the target
                        # & current sublist looked at aren't the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(0)
                        findings = binary_search(newarray,target)
                        return findings

                    else:
                        #looks @ lower half if the names of the target
                        # & current sublist looked at aren't the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(len(newarray) - 1)
                        findings = binary_search(newarray,target)
                        return findings

                elif midpoint[1] == target[0]:
                    if midpoint[2] < target[1]:
                        #looks @ upper half if the names of the target
                        # & current sublist looked at are the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(0)
                        findings = binary_search(newarray,target)
                        return findings

                    else:
                        #looks @ lower half if the names of the target
                        # & current sublist looked at are the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(len(newarray) - 1)
                        findings = binary_search(newarray,target)
                        return findings
        else:
            midpoint = array[0]
            midpoint_nd = [midpoint[1], midpoint[2]]
            #nd means name date (so: midpoint_namedate)

            if midpoint_nd == target:                     #if found
                return midpoint

            elif midpoint_nd != target:                   #if not found
                return midpoint

    array = quick_sort_by_name(currenthv)

    findings = binary_search(array, target)
    findings_nd = [findings[1], findings[2]]


    if findings_nd != target:
        print("Target not found.")
    else:
        print("Target found:\n")
        display_single_vendor(findings)
        return findings

#Quick Sort function
def sort_vendors(array):
    """Sorts the vendors by name or date"""

    while True:
        try:
            index = int(input("Would you like to sort by...\n" \
                "1. Name\n" \
                "2. Date\n"))

            if ((index != 1) and (index != 2)):
                print("Please enter the integer 1 or 2.\n")
            else:
                break
        except ValueError:
            print("Please enter the integer 1 or 2.\n")

    return quick_sort(array, index)

def quick_sort(array, index):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()

    greater = []
    less = []

    for i in array:
        if isinstance(i, str):
            i = i.split(",")

        if i[index] > pivot[index]:
            greater.append(i)
        else:
            less.append(i)

    combined = quick_sort(less,index) + [pivot] + quick_sort(greater,index)

    return combined

#Efficiency calculator procedure

def efficiency_calculator():
    """Calculates and displays the efficiency of each search and sort
    Then outputs the sort and search used, and why.

    Sorts tested:
    * Bubble Sort
    * Quick Sort

    Searches tested:
    * Linear search
    * Binary search"""

    #Bubble Sort
    swap = True

    bubble_start = time.time() #takes total time the code has been running

    while (swap == True):
        swap = False                              #to stop the loop
        for i in range(0, (len(currenthv) - 1)):
            if ((currenthv[i][1]) > (currenthv[i+1][1])):
                #compares the values (names) in each sublist, 
                #swaps if left value is bigger than right value

                a = currenthv[i]
                currenthv.remove(currenthv[i])
                currenthv.insert(i+1,a)
                swap = True                       #to start it again if a swap has been made

    bubble_end = time.time()

    bubble_time = bubble_end - bubble_start #calculates total time for bubble sort to run

    #Quick Sort

    quick_start = time.time()
    quick_sort(currenthv,1)
    quick_end = time.time()

    quick_time = quick_end - quick_start #calculates total time for quick sort to run

    print(f"The quick sort took {round(quick_time,7)} seconds to complete.")
    print(f"The bubble sort took {round(bubble_time,7)} seconds to complete.\n")

    #Comparing efficiency of sorters:

    if quick_time > bubble_time:
        print(f"Bubble sort is faster than quick sort by {round(quick_time-bubble_time, 10)} seconds.\n")

    elif bubble_time > quick_time:
        print(f"Quick sort is faster than bubble sort by {round(bubble_time-quick_time, 10)} seconds.\n")

    else:
        print("The quick sort and bubble sort currently take the same amount of time to run.\n"\
        "If this keeps happening, please change the size of the list in 'Hotdogs.txt' to see a difference.\n")

    #Sorted linear search when value is found
    target = "Dolly Dogs"
    findings = []
    found = False
    
    valid_linear_start = time.time()

    for i in range(0, len(currenthv) - 1):
        if (currenthv[i][1] == target):
            findings.append(currenthv[i])
            found = True
        
    if (found == True):
        targetdate = 202315
        found = False
        for i in range(0, len(findings) - 1):
            if (int(findings[i][2]) == targetdate):
                found = True

    valid_linear_end = time.time()

    valid_linear_time = valid_linear_end - valid_linear_start


    #Binary search when value is found
    
    valid_binary_start = time.time()

    target = ["Dolly Dogs", str(202315)]

    def quick_sort_by_name(array):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()

        greater = []
        less = []

        for i in array:
            if i[1] > pivot[1]:
                greater.append(i)
            else:
                less.append(i)

        combined = quick_sort_by_name(less) + [pivot] + quick_sort_by_name(greater)

        return combined

    def binary_search(array, target):
        if len(array) > 2:
            midpoint = array[round((len(array) - 1)//2)]

            midpoint_nd = [midpoint[1], midpoint[2]]
            #nd means name date (so: midpoint_namedate)

            if midpoint_nd == target:                     #if found
                return midpoint
            else:
                if midpoint[1] != target[0]:
                    if midpoint[1] < target[0]:
                        #looks @ upper half if the names of the target
                        # & current sublist looked at aren't the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(0)
                        findings = binary_search(newarray,target)
                        return findings

                    else:
                        #looks @ lower half if the names of the target
                        # & current sublist looked at aren't the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(len(newarray) - 1)
                        findings = binary_search(newarray,target)
                        return findings

                elif midpoint[1] == target[0]:
                    if midpoint[2] < target[1]:
                        #looks @ upper half if the names of the target
                        # & current sublist looked at are the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(0)
                        findings = binary_search(newarray,target)
                        return findings

                    else:
                        #looks @ lower half if the names of the target
                        # & current sublist looked at are the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(len(newarray) - 1)
                        findings = binary_search(newarray,target)
                        return findings
        else:
            midpoint = array[0]
            midpoint_nd = [midpoint[1], midpoint[2]]
            #nd means name date (so: midpoint_namedate)

            if midpoint_nd == target:                     #if found
                return midpoint

            elif midpoint_nd != target:                   #if not found
                return midpoint

    array = quick_sort_by_name(currenthv)

    findings = binary_search(array, target)

    valid_binary_end = time.time()

    valid_binary_time = valid_binary_end - valid_binary_start

    print(f"When the value is found, a sorted linear search takes {round(valid_linear_time,5)} seconds.")
    print(f"When the value is found, a binary search takes {round(valid_binary_time,5)} seconds.\n")


    #Comparing efficiency of searchers when value is found:

    if valid_linear_time > valid_binary_time:
        print(f"When the value is found, "\
        f"a binary search is faster than a linear search by {round(valid_linear_time-valid_binary_time, 7)} seconds.\n")

    elif valid_binary_time > valid_linear_time:
        print(f"When the value is found, "\
        f"a linear search is faster than a binary search by {round(valid_binary_time-valid_linear_time, 7)} seconds.\n")

    else:
        print("When the value is found, a "\
        "linear search and binary search currently take the same amount of time to run.\n" \
        "Please change the size of the list in 'Hotdogs.txt' to see a difference.\n")


    #Sorted linear search when value isn't found
    target = "Fake Vendor"
    findings = []
    found = False
    
    invalid_linear_start = time.time()

    for i in range(0, len(currenthv) - 1):
        if (currenthv[i][1] == target):
            findings.append(currenthv[i])
            found = True
        
    if (found == True):

        targetdate = 202618
        found = False
        for i in range(0, len(findings) - 1):
            if (int(findings[i][2]) == targetdate):
                found = True

    invalid_linear_end = time.time()

    invalid_linear_time = invalid_linear_end - invalid_linear_start

    #Binary search when value isn't found
    invalid_binary_start = time.time()

    target = ["Fake Vendor", str(202618)]

    def quick_sort_by_name(array):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()

        greater = []
        less = []

        for i in array:
            if i[1] > pivot[1]:
                greater.append(i)
            else:
                less.append(i)

        combined = quick_sort_by_name(less) + [pivot] + quick_sort_by_name(greater)

        return combined

    def binary_search(array, target):
        if len(array) > 2:
            midpoint = array[round((len(array) - 1)//2)]

            midpoint_nd = [midpoint[1], midpoint[2]]
            #nd means name date (so: midpoint_namedate)

            if midpoint_nd == target:                     #if found
                return midpoint
            else:
                if midpoint[1] != target[0]:
                    if midpoint[1] < target[0]:
                        #looks @ upper half if the names of the target
                        # & current sublist looked at aren't the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(0)
                        findings = binary_search(newarray,target)
                        return findings

                    else:
                        #looks @ lower half if the names of the target
                        # & current sublist looked at aren't the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(len(newarray) - 1)
                        findings = binary_search(newarray,target)
                        return findings

                elif midpoint[1] == target[0]:
                    if midpoint[2] < target[1]:
                        #looks @ upper half if the names of the target
                        # & current sublist looked at are the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(0)
                        findings = binary_search(newarray,target)
                        return findings

                    else:
                        #looks @ lower half if the names of the target
                        # & current sublist looked at are the same
                        newarray = array.copy()
                        for i in range(0, array.index(midpoint) + 1):
                            newarray.pop(len(newarray) - 1)
                        findings = binary_search(newarray,target)
                        return findings
        else:
            midpoint = array[0]
            midpoint_nd = [midpoint[1], midpoint[2]]
            #nd means name date (so: midpoint_namedate)

            if midpoint_nd == target:                     #if found
                return midpoint

            elif midpoint_nd != target:                   #if not found
                return midpoint

    array = quick_sort_by_name(currenthv)

    findings = binary_search(array, target)
    findings_nd = [findings[1], findings[2]]

    invalid_binary_end = time.time()

    invalid_binary_time = invalid_binary_end - invalid_binary_start

    print(f"When the value isn't found, a sorted linear search takes {round(invalid_linear_time, 5)} seconds.")
    print(f"When the value isn't found, a binary search takes {round(invalid_binary_time,5)} seconds.\n")

    #Comparing efficiency of searchers isn't found:

    if invalid_linear_time > invalid_binary_time:
        print(f"When the value isn't found, "\
        f"a binary search is faster than a linear search by {round(invalid_linear_time-invalid_binary_time, 7)} seconds.\n")

    elif invalid_binary_time > invalid_linear_time:
        print(f"When the value isn't found, "\
        f"a linear search is faster than a binary search by {round(invalid_binary_time-invalid_linear_time, 7)} seconds.\n")

    else:
        print("When the value isn't found, a "\
        "linear search and binary search currently take the same amount of time to run.\n"\
        "Please change the size of the list in 'Hotdogs.txt' to see a difference.\n")
    
    print("When sorting and searching, a quick sort and binary search are used respectively as they "\
    "repeatedly tested to be faster.\n")

#Save function

def save():
    """Overwrites the 'Hotdogs.txt' file with currenthv"""

    save_currenthv = ""

    for i in currenthv:
        if isinstance(i, str):
            i = i.split(",")


        for j in i:
            if j != i[len(i) - 1]:
                save_currenthv += f"{j},"
            else:
                save_currenthv += f"{j}\n"

    save_currenthv = save_currenthv.rstrip()

    with open ("Hotdogs.txt", "r+", encoding="utf-8") as data:
        data.write(save_currenthv)


user = password_validation()

if ((user == "WDC_employee1") or (user == "WDC_employee2")):
    employee_menu()

    while True:
        display = (input("Display vendor analysis? Yes/No: ")).title()
        if (display != "Yes") and (display != "No"):
            print("Please input yes or no.\n")
        elif display == "No":
            break
        else:
            display_analysis()
            break

elif user == "WDC_IT":
    it_menu()

    while True:
        display = (input("Display vendor analysis? Yes/No: ")).title()
        if (display != "Yes") and (display != "No"):
            print("Please input yes or no.\n")
        elif display == "No":
            break
        else:
            display_analysis()
            break

save()

print("Goodbye.")

time.sleep(5.00)