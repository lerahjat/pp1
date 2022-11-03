rows = 4

for i in range(rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
for i in range(rows, -1,-1):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
