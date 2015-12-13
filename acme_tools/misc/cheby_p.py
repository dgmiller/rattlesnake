#plot chebyshev interpolating polynomial

import numpy as np
from matplotlib import pyplot as plt
from numpy.polynomial.chebyshev import chebval

def cheb_interp(f,n):
    extrema = np.cos((np.pi * np.arange(2*n)) / n)
    samples = np.array([f(x) for x in extrema])
    coeffs = np.real(np.fft.fft(samples/n))
    coeffs[0] = coeffs[0]/2
    coeffs[n] = coeffs[n]/2

    return coeffs[:n+1]

a = [0,1,-1,0,-1,1]
print np.fft.fft(a).real

def f(x):
    if x < 0:
        return 1+x
    else:
        return x

def plot_result():
    n = [2**x for x in range(1,8)]
    for j in n:
        x = np.linspace(-1,1,num=100,endpoint=True)
        y = np.array([f(i) for i in x])
        chebpoly = chebval(x,cheb_interp(f,j))
        plt.plot(x,y)
        plt.plot(x,chebpoly)
    plt.show()

plot_result()
