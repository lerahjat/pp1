array1 = [4,36,12,28,9,44,5]
array2 = [5, 1, 36]

for i in range(len(array2)):
    for j in range(len(array1)):
        if array1[j] == array2[i]:
            array1[j] = 0

for i in range(len(array1)):
    if array1[i] != 0:
        print(array1[i], end = " ")