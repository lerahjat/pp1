list = [[True,False],[True,True],[False,False]]


for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] == True:
            list[i][j] = False
        elif list[i][j] == False:
            list[i][j] = True

print(list)