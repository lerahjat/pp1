array = [6,8,3,1,0,5,7]
num = int(input("Input your number:"))
count = 0
for i in array:
    if num > i:
        count = count + 1


print(f"The numbers greater than {num} : {count}")

