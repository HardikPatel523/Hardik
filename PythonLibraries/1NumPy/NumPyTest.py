import time
import numpy as np # type: ignore

print("\n==============================")
print("1. BASIC ARRAY CREATION")
print("==============================")

arr = np.array([1, 2, 3, 4])
print("NumPy Array:", arr)

matrix = np.array([[1,2,3], [4,5,6]])
print("\n2D Array:")
print(matrix)

zeros = np.zeros((2,3))
ones = np.ones((3,3))
arange_arr = np.arange(1, 10)
arange_arr2 = np.arange(2, 5)


print("\nZeros:\n", zeros)
print("\nOnes:\n", ones)
print("\nArange (1 to 9):", arange_arr)
print("\nArange (2 to 5):", arange_arr2)


print("\n==============================")
print("2. VECTORIZED OPERATIONS (FAST)")
print("==============================")

arr = np.array([1, 2, 3, 4])

print("arr + 5:", arr + 5)     # Add
print("arr * 2:", arr * 2)     # Multiply
print("arr ** 2:", arr ** 2)   # Square
print("arr / 2:", arr / 2)     # Divide


print("\n==============================")
print("3. COMPARISON: PYTHON LIST vs NUMPY SPEED")
print("==============================")

size = 1_000_000
py_list = list(range(size))
np_arr = np.arange(size)

# Python list time
start = time.time()
py_result = [x * 2 for x in py_list]
py_time = time.time() - start

# NumPy time
start = time.time()
np_result = np_arr * 2
np_time = time.time() - start

print(f"Python List Time: {py_time:.4f} seconds")
print(f"NumPy Array Time: {np_time:.4f} seconds")
print("Speedup:", round(py_time / np_time), "x faster!")


print("\n==============================")
print("4. ARRAY SHAPE & RESHAPE")
print("==============================")

arr = np.arange(1, 13)
print("Original:", arr)

reshaped = arr.reshape((3,4))
print("\nReshaped 3x4 matrix:\n", reshaped)


print("\n==============================")
print("5. INDEXING & SLICING")
print("==============================")

arr = np.arange(10)
print("Array:", arr)
print("Element at index 3:", arr[3])
print("Slice 2:7:", arr[2:7])
print("Every second element:", arr[::2])


print("\n==============================")
print("6. STATISTICS")
print("==============================")

arr = np.array([10, 20, 30, 40, 50])

print("Mean:", arr.mean())
print("Sum:", arr.sum())
print("Standard Deviation:", arr.std())
print("Min:", arr.min())
print("Max:", arr.max())


print("\n==============================")
print("7. BROADCASTING EXAMPLES")
print("==============================")

matrix = np.array([[1,2,3],
                   [4,5,6]])

print("Original Matrix:\n", matrix)
print("\nAdd 5 to entire matrix:\n", matrix + 5)

row = np.array([1,1,1])
print("\nAdd row [1,1,1] to each row:\n", matrix + row)


print("\n==============================")
print("8. REAL ML EXAMPLE: FEATURE SCALING")
print("==============================")

data = np.array([50, 100, 150, 200, 250])

scaled = (data - data.mean()) / data.std()
print("Original:", data)
print("Standardized:", scaled)


print("\n==============================")
print("9. RANK & DIMENSIONS")
print("==============================")

matrix = np.array([[1,2,3], [4,5,6]])

print("Array:", matrix)
print("Shape:", matrix.shape)
print("Dimensions (ndim):", matrix.ndim)
print("Total elements:", matrix.size)


print("\n==============================")
print("10. COPYING vs VIEW")
print("==============================")

arr = np.array([1,2,3,4])
view = arr.view()
copy = arr.copy()

arr[0] = 99

print("Original:", arr)
print("View (changes reflect):", view)
print("Copy (separate data):", copy)


print("\n==============================")
print("FINISHED! NumPy Demonstration Complete")
print("==============================")
