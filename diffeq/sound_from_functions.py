# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 23:23:14 2015

@author: Georg
"""
from scitools.sound import *
import matplotlib.pyplot as plt
import numpy as np

def oscillations(N):
    x = np.arange(N+1)
    x = np.exp(-4*x/float(N))*np.sin(8*np.pi*x/float(N))
    return x
 
def logistic(N):
    x = np.zeros(N+1)
    x[0] = 0.01
    q = 2
    for n in range(1, N+1):
        x[n] = x[n-1] + q*x[n-1]*(1 - x[n-1])
    return x

def make_sound(N, seqtype):
    filename = 'temp.wav'
    x = eval(seqtype)(N)
    
    # Convert x values to frequencies around 440 Hz
    freqs = 440 + x*220
    plt.plot(range(N+1), freqs, 'r-')
    plt.show()
    
    # Generate tones
    tones = []
    duration = 30.0/N
    for n in range(N+1):
        tones.append(max_amplitude*note(freqs[n], duration, 1))
    data = np.asarray(tones)
    write(data, filename)
    play(filename)

if __name__ == '__main__':
    try:
        seqtype = str(sys.argv[1])
        N       = int(sys.argv[2])
    except:
        raise IndexError('Usage: %s oscillations|logistic N' % sys.argv[0])
    make_sound(N, seqtype)