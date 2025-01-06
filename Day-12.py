# CREATING ARRAY
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Created Array:", arr)
print("Type of the Array:", type(arr))

# 0-D ARRAY
import numpy as np
arr = np.array(42)
print("0-D Array:", arr)

# 1-D ARRAY
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("1-D Array:", arr)

# 2-D ARRAY
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D Array:\n", arr)

# 3-D ARRAY
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3-D Array:\n", arr)

# DIMENSIONS
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Dimension of a:", a.ndim)
print("Dimension of b:", b.ndim)
print("Dimension of c:", c.ndim)
print("Dimension of d:", d.ndim)

# NEGATIVE INDEXING
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last element from 2nd dimension:", arr[1, -1])

# SLICING-1
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Sliced Array [1:5]:", arr[1:5])

# SLICING-2
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Sliced Array [4:]:", arr[4:])

# SLICING-3
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Sliced Array [:4]:", arr[:4])

# NEGATIVE SLICING
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Negative Slicing [-3:-1]:", arr[-3:-1])

# STEP VALUE IN SLICING-1
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Sliced Array [1:5:2]:", arr[1:5:2])

# STEP VALUE IN SLICING-2
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Sliced Array [::2]:", arr[::2])

# SLICING IN 2-D ARRAYS
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Elements at [0:2, 2]:", arr[0:2, 2])
print("Subarray [0:2, 1:4]:\n", arr[0:2, 1:4])

# DATA TYPE - NUMERIC ARRAY
import numpy as np
arr = np.array([1, 2, 3, 4])
print("Data type of Numeric Array:", arr.dtype)

# DATA TYPE - STRING ARRAY
import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print("Data type of String Array:", arr.dtype)

# CREATING WITH DTYPE
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print("Array with DTYPE 'S':", arr)
print("Data type:", arr.dtype)

# CREATE ARRAY WITH 4-BYTE INTEGER
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
print("Array with 4-byte integer dtype:", arr)
print("Data type:", arr.dtype)

# COPY
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print("Original Array After Modification:", arr)
print("Copied Array:", x)

# VIEW
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print("Original Array After Modification:", arr)
print("Viewed Array:", x)

# ARRAY RESHAPE-1
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print("Reshaped Array (4x3):\n", newarr)

# ARRAY RESHAPE-2
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print("Reshaped Array (2x3x2):\n", newarr)

# FLATTENING ARRAYS
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print("Flattened Array:", newarr)

# ITERATING
import numpy as np
arr = np.array([1, 2, 3])
print("Iterating through 1D Array:")
for x in arr:
    print(x)

# ITERATING OVER ROWS IN A 2D NUMPY ARRAY
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Iterating Over Rows in 2D Array:")
for x in arr:
    print(x)

# ITERATING OVER ELEMENTS IN A 2D NUMPY ARRAY
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Iterating Over Elements in 2D Array:")
for x in arr:
    for y in x:
        print(y)

# CONCATENATION
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("Concatenated Array:", arr)

# CONCATENATION IN 2-D
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print("Concatenated 2D Array along rows:\n", arr)

# STACKING
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print("Stacked Array:\n", arr)

# HSTACK
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print("Horizontally Stacked Array:", arr)

# VSTACK
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print("Vertically Stacked Array:\n", arr)
