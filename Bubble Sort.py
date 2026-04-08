#---Bubble sort

testlist = [75, 6, 20, 19]

swap = True
while (swap == True):
    swap = False
    for i in range (0, (len(testlist) - 1)):
        if (testlist[i] > testlist[i+1]):
            a = testlist[i]
            testlist.remove(testlist[i])
            testlist.insert(i+1, a)
            swap = True
        print(testlist)

print("Final list is", testlist)
