# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:55:02 2015

@author: Georg
"""

from scitools.sound import *
import numpy as np
import matplotlib.pyplot as plt

def bass_filter(x):
    y = np.zeros_like(x)
    index_set = range(len(x))
    y[0] = x[0]; y[-1] = x[-1]
    for n in index_set[1:-1]:
        y[n] = -0.25*(x[n-1] - 2*x[n] + x[n+1])
    return y

data1_original = Nothing_Else_Matters()
data1_filtered = bass_filter(data1_original)

fig1 = plt.figure()
ax1 = fig1.add_subplot(121)
ax1.plot(range(300), data1_original[:300], 'b-', label='original')
ax1.legend(loc=1)
ax2 = fig1.add_subplot(122)
ax2.plot(range(300), data1_filtered[:300], 'r-', label='filtered')
ax2.legend(loc=1)

data1 = np.concatenate((data1_original, data1_filtered), axis=1)
write(data1, 'nothing_else_matters.wav')
play('nothing_else_matters.wav')