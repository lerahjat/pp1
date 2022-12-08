import re

with open("grades.txt", "r") as f:
    data = f.read()
    num = re.findall("\d.\d", data)
    sum = 0.0
    for i in num:
        sum +=float(i)


    print(sum/len(num))
