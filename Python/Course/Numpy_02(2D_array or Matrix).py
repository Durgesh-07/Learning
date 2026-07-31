import numpy as np
a = [[11,12,13],[21,22,23],[31,32,33]]
print(a)
A = np.array(a)
print(A)
print(A.ndim) # number of dimensions of the array
print(A.shape) # shape of the array; returns a tuple of dimensions
print(A.size) # size of numpy array
print(A[1,2])
print(A[1][2])

# adding two 2D arrays
X = np.array([[1,0],[0,1]])
print(X)
Y = np.array([[2,1],[1,2]])
print(Y)
Z =X + Y
print(Z)

# multiply to scalar
y = np.array([[2,1],[1,2]])
print(y)
z = 2 * y
print(z)

# multiplication of two 2D arrays

Y = np.array([[2, 1], [1, 2]]) 
print(Y)

X = np.array([[1, 0], [0, 1]]) 
print(X)
print(X * y)

# Matrix multiplication of two 2D arrays

A = np.array([[0,1,1],[1,0,1]])
B = np.array([[1,1], [1,1], [-1,1]])
Z = np.dot(A,B)
print(Z)
print(np.sin(Z))

# Transpose of a 2D array

C = np.array([[1,1],[2,2],[3,3]])
print(C.T)