#Prepping the code to be read "&" manipulated:

with open ("Testhotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")


#UNLINTED, UNVALIDATED Display Analysis

def displayAnalysis():
    while True:                                                         #enter today's date
        year = int(input("Enter year: "))
        if ((year < 10000) and (year >= 1000)):
            week = int(input("Enter week: "))
            if((week >= 1) and (week <= 52)):
                date = str(year) + str(week).zfill(2)                   #todays date in YYYYMM format
                print(f"Date valid: {date}\n")
                break
            else:
                print("Week must be between 1 and 52")
        else:
            print("Year must be in YYYY format (e.g. 2026)")
    
    analysis = ""
    array = []

    while True:
        vendorChoice = int(input("Analyse...\n" \
        "1. All Vendors\n" \
        "2. One Vendor\n" \
        "Input: "))

        if (vendorChoice == 1):
            array = currenthv
            break
        elif (vendorChoice == 2):
            while True:
                v_name = input("Input vendor name: ")
                for i in range (0, len(currenthv)):
                    if (type(currenthv[i]) == str):
                        currenthv[i] = currenthv[i].split(",")
                    
                    if (currenthv[i][1] == v_name):
                        array.append(currenthv[i])
                
                if (array != []):
                    break
                else:
                    print("Vendor not found.\n")
            break
        else:
            print("Please enter 1 or 2 (integers).\n") 
    
    def superlativeFinder(index):
        superlative = array[0]
        superlative_nd = []
        superlative = float(superlative[index])

        for i in array:
            if (type(i) == str):
                i = i.split(",")

            currentval = float(i[index])

            if (currentval > superlative):
                superlative_nd = f"{i[1]} during {i[2]}"
                superlative = currentval
            elif (currentval == superlative):
                superlative_nd += f" and {i[1]} during {i[2]}"
                superlative = currentval
        
        return(superlative_nd)

    #Most Productive Vendor
    superlative = []
    superlative = array[0]
    superlative_nd = []
    
    superlative = float(superlative[3]) + float(superlative[4]) + float(superlative[5]) + float(superlative[6])
    
    for i in array:
        if (type(i) == str):
            i = i.split(",")

        currentval = float(i[3]) + float(i[4]) + float(i[5]) + float(i[6])

        if (currentval > superlative):
            superlative_nd = f"{i[1]} during {i[2]}"
            superlative = currentval
        elif (currentval == superlative):
            superlative_nd += f" and {i[1]} during {i[2]}"
            superlative = currentval
    
    analysis += f"The vendor(s) that was/were the most productive is/are {superlative_nd} \n \n"

    #Number of vegan hotdogs versus meat hotdogs supplied
    veganHotdogCount = 0
    meatHotdogCount = 0

    for i in array:
        if (type(i) == str):
            i = i.split(",")

        veganHotdogCount += int(i[3])
        meatHotdogCount += int(i[4])
    
    if (veganHotdogCount > meatHotdogCount):
        hotdogEvaluation = f"Overall, there were {veganHotdogCount-meatHotdogCount} more vegan hotdogs supplied than meat hotdogs."
    elif (veganHotdogCount == meatHotdogCount):
        hotdogEvaluation = f"Overall, there has been an equal amount of vegan and meat hotdogs supplied ({veganHotdogCount})"
    else:
        hotdogEvaluation = f"Overall, there were {meatHotdogCount-veganHotdogCount} more meat hotdogs supplied than vegan hotdogs."
    
    analysis += f"{hotdogEvaluation} \n \n"

    #Vendor using the most amount of ketchup

    ketchup = 0

    for i in array:
        if (type(i) == str):
            i = i.split(",")

        ketchup += int(i[6])
    
    analysis += f"Total ketchup supplied as of {date} is {ketchup} litres. \n \n"

    #Vendor that has ordered the most amount of onions

    analysis += f"The vendor(s) that ordered the most onions was/were {superlativeFinder(6)} \n \n"

    #Vendor that ordered the most vegan hotdogs

    analysis += f"The vendor(s) that ordered the most vegan hotdogs was/were {superlativeFinder(3)} \n \n"

    #Vendor that ordered that most meat hotdogs
    
    analysis += f"The vendor(s) that ordered the most meat hotdogs was/were {superlativeFinder(4)} \n \n"

    print(f"\nAnalysis... \n{("-"*11)} \n{analysis}")

    if (vendorChoice == 1):
        with open (f"Analysis on {date}", "a+") as file:
            file.write(analysis)
    elif (vendorChoice == 2):
        with open (f"{v_name} Analysis on {date}", "a+") as file:
            file.write(analysis)


displayAnalysis()