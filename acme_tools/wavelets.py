# name this file solutions.py
"""Volume II Lab 11: Wavelets
Derek Miller
Volume 2
"""

import numpy as np
from scipy.signal import fftconvolve
from matplotlib import pyplot as plt

# Problem 1: Implement this AND the following function.

def dwt(X, L, H, n):
    """Compute the Discrete Wavelet Transform of X using filters L and H.

    Parameters:
        X (1D ndarray): The signal to be processed.
        L (1D ndarray): The low-pass filter.
        H (1D ndarray): The high-pass filter.
        n (int > 0): Controls the degree of transformation.
    
    Returns:
        a list of the wavelet decomposition arrays.
    """
    wavelets = []
    i = 0
    A = X
    while i < n:
        D = fftconvolve(A,H)[1::2]
        wavelets.append(D)
        A = fftconvolve(A,L)[1::2]
        i += 1
    wavelets.append(A)
    return wavelets[::-1]


def plot(X, L, H, n):
    """Plot the results of dwt with the given inputs.
	Your plot should be very similar to Figure 2.

    Parameters:
        X (1D ndarray): The signal to be processed.
        L (1D ndarray): The low-pass filter.
        H (1D ndarray): The high-pass filter.
        n (int > 0): Controls the degree of transformation.
    """
    wav_decomp = dwt(X,L,H,n)
    plt.subplot(n+2,1,1)
    plt.plot(X)
    for x in range(n+1):
        plt.subplot(n+2,1,x+2)
        plt.plot(wav_decomp[x])
    plt.show()


# Problem 2: Implement this function.
def idwt(coeffs, L, H):
    """
    Parameters:
        coeffs (list): a list of wavelet decomposition arrays.
        L (1D ndarray): The low-pass filter.
        H (1D ndarray): The high-pass filter.
    Returns:
        The reconstructed signal (as a 1D ndarray).
    """
    i = 1
    A = coeffs[0]
    while i < len(coeffs):
        D = coeffs[i]
        up_A = np.zeros(2*A.size)
        up_A[::2] = A
        up_D = np.zeros(2*D.size)
        up_D[::2] = D
        A = fftconvolve(up_A,L)[:-1] + fftconvolve(up_D,H)[:-1]
        i += 1
    X = A
    return X

