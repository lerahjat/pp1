array = [1,2,3,4,5,6,7,8,9]
i = 0
even = 0
odd = 0
while i < len(array):
    if array[i] % 2 == 0:
        even += 1
        i += 1
    else:
        odd += 1
        i += 1


print()
print(f"Amount of even numbers is {even}")
print(f"Amount of odd numbers is {odd}")

