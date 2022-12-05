ar = [15, 38, 7, 23, 14]
a = int(input("Your number"))
for i in range(len(ar)):
    if ar[i] == a:
        print(f"In {i} there is number {a}")

    else:
        print(f"In {i} there is no such a number {a}")
