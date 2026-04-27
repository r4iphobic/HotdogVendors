#UNLINTED, UNVALIDATED Bubble Sort

#---Prepping the code to be read & manipulated:

with open ("Testhotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")

#---Bubble sort

swap = True
index = int(input("Input index: "))           #is the index of the value the array will be sorted by

while (swap == True):
    swap = False                              #to stop the loop
    for i in range(0, (len(currenthv) - 1)):
        if ((currenthv[i][index]) > (currenthv[i+1][index])):
            #compares the values in each sublist, swaps if left value is bigger than right value
            a = currenthv[i]
            currenthv.remove(currenthv[i])
            currenthv.insert(i+1,a)
            swap = True                       #to start it again if a swap has been made

print(currenthv)
