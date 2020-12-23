import numpy as np

mat = np.array([[1,2,3],[4,5,6]])
mat_2 = np.array([[1,2],[4,5],[7,8]])
print(mat, "\n", mat_2)

mult = mat.dot(mat_2)
print(mult)

