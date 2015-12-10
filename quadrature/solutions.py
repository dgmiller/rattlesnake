# name this file solutions.py
"""Volume 2 Lab 12: Gaussian Quadrature
Derek Miller
Vol 2
Dec 7 2015

Do not chage the names of the functions defined below.
You may name additional functions whatever you want to.
"""

import numpy as np
import scipy.integrate as spint
from scipy.stats import norm
from matplotlib import pyplot as plt

def shift_example(f, a, b):
    """Plot f(x) = x**2 on [1, 4] and the corresponding function
    ((b-a)/2)*g(x) on [-1, 1].
    """
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


def gaussian_quadrature(f, a, b, n):
    """Using the functions from the previous problems, integrate the function
    'f' over the domain [a,b] using 'n' points in the quadrature.
    """
    roots, weights = np.polynomial.legendre.leggauss(n)
    return np.inner(f(roots),weights)


def normal_cdf(x):
    """Compute the CDF of the standard normal distribution at the point 'x'.
    That is, compute P(X <= x), where X is a normally distributed random
    variable.
    """
    N = norm()
    return spint.quad(N.pdf,-5,1)[0]

