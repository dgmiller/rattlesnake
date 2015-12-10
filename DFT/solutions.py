# name this file solutions.py
"""Volume II Lab 9: Discrete Fourier Transform
Derek Miller
Volume 2
Today
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft
import scipy as sp

# Modify this class for problems 1, 2, 4, 5, and 6.
class Signal(object):
    def __init__(self, rate, samples):
        self.rate = rate
        self.samples = samples
        
    def __add__(self, other):
        if self.rate != other.rate:
            raise ValueError("Sample rates differ.")
        else:
            return Signal(self.rate, self.samples + other.samples)
    
       
    def plot(self):
        dft_samp = np.abs(DFT(self.samples))
        x_vals = np.arange(0,len(dft_samp),1)*1.
        x_vals /= len(self.samples)
        x_vals *= self.rate
        plt.subplot(211)
        plt.plot(self.samples)
        plt.subplot(212)
        plt.plot(x_vals,dft_samp)
        plt.show()
        
    def export(self,filename):
        sound = np.int16((self.samples / np.absolute(self.samples).max()) * 32767)
        wavfile.write(filename, self.rate, sound)


# Problem 3: Implement this function.

def wave_function(samplepts, freq):
    return np.sin(2*np.pi*samplepts*freq)

def generate_note(frequency=440., duration=5.):
    """Return an instance of the Signal class corresponding to the desired
        soundwave. Sample at a rate of 44100 samples per second.
    """
    rate = 44100
    stepsize = 1./rate
    sample_points = np.arange(0, duration, stepsize)
    samples = wave_function(sample_points, frequency) # the sine wave of the sample points
    my_sound = Signal(rate, samples) # creates a signal object
    return my_sound

# Problem 4: Implement this function.
def DFT(samples):
    return fft(samples)

def notes():
    A = 440.00
    B = 493.88
    C = 523.25
    D = 587.33
    E = 659.25
    F = 698.46
    G = 783.99
    
    return A,B,C,D,E,F,G

# Problem 6: Implement this function.

def progression(sound1, sound2):
    samples = np.hstack((sound1.samples, sound2.samples))
    return Signal(44100,samples)

def generate_chord(duration=3.):
    """Write a chord to a new file, 'chord1.wav'. Write a chord that changes
    over time to a new file, 'chord2.wav'.
    """
    A = generate_note(440.00,3.)
    C = generate_note(523.25,3.)
    E = generate_note(659.25,3.)
    G = generate_note(783.99,3.)

    a_minor = A + C + E
    a_minor.export('chord1.wav')

    c_major = C + E + G
    chord = progression(a_minor,c_major)
    chord.export('chord2.wav')

