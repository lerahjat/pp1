from numpy import asarray

data = [[1, 2, 3], [4, 5, 6]]
data = asarray(data)
# step through rows
for i in range(data.shape[0]):
    print(data[i, :])


data1 = [[1, 2, 3], [4, 5, 6]]
data1 = asarray(data1)
# step through rows
for i in range(data1.shape[1]):
    print(data1[:, i])
