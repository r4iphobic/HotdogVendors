#Sorted Linear Search

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
        print(f"{len(findings)} instances of {target} found.")
        return(findings)
    else:
            print(f"{target} not found.")
            return("")


s_linearsearch()
