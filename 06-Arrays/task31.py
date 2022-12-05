array = [1,2,3,4,5,6,7,8,9]
even = []
odd = []
for i in range(len(array)):
    if i % 2 :
        even.append(array[i])
    else:
         odd.append(array[i])
print(even+odd)
