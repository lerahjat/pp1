arr = [5,1,9,6,1]
def bubbleSort(arr):


    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

bubbleSort(arr)
print(arr[-2])
