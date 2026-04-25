#Binary searcher


#Prepping the code to be read "&" manipulated:

with open ("Hotdogs.txt", "r+") as data:      #opens file to read and write (also automatically closes)
    currenthv =[]
    currenthv = data.read().split("\n")       #splits the text file into a list by each new line

for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
    currenthv[i] = currenthv[i].split(",")

#------------------------------------------

targetname = input("Input vendor's name: ")
targetdate = input(f"Input the date you wish to view for {targetname}: ")
target = [targetname, targetdate]
print(target)

def binarySearch(list, target):
    if (len(list)> 2):
        midpoint = list[round((len(list) - 1)//2)]

        midpoint_nd = [midpoint[1], midpoint[2]]        #nd means name date (so: midpoint_namedate)
        print(midpoint, "\n", midpoint_nd)

        if (midpoint_nd == target):
            print(f"we found it: {midpoint}")
            return(midpoint)
        else:
            if (midpoint[1] != target[0]):
                if (midpoint[1] < target[0]):
                    print("looking at upper half...")
                    newlist = list.copy()
                    for i in range(0, list.index(midpoint) + 1):
                        newlist.pop(0)
                    findings = binarySearch(newlist,target)
                    return(findings)

                else:
                    print("looking at lower half...")
                    newlist = list.copy()
                    for i in range(0, list.index(midpoint) + 1):
        	            newlist.pop(len(newlist) - 1)
                    findings = binarySearch(newlist,target)
                    return(findings)
                
            elif (midpoint[1] == target[0]):
                if (midpoint[2] < target[1]):
                    print("looking at upper half...")
                    newlist = list.copy()
                    for i in range(0, list.index(midpoint) + 1):
                        newlist.pop(0)
                    findings = binarySearch(newlist,target)
                    return(findings)
                    
                else:
                    print("looking at lower half...")
                    newlist = list.copy()
                    for i in range(0, list.index(midpoint) + 1):
        	            newlist.pop(len(newlist) - 1)
                    findings = binarySearch(newlist,target)
                    return(findings)
    else:
        midpoint = list[0]
        midpoint_nd = [midpoint[1], midpoint[2]]        #nd means name date (so: midpoint_namedate)

        if (midpoint_nd == target):
            print(f"we found it: {midpoint}")
            return(midpoint)
        
        elif (midpoint_nd != target):
            return(midpoint)
                

findings = binarySearch(currenthv, target)
print(findings)
findings_nd = [findings[1], findings[2]]

if (findings_nd != target):
    print("target not found. sorry!")