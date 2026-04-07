#Prepping the code to be read & manipulated:

with open ("Hotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")


#---Unsorted Linear searcher

def testus_linearsearch(targetlist, target):
    while True:
        for i in targetlist:
            for j in i:                    #looks at each value in each sublist, if it matches, prints out whole sublist
                if (j == target):
                    print(i)
        break
    
testus_linearsearch(currenthv, "Dolly Dogs")  #"Dolly Dogs" is a placeholder, will be user input
