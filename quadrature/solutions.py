# name this file solutions.py
"""Volume 2 Lab 12: Gaussian Quadrature
Derek Miller
Vol 2
Dec 7 2015

Do not chage the names of the functions defined below.
You may name additional functions whatever you want to.
"""

import numpy as np
import scipy.linalg as la
import scipy.integrate as spint
from scipy.stats import norm
from matplotlib import pyplot as plt
import scipy as sp

def shift_example():
    """Plot f(x) = x**2 on [1, 4] and the corresponding function
    ((b-a)/2)*g(x) on [-1, 1].
    """
    a = 1
    b = 4
    f = lambda x: x**2
    def g(x):
        return f(((b-a)/2.)*x + (b+a)/2.)
    x = np.linspace(a,b,1000)
    x_g = np.linspace(-1,1,1000)
    plt.subplot(1,2,1)
    plt.plot(x,f(x))
    plt.subplot(1,2,2)
    plt.plot(x_g,((b-a)/2.)*g(x))
    plt.show()


def estimate_integral(f, a, b, points, weights):
    """Estimate the value of the integral of the function 'f' over the
    domain [a, b], given the 'points' to use for sampling, and their
    corresponding 'weights'.

    Return the value of the integral.
    """
    g = lambda x: f((b-a)/2. * x + (b+a)/2.)
    return (b-a)/2. * np.inner(weights,g(points))


def jacobi(gamma,alpha,beta):
    n = len(alpha)
    a = -beta/alpha
    b = np.array([gamma[j+1]/(alpha[j]*alpha[j+1]) for j in range(n-1)])
    b = np.sqrt(b)
    J = sp.sparse.diags([b,a,b],[-1,0,1]).toarray()
    return J


def gaussian_quadrature(f, a, b, n):
    """Using the functions from the previous problems, integrate the function
    'f' over the domain [a,b] using 'n' points in the quadrature.
    """
    roots = np.arange(1,n+1)
    beta = np.zeros(n)
    alpha = np.array([(2*i-1)/float(i) for i in roots])
    gamma = np.array([(i-1)/float(i) for i in roots])
    J = jacobi(gamma,alpha,beta)
    eigvals, eigvecs = la.eig(J)
    weights = (eigvecs[0]**2)*2.
    points = np.real(eigvals)

    return estimate_integral(f, a, b, points, weights)


def normal_cdf(x):
    """Compute the CDF of the standard normal distribution at the point 'x'.
    That is, compute P(X <= x), where X is a normally distributed random
    variable.
    """
    N = norm()
    return spint.quad(N.pdf,-5,x)[0]

### TEST FUNCTION ###

def test():
    f = lambda x: x**2
    a = 1
    b = 4
    n = 5
    result = gaussian_quadrature(f,a,b,n)
    print result
