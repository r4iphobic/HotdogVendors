#Data reader/writer

with open ("Hotdogs.txt", "r+") as data:
    hotdogs =[]
    hotdogs = data.read().split("\n")
    print(hotdogs)

for i in hotdogs:
    vendor = i.split(",")
    print(vendor)