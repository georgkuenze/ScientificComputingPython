# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:14:31 2015

@author: Georg
"""

from scitools.sound import *
import numpy as np
import matplotlib.pyplot as plt

def filter_1(x):
    y = np.zeros_like(x)
    index_set = range(len(x))
    y[0] = x[0]; y[-1] = x[-1]
    for n in index_set[1:-1]:
        y[n] = (x[n-1] + x[n] + x[n+1])/3.0
    return y

def filter_2(x):
    y = np.zeros_like(x)
    index_set = range(len(x))
    y[0] = x[0]; y[-1] = x[-1]
    for n in index_set[1:-1]:
        y[n] = 0.25*(x[n-1] + 2*x[n] + x[n+1])
    return y
    
def filter_3(x):
    y = np.zeros_like(x)
    index_set = range(len(x))
    y[:2] = x[:2]; y[-2:] = x[-2:]
    for n in index_set[2:-2]:
        y[n] = 0.0625*(x[n-2] + 4*x[n-1] + 6*x[n] + 4*x[n+1] + x[n+2])
    return y

data_original = Nothing_Else_Matters()
data_filtered_1 = filter_1(data_original)
data_filtered_2 = filter_2(data_original)
data_filtered_3 = filter_3(data_original)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=False, sharey=False)
ax1.plot(range(300), data_original[:300], 'k-', label='original'); ax1.legend(loc=1)
ax2.plot(range(300), data_filtered_1[:300], 'b-', label='filter 1'); ax2.legend(loc=1)
ax3.plot(range(300), data_filtered_2[:300], 'r-', label='filter 2'); ax3.legend(loc=1)
ax4.plot(range(300), data_filtered_3[:300], 'g-', label='filter 3'); ax4.legend(loc=1)

data = np.concatenate((data_original, data_filtered_1, data_filtered_2, data_filtered_3))
write(data, 'nothing_else_matters_2.wav')
play('nothing_else_matters_2.wav')