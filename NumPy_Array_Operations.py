import numpy as np

# 1. Create a 1D array from 1 to 20
arr = np.arange(1, 21)

print("1D Array:")
print(arr)

# 2. Reshape into 4 x 5 matrix
matrix = arr.reshape(4, 5)

print("\n4 x 5 Matrix:")
print(matrix)

# 3. Find transpose
transpose = matrix.T

print("\nTranspose of Matrix:")
print(transpose)

# 4. Calculate sum of all elements
total = np.sum(matrix)
print("\nSum of All Elements:", total)

# Row-wise sum
row_sum = np.sum(matrix, axis=1)
print("Row-wise Sum:", row_sum)

# Column-wise sum
col_sum = np.sum(matrix, axis=0)
print("Column-wise Sum:", col_sum)

# 5. Extract even numbers using Boolean indexing
even = arr[arr % 2 == 0]

print("\nEven Numbers:")
print(even)