arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
for i in arr:
   for k in arr[0]:
       k += 1
   for x in arr[1]:
       x += 1
   for y in arr[2]:
       y += 1
   for z in arr[3]:
       z += 1
sum = k+x+y+z

print(sum)


