file = open('numbers.txt','r')
sum =0
for line in file:
    num = int(line)
    sum = sum+num

file.close()
print(sum, end=" ")