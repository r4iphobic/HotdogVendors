#Data reader/writer

data = open("Hotdogs.txt", "r")         #opens file to read
print(data.read())                      #prints out file data
data.close()                            #closes file, important so that files don't risk corruption

print("-------------------")
#---------------------------

data = open("Hotdogs.txt", "a+")        #"a+" opens file to read and write to the end of the file
data.write("blahblahblah")
data.seek(0)                            #moves file pointer to the beginning of the file
print(data.read())
print("-----------please-----------")
#---------------------------

with open ("Hotdogs.txt", "r+") as data:
    currenthv =[]
    currenthv = data.read().split("\n")
    print(currenthv)

for i in currenthv:
    vendor = i.split(",")
    print(vendor)
