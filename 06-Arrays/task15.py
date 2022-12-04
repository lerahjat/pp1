ar =[ [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
for i in range(len(ar)):
    for j in range(len(ar[i])):
        if i == j  :
            ar[i][j] = 1
print(ar)


