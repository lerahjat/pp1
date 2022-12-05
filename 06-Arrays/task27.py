arr = [5,1,9,6,1]
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
    print(max-min)






ans = minmax(arr, n)


