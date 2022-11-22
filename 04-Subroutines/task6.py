def sq_matrix(n):
    for i in range(0,9,3):
        for j in range(1,n+1):
            print((j+i), end=" ")
        print()

sq_matrix(3)