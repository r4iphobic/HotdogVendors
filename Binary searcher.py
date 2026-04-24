#Binary searcher

def binarySearch():
    #Prepping the code to be read "&" manipulated:

    with open ("Hotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
        currenthv =[]
        currenthv = data.read().split("\n")       #splits the text file into a list by each new line

    for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
        currenthv[i] = currenthv[i].split(",")

    #------------------------------------------

    target = input("Input vendor's name: ")