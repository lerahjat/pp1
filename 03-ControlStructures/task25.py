hight = int(input())
wight = int(input())

for i in range(hight):
    if i == 0 or i == hight - 1:
        for j in range(wight):
            print("*", end='')
    else:
        print("*", end='')
        for j in range(1, wight - 1):
            print(' ', end='')
        print("*", end='')
    print()
