#Data reader/writer

data = open("Hotdogs.txt", "r")         #opens file to read
print(data.read())                      #prints out file data
data.close()                            #closes file, important so that files don't risk corruption

print("-------------------")
#---------------------------

data = open("Hotdogs.txt", "a+")        #"a+" opens file to read and write to the end of the file
data.write("blahblahblah")
data.seek(0)                            #moves file pointer to the beginning of the code
print(data.read())