arr = [4,2,8,4,7,9,5]
n = len(arr)

def minmax(arr, n):
    max = arr[0]
    min = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    print(min,max)






ans = minmax(arr, n)
