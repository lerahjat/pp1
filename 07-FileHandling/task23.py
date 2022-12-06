import csv

with open("students.csv", "r") as f:
    a = csv.reader(f)
    for i in a:
        if int(i[2]) < 30:
            print(i[0], i[1], i[3], i[4])
