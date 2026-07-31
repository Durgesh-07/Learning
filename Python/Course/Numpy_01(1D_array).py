import numpy as np
a = np.array([1,2,3,4,5])
print(a)
# Print each element

for i in range(len(a)):
    print(f"a[{i}]: {a[i]}")
print(np.__version__)
print(type(a))
print(a.dtype) # Data type of the array elements

b = np.array([31.,11.02,6.2,213.2,5.2])
c = np.array([20,1,2,3,4])
print(c)
c[4] = 0
print(c)
a = np.array([10,2,30,40,50])
print(a)
a[1] = 20
print(a)
d = c[1:4]
print(d)
c[3:5] = 300,400
print(c)
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])
print(arr[:4])
print(arr[4:])
print(arr[1:5:])


arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:8:2]) # printing even no.s

select = [0,2,3,4] # using list to select the elements from the array
print(arr[select])
d = c[select]
print(d)
c[select] = 100000
print(c)

a = np.array([1,2,3,4,5])
print(a.size) # size of numpy array
print(a.ndim) # number of dimensions of the array
print(a.shape) # shape of the array; returns a tuple of dimensions

# Numpy statistics functions
a = np.array([1,-1,1,-1])
mean = np.mean(a) # mean
print(mean)
standard_deviation = np.std(a) # standard deviation
print(standard_deviation)
b = np.array([-1,2,3,4,5])
max_b = b.max() # maximum value
print(max_b)
min_b = b.min() # minimum value
print(min_b)
c = np.array([-10,201,43,94,502])
print(c.min()+c.max()) # sum of min and max

# Numpy array operations
u = np.array([1,0])
print(u)
v = np.array([0,1])
print(v)
z = np.add(u,v) # addition of two numpy arrays
print(z)

# visualization of numpy arrays
import matplotlib.pyplot as plt

def Plotvec1(u,v,z):
    """ This function plots the vectors u, v and z in 2D space. """
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u+0.1), 'u') # adds the text u to the u arrow

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v+0.1), 'v') # adds the text u to the u arrow    

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z+0.1), 'z') # adds the text u to the u arrow
    plt.ylim(-2,2)
    plt.xlim(-2,2)
    plt.show()

# plot numpy arrays
help(Plotvec1)
Plotvec1(u,v,z)

a = np.array([10,20,30])
print(a)
b = np.array([5,10,15])
print(b)
c = np.subtract(a,b) # element-wise subtraction
print(c)
x = np.array([1,2])
print(x)
y = np.array([2,1])
print(y)
z = np.multiply(x,y) # element-wise multiplication
print(z)
a = np.array([10,20,30])
print(a)
b = np.array([2,10,5])
print(b)
c = np.divide(a,b) # element-wise division
print(c)
x = np.array([1,2])
y = np.array([3,2])
print(np.dot(x,y)) # dot product of two numpy arrays
print(x[0])
print(x[1])
print(y[0])
print(y[1])
print(x[0]*y[0]+x[1]*y[1]) # dot product of two numpy arrays
u = np.array([1,2,3,-1])
print(u)
print(u+1)

# Maths Functions

x = np.array([0,np.pi/2,np.pi])
y = np.sin(x) # sine of the elements of the array
print(y)

# linespace

print("np.linspace(-2,2,5): ", np.linspace(-2,2,5))
print("np.linspace(-2,2,9): ", np.linspace(-2,2,9))
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
plt.plot(x,y) # ploting results of sine function
plt.show()
arr1 = np.array([1, 2, 3])
for x in arr1:
  print(x)