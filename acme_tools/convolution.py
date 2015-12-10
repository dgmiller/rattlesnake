# An example of convolution using sound files

from scipy.io import wavfile
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

def clean_signal(outfile='prob1.wav'):
    """Cleans and plots the resulting sound wave and
    write the resulting sound to the specified outfile.
    """
    rate,data = wavfile.read(outfile)
    fsig = sp.fft(data,axis=0)
    for j in xrange(14990,50000):
        fsig[j] = 0
        fsig[-j] = 0
    newsig = sp.ifft(fsig)
    newsig = sp.real(newsig)
    newsig = sp.int16(newsig / sp.absolute(newsig).max() * 32767)
    plt.plot(newsig)
    plt.show()
    wavfile.write(outfile,rate,newsig)

def convolve(source='chopin.wav', pulse='balloon.wav', outfile='prob3.wav'):
    """Convolve the specified source file with the specified pulse file, then
    write the resulting sound wave to the specified outfile.
    """
    rate1,data = wavfile.read(source)
    data = np.hstack((data[:,0],np.zeros(863)))
    rate2,response = wavfile.read(pulse)
    response = np.hstack((response[:,0],np.zeros(135001)))
    mid_index = len(response // 2)
    conv_sig = np.fft.fft(data) * np.fft.fft(response)
    new_signal = np.real(np.fft.ifft(conv_sig))
    new_signal = np.int16(new_signal / sp.absolute(new_signal).max() * 32767)

    wavfile.write(outfile,rate1,new_signal)

def white_noise(outfile='prob4.wav'):
    """Generate some white noise, write it to the specified outfile,
    and plot the spectrum (DFT) of the signal.
    """
    samplerate = 22050
    noise = sp.int16(sp.random.randint(-32767,32767,samplerate*10))
    plt.plot(noise)
    plt.show()
    wavfile.write(outfile,samplerate,noise)
