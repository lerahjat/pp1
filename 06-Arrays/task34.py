arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [5, 6, 7, 8, 9]
set = 0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            set += 1
if set > 0:
    print(True)
else:
    print(False)


