# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:24:43 2015

@author: Georg
"""

from scitools.sound import *
import numpy as np

def solve_v1(duration, p):
    x = np.zeros(duration)
    index_set = range(int(duration))
    ## initial conditions    
    x[0] = 1.0
    x[1:p+1] = 0.0
    
    for n in index_set[p+1:]:
        x[n] = 0.5*(x[n-p] + x[n-p-1])
    return x

def solve_v2(duration, p):
    x = np.zeros(duration)
    index_set = range(int(duration))
    ## initial conditions
    x[0:p+1] = np.random.uniform(-1, 1, size=p+1)
    
    for n in index_set[p+1:]:
        x[n] = 0.5*(x[n-p] + x[n-p-1])
    return x

r  = 44100.0   ## sampling rate
f1 = 440.0     ## frequency of tone A
p1 = int(r/f1)
x1 = solve_v1(3*r, p1)
x1 *= max_amplitude

f2 = 392.0     ## frequency of tone G
p2 = int(r/f2)
x2 = solve_v2(2*r, p2)
x2 *= max_amplitude

data = np.concatenate((x1, x2), axis=1)
write(data, 'guitar_sound.wav')
play('guitar_sound.wav')