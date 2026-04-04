#Linear searcher

testlist = ["wrong", "not looking for this", "right", "incorrect", "extremely loud incorrect buzzer", "correct!"]

def us_linearsearch(targetlist, target):     #us means unsorted
    while True:
        for i in targetlist:
            if (i == target):
                print(f"Found {target} @ index {testlist.index(i)}")
        break

us_linearsearch(testlist,"right")
