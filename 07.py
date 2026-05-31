"""
Python List vs NumPy Array

1. Python lists can store different data types
   (e.g., int, float, string).
   NumPy arrays usually store elements of the same data type.

2. Python lists are slower for numerical computations.
   NumPy arrays are faster because they are optimized for mathematical operations.

3. Python lists require more memory.
   NumPy arrays use memory more efficiently.

4. Mathematical operations on Python lists are limited.
   NumPy arrays support vectorized operations.

5. Python lists are part of Python's built-in library.
   NumPy arrays require importing the NumPy package.

Example:
"""

import numpy as np

# Python List
lst = [1, 2, 3]
print("Python List:", lst)

# NumPy Array
arr = np.array([1, 2, 3])
print("NumPy Array:", arr)

# Addition
print("List + List:", lst + lst)
print("Array + Array:", arr + arr)