#Prepping the code to be read & manipulated:

with open ("Hotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")


#---Unsorted Linear searcher (with date specification)

def us_linearsearch(targetlist, target):
    found = False
    findings = []                          #holds all instances of the search value found
    while True:                            #searches for the user input
        for i in targetlist:
            for j in i:                    #looks at each value in each sublist, if it matches, prints out whole sublist
                if (j == target):
                    findings.append(i)
                    print(i)
                    found = True           #makes it so that the procedure doesn't ask to try again
        break
    

    if (found == False):                   #if user input not found
        print(f"{target} not found.")
        retry = input("Try again? (Yes/No)")
        if (retry == "Yes"):
            us_linearsearch(targetlist, input(""))   #runs the procedure again
    else:
        return(findings)
        


def us_datesearch(findings):
    found = False
    if (findings != None):                    #looks for then displays specific date requested by user
        
        date = int(input("Which date would you like to view? YYYYWW: "))
        date = str(date)

        for i in findings:
            for j in i:
                if (j == date):
                    print(i)                    #prints out all stats for the vendor on that date
                    found = True
        
        if (found == False):
            print(f"Data for the vendor inputted on the date {date} not found.")
            retry = input("Try again? (Yes/No)")
            if (retry == "Yes"):
                us_datesearch(findings)
        

    
us_datesearch(us_linearsearch(currenthv, input("")))     #searches for inputted value first, then searches for date
