# Invertible Affine Transformations and Linear Systems

# include your import statements here.
import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la
import time

# Helper Functions
def plot_transform(original, new):
    """Display a plot of points before and after a transform.
    
    Inputs:
        original (array) - Array of size (2,n) containing points in R2 as columns.
        new (array) - Array of size (2,n) containing points in R2 as columns.
    """
    window = [-5,5,-5,5]
    plt.subplot(1, 2, 1)
    plt.title('Before')
    plt.gca().set_aspect('equal')
    plt.scatter(original[0], original[1])
    plt.axis(window)
    plt.subplot(1, 2, 2)
    plt.title('After')
    plt.gca().set_aspect('equal')
    plt.scatter(new[0], new[1])
    plt.axis(window)
    plt.show()

def type_I(A, i, j):  
    """Swap the i-th and j-th rows of A."""
    A[i], A[j] = np.copy(A[j]), np.copy(A[i])
    
def type_II(A, i, const):  
    """Multiply the i-th row of A by const."""
    A[i] *= const
    
def type_III(A, i, j, const):  
    """Add a constant of the j-th row of A to the i-th row."""
    A[i] += const*A[j]


# Problem 1
def dilation2D(A, x_factor, y_factor):
    """Scale the points in A by x_factor in the x direction and y_factor in
    the y direction. Returns the new array.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        x_factor (float) - scaling factor in the x direction.
        y_factor (float) - scaling factor in the y direction.
    """
    newA = np.array([[A[0]*x_factor],[A[1]*y_factor]])
    return newA
    
# Problem 2
def rotate2D(A, theta):
    """Rotate the points in A about the origin by theta radians. Returns 
    the new array.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        theta (float) - number of radians to rotate points in A.
    """
    R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    newA = np.dot(R,A)
    return newA
    
# Problem 3
def translate2D(A, b):
    """Translate the points in A by the vector b. Returns the new array.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        b (2-tuple (b1,b2)) - Translate points by b1 in the x direction and by b2 
            in the y direction.
    """
    translate = np.vstack([b[0],b[1]])
    return A+translate
   
# Problem 4
def rotatingParticle(time, omega, direction, speed):
    """Display a plot of the path of a particle P1 that is rotating 
    around another particle P2.
    
    Inputs:
     - time (2-tuple (a,b)): Time span from a to b seconds.
     - omega (float): Angular velocity of P1 rotating around P2.
     - direction (2-tuple (x,y)): Vector indicating direction.
     - speed (float): Distance per second.
    """
    p1 = (1,0)
    t = np.linspace(time[0],time[1],500)
    x = np.empty(500)
    y = np.empty(500)

    counter = 0
    for i in t:
        p2 = np.array((speed*i)/np.linalg.norm(direction)*np.vstack(direction))
        rotate = rotate2D(np.vstack(p1),i*omega)
        p1x = translate2D(rotate,p2)
        x[counter] = p1x[0]
        y[counter] = p1x[1]
        counter += 1
    plt.plot(x,y)
    plt.show()


# Problem 5
def REF(A):
    """Reduce a square matrix A to REF. During a row operation, do not
    modify any entries that you know will be zero before and after the
    operation. Returns the new array."""
    
    for i in range(len(A)): # i indicates a row above
        for j in range(i+1,len(A)): # j indicates a row below
            type_III(A, j, i, (-A[j,i]/A[i,i]))
    return A

# Problem 6
def LU(A):
    """Returns the LU decomposition of a square matrix."""

    n = len(A)
    U = np.copy(A)
    L = np.identity(n)
    for i in range(1,n):
        for j in range(i):
            L[i,j] = U[i,j]/U[j,j]
            U[i,j:] = U[i,j:] - (L[i,j])*(U[j,j:])
    return L,U

# Problem 7
def time_LU():
    """Print the times it takes to solve a system of equations using
    LU decomposition and (A^-1)B where A is 1000x1000 and B is 1000x500."""

    A = np.random.rand(1000,1000)
    b = np.random.rand(1000,500)

    start = time.time()
    A_lu_factor = la.lu_factor(A)
    end = time.time()
    time_lu_factor = end - start  

    start = time.time()
    A_inv = la.inv(A)
    end = time.time()
    time_inv = end - start 

    start = time.time()
    la.lu_solve(A_lu_factor,b)
    end = time.time()
    time_lu_solve = end - start 

    start = time.time()
    la.inv(A).dot(b)
    end = time.time()
    time_inv_solve = end - start 


    print "LU solve: " + str(time_lu_factor + time_lu_solve)
    print "Inv solve: " + str(time_inv + time_inv_solve)
    
    # What can you conclude about the more efficient way to solve linear systems?
    print "Solutions are much faster with LU solve."  # print your answer here.

