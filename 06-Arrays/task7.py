arr = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0
for i in arr:
    if i % 2 == 0:
        even = even+1
    else:
        odd = odd+i
print(f"number of odd elements is: {odd}\nnumber of even elements is: {even} ")
