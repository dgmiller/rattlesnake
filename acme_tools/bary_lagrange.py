# Computes the barycentric Lagrange interpolation

import numpy as np
from matplotlib import pyplot as plt

def weights(x):
    """INPUT
         x  := (ndarray) vector of x-coordinate points

       OUTPUT
         w  := (list) barycentric weights for Lagrange Interpolation
    """
    n = len(x)
    w = []
    for j in range(n):
        w_i = 1.
        for k in range(n):
            if j == k:
                continue
            else:
                w_i *= 1./(x[j] - x[k])
        w.append(w_i)
    return np.array(w)

def polynomial(points,x,y,w):
    """INPUT:
         points := nparray of axis points
         x      := nparray of x-coordinate points
         y      := nparray of y-coordinate points
         w      := nparray of barycentric weights

       OUTPUT:
         p      := array of values of the polynomial at the given points
    """
    n = len(w)
    numer = 0.
    denom = 0.
    for j in range(n):
        numer += (w[j] * y[j]) / (points - x[j])
        denom += w[j] / (points - x[j])
    return numer / denom # this is the output p

def plot_results():
    axis = np.linspace(-1.,1.,1000) # the x_axis
    f_x = np.absolute(axis) # my function f(x)
    for n in range(2,21):
        # the n+1 distinct points (x values for our interpolating polynomial)
        x = np.linspace(-1.,1.,n+1)
        y = np.absolute(x)
        w = weights(x) # weights of points
        p_x = polynomial(axis,x,y,w) # this is the polynomial we are plotting
        plt.subplot(5,4,n-1)
        plt.plot(axis, p_x, color='k')
        plt.plot(axis, f_x, color='r')
        plt.axis([-1,1,-5,5])
    plt.show()

def plot_cheby(x,y):
    """
    Takes in two vectors of x and y coordinate points.
    Plots the usual barycentric interpolation on one plot
    and the interpolation using the chebyshev points on
    another plot.
    """
    axis = np.linspace(-1.,1.,1000)
    chx = []
    chy = []
    for j in range(4):
        chx.append(np.cos(j*np.pi/3))
        chy.append(np.sin(chx[j]*np.pi))
    cheby_x = np.array(chx)
    cheby_y = np.array(chy)

    f_x = np.sin(np.pi*axis)
    w = weights(x)
    p_x = polynomial(axis,x,y,w)
    cheby_w = weights(cheby_x)
    chebyp_x = polynomial(axis,cheby_x,cheby_y,cheby_w)

    plt.subplot(2,1,1)
    plt.title('Normal Interpolation')
    plt.plot(axis,p_x,color='r')
    plt.plot(axis,f_x,color='k')
    plt.subplot(2,1,2)
    plt.title('Chebyshev Points')
    plt.plot(axis,chebyp_x,color='r')
    plt.plot(axis,f_x,color='k')
    plt.show()
