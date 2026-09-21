import numpy as np

A = np.array([[1, 2],
              [3, 4]])

print("Matrix:")
print(A)

print("Determinant:")
print(np.linalg.det(A))

print("Inverse:")
print(np.linalg.inv(A))

print("Rank:")
print(np.linalg.matrix_rank(A))

