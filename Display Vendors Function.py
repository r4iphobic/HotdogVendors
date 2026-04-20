#Display Vendors

def displayVendors(file):
    #Prepping the code to be read "&" manipulated:

    with open (file, "r+") as data:      #opens file to read and write (also automatically closes)
        currenthv =[]
        currenthv = data.read().split("\n")       #splits the text file into a list by each new line

    for i in range(0,(len(currenthv) -1) ):       #splits the text file into smaller lists by each ','
        currenthv[i] = currenthv[i].split(",")


    title = "{:<20} {:^25} {:>20}       {:>20} {:>20} {:^15} {:^15}"        #formats the titles (clarifying what each value in the file is)
    values = "{:<20} {:^25}{:>20}       {:^20} {:^20} {:^15} {:^15}"        #formats the values within the file

    print(title.format("Vendor ID", "Vendor Name", "Year and Week", "# of Vegan Hotdogs", "# of Meat Hotdogs", "Onions (kg)", "Ketchup (litres)"), f"\n{"-"*139}")

    for i in range(0,(len(currenthv) -1)):
        print(values.format(currenthv[i][0],currenthv[i][1],currenthv[i][2],currenthv[i][3],currenthv[i][4],currenthv[i][5],currenthv[i][6]))

displayVendors("Hotdogs.txt")