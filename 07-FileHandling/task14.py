fileName = input("Enter the file's name: ")
file = open(fileName, 'r')
counter = 0
for i in file:
    counter +=1
print(f"File's name: {fileName}")
print(f"The number of rows: {counter}")
file.close()