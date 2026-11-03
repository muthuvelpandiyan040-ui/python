import numpy as np

# Create 5 x 5 array with numbers from 1 to 25
arr = np.arange(1, 26).reshape(5, 5)

print("Original Array:")
print(arr)

# 1. Print center 3 x 3 part
center = arr[1:4, 1:4]
print("\nCenter 3 x 3 Array:")
print(center)

# 2. Print reverse of center 3 x 3 part
reverse = center[::-1, ::-1]
print("\nReverse of Center 3 x 3 Array:")
print(reverse)

# 3. Print first 2 rows and last 2 columns
result = arr[:2, -2:]
print("\nFirst 2 Rows and Last 2 Columns:")
print(result)

# 4. Print all elements in a single line
print("\nAll Elements in a Single Line:")
print(arr.flatten())