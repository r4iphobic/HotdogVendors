#Prepping the code to be read "&" manipulated:

with open ("Testhotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")


#UNLINTED, UNVALIDATED Quick Sort function

while True:
    index = int(input("Would you like to sort by...\n" \
        "1. Name\n" \
        "2. Date\n"))

    if ((index != 1) and (index != 2)):
        print("Please enter the integer 1 or 2.\n")
    else:
        break

def quickSort(list):
    if (len(list) <= 1):
        return(list)
    else:
        pivot = list.pop()

    greater = []
    less = []

    for i in list:
        if (i[index] > pivot[index]):
            greater.append(i)
        else:
            less.append(i)
        
    combined = quickSort(less) + [pivot] + quickSort(greater)

    return(combined)

print(quickSort(currenthv))


