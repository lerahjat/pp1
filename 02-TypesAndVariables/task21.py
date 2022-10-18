import random
number = random.randint(1, 100)
a = int(input("Your number:"))
while a != number:
    a = int(input("Your number:"))

    if a == number:
        print("True")
        break
    elif a < number:
        print ("Go higher!")
    else:
        print("Go lower!")