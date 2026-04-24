#Sorted Linear Search

def s_datesearch(findings):
    targetdate = int(input("Input date to view: ")) 
    found = False
    for i in range(0, len(findings) - 1):
        if (int(findings[i][2]) == targetdate):
               print(findings[i])
               found = True
               repeat = input("Would you like to search for another date?: ")
               if (repeat == "Yes"):
                    s_datesearch(findings)
    if (found == False):
        repeat = ""
        repeat = input(f"{targetdate} not found.\nTry again?: ")
        if (repeat == "Yes"):
            s_datesearch(findings)
                    
        


def s_linearsearch():
    #Prepping the code to be read "&" manipulated:

    with open ("Hotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
        currenthv =[]
        currenthv = data.read().split("\n")       #splits the text file into a list by each new line

    for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
        currenthv[i] = currenthv[i].split(",")

    #------------------------------------------

    target = input("Input vendor's name: ")
    findings = []
    found = False
    
    for i in range(0, len(currenthv) - 1):
        if (currenthv[i][1] == target):
            findings.append(currenthv[i])
            found = True
        
    if (found == True):
        print(f"{len(findings)} instances of {target} found.\n")
        
        print(f"Dates available:")
        for i in range(0, len(findings) - 1):
             print(findings[i][2])

        s_datesearch(findings)
        
    else:
            print(f"{target} not found.")
            repeat = ""
            repeat = input("Try again?: ")
            if (repeat == "Yes"): 
                 s_linearsearch()
    


s_linearsearch()
