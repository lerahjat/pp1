arr = [[7, 3, 7, 9, 0], [2, 9, 0, 1, 5], [3, 8, 6, 4, 7], [8, 7, 1, 1, 5]]
sum = 0
sum1 = 0

for i in range(len(arr)):
    sum = sum + arr[i][-1]
    sum1 += arr[i][0]

print(sum)
print(sum1)
