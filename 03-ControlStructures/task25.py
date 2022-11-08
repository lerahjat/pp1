height = int(input())
width = int(input())

for i in range(height):
    if i !=0 and i != height-1:
        print('*' + '  ' * (width-2)+ ' *')
    else:
        print("* "*width)