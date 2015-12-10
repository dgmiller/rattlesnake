# Problem 5.34 Jarvis

import numpy as np

def gauss_quad(h,n):
    roots, weights = np.polynomial.legendre.leggauss(n)
    return np.inner(h(roots),weights)


def f(x):
    return np.absolute(x)

def g(x):
    return np.cos(x)

### EVALUATION ###

N = [10,20,30,40,50,60,70,80,90,100]
ans = 2*np.sin(1.)
print "INTEGRATE |x| FROM -1 TO 1\n"
for n in N:
    print gauss_quad(f,n), 'vs. 1'

print "\n\n\nINTEGRATE cos(x) FROM -1 TO 1\n"
for m in N:
    print gauss_quad(g,m), 'vs. ', ans

