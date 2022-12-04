import numpy as np

A = np.array([[1, 1], [2, 2]])
B = np.array([[1, 1], [2, 2]])
equal_arrays = (A == B).all()

print(equal_arrays)