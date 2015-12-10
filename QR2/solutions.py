#spec.py
'''
Derek Miller
Vol 1
'''
from scipy import linalg as la
import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def least_squares(A,b):
    """Return the least squares solutions to Ax = b using QR decomposition."""
    Q,R = la.qr(A)
    n = len(Q)
    QT = np.transpose(Q)
    b_hat = QT.dot(b)[:n]
    return la.solve_triangular(R,b_hat)


# Problem 2
def line_fit():
    """Plot linepts and its best-fit line on the same plot."""
    linepts = np.load('data.npz')['linepts']
    A = np.vstack(linepts[:,0])
    b = np.vstack(linepts[:,1])
    k = la.lstsq(A,b)[0]
    x0 = np.linspace(0,4000,100)
    y0 = k[0] * x0
    plt.plot(A,b,'ro',x0,y0)
    plt.show()
    

# Problem 3
def ellipse_fit():
    """Plot ellipsepts and its best-fit line on the same plot."""
    ellipsepts = np.load('data.npz')['ellipsepts']
    X = ellipsepts[:,:1]
    Y = ellipsepts[:,1:]
    A = np.hstack((X**2, X, X*Y, Y, Y**2))
    b = np.ones_like(X)
    a = la.lstsq(A,b)[0]
    plot_ellipse(X,Y,a[0],a[1],a[2],a[3],a[4])

def plot_ellipse(X, Y, a, b, c, d, e):
    """Plots an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1.

    Input:
      X (array) - x-coordinates of all the data points.
      Y (array) - y-coordinates of all the data points.
      a,b,c,d,e (float) - the coefficients from the equation of an 
                    ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1.
    """
    def get_r(a, b, c, d, e):
        theta = np.linspace(0,2*np.pi,200)
        A = a*(np.cos(theta)**2) + c*np.cos(theta)*np.sin(theta) + e*(np.sin(theta)**2)
        B = b*np.cos(theta) + d*np.sin(theta)
        r = (-B + np.sqrt(B**2 + 4*A))/(2*A)
        return r, theta
        
    r,theta = get_r(a,b,c,d,e)
    plt.plot(r*np.cos(theta), r*np.sin(theta), color = "r")
    plt.plot(X,Y,".", color = "b")
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()

# Problem 4
def power_method(A,tol):
    """Return the dominant eigenvalue of A and its corresponding eigenvector."""
    v = np.random.rand(len(A))
    x0 = v / la.norm(v)
    x1 = np.dot(A,x0) / la.norm(np.dot(A,x0))
    while abs(x1-x0).all() >= tol:
        x0 = x1
        x1 = np.dot(A,x0) / la.norm(np.dot(A,x0))
    y = np.inner(A.dot(x1), x1) / la.norm(x1)**2
    return x1,y
    
# Problem 5
def QR_algorithm(A,niter,tol):
    """Return the eigenvalues of A using the QR algorithm."""
    eigs = []
    A0 = la.hessenberg(A)
    Q,R = la.qr(A0)
    A1 = R.dot(Q)
    for x in xrange(niter):
        Q,R = la.qr(A1)
        A1 = R.dot(Q)
    for x in range(len(A)):
        if A[x,x] == A[-1,-1]:
            eigs.append(A[x,x])
        elif A[x+1,x] >= tol:
            e1 = A[x,x]*A[x+1,x+1] - A[x,x+1]*A[x+1,x] # determinant
            eigs.append(e1)
        elif A[x,x-1] >= tol:
            continue
        else:
            eigs.append(A[x,x])

    return eigs

