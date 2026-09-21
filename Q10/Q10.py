
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Addition:")
print(A + B)

print("Subtraction:")
print(A - B)

print("Multiplication:")
print(np.dot(A, B))

print("Transpose of A:")
print(A.T)

### B. Without NumPy
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Addition
addition = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        addition[i][j] = A[i][j] + B[i][j]

print("Addition:")
print(addition)

# Subtraction
subtraction = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        subtraction[i][j] = A[i][j] - B[i][j]

print("Subtraction:")
print(subtraction)

# Multiplication
multiplication = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            multiplication[i][j] += A[i][k] * B[k][j]

print("Multiplication:")
print(multiplication)

# Transpose
transpose = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        transpose[j][i] = A[i][j]

print("Transpose of A:")
print(transpose)


