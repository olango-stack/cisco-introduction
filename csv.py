import csv
with open("potions.csv") as my_file:
    x = csv.reader(my_file)
    y = []
    for z in x:
        y += z